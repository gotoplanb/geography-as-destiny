-- print-endnotes.lua
-- Print build only: turn the book's footnotes into per-chapter endnotes.
-- The preamble does \let\footnote\endnote and defines \flushnotes (which
-- prints the accumulated endnotes under a "Notes" heading and resets the
-- counter, or does nothing if the section had no notes). This filter drops a
-- \flushnotes just before every top-level heading (so each section's notes
-- print at its end) and once more at the very end for the final section.
-- Latex/PDF output only; the epub build does not use this filter.

function Pandoc(doc)
  if not (FORMAT:match 'latex') then return doc end
  local out = {}
  local seen = false
  for _, b in ipairs(doc.blocks) do
    if b.t == 'Header' and b.level == 1 then
      if seen then
        table.insert(out, pandoc.RawBlock('latex', '\\flushnotes'))
      end
      seen = true
    end
    table.insert(out, b)
  end
  table.insert(out, pandoc.RawBlock('latex', '\\flushnotes'))
  doc.blocks = out
  return doc
end
