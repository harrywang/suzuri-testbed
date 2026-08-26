# Block interaction check

Editing at the edges of rendered block widgets. Both sections reproduce bugs that shipped once; the fixture is this file itself. Restore afterwards with `git checkout -- md/block-interaction-check.md`.

## Deleting into a rendered block

Put the cursor at the end of the empty line below, then press forward-delete (fn+Delete):

# A Heading To Keep

- [ ] Only the empty line goes — the heading above survives and merges up one line (this used to delete the heading's entire text along with the newline)
- [ ] Undo (`cmd+z`) restores the empty line, and clicking the rendered heading then pressing backspace at its start merges the same way
- [ ] With the cursor sitting on the heading's line it shows raw `# A Heading To Keep` — that is the reveal-on-cursor rule, not a bug; click any other line and it renders again

## Clicking a widget's text

- [ ] Click directly ON the word in the rendered heading above: the source reveals with the cursor at the character you clicked (it used to start a blue widget-text selection and never reveal)
- [ ] Click the empty space to the right of the rendered heading: the source reveals with the cursor at the block start, as before
- [ ] In the fenced block below, hover it and click its copy button: the code is copied and the block does NOT reveal — buttons still win over click-to-reveal

```python
print("copy me with the button")
```
