# Inline rendering check

Three Obsidian-flavored inline constructs: `==highlight==`, `#tag`, and `[^footnote]`. Each is found by scanning prose, not by the markdown grammar, so most of what can go wrong is a false positive — something that merely looks like the syntax getting swallowed. Open this note in live preview with the cursor parked somewhere else and check each section. Linked from [[grinding-the-ink]].

- [ ] Section 1 paints highlights and leaves near-misses as prose
- [ ] Section 2 draws tag chips, leaves near-misses as prose, and chips a hex color on purpose
- [ ] Section 3 raises footnote markers and mutes their definitions
- [ ] Section 4 hands back the source when the cursor touches a construct

## 1. Highlights

The ==important part== is that the delimiters vanish and the words behind them get a highlighter wash.

Delimiters bind tightly, the way emphasis does, so none of the following is a mark and every `=` below must still be on screen:

- Padded: a == b == c, which is prose comparing two values
- Empty: ==== and ======
- Split across lines, where the opener ends one line ==and
  the closer opens the next== so neither pairs
- In code: `==nope==` and `a == b`
- Bare: 3 == 3 in a sentence with no second pair

Two marks on one line both take: ==first== and ==second==, with plain text between them.

A mark holds other inline syntax: ==**bold inside a mark**== and ==a [[duan-ratios]] wikilink inside one==.

## 2. Tags

Filed under #inkstone and #stone/duan and #stone/she — three chips, each keeping its `#`, because the `#` is part of the tag's name and never gets concealed.

None of the following is a tag:

- A URL fragment: https://example.com/inkstones#duan
- A wikilink's heading target: [[inkstone-care#Daily rinse]]
- An issue reference: #1 and #2026 — a tag needs at least one non-digit
- In code: `#nope`
- Mid-word: care#duan, because a tag has to open a word

One that *is* a tag, and surprises people: #ffcc00. Obsidian's rule is only that a tag hold one non-numeric character, and `f` and `c` qualify — so a hex color written in prose becomes a tag in Obsidian too. Matching Obsidian matters more than being clever here, so this chip is correct and must stay.

Headings are the case worth watching, because a heading's `#` is the same character. The `## 2. Tags` above and every other heading in this note must show zero chips.

## 3. Footnotes

Density follows the plate series[^tanaka] and the ratios were re-weighed twice[^2], both of which should appear as small raised markers rather than bracketed text.

Not footnotes, and all still on screen as written:

- Spaced: [^ not a label]
- In code: `[^nope]`
- A plain reference link: [reading][reading-list-ref]

[reading-list-ref]: reading-list.md

The definitions below are deliberately NOT concealed — a bare paragraph would give no sign of which footnote it defines — but their `[^label]:` markers must be muted, the way a link reference definition is.

[^tanaka]: Tanaka (2019), plates 12–19. See [[reading-list]].
[^2]: Three parts water to five parts stone, per [[duan-ratios]].

## 4. Reveal on cursor

- [ ] Click inside a highlight: the `==` delimiters come back, and the rest of the line stays rendered
- [ ] Click a footnote marker: `[^tanaka]` comes back as text
- [ ] Move the cursor away: both render again
- [ ] Click a tag: nothing changes, because a tag has no hidden syntax to restore
