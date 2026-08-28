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
- `duan-ratios.md`, `inkstone-care.md`, and `reading-list.md` are satellites. They exist so the hub's wikilinks resolve and markdown-oxide has something to complete and backlink against. `inkstone-care.md` carries three `##` sections because `embed-rendering-check.md` transcludes them; editing its headings will break that note's section checks.
- `callout-rendering-check.md` covers Obsidian callouts (`> [!note] Title`): the six visual families and the aliases that collapse onto them, an untitled callout taking its type's name, the `+`/`-` fold and the click that toggles it without also revealing source, an unknown type still rendering as a callout, and — the case most likely to regress — an ordinary block quote staying an ordinary block quote.
- `inline-rendering-check.md` covers `==highlight==`, `#tag`, and `[^footnote]`. All three are found by scanning prose rather than by the markdown grammar, so most of the note is near-misses that must stay prose: `a == b == c`, a URL fragment, a wikilink's heading target, `#1`, a hex color, and every one of the note's own headings.
- `embed-rendering-check.md` covers note transclusion (`![[Note]]`, `![[Note#Section]]`), using `inkstone-care.md`'s sections as targets. It checks whole-note and single-section embeds, the muted card an unresolvable target draws, inline and image embeds staying out of it, and — with a shell command the note carries — the cache eviction that makes an edited target update in place.
- `math-rendering-check.md` and `table-rendering-check.md` are self-verifying regression checks: open one in live preview, park the cursor where the note says, and tick the checkboxes against what each section says it should look like. The sections cover edge cases that have actually broken before — mid-line `$$`, dollar amounts that must stay prose, `<br>` inside table cells, wikilinks in cells.
- `frontmatter-rendering-check.md` covers the Properties card: YAML frontmatter rendering as a Zed-preview-style two-column table (quoted strings, booleans as checkboxes, block lists and inline arrays as pills, an empty value), in-place value editing, the `+ Add property` flow, the `</>` source reveal, and the toolbar's source-mode toggle. Its editing checks rewrite the note's own frontmatter; the note carries the `git checkout` to restore it.
- `mermaid-rendering-check.md` covers mermaid diagrams, which come from upstream Zed rather than the fork: a fence becoming a drawn diagram, the Preview/Code tabs and copy button, cmd-scroll zoom and sideways scrolling on a too-wide diagram, the `mermaid 150` scale suffix Obsidian has no equivalent for, tilde fences, theme recoloring, CJK entity names in an ER diagram, a diagram nested in a callout, and the near-misses that must stay code blocks. Section 10 pins the known gap on purpose — Zed allowlists fifteen diagram types and leaves the rest (`requirementDiagram`, `sankey-beta`) as plain code blocks until their CSS guarantees readable text, so those two rendering as source is the pass, not the failure.
- `block-interaction-check.md` covers editing at rendered-block edges: forward-delete/backspace of a line bordering a rendered heading must take only the newline (deleting the block's whole replaced range shipped once), and clicking a widget's own text must reveal source at the clicked character while code-block copy buttons keep winning the click.
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

`latex/aaai/` covers the case those two cannot: a document that dictates its engine. AAAI's style calls `\RequirePDFTeX`, so `aaai-pdftex-check.tex` builds under pdfTeX and aborts under XeTeX with "pdfTeX is required to compile this document. Sorry!" — the check is that preview picks an engine the template accepts. Many IEEE styles pin the engine the same way. It ships the unmodified `aaai2027.sty` and `.bst` it needs, and the reference PDF is the two-column output a correct build produces.

`latex/aaai/expected/` holds what the first preview should look like on a machine with no TeX at all: `install-prompt.png` is the offer, and `installing-toolchain.png` is the toast that replaces it once accepted. The second one matters — provisioning takes far longer than a compile, so if that toast ever says "Compiling…" again, a first run will look like a hang.

Two things about the source are load-bearing and easy to "fix" into breakage: the empty `\affiliations{}` block is required even for an anonymous submission (`\maketitle` expands it unconditionally), and there is deliberately no `\bibliographystyle` line, because the style file sets it and a second one makes bibtex fail.

It also exercises on-demand package installation: the template pulls in `newtx`, `caption`, `courier`, and `tex-gyre`, among others, which a minimal TeX Live will not have until something fetches them.

`latex/neurips/` is the other half of that pair. NeurIPS pins no engine, so it builds under pdfTeX, XeTeX, or LuaTeX alike — what it covers instead is a different package set (`lineno`, `environ`, `units`, `microtype`) and a visibly different page. Left in submission mode, `neurips-rendering-check.tex` anonymises the authors and prints line numbers down the left margin, so a preview that silently loses `lineno` is obvious at a glance rather than only in a log. Adding a `preprint` or `final` option to the `\usepackage` line switches both off, which is a quick way to check the template still responds to its options.

## pdf/ — PDF viewer

`tanaka-2019.pdf` — the (fictional) paper the markdown notes cite, doing double duty as the PDF-viewer fixture.
