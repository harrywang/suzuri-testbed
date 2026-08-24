# Table rendering check

Two table bugs were fixed on 2026-08-20. Open this note in live preview — with the cursor parked somewhere else, so the tables stay rendered — and check each section against what it says it should look like. Linked from [[grinding-the-ink]].

- [ ] Section 1 renders `<br>` as a line break
- [ ] Section 2 keeps long text inside its own column
- [ ] Section 3 draws one clean grid — every cell in a row is the same height
- [ ] Section 4 shows wikilinks without their brackets

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
