"""Discounted cash flow valuation for Organon (standalone, unlevered)."""
from __future__ import annotations
import pandas as pd
from .wacc import wacc as compute_wacc


def project_fcf(a) -> pd.DataFrame:
    """Five-year unlevered FCF projection."""
    rev, r = [], a.base_revenue
    for g in a.revenue_growth:
        r *= (1 + g)
        rev.append(r)
    rows = []
    for i, rv in enumerate(rev):
        ebitda = rv * a.ebitda_margin
        ebit = ebitda - a.d_and_a
        nopat = ebit * (1 - a.tax_rate)
        ufcf = nopat + a.d_and_a - a.capex - a.delta_nwc
        rows.append(dict(year=2026 + i, revenue=rv, ebitda=ebitda, ebit=ebit,
                         nopat=nopat, ufcf=ufcf))
    return pd.DataFrame(rows)


def enterprise_value(a, wacc: float | None = None, exit_multiple: float | None = None) -> dict:
    """DCF EV / equity / per-share using an exit-multiple terminal value."""
    w = compute_wacc(a) if wacc is None else wacc
    xm = a.terminal_exit_multiple if exit_multiple is None else exit_multiple
    proj = project_fcf(a)
    disc = [(1 + w) ** -(i + 1) for i in range(len(proj))]
    pv_fcf = float((proj["ufcf"].values * disc).sum())
    tv = xm * proj["ebitda"].iloc[-1]
    pv_tv = tv * (1 + w) ** -len(proj)
    ev = pv_fcf + pv_tv
    equity = ev - a.net_debt
    per_share = equity / a.shares
    return dict(wacc=w, exit_multiple=xm, pv_fcf=pv_fcf, tv=tv, pv_tv=pv_tv,
                ev=ev, equity=equity, per_share=per_share,
                premium_to_offer=per_share / a.offer_price - 1)


def terminal_value_gordon(a, wacc: float | None = None) -> float:
    """Gordon-growth terminal value cross-check (informational)."""
    w = compute_wacc(a) if wacc is None else wacc
    proj = project_fcf(a)
    last = proj["ufcf"].iloc[-1]
    return last * (1 + a.terminal_growth) / (w - a.terminal_growth)
