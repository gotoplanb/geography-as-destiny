---
id: fig-009
title: "Process Knowledge vs. Commodity Diffusion"
type: graph
implementation: python
status: concept
chapter: 4
---

## What It Shows
Two diffusion curves with fundamentally different shapes: commodity diffusion (gradual, supply-chain-dependent, continuous) vs. process knowledge diffusion (long delay, single threshold event, then rapid self-replicating spread). Paper as the worked example.

## Why It Matters
Extends Rogers with a distinction he doesn't fully articulate. The reader sees that two things traveling the same corridor follow completely different curves because of their transmission mechanism — not because of cultural resistance or geographic barriers. The corridor is the control. The mechanism is the variable.

## Data Sources
- Paper timeline: invention in China ~105 CE, transfer at Talas 751 CE, Baghdad mills 790s CE, Egypt 900s, Europe 1100s
- Silk timeline: continuous trade flow documented across the same period (used as commodity comparison)
- Both are approximate historical dates, not measured quantities

## Implementation Notes
- Python: matplotlib
- X-axis: time (0 CE to 1200 CE)
- Y-axis: "geographic extent of adoption" or "number of production sites"
- Curve 1 (silk/commodity): gradual, continuous, proportional to supply chain capacity. Steady flow from the beginning.
- Curve 2 (paper/process): flat for 650 years (knowledge exists but hasn't transferred), sharp vertical jump at 751 (threshold event), then rapid spread (Samarkand 750s → Baghdad 790s → Egypt 900s → Europe 1100s)
- Annotations: "Knowledge exists in China" (flat period), "Talas — threshold event" (jump), "Self-replicating spread" (rapid rise)
- The 650-year gap is the visual argument

## Sketch
```
Spread
  ▲
  │                                          ╭──── Paper (process)
  │                                        ╱
  │                                      ╱
  │                        ╭───────────╱
  │                       │
  │  ╱─────────────────── │ ──────────────── Silk (commodity)
  │╱                      │
  │                       │
  │   ← 650-year gap →   │← Talas 751
  └───────────────────────────────────────→ Time
  100 CE                              1200 CE
```
