---
id: fig-013
title: "New Mexico Trading Posts Aligned to Geography — Transoxiana in Formation"
type: map
implementation: python
status: spec
chapter: 6
---

## What It Shows
Known New Mexico trading posts and frontier trade fair locations plotted against terrain — Rio Grande valley, mountain passes, and the transition zone into the southern Plains. The argument is that the trading post locations will cluster at geographic chokepoints: river crossings, pass entrances, the friction boundary between the mountain-backed sedentary zone and the open Plains nomadic zone. The geography determines where trade has to happen; the trading posts just mark the spots.

## Why It Matters
Visualizes New Mexico as an emerging Transoxiana — a boundary zone where sedentary and nomadic economies met and both populations had to participate simultaneously. If the trading post locations cluster at the terrain-forced interface points, the map confirms that the trade network was geographically determined, not culturally chosen. Companion to fig-011 (Comanchería non-linear outposts): fig-011 shows the nomadic side's terrain-forced dispersal; fig-013 shows the sedentary-nomadic interface where the two systems had to meet.

## Data Sources
- New Mexico trading post / trade fair locations: Hämäläinen *The Comanche Empire* — specific sites mentioned in the New Mexico / 1786 peace chapters
- Terrain: SRTM elevation for New Mexico and the southern Plains transition zone
- Rio Grande valley corridor: primary sedentary settlement spine
- Mountain passes (Sangre de Cristos, Sacramento Mountains): the geographic features that would force trade routes through specific points
- Plains transition zone: the eastern edge of the mountains where the terrain changes character — this is where the friction boundary runs

## Implementation Notes
- Python: matplotlib with cartopy
- Single panel: New Mexico terrain (elevation shading) with Rio Grande marked, mountain ranges visible, Plains to the east
- Trading post dots plotted over terrain — the clustering pattern at the mountain-Plains interface is the argument
- Optional: draw the approximate friction boundary line (where sedentary administration effectively ended and Comanche territory began)
- Optional comparison inset: Transoxiana at comparable scale showing Sogdian trading cities clustered at the same type of mountain-steppe interface (Fergana Valley edge, Amu Darya crossings)

## The Test
If the trading posts cluster at the terrain-forced interface points — river crossings, pass entrances, the mountain-Plains transition — the geography-determines-trade-location argument is confirmed visually. If they're randomly distributed across the terrain, the argument weakens. The clustering is the prediction; the map is the test.
