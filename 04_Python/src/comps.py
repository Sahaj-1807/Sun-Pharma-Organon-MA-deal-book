"""Trading comparables and precedent transactions."""
from __future__ import annotations
import pandas as pd
from . import config


def _implied(ebitda, mult_low, mult_high, net_debt, shares):
    ev_lo, ev_hi = mult_low * ebitda, mult_high * ebitda
    return dict(ev_low=ev_lo, ev_high=ev_hi,
                ps_low=(ev_lo - net_debt) / shares,
                ps_high=(ev_hi - net_debt) / shares)


def trading_comps(a, ebitda: float = 1910.0) -> dict:
    tbl = pd.DataFrame(sorted(config.TRADING_COMPS.items(), key=lambda kv: kv[1]),
                       columns=["peer", "ev_ebitda"])
    lo, hi = config.TRADING_RELEVANT_RANGE
    return {"table": tbl, **_implied(ebitda, lo, hi, a.net_debt, a.shares)}


def precedent_transactions(a, ebitda: float = 1910.0) -> dict:
    tbl = pd.DataFrame(sorted(config.PRECEDENTS.items(), key=lambda kv: kv[1]),
                       columns=["precedent", "ev_ebitda"])
    lo, hi = config.PRECEDENT_RELEVANT_RANGE
    return {"table": tbl, **_implied(ebitda, lo, hi, a.net_debt, a.shares)}
