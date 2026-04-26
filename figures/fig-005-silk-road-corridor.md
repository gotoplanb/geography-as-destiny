---
id: fig-005
title: "The Silk Road Corridor — Terrain Determines Routes"
type: map
implementation: leaflet
status: rendered
chapter: 4
---

## What It Shows
Interactive terrain map showing why the Silk Road routes went where they did. The topography makes the routes obvious before you draw them — funnels, fans, the Pamir Knot, the Taklamakan void, the Gansu Corridor compression.

## Why It Matters
The single most important visual in Chapter 4. The reader sees the terrain and understands immediately why trade concentrated at these specific nodes. No narrative required — the geography speaks for itself. This is what "reading the channel" means in practice.

## Data Sources
- Terrain: SRTM or Mapbox terrain tiles (freely available)
- Routes: GeoJSON lines for the northern and southern overland routes, maritime route
- Nodes: GeoJSON points for Samarkand, Bukhara, Dunhuang, Kashgar, Turfan, Niya, etc.
- Chokepoints: highlighted zones (Gansu Corridor, Pamir Knot, Afghan corridor)

## Implementation Notes
- Leaflet.js or MapLibre GL with terrain hillshade base layer
- Interactive: hover over nodes for brief description, click for detail
- Toggle layers: overland routes / maritime route / chokepoints / abandoned oasis cities
- The terrain base is always visible and dominant — routes and nodes overlay, they don't replace
- Consider a "remove all routes" button that shows the reader the bare terrain — the routes should be guessable from topography alone

## Sketch / Requirements
- Extent: roughly Mediterranean to Chinese coast, Horn of Africa to Siberia
- Base: terrain hillshade (mountains visible, deserts visible, water visible)
- Layer 1: Northern overland route (blue line)
- Layer 2: Southern overland route (red line, dashed where abandoned/fragile)
- Layer 3: Maritime route (green line, around Southeast Asia)
- Layer 4: Active nodes (circles, sized by historical significance)
- Layer 5: Abandoned nodes (hollow circles — Niya, Loulan, Miran)
- Layer 6: Chokepoints (shaded polygons — Gansu Corridor, Pamir Knot, Strait of Malacca)
- Interaction: toggle layers, hover tooltips, click to open reference card for that node

## The Test
Show the bare terrain to someone who knows nothing about the Silk Road. Ask them to guess where trade would concentrate. If they point at the actual nodes, the figure has made the argument.
