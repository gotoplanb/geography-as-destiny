"""Minimal client for Conduct's media jobs (upload -> job -> poll -> fetch).

Conduct knows nothing about covers; it only upscales and outpaints. This
module keeps that boundary: it speaks the jobs API and records, for every
step, the request we sent and the *effective* parameters Conduct echoes
back (seed, model), so any artifact can be regenerated exactly.

Credentials: CONDUCT_API_URL / CONDUCT_API_KEY in the environment, else read
from ~/conduct-private/book-covers-client.env (never committed here).
"""
from __future__ import annotations

import hashlib
import json
import os
import shutil
import time
from pathlib import Path

import requests

ENV_FILE = Path.home() / "conduct-private" / "book-covers-client.env"


def _load_env() -> tuple[str, str]:
    url, key = os.environ.get("CONDUCT_API_URL"), os.environ.get("CONDUCT_API_KEY")
    if not (url and key) and ENV_FILE.exists():
        for line in ENV_FILE.read_text().splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            if k == "CONDUCT_API_URL" and not url:
                url = v.strip()
            elif k == "CONDUCT_API_KEY" and not key:
                key = v.strip()
    if not (url and key):
        raise SystemExit(
            "Conduct credentials missing: set CONDUCT_API_URL and CONDUCT_API_KEY "
            f"or create {ENV_FILE}"
        )
    return url.rstrip("/"), key


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


class Conduct:
    def __init__(self, record_path: Path):
        self.base, key = _load_env()
        self.s = requests.Session()
        self.s.headers["Authorization"] = f"Bearer {key}"
        self.record_path = record_path
        self.records: dict = {}
        if record_path.exists():
            self.records = json.loads(record_path.read_text())

    # -- raw API -----------------------------------------------------------
    def upload(self, path: Path) -> dict:
        with open(path, "rb") as f:
            r = self.s.post(f"{self.base}/uploads", files={"file": (path.name, f)}, timeout=300)
        r.raise_for_status()
        return r.json()

    def submit(self, task_type: str, inputs: dict, prompt: str = "", metadata: dict | None = None) -> str:
        body = {"task_type": task_type, "prompt": prompt, "async": True,
                "inputs": inputs, "metadata": metadata or {}}
        r = self.s.post(f"{self.base}/jobs", json=body, timeout=60)
        r.raise_for_status()
        return r.json()["job_id"]

    def job(self, job_id: str) -> dict:
        r = self.s.get(f"{self.base}/jobs/{job_id}", timeout=60)
        r.raise_for_status()
        return r.json()

    def wait(self, job_id: str, timeout_s: float = 3600, poll_s: float = 3.0) -> dict:
        t0 = time.time()
        while True:
            j = self.job(job_id)
            if j["status"] == "complete":
                return j
            if j["status"] in ("failed", "cancelled"):
                raise RuntimeError(f"Conduct job {job_id} {j['status']}: {j.get('error')}")
            if time.time() - t0 > timeout_s:
                raise TimeoutError(f"Conduct job {job_id} still {j['status']} after {timeout_s}s")
            time.sleep(poll_s)

    def fetch(self, media_url: str, dest: Path) -> Path:
        r = self.s.get(f"{self.base}{media_url}", timeout=600, stream=True)
        r.raise_for_status()
        dest.parent.mkdir(parents=True, exist_ok=True)
        with open(dest, "wb") as f:
            for chunk in r.iter_content(1 << 20):
                f.write(chunk)
        return dest

    # -- recorded, idempotent steps ---------------------------------------
    def _save(self) -> None:
        self.record_path.parent.mkdir(parents=True, exist_ok=True)
        self.record_path.write_text(json.dumps(self.records, indent=2, sort_keys=True) + "\n")

    def upload_step(self, name: str, path: Path) -> str:
        """Upload once per file content; returns Conduct's source_url."""
        digest = _sha256(path)
        rec = self.records.get(name)
        if rec and rec.get("sha256") == digest and rec.get("source_url"):
            return rec["source_url"]
        out = self.upload(path)
        self.records[name] = {"kind": "upload", "file": str(path), "sha256": digest,
                              "upload_id": out["upload_id"], "source_url": out["source_url"],
                              "bytes": out["bytes"]}
        self._save()
        return out["source_url"]

    def job_step(self, name: str, task_type: str, inputs: dict, dest: Path,
                 prompt: str = "", metadata: dict | None = None, force: bool = False) -> tuple[Path, dict]:
        """Run a media job unless an identical request already produced `dest`.

        Returns (dest, effective_params). Identity = task_type + inputs + prompt,
        so changing a seed or an extension amount re-runs; re-running the build
        with nothing changed costs no GPU time.
        """
        request = {"task_type": task_type, "inputs": inputs, "prompt": prompt}
        req_hash = hashlib.sha256(json.dumps(request, sort_keys=True).encode()).hexdigest()
        if not force:
            # Reuse any recorded job (under this or another step name) whose
            # request is byte-identical and whose output is still on disk.
            for rec in [self.records.get(name)] + list(self.records.values()):
                if not rec or rec.get("kind") != "job" or rec.get("request_sha256") != req_hash:
                    continue
                src = Path(rec["output"])
                if src.exists() and rec.get("output_sha256") == _sha256(src):
                    if src.resolve() != dest.resolve():
                        dest.parent.mkdir(parents=True, exist_ok=True)
                        shutil.copyfile(src, dest)
                    self.records[name] = dict(rec, output=str(dest))
                    self._save()
                    return dest, rec["effective_params"]
        job_id = self.submit(task_type, inputs, prompt, metadata)
        print(f"  conduct: {name} -> job {job_id} ({task_type}) ...", flush=True)
        j = self.wait(job_id)
        self.fetch(j["media_url"], dest)
        media = j.get("metadata", {}).get("media", {})
        eff = media.get("extra", {}).get("params", {})
        self.records[name] = {
            "kind": "job", "job_id": job_id, "task_type": task_type, "request": request,
            "request_sha256": req_hash, "media_url": j["media_url"], "output": str(dest),
            "output_sha256": _sha256(dest), "effective_params": eff,
            "workflow_template": media.get("extra", {}).get("workflow_template"),
            "provider": media.get("provider"), "latency_ms": j.get("latency_ms"),
            "completed_at": j.get("completed_at"),
        }
        self._save()
        print(f"  conduct: {name} complete in {j.get('latency_ms')} ms; params {eff}", flush=True)
        return dest, eff
