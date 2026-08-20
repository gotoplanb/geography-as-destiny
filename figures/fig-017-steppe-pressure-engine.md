---
id: fig-017
title: "The Steppe Pressure Engine"
type: map
implementation: python
status: rendered
chapter: 4
---

## What It Shows
Where a nomadic core on the Pontic–Caspian steppe can project power *cheaply* — a least-cost field over real biomes and terrain that spreads far along the grass corridor (east to the Kazakh steppe, west to its terminus at the Great Hungarian Plain), is dammed by mountains (Caucasus, Carpathians, Alps, Tien Shan), and cannot cross open water.

## Why It Matters
Makes the friction-collapse claim visual and probabilistic: reach is set by the *cost of the ground*, not by the ambition of a leader. The corridor shape is not drawn — it emerges from the real grassland belt, so the reader sees the grass do the work. Two emergent details reward a close look: the western terminus at the Hungarian plain (where forest and the Alps halt the grass), and a thin southward tendril down the west-Caspian shore — the historical "Caspian Gates" invasion route, produced by the model rather than annotated onto it.

## Data Sources
- **Illustrative, not measured.** The *shape* is grounded in real geography; the *cost weights* and *decay scale* are a documented model, not empirical reach or any specific polity.
- Biomes: RESOLVE/WWF Terrestrial Ecoregions 2017 (`BIOME_NUM`). Temperate grassland (steppe) is cheap; desert, forest, taiga are costly.
- Terrain: ETOPO 2022 60-arcsecond elevation (NOAA), read windowed over the frame; high terrain adds cost.
- Land/water: Natural Earth 50m; open water is impassable.
- Honest about this, per fig-001: the figure demonstrates the *mechanism*, not magnitudes.

## Implementation Notes
- `src/fig_017_steppe_pressure_engine.py`. Requires the `geofig` conda env (gdal, geopandas, xarray, **isobands**, cartopy, scikit-image, rioxarray/rasterio). Heavier than the matplotlib-only figures; runs offline once inputs are cached; output committed as static SVG/PNG.
- Pipeline: rasterize ecoregion biomes + windowed ETOPO elevation to the grid → per-cell cost (biome base + elevation + water=∞) → least-cost distance from the core (`skimage.graph.MCP_Geometric`, physical-km sampling) → `power = exp(-cost/scale)` → light Gaussian smoothing → `isobands.from_raster(levels=…)` → filled contour polygons → clipped to land → cartopy parchment base in the house style.
- Derived inputs are cached to `src/fig_017_inputs.npz` (committed, ~0.9 MB) so the figure rebuilds without the raw downloads. Raw DEM/ecoregion files live in `src/data/` (gitignored). All cost weights are explicit constants at the top of the script.

## Limitations / Next Iterations
- Cost weights (per-biome cost, elevation walling thresholds, decay scale) are a chosen model — the honest knob to argue about. They live at the top of the script for easy tuning.
- Single fixed core and a single static snapshot; no seasonality (winter grass/frozen rivers change the cost surface), no multiple competing cores. Each would be a further figure, not a fix to this one.

## Sketch / Description
Wide Eurasian frame (~12°E–96°E, 33°N–60°N), Pontic–Caspian core marked with a star. Nested translucent terracotta bands = relative projected power, following the real steppe belt. Bands ribbon east–west along the grass, stack tightly (pinch) at the Caucasus, terminate near the Hungarian plain in the west, and fade before the Altai / Tien Shan in the east. Anchors labeled: Great Hungarian Plain, Carpathians, Caucasus, Kazakh steppe, Tien Shan, Altai. Caption states plainly that it is an illustrative least-cost model over real biomes and terrain, not measured reach.
