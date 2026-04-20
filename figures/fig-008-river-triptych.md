---
id: fig-008
title: "Nile / Amazon / Volga Triptych"
type: map
implementation: python
status: concept
chapter: 2
---

## What It Shows
Three rivers at the same scale. Terrain, climate zone, and outlet connectivity visible. Three different rivers, three different outcomes, all predictable from the five-variable model.

## Why It Matters
The counter-case argument made visual. The reader sees that the Nile, Amazon, and Volga are all major rivers — but the surrounding terrain explains why only one built a grain empire, one produced nothing, and one produced a trading state. The differences are visible in the geography before you read a word of history.

## Data Sources
- Terrain: SRTM elevation data for all three river basins
- Climate zones: standard climate classification overlays (Köppen or similar)
- River courses: Natural Earth or equivalent vector data
- City/site locations: major archaeological sites along each river

## Implementation Notes
- Python: matplotlib with cartopy or geopandas, or static image generated from GIS data
- Three panels side by side, same scale, same projection
- Terrain hillshade base with climate zone tinting
- River courses highlighted
- Major sites plotted: Memphis/Thebes on Nile, nothing comparable on Amazon, Atil/Astrakhan on Volga
- Outlet labeled: Mediterranean (connected), Atlantic (connected but wrong environment), Caspian (landlocked)
- Five-variable scorecard below each panel

## Sketch / Requirements
```
┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│              │ │              │ │              │
│     NILE     │ │    AMAZON    │ │    VOLGA     │
│              │ │              │ │              │
│  ● Memphis   │ │              │ │ ● Atil       │
│  ● Thebes    │ │   (nothing)  │ │ ● Astrakhan  │
│              │ │              │ │              │
│  → Medit.    │ │  → Atlantic  │ │  → Caspian   │
│  (connected) │ │  (wrong env) │ │  (landlocked)│
└──────────────┘ └──────────────┘ └──────────────┘

Climate:  subtropical    tropical      continental
Geometry: narrow/linear  vast/diffuse  moderate
Cycle:    predictable    chaotic       seasonal
Outlet:   connected      connected*    landlocked
Adjacent: desert(good)   forest(bad)   steppe(bad)
Score:    5/5            1/5           1/5
```
