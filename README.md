# Geography as Destiny
### A Probabilistic History of Human Civilization

Geography doesn't determine history. It sets the probability distribution.

Rivers build states. Mountains prevent them. Chokepoints create contests. And every few centuries, a technology collapses the friction that made those geographic constraints matter — the railroad, the firearm, the internet — and the entire distribution resets.

This book argues that framework across eight chapters, from the Nile to the Silk Road to a pair of parallel conquests that happened simultaneously on opposite sides of the planet, driven by the same technology, against the same kind of culture, with neither side aware of the other. That's not coincidence. That's geography.

## How this is being made

The obvious question: is a human-AI collaboration legitimate scholarship?

The short answer is that this project follows the same process a PhD candidate would use — because one of the authors has already been through a doctoral program and knows what rigor actually requires. The tool changed. The process didn't.

### The semester model

The project is structured as a self-directed doctoral program. Each "semester" follows a repeating cascade:

1. **A survey lecture or book** covering a major intellectual area — the equivalent of a graduate seminar. The human listens, takes notes, discusses in real time with an AI conversation partner.
2. **Three deep-read books** chosen to support, challenge, and extend what the lectures cover. The human reads these. Not skims. Not summarizes. Reads, highlights, and annotates.
3. **Reference harvesting** — specific passages, facts, places, and data points are filed as individual notes, the way a grad student fills index cards. These become the footnotes and endnotes later.
4. **Dissertation scaffolding** — connectivity ideas that emerge from reading are brought to the AI research assistant (a different interface, optimized for structural work) to be filed into chapter stubs, cross-referenced with other sources, and connected to the argument.

Five semesters of this cascade — each covering a different intellectual area, each building the evidence base for specific chapters — should produce a dissertation-level artifact.

The human does the reading. The human forms the interpretations. The human makes every editorial decision. The AI accelerates retrieval, surfaces sources, maintains the organizational scaffolding, and helps identify connections across a wider body of scholarship than any individual could hold in memory. This is what research assistants and librarians have always done. The tool is faster. The dynamic is the same.

### What's in the repo

#### Drafts in progress
- **[`prologue.md`](prologue.md)** — On method: the river metaphor, the R-squared framing, Shannon, and why human-AI collaboration is scholarship *(draft — in review)*
- **[`chapters/01-the-distribution/index.md`](chapters/01-the-distribution/index.md)** — Chapter 1: the three lenses, the great man reframe, falsifiability, and the Parallel Conquests preview *(draft — in review)*
- **[`chapters/02-the-river-spine/index.md`](chapters/02-the-river-spine/index.md)** — Chapter 2: the thermodynamic river model, settlement gradient, Goldilocks zone, class structure *(draft — in review)*
- **[`chapters/03-the-chokepoint/index.md`](chapters/03-the-chokepoint/index.md)** — Chapter 3: position not wealth, the pulsing frontier, chokepoint economy, peace through irrelevance *(draft — in review)*
- **[`chapters/04-the-silk-road/index.md`](chapters/04-the-silk-road/index.md)** — Chapter 4: relay network not road, friction filter, maritime corridor, climate pulse, Sogdians *(draft — in review)*
- **[`chapters/05-the-islamic-diffusion/index.md`](chapters/05-the-islamic-diffusion/index.md)** — Chapter 5: Islam's two curves, Manichaeism as contrast case, boundaries as load-bearing *(draft — in review)*
- **[`chapters/06-the-parallel-conquests/index.md`](chapters/06-the-parallel-conquests/index.md)** — Chapter 6: the flagship chapter — horse as friction collapse quantified, bilateral deficit, Why No Dunhuang, the orthogonal rotation, Atlantic parallel *(draft — in review)*
- **[`chapters/07-the-great-mans-hardest-test/index.md`](chapters/07-the-great-mans-hardest-test/index.md)** — Chapter 7: Genghis as norm enforcer, four-khanate natural experiment, Timur as budget mechanism *(draft — in review)*
- **[`chapters/08-the-synthesis-frontier/index.md`](chapters/08-the-synthesis-frontier/index.md)** — Chapter 8: the correction loop, holdout validation, canal vs. river, process as evidence *(draft — in review)*

#### Project scaffolding
- **[`geography-as-destiny-seed.md`](geography-as-destiny-seed.md)** — The original seed document, captured via voice-to-text on a walk in Gainesville, FL
- **[`table-of-contents.md`](table-of-contents.md)** — Full chapter structure with summaries
- **[`dissertation-proposal.md`](dissertation-proposal.md)** — Formal proposal submitted to Charlie (committee advisor)
- **[`collaboration-roles.md`](collaboration-roles.md)** — How Dave, Alpha, Beta, and Charlie work together
- **[`visualizations.md`](visualizations.md)** — Planned graphs, distributions, and interactive maps

#### Semester materials
- **[`semester-1.md`](semester-1.md)** — Completed: Tasar's Central Asian history, Morrison, Starr, Hämäläinen
- **[`semester-2.md`](semester-2.md)** — Next: Hansen's Silk Road, Frankopan, Starr, Rogers

#### Research
- **[`chapters/`](chapters/)** — Chapter stubs with source references, argument scaffolding, and working notes
- **[`literature-review/`](literature-review/)** — One file per source: what it argues, what we use it for, key excerpts, limitations, and connections
- **[`references/`](references/)** — 33 harvested reference cards filed during semester 1
- **[`CLAUDE.md`](CLAUDE.md)** — Working instructions for the AI collaborator

## Challenge the evidence

This project claims its thesis is falsifiable. Here's where you test that.

If you find weak evidence, a stronger counter-argument, a misidentified source, or a case where geography clearly *doesn't* explain the outcome — [open an issue](https://github.com/gotoplanb/geography-as-destiny/issues). That's not a bug report. It's how scholarship works.

A core risk of human-AI collaboration is that the AI pattern-matches to something plausible and the human accepts it because it *looks* right. We've already caught this happening during our own process — the AI suggested one historical figure, the human rejected it because the *connections to the argument* were weak, did independent research, and found a different figure that made the evidence dramatically stronger. The right answer changed the shape of the argument. The wrong answer would have hidden that.

We use the `evidence-strength` label for these. You don't need to add the label yourself — just open the issue. Tell us what's weak, what's wrong, or what we missed. We'll take it seriously because the whole point of probabilistic reasoning is that you have to name the conditions under which you'd be wrong.

If you can break the thesis, the thesis deserved to break.

## Run your own committee review

This project uses an AI committee advisor (Charlie) for adversarial evaluation of each draft. The full review protocol — role definition, core claims, review instructions, issue tracking, and review history — is in **[`charlie-prompt.md`](charlie-prompt.md)**.

If you want to replicate the review process yourself:

1. Open a new Claude session (Opus 4.6 or later, with extended thinking if available)
2. Paste the contents of [`charlie-prompt.md`](charlie-prompt.md) as the system prompt
3. Provide the chapter text — either pasted directly or via a commit-pinned GitHub URL (use the full commit hash, not `main`, to avoid caching)
4. Charlie will verify closed-issue resolutions, assess open issues, and flag new weaknesses

The prompt is a living document that gets updated after each review cycle. It carries the full project context — what's been resolved, what's still open, what previous reviews found. A fresh Claude instance with this prompt and the chapter text has everything it needs to do a rigorous committee review.

Anyone can play committee advisor. If your review finds something ours missed, [open an issue](https://github.com/gotoplanb/geography-as-destiny/issues).

## Status

All eight chapters drafted. 120+ reference cards harvested. Five committee reviews completed. The framework has been tested across six continents, multiple millennia, and the hardest cases available — including Genghis Khan as the great man stress test. Tentative final draft submitted for review.

---

Open access. No institutional affiliation. No paywall. If three anthropology students find it useful, that's enough.

*Dave Stanton & Claude (Anthropic), 2026*
