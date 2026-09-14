# Print cover pipeline (KDP paperback)

Builds the full-wrap paperback cover — back, spine, front — as a single
CMYK PDF sized exactly to KDP's calculator output. The interior comes from
`build-print-pdf.sh`; this directory only makes the cover.

## What it does

1. **Geometry** from `kdp.json`: 6 × 9 trim, 0.125 in bleed, 300 dpi, and the
   spine width KDP's cover calculator reports for the interior's page count
   and paper. The spine is never estimated — the script cross-checks the
   recorded value against KDP's published per-page thickness and refuses to
   build on a mismatch. **If the interior page count changes, re-run the
   calculator and update `page_count` and `spine_in` together.**
2. **Art via Conduct** (generic image tasks, no KDP knowledge):
   - `upscale_image` — Real-ESRGAN x4 + lanczos to exactly 1800 × 2700 (the
     front trim at 300 dpi) from `cover.png`.
   - `inpaint_image` — SDXL outpaint of the back + spine from a half-scale
     working copy (896 × 1344 front, 1072 px extension, 16 px top/bottom; all
     multiples of 8). ComfyUI cannot VAE-encode the full 3993 × 2776 wrap on
     Apple silicon, so the fill is generated at half scale and then
     `upscale_image`d to exact print pixels. Only the generated fill is
     upscaled; the front art is pasted from the full-resolution upscale.
   - Every step is idempotent: `build/cover/jobs.json` records the request,
     Conduct's job id, and the *effective* parameters it echoes back (seed,
     model, steps, cfg). Re-running with nothing changed costs no GPU time.
3. **Composite**: fill underneath; untouched front art on top with a 24 px
   soft ramp at the spine fold; the front's outer bleed is mirrored from the
   art (continuous at the trim line, cut off in binding). Spine and back text
   set in EB Garamond (`brew install --cask font-eb-garamond`) in the ink
   color sampled from the front title. Back copy lives in `back-cover.md`.
   KDP's barcode zone (2 × 1.2 in, 0.25 in from the trim corner) is kept clear.
4. **Proof**: `build/cover/cover-proof.jpg` at 1/3 scale with trim, safe-zone,
   spine-clearance and barcode guides (tracked in git).
5. **Print**: sRGB → U.S. Web Coated (SWOP) v2 via littleCMS (relative
   colorimetric + black-point compensation), written as a one-page PDF whose
   MediaBox is the exact wrap (13.305 × 9.25 in for 422 cream pages), with
   TrimBox, BleedBox and the SWOP profile as OutputIntent. Lossless Flate when
   it fits KDP's 40 MB limit, otherwise JPEG q95.

## Setup

```bash
uv venv .venv --python 3.12 && uv pip install --python .venv/bin/python -r cover/requirements.txt
brew install --cask font-eb-garamond
# Conduct credentials: ~/conduct-private/book-covers-client.env (never in git)
# Press profile (not in git): download Adobe's ICC bundle and drop
#   "U.S. Web Coated (SWOP) v2" at build/cover/profiles/USWebCoatedSWOP.icc
curl -sSL -o /tmp/adobe-icc.zip https://download.adobe.com/pub/adobe/iccprofiles/win/AdobeICCProfilesCS4Win_end-user.zip
mkdir -p build/cover/profiles && unzip -j /tmp/adobe-icc.zip "*/CMYK/USWebCoatedSWOP.icc" -d build/cover/profiles
```

## Build and test

```bash
.venv/bin/python cover/build_cover.py            # full pipeline (calls Conduct as needed)
.venv/bin/python cover/build_cover.py --no-conduct   # re-composite / re-typeset only
.venv/bin/python cover/build_cover.py --seed 7   # different outpaint
.venv/bin/python -m pytest cover/ -q
```

Outputs in `build/cover/` (gitignored except the proof, `jobs.json`, and the print PDF):
`01-front-upscaled.png`, `03-outpaint-working.png`, `04-fill-upscaled.png`,
`05-wrap-art.png` (no text), `06-wrap-final-rgb.png`, `cover-proof.jpg`,
`geography-as-destiny-cover.pdf`, `build-report.json`.

## Tuning

- `kdp.json` → `outpaint.prompt` / `negative_prompt` / `seed` change the fill.
- `kdp.json` → `text` sets type sizes and margins; `back_text_panel.opacity`
  (0–1) adds a soft parchment wash behind the blurb if the fill is too busy.
- `back-cover.md` is the copy: `# blurb`, `# bio`, `# url` sections,
  `*italics*` supported. The layout reflows.
