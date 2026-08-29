"""Sensitivity grids over WACC and terminal exit multiple."""
from __future__ import annotations
import pandas as pd
from .dcf import enterprise_value


def per_share_grid(a, waccs=None, exits=None) -> pd.DataFrame:
    waccs = waccs or [0.080, 0.085, 0.090, 0.095, 0.100]
    exits = exits or [5.0, 5.5, 6.0, 6.5, 7.0]
    data = {f"{w:.1%}": [enterprise_value(a, wacc=w, exit_multiple=x)["per_share"]
                         for x in exits] for w in waccs}
    return pd.DataFrame(data, index=[f"{x:.1f}x" for x in exits])
