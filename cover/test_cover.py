"""Checks for the KDP wrap cover. Geometry tests always run; output tests run
when build/cover has been built (`.venv/bin/python cover/build_cover.py`).

    .venv/bin/python -m pytest cover/ -q
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
import pytest
from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_cover import (CFG, FOLD_RAMP_PX, KDP_IN_PER_PAGE, OUT, ROOT, SPINE_TOLERANCE_IN,  # noqa: E402
                         Geometry)

cfg = json.loads(CFG.read_text())
g = Geometry.from_config(cfg)
PDF = OUT / "geography-as-destiny-cover.pdf"
built = pytest.mark.skipif(not PDF.exists(), reason="cover not built yet")


# ------------------------------------------------------------- geometry ----
def test_spine_matches_kdp_thickness_for_recorded_page_count():
    assert abs(cfg["page_count"] * KDP_IN_PER_PAGE[cfg["paper"]] - cfg["spine_in"]) <= SPINE_TOLERANCE_IN


def test_wrap_dimensions_are_kdp_formula():
    # KDP: width = bleed + trim + spine + trim + bleed ; height = trim + 2*bleed
    assert g.page_w_in == pytest.approx(0.125 + 6 + cfg["spine_in"] + 6 + 0.125)
    assert g.page_h_in == pytest.approx(9.25)
    assert (g.canvas_w, g.canvas_h) == (3993, 2776)
    assert g.canvas_w / g.page_w_in >= 300 and g.canvas_h / g.page_h_in >= 300


def test_panels_tile_the_canvas_left_to_right():
    assert g.spine_x0 == g.bleed + g.trim_w
    assert g.front_x0 == g.spine_x0 + g.spine_w
    assert g.front_x0 + g.trim_w + g.bleed == g.canvas_w


def test_working_plan_maps_fill_edge_onto_front_edge():
    p = g.working_plan()
    assert p["work_size"][0] % 8 == 0 and p["work_size"][1] % 8 == 0
    assert round(p["left"] * p["upscale_size"][0] / p["work_size"][0]) == g.front_x0
    assert p["upscale_size"][1] == g.canvas_h


def test_barcode_box_inside_back_trim_with_quarter_inch_margin():
    x0, y0, x1, y1 = g.barcode_box
    assert (x1 - x0, y1 - y0) == (600, 360)
    assert x1 == g.spine_x0 - 75 and y1 == g.canvas_h - g.bleed - 75
    assert x0 > g.bleed + g.safe


# -------------------------------------------------------------- outputs ----
@built
def test_pdf_page_is_exact_kdp_wrap_with_trim_and_output_intent():
    from pypdf import PdfReader
    r = PdfReader(str(PDF))
    assert len(r.pages) == 1
    pg = r.pages[0]
    w, h = float(pg.mediabox.width) / 72, float(pg.mediabox.height) / 72
    assert w == pytest.approx(g.page_w_in, abs=0.001) and h == pytest.approx(g.page_h_in, abs=0.001)
    tb = pg.trimbox
    assert float(tb.left) == pytest.approx(9.0, abs=0.01) and float(tb.bottom) == pytest.approx(9.0, abs=0.01)
    assert float(tb.width) / 72 == pytest.approx(g.page_w_in - 0.25, abs=0.001)
    xo = pg["/Resources"]["/XObject"]["/Im0"].get_object()
    assert xo["/ColorSpace"] == "/DeviceCMYK" and xo["/BitsPerComponent"] == 8
    assert (xo["/Width"], xo["/Height"]) == (g.canvas_w, g.canvas_h)
    assert xo["/Width"] / w >= 300 and xo["/Height"] / h >= 300
    intents = r.trailer["/Root"]["/OutputIntents"]
    assert "SWOP" in str(intents[0].get_object()["/Info"])
    assert PDF.stat().st_size <= 40 * 1024 * 1024


@built
def test_pdf_image_round_trips_as_cmyk_with_parchment_not_inverted():
    from pypdf import PdfReader
    im = PdfReader(str(PDF)).pages[0].images[0].image
    assert im.mode == "CMYK" and im.size == (g.canvas_w, g.canvas_h)
    # a patch of bare parchment on the front, right of the title block: light, warm -> low C, low K
    c, m, y, k = np.asarray(im.crop((g.front_x0 + 1500, 100, g.front_x0 + 1700, 300))).reshape(-1, 4).mean(0)
    assert k < 60 and c < 90 and y > m, (c, m, y, k)


@built
def test_front_art_is_untouched_except_fold_ramp_and_bleed():
    art = np.asarray(Image.open(OUT / "01-front-upscaled.png").convert("RGB"))
    final = np.asarray(Image.open(OUT / "06-wrap-final-rgb.png").convert("RGB"))
    x0, y0 = g.front_x0 + FOLD_RAMP_PX, g.bleed
    region = final[y0:y0 + g.trim_h, x0:x0 + g.trim_w - FOLD_RAMP_PX]
    assert np.array_equal(region, art[:, FOLD_RAMP_PX:])


@built
def test_text_stays_in_spine_and_back_safe_zones_and_off_the_barcode():
    base = np.asarray(Image.open(OUT / "05-wrap-art.png").convert("RGB"))
    final = np.asarray(Image.open(OUT / "06-wrap-final-rgb.png").convert("RGB"))
    diff = np.any(base != final, axis=2)
    ys, xs = np.nonzero(diff)
    assert len(xs) > 0
    # nothing drawn on the front panel
    assert not diff[:, g.front_x0:].any()
    # spine text within the spine minus 1/16 in clearance on each side, and inside top/bottom safe zone
    sx = xs[(xs >= g.spine_x0) & (xs < g.front_x0)]
    sy = ys[(xs >= g.spine_x0) & (xs < g.front_x0)]
    assert sx.min() >= g.spine_x0 + g.spine_clear and sx.max() < g.front_x0 - g.spine_clear
    assert sy.min() >= g.bleed + g.safe and sy.max() < g.canvas_h - g.bleed - g.safe
    # back text inside the safe zone
    bx = xs[xs < g.spine_x0]; by = ys[xs < g.spine_x0]
    assert bx.min() >= g.bleed + g.safe and bx.max() < g.spine_x0 - g.safe
    assert by.min() >= g.bleed + g.safe and by.max() < g.canvas_h - g.bleed - g.safe
    # barcode zone untouched
    x0, y0, x1, y1 = g.barcode_box
    assert not diff[y0:y1, x0:x1].any()


@built
def test_build_report_records_conduct_params_for_reproducibility():
    jobs = json.loads((OUT / "jobs.json").read_text())
    for step in ("front-upscale", "outpaint-working", "fill-upscale"):
        assert jobs[step]["kind"] == "job" and jobs[step]["effective_params"], step
    assert "seed" in jobs["outpaint-working"]["effective_params"]
    rep = json.loads((OUT / "build-report.json").read_text())
    assert rep["pdf"]["dpi"][0] >= 300 and rep["pdf"]["dpi"][1] >= 300
