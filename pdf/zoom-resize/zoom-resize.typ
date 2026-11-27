// Fixture for pdf-zoom-resize-check.md. Every line names its page and line,
// so after a resize or zoom the line at the top of the view says exactly
// where the viewer put you. Rebuild: typst compile zoom-resize.typ
#set page(paper: "us-letter", margin: (x: 0.8in, y: 0.7in), numbering: "1 / 1")
#set text(size: 11pt)

#let pages = 30
#for page-number in range(1, pages + 1) {
  if page-number > 1 { pagebreak() }
  align(center, text(size: 40pt, weight: "bold")[Page #page-number])
  v(4pt)
  for line in range(1, 15) {
    [p#page-number · L#line — #lorem(9)]
    linebreak()
  }
  v(6pt)
  // Fine print to pinch into: unreadable at fit width, sharp when zoomed.
  align(center, block(stroke: 0.5pt + gray, inset: 6pt, grid(
    columns: 12,
    gutter: 2pt,
    ..range(1, 85).map(cell => text(size: 3pt)[p#(page-number)·c#cell]),
  )))
  align(center, text(size: 9pt, style: "italic")[Figure #page-number: fine print, pinch over it to read])
  v(4pt)
  $ integral_0^infinity e^(-x^2) dif x = sqrt(pi) / 2 quad "(page" #page-number ")" $
  for line in range(15, 26) {
    [p#page-number · L#line — #lorem(9)]
    linebreak()
  }
}
