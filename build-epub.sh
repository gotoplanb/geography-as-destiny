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
DATE="2026"
OUTPUT_DIR="build"
OUTPUT_FILE="${OUTPUT_DIR}/geography-as-destiny.epub"

mkdir -p "$OUTPUT_DIR"

# Chapter order — the reading sequence
CHAPTERS=(
    prologue.md
    chapters/01-the-distribution/index.md
    chapters/02-the-river-spine/index.md
    chapters/03-the-chokepoint/index.md
    chapters/04-the-silk-road/index.md
    chapters/05-the-islamic-diffusion/index.md
    chapters/06-the-parallel-conquests/index.md
    chapters/07-the-great-mans-hardest-test/index.md
    chapters/08-the-synthesis-frontier/index.md
    chapters/appendix-a/index.md
    chapters/appendix-b/index.md
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

# Build the epub
# --toc: generate table of contents
# --toc-depth=1: only top-level headings in TOC
# --epub-chapter-level=1: split on H1 headings
# --metadata-file: book metadata
# --resource-path: where to find images
pandoc \
    --metadata-file="${OUTPUT_DIR}/metadata.yaml" \
    --toc \
    --toc-depth=1 \
    --epub-chapter-level=1 \
    --resource-path=.:figures/output:chapters \
    --strip-comments \
    -o "$OUTPUT_FILE" \
    "${CHAPTERS[@]}"

# Clean up temp metadata
rm "${OUTPUT_DIR}/metadata.yaml"

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
