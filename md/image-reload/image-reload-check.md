# Image reload check

Two image-caching bugs were fixed on 2026-08-22 and 2026-08-23. Both have the same
symptom — you re-crop a screenshot, and the note keeps showing the old picture until
you close the tab and reopen it. Open this note in live preview, overwrite the files
below from a terminal, and watch the previews change without touching the editor.
Linked from [[grinding-the-ink]].

**Open the vault folder itself**, not this note on its own. The reload rides on the
project's filesystem watcher, so the images have to sit inside an open worktree. A
lone `.md` opened by itself gets a worktree of exactly one file, no events reach it,
and both sections below will fail for a reason that has nothing to do with these bugs.

- [ ] Section 1 updates an image that sits beside the note
- [ ] Section 2 updates an image reached through `../`
- [ ] Both go back to a clean 1-6 grid after the restore command

Each fixture is a 3x2 grid of numbered cells, so a crop is unmistakable: crop one and
some of the numbers disappear. A flat colour block could not tell you whether anything
happened.

## 1. An image beside the note

The image cache is keyed by file path and gpui's app-level asset cache is never
evicted, so the bitmap decoded on first render was served for the life of the process.
Reopening the document did not help, because that cache outlives the document. Renaming
the file worked around it only because a new path is a new key.

**Broken:** the grid below still shows all six numbered cells after you run the crop.
**Fixed:** within a second or so it becomes a small centred fragment — two partial
numerals and slivers of their neighbours — with no click anywhere in the editor. The
block shrinks to match, so the text below it moves up.

![](reload-check-sibling.png)

```sh
sips -c 170 330 md/image-reload/reload-check-sibling.png
```

## 2. An image reached through a parent folder

The first fix still missed the ordinary vault layout — notes in one folder, images in a
folder beside it, every reference spelled `../images/x.png`. Resolution joined that onto
the note's directory and `PathBuf::join` keeps the `..` literally, while the worktree
reports the file under its collapsed path. Two spellings of one file hashed differently,
so the eviction matched nothing.

This note lives in `md/image-reload/` and the image lives in `md/attachments/`, so the
reference has to climb out — the same shape as a real vault.

**Broken:** section 1 updates but this one does not, which is the tell for this bug
specifically.
**Fixed:** both sections behave identically.

![](../attachments/reload-check-parent.png)

```sh
sips -c 170 330 md/attachments/reload-check-parent.png
```

## Restoring the fixtures

Both commands above overwrite the files in place — that is the whole point — so put them
back when you are done. From the vault root:

```sh
python3 md/image-reload/make-fixtures.py
```

That regenerates both grids from scratch with the stdlib alone, so it works whether or
not the fixtures are committed yet. `git checkout` on the two paths does the same job
once they are tracked.

The previews should return to a full 1-6 grid without a reopen. That restore is itself a
third pass through the same code path, in the opposite direction.

## Known gap

An image outside every worktree still goes stale, because no filesystem event ever
arrives for it. That covers a note opened without its folder, and an image referenced by
an absolute path pointing somewhere outside the project. Neither is fixed; if either
starts mattering, the fix is to watch the image's own directory rather than relying on
the worktree.
