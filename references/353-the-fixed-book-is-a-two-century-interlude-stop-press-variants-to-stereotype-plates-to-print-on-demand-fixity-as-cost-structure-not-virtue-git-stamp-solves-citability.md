# The Fixed Book Is a Two-Century Interlude — Stop-Press Variants → Stereotype Plates → Print-on-Demand / Fixity Was a Cost Structure, Not a Virtue / The Git Stamp Already Solves Citability Better Than the ISBN Does

**Source:** Dave, 2026-11-02, from a working discussion about whether to push patch and minor releases to KDP. His instinct: "it kind of feels like we shouldn't move a printed version much... that's kind of the point, is that it's kind of fixed in time" — immediately followed by the suspicion that this is inherited bias rather than a reason.
**Type:** connection / framework applied to the project itself
**Relevant to:** Chapter 11 (The Synthesis Frontier; process as evidence), card 350 (fixed borders as a friction-collapse product), card 347 (monuments as compression), the Releases and Publishing policy in CLAUDE.md

## The claim

The fixed, identical book is not a property of books. It is a roughly two-century interlude between two friction regimes, and we mistook the interlude for the nature of the thing.

**Before — the hand-press, variable by default.** Printers corrected type *during* the run. The press kept going with uncorrected type while the proofreader worked, because pressmen would otherwise sit idle and paper was far too expensive to discard; when corrections were ready the press stopped, the type was fixed, and the run continued. The corrected and uncorrected sheets were then bound together indiscriminately. The result is that **each of the 235 surviving copies of the Shakespeare First Folio is unique.** The canonical fixed artifact of English literature was never fixed. The economics of paper and idle labour produced variance, and nobody treated it as a defect.

**During — stereotype plates, fixity as a side effect.** From the early nineteenth century, stereotyping let a printer store plates and reprint without resetting type, which collapsed the cost of an identical reprint. But correcting a stereotype meant *replacing the whole plate*, so errors persisted across printings, and by the 1830s the plates were capital investment in their own right. Reprinting became cheap and correcting became expensive. **Fixity was the output of that asymmetry, not a decision anyone made about what a book should be.**

**After — print-on-demand, variable again.** Both costs collapse. There is no plate, no run, no warehouse. Revision costs what the edit costs.

So the arc is variable → fixed → variable, and the norms we inherited were formed in the middle. "Books are set in stone" looks like a value and is an artifact of what used to be expensive.

## Why this matters here

**It is the book's own thesis applied to the book's own distribution**, which is a place the argument has not been pointed before. It is the same move as card 350: an institution that feels natural and permanent — the policed border there, the fixed edition here — turns out to be what a particular cost structure made affordable, bracketed on both sides by regimes that did it differently. Card 347 is a third instance with monuments. Three cases is the point at which this stops being an observation and becomes a pattern worth naming: **apparently natural institutions are frequently frozen cost structures, and friction collapse is what unfreezes them.**

**It also disposes of the weak argument for fixity.** The usual defence is that readers should be able to discuss the same artifact. Dave rejects this and is right to: readers bring their own biases and lived experience, the processing differs regardless, and nobody worries that the hardback and the paperback paginate differently.

**The strong argument is citability, and this project already solved it.** What fixity actually buys is that "Stanton, p. 203" means something checkable — which matters for a book deliberately built as a dissertation, since citation is what scholars do with one. Traditionally the ISBN is the handle. But the copyright page here stamps the git version and commit (*built from version v5.2.1-14-g3293c2d*), so any physical copy is identifiable to the character: check out that tag and you have exactly what the reader is holding. That is a finer-grained and more verifiable identity than an ISBN can provide, and it was built before there was a reason to need it.

## The rule this implies

With citability handled by the version stamp, the only remaining constraint is **pagination, not content**. A citation to p. 203 survives any correction that does not reflow the page.

- **Pagination stable → corrected printing.** Same ISBN, new version stamp, upload as often as is worth the review cycle. This is Dave's "minor variants in the wild" idea and it works.
- **Pagination moves → new edition.** New ISBN, major version, stated on the copyright page.

Which is what printers have always done, with corrected reprints against new editions — arrived at here from a different direction. It also means the page-count check already in the publishing policy is doing double duty: the event that invalidates the printed cover and the event that breaks citations are the same event.

## To verify before acting

KDP's own threshold for when a content change requires a new listing rather than a file update has not been checked. The convention above is the publishing-industry one; confirm KDP's wording before relying on it.

## Status

Not for the book, though it is the one card so far whose subject is the book's own production. A candidate for the website, or for a future edition of Chapter 11, which already argues that process is evidence — this would be the production process making the same argument about itself.
