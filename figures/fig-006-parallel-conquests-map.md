---
id: fig-006
title: "The Parallel Conquests — Same Decade, Opposite Sides"
type: map
implementation: d3
status: concept
chapter: 6
---

## What It Shows
Split-screen or side-by-side animated map: American westward expansion and Russian Central Asian conquest advancing simultaneously (1860s-1880s). Railroad lines extending. Territory changing control. The visual parallelism IS the argument.

## Why It Matters
The flagship evidence for the entire thesis, rendered as an image. The reader watches two independent processes — driven by the same technology, against the same kind of culture, with no coordination — produce the same result in the same decade. The convergence is viscerally apparent without any text needed.

## Data Sources
- Railroad construction timelines: historically documented (year by year for both Transcontinental and Transcaspian)
- Territory control boundaries: historical maps by decade (1860, 1870, 1880, 1890)
- Terrain base: same SRTM/terrain tiles as other maps
- Nomadic territory boundaries (approximate): Comanchería, Kazakh hordes

## Implementation Notes
- D3.js with timeline slider (or auto-playing animation)
- Split-screen: American West on left, Central Asian steppe on right
- Same scale, same projection distortion (both showing large flat steppe/plains)
- Railroad lines appearing year by year (extending from east on the American side, from west on the Russian side)
- Territory shading changing as control shifts
- Timeline at bottom: single slider controls both maps simultaneously
- The simultaneity is the point — one slider, both maps moving together

## Sketch / Requirements
- Left panel: Great Plains (Texas to Montana, Mississippi to Rockies)
  - Railroad lines extending westward from 1860
  - Comanchería shrinking
  - Blue = U.S. controlled, fading = contested
- Right panel: Central Asian steppe (Caspian to Tian Shan)
  - Transcaspian Railway extending eastward from 1880
  - Kazakh/Turkmen territory shrinking
  - Red = Russian controlled, fading = contested
- Bottom: timeline slider 1855-1895, single control for both panels
- Optional: click on a year to get a brief text card (what happened that year on each side)

## The Test
Show this to someone without explanation. Ask: "What is the relationship between these two maps?" If they say "the same thing is happening at the same time," the figure made the argument.
