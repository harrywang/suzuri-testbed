#!/usr/bin/env python3
"""Python rendering check.

Syntax highlighting for embedded ``.py`` files landed on 2026-08-21. Open this
file in Suzuri and walk the checklist. Linked from [[grinding-the-ink]].

- [ ] Section 1 highlights keywords, builtins and comments distinctly
- [ ] Section 2 keeps decorators and type hints on one token colour each
- [ ] Section 3 renders f-string braces as code, not as literal text
- [ ] Section 4 keeps a triple-quoted string closed even when it holds ``` fences
- [ ] Section 5 renders CJK identifiers and strings without clipping the line
- [ ] Section 6 colours hex, underscore and complex numeric literals
- [ ] Section 7 highlights ``match``/``case`` as keywords, not as names
- [ ] Section 8 runs clean under ``python3 code/python-rendering-check.py``

The module is stdlib-only on purpose, so the checklist can end with a real run.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from functools import lru_cache
from typing import Iterable, Iterator

# --- 1. keywords, builtins, comments ---------------------------------------

STONES: tuple[str, ...] = ("Duan", "She", "Tao")
TAU_GRID = [t / 10 for t in range(5, 400)]  # minutes, 0.5 .. 39.9


def samples() -> Iterator[tuple[float, float]]:
    """Grinding time in minutes against measured optical density."""
    yield from (
        (1.0, 0.21), (2.0, 0.38), (4.0, 0.62), (6.0, 0.78),
        (8.0, 0.88), (12.0, 0.99), (16.0, 1.04), (24.0, 1.08),
    )


# --- 2. decorators, dataclasses, type hints --------------------------------


@dataclass(frozen=True, slots=True)
class Fit:
    """A saturating exponential ``D(t) = d_inf * (1 - exp(-t / tau))``."""

    d_inf: float
    tau: float
    sse: float
    stone: str = "Duan"
    residuals: list[float] = field(default_factory=list)

    def density(self, t: float) -> float:
        return self.d_inf * (1.0 - math.exp(-t / self.tau))

    @property
    def half_time(self) -> float:
        return self.tau * math.log(2)


@lru_cache(maxsize=None)
def _cached_exp(x: float) -> float:
    return math.exp(x)


# --- 3. f-strings ----------------------------------------------------------


def report(fit: Fit, *, width: int = 34) -> str:
    label = f"{fit.stone!r} stone"
    return (
        f"{label:<{width}} d_inf={fit.d_inf:.3f}  "
        f"tau={fit.tau:.2f} min  t50={fit.half_time:6.2f} min  "
        f"sse={fit.sse:.2e}  {'ok' if fit.sse < 1e-2 else 'CHECK'}"
    )


# --- 4. a triple-quoted string that holds markdown -------------------------

NOTE_TEMPLATE = """
# Fit for {stone}

Density saturates at **{d_inf:.2f}** with a time constant of {tau:.1f} min.

```python
fit.density(12.0)  # -> {at12:.3f}
```

Ratios live in [[duan-ratios]]; the source is [@tanaka2019, p. 41].
"""

# --- 5. CJK identifiers and strings -----------------------------------------

硯 = "suzuri"  # noqa: N816 - the mark itself, kept for the highlighter
产地 = {"Duan": "广东", "She": "安徽", "Tao": "甘肃"}
GRADE = "1甲"  # the She stone's grade, as printed on the box


def 描述(stone: str) -> str:
    """Return a one-line CJK description of *stone*."""
    return f"{stone}硯 · 产地{产地.get(stone, '不明')} · 等级{GRADE}"


# --- 6. numeric literals ---------------------------------------------------

INK_BLACK = 0x17130F
PAPER_CREAM = 0xEFE6D5
GRAINS_PER_STICK = 1_200_000
PLANCK_ISH = 6.626e-34
ROTATION = 0.70710678 + 0.70710678j
BINARY_MASK = 0b1010_1010
OCTAL_PERM = 0o755

# --- 7. match / case, walrus, comprehensions -------------------------------


def classify(fit: Fit) -> str:
    match fit:
        case Fit(sse=sse) if sse > 1.0:
            return "diverged"
        case Fit(tau=tau) if tau < 1.0:
            return "instant"
        case Fit(stone="Duan" | "She" as stone, d_inf=d) if d > 1.0:
            return f"deep-{stone.lower()}"
        case _:
            return "nominal"


def fit_samples(points: Iterable[tuple[float, float]] = ()) -> Fit:
    """Grid-search ``tau``; solve ``d_inf`` in closed form for each candidate."""
    data = list(points) or list(samples())
    best: Fit | None = None

    for tau in TAU_GRID:
        basis = [1.0 - _cached_exp(-t / tau) for t, _ in data]
        if not (denom := sum(b * b for b in basis)):
            continue
        d_inf = sum(b * d for b, (_, d) in zip(basis, data)) / denom
        resid = [d - d_inf * b for b, (_, d) in zip(basis, data)]
        if (sse := sum(r * r for r in resid)) < (best.sse if best else math.inf):
            best = Fit(d_inf=d_inf, tau=tau, sse=sse, residuals=resid)

    assert best is not None, "TAU_GRID must not be empty"
    return best


# --- 8. a real run ---------------------------------------------------------


def main() -> int:
    fit = fit_samples()
    print(report(fit))
    print(描述("Duan"))
    print(f"class={classify(fit)}  mark={硯}  ink=#{INK_BLACK:06X}")
    print(
        NOTE_TEMPLATE.format(
            stone=fit.stone, d_inf=fit.d_inf, tau=fit.tau, at12=fit.density(12.0)
        ).strip()
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
