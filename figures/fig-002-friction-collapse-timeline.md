---
id: fig-002
title: "Friction Collapse Timeline"
type: graph
implementation: python
status: concept
chapter: 1
---

## What It Shows
Effective geographic friction as a function of time, with technology events marked as step-change drops. Long stable plateaus with sudden drops — the punctuated equilibrium model rendered as a curve.

## Why It Matters
Makes the punctuated equilibrium visible. The reader sees that geographic constraints held for millennia, then reset in decades. The "long stable, sudden break" pattern is the thesis in visual form.

## Data Sources
- Timeline is historical (known dates of technology adoption)
- Friction levels are illustrative/argued, not measured
- Honest about this: relative positions are defensible, absolute scale is conceptual

## Implementation Notes
- Python: matplotlib
- X-axis: time (roughly 3000 BCE to present)
- Y-axis: "effective geographic friction" (qualitative scale)
- Step-function drops at: sail (~1500 BCE for Phoenicians? or Age of Exploration), gunpowder (~1400s), telegraph (~1840s), railroad (~1860s), internet (~1990s)
- Long flat plateaus between drops
- Annotations at each drop naming the technology and what friction it collapsed
- Possibly shade regions: "geography holds" (plateaus) vs. "distribution resets" (drops)

## Sketch
```
Friction
  ▲
  │ ████████████████████████████████
  │                                 █
  │                                 █████████████
  │                                              █
  │                                              ████████
  │                                                      █
  │                                                      ██████
  │                                                            █
  └──────────────────────────────────────────────────────────────→ Time
        Ancient     Sail    Gunpowder  Telegraph  Railroad  Internet
        empires                                    
```
