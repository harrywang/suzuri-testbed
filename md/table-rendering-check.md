# Table rendering check

Two table bugs were fixed on 2026-08-20, and two layout bugs on 2026-08-31. Open this note in live preview — with the cursor parked somewhere else, so the tables stay rendered — and check each section against what it says it should look like. Linked from [[grinding-the-ink]].

- [ ] Section 1 renders `<br>` as a line break
- [ ] Section 2 keeps long text inside its own column
- [ ] Section 3 draws one clean grid — every cell in a row is the same height
- [ ] Section 4 shows wikilinks without their brackets
- [ ] Section 5 sizes columns to their content — no table stretched across the pane
- [ ] Section 6 scrolls a wide table horizontally in place
- [ ] Section 7 typesets `$...$` math in cells, on the baseline of the text beside it

## 1. Line breaks inside a cell

A pipe table row cannot contain a newline, so `<br>` is the only way to break a line inside a cell. Table cells were built without the HTML parser that every other block already enabled, so the tag survived to the screen as literal text.

**Broken:** the characters `<br>` appear in the middle of the sentence.
**Fixed:** each cell below is two stacked lines, with no angle brackets anywhere.

| stone | provenance |
| --- | --- |
| **Duan** (端硯) | Lower rock, purple-brown with banded eyes<br>Zhaoqing, Guangdong, quarried 1782 |
| **She** (歙硯) | Gold-thread stripe, fine and slow to raise a slurry<br>Wuyuan, Jiangxi, undated |
| Spellings | Self-closing<br/>and uppercase<BR>must break too |
|   |   |

## 2. Long content wraps inside its column

Cells are flex containers, and text measured without a definite width reports its whole unwrapped line as its minimum size — so the cell shrank to its column while the text kept full width and spilled across the border into the next column.

**Broken:** the first row's text runs under the `year` column and collides with the number.
**Fixed:** long text wraps onto as many lines as it needs and the row grows taller. The `year` values stay legible in their own column.

| method | year |
| --- | --- |
| Grind at a shallow angle with three parts water to five parts stone, adding water a few drops at a time until the slurry holds a stroke, then rest the stick dry on cloth so the face does not lift | 1782 |
| Rinse, never soap | 1甲 |

## 3. Row heights and grid lines

This is the shape that first surfaced the bugs — a long cell with a `<br>` in it, next to a short numeric column. Once cells started wrapping, a second bug showed up behind the first: the container holding the cells centered them at their own height instead of stretching them, so a short cell floated in the middle of a tall row with its borders cut short.

**Broken:** the `year` cells are shorter than the row, and the grid lines do not line up across the table.
**Fixed:** every cell in a row is exactly as tall as the row, so the borders form one unbroken grid.

| entry | year |
| --- | --- |
| **Ink density and grinding time** (Tanaka, plates 12–19)<br>Kyoto University Press, reviewed in [[reading-list]] | 2019 |
| **Duan ratios**<br>see [[duan-ratios]] | n/a |

## 4. Wikilinks inside cells

Wikilinks are concealed on the buffer text, but a cell is drawn from extracted text by the markdown renderer, which has no wikilink support — so the raw brackets used to reach the screen. Cells now rewrite them to the same display text concealment shows.

**Broken:** cells show `[[reading-list]]`, brackets and all.
**Fixed:** the brackets are gone. Aliases show only the alias. Embeds and code spans are deliberately left raw.

| form | renders as |
| --- | --- |
| `[[reading-list]]` | [[reading-list]] |
| `[[duan-ratios\|the ratios]]` | [[duan-ratios\|the ratios]] |
| `[[inkstone-care#Rinsing]]` | [[inkstone-care#Rinsing]] |
| code span, left raw | `[[not-a-link]]` |
| two in one cell | [[duan-ratios]] and [[reading-list]] |

These are display-only — clicking one does not navigate yet.

## 5. Columns take their content width

Tables used to stretch to the full block width, with the leftover space split equally across columns — so a rank column with a single digit in it grew as wide as a column of sentences, and the whole table sprawled across the pane. Columns are now sized from their content, and the table hugs the grid.

**Broken:** the table below spans the whole pane, with acres of blank space after `1` and `4.8`.
**Fixed:** the table is a compact block on the left; the `rank` and `grade` columns are narrow, the `stone` column a little wider, and nothing stretches.

| rank | stone | grade |
| --- | --- | --- |
| 1 | Duan | 4.8 |
| 2 | She | 4.5 |
| 3 | Tao | 4.2 |

## 6. Wide tables scroll in place

A table wider than the pane used to be simply cut off: the hidden columns were unreachable, because the replaced source lines never extend the editor's own scroll range. The grid now lives in its own horizontal scroll region, capped at the visible pane width.

**Broken:** the columns past the right edge cannot be reached at all.
**Fixed:** the table stops at the pane edge; a trackpad swipe (or shift+wheel) over it slides the grid to reveal `water ratio` through `notes`, while the rest of the note stays put. The `</>` and `+` buttons stay pinned at the right edge while the grid scrolls.

| stone | provenance | quarried | water ratio | grind angle | slurry time | resting | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Duan** (端硯) | Lower rock of the Meikeng pit, purple-brown with banded eyes throughout the face | 1782 | three parts water to five parts stone | shallow, almost flat to the face | slow to raise, holds a stroke well | dry on cloth, never in the well | the reference stone for [[duan-ratios]] |
| **She** (歙硯) | Gold-thread stripe from Wuyuan, fine-grained and cold to the touch in winter | undated | four parts water to five parts stone | slightly steeper than Duan | very slow, fine slurry | rinse and stand on edge | compare against [[grinding-the-ink]] |
| **Tao** (洮硯) | Green Tao river stone, rippled like the current that carried it | 1911 | equal parts | shallow | quick but coarse | dry flat | rarely used, kept for guests |

## 7. Math inside cells

Covers [suzuri#127](https://github.com/harrywang/suzuri/pull/127) and [suzuri#128](https://github.com/harrywang/suzuri/pull/128). Like wikilinks, a cell is drawn by the markdown renderer, which drops math, so `$x_1^{(i)}$` used to reach the screen as raw LaTeX. Cells now typeset their formulas and keep the text around them as Markdown.

**Broken:** the header row shows `$x_1^{(i)}$ (population)`, dollar signs and all.
**Fixed:** every formula is typeset. A formula and the label after it share one line, and the label's letters sit on the formula's baseline rather than being centered against it.

| $i$ | $x_1^{(i)}$ (population) | $x_2^{(i)}$ (median income) | $x_3^{(i)}$ (age) | $y^{(i)}$ |
| --- | --- | --- | --- | --- |
| 1 | 322 | 8.3252 | 41 | 452600 |
| 2 | 2401 | 8.3014 | 21 | 358500 |

The near-misses must stay text, as they do outside tables:

| form | renders as |
| --- | --- |
| inline | $\hat{y} = \mathbf{w}^\top \mathbf{x}$ |
| mid-cell `$$` | the ratio $$\frac{w}{s}$$ inline |
| code span, left raw | `$x$` |
| escaped dollars | \$5 and \$10 |
| loose delimiters | $ a = b $ |
| broken LaTeX, shown as source | $\frac{3}{$ |
