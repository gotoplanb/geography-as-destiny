---
id: fig-001
title: "The Great Man as Outlier"
type: graph
implementation: python
status: concept
chapter: 1
---

## What It Shows
A normal distribution with the historical outcome range, specific figures plotted as standard deviations from the mean — showing great men as high-leverage draws, not system overrides.

## Why It Matters
Makes the probabilistic claim visual. The reader sees that Peter and Tecumseh are outliers on opposite tails of the *same* distribution — not different forces, but different draws from one geographic probability space.

## Data Sources
- The distribution is illustrative (not computed from data)
- Positions of historical figures are argued in the text, not empirically measured
- Honest about this: the figure demonstrates the *concept*, not measured magnitudes

## Implementation Notes
- Python: matplotlib or seaborn
- Normal curve with shaded regions
- Annotated points: Peter (~+2σ, compressed timeline), Tecumseh (~-2σ, extended resistance), mean labeled "structural outcome regardless of individual"
- Possibly add Hitler, Timur as additional points with brief labels
- Clean, minimal — not cluttered with too many examples

## Sketch
```
                        ┌─── mean: structural outcome
                        │    (geography determines this)
                        ▼
            ╭──────────────────────╮
           ╱│                      │╲
          ╱ │                      │ ╲
         ╱  │                      │  ╲
        ╱   │                      │   ╲
───────╱────│──────────────────────│────╲───────
   Tecumseh │    most events here  │  Peter
   (-2σ)    │                      │  (+2σ)
   extended │                      │  compressed
   resistance                         timeline

X-axis: "Timing shift from geographic mean"
Y-axis: "Frequency of historical outcomes"
```
