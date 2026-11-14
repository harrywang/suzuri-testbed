# Local graph check

Check for the local graph ([suzuri#166](https://github.com/harrywang/suzuri/pull/166), for [suzuri#165](https://github.com/harrywang/suzuri/issues/165)): a pane that shows the active note in the middle and the notes linked to and from it around it.

**How to run this check.** Open the testbed root as the project, then open `graph/centre.md`. This note names the fixtures in code spans on purpose: a real link from here would add this note to their graphs.

## 1. Opening

- [ ] With `centre.md` focused, **Document → Show Local Graph** is enabled. With `pyproject.toml` focused, it is greyed out.
- [ ] Choosing it opens a **Local Graph** tab in a split to the right. The cursor stays in `centre.md`: typing goes into the note.
- [ ] The graph is fitted into the pane, with **centre** in the middle in the accent color.
- [ ] Choosing the command again does not open a second graph.

## 2. What counts as a link

- [ ] Exactly six notes surround the centre: **outgoing**, **aliased**, **embedded**, **markdown-linked**, **twin**, and **backlink**.
- [ ] **outgoing** appears once, though `centre.md` links to it twice.
- [ ] **aliased** is labelled with its file name, not "a different label".
- [ ] **backlink** is there although `centre.md` never mentions it: links count in both directions.
- [ ] **only-in-code** is absent. Frontmatter, a code span, and a fenced block are not links.
- [ ] Nothing is drawn for `no-such-note`, the web link, or the `#counted` heading link.

## 3. Depth

- [ ] The corner shows **Depth 1 2 3**, with 1 selected.
- [ ] Depth 2 adds **second-hop**, joined to **outgoing**, and the graph refits.
- [ ] Depth 3 adds **third-hop**, joined to **second-hop**.
- [ ] Back at depth 1 both are gone.

## 4. Clicking and following

- [ ] Hovering a note shows a pointing hand and highlights its links.
- [ ] Clicking **outgoing** opens `outgoing.md` in the left pane, where the notes are, not in the graph's pane. The graph stays visible and re-centres on **outgoing**, with **centre** and **second-hop** around it.
- [ ] Back on `centre.md`, clicking **twin** opens `graph/twin.md`, titled "Twin (beside the centre)", not `graph/elsewhere/twin.md`.
- [ ] Switching tabs in the left pane re-centres the graph each time.
- [ ] Opening `pyproject.toml` leaves the last graph in place instead of emptying it.
- [ ] Opening `only-in-code.md` shows **No other note links to or from this one.**

## 5. Moving around

- [ ] Dragging pans the graph and opens nothing, even when the drag starts on a note.
- [ ] Two-finger scroll pans; pinch or cmd-scroll zooms about the pointer.
- [ ] `−`, `+`, and the fit button work, and the percentage updates.

## 6. Staying current

- [ ] In `centre.md`, type `[[only-in-code]]` on a new line. Within a second **only-in-code** joins the graph, without saving. Undo, and it leaves.
- [ ] From a terminal at the testbed root, add a note that links to the centre, and it appears as a seventh neighbour:

  ```sh
  printf '[[centre]]\n' > graph/new-backlink.md
  ```

- [ ] Remove it again, and the neighbour goes. `git status` should then be clean.

  ```sh
  rm graph/new-backlink.md
  ```

## 7. A crowded graph: `hub/hub.md`

- [ ] Open `graph/hub/hub.md`. All sixty **spoke** notes are drawn, in more than one ring, and no two labels overlap.
- [ ] The fit button brings the whole of it into view.
- [ ] Clicking a spoke opens it, and its graph is just the spoke and **hub**.
