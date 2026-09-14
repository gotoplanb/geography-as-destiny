"""Write a single-page CMYK PDF for print submission, dependency-free.

One image XObject in /DeviceCMYK fills a page whose MediaBox is the exact
KDP wrap size (bleed included); TrimBox marks the trim. The press ICC profile
is embedded as an OutputIntent so the PDF declares which CMYK it means.
Compression: Flate (lossless) when it fits under KDP's 40 MB cover limit,
else JPEG (DCTDecode) at high quality.
"""
from __future__ import annotations

import io
import zlib
from datetime import datetime, timezone
from pathlib import Path

from PIL import Image

KDP_MAX_BYTES = 40 * 1024 * 1024
FLATE_BUDGET = 36 * 1024 * 1024  # leave headroom under the 40 MB limit


def _pdf_string(s: str) -> bytes:
    s = s.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")
    return b"(" + s.encode("latin-1", "replace") + b")"


def write_cmyk_pdf(img: Image.Image, dest: Path, *, page_w_in: float, page_h_in: float,
                   bleed_in: float, icc_path: Path, title: str, author: str,
                   prefer: str = "flate") -> dict:
    assert img.mode == "CMYK", "image must already be CMYK"
    w_px, h_px = img.size
    W, H = page_w_in * 72.0, page_h_in * 72.0
    b = bleed_in * 72.0

    raw = img.tobytes()
    filt, data, decode = None, None, b""
    if prefer == "flate":
        flate = zlib.compress(raw, 9)
        if len(flate) <= FLATE_BUDGET:
            filt, data = b"/FlateDecode", flate
    if filt is None:
        buf = io.BytesIO()
        # Pillow writes CMYK JPEG "Adobe style" (APP14, inverted samples);
        # /Decode [1 0 x4] tells the PDF consumer to un-invert, exactly as
        # Pillow's own PDF plugin does.
        img.save(buf, "JPEG", quality=95, subsampling=0, optimize=True)
        filt, data = b"/DCTDecode", buf.getvalue()
        decode = b" /Decode [1 0 1 0 1 0 1 0]"

    icc = icc_path.read_bytes()
    icc_z = zlib.compress(icc, 9)
    content = f"q {W:.4f} 0 0 {H:.4f} 0 0 cm /Im0 Do Q".encode()
    now = datetime.now(timezone.utc).strftime("D:%Y%m%d%H%M%SZ")
    desc = "U.S. Web Coated (SWOP) v2"

    objs: list[bytes] = []
    def add(body: bytes) -> int:
        objs.append(body); return len(objs)

    icc_obj = add(b"<< /N 4 /Alternate /DeviceCMYK /Filter /FlateDecode /Length %d >>\nstream\n" % len(icc_z)
                  + icc_z + b"\nendstream")
    intent_obj = add(b"<< /Type /OutputIntent /S /GTS_PDFX /OutputConditionIdentifier (CGATS TR 001) "
                     b"/RegistryName (http://www.color.org) /Info " + _pdf_string(desc) +
                     b" /DestOutputProfile %d 0 R >>" % icc_obj)
    img_obj = add(b"<< /Type /XObject /Subtype /Image /Width %d /Height %d /ColorSpace /DeviceCMYK "
                  b"/BitsPerComponent 8 /Filter %s%s /Length %d >>\nstream\n" % (w_px, h_px, filt, decode, len(data))
                  + data + b"\nendstream")
    content_obj = add(b"<< /Length %d >>\nstream\n" % len(content) + content + b"\nendstream")
    pages_obj_num = len(objs) + 2
    page_obj = add((f"<< /Type /Page /Parent {pages_obj_num} 0 R "
                    f"/MediaBox [0 0 {W:.4f} {H:.4f}] /BleedBox [0 0 {W:.4f} {H:.4f}] "
                    f"/TrimBox [{b:.4f} {b:.4f} {W - b:.4f} {H - b:.4f}] "
                    f"/Resources << /XObject << /Im0 {img_obj} 0 R >> /ProcSet [/PDF /ImageC] >> "
                    f"/Contents {content_obj} 0 R >>").encode())
    pages_obj = add(b"<< /Type /Pages /Kids [%d 0 R] /Count 1 >>" % page_obj)
    assert pages_obj == pages_obj_num
    catalog_obj = add(b"<< /Type /Catalog /Pages %d 0 R /OutputIntents [%d 0 R] >>" % (pages_obj, intent_obj))
    info_obj = add(b"<< /Title " + _pdf_string(title) + b" /Author " + _pdf_string(author) +
                   b" /Creator (geography-as-destiny cover/build_cover.py) /Producer (cover/pdfwriter.py) "
                   b"/CreationDate " + _pdf_string(now) + b" /Trapped /False >>")

    out = bytearray(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
    offsets = []
    for i, body in enumerate(objs, 1):
        offsets.append(len(out))
        out += b"%d 0 obj\n" % i + body + b"\nendobj\n"
    xref = len(out)
    out += b"xref\n0 %d\n0000000000 65535 f \n" % (len(objs) + 1)
    for off in offsets:
        out += b"%010d 00000 n \n" % off
    out += (b"trailer\n<< /Size %d /Root %d 0 R /Info %d 0 R >>\nstartxref\n%d\n%%%%EOF\n"
            % (len(objs) + 1, catalog_obj, info_obj, xref))
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(out)
    return {"bytes": len(out), "filter": filt.decode(), "width_px": w_px, "height_px": h_px,
            "page_in": [page_w_in, page_h_in], "dpi": [w_px / page_w_in, h_px / page_h_in]}
