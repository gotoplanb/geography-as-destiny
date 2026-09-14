"""Build the ebook cover JPEG that ships inside the epub.

Amazon bills KDP delivery at $0.15/MB, so every megabyte in the epub comes
straight out of the 70% royalty. A 3 MB PNG cover is the single largest file
in the book and buys nothing a JPEG cannot carry.

Source of truth is the print wrap (build/cover/06-wrap-final-rgb.png), whose
front panel is 300 DPI -- far better than the 1024x1536 cover.png. The panel
is cropped inside the bleed using the geometry build_cover.py recorded, then
downsampled to EBOOK_WIDTH. The art is 1:1.5; Kindle prefers 1:1.6 but accepts
1.5, and padding or stretching to hit 1.6 would alter the design, so the
native ratio is preserved.

The wrap is a build artifact and is gitignored, so on a clean checkout this
falls back to cover.png. Output is tracked -- it must exist for build-epub.sh
whether or not the print pipeline has been run here.

Usage: python cover/build_ebook_cover.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
WRAP = ROOT / "build" / "cover" / "06-wrap-final-rgb.png"
REPORT = ROOT / "build" / "cover" / "build-report.json"
FALLBACK = ROOT / "cover.png"
DEST = ROOT / "cover-ebook.jpg"

EBOOK_WIDTH = 1600   # Kindle's recommended long edge; min shortest side is 1000
JPEG_QUALITY = 88


def _front_panel() -> tuple[Image.Image, str]:
    """Crop the trimmed front panel out of the print wrap, else use cover.png."""
    if not (WRAP.exists() and REPORT.exists()):
        return Image.open(FALLBACK).convert("RGB"), f"{FALLBACK.name} (wrap not built)"

    geom = json.loads(REPORT.read_text())["geometry"]
    wrap = Image.open(WRAP).convert("RGB")
    canvas_w, canvas_h = geom["canvas_px"]
    if wrap.size != (canvas_w, canvas_h):
        raise SystemExit(f"wrap is {wrap.size}, build-report says {(canvas_w, canvas_h)}")

    # bleed trims every outer edge; front_x0 is the spine-side boundary, which
    # is an interior cut and takes no bleed.
    dpi = canvas_w / geom["page_in"][0]
    bleed = round(json.loads((ROOT / "cover" / "kdp.json").read_text())["bleed_in"] * dpi)
    box = (geom["front_x0"], bleed, canvas_w - bleed, canvas_h - bleed)
    return wrap.crop(box), f"{WRAP.name} front panel {box}"


def main() -> int:
    img, source = _front_panel()
    w, h = img.size
    img = img.resize((EBOOK_WIDTH, round(h * EBOOK_WIDTH / w)), Image.LANCZOS)
    img.save(DEST, "JPEG", quality=JPEG_QUALITY, optimize=True, progressive=True)

    kb = DEST.stat().st_size / 1024
    print(f"source: {source}")
    print(f"wrote:  {DEST.relative_to(ROOT)}  {img.size[0]}x{img.size[1]}  {kb:.0f} KB")
    print(f"        delivery cost at $0.15/MB: ${kb / 1024 * 0.15:.2f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
