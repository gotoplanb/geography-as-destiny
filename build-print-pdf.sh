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
AUTHOR="Dave Stanton"
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
% No clickable links in a print interior. KDP strips link annotations itself
% and then reports "we removed non-printable markup" for every page that had
% one; giving it nothing to strip keeps the Previewer clean. draft mode leaves
% every URL and cross-reference printed as ordinary text -- it only suppresses
% the annotation layer. Passed as a package option because pandoc's template
% loads hyperref after this preamble is inserted.
\PassOptionsToPackage{draft}{hyperref}
\usepackage{xeCJK}
\setCJKmainfont{Songti SC}
% xeCJK classifies em/en dashes, curly quotes and the ellipsis as CJK
% punctuation and applies CJK spacing to them, which swallows the following
% space ("river"prediction", "Reinterpretation —Missionary") in 2400+ places.
% xeCJK is here only for the handful of Chinese glyphs in captions and names,
% so hand these characters back to the Latin typesetting rules.
\xeCJKDeclareCharClass{Default}{"2013, "2014, "2018, "2019, "201C, "201D, "2026}
\raggedbottom
% Footnotes -> per-chapter endnotes (paired with print-endnotes.lua):
% every note becomes an \endnote; \flushnotes prints a section's accumulated
% notes under a "Notes" heading and resets numbering, or is a no-op if the
% section had none.
\usepackage{endnotes}
\let\footnote\endnote
% Suppress the endnotes package's own "Notes" heading + running-head mark:
% every note-bearing section already carries its own "## Notes" signpost in
% the source, which heads the list. Avoids a doubled heading.
\renewcommand{\enoteheading}{}
\newcommand{\flushnotes}{\ifnum\value{endnote}>0\relax\theendnotes\setcounter{endnote}{0}\fi}
% Running heads. The book class puts the *section* title on the recto, and this
% book's section titles ("V. The Receiving End -- Frontier Lifecycle and
% Threshold Crossing") are far wider than the 324pt text block. LaTeX does not
% wrap a head, it overflows it, so those ran off the page edge and KDP rejected
% the file for text outside the margins. Verso carries the book title, recto the
% chapter title, and truncate caps both so a long one can never overrun.
\usepackage{fancyhdr}
\usepackage{truncate}
\pagestyle{fancy}
\fancyhf{}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\chaptermark}[1]{\markboth{#1}{}}
\fancyhead[LE]{\small\thepage}
\fancyhead[RE]{\small\scshape\truncate{0.8\headwidth}{Geography as Destiny}}
\fancyhead[LO]{\small\scshape\truncate{0.8\headwidth}{\leftmark}}
\fancyhead[RO]{\small\thepage}
% Pandoc 3.x bounds every figure with \pandocbounded, which scales to full
% \textheight -- for a full-height portrait plate that leaves no room for the
% caption, and the frontispiece pushed its caption past the bottom trim. Same
% definition, scaled to 0.85\textheight so plate and caption fit together.
\makeatletter
\AtBeginDocument{%
  \renewcommand*\pandocbounded[1]{%
    \sbox\pandoc@box{#1}%
    \Gscale@div\@tempa{\dimexpr 0.85\textheight\relax}{\dimexpr\ht\pandoc@box+\dp\pandoc@box\relax}%
    \Gscale@div\@tempb{\linewidth}{\wd\pandoc@box}%
    \ifdim\@tempb\p@<\@tempa\p@\let\@tempa\@tempb\fi
    \ifdim\@tempa\p@<\p@\scalebox{\@tempa}{\usebox\pandoc@box}%
    \else\usebox\pandoc@box\fi}}
\makeatother
% Let TeX loosen a paragraph on a final pass rather than shove an unbreakable
% token past the margin (e.g. "Tajik/Uzbek/Turkmen" -- no hyphenation point and
% no break at a slash).
\setlength{\emergencystretch}{3em}
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
\\noindent ISBN: 9798174359512\\par
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
    --lua-filter=print-endnotes.lua \
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
