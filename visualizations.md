# Visualizations — Graphs, Distributions, and Maps

These aren't illustrations. They're the methodology made visible. The book argues that history should be told as distribution, not narrative. If we don't show the distributions, we're still writing narrative history with statistical vocabulary sprinkled on top.

---

## Graphs and Distributions

### 1. The Great Man as Outlier
A normal distribution showing the historical outcome range for a given geographic context. Specific figures plotted as standard deviations from the mean. Peter the Great at ~2.5σ (compressed the conquest timeline). Kenesary Qasymov at ~2σ in the other direction (extended resistance). Both are outliers. Neither shifts the distribution itself.

**Analytical question:** How far from the mean does a "great man" actually move the outcome?

### 2. The Friction Collapse Timeline
Effective geographic friction as a function of time. Technology events marked as step-change drops: sail, railroad, telegraph, internet. Long stable plateaus with sudden drops — the punctuated equilibrium model rendered as a curve.

**Analytical question:** When did geographic constraints stop mattering, and what technology caused each reset?

### 3. The R-Squared Comparison
Three bars or overlapping models: great man theory (low R²), geographic determinism alone (moderate R²), combined three-lens model (higher R²). Even illustrative numbers make the point — we're improving explanatory power, not just reframing.

**Analytical question:** How much more of the historical variance do the three lenses explain compared to alternatives?

### 4. The Diffusion S-Curves
Rogers S-curves applied to specific historical spreads. Candidates:
- Islam along trade routes vs. Islam by conquest (two curves, same religion, different mechanisms)
- Railroad technology adoption in Russia and America (parallel curves, same decade)
- Paper from Talas westward (slow S-curve across centuries)
- The printing press

Geographic variables annotated at inflection points — where did terrain accelerate or slow diffusion?

**Analytical question:** What does the adoption curve actually look like, and where does geography bend it?

### 5. Border Thrash vs. Terrain Stability
Political boundary changes over time overlaid on terrain ruggedness index. The hypothesis: the rougher the terrain, the more stable the borders. Potentially empirically testable with existing GIS data.

**Analytical question:** Does geographic ruggedness predict political boundary stability?

**Data note:** Terrain ruggedness indices exist (e.g., Riley et al. 1999). Historical border datasets exist (e.g., CShapes). This could be an actual quantitative test of the thesis, not just illustration.

---

## Interactive Maps

### 6. The Silk Road Corridor
Terrain base showing why those specific routes — the funnels, fans, and Pamir Knot visible in topography. Trade routes overlaid. The geography makes the routes obvious before you draw them.

**Analytical question:** Why these routes and not others?

### 7. The Parallel Conquests
Split screen or overlay: American West and Russian steppe, same decade (1860s-1880s). Railroad lines advancing. Territory changing control. Same pattern, opposite sides of the planet.

**Analytical question:** How similar were these two independent processes?

### 8. Soviet Border Drawing
Central Asian borders overlaid on ethnic/linguistic distribution. The deliberate mismatch visible — borders that ignore terrain and ethnic boundaries.

**Analytical question:** Do these borders follow geographic or ethnic logic, or neither?

### 9. The Aral Sea Timeline
Before/after satellite imagery with timeline slider. The rivers diverted. The lake disappearing. The toxic salt flat expanding. Possibly the most powerful single image in the book.

**Analytical question:** What happens when you override a geographic system with more complexity than your model accounts for?

### 10. The Nile/Amazon/Volga Triptych
Same scale, three rivers. Terrain, climate zone, and outlet connectivity visible. Three different rivers, three different outcomes, all predictable from the geographic variables.

**Analytical question:** Why did the Nile build a civilization and the Amazon didn't?

### 11. The Inca Vertical Supermarket
Andes cross-section showing altitudinal zones — potatoes, maize, coca, tropical fruits stacked within a day's walk. The mountain range as rotated river valley.

**Analytical question:** How does vertical resource density substitute for horizontal river distribution?

### 12. The Universal River Settlement Gradient
Stylized river cross-section from headwaters to delta with settlement density curve overlaid. Headwaters = high energy, erosive, sparse (chokepoints only). Middle = moderating, early settlement. Floodplain = depositional, dense agriculture, cities. Delta = maximum fertility, highest density. Applicable to every major river civilization simultaneously.

**Analytical question:** Does energy dissipation rate predict settlement density along any river?

---

## Design Principles

- Every visualization answers a specific analytical question statable in one sentence
- The terrain base layer is persistent across all maps — the geography doesn't move, everything else does
- Graphs show distributions, not narratives — if it's a timeline of events, it's not doing enough work
- If a visualization is decorative rather than analytical, cut it (color-is-a-smell applies to visuals too)
- Tech stack TBD but candidates: Leaflet.js / MapLibre for maps, D3.js for graphs, GeoJSON for boundaries
