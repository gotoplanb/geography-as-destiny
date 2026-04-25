---
id: fig-012
title: "Cargo Capacity Across Plains Transportation Technologies"
type: graph
implementation: python
status: concept
chapter: 6
---

## What It Shows
Step function showing cargo capacity: dog+travois (75 lbs) → horse+travois (300 lbs) → railroad freight car (200,000 lbs). Logarithmic scale. Two discontinuous jumps — each a friction collapse.

## Why It Matters
Quantifies the two sequential friction collapses on the same terrain. The horse was a 4x multiplier that enabled the Comanche Empire. The railroad was a 670x multiplier that ended it. The visual makes the magnitude argument immediately: no institutional adaptation could bridge the second gap because it's categorically larger than the first.

## Data Sources
- Dog+travois: ~75 lbs (Hämäläinen, *The Comanche Empire*, Ch. 2 — exact page TBD)
- Horse+travois: ~300 lbs (same source)
- Railroad freight car: ~100 tons / 200,000 lbs (standard rail history)

## Implementation Notes
- Python: matplotlib
- Logarithmic y-axis (necessary — the range is 75 to 200,000)
- Three bars or step function with dates on x-axis (~pre-1700, ~1710, ~1870)
- Annotations: "4x" between dog and horse, "670x" between horse and railroad
- The gap between the second and third bars IS the argument

## Sketch
```
lbs (log)
200,000 ─                              ████
                                       ████  ← Railroad
                                       ████    (670x over horse)
                                       ████
    300 ─              ████            ████
                       ████  ← Horse   ████
                       ████    (4x)    ████
     75 ─  ████       ████            ████
           ████ ← Dog ████            ████
           ████       ████            ████
         ─────────────────────────────────────
         pre-1700    ~1710          ~1870
```
