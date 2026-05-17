#!/bin/bash
# Build epub from the book's markdown chapters
# Requires: pandoc (brew install pandoc)
#
# Usage: ./build-epub.sh
# Output: build/geography-as-destiny.epub

set -e

TITLE="Geography as Destiny"
SUBTITLE="A Probabilistic History of Human Civilization"
AUTHOR="Dave Stanton & Claude (Anthropic)"
OUTPUT_DIR="build"
OUTPUT_FILE="${OUTPUT_DIR}/geography-as-destiny.epub"
TEMP_DIR="${OUTPUT_DIR}/temp_chapters"

# Version info from git
VERSION=$(git describe --tags --abbrev=0 2>/dev/null || echo "untagged")
COMMIT=$(git rev-parse --short HEAD 2>/dev/null || echo "unknown")
GIT_DESCRIBE=$(git describe --tags 2>/dev/null || echo "${COMMIT}")
BUILD_DATE=$(date '+%Y-%m-%d')
BUILD_MONTH_YEAR=$(date '+%B %Y')
DATE="${BUILD_MONTH_YEAR} · ${VERSION} (${COMMIT})"

mkdir -p "$OUTPUT_DIR" "$TEMP_DIR"

# Generate colophon page with version info
cat > "${TEMP_DIR}/colophon.md" << EOF
---
title: Colophon
part: Back Matter
---

# Colophon

This book is version-controlled like software. Each tagged version is a coherent readable state of the same evolving body of work. Major version bumps reflect structural changes to the framework; minor version bumps reflect substantive content additions; patch versions reflect corrections and cleanup.

**This edition.**

- Version: \`${VERSION}\`
- Git describe: \`${GIT_DESCRIBE}\`
- Commit: \`${COMMIT}\`
- Built: ${BUILD_DATE}

The complete source — including all reference cards, figures, the full revision history, and earlier versions accessible by tag — is available at <https://github.com/gotoplanb/geography-as-destiny>.

This approach is described in the foreword as the renegade-historian methodology: the book evolves continuously under git versioning rather than as discrete editions separated by years. The reader holds a specific moment in the framework's development. Earlier moments remain accessible. Later moments will exist.

The framework that argues geography sets the probability distribution of civilizational outcomes is itself a draw from a distribution. This is the draw at ${VERSION}.
EOF

# Chapter order — the reading sequence
CHAPTERS=(
    foreword.md
    prologue.md
    chapters/01-the-distribution/index.md
    chapters/01a-bronze-age-substrate/index.md
    chapters/02-the-river-spine/index.md
    chapters/03-the-chokepoint/index.md
    chapters/04-the-silk-road/index.md
    chapters/05-the-islamic-diffusion/index.md
    chapters/06-the-parallel-conquests/index.md
    chapters/07-the-great-mans-hardest-test/index.md
    chapters/08-the-synthesis-frontier/index.md
    chapters/appendix-a/index.md
    chapters/appendix-b/index.md
    chapters/appendix-c/index.md
    ${TEMP_DIR}/colophon.md
)

echo "Building epub..."
echo "  Title: $TITLE"
echo "  Chapters: ${#CHAPTERS[@]}"

# Create a temporary metadata file
cat > "${OUTPUT_DIR}/metadata.yaml" << EOF
---
title: "${TITLE}"
subtitle: "${SUBTITLE}"
author: "${AUTHOR}"
date: "${DATE}"
lang: en-US
description: |
  Geography sets the probability distribution of historical outcomes.
  This is not determinism. It is statistics.
rights: "Open Access"
---
EOF

# Strip YAML frontmatter from each chapter to prevent pandoc from
# using the last chapter's title as the book title
STRIPPED_CHAPTERS=()
for i in "${!CHAPTERS[@]}"; do
    src="${CHAPTERS[$i]}"
    dest="${TEMP_DIR}/$(printf '%02d' $i).md"
    # Remove YAML frontmatter (everything between first --- and second ---)
    sed '1{/^---$/!q;};1,/^---$/d' "$src" > "$dest"
    STRIPPED_CHAPTERS+=("$dest")
done

# Build the epub
# --toc: generate table of contents
# --toc-depth=1: only top-level headings in TOC
# --split-level=1: split on H1 headings
# --metadata-file: book metadata
# --resource-path: where to find images
pandoc \
    --metadata-file="${OUTPUT_DIR}/metadata.yaml" \
    --epub-cover-image=cover.png \
    --css=epub.css \
    --toc \
    --toc-depth=1 \
    --split-level=1 \
    --resource-path=.:figures/output:chapters \
    --strip-comments \
    -o "$OUTPUT_FILE" \
    "${STRIPPED_CHAPTERS[@]}"

# Clean up temp files
rm -rf "$TEMP_DIR" "${OUTPUT_DIR}/metadata.yaml"

# Report
FILE_SIZE=$(du -h "$OUTPUT_FILE" | cut -f1)
echo ""
echo "Built: $OUTPUT_FILE ($FILE_SIZE)"
echo ""
echo "Contents:"
for ch in "${CHAPTERS[@]}"; do
    echo "  ✓ $ch"
done
echo ""
echo "Note: Reference cards and interactive figures are available at"
echo "      davestanton.com/book"
