# suzuri-notes

A test vault for [Suzuri](https://github.com/harrywang/suzuri). The `notes/` files exercise markdown live preview; `code/` exercises Python execution and notebook rendering.

This README covers the one-time Python setup needed before anything in `code/` will run.

## What Suzuri can actually do with Python

There are two separate features, and they are at different stages:

| | What it is | Status |
| --- | --- | --- |
| **REPL** | Run code inline in a normal `.py` file, cell by cell, with output rendered under each cell | Shipped and on by default |
| **Notebook editor** | Open `.ipynb` as a real notebook UI (cells, execution counts, rich outputs) | Built and compiled in, but gated behind an unreleased upstream feature flag |

Both use the same Jupyter kernel underneath, so the setup below serves both.

## One-time setup with uv

Suzuri finds Python kernels by scanning the **worktree root** for Python environments, then running `python -c "import ipykernel"` against each one. Only environments where that import succeeds are offered as kernels. So the environment has to live at the root of the folder you open in Suzuri — here, `suzuri-notes/` itself.

From the vault root:

```sh
cd ~/sandbox/suzuri-notes
uv venv                        # creates .venv/ using your default Python
uv pip install ipykernel       # the only hard requirement
```

Add whatever else your notes actually use:

```sh
uv pip install numpy pandas matplotlib
```

That is the whole setup. You do **not** need to install `jupyter`, and you do not need `jupyter kernelspec` registration — Suzuri launches the kernel directly as `python -m ipykernel_launcher`, and sets `VIRTUAL_ENV` and `PATH` to point at `.venv` for you.

### Why uv specifically

Homebrew's Python is marked externally managed, so `pip install ipykernel` against it fails outright. A `uv venv` sidesteps that and is fast enough that a throwaway environment per vault costs nothing.

There is also a payoff inside Suzuri. Because uv writes a `uv = <version>` marker into `.venv/pyvenv.cfg`, Suzuri detects the environment kind as `uv`, and its recovery path for a missing `ipykernel` then runs `uv pip install ipykernel --python <path>` instead of falling back to `python -m pip` — which against an externally managed Python would just fail again.

That recovery path is worth knowing precisely, because it is easy to look for and not find:

- It is **not a button**. It is a row in the REPL kernel picker. An environment missing `ipykernel` is still listed, dimmed, with an orange `ipykernel not installed` label next to its name. **Selecting that row** is what triggers the install; you get an "Installing ipykernel in ..." toast, and the kernel is assigned automatically when it finishes.
- It lives in the **REPL menu in the editor toolbar** — the REPL icon at the top right of the editor, visible while a `.py` file is focused. It requires `"jupyter": {"enabled": true}` in settings, which is the default.
- It does **not** exist in the notebook editor. The `.ipynb` kernel selector, in the bar at the bottom of the notebook, changes the kernel directly with no `ipykernel` check at all — so picking an environment that lacks it there fails without offering to fix anything.

So if you skip the setup above, the one-click repair is reachable from a `.py` file and not from a notebook. Running `uv pip install ipykernel` yourself is the reliable path either way.

## Running code in a `.py` file

This works in the Suzuri you already have installed, with no flags.

Open `code/python-rendering-check.py`. Split it into cells with `# %%` separators — that is the jupytext convention, and Suzuri understands it:

```python
# %%
import numpy as np
np.arange(10) ** 2

# %%
print("second cell")
```

Put the cursor in a cell and press `ctrl-shift-enter` (`repl::Run`). The first run spins up the kernel, which takes a few seconds; after that it stays warm. Output renders inline beneath the cell.

If no kernel is picked automatically, run `repl: refresh kernelspecs` from the command palette, then choose the `.venv` environment.

## Running an `.ipynb` notebook

Opening a `.ipynb` in a normal Suzuri build shows **raw JSON**. That is expected and is not a broken install: the notebook editor exists and is compiled into the binary, but it only registers itself as the handler for `.ipynb` when a feature flag is on.

This is fixed on the Suzuri branch `worktree-notebook-default-on`, which turns notebooks on by default and adds an `ipykernel` install path to the notebook's own kernel picker. Once you build and install that, `.ipynb` just opens as a notebook and the rest of this section no longer applies.

Until then, launch the installed app's binary directly with the dev escape hatch:

```sh
LOCAL_NOTEBOOK_DEV=1 /Applications/Suzuri.app/Contents/MacOS/zed ~/sandbox/suzuri-notes
```

Launching from Finder or with `open -a Suzuri` will **not** work — macOS does not forward environment variables that way, so it has to be the binary path.

Note that setting `"feature_flags": {"notebooks": "on"}` in `settings.json` does not work either, in a release build. Suzuri gates feature-flag overrides themselves on debug builds or a Zed staff account, so the override is ignored.

Once the notebook opens, the keybindings are:

| Key | Action |
| --- | --- |
| `cmd-enter` | Run the current cell |
| `shift-enter` | Run and advance |
| `cmd-shift-enter` | Run all cells |
| `cmd-m` / `cmd-shift-m` | Add a code / markdown cell |
| `cmd-shift-r` | Restart the kernel |
| `alt-up` / `alt-down` | Move a cell |

The editor also has vim-style command and edit modes — `enter` to enter edit mode, `d d` to delete a cell.

Treat this as a preview. Upstream still has open work on dirty-state tracking and notebook metadata round-tripping, so save behavior can be rough. Do not put anything here you have not committed.

## Troubleshooting

**No kernels listed.** The environment is not at the worktree root, or `ipykernel` is missing. Confirm with `.venv/bin/python -c "import ipykernel"` — if that errors, the kernel will never appear. Then `repl: refresh kernelspecs`.

**Kernel dies immediately.** Usually a Python version mismatch after recreating `.venv`. Delete and rebuild: `rm -rf .venv && uv venv && uv pip install ipykernel`.

**`.ipynb` still shows JSON with the env var set.** Check you launched `Contents/MacOS/zed` directly and not the `.app`.

## Open item

Making notebooks work without the env var is a small change in the Suzuri fork — giving `NotebookFeatureFlag` an `enabled_for_all() -> true` in `crates/feature_flags/src/flags.rs`. It is three lines, but in a file the fork otherwise leaves alone, so it becomes a permanent merge-conflict surface against upstream. Worth doing only after the preview proves itself useful in practice.
