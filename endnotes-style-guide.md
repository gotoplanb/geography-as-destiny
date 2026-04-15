# Endnotes and Citation Style Guide

---

## Format

**Endnotes, not footnotes.** No page breaks in web-native markdown, so endnotes collected at the bottom of each chapter file. Markdown footnote syntax (`[^1]`) auto-numbers and links bidirectionally in most renderers (GitHub, Obsidian, Hugo, etc.).

## Citation Style

**Chicago Notes-Bibliography (17th ed.)** — the standard for history writing and the most readable for a general audience.

### First reference to a source
> Author First Last, *Title: Subtitle* (Place: Publisher, Year), page.

Examples:
```
[^1]: Alexander Morrison, *The Russian Conquest of Central Asia: A Study in Imperial Expansion, 1814–1914* (Cambridge: Cambridge University Press, 2021), 47.
[^2]: Pekka Hämäläinen, *The Comanche Empire* (New Haven: Yale University Press, 2008), 112–15.
[^3]: Claude Shannon, "A Mathematical Theory of Communication," *Bell System Technical Journal* 27, no. 3 (1948): 379–423.
```

### Subsequent references to the same source
> Last, *Short Title*, page.

Examples:
```
[^4]: Morrison, *Russian Conquest*, 203.
[^5]: Hämäläinen, *Comanche Empire*, 89.
```

### Audiobook / lecture series (no page numbers)
> Author, *Title* (Publisher, Year), lecture number or chapter title.

Example:
```
[^6]: Eren Tasar, *Crossroads of Civilization: A History of Central Asia* (The Great Courses, 2025), lecture 18.
```

## Reference Card Links

Beyond citing sources, endnotes should link to the reference card or working note where the idea developed. This shows the reader not just *what* was cited but *why* — the interpretive layer between the source and the argument.

### Format
After the citation, add: `See [card title](path).`

Example:
```
[^7]: Morrison, *Russian Conquest*, 312–18. The orthogonal rotation concept — the same terrain inverting its military function — emerged from connecting Morrison's logistics analysis with Schivelbusch's perceptual framework. See [The Orthogonal Rotation](chapters/06-the-parallel-conquests/notes.md).
```

```
[^8]: The eugenics reductio is not original to this book, but the specific formulation — that the geographic explanation is *necessary* rather than merely interesting — emerged from connecting Diamond's axis argument with the Plains nomadism case. See [ref 011](references/011-eugenics-reductio-and-thermodynamic-complexity.md).
```

### When to link to a card vs. just cite
- **Cite only** when the endnote is a straightforward source attribution (this fact comes from this book, page X)
- **Cite + card link** when the endnote involves interpretation, synthesis, or an idea that developed across multiple sources or discussions. The card shows the work.

## Discussion-Origin Notes

Some ideas in the book originated in Alpha or Beta discussions rather than from a published source. These still get endnotes, attributed to the discussion process rather than a citation:

```
[^9]: This formulation emerged from a seminar discussion while listening to Tasar's lecture on the Kazakh rebellions. The parallel between Kenesary Qasymov and Tecumseh was not drawn from any single published source but from the structural comparison developed in [ref 004](references/004-peter-tecumseh-mirror.md) and [ref 005](references/005-tecumseh-pattern-archetype.md).
```

This is the transparency the Prologue promises. The reader can see which ideas came from sources, which from synthesis, and which from the collision between the two.

## Practical Notes

- Endnotes go at the bottom of each chapter file under an `---` divider and `## Notes` header
- Number sequentially within each chapter (restart at 1 per chapter)
- Keep endnote text concise — the reference cards carry the full interpretive detail
- If a claim has no endnote, it's either common knowledge or it needs one. When in doubt, add the note.
