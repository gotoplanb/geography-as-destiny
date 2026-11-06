# Scholarship in Both Directions — Reader Release Notes Diff the *Argument*, Not the Text / A Periodic, Claim-Indexed Literature Sweep / The Versioned Book as Method

**Source:** Dave, Alpha session, 2026-11-06, reflecting on the research process after a day of verification passes (cards 363–365). Three linked ideas:
1. Citing specific commits, rather than a locked print edition, is an innovation in itself.
2. At each new version, readers could get a short release document instead of having to reread the book and work out what changed. It is something like errata, possibly organized by chapter.
3. Every few months, a detailed research sweep could check recent scholarship against the cards and framework, because finding new work by string matching and citation webs is slow and incomplete.

He frames it as two ways scholarship changes because of this book: **how the author updates readers**, and **how the field updates the author**, including which of his ideas need challenging.
**Type:** process journal / method. Same family as cards 027, 034, 050 and 101.
**Relevant to:** Chapter 11 (the public-repository passage and the reproducibility argument), cards 027 (AI as friction collapse for scholarship), 033 (Shannon receiver side), 154 (citation incentives as a sender-side bias), 229 (framework production conditions), 356 (the project as its own measurement apparatus), 365 (Rogers' pro-innovation bias); CHANGELOG.md; the release rules in CLAUDE.md

## What already exists, and what is new

**Chapter 11 already claims the first half.** It says the whole process is in a public repository, so a reader can trace a claim from seminar to card to endnote, and argues that this is better practice because it makes errors detectable. What it doesn't say is what happens *after* publication. A fixed edition freezes the argument; a versioned book keeps changing it. The two new pieces are the channels that carry those changes **out to readers** and **in from the field**.

**CHANGELOG.md is the author's ledger, not the reader's.** It records page counts, spine widths and KDP status, which are things the author needs to ship. A v6 reader needs something else: *which of the beliefs the book gave me should I now hold differently?* The v6.0.1 entry is already halfway there ("The argument is unchanged; only its dating was wrong"). That sentence is the reader-facing content. The rest of the entry is production detail.

## Outbound: reader release notes

**Diff the argument, not the text.** A text diff (redline) tells a reader which sentences moved. That is sender-side information: it reports what the author did. The receiver-side version (card 033) reports what changed in the claims. Each entry carries the claim, the change, and why:

| Change type | Meaning for a returning reader |
|---|---|
| **Corrected** | The fact was wrong; the argument stands (v6.0.1's 1871 belting date) |
| **Strengthened** | New evidence supports the claim more tightly |
| **Narrowed** | The claim survives in a smaller form (card 323's Younger Dryas kernel; card 306's Baltic contrast) |
| **Weakened or withdrawn** | Stop relying on this. **This is the most valuable row, and the one authors least like to publish** |
| **New** | Added material (v6.0.2's Appendix A entry 21) |

**Semver already tells readers how much to read:**
- **Patch:** nothing to reread; the notes are enough.
- **Minor:** read the new sections.
- **Major:** the structure moved, so the notes give a route back in.

This uses the project's existing release rules as a reading guide rather than inventing a second scheme.

**Precedents, so the claim is calibrated:**
- Revised academic editions often carry a "new to this edition" preface, so the idea isn't unprecedented.
- Corrections have names: *errata* or *corrigenda* for corrections, *addenda* for additions.
- Software release notes and the "changes since the previous version" sections in internet-standards drafts are the closest structural models.

What is new here is the combination:
- per-claim granularity;
- every entry linked to the commit, issue or card that produced it;
- a typed change (above), so a reader can filter by "what got weaker";
- releases often enough that the notes stay short.

**It can be generated, not written from scratch.** The raw material already exists between any two tags:
- the git log;
- closed `evidence-strength` issues;
- card status lines ("superseded by", "verified", "withdrawn");
- the CHANGELOG.

A draft can be assembled from these and then edited. The editing is the part that needs judgment: deciding which changes move a belief.

**Citability is solved by tags.** The standing objection to living texts is that no one can cite a moving target. A tag is an edition: "*Geography as Destiny*, v6.0.0" is as fixed as a printed second edition, and a commit hash is finer than any edition has ever been. The innovation Dave named is the granularity, not citability itself.

**Each printed version stands on its own (Dave, 2026-11-06).** No version of the book carries release notes, diffs or belief-change context inside it. The diff, the belief changes and the trail of cards, issues and commits behind them live only in the digital version. They form a graph of nodes and edges, and a linear printed book can't represent one. Print is a snapshot of the argument. The repo is the argument's history.

**Print readers need a way in.** A paperback can't link. **Decided (Dave, 2026-11-06):** the printed book carries one stable URL for the release notes, in the colophon, and nothing more. Still to choose: the URL itself. It has to outlive any repo rename or site move, so it should be a redirect Dave controls, not a raw GitHub path. *(It would go in the next interior build that goes to KDP anyway. Don't make it a separate upload; see the release rules.)*

## Inbound: a periodic, claim-indexed literature sweep

**The old method searches by vocabulary.** Keyword alerts and citation chaining (who cited Scott, who cited Librado 2021) find work that uses your words or cites your sources. They miss work that bears on your claim in someone else's vocabulary. That is the same failure as the compass case (card 085): relevant material filed in a category you don't search.

**The new method searches by claim.** Each reference card already states a claim, usually with what would falsify it. A sweep can be organized around those claims rather than keywords:
- *"What has been published since [date] on whether canal-dependent states fared worse under the 4.2 ka event?"* (card 363, issue #38)
- *"New ancient-DNA results on the Baltic farming transition?"* (card 306)
- *"Has anyone dated the Huayuankou breach differently?"* (card 364)

**The precedent is the living systematic review.** In clinical medicine these are reviews updated continually as new trials appear (Elliott et al., "Living Systematic Reviews: An Emerging Opportunity to Narrow the Evidence-Practice Gap," *PLOS Medicine*, 2014; Cochrane now runs living reviews). *(Citation from memory; verify.)* This sweep is the same practice applied to a historical argument, with the reference cards serving as the review protocol.

**A sweep design** (proposal; not yet run):
- **Cadence:** quarterly, or before any KDP upload, whichever comes first.
- **Inputs, in priority order:**
  1. open `evidence-strength` issues;
  2. claims the published chapters lean on;
  3. cards marked "from memory; verify";
  4. the core authors' new work (Scott, Reich, Cunliffe, Librado, Anthony, Hämäläinen).
- **Search on mechanisms and cases, never on the book's coined terms.** No one else says "friction collapse" or "beneficiary mismatch," so searching for them returns nothing and creates false confidence.
- **Weight disconfirmation.** The sweep should ask "what cuts against this?" before "what supports this?" Rogers' pro-innovation bias (card 365) and the citation-incentive bias (card 154) are the failure modes it is guarding against.
- **Outputs:**
  - an `evidence-strength` issue for every finding that cuts against a claim;
  - card updates for findings that support or narrow one;
  - a line in the next reader release notes.
- **Every citation verified by DOI or publisher record before it is filed.** The search tool will produce plausible citations. Today's session caught two date discrepancies (Huayuankou, the *sinan*) only because both were checked against scholarly sources.

**The human filter stays.** Card 027's division of labour holds: the machine supplies retrieval breadth, Dave supplies the recognition filter. A sweep produces candidates. Deciding which ones challenge an idea is still Dave's job, and the Tecumseh correction (card 007) is the reminder of why.

## Why this matters

1. **The two channels are one pipeline.** The inbound sweep produces issues, issues produce patches, and patches produce release notes. The book's error-correction loop then runs past publication instead of stopping at it. Chapter 11's claim that process transparency "makes error detection possible" becomes a practice with a schedule rather than an affordance.
2. **The "weakened or withdrawn" row is the test of sincerity.** A book that publishes its own reversals in a form readers can find is doing what the framework asks of its sources: recording the uncertainty alongside the claim.
3. **It belongs in Chapter 11 at the next minor release, if anywhere.** As a description of method it would be new material, not a correction, so it is a minor release, not a patch. Charlie should see it first if it changes Chapter 11's argument.

## Open decisions (Dave's)

- Name and form: "release notes," "reader's errata," or a running "What changed" document? One document or one per chapter?
- Whether the first edition of the notes reconstructs v6.0.0 → v6.0.2 retroactively, or starts from the next release.
- Sweep cadence, and whether to run it as a scheduled agent or by hand at each release.

## Sources

- Chapter 11, the public-repository and reproducibility passages
- CHANGELOG.md (v6.0.1, v6.0.2 entries as models)
- J. H. Elliott et al., "Living Systematic Reviews: An Emerging Opportunity to Narrow the Evidence-Practice Gap," *PLOS Medicine* 11(2) (2014): e1001603 — *from memory; verify*
- Cards 027, 033, 034, 050, 085, 101, 154, 229, 356, 365, 007
