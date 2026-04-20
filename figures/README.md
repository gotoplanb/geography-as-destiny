# Figures and Tables

One file per figure or table. Each is a self-contained unit — like a reference card but for visual evidence.

## File Structure

```markdown
---
id: fig-001
title: "The Great Man as Outlier"
type: graph | map | table | diagram
implementation: python | d3 | leaflet | static
status: concept | spec | implemented
chapter: 1
---

## What It Shows
[One sentence analytical question this figure answers]

## Why It Matters
[How this advances the argument — not decoration, analytical work]

## Data Sources
[Where the underlying data comes from — public datasets, reference cards, computed]

## Implementation Notes
[Technical details: libraries, data format, interactivity requirements]

## Sketch / Description
[Detailed description of what the reader sees, axis labels, annotations]
```

## Naming Convention

`fig-NNN-short-description.md` — numbered sequentially. The source code (Python scripts, D3 components) lives alongside or in a `src/` subdirectory once implemented.

## Types

| Type | Tool | Use Case |
|------|------|----------|
| `graph` | Python (matplotlib/seaborn) | Distributions, S-curves, timelines, scatter plots |
| `map` | D3.js + Leaflet/MapLibre | Interactive corridors, border thrash, terrain overlays |
| `table` | Markdown or generated | Comparative data, variable scoring, timeline alignments |
| `diagram` | Python or static SVG | River cross-sections, system models, flow diagrams |

## Embedding

The web version pulls figures by `id` from this directory. Each chapter's markdown can reference figures inline:

```markdown
See [Figure 1: The Great Man as Outlier](figures/fig-001-great-man-outlier.md).
```

The rendering layer (Flask) resolves this to the appropriate output — static image, interactive D3 component, or data table — based on the `implementation` field in frontmatter.

## Design Principles (from visualizations.md)

- Every figure answers a specific analytical question statable in one sentence
- The terrain base layer is persistent across all maps
- Graphs show distributions, not just narratives
- If a visualization is decorative rather than analytical, cut it (color-is-a-smell applies to visuals)
