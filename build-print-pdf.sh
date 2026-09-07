#!/bin/bash
# Build a print-ready interior PDF for KDP paperback (6x9, B&W).
# Requires: pandoc + tectonic (brew install pandoc tectonic)
#
# Usage: ./build-print-pdf.sh
# Output: build/geography-as-destiny-print.pdf
#
# NOTE: this is the INTERIOR only. The wraparound cover is a separate
# KDP upload (front + spine + back as one CMYK PDF).

set -e

TITLE="Geography as Destiny"
SUBTITLE="A Probabilistic History of Human Civilization"
AUTHOR="Dave Stanton & Claude (Anthropic)"
OUTPUT_DIR="build"
OUTPUT_FILE="${OUTPUT_DIR}/geography-as-destiny-print.pdf"
TEMP_DIR="${OUTPUT_DIR}/temp_print"

# Version info from git (mirrors build-epub.sh)
VERSION=$(git describe --tags --abbrev=0 2>/dev/null || echo "untagged")
COMMIT=$(git rev-parse --short HEAD 2>/dev/null || echo "unknown")
GIT_DESCRIBE=$(git describe --tags 2>/dev/null || echo "${COMMIT}")
BUILD_DATE=$(date '+%Y-%m-%d')

mkdir -p "$OUTPUT_DIR" "$TEMP_DIR"

# Colophon with version info (same as epub)
cat > "${TEMP_DIR}/colophon.md" << EOF
---
title: Colophon
---

# Colophon {-}

This book is version-controlled like software. Each tagged version is a coherent readable state of the same evolving body of work.

**This edition.** Version \`${VERSION}\` · git describe \`${GIT_DESCRIBE}\` · commit \`${COMMIT}\` · built ${BUILD_DATE}.

The complete source — all reference cards, figures, the full revision history, and earlier versions accessible by tag — is at <https://github.com/gotoplanb/geography-as-destiny>.

The framework that argues geography sets the probability distribution of civilizational outcomes is itself a draw from a distribution. This is the draw at ${VERSION}.
EOF

# Reading sequence (mirrors build-epub.sh; interior only, no cover)
CHAPTERS=(
    frontispiece.md
    foreword.md
    prologue.md
    chapters/intellectual-lineage/index.md
    chapters/01-the-distribution/index.md
    chapters/02-the-anti-hero/index.md
    chapters/02a-bronze-age-substrate/index.md
    chapters/03-the-bronze-age-collapse/index.md
    chapters/04-the-river-spine/index.md
    chapters/05-the-chokepoint/index.md
    chapters/06-the-silk-road/index.md
    chapters/07-the-maritime-turn/index.md
    chapters/08-the-islamic-diffusion/index.md
    chapters/09-the-parallel-conquests/index.md
    chapters/10-the-great-mans-hardest-test/index.md
    chapters/11-the-synthesis-frontier/index.md
    epilogue.md
    chapters/appendix-a/index.md
    chapters/appendix-b/index.md
    chapters/appendix-c/index.md
    chapters/appendix-d/index.md
    ${TEMP_DIR}/colophon.md
)

echo "Building print interior PDF..."
echo "  Trim: 6x9 in  ·  Chapters: ${#CHAPTERS[@]}"

# Metadata (drives the title page)
cat > "${TEMP_DIR}/metadata.yaml" << EOF
---
title: "${TITLE}"
subtitle: "${SUBTITLE}"
author: "${AUTHOR}"
lang: en-US
---
EOF

# Strip YAML frontmatter from each source file
STRIPPED_CHAPTERS=()
for i in "${!CHAPTERS[@]}"; do
    src="${CHAPTERS[$i]}"
    dest="${TEMP_DIR}/$(printf '%02d' $i).md"
    sed '1{/^---$/!q;};1,/^---$/d' "$src" > "$dest"
    STRIPPED_CHAPTERS+=("$dest")
done

# Build the PDF via tectonic (XeTeX; embeds fonts; 6x9 book geometry).
# Margins sized for a ~400-450pp perfect-bound book: KDP requires a >=0.75in
# inside (gutter) margin in that range; outside/top/bottom kept generous.
pandoc \
    --metadata-file="${TEMP_DIR}/metadata.yaml" \
    --toc \
    --toc-depth=1 \
    --resource-path=.:figures/output:chapters \
    --pdf-engine=tectonic \
    -V documentclass=book \
    -V classoption=twoside \
    -V geometry:paperwidth=6in \
    -V geometry:paperheight=9in \
    -V geometry:inner=0.875in \
    -V geometry:outer=0.625in \
    -V geometry:top=0.75in \
    -V geometry:bottom=0.75in \
    -V fontsize=11pt \
    -V linkcolor=black \
    -V urlcolor=black \
    -V toccolor=black \
    -o "$OUTPUT_FILE" \
    "${STRIPPED_CHAPTERS[@]}"

rm -rf "$TEMP_DIR"

FILE_SIZE=$(du -h "$OUTPUT_FILE" | cut -f1)
PAGES=$(pdfinfo "$OUTPUT_FILE" 2>/dev/null | awk '/^Pages:/{print $2}')
echo ""
echo "Built: $OUTPUT_FILE ($FILE_SIZE)"
echo "Page count: ${PAGES:-unknown}"
if [ -n "$PAGES" ]; then
    SPINE=$(python3 -c "print(f'{$PAGES*0.0025:.3f}')")
    echo "=> Cream-paper spine width: ${SPINE} in  (page_count x 0.0025)"
fi
