---
csl: apa
---

# Citation insert check

The citation picker searches this vault's `.bib` files and, when Zotero is running with its local API on, the Zotero library too. Picking a Zotero item writes the entry to `refs/refs.bib` at the vault root under a key Suzuri mints, copies the PDF to `refs/<key>.pdf`, and inserts the citation at the cursor. This note is for a Zotero that holds at least one paper with a PDF; the checks below assume the SkillsBench preprint (arXiv 2602.12670), but any paper works if you adjust the search words.

One-time setup: in Zotero, Settings → Advanced → tick "Allow other applications on this computer to communicate with Zotero". Without it the picker still searches the vault and its footer names the box to tick.

- [ ] Section 1 inserts a Zotero paper and records it in `refs/`
- [ ] Section 2 offers vault entries first and dedupes a paper already in the vault
- [ ] Section 3 renders the hover card in the frontmatter's style
- [ ] Section 4 turns the References heading into a formatted list
- [ ] Section 5 opens the PDF in a split
- [ ] Section 6 emits the right syntax in `.tex` and `.typ`

## 1. Insert from Zotero

Put the cursor at the end of this sentence and press `cmd-alt-c`: agent skills raise pass rates on expertise-heavy tasks

Type `skills`. After a beat the list shows the SkillsBench preprint with its authors and year, marked "Zotero". Press Enter. Expect, in this order:

- the sentence now ends with the chip `[@li2026skillsbench]` (first author's surname, year, first title word);
- `refs/refs.bib` exists at the vault root with one `@misc{li2026skillsbench,` entry and no `file =` line;
- `refs/li2026skillsbench.pdf` exists beside it;
- the chip is the ordinary citation color, not the red of an unresolved key.

## 2. Vault first, no duplicates

Press `cmd-alt-c` again with an empty query: the list starts with this vault's own entries (`hayashi2003`, `wong1987`, `okada2015`, `fourtreasures2024` from `md/references.bib`, plus whatever `refs/refs.bib` now holds), each marked "in vault as @key". Type `skills` again: the paper appears once, as the vault entry, not a second time from Zotero. Esc closes without inserting.

Multi-select: open the picker, type `ink`, press `tab` on two entries, then Enter. Expect one group like `[@hayashi2003; @okada2015]`.

## 3. Hover card

Hover the chip from Section 1. The card is the reference in APA (`Li, X., Liu, Y., …`), then **In text:** `(Li et al., 2026)`, then the style name. Change the frontmatter above to `csl: ieee` and hover again: the reference is now numbered IEEE style. Change it back.

## 4. References list

The heading at the bottom of this note is special: once one citation in the note resolves, the heading renders as a block that also lists every cited work, formatted in the frontmatter's style, in the style's order. Nothing is typed under it. Cite a second paper anywhere above and the list grows; put the cursor on the heading's line to see the plain `## References` source and move away to get the list back.

## 5. Open the source

Put the cursor inside the chip from Section 1 and press `cmd-alt-o`. `refs/li2026skillsbench.pdf` opens in a split to the right. Press it again: the existing tab is reused, no second split. On a key with no PDF, such as `[@wong1987]`, a toast says so and nothing opens.

## 6. Other syntaxes

Open `latex/latex-rendering-check.tex` and press `cmd-alt-c`, pick anything: the insert is `\cite{key}`. In `typst/typst-rendering-check.typ` it is `@key`. Both write to the same `refs/refs.bib`. Undo the inserts afterwards; those fixtures have their own reference PDFs.

## References
