---
id: fig-011
title: "Comanche Outposts as Non-Linear — No River Spine, No Fixed Infrastructure"
type: map
implementation: python
status: rendered
chapter: 6
---

## What It Shows
The Comanchería with known outpost/camp locations plotted against the terrain. The contrast with a linear organizing feature (river, mountain corridor, wall) is the point. The outposts are dispersed, fluid, non-linear — because the terrain has no linear feature to organize around.

## Why It Matters
Makes the geographic-constraint argument visual. The reader sees the open steppe with scattered outposts and understands immediately why the Comanche couldn't build the kind of fixed frontier infrastructure that Chinese/Persian empires built along rivers and mountain corridors. The terrain doesn't offer a spine. The administration reflects the terrain.

## Data Sources
- Comanchería extent: approximate boundaries from Hämäläinen (roughly Texas panhandle to New Mexico, Oklahoma to northern Mexico)
- Outpost/camp locations: from Hämäläinen if specific sites are named, otherwise approximate based on known seasonal patterns
- Terrain: SRTM for the southern Plains — the flat, featureless topography IS the data
- Contrast panel: a comparable-scale map of the Gansu Corridor or the Nile valley showing linear organizing geography with fixed infrastructure along it

## Implementation Notes
- Python: matplotlib with cartopy
- Two panels side by side:
  - Left: Comanchería — flat terrain, scattered outpost dots, no linear pattern visible
  - Right: Gansu Corridor or Silk Road northern route — terrain forcing linear infrastructure along a visible corridor
- The contrast is the argument. No annotation needed beyond labels.

## The Test
Show both panels without labels. Ask: "Which terrain supports permanent imperial infrastructure?" The answer should be visually obvious.
