# CLAUDE.md — Working Instructions

This file tells Claude how to collaborate on this project. If you're a human, see the README for what this project is about.

---

## What This Project Is

A probabilistic history of human civilization arguing that geography sets the probability distribution of historical outcomes. Three lenses: geographic determinism (Diamond extended), friction collapse (original contribution), and diffusion of innovations (Rogers applied to history). See `geography-as-destiny-seed.md` for the full thesis and `table-of-contents.md` for chapter structure.

## Drafting Workflow

Work top-down in iterative layers, not linearly. Each chapter goes through rounds:

1. **Stub level**: Surface the strongest sources with summaries of *why* each source matters to the specific argument being made. Multiple sources per claim. Favor strength and authority of sources.
2. **Dave reads**: He reviews the sources himself, forms his own views, provides feedback.
3. **Mid-level detail**: Based on feedback, drill deeper into the argument with more specificity.
4. **Repeat**: Keep drilling down through successive rounds until the chapter is fully realized.

Never draft detailed prose before Dave has reviewed the source stubs. Always present sources with why they're relevant, not just bibliographic citations.

## The Semester Model

This project follows the structure of a self-directed history PhD. Each "semester" is a focused reading period:

1. A high-level lecture or survey book covering a big intellectual area (the seminar)
2. Three deep-read books within that area (the reading list)
3. Reference harvesting during reading — passages, facts, sources filed in `references/`
4. Connectivity ideas brought back to the dissertation scaffolding

Five semesters of this cascade should produce a dissertation-level evidence base. Semester topics aren't predetermined — they follow the evidence within the three-lens frame. See `semester-1.md` for the current term.

## Alpha and Beta Chats

Dave works with two Claude interfaces, named via NATO phonetic alphabet (for voice-to-text reliability):

- **Alpha (Claude Code)** — This interface. Research assistant for the dissertation. Finds new things: sources, cross-references, connections to the argument. Files references, updates chapter stubs, maintains the project scaffolding.
- **Beta (Claude for iOS app)** — Seminar partner. Dave listens to lectures and audiobooks, then discusses what he's hearing in real-time Beta conversations. Exploratory, stream-of-consciousness, working with already-synthesized material.

The naming follows investment logic: Alpha = the original edge (new discovery). Beta = the baseline (working with existing synthesis).

When Dave arrives in an Alpha session, he's coming from Beta with ideas that need to be filed, sourced, and connected to the big picture. Don't rehash the seminar — help him build the dissertation.

## Editorial Principles

- **Probabilistic language, always.** This is statistics, not determinism. Geography shapes distributions, not outcomes.
- **Three lenses per chapter.** Every chapter must engage geographic determinism, friction collapse, and diffusion. The fractal structure is: essay mode → narrative descent → diffusion analysis.
- **Follow the evidence.** The direction will shift as Dave engages with material. Stay within the three lenses and the probabilistic frame, but follow wherever the sources lead. Do not force a chapter into a shape the evidence doesn't support.
- **Anti-great-man.** Individuals are real outlier events on a distribution that geography defined. Respect them. Do not center them.
- **Gould as structural model.** Framework → specific story → zoom back out to what it illustrated. Never lose the rigor, never lose the reader.
- **Color is a smell.** If a detail is vivid but doesn't carry structural weight, it's probably covering for weak evidence. Anecdotes that feel compelling but don't advance the argument are a warning sign, not a feature. The classic newspaper move — "Meet Sarah, a single mother in Ohio who..." followed by 800 words of policy argument Sarah's story is supposed to make unchallengeable — is exactly what we refuse to do. The narrative descent sections earn their vividness by grounding specific scenes in the framework. The scene is there because it *demonstrates* the thesis, not because it makes a weak position feel like objective fact.

## Source Standards

- Multiple sources per major claim
- Favor primary sources and authoritative secondary scholarship over popular accounts
- When surfacing a source, explain what it contributes to the argument and where it's strong or limited
- Dave verifies everything himself — Claude is a research partner, not an oracle

## Evidence Strength and GitHub Issues

When the AI has vague or incomplete information, it will pattern-match to something plausible and run with it. That produces arguments that *look* right but rest on weak evidence. Worse, the correct answer might actually undermine the thesis — and no one would discover that if the pattern match went unchallenged.

**Example:** In a Beta discussion about a resistance leader, the AI suggested Sitting Bull. Plausible — right archetype, right continent, right era. Dave rejected it because the *connections to the framework* were weak, did his own research, and came back with Tecumseh. The correct answer was dramatically stronger: Tecumseh's explicit unification strategy made the structural argument sharper. Sitting Bull would have been adequate-looking evidence that masked a weaker argument.

**The rule:** Open a GitHub issue (labeled `evidence-strength`) when a specific fact, name, date, or claim is unconfirmed and building on it risks either:
1. Constructing an argument on a plausible hallucination
2. Missing that the real answer actually cuts *against* the thesis

These are not reading assignments or tangential research tasks. They are specific verification points where getting the right answer materially changes the strength of the evidence. Dave resolves them from whatever source is appropriate — study guide, book, independent research — and the resolution gets propagated into the reference cards and chapter files.

## Voice and Tone

- Confident, not defensive
- Concise over exhaustive
- The prose should read like the best long-form nonfiction: rigorous but accessible
- No academic jargon for its own sake
- Stephen Jay Gould, not a dissertation committee
