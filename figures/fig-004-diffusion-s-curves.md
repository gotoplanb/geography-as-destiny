---
id: fig-004
title: "Diffusion S-Curves: Islam's Two Mechanisms"
type: graph
implementation: python
status: rendered
chapter: 5
---

## What It Shows
Two curves overlaid: Islam's conquest curve (step function) and Islam's trade-route curve (classic S-curve). The gap between them is where the interesting history lives — the political overlay is fast, the belief diffusion is slow.

## Why It Matters
Makes the Chapter 5 argument visual. The reader sees that what looks like "Islam spread" is actually two completely different diffusion mechanisms with different shapes, different timescales, and different implications. The Rogers lens earns its weight by revealing structure invisible in narrative.

## Data Sources
- The curve shapes are argued from historical evidence, not computed from data
- X-axis positions (approximate dates of arrival in specific regions) can be grounded in historiography
- Honest about this: the curves represent the *pattern*, not measured adoption rates

## Implementation Notes
- Python: matplotlib
- X-axis: time (roughly 630 CE to 1500 CE)
- Y-axis: "adoption level" (0 to 1, normalized)
- Curve 1 (conquest): sharp step function — jumps from 0 to ~0.8 within a decade at each conquest event (Arabia, Levant, Persia, Central Asia)
- Curve 2 (trade-route): classic S-curve — slow start, inflection point, gradual saturation — with Rogers adopter categories annotated along the curve
- Gap between curves shaded and labeled: "political Islam precedes cultural Islam by centuries"
- Possibly add a third curve: Manichaeism — fast rise then collapse, showing the contrast

## Sketch
```
Adoption
  1.0 ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┌───────────── Conquest (step)
      │                       │
  0.8 │                       │      ╭─────── Trade-route (S-curve)
      │                       │    ╱
  0.6 │                       │  ╱    ← gap = political precedes cultural
      │                       │╱
  0.4 │          ╭────────────╱
      │        ╱
  0.2 │      ╱        ╭──╮
      │    ╱          │  ╰──── Manichaeism (rise then collapse)
  0.0 ─────────────────────────────────────────────→ Time
      630    750    900    1050    1200    1400
              ↑
          Conquest arrives
```
