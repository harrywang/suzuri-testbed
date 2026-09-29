# Minimap rendering check

Regression check for [suzuri#103](https://github.com/harrywang/suzuri/issues/103): the minimap drew live preview's links, bullets, and other inline widgets at full buffer font size, so each one overlapped the minimap rows around it and the top of the minimap turned into a smear of purple text. The minimap shares the main editor's display map, and the widgets used to read their size from settings instead of from the editor drawing them.

**How to run this check.** Turn the minimap on (`"minimap": { "show": "always" }` in settings), open this note, and look at the minimap on the right.

- [ ] Every line in the minimap is a thin strip of tiny marks, the same height as the plain paragraphs in section 5.
- [ ] No readable text appears in the minimap: no link labels, no `•` bullets, no citation chips, no footnote numbers, no math.
- [ ] Links in the minimap are small purple marks that stay inside their own line.
- [ ] In the main editor, links, bullets, citations, footnotes, and inline math look exactly as they did before the fix, at buffer size.
- [ ] Clicking a wikilink in the main editor still opens its note.
- [ ] Zooming the buffer font (`cmd-=`, `cmd--`) resizes the widgets in the main editor and leaves the minimap unchanged.

## 1. Wikilinks in bullets

This is the shape from the report: a bulleted list where most lines start with a wikilink.

- [[grinding-the-ink]] -- the hub note. Supersedes [[duan-ratios]] and [[inkstone-care]].
- [[reading-list]] -- what to read next, newest first.
- [[inkstone-care]] -- washing, drying, and storing a stone.
- [[duan-ratios]] -- a paragraph parked for later, not in the plan.
- Background for the notes: [[math-rendering-check]], [[table-rendering-check]], [[inline-rendering-check]].

## 2. Ordinary links

- Stones bought from [Example Stones](https://example.com/stones) and [Example Brushes](https://example.com/brushes), both delivered in a week.
- A link with a long label: [the complete guide to grinding ink on a Duan inkstone](https://example.com/guide).

## 3. Citations and footnotes

Grinding speed changes the ink's particle size [@hayashi2003]. Slow grinding gives a finer ink[^1].

[^1]: As every calligraphy teacher says.

## 4. Inline math

The ratio of water to ink is roughly $w / i \approx 3$, and the grinding time grows as $t \propto \sqrt{n}$.

## 5. Plain lines for comparison

These lines carry no links, so the minimap should draw them as the same small marks it draws for any text. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
