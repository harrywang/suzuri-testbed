---
title: "Frontmatter Rendering Check"
date: 2026-08-26T00:00:00.000Z
rating: 4.5
published: false
reviewed: true
notes:
tags:
  - frontmatter
  - properties
aliases: [fm-check, properties-check]
dafsdfa: dfasda
---

# Frontmatter rendering check

Park the cursor on this line and check the card at the top of the file against each section. The editing checks rewrite this file's own frontmatter; restore it afterwards with `git checkout -- md/frontmatter-rendering-check.md`.

## Rendering

- [ ] The frontmatter renders as a bordered two-column table — muted bold key column, value column — like Zed's built-in markdown preview, with visible space above it so it does not hug the tab bar
- [ ] `title` shows `Frontmatter Rendering Check` with the quotes stripped
- [ ] `published` renders as an unchecked checkbox and `reviewed` as a checked one
- [ ] `notes` (no value) shows a muted `Empty`
- [ ] `tags` (a YAML block list) and `aliases` (an inline array) both render as pills
- [ ] Press arrow-up from this line until the cursor sits inside the frontmatter rows: the card must NOT dissolve into raw YAML — it only reveals via its `</>` button

## Editing

- [ ] Click the `rating` value: a single-line editor appears seeded with `4.5`. Type `5.0` and press Enter, then reveal the source with `</>` — the line reads `rating: 5.0`
- [ ] Click a value, type something, press Escape: the source is unchanged
- [ ] Toggle the `published` checkbox: the source flips between `published: false` and `published: true`
- [ ] Click `+ Add property`, type `status`, press Enter: a `status: ` line lands before the closing `---` and the value editor opens chained; type `draft` and press Enter
- [ ] Hover the card: a `</>` appears on its right edge. Clicking it reveals the raw YAML with the cursor inside; moving the cursor below the block re-renders the card and a second visit needs the button again

## Toolbar

- [ ] A `</>` button sits next to the eye in the quick action bar; clicking it switches the whole buffer to raw markdown and shows a pressed state; clicking again restores live preview
- [ ] The eye button still opens the classic markdown preview, and in that preview this frontmatter also renders as the same style of two-column table
