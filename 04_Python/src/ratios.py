"""Financial-ratio helpers operating on a tidy statements DataFrame.

Expected columns (per period): revenue, ebitda, net_income, gross_debt, cash.
"""
from __future__ import annotations
import pandas as pd


def add_ratios(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out["ebitda_margin"] = out["ebitda"] / out["revenue"]
    out["net_margin"] = out["net_income"] / out["revenue"]
    out["revenue_growth"] = out["revenue"].pct_change()
    if {"gross_debt", "cash"}.issubset(out.columns):
        out["net_debt"] = out["gross_debt"] - out["cash"]
        out["net_debt_to_ebitda"] = out["net_debt"] / out["ebitda"]
    return out


def cagr(series: pd.Series) -> float:
    s = series.dropna()
    n = len(s) - 1
    if n <= 0 or s.iloc[0] <= 0:
        return float("nan")
    return (s.iloc[-1] / s.iloc[0]) ** (1 / n) - 1
