---
id: fig-010
title: "Imperial Climate Pulse — Chinese Power Projection vs. Water Supply"
type: graph
implementation: python
status: concept
chapter: 4
---

## What It Shows
Two overlaid time series: Chinese imperial projection into the Tarim Basin (measured by garrison presence, territory control, or administrative records) and a proxy for regional water availability (tree-ring data, ice-core data, or similar paleoclimate proxy). The correlation should be visible.

## Why It Matters
This is the holdout validation made visual. If imperial projection tracks water supply — advancing during wet periods, retreating during dry — the reader sees the thermodynamic framework confirmed in a graph. The framework predicted this before we saw the data (ref 054). Now the reader sees whether it holds.

## Data Sources
- Imperial projection: historical dates of Chinese garrison presence in Tarim Basin (Han, Tang, Qing). Binary or graded: present/absent, or strength estimate.
- Climate proxy: paleoclimate data for Central Asian precipitation/temperature. Candidates:
  - Tree-ring chronologies from Tian Shan or Kunlun
  - Ice-core data from Guliya or similar
  - Published paleoclimate reconstructions for the Tarim Basin region
- **This figure may require sourcing real data.** If data is available, this becomes the strongest single empirical figure in the book. If not, it remains conceptual.

## Implementation Notes
- Python: matplotlib with dual y-axis
- X-axis: time (200 BCE to 1900 CE)
- Y-axis left: "Imperial projection" (graded scale or binary)
- Y-axis right: "Climate proxy" (precipitation or temperature anomaly)
- The two curves should track visibly if the hypothesis holds
- Annotated events: Han peak, An Lushan collapse, Tang peak, Talas, Qing expansion
- Shaded bands: "wet period" (blue), "dry period" (orange)

## Sketch
```
Projection │    ╭──╮        ╭────╮              ╭───── Climate Proxy
           │    │  │        │    │            ╱
           │ ╭──╯  ╰──╮ ╭──╯    ╰──╮      ╱
           │ │         │ │          │    ╱
           │─╯         ╰─╯          ╰──╱────────────
           └─────────────────────────────────────────→ Time
           Han         Tang              Qing
           peak        peak              peak
```

## Status Note
This figure depends on whether real paleoclimate data is accessible and comparable to the imperial projection timeline. If yes: strongest empirical figure. If no: remains a conceptual diagram showing the predicted correlation. Either way, honest about which it is.
