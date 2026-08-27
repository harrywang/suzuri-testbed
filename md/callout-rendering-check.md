# Callout rendering check

Obsidian callouts: a block quote whose first line is `> [!type]`. Open this note in live preview with the cursor parked somewhere else, so the callouts stay rendered, and check each section against what it says it should look like. Linked from [[grinding-the-ink]].

- [ ] Section 1 draws each family with its own icon, and each accent comes from the theme
- [ ] Section 2 resolves aliases onto the same look
- [ ] Section 3 titles an untitled callout with its type's name
- [ ] Section 4 folds and unfolds on a click, and only on the title
- [ ] Section 5 leaves an ordinary block quote alone
- [ ] Section 6 still renders an unknown type as a callout
- [ ] Section 7 renders markdown inside a callout body

## 1. The families

Every accent comes from the theme's status palette, so these must stay legible after `theme selector` switches between Suzuri Dark and Suzuri Light, and no accent may be a color the theme does not define. There are more icons than colors: some families share an accent and are told apart by their icon alone.

> [!note] Note
> Blue, with an info icon. `abstract` (notepad) and `todo` (checklist) share this color.

> [!tip] Tip
> Green, with a flame. `success` shares the color, with a check.

> [!warning] Warning
> Amber, with a warning triangle. `question` shares the color, with a question mark.

> [!failure] Failure
> Red, with a circled cross. `danger` shares the color, with a bolt.

> [!example] Example
> Blue with a book — deliberately the same accent as **Note** above. Obsidian gives this family a purple of its own, but the status palette has no purple, and the near-purple it does have renders blue in one theme and grey in the other. The book icon is what tells them apart.

> [!quote] Quote
> Muted, with the editor's quote glyph (stacked lines, not a curly quotation mark — that icon does not exist in the icon set). The one family that is not a status color.

## 2. Aliases

Obsidian gives most types several spellings. All three below must come out identical — same icon, same color — and differ only in their titles.

> [!tip] Spelled tip
> One flame, green.

> [!hint] Spelled hint
> Must match the one above exactly.

> [!important] Spelled important
> And so must this one.

## 3. No title

An untitled callout takes its type's name as the title, capitalized.

> [!warning]
> The title bar above must read **Warning**, not an empty row and not the raw `[!warning]`.

> [!tldr]
> And this one must read **Abstract** — the title is the family's name, not the alias that was typed.

## 4. Folding

A `-` or `+` immediately after the `]` makes the callout collapsible and sets which way it starts. Anything else — including a title that merely opens with a dash — leaves it fixed.

> [!danger]- Starts folded
> This body is hidden until the title is clicked.

> [!success]+ Starts open
> This body is visible, and the callout can still be folded.

> [!note] - A title that starts with a dash
> The dash is part of the title because it comes after a space, so this callout is NOT collapsible and has no chevron.

- [ ] The first two show a chevron; the third does not
- [ ] Clicking the folded title opens it, and the chevron turns from `›` to `⌄`
- [ ] Clicking it again folds it back
- [ ] Neither click reveals the raw `> [!danger]-` source — the title claims the click
- [ ] Clicking the third callout's title DOES reveal its source, because a fixed callout has nothing to toggle
- [ ] Clicking a folded callout's body area (not the title) also reveals source

## 5. Ordinary quotes are untouched

> A block quote with no `[!type]` on its first line.
> It must keep the plain vertical rule it has always had — no card, no icon, no tint.

> [!not a type] Two words
> A type is one word, so this is an ordinary quote too, brackets and all still on screen.

## 6. Unknown types

> [!inkstone] A type Obsidian never defined
> A vault full of `[!recipe]` callouts should still read as callouts, so an unrecognized type falls back to the note styling rather than dropping to a plain quote. This must show the blue note card, with the title as written.

## 7. Markdown inside the body

> [!example] The full grind
> Water **a few drops** at a time, per [[duan-ratios]], saturating near $t^* \approx 4$ min:
>
> $$D(t) = D_{\max}\left(1 - e^{-t/\tau}\right)$$
>
> 1. Wet the face
> 2. Grind at a shallow angle
> 3. Rest the stick dry, per [[inkstone-care]]
>
> ```python
> print("grinding")
> ```

- [ ] Bold, inline math, and display math all render inside the card
- [ ] The wikilinks read as plain words, with no `[[` brackets on screen — a card body renders through the markdown crate, which has no wikilink syntax, so the brackets are stripped as a table cell strips them. They are not clickable inside a card
- [ ] The ordered list keeps its numbers and the fenced block is syntax-highlighted
- [ ] The code block's copy button still wins its click and does not reveal source

## 8. Reveal on cursor

- [ ] Click any callout's body text: the source reveals with the cursor at the character clicked, `>` markers and all
- [ ] Move the cursor to another line: it renders again
