# Citation rendering check

Pandoc-style `[@key]` citations now resolve against the project's `.bib` files. This vault carries `md/references.bib` with four entries — `hayashi2003`, `wong1987`, `okada2015`, `fourtreasures2024` — and the repo's `latex/` and `typst/` folders carry three more: `tanaka2019`, `mizuta1968`, `chen2021`. Every `.bib` in the opened project is indexed, so which keys resolve depends on which folder is open: open the testbed root and all seven resolve; open only `md/` and just the four local ones do.

- [ ] Section 1 chips resolved keys and red-flags unresolved ones
- [ ] Section 2 offers cite-key completion after `@` with reference details
- [ ] Section 3 clears a red flag live when the `.bib` gains the entry
- [ ] Section 4 leaves near-misses as prose
- [ ] Section 5 hands back source on touch

## 1. Resolution

A resolved key keeps the ordinary citation chip: grinding pressure matters more than duration [@hayashi2003], and the classic manual agrees [@wong1987].

A group resolves per key, not per group: quarry provenance is contested [@okada2015; @hayashi2003].

This key exists in no `.bib` anywhere and must show error-colored text with a wavy underline: the effect was first reported by [@phantom1999].

Cross-folder resolution (only when the testbed *root* is open): saturation curves [@tanaka2019] and the survey [@chen2021]. With only `md/` open these two must flag as unresolved instead — that is correct behavior, not a bug.

An entry with no author still resolves and still chips: see the overview [@fourtreasures2024].

@mizuta1968

## 2. Completion

On a fresh line below, type `[@` — a completion menu should list every indexed key. Keep typing (`[@hay`) and it should narrow to `hayashi2003`. The selected entry's card shows title, authors, and year; `wong1987` must show **1987** even though its `.bib` entry uses a BibLaTeX `date` field, and `fourtreasures2024` shows its title with no author line. Accepting a completion must produce `[@hayashi2003]`-style text with exactly one `@`.

Try it here: @okada2015



Completion also works bare, without brackets — and per Pandoc a bare key is a citation exactly like a bracketed one: the @hayashi2003 you accepted on the line above must be a chip, and an unresolved bare word like @somehandle must flag red the same way [@phantom1999] does. Emails and infix `@` still never register: curator@example.com.

## 3. Live reload

`[@phantom1999]` in Section 1 is red. Open `md/references.bib` in a split, paste the entry below at the end, and save — the flag on this note must clear within a beat, without touching this note.

```bibtex
@article{phantom1999,
  author  = {Phantom, Alice},
  title   = {A Reference That Arrives Late},
  journal = {Journal of Reproducibility},
  year    = {1999}
}
```

Delete it again and save: the red flag must come back.

## 4. Near-misses

None of the following is a citation, and none may chip or flag:

- An email address: reach me at curator@example.com
- A plain bracket: [not a citation] and [see chapter 4]
- In code: `[@nope]` stays raw
- A markdown link label: [@looks-like-one](https://example.org) is a link, not a citation
- Mid-word: price@quantity is prose

## 5. Reveal on touch

Click into [@hayashi2003] — the chip must hand back the raw `[@hayashi2003]` for editing, exactly as before this feature. Move the cursor away and the chip returns, still resolved.
