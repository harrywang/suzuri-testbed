# Canvas rendering check

Check for the read-only JSON Canvas viewer ([suzuri#157](https://github.com/harrywang/suzuri/pull/157), for [suzuri#155](https://github.com/harrywang/suzuri/issues/155)). `.canvas` files open as a canvas instead of JSON. The viewer never edits: an agent (or the JSON editor) writes the file and the canvas follows it.

**How to run this check.** Open the testbed root as the project (canvas `file` paths are relative to it), then open each canvas below from the project panel.

## 1. Opening and navigating: `canvas-rendering-check.canvas`

- [ ] The file opens as a canvas, not as JSON, and the tab shows `canvas-rendering-check.canvas`.
- [ ] The whole canvas is fitted into view on open, with a margin, and the zoom bar in the bottom-right corner shows a percentage of 100% or less.
- [ ] Dragging anywhere, including on a card, pans the canvas and opens nothing.
- [ ] Two-finger scroll pans in both directions; with a mouse wheel, shift turns vertical scrolling sideways.
- [ ] Pinch, or cmd-scroll, zooms about the pointer: the spot under the pointer stays put.
- [ ] `−`, `+`, and the fit button in the zoom bar work, and the percentage updates.
- [ ] Text inside cards scales with the zoom, so a card's contents look the same at every zoom, only bigger or smaller.

## 2. Groups

- [ ] Four groups, each with its label above its top-left corner: green **1. Notes**, purple **2. Files**, uncolored **3. Links and text**, red **4. Edges**.
- [ ] Groups sit behind everything else and are tinted with their color. The uncolored group has a plain border.
- [ ] Clicking inside a group but not on a card does nothing.

## 3. Note cards (green group)

- [ ] `inkstone-care.md` shows the whole note, starting at **Inkstone care**, with its file name in small muted text above the card.
- [ ] The cyan card shows only the **Deep clean** section of the same note (subpath `#Deep clean`), not the rest.
- [ ] `frontmatter-note.md` starts at its **Frontmatter note** heading; no `tags:` or `status:` text.
- [ ] The orange card says **Not found: md/this-note-does-not-exist.md** with a warning icon, and clicking it does nothing.
- [ ] Clicking a note card opens that note in a tab. Hovering it shows a pointing hand.
- [ ] Edit `md/inkstone-care.md`, for example add a line under the heading, and the two cards built from it update without reopening the canvas. Undo the edit afterwards.

## 4. Files (purple group)

- [ ] The image card shows the Suzuri banner, fitted inside the card without stretching.
- [ ] The PDF card shows a PDF icon and `tanaka-2019.pdf`; clicking it opens the PDF viewer.
- [ ] The vermilion card's border and tint are `#c0472b`, distinct from the six presets.

## 5. Links and text

- [ ] The `jsoncanvas.org` link card shows a link icon and the URL; clicking it opens the spec in the browser.
- [ ] Clicking the `file:///System/Applications/Calculator.app` card opens **nothing**, since only web and mail links are followed. Calculator must not launch.
- [ ] The yellow text card renders markdown: a heading, bold, italic, inline code, a bullet list, and a block quote. Clicking its link does not open anything.
- [ ] The text card's purple arrow reaches the image card.

## 6. Edges (red group)

- [ ] **A → B**: one arrowhead, at B, labelled *default: arrow at B only*.
- [ ] **C ↔ D**: cyan, arrowheads at both ends.
- [ ] **E — F**: vermilion, no arrowheads.
- [ ] **A → C**: yellow, leaves the bottom of A and enters the top of C.
- [ ] **F → G**: leaves the side of F facing G and enters the side of G facing F, labelled *inferred*.
- [ ] Every curve leaves its card straight out of the side it is attached to, and no arrowhead pokes past its tip into the card.
- [ ] The card of unknown type `sticker` shows **Unsupported card type “sticker”**.
- [ ] Labels sit on the middle of their curves, on a background that hides the line behind them.

## 7. Tolerance: `edge-cases.canvas`

- [ ] Four cards: **Kept**, the uncolored "Color 9" card, an empty card, and the fractional-coordinate card.
- [ ] The text "You must NOT see this text" appears nowhere, and neither does the label "must NOT be drawn".
- [ ] One edge, labelled *the only edge*.

## 8. Empty file: `empty.canvas`

- [ ] Shows "This canvas is empty." in the middle, and the zoom bar still works.

## 9. Following the file: `live-reload/agent-writes.canvas`

This is the point of the viewer. Open the canvas (it starts empty), then run each step from a terminal at the testbed root and watch the canvas without touching it.

```sh
python3 canvas/live-reload/simulate-agent.py 1
python3 canvas/live-reload/simulate-agent.py 2
python3 canvas/live-reload/simulate-agent.py 3
python3 canvas/live-reload/simulate-agent.py broken
python3 canvas/live-reload/simulate-agent.py 2
python3 canvas/live-reload/simulate-agent.py reset
```

- [ ] Step 1: "This canvas is empty." is replaced by three paper cards, fitted into view. Each card shows its bold title on one line and its finding on the next: a single newline in a card is a line break, as in Obsidian.
- [ ] Step 2: a yellow **Synthesis** card appears below, with three arrows into it. The view does not jump.
- [ ] Step 3: Paper 3 turns red and its arrow is labelled *contradicts?*.
- [ ] `broken`: the step 3 canvas stays on screen, and a banner at the top says the canvas could not be read and shows the parse error.
- [ ] Step 2 again: the banner goes away and the canvas shows step 2.
- [ ] `reset` leaves the file empty, matching git. Run `git status canvas/` to confirm nothing is left modified.

## 10. Edit JSON

- [ ] The `</>` button in the zoom bar opens the canvas file as JSON in a split to the right.
- [ ] In that split, change a card's `"text"` in `canvas-rendering-check.canvas`; the canvas updates as you type. Undo the change and let autosave restore the file, then confirm with `git status canvas/`.
- [ ] Break the JSON in the split (delete a closing brace): the banner appears and the last good canvas stays. Undo.
- [ ] The canvas tab never shows an unsaved-changes dot; the JSON tab does while it has edits.
