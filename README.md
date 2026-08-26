# suzuri-testbed

A test vault for [Suzuri](https://github.com/harrywang/suzuri). Every folder exercises one rendering surface, and the fixtures are written so a human can open them and verify behavior by eye — several are self-checking notes with a checklist at the top.

Open this folder itself in Suzuri. The wikilinks and the Python kernel discovery both assume the vault root is the worktree root.

## Layout

```
md/       markdown live preview (image-reload/ holds the image-caching check)
code/     Python REPL and notebook execution
latex/    LaTeX preview
typst/    Typst preview
pdf/      PDF viewer
```

## md/ — markdown live preview

A small interlinked vault themed around inkstones (suzuri, 硯).

- `grinding-the-ink.md` is the hub note. It packs the whole live-preview feature surface into one screen — bold, wikilinks, an embedded image with a width attribute (`![|450](...)`), a pandoc-style citation, inline and display math, and a table.
- `duan-ratios.md`, `inkstone-care.md`, and `reading-list.md` are satellites. They exist so the hub's wikilinks resolve and markdown-oxide has something to complete and backlink against.
- `math-rendering-check.md` and `table-rendering-check.md` are self-verifying regression checks: open one in live preview, park the cursor where the note says, and tick the checkboxes against what each section says it should look like. The sections cover edge cases that have actually broken before — mid-line `$$`, dollar amounts that must stay prose, `<br>` inside table cells, wikilinks in cells.
- `frontmatter-rendering-check.md` covers the Properties card: YAML frontmatter rendering as a Zed-preview-style two-column table (quoted strings, booleans as checkboxes, block lists and inline arrays as pills, an empty value), in-place value editing, the `+ Add property` flow, the `</>` source reveal, and the toolbar's source-mode toggle. Its editing checks rewrite the note's own frontmatter; the note carries the `git checkout` to restore it.
- `image-reload/image-reload-check.md` covers image caching: overwrite a fixture from a terminal and the preview should update without reopening the note. It deliberately sits one folder down, with one image beside it and one in `attachments/` reached through `../`, because those two spellings of a path used to be cached under different keys. The fixtures are numbered grids so a crop is unmistakable, and the note carries the `sips` commands to crop them and the `git checkout` to restore them.

**Convention:** when a live-preview bug gets fixed, add a section for it to the relevant check note (or start a new `*-rendering-check.md`), so the fix stays verifiable on every later build.

## code/ — Python execution

- `python-rendering-check.py` — a `# %%`-celled script for the inline REPL. Put the cursor in a cell and run `repl::Run` (`ctrl-shift-enter`).
- `notebook-rendering-check.ipynb` — a run-through for the notebook editor whose cells produce each output kind in turn: an image, an HTML table, a traceback, interleaved stdout/stderr streams, plus markdown cells with math and a deliberately unexecuted cell.

Both need a Python environment with `ipykernel` at the vault root. One-time setup, following the [uv project workflow](https://docs.astral.sh/uv/guides/integration/jupyter/):

```sh
cd ~/sandbox/suzuri-testbed
uv init
uv add ipykernel numpy pandas matplotlib
```

`uv add` creates `.venv/` and pins everything in `pyproject.toml` and `uv.lock`. No `jupyter` install and no kernelspec registration are needed — Suzuri launches the kernel from `.venv` directly. If no kernel shows up, run `repl: refresh kernelspecs` from the command palette and check that `uv run python -c "import ipykernel"` succeeds.

## latex/ and typst/ — typeset preview

Each folder holds one source document (`latex-rendering-check.tex`, `typst-rendering-check.typ`), the `references.bib` it cites, and the reference PDF it should produce. Together they exercise the `.tex`/`.typ` preview button end to end, including bibliography resolution.

## pdf/ — PDF viewer

`tanaka-2019.pdf` — the (fictional) paper the markdown notes cite, doing double duty as the PDF-viewer fixture.
