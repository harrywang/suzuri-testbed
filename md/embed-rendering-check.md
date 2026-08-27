# Embed rendering check

Note transclusion — `![[Note]]` and `![[Note#Section]]` — which pulls another note's markdown into this one. The target is a note *name* resolved against the whole vault, not a path resolved against this folder, so these checks only mean anything with the vault root open as the worktree. Linked from [[grinding-the-ink]].

- [ ] Section 1 embeds a whole note
- [ ] Section 2 embeds one section of it
- [ ] Section 3 reports a target that does not resolve
- [ ] Section 4 leaves inline embeds and image embeds alone
- [ ] Section 5 picks up an edit to the target without reopening this note

## 1. A whole note

![[inkstone-care]]

- [ ] The card shows all of [[inkstone-care]] — the opening line and all three sections
- [ ] Its header reads `inkstone-care` in the accent color, next to a link icon
- [ ] Clicking the header opens that note in this pane
- [ ] Clicking the card's body reveals this note's `![[inkstone-care]]` source instead
- [ ] The wikilinks in the embedded text read as plain words — no `[[` brackets on screen. A card body renders through the markdown crate, which has no wikilink syntax, so the brackets are stripped the same way a table cell strips them. They are **not** clickable inside a card; that is the known limit, not a bug

## 2. One section

![[inkstone-care#Deep clean]]

- [ ] Only the **Deep clean** section appears — the bean-curd paragraph and its heading, with no *Daily rinse* above it and no *Storage* below
- [ ] The header reads `inkstone-care › Deep clean`

A section runs to the next heading at the same or a higher level, so a section with a subsection under it carries that subsection along:

![[grinding-the-ink#Grinding the ink]]

- [ ] That one pulls the whole hub note, because its heading is the note's only top-level heading

## 3. Targets that do not resolve

![[No Such Inkstone]]

![[inkstone-care#No Such Section]]

- [ ] Both draw a card reading *No note in this project answers to that name.*
- [ ] Both headers are **muted, not accent-colored** — a header only reads as a link when it has something to open
- [ ] Neither collapses to a blank line, which would read as a rendering bug

## 4. What must not become a note embed

An inline embed like ![[inkstone-care]] in the middle of a sentence stays raw, because a card cannot sit inside a line of prose. The characters `![[inkstone-care]]` must still be on screen in this paragraph.

![|450](attachments/suzuri-banner.png)

![[attachments/suzuri-banner.png]]

- [ ] Both of the above are images, not transclusion cards — an image target keeps going to the image widget
- [ ] The wikilink `[[inkstone-care]]` with no `!` is still just a link

## 5. Live update

Embedded text is cached, and the cache is evicted when the file changes on disk. From a terminal at the vault root:

```sh
echo "\nA line added from the terminal." >> md/inkstone-care.md
```

- [ ] The section 1 card grows the new line without this note being touched or reopened
- [ ] The section 2 card does not change, because the new line is not in *Deep clean*

Restore afterwards:

```sh
git checkout -- md/inkstone-care.md
```

- [ ] The card returns to its original text
