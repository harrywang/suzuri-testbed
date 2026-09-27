"""Fit the saturating exponential in paper/ink-density.typ to grinding samples.

D(t) = D_inf * (1 - exp(-t / tau)), sampled every 30 seconds on a Duan stone.
"""

from __future__ import annotations

import csv
import math
from pathlib import Path

SAMPLES = Path(__file__).parent / "samples.csv"


def load_samples(path: Path) -> list[tuple[float, float]]:
    with path.open() as file:
        return [(float(row["minutes"]), float(row["density"])) for row in csv.DictReader(file)]


def model(minutes: float, d_inf: float, tau: float) -> float:
    return d_inf * (1 - math.exp(-minutes / tau))


def squared_error(samples: list[tuple[float, float]], d_inf: float, tau: float) -> float:
    return sum((density - model(minutes, d_inf, tau)) ** 2 for minutes, density in samples)


def fit(samples: list[tuple[float, float]]) -> tuple[float, float]:
    # A coarse grid is plenty: two parameters, a few dozen samples, and the
    # paper reports tau to one decimal place.
    best = min(
        (squared_error(samples, d_inf / 100, tau / 10), d_inf / 100, tau / 10)
        for d_inf in range(100, 250)
        for tau in range(20, 300)
    )
    return best[1], best[2]


if __name__ == "__main__":
    samples = load_samples(SAMPLES)
    d_inf, tau = fit(samples)
    print(f"D_inf = {d_inf:.2f}, tau = {tau:.1f} min over {len(samples)} samples")
