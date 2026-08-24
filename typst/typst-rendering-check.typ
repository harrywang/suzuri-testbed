#set document(
  title: "Ink Density Saturation in Duan Inkstones: A Typst Rendering Check",
  author: "Harry Wang",
)
#set page(paper: "a4", margin: 2.5cm)
#set text(size: 11pt)
#set heading(numbering: "1.")
#set math.equation(numbering: "(1)")

#align(center)[
  #text(size: 17pt, weight: "bold")[
    Ink Density Saturation in Duan Inkstones:\
    A Typst Rendering Check
  ]

  Harry Wang \
  August 2026
]

#align(center)[
  #block(width: 85%)[
    #text(weight: "bold")[Abstract.]
    A short sample document for testing `.typ` rendering, syntax
    highlighting, and citation handling. The content mirrors the
    vault's notes on grinding ink: density saturates as a function of
    grind time, and the stone --- not the stick --- sets the ceiling.
  ]
]

= Introduction

Grinding ink is a slow circular process: water is added _a few drops_
at a time, and the stone decides how dark the ink gets. Prior work
established the density--time relationship empirically @tanaka2019,
while the classical treatment of stone provenance goes back much
further @mizuta1968. A modern survey is given by @chen2021.

= Model

Let $D(t)$ denote ink density after $t$ minutes of grinding. Density
follows a saturating exponential,

$ D(t) = D_max (1 - e^(-t\/tau)) $ <eq-density>

where $D_max$ is the stone-specific ceiling and $tau$ the time
constant. Saturation is effectively reached near $t^* approx 4$ min,
since from @eq-density,

$ D(t^*) / D_max = 1 - e^(-t^*\/tau) approx 0.98 quad "for" tau approx 1 "min". $

Inline math also needs checking: the residual is
$epsilon(t) = D_max e^(-t\/tau)$, and $lim_(t -> infinity) epsilon(t) = 0$.

= Stones

@tab-stones lists the stones used in the vault's notes.

#figure(
  table(
    columns: 4,
    align: (left, left, right, left),
    table.header([*Stone*], [*Origin*], [*Year*], [*Grind*]),
    [Duan], [Guangdong], [1782], [slow],
    [She], [Anhui], [1854], [fine],
  ),
  caption: [Inkstones referenced in the grinding notes.],
) <tab-stones>

= Conclusion

If this document compiles with `typst compile`, renders with
highlighting, and resolves all three citations from `references.bib`,
the check passes.

#bibliography("references.bib", style: "chicago-author-date")
