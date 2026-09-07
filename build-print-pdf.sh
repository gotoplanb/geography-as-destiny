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

VERSION=$(git describe --tags --abbrev=0 2>/dev/null || echo "untagged")
COMMIT=$(git rev-parse --short HEAD 2>/dev/null || echo "unknown")
GIT_DESCRIBE=$(git describe --tags 2>/dev/null || echo "${COMMIT}")
BUILD_DATE=$(date '+%Y-%m-%d')
YEAR=$(date '+%Y')

mkdir -p "$OUTPUT_DIR" "$TEMP_DIR"

# --- LaTeX preamble (included in header) ---------------------------------
# secnumdepth=-1  : suppress LaTeX auto chapter/section numbers. The source
#                   headings already carry their own labels ("Chapter 1: ...",
#                   "Interlude: ...", "Appendix A: ..."), so auto-numbering
#                   would double them.
# tocdepth=0      : list only chapter-level entries in the TOC.
# xeCJK           : render the CJK glyphs in the frontispiece caption.
cat > "${TEMP_DIR}/preamble.tex" << 'EOF'
\setcounter{secnumdepth}{-1}
\setcounter{tocdepth}{0}
\usepackage{xeCJK}
\setCJKmainfont{Songti SC}
\raggedbottom
EOF

# --- Copyright page (raw LaTeX; own page, not in TOC) --------------------
cat > "${TEMP_DIR}/00_copyright.md" << EOF
\`\`\`{=latex}
\\thispagestyle{empty}
\\vspace*{\\fill}
\\noindent \\textit{${TITLE}: ${SUBTITLE}}\\par
\\vspace{1em}
\\noindent Copyright \\textcopyright\\ ${YEAR} Dave Stanton. All rights reserved.\\par
\\vspace{1em}
\\noindent This book is version-controlled like software. This printing is built from version \\texttt{${GIT_DESCRIBE}} (commit \\texttt{${COMMIT}}), ${BUILD_DATE}. The complete source, reference cards, and revision history are at \\texttt{github.com/gotoplanb/geography-as-destiny}.\\par
\\vspace{1em}
\\noindent ISBN: (assigned at publication)\\par
\\clearpage
\`\`\`
EOF

# --- Table of contents (placed after the copyright page) -----------------
cat > "${TEMP_DIR}/01_toc.md" << 'EOF'
```{=latex}
\tableofcontents
\clearpage
```
EOF

# --- Colophon (back matter) ----------------------------------------------
cat > "${TEMP_DIR}/zz_colophon.md" << EOF
# Colophon

This book is version-controlled like software. Each tagged version is a coherent readable state of the same evolving body of work.

**This edition.** Version \`${VERSION}\` · git describe \`${GIT_DESCRIBE}\` · commit \`${COMMIT}\` · built ${BUILD_DATE}.

The complete source — all reference cards, figures, the full revision history, and earlier versions accessible by tag — is at <https://github.com/gotoplanb/geography-as-destiny>.

The framework that argues geography sets the probability distribution of civilizational outcomes is itself a draw from a distribution. This is the draw at ${VERSION}.
EOF

# Reading sequence (interior only, no cover)
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
)

echo "Building print interior PDF (6x9, polished)..."

cat > "${TEMP_DIR}/metadata.yaml" << EOF
---
title: "${TITLE}"
subtitle: "${SUBTITLE}"
author: "${AUTHOR}"
lang: en-US
---
EOF

# Front-matter title page + copyright + TOC come first.
STRIPPED_CHAPTERS=("${TEMP_DIR}/00_copyright.md" "${TEMP_DIR}/01_toc.md")

# Strip YAML frontmatter and neutralize dead cross-reference links
# ([text](something.md) -> text) so print has no live links to files that
# don't exist on paper; this also removes the hyperref page-break warnings.
# Image embeds (![alt](x.png)) and real URLs (http...) are left intact.
for i in "${!CHAPTERS[@]}"; do
    src="${CHAPTERS[$i]}"
    dest="${TEMP_DIR}/$(printf '%02d' $((i+2)))_body.md"
    sed '1{/^---$/!q;};1,/^---$/d' "$src" \
      | perl -pe 's/\[([^\]]*)\]\([^)]*\.md[^)]*\)/$1/g' > "$dest"
    STRIPPED_CHAPTERS+=("$dest")
done

STRIPPED_CHAPTERS+=("${TEMP_DIR}/zz_colophon.md")

pandoc \
    --metadata-file="${TEMP_DIR}/metadata.yaml" \
    -H "${TEMP_DIR}/preamble.tex" \
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
