# Math rendering check

Inline and display LaTeX landed on 2026-08-20. Open this note in live preview — cursor parked here on the top lines, so everything below stays rendered — and walk the checklist. Linked from [[grinding-the-ink]].

- [ ] Section 1 typesets inline formulas on the text baseline
- [ ] Section 2 leaves dollar amounts as plain prose
- [ ] Section 3 centers a display formula on its own line
- [ ] Section 4 renders a multi-line matrix and cases block
- [ ] Section 5 keeps the rendering visible below the source while editing
- [ ] Section 6 renders mid-line `$$` inline, not as a block
- [ ] Section 7 shows broken LaTeX as source, never as a blank
- [ ] Section 8 reads naturally as a real note

## 1. Inline math and the baseline

The ink darkens as $E = mc^2$ predicts nothing about, but the formula should sit on the same baseline as this sentence — not float above it. A formula with a descender, like the ratio $\frac{3}{5}$ of water to stone, hangs partly below the line; one without, like $x^2 + y^2 = r^2$, sits flush. Click any of them: the widget swaps to raw LaTeX for editing, and moving the cursor away re-typesets it. Greek should work inline too: the slurry's viscosity $\eta$ rises with grind time $t$ as $\eta(t) = \eta_0 e^{\lambda t}$.

**Broken:** formulas float mid-line, render as literal `$...$` text, or vanish.
**Fixed:** typeset symbols, aligned to the sentence's baseline, revealing their source only under the cursor.

## 2. Dollar amounts stay prose

A Duan stone cost $120 and the She stone $85 at auction — both prices should read exactly as typed. The rule is Obsidian's: a `$` with a space just inside it never opens math, so $ a = b $ also stays literal. But $a=b$ with tight delimiters is math.

**Broken:** the text between the two prices disappears into a garbled formula.
**Fixed:** this whole section is plain prose except the single tight `$a=b$` at the end of the paragraph.

## 3. Display math on its own line

The density of a well-ground ink follows a saturation curve:

$$D(t) = D_{\max}\left(1 - e^{-t/\tau}\right)$$

That formula should stand centered on its own line, larger than inline math, with the `$$` delimiters hidden. Click it to edit.

## 4. Multi-line display math

The delimiters on their own lines — the shape every research note actually uses:

$$
\begin{pmatrix} d_1 \\ d_2 \end{pmatrix} =
\begin{pmatrix} \tau_{11} & \tau_{12} \\ \tau_{21} & \tau_{22} \end{pmatrix}
\begin{pmatrix} w \\ s \end{pmatrix}
$$

And a cases block, with operators that take limits above and below:

$$
\eta(w) = \begin{cases}
\eta_0 & w \le w_c \\
\eta_0 + \sum_{k=1}^{n} \frac{(w - w_c)^k}{k!} & w > w_c
\end{cases}
$$

**Broken:** the block renders as raw source, or the matrix collapses onto one garbled line.
**Fixed:** two centered typeset blocks; the sum shows its limits above and below the Σ.

## 5. Live preview while editing

Put the cursor inside the formula below. The source should reveal for editing — and the rendered result should stay visible as a block *underneath* it, updating as you type. Try changing the exponent.

$$\int_0^\infty e^{-x^2}\,dx = \frac{\sqrt{\pi}}{2}$$

**Broken:** the rendering vanishes the moment the cursor enters the line.
**Fixed:** source above, live rendering below, until the cursor leaves.

## 6. Mid-line display math

A display formula sandwiched in prose — the ratio $$\frac{w}{s} = \frac{3}{5}$$ mid-sentence — cannot take over its whole line without swallowing this text, so it renders inline instead, at inline size.

**Broken:** the words around the formula disappear.
**Fixed:** the sentence reads through, formula typeset in place.

## 7. Broken LaTeX degrades to source

An unclosed fraction like $\frac{3}{$ and an unknown command like $\inkstone{duan}$ do not parse. They must show as their raw source — never a blank, never a crash — so there is something on screen to fix.

## 8. A real passage

Grinding transfers pigment at a rate proportional to pressure $p$ and inversely to the stone's grit spacing $g$, so the mass ground after time $t$ is $m(t) = \frac{\alpha p t}{g}$. Darkness saturates once particle concentration reaches $c^* \approx 0.18$, which for the 1782 Duan stone at three parts water to five parts stone arrives near

$$t^* = \frac{g\, c^* V}{\alpha p} \approx 4 \text{ minutes}$$

of slow circular work — matching what [[inkstone-care]] says the hand learns anyway.
