---
id: fig-007
title: "The Aral Sea — The Canal That Destroyed the Lake"
type: map
implementation: leaflet
status: concept
chapter: 4
---

## What It Shows
Before/after satellite imagery with timeline slider. The Aral Sea disappearing over decades as the rivers feeding it were diverted. The most powerful single image of the "variance explosion" principle.

## Why It Matters
The canal metaphor made visceral. The reader sees what happens when you override a geographic system with more complexity than your model accounts for. No text required. The image is the argument.

## Data Sources
- Satellite imagery: Landsat archive (freely available, 1972-present)
- Historical extent: maps/reconstructions for pre-1960 baseline
- Timeline: imagery available at roughly 5-year intervals from 1972

## Implementation Notes
- Leaflet.js with timeline slider
- Base: satellite imagery tiles for each decade (1960s reconstruction, 1972, 1980, 1990, 2000, 2010, 2020)
- Slider scrubs through decades
- The lake shrinks visibly with each step
- Optional overlay: the diverted river channels (Amu Darya, Syr Darya) showing where the water went instead
- Optional: cotton field area growing as lake shrinks (if data available)

## Sketch / Requirements
- Extent: Aral Sea region (roughly 58-62°E, 43-47°N)
- 7-8 time steps from ~1960 to present
- The water area shrinking is the entire visual. Keep it simple.
- Minimal annotation: year label, lake area in km² if computable
- Let the image do the work

## The Test
Show this without context. Ask: "What happened?" Everyone will see it. That's why it's the most powerful image in the book.
