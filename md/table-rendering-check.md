# Table rendering check

Two table bugs were fixed on 2026-08-20, two layout bugs on 2026-08-31, and column fitting on 2026-11-17. Open this note in live preview — with the cursor parked somewhere else, so the tables stay rendered — and check each section against what it says it should look like. Linked from [[grinding-the-ink]].

- [ ] Section 1 renders `<br>` as a line break
- [ ] Section 2 keeps long text inside its own column
- [ ] Section 3 draws one clean grid — every cell in a row is the same height
- [ ] Section 4 shows wikilinks without their brackets
- [ ] Section 5 sizes columns to their content — no table stretched across the pane
- [ ] Section 6 scrolls a table of unbreakable cells horizontally in place
- [ ] Section 7 typesets `$...$` math in cells, on the baseline of the text beside it
- [ ] Section 8 wraps every column of a table wider than the pane, so it fits without scrolling

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

Since section 8's fix, a table only scrolls when wrapping cannot make it fit, which is when its longest unbreakable words are together wider than the pane. The cells below are single tokens joined by underscores, which offer no place to break a line.

**Broken:** the columns past the right edge cannot be reached at all, or a token is split in the middle to force the table into the pane.
**Fixed:** the table stops at the pane edge with every token on one line; a trackpad swipe (or shift+wheel) over it slides the grid to reveal `resting_instruction` and `catalogue_note`, while the rest of the note stays put. The `</>` and `+` buttons stay pinned at the right edge while the grid scrolls.

| stone_identifier | provenance_record | water_ratio_setting | grind_angle_setting | resting_instruction | catalogue_note |
| --- | --- | --- | --- | --- | --- |
| duan_lower_rock_meikeng_pit_1782 | zhaoqing_guangdong_purple_brown_banded_eyes | three_parts_water_to_five_parts_stone | shallow_almost_flat_to_the_face | dry_on_cloth_never_in_the_well | reference_stone_for_the_duan_ratios_note |
| she_gold_thread_wuyuan_undated | wuyuan_jiangxi_fine_grained_cold_in_winter | four_parts_water_to_five_parts_stone | slightly_steeper_than_the_duan | rinse_and_stand_on_its_edge | compare_against_grinding_the_ink_note |

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

## 8. A table wider than the pane wraps every column

Covers [suzuri#177](https://github.com/harrywang/suzuri/issues/177), fixed in [suzuri#178](https://github.com/harrywang/suzuri/pull/178). Each column was sized to its longest cell, up to a cap of 60 characters, and nothing shrank the columns when together they were wider than the pane. A column under the cap therefore never wrapped: only a column over it did, and the rest pushed the table into sideways scrolling. Columns now shrink the way a browser's do. Each keeps its longest word whole, and the width left over is shared by how much text a column holds.

Check these in a pane about half the screen wide (split the editor, or open a dock), then drag the divider.

**Broken:** in the first table the two left columns sit on one line each, only the right column wraps, and the table runs past the pane edge and scrolls sideways.
**Fixed:** the table ends at the pane edge with nothing to scroll. All three columns wrap, and the right column, which holds the most text, is the widest. This is the reporter's table verbatim.

| xxxxxxxx | xxxxxxx | xxxxxxx |
| --- | --- | --- |
| **xxxxxxxxxxxx xxxxxxxxx xxxxxxxxxxxx xxxxxxxxx** | ssssssssssssss sssssssssssssss ssssssssssssssssss. | xxxxxxxxx xxxxxxxxxx xxxxxxxxxx xxxxxxxxxxxxxxx (  $\delta_{\text{xxx}}$ xx xxxx par $y_{\text{xxx}}$) xxxxxxxxxx xxxxxxxxx xxxxxxxxxxxxxs. |
| **ssssssssss xxxxxxxxxx yyyyyyyyy yyyyyy yyyyyyy** | ssssss xxxxxxxxxxx  cxxxxxxxx  xxxxxxxxxxxx. | xxxxxxxxxx s *xxxxxx* xxx  xxx xxxx xxxxxxxx  xxxx  xx  xxxxxxx  *xxxxx* (xxxxx de $\delta_{\text{xxxxx}}$ xx xxxxxxxxxx xxx $k_{\text{xxxxx}}$) xxxx xxxxxx xxxxxx xxxxx xx xxxxxx. |

The same shape in prose. **Fixed:** the `year` column stays as narrow as its four digits, because a one-word column has nothing to give up, and the two text columns share the rest, `method` taking more than `stone`.

| stone | method | year |
| --- | --- | --- |
| Lower rock of the Meikeng pit, purple-brown | Grind at a shallow angle with three parts water to five parts stone, adding water a few drops at a time until the slurry holds a stroke, then rest the stick dry on cloth | 1782 |
| Gold-thread stripe from Wuyuan, cold in winter | Slightly steeper than the Duan, with four parts water to five parts stone, and a slow, fine slurry | 1911 |

Text without spaces wraps between characters, so it must not count as one long word that pins its column. **Fixed:** all three columns wrap and the table fits the pane.

| 硯 | 產地 | 研墨 |
| --- | --- | --- |
| 端硯出自廣東肇慶的老坑石質細膩溫潤紫中帶青石眼分明 | 歙硯出自江西婺源的龍尾山金星金暈紋理緻密發墨如油 | 研墨時水要一滴一滴地加墨錠與硯面保持平穩的角度慢慢畫圈直到墨汁濃淡合適為止 |

Then resize. **Fixed:** as the pane narrows the columns narrow with it and the rows grow taller; as it widens they grow back only as far as their natural width, so the tables then sit on the left rather than stretching across the pane. Narrow the pane far enough and the first table starts to scroll, once its longest words no longer fit side by side.

One limit is by design: a formula is measured by its source, so a cell with long LaTeX keeps its column wider than the typeset result needs.
