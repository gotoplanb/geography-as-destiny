---
id: fig-015
title: "Pressure-System Geometry Determines Cultural Outcome — Tidal vs Breaking Wave"
type: map
implementation: python
status: rendered
chapter: 1 (framework) / interlude (Bronze Age substrate) / 4 (Silk Road)
---

## What It Shows
Two-panel comparison illustrating that pressure-system geometry determines cultural outcome at contact zones.

**Left panel — Silk Road Tidal System (~50 BCE – 1200 CE).** Two civilization masses (Rome/Persia on the western end, Han/Tang China on the eastern end) shown with concentric gravitational rings representing commercial pull. Bidirectional flow arrows along the corridor between them. Three hybrid cultural nodes (Sogdiana, Gandhara, Dunhuang) shown in purple at the middle relay positions where the two flows meet.

**Right panel — Yamnaya Breaking Wave (~3300–2500 BCE).** Single high-pressure source (Yamnaya/Pontic-Caspian) shown in red with concentric pressure rings radiating outward. Three outward wave arrows (red, thick) in three directions: west to European overlay zone (Corded Ware, Bell Beaker), east to Altai overlay zone (Afanasievo), southeast to Iranian plateau overlay zone (Indo-Iranian). Cultural overlay zones shown in light blue. Thin grey backwash arrows show weak return flow from each overlay zone back toward the source.

## Why It Matters
Makes visible the structural difference between two pressure-system geometries that produce categorically different cultural outcomes through the same general gradient-following mechanism.

- **Tidal geometry** (Silk Road): two comparable civilization masses + compatible commercial logic + stable corridor → continuous bidirectional flow → rich hybrid cultural forms at relay nodes
- **Breaking-wave geometry** (Yamnaya): one high-pressure source + asymmetric receiver capacity → outward pulse with weak backwash → population/cultural overlay rather than synthesis

The figure resolves a question the existing chapters had treated as exceptional cultural creativity at Silk Road nodes versus population replacement at Bronze Age contact zones. The framework's reading: the cultural outcomes are predictable from the pressure-system geometry. Same humans, same general mechanism, different geometry produces different outcome.

## Data Sources
- Silk Road extent: ~30°E to 125°E, approximate corridor across Eurasian land mass
- Han/Tang China extent: approximate around Chang'an region, projected westward
- Rome/Persia extent: approximate around eastern Mediterranean and Iranian plateau
- Sogdiana coordinates: ~65°E, 40°N (Samarkand region)
- Gandhara coordinates: ~72°E, 35°N (upper Indus / northern Pakistan)
- Dunhuang coordinates: ~94°E, 40°N (Gansu Corridor)
- Yamnaya homeland: Pontic-Caspian steppe, ~38–55°E, 44–52°N
- European overlay (Corded Ware, Bell Beaker): ~-5°E to 25°E, 44–58°N
- Altai overlay (Afanasievo): ~78–95°E, 46–55°N
- Iranian overlay (Indo-Iranian): ~50–70°E, 30–40°N

## Implementation Notes
- Python: matplotlib with cartopy, PlateCarree projection
- Color language extends the weather-map palette from fig-014:
  - Gold/dark red = civilization masses (sedentary)
  - Red high-saturation = high-pressure source (pastoralist)
  - Light blue = cultural overlay zone
  - Purple = hybrid cultural node
  - Blue = bidirectional commercial flow (tidal arrows)
  - Red = outward wave arrows (strong, thick)
  - Grey = backwash arrows (thin, dashed)
- Concentric rings around the civilization masses and the Yamnaya source visualize gravitational/pressure intensity
- Shared bottom legend, suptitle carries the structural principle
- Path effects (white stroke) keep labels readable over colored regions

## The Test
Cover the panel labels. The visual should communicate:
- **Left panel:** two colored centers with arrows flowing between them; small purple dots in the middle where the arrows cross
- **Right panel:** one colored center with thick arrows radiating outward; three colored receiving zones with thin arrows trickling back

The viewer should immediately read "two things in mutual exchange" vs "one thing radiating outward." The labels then tell you what the things are and what the cultural products were.

## Relevant Reference Cards
- [ref 183](../references/183-tidal-vs-breaking-wave-pressure-systems-bidirectional-synthesis-vs-unidirectional-overlay.md): The tidal-vs-breaking-wave distinction (this figure's framework)
- [ref 174](../references/174-robust-frontiers-anthony-citation-bundles-of-opposed-customs.md): Anthony's robust frontiers concept
- [ref 179](../references/179-thermodynamic-gradient-following-anti-eugenic-explanation-of-migration-directionality.md): General gradient-following mechanism
- [ref 182](../references/182-directionality-of-knowledge-flow-pressure-gradient-prediction.md): Knowledge flow directionality
- [ref 169](../references/169-innovation-source-vs-amplification-zone-anatolian-farming-mesopotamian-civilization.md): Three-wave European population history
- [ref 076](../references/076-sogdian-identity-dissolution-ethnogenesis.md): Sogdian commercial culture
