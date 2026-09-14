#!/usr/bin/env python3
"""Build the KDP full-wrap paperback cover (back + spine + front) as a CMYK PDF.

Pipeline (see cover/README.md):
  1. geometry     -- exact pixel canvas at 300 DPI from cover/kdp.json (KDP
                     calculator numbers; the spine is cross-checked, not estimated)
  2. conduct      -- upscale the front art to trim size; outpaint the back +
                     spine at a half-scale working canvas (ComfyUI cannot
                     VAE-encode the full 3993x2776 wrap on MPS); upscale the fill
  3. composite    -- fill + spine band under everything, untouched front art on top
                     (soft 24 px ramp at the fold), mirrored bleed on the front's
                     three outer edges, spine + back text in EB Garamond
  4. proof        -- 1/3-scale JPEG with trim / safe-zone / spine / barcode guides
  5. print        -- sRGB -> U.S. Web Coated (SWOP) v2 via littleCMS, single-page
                     PDF sized exactly to the KDP wrap with TrimBox + OutputIntent

Every Conduct step is idempotent and recorded in build/cover/jobs.json with the
effective parameters (seed, model) Conduct echoes back.

Usage:  .venv/bin/python cover/build_cover.py [--no-conduct] [--seed N] [--force]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

import numpy as np
from PIL import Image, ImageCms, ImageDraw, ImageFilter, ImageFont

sys.path.insert(0, str(Path(__file__).resolve().parent))
from conduct import Conduct  # noqa: E402
from pdfwriter import write_cmyk_pdf  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "build" / "cover"
CFG = ROOT / "cover" / "kdp.json"
COPY = ROOT / "cover" / "back-cover.md"

# KDP's published paper thickness (inches per page) -- used only to sanity-check
# the calculator value in kdp.json, never to derive the spine.
KDP_IN_PER_PAGE = {"white": 0.002252, "cream": 0.0025, "color-standard": 0.002252, "color-premium": 0.002347}
SPINE_TOLERANCE_IN = 0.002  # the calculator rounds to 3 decimals

TITLE = "Geography as Destiny"
AUTHOR = "Dave Stanton"
INK = (44, 39, 33)  # sampled from the front title

FONT_DIRS = [Path.home() / "Library/Fonts", Path("/Library/Fonts"), Path("/System/Library/Fonts/Supplemental")]
FONT_REGULAR = ["EBGaramond12-Regular.otf", "EBGaramond08-Regular.otf", "Hoefler Text.ttc", "Georgia.ttf"]
FONT_ITALIC = ["EBGaramond12-Italic.otf", "EBGaramond08-Italic.otf", "Hoefler Text.ttc", "Georgia Italic.ttf"]

# Working canvas for the outpaint (multiples of 8 so ComfyUI's VAE does not crop).
WORK_FRONT = (896, 1344)
WORK_TB = 16
FOLD_RAMP_PX = 24


# ---------------------------------------------------------------- geometry --
@dataclass(frozen=True)
class Geometry:
    dpi: int
    bleed_in: float
    trim_w_in: float
    trim_h_in: float
    spine_in: float

    @staticmethod
    def from_config(cfg: dict) -> "Geometry":
        paper = cfg["paper"]
        expected = cfg["page_count"] * KDP_IN_PER_PAGE[paper]
        if abs(expected - cfg["spine_in"]) > SPINE_TOLERANCE_IN:
            raise SystemExit(
                f"spine_in={cfg['spine_in']} disagrees with KDP's {paper} thickness for "
                f"{cfg['page_count']} pages ({expected:.4f} in). Re-run the KDP cover calculator "
                "and update cover/kdp.json (page_count and spine_in together)."
            )
        return Geometry(cfg["dpi"], cfg["bleed_in"], cfg["trim_width_in"], cfg["trim_height_in"], cfg["spine_in"])

    def px(self, inches: float) -> int:
        # round half up (Python's round() is banker's: 316.5 -> 316, 37.5 -> 38)
        return int(np.floor(inches * self.dpi + 0.5))

    @property
    def bleed(self): return self.px(self.bleed_in)
    @property
    def trim_w(self): return self.px(self.trim_w_in)
    @property
    def trim_h(self): return self.px(self.trim_h_in)
    @property
    def spine_w(self): return self.px(self.spine_in)
    @property
    def canvas_w(self): return 2 * self.bleed + 2 * self.trim_w + self.spine_w
    @property
    def canvas_h(self): return self.trim_h + 2 * self.bleed
    @property
    def spine_x0(self): return self.bleed + self.trim_w
    @property
    def front_x0(self): return self.spine_x0 + self.spine_w
    @property
    def page_w_in(self): return 2 * self.bleed_in + 2 * self.trim_w_in + self.spine_in
    @property
    def page_h_in(self): return self.trim_h_in + 2 * self.bleed_in
    @property
    def safe(self): return self.px(0.125)          # inside the trim line
    @property
    def spine_clear(self): return self.px(0.0625)  # from each spine edge
    @property
    def barcode_box(self):
        """KDP's own barcode: 2 x 1.2 in, 0.25 in from the back cover's trim edges."""
        m, w, h = self.px(0.25), self.px(2.0), self.px(1.2)
        x1, y1 = self.spine_x0 - m, self.canvas_h - self.bleed - m
        return (x1 - w, y1 - h, x1, y1)

    def working_plan(self) -> dict:
        """Half-scale outpaint plan and the exact upscale that maps it back."""
        s = WORK_FRONT[0] / self.trim_w
        left = int(round(self.front_x0 * s / 8) * 8)
        work_w, work_h = WORK_FRONT[0] + left, WORK_FRONT[1] + 2 * WORK_TB
        scale_x = self.front_x0 / left  # so the fill's front edge lands exactly on front_x0
        return {"left": left, "top": WORK_TB, "bottom": WORK_TB, "work_size": (work_w, work_h),
                "upscale_size": (round(work_w * scale_x), self.canvas_h)}


# ------------------------------------------------------------------- fonts --
def find_font(names: list[str], size: int) -> ImageFont.FreeTypeFont:
    for n in names:
        for d in FONT_DIRS:
            p = d / n
            if p.exists():
                return ImageFont.truetype(str(p), size)
    raise SystemExit(f"no font found among {names}; brew install --cask font-eb-garamond")


# ------------------------------------------------------------- text layout --
def parse_copy(path: Path) -> dict[str, list[str]]:
    text = re.sub(r"<!--.*?-->", "", path.read_text(), flags=re.S)
    sections: dict[str, list[str]] = {}
    key = None
    for block in re.split(r"\n\s*\n", text.strip()):
        block = block.strip()
        if not block:
            continue
        if block.startswith("# "):
            key = block[2:].strip().lower(); sections[key] = []
        elif key:
            sections[key].append(" ".join(block.split()).replace(" -- ", " — ").replace("--", "—"))
    return sections


def runs(paragraph: str) -> list[tuple[str, bool]]:
    """Split '*italic*' markup into (word, italic) tokens."""
    out, italic = [], False
    for piece in re.split(r"(\*)", paragraph):
        if piece == "*":
            italic = not italic
        elif piece:
            out += [(w, italic) for w in piece.split(" ") if w]
    return out


def wrap(tokens, fonts, max_w, draw) -> list[list[tuple[str, bool]]]:
    lines, line, width = [], [], 0
    space = draw.textlength(" ", font=fonts[False])
    for word, it in tokens:
        w = draw.textlength(word, font=fonts[it])
        if line and width + space + w > max_w:
            lines.append(line); line, width = [], 0
        width += (space if line else 0) + w
        line.append((word, it))
    if line:
        lines.append(line)
    return lines


def draw_paragraphs(draw, paragraphs, x, y, max_w, size, leading=1.4, para_gap=0.6, fill=INK) -> int:
    fonts = {False: find_font(FONT_REGULAR, size), True: find_font(FONT_ITALIC, size)}
    lh = round(size * leading)
    space = draw.textlength(" ", font=fonts[False])
    for p in paragraphs:
        for line in wrap(runs(p), fonts, max_w, draw):
            cx = x
            for word, it in line:
                draw.text((cx, y), word, font=fonts[it], fill=fill)
                cx += draw.textlength(word, font=fonts[it]) + space
            y += lh
        y += round(lh * para_gap)
    return y


def paragraphs_height(paragraphs, max_w, size, leading=1.4, para_gap=0.6) -> int:
    scratch = ImageDraw.Draw(Image.new("RGB", (8, 8)))
    return draw_paragraphs(scratch, paragraphs, 0, 0, max_w, size, leading, para_gap) - round(size * leading * para_gap)


def spine_label(text: str, size: int) -> Image.Image:
    """Text rendered horizontally then rotated to read top-to-bottom (US convention)."""
    font = find_font(FONT_REGULAR, size)
    l, t, r, b = font.getbbox(text)
    im = Image.new("RGBA", (r - l + 4, b - t + 4), (0, 0, 0, 0))
    ImageDraw.Draw(im).text((2 - l, 2 - t), text, font=font, fill=INK + (255,))
    return im.transpose(Image.Transpose.ROTATE_270)


# --------------------------------------------------------------- composite --
def mirror_extend(art: Image.Image, right: int, top: int, bottom: int) -> Image.Image:
    """Bleed for the front's outer edges: mirrored pixels are continuous at the
    trim line and get cut off, so nothing is invented there."""
    w, h = art.size
    out = Image.new("RGB", (w + right, h + top + bottom))
    out.paste(art, (0, top))
    out.paste(art.crop((w - right, 0, w, h)).transpose(Image.Transpose.FLIP_LEFT_RIGHT), (w, top))
    band = out.crop((0, top, w + right, top + top)).transpose(Image.Transpose.FLIP_TOP_BOTTOM)
    out.paste(band, (0, 0))
    band = out.crop((0, top + h - bottom, w + right, top + h)).transpose(Image.Transpose.FLIP_TOP_BOTTOM)
    out.paste(band, (0, top + h))
    return out


def fill_canvas(g: Geometry, fill: Image.Image) -> Image.Image:
    canvas = Image.new("RGB", (g.canvas_w, g.canvas_h))
    canvas.paste(fill.crop((0, 0, min(fill.width, g.canvas_w), g.canvas_h)), (0, 0))
    return canvas


def paste_front(g: Geometry, canvas: Image.Image, art: Image.Image) -> Image.Image:
    """Untouched front art (plus mirrored bleed) over everything, with a short
    ramp at the fold so the seam into the generated fill is soft."""
    assert art.size == (g.trim_w, g.trim_h), art.size
    block = mirror_extend(art, g.bleed, g.bleed, g.bleed)  # (trim_w + bleed) x canvas_h
    ramp = np.ones((block.height, block.width), dtype=np.float32)
    ramp[:, :FOLD_RAMP_PX] = np.linspace(0.0, 1.0, FOLD_RAMP_PX, endpoint=False)
    mask = Image.fromarray((ramp * 255).astype(np.uint8), "L")
    canvas.paste(block, (g.front_x0, 0), mask)
    return canvas


def soft_panel(canvas: Image.Image, box, color, opacity: float, feather: int) -> None:
    """Optional parchment wash behind the blurb when the fill is too busy."""
    if opacity <= 0:
        return
    x0, y0, x1, y1 = box
    mask = Image.new("L", canvas.size, 0)
    ImageDraw.Draw(mask).rectangle((x0, y0, x1, y1), fill=round(255 * opacity))
    mask = mask.filter(ImageFilter.GaussianBlur(feather))
    canvas.paste(Image.new("RGB", canvas.size, tuple(color)), (0, 0), mask)


def plan_back(g: Geometry, copy: dict, cfg: dict) -> dict:
    """Where the back-cover blocks go (shared by the washes and the type)."""
    margin = g.px(cfg.get("back_margin_in", 0.5))
    x0, x1 = g.bleed + margin, g.spine_x0 - margin
    body_px, small_px = cfg.get("back_body_px", 50), cfg.get("back_small_px", 40)
    y = g.bleed + g.px(cfg.get("back_top_in", 0.8))
    blurb_h = paragraphs_height(copy["blurb"], x1 - x0, body_px)
    bx0, by0, bx1, by1 = g.barcode_box
    col_w = bx0 - g.px(0.3) - x0
    bio, url = copy.get("bio", []), copy.get("url", [])
    bio_h = paragraphs_height(bio, col_w, small_px, leading=1.35) if bio else 0
    url_h = paragraphs_height(url, col_w, small_px, leading=1.35) if url else 0
    gap = round(small_px * 0.5)
    yb = max(by1 - url_h - (gap if bio else 0) - bio_h, y + blurb_h + g.px(0.5))
    return {"body_px": body_px, "small_px": small_px, "gap": gap, "col_w": col_w,
            "blurb": (x0, y, x1, y + blurb_h), "bio": (x0, yb, x0 + col_w, by1)}


def spine_band(g: Geometry, canvas: Image.Image, cfg: dict) -> None:
    """Parchment band the full height of the spine (small overhang past each
    fold) so spine type stays legible over the painted fill. Drawn before the
    front art is pasted, so the art itself is never altered."""
    band = cfg.get("spine_band", {})
    if band.get("opacity", 0) > 0:
        over = g.px(band.get("overhang_in", 0.03))
        soft_panel(canvas, (g.spine_x0 - over, -200, g.front_x0 + over, g.canvas_h + 200),
                   band.get("color", [214, 186, 146]), band["opacity"], band.get("feather", 12))


def back_panels(g: Geometry, canvas: Image.Image, plan: dict, cfg: dict) -> None:
    """Soft parchment panels behind the blurb and the bio block."""
    panel = cfg.get("back_text_panel", {})
    if panel.get("opacity", 0) > 0:
        pad = g.px(0.3)
        for key in ("blurb", "bio"):
            x0, y0, x1, y1 = plan[key]
            soft_panel(canvas, (x0 - pad, y0 - pad, x1 + pad, y1 + pad),
                       panel.get("color", [214, 186, 146]), panel["opacity"], panel.get("feather", 60))


def add_text(g: Geometry, canvas: Image.Image, copy: dict, plan: dict, cfg: dict) -> dict:
    """Draw spine and back text. Returns the boxes used (for tests/proof)."""
    boxes = {}
    d = ImageDraw.Draw(canvas)

    # --- spine: title reading downward from the top, author ending at the bottom
    inset = g.px(0.75)
    title = spine_label(TITLE, cfg.get("spine_title_px", 118))
    author = spine_label(AUTHOR, cfg.get("spine_author_px", 88))
    for lab in (title, author):
        assert lab.width <= g.spine_w - 2 * g.spine_clear, "spine text too large for spine width"
    assert title.height + author.height + g.px(0.5) <= g.canvas_h - 2 * (g.bleed + inset), "spine text too long"
    tx = g.spine_x0 + (g.spine_w - title.width) // 2
    ty = g.bleed + inset
    canvas.paste(title, (tx, ty), title)
    boxes["spine_title"] = (tx, ty, tx + title.width, ty + title.height)
    ax = g.spine_x0 + (g.spine_w - author.width) // 2
    ay = g.canvas_h - g.bleed - inset - author.height
    canvas.paste(author, (ax, ay), author)
    boxes["spine_author"] = (ax, ay, ax + author.width, ay + author.height)

    # --- back: blurb top-left, bio + url bottom-left beside the barcode zone
    x0, y, x1, _ = plan["blurb"]
    y_end = draw_paragraphs(d, copy["blurb"], x0, y, x1 - x0, plan["body_px"])
    boxes["blurb"] = (x0, y, x1, y_end)
    x0, yb, xb1, by1 = plan["bio"]
    small_px, col_w = plan["small_px"], plan["col_w"]
    bio, url = copy.get("bio", []), copy.get("url", [])
    if bio:
        yb = draw_paragraphs(d, bio, x0, yb, col_w, small_px, leading=1.35) - round(small_px * 1.35 * 0.6) + plan["gap"]
    if url:
        yb = draw_paragraphs(d, url, x0, yb, col_w, small_px, leading=1.35)
    boxes["bio"] = (x0, plan["bio"][1], xb1, min(yb, by1))
    return boxes


# ------------------------------------------------------------------- proof --
def write_proof(g: Geometry, canvas: Image.Image, dest: Path, scale: float = 1 / 3) -> None:
    im = canvas.resize((round(g.canvas_w * scale), round(g.canvas_h * scale)), Image.LANCZOS).convert("RGB")
    d = ImageDraw.Draw(im, "RGBA")
    s = lambda v: round(v * scale)
    b, sf = g.bleed, g.bleed + g.safe
    W, H = g.canvas_w, g.canvas_h
    d.rectangle((s(b), s(b), s(W - b) - 1, s(H - b) - 1), outline=(220, 0, 0, 255), width=1)       # trim
    d.rectangle((s(sf), s(sf), s(W - sf) - 1, s(H - sf) - 1), outline=(0, 90, 220, 180), width=1)  # safe
    for x in (g.spine_x0, g.front_x0):
        d.line((s(x), 0, s(x), im.height), fill=(0, 150, 0, 255), width=1)
    for x in (g.spine_x0 + g.spine_clear, g.front_x0 - g.spine_clear):
        d.line((s(x), 0, s(x), im.height), fill=(0, 150, 0, 120), width=1)
    bx0, by0, bx1, by1 = g.barcode_box
    d.rectangle((s(bx0), s(by0), s(bx1), s(by1)), fill=(255, 255, 255, 200), outline=(200, 0, 200, 255))
    font = find_font(FONT_REGULAR, 22)
    d.text((s(bx0) + 8, s(by0) + 8), "KDP barcode\n2 x 1.2 in", font=font, fill=(120, 0, 120, 255))
    d.text((8, 8), f"PROOF  {g.page_w_in:.3f} x {g.page_h_in:.2f} in  |  red=trim  blue=safe zone  "
                   f"green=spine ({g.spine_in} in)  |  {g.canvas_w}x{g.canvas_h} px @ {g.dpi} dpi",
           font=font, fill=(200, 0, 0, 255))
    im.save(dest, "JPEG", quality=88, optimize=True)


# ------------------------------------------------------------------- print --
def to_cmyk(rgb: Image.Image, icc_path: Path, src_icc: bytes | None) -> Image.Image:
    src = ImageCms.getOpenProfile(__import__("io").BytesIO(src_icc)) if src_icc else ImageCms.createProfile("sRGB")
    dst = ImageCms.getOpenProfile(str(icc_path))
    xf = ImageCms.buildTransform(src, dst, "RGB", "CMYK", renderingIntent=ImageCms.Intent.RELATIVE_COLORIMETRIC,
                                 flags=ImageCms.Flags.BLACKPOINTCOMPENSATION)
    return ImageCms.applyTransform(rgb, xf)


# -------------------------------------------------------------------- main --
def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--front", default=str(ROOT / "cover.png"), help="source front-cover art")
    ap.add_argument("--no-conduct", action="store_true", help="reuse build/cover intermediates; never call Conduct")
    ap.add_argument("--seed", type=int, help="override outpaint seed from kdp.json")
    ap.add_argument("--force", action="store_true", help="re-run Conduct steps even if recorded")
    args = ap.parse_args()

    cfg = json.loads(CFG.read_text())
    g = Geometry.from_config(cfg)
    plan = g.working_plan()
    OUT.mkdir(parents=True, exist_ok=True)
    print(f"canvas {g.canvas_w}x{g.canvas_h} px = {g.page_w_in:.3f} x {g.page_h_in:.2f} in @ {g.dpi} dpi; "
          f"spine {g.spine_in} in = {g.spine_w} px; front at x={g.front_x0}")

    icc_path = ROOT / cfg["cmyk_profile"]
    if not icc_path.exists():
        raise SystemExit(f"missing press profile {icc_path} -- see cover/README.md (Adobe ICC bundle)")

    front_src = Path(args.front)
    front_up = OUT / "01-front-upscaled.png"
    work_png = OUT / "02-front-working.png"
    outpaint = OUT / "03-outpaint-working.png"
    fill_up = OUT / "04-fill-upscaled.png"
    op = dict(cfg["outpaint"])
    if args.seed is not None:
        op["seed"] = args.seed

    if not args.no_conduct:
        c = Conduct(OUT / "jobs.json")
        meta = {"project": "geography-as-destiny", "book": TITLE}
        src_url = c.upload_step("upload-front", front_src)
        c.job_step("front-upscale", "upscale_image",
                   {"source_image_url": src_url, "params": {"width": g.trim_w, "height": g.trim_h}},
                   front_up, metadata=meta | {"step": "front-upscale"}, force=args.force)
        Image.open(front_src).convert("RGB").resize(WORK_FRONT, Image.LANCZOS).save(work_png)
        work_url = c.upload_step("upload-front-working", work_png)
        c.job_step("outpaint-working", "inpaint_image",
                   {"source_image_url": work_url,
                    "params": {"left": plan["left"], "top": plan["top"], "right": 0, "bottom": plan["bottom"],
                               "seed": op["seed"], "negative_prompt": op["negative_prompt"]}},
                   outpaint, prompt=op["prompt"], metadata=meta | {"step": "outpaint-working"}, force=args.force)
        assert Image.open(outpaint).size == plan["work_size"], (Image.open(outpaint).size, plan["work_size"])
        op_job = c.records["outpaint-working"]["job_id"]
        uw, uh = plan["upscale_size"]
        c.job_step("fill-upscale", "upscale_image",
                   {"source_image_job_id": op_job, "params": {"width": uw, "height": uh}},
                   fill_up, metadata=meta | {"step": "fill-upscale"}, force=args.force)
    for p in (front_up, fill_up):
        if not p.exists():
            raise SystemExit(f"{p} missing; run without --no-conduct")

    art = Image.open(front_up).convert("RGB")
    fill = Image.open(fill_up).convert("RGB")
    copy = parse_copy(COPY)
    text_cfg = cfg.get("text", {})
    plan_b = plan_back(g, copy, text_cfg)
    wrap_art = fill_canvas(g, fill)
    spine_band(g, wrap_art, text_cfg)
    paste_front(g, wrap_art, art)
    back_panels(g, wrap_art, plan_b, text_cfg)
    wrap_art.save(OUT / "05-wrap-art.png")

    final = wrap_art.copy()
    boxes = add_text(g, final, copy, plan_b, text_cfg)
    final.save(OUT / "06-wrap-final-rgb.png")
    write_proof(g, final, OUT / "cover-proof.jpg")

    src_icc = Image.open(front_src).info.get("icc_profile")
    cmyk = to_cmyk(final, icc_path, src_icc)
    arr = np.asarray(cmyk).astype(np.uint16)
    tac = arr.sum(axis=2)
    pdf = OUT / "geography-as-destiny-cover.pdf"
    info = write_cmyk_pdf(cmyk, pdf, page_w_in=g.page_w_in, page_h_in=g.page_h_in, bleed_in=g.bleed_in,
                          icc_path=icc_path, title=f"{TITLE} (cover)", author=AUTHOR)
    report = {"geometry": {"canvas_px": [g.canvas_w, g.canvas_h], "page_in": [g.page_w_in, g.page_h_in],
                           "spine_in": g.spine_in, "spine_px": g.spine_w, "front_x0": g.front_x0,
                           "barcode_box": g.barcode_box, "working_plan": plan},
              "text_boxes": boxes, "cmyk": {"profile": str(icc_path.relative_to(ROOT)),
                                            "max_total_ink_pct": round(float(tac.max()) / 255 * 100, 1),
                                            "p99_total_ink_pct": round(float(np.percentile(tac, 99)) / 255 * 100, 1)},
              "pdf": info}
    (OUT / "build-report.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report["cmyk"] | {"pdf_bytes": info["bytes"], "filter": info["filter"]}))
    print(f"wrote {pdf.relative_to(ROOT)} and {OUT.relative_to(ROOT)}/cover-proof.jpg")
    return 0


if __name__ == "__main__":
    sys.exit(main())
