# Changelog

Version history for *Geography as Destiny*. Each version corresponds to a git tag and a built epub. The colophon and title page of the epub display the version that built them.

## v3.1 — 2026-05-17

**Reader-onboarding apparatus added: foreword popovers + Appendix C "Intellectual Lineage."**

The foreword's name-drops (Shannon, Rogers, Diamond, Anthony, Gimbutas, Kurgan hypothesis, Yamnaya, Sintashta, DOM2, Pontic-Caspian steppe, Librado et al. 2021, propaganda research, human factors, anti-eugenics, social constructionism) were a barrier for new readers who had not encountered these figures and theories before. Two-tier solution added:

1. **Brief popover footnotes in the foreword** (13 new `[^fwd-NN]` notes) — each is a ~80–120-word explainer that pops up on tap in the epub, giving enough orientation to keep reading without breaking flow. Each ends with "See Appendix C."
2. **New Appendix C: Intellectual Lineage** — 9 longer entries (~300–500 words each) covering Shannon & Information Theory; Rogers & Diffusion of Innovations; The Propaganda Research Tradition; Diamond & Continental Geography; Gimbutas & the Kurgan Hypothesis; Anthony & the Pontic-Caspian Archaeology; Yamnaya, Sintashta & DOM2 (bundled); Human Factors & Usability Research; Anti-Eugenics & Social Constructionism. Arranged in the order names appear in the foreword.

Wired into `build-epub.sh` and `table-of-contents.md`. Minor bump (not patch) because this is substantive content addition that meaningfully expands the book's surface area, not a typo or correction.

---

## v3.0.1 — 2026-05-14

**Foreword polish.**

Three targeted foreword changes:

1. **Hard-coded durations removed.** The project is a continuous evolution; the git log preserves exact dates for anyone who wants them. "Twenty years before the first word was written" → "long before the first word was written"; "Two decades of building" → "Years of building"; redundant "twenty years of usability and human factors research" references → "professional usability and human factors research"; "a month of walks in Gainesville and New Orleans" → "listening, talking, writing, and walking — audiobooks ranging from Central Asian history to Comanche expansion, conversations with an AI research partner, and the streets of Gainesville and New Orleans while the ideas connected."
2. **Card-count framing reworked.** "More than a hundred reference cards" replaced with explanation of what the cards do plus current count: "Each synthesis, connection, and framework move is recorded as a reference card — the research lineage and its history preserved alongside the prose. The card count is currently 208 and growing."
3. **Long theory paragraph broken up.** Single dense block split into seven shorter paragraphs at natural logical breaks (opening / Diamond / Gimbutas-Anthony-Librado / Rogers-Shannon / UX foundation / anti-eugenics-social-constructionism / closing one-liner). Previously rendered as one continuous block of text filling an entire iPhone screen in the epub.

---

## v3.0 — 2026-05-13

**Bronze Age substrate restructured around two-friction-collapse framework.**

Major framework restructure triggered by Librado et al. 2021 (*Nature*) ancient DNA redating of modern domestic horse lineage (DOM2) emergence to ~2200 BCE, superseding Anthony 2007's ~4000 BCE horse-domestication anchor.

### Framework moves articulated

- **Two friction collapses on the Pontic-Caspian steppe.** Wagon-driven Yamnaya expansion (~3300 BCE) and DOM2+chariot Sintashta horse-cavalry emergence (~2200 BCE). The "Big Bang" vocabulary retired as poetic stretch — actual pattern is intensification with compressing intervals, not energy dilution from an originating event.
- **State-dependent climate forcing.** Same forcing event produces opposite responses depending on pressure-system state (charging vs overextended) AND simultaneously produces intra-system concentration + inter-system convergence when each end holds distributed critical resources.
- **Friction-collapse intensification.** Intervals compress monotonically across the sequence: wagon → DOM2-chariot 1100 years; DOM2 → sail 3700 years; sail → industrial 350 years; industrial → internet 150 years; internet → AI 30 years. Disruption grows because multipliers compound (mobility, communication, now cognition) rather than substitute.
- **BMAC as Bronze Age structural equivalent of the later Silk Road's Transoxianan node.** Recursive structural parallel principle: same terrain produces gravity-well nodes whenever multi-system trade conditions converge.
- **Locational identity vs ethnic/lineage identity** as distinct organizing principles. Bactria-across-four-millennia as canonical case: BMAC → Achaemenid → Hellenistic → Kushan → Sasanian → Samanid → Bukharan → Soviet → present. Locational substrate persists; political vocabularies change.
- **Diamond/Anthony/framework triangulation.** Diamond gives continent-scale orientation; Anthony gives regional terrain refinement; the framework gives sub-regional systematic apparatus operating where specific features (friction sieves, gravity wells, river-spine corridors, choke points, pressure-system geometry) matter. River-delta diffusion analogy replaces the wave-front model.

### Cards added or substantially revised

184 (calibration warning), 196 (calibration warning), 197 (calibration warning), 198 (Maykop relay node), 199 (wagon and Big Bang conjunction — strengthened reading), 200 (UX foundation / four-stage mechanism), 201 (kurgan access restriction), 202 (frontier-management institutional stack), 203 (Sintashta inversion), 204 (two friction collapses), 205 (friction-collapse intensification), 206 (BMAC as Bronze Age Silk Road node), 207 (locational identity vs ethnic identity / Bactria), 208 (Diamond-Anthony-framework triangulation).

### Heavy inspection of all 208 cards

8 high-severity factual errors corrected with calibration updates (cards 006, 009, 167, 172, 181, 185, 187, 188). Categorical diagnosis showed none undermined the framework: one framework refinement (card 181 — multi-origin bronze), one wrong-evidence-for-valid-point (card 009 — winter steppe not desert), rest sloppy facts the framework didn't depend on. Calibration discipline established mid-arc to prevent future overreach.

### Prose changes

- **Foreword.** Intellectual lineage paragraph expanded from five to six traditions (UX/usability foundation added explicitly). Diamond/Anthony positioning made explicit. Horse-domestication reference updated to two-friction-collapse structure.
- **Chapter 1.** Section II extended with framework's specific-terrain-feature toolkit. Section III temporal-scope paragraph rewritten around two-friction-collapse structure with intensification principle articulated.
- **Bronze Age substrate interlude.** Section II rewritten as "Two Friction Collapses." New Section VI on Sintashta and the DOM2 horse. Tocharian Bridge (Section VIII) updated for layered descent per Zhang et al. 2021 aDNA. Long Way Home (Section X) extended with locational identity arc closure.
- **Chapter 4 (Silk Road).** Transoxiana description extended with BMAC as Bronze Age predecessor on the same Zeravshan corridor. Sogdians section extended with four-millennium locational identity continuity.

### Closing observation

Closes the Tasar-Anthony arc that opened in semester 1. The river ran from Eren Tasar's *Crossroads of Civilization* audiobook through David Anthony's Bronze Age steppe archaeology and arrived at the same place. Bactria was always the answer.

---

## v2.4 — 2026-05

**Three-phase PIE crystallization + Tocharian river-spine integration.**

Cards 196 and 197 integrated into Bronze Age substrate interlude. Section III treats the three-phase sequence (federation crystallization → power explosion → simultaneous expansion) with the lingua-franca-during-federation timing claim. Section VII treats the river-spine logic on both ends of the Tocharian story — the Irtysh enabling the eastward leapfrog, the Syr Darya enabling the eventual reconnection to the Silk Road.

*(Subsequently superseded by v3.0's two-friction-collapse restructure; calibration warnings added to cards 196 and 197 during v3.0 inspection pass.)*

## v2.3 — 2026-05

Koryos institutional mechanism (card 195) integrated into Bronze Age substrate interlude. The PIE-era youth-warrior-band institutional vocabulary as parallel evolution case to the Comanche confederation four thousand years later — the framework's strongest single confirmation type.

## v2.2 — 2026-04

Anthony reading arc continuation: pressure-differential threshold mechanism (card 194), Old Europe collapse as pressure-reversal signature, four-phase frontier lifecycle articulation.

## v2.1.2 — 2026-04

Epub displays its own version. Title page date field and back-matter colophon both display the version that built the epub.

## v2.1.1 — 2026-04

Build artifact cleanup + ch4-11 footnote orphan fix.

## v2.1 — 2026-04

Integrate Anthony-arc cards 180-187 plus figure 015 (tidal vs breaking wave pressure systems). Bronze Age substrate interlude established between Chapter 1 and Chapter 2.

## v2.0 — 2026-04

**Anthony arc integration.**

Major restructuring incorporating ~30 cards from the Anthony reading arc: robust frontiers as central organizing concept, temporal scope precision (pre-horse vs post-horse dynamics), Bronze Age substrate as analytical case, methodology articulation (theoretical-experimental physics analogy, Saussure mode for falsifiable predictions, Rosetta Stone receiver-side inference for pre-documentary periods).

## v1.3 — 2026-03

Chapter 6 convergence integration; Comanche collapse mechanism complete with conjunction logic (encoding shift + capacity recovery in same window).

## v1.2.1 — 2026-03

Appendices moved to chapters/ folder for structural consistency.

## v1.2 — 2026-03

**Complete book with appendices — all sections written.**

Prologue + 8 chapters + 2 appendices. All statuses: complete.

## v1.1 — 2026-02

All Charlie v1.0 feedback addressed except one remaining item.

## v1.0.1 — 2026-02

Fix pass complete — 11 of 13 issues from Charlie's v1.0 review resolved.

## v1.0-draft — 2026-02

**Tentative final draft — all eight chapters complete.**

Eight chapters + Prologue + Epilogue concept. 120+ reference cards.

## v0.6.1 — 2026-02

Charlie v0.6 feedback saved — five issues, none structural. Fifth committee review complete.

## v0.6 — 2026-01

**Semester 2 complete — Hansen integrated, all 97 cards synthesized.**

Full integration pass: all reference cards mapped against all chapter content.

## v0.5 — 2026-01

Semester 2 milestone — Charlie satisfied, one issue remaining. Four rounds of committee review completed.

## v0.4.1 — 2026-01

All v0.4 committee issues resolved except Timur and SRTM items.

## v0.4 — 2026-01

Six chapters drafted, 78 cards, Ch. 6-7 awaiting source reading.

## v0.3.1 — 2025-12

Five committee issues resolved in Ch. 1 revision.

## v0.3 — 2025-12

**Chapter 8 drafted — process methodology chapter.**

Three chapters now drafted: Prologue, Ch. 1 (The Distribution), Ch. 8 (The Synthesis Frontier).

## v0.2.2 — 2025-12

Chapter 1 methodology upgraded with holdout validation. Section IV revised: framework generates predictions and tests them.

## v0.2.1 — 2025-12

Full Charlie verbatim feedback captured.

## v0.2 — 2025-12

Chapter 1 and Prologue reviewed by committee advisor. Charlie's verdict: "This is a dissertation. Finish it."

## v0.1 — 2025-11

**Semester 1 complete.**

Prologue and Chapter 1 drafted with 37 endnotes. 34 reference cards.
