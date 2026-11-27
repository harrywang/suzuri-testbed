# PDF zoom and resize check

Open `zoom-resize.pdf` beside this note. It has 30 pages, and every line names its page and line (`p12 · L17`), so after each step the line at the top of the view says exactly where the viewer put you. Each page also has a figure of 3pt fine print (`p12·c40`) that is unreadable at fit width.

Before each section, type `12` into the page box in the PDF toolbar and press Enter, then scroll down a little so a line such as `p12 · L8` sits at the top. Write that line down; it is the one each check expects to stay in view.

## 1. Resizing keeps your place ([suzuri#199](https://github.com/harrywang/suzuri/issues/199))

The pages scale with the pane's width. The scroll position used to be kept in pixels, so the same pixel offset landed somewhere else after a resize.

Click a page first so the PDF has focus: in a markdown note `cmd-b` means bold, not the panel.

- [ ] Toggle the project panel (`cmd-b`). The same line is still at the top of the view, even though the pages got bigger or smaller.
- [ ] Toggle it back. Still the same line.
- [ ] Open and close the agent panel (`cmd-?`). Still the same line.
- [ ] Drag the split between this note and the PDF a long way. Still the same line.

## 2. Pinch to zoom ([suzuri#200](https://github.com/harrywang/suzuri/issues/200))

- [ ] Put the pointer over a cell of Figure 12's fine print, say `p12·c40`, and pinch out on the trackpad. The PDF zooms, and `p12·c40` stays under the pointer the whole time.
- [ ] The fine print becomes sharp and readable shortly after the fingers stop. (Mid-pinch the page stretches its old bitmap, so it looks soft for a moment; that is expected.)
- [ ] Pinch back in over the same cell. It stays under the pointer.
- [ ] Repeat on page 28. Deep in the document is where the old zoom drifted most: it slid the page away by about 20px per page above the pointer.

## 3. Cmd+scroll zooms around the pointer without scrolling

- [ ] Hold `cmd` and scroll over a cell of the fine print. The PDF zooms and the cell stays under the pointer. It used to drift, because the view also scrolled by the wheel amount.
- [ ] Scroll without `cmd`. The view scrolls normally.
- [ ] `shift`+scroll while zoomed in. The page pans sideways without moving down ([suzuri#131](https://github.com/harrywang/suzuri/issues/131)).

## 4. Zoom buttons and keys keep your place

- [ ] Click `+` in the PDF toolbar three times. The line you wrote down stays at the top of the view.
- [ ] Click `−` and then the zoom percentage (which resets to 100%). Still the same line.
- [ ] With the PDF focused, `cmd-=`, `cmd--` and `cmd-0` (reset) behave the same.

## Rebuilding the fixture

```sh
cd pdf/zoom-resize && typst compile zoom-resize.typ
```
