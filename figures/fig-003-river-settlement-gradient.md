---
id: fig-003
title: "Universal River Settlement Gradient"
type: diagram
implementation: python
status: rendered
chapter: 2
---

## What It Shows
A stylized river cross-section from headwaters to delta with settlement density curve overlaid. The energy dissipation curve predicts where humans settle — and the archaeological record confirms it.

## Why It Matters
This is potentially the quantitative heart of the thesis. If the settlement density curve matches the energy gradient prediction across multiple independent river civilizations, the image alone makes the argument. The figure is the prediction *and* the evidence in one visual.

## Data Sources
- Elevation profile: conceptual/stylized (or actual SRTM data for specific rivers)
- Settlement density: conceptual (or actual archaeological site data if sourced)
- If using real data: SRTM freely available, archaeological databases vary by region
- If conceptual: honest about this, labeled as "predicted pattern"

## Implementation Notes
- Python: matplotlib with dual y-axis
- X-axis: distance from headwaters to delta (normalized)
- Y-axis left: elevation (gradient profile)
- Y-axis right: settlement density (predicted curve)
- Annotated zones: "Headwaters (erosive, sparse)", "Goldilocks zone (first movers)", "Floodplain (surplus, cities)", "Delta (maximum density)"
- Asymmetry visible: hard upstream boundary, soft downstream boundary
- Optionally: overlay multiple rivers (Nile, Indus, Yellow River) on same normalized axes to show the pattern repeats

## Sketch
```
Elevation                                    Settlement Density
  ▲                                                          ▲
  │╲                                                        │
  │  ╲                                                     ╱│
  │    ╲         Goldilocks                              ╱  │
  │      ╲        zone                                 ╱    │
  │        ╲───────┐                               ╱        │
  │          ╲     │                            ╱           │
  │            ╲───┘────────────────────── ╱                │
  │              ╲     Floodplain       ╱                   │
  │                ╲────────────────╱     Delta              │
  └──────────────────────────────────────────────────────────→
  Headwaters                                              Coast
  
  ─── Elevation profile
  ─── Settlement density (predicted)
  ●●● Archaeological sites (actual, if data available)
```

## Extension
If real data is sourced for multiple rivers, this becomes a multi-panel figure showing the same pattern repeating independently. That would be the strongest single image in the book.
