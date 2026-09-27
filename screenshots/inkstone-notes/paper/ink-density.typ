#set page(margin: 2.4cm)
#set text(font: "New Computer Modern", size: 11pt)
#set par(justify: true)

#align(center)[
  #text(17pt)[*Ink density as a function of grinding time*] \
  #v(4pt)
  H. Wang · Suzuri Lab \
  #v(2pt)
  #text(9pt)[August 2026]
]

#v(10pt)

*Abstract.* We measure the optical density of hand-ground ink against grinding time for two inkstones, and fit a saturating exponential.

= Method

Sticks were ground on a Duan stone at constant pressure. Density $D(t)$ was sampled every 30 seconds:

$ D(t) = D_infinity (1 - e^(-t / tau)) $

where $tau$ is the characteristic grinding time.

= Results

For the 1782 Duan sample, $tau = 11.4$ minutes and $D_infinity = 1.63$. Grinding past twenty minutes produced no measurable gain.
