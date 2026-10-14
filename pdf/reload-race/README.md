# PDF reload race

Checks that the PDF viewer re-extracts a document's text after the file is replaced on disk, rather than keeping the glyph positions of the document it was showing before.

This is the failure behind "I can't select text in the PDF until I compile again". A live typeset preview rewrites its PDF on every pause in typing, and `reload_document` used to clear the extracted layouts while the previous extraction was still running. That extraction refilled the map across the await for the new metadata, and `extract_all_text` skips its work once the map holds a layout per page, so the new document was never extracted. Selection then hit-tested against coordinates from the replaced document, and clicks landing where the old layout had no glyph cleared the selection instead of starting one.

The two fixtures differ in page count as well as text, so a single stale page is enough to satisfy the skip guard — `long.pdf` has six pages, `short.pdf` has one.

## Running it

```sh
./swap.sh reset          # doc.pdf = long.pdf
```

Open `doc.pdf` in Suzuri, wait for it to render, then:

```sh
./swap.sh race           # replaces it mid-extraction
```

Click in the PDF pane and press cmd-c, which copies the whole document when nothing is selected. The clipboard should hold `SHORTDOCUMENTMARKER`. `LONGDOCUMENTMARKER` means the viewer is still describing the replaced document.

`./swap.sh race 0.4` widens the gap between the two writes if the machine is fast enough to finish extracting before the second one lands.

`doc.pdf` is a copy made by the script. `long.pdf` and `short.pdf` were built with `tectonic -X compile long.tex` and the same for `short.tex`; any LaTeX engine produces equivalent fixtures, since all that matters is that one is several pages and the other is one, and that each carries its own marker.
