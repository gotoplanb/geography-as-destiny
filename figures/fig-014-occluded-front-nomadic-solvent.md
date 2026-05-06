---
id: fig-014
title: "The Occluded Front — Nomadic Solvent and Sedentary Succession"
type: map
implementation: python
status: rendered
chapter: 6
---

## What It Shows
Two-panel comparison using weather-map visual language. Left panel: North America ~1820–1845 — Comanche pressure system (red arrows, moving SW) dissolving Mexican sovereignty over northern Mexico (amber dissolved zone), American pressure system (blue arrows, moving W) catching the slower Comanche front, collision zone in Texas/New Mexico (purple). Right panel: Central Asia ~700–900 CE — Turkic/steppe confederation pressure (red) dissolving Tang grip on Transoxiana, Abbasid/Samanid expansion (blue) crystallizing in the dissolved space, collision zone at Samarkand.

## Why It Matters
Makes the abstract mechanism visual: two pressure systems moving in the same direction at different speeds. The faster catches the slower. The incoming sedentary empire doesn't fight the incumbent — it administers the vacuum the nomadic solvent created. Same mechanism, two independent cases, one figure. The meteorological framing carries the key insight: the collision zone (Texas; Transoxiana) is where the most dramatic weather happens — not between the two sedentary empires directly, but at the leading edge of the faster front catching the slower one.

## Data Sources
- Comanchería extent: approximate from Hämäläinen
- Mexican power vacuum: northern Mexico frontier zone, ~1820s onward
- American expansion direction: westward settlement pressure
- Transoxiana dissolved zone: Amu Darya / Syr Darya basin, approximate extent
- Samarkand coordinates: 66.9°E, 39.7°N
- Abbasid/Samanid expansion arc: from Iranian plateau NE into Central Asia

## Implementation Notes
- Python: matplotlib with cartopy
- Weather-map color language: amber = dissolved zone, red = nomadic pressure, blue = incoming sedentary, purple = collision front, grey = retreating empire
- Pressure system arrows drawn with matplotlib annotate for consistent arrowhead sizing
- Path effects (white stroke) keep labels readable over colored regions
- Shared legend at bottom, suptitle carries the structural principle

## The Test
Cover the panel labels. The visual should communicate: two colored arrow systems converging on an amber zone, with a purple overlap. The viewer should immediately read "two things moving toward the same space at different speeds." The labels then tell you what the things are.
