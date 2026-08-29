#!/usr/bin/env python3
"""Run the full Sun Pharma / Organon valuation and print a console report.

Usage:
    python run_valuation.py            # print report
    python run_valuation.py --charts   # also regenerate PNG charts into ../06_Visuals/python
Runs fully offline from bundled data. All figures are analyst estimates (see report Ch.7-8).
"""
import argparse
import os
import pandas as pd

from src import Assumptions
from src.wacc import wacc_breakdown
from src.dcf import enterprise_value, project_fcf, terminal_value_gordon
from src.sensitivity import per_share_grid
from src.comps import trading_comps, precedent_transactions
from src.merger import accretion, ppa
from src.ratios import add_ratios, cagr
from src.data import load_organon_financials

pd.set_option("display.float_format", lambda v: f"{v:,.2f}")
pd.set_option("display.width", 120)


def rule(t):
    print("\n" + "=" * 78 + f"\n{t}\n" + "=" * 78)


def main(charts=False):
    a = Assumptions()

    rule("WACC BUILD")
    for k, v in wacc_breakdown(a).items():
        print(f"  {k:<28} {v:.2%}")

    rule("DCF — PROJECTION (US$ mm)")
    print(project_fcf(a).to_string(index=False))

    rule("DCF — VALUATION")
    ev = enterprise_value(a)
    print(f"  PV of UFCF (2026-30)   ${ev['pv_fcf']:,.0f} m")
    print(f"  PV of terminal value   ${ev['pv_tv']:,.0f} m  (exit {ev['exit_multiple']:.1f}x)")
    print(f"  Enterprise value       ${ev['ev']:,.0f} m")
    print(f"  Equity value           ${ev['equity']:,.0f} m")
    print(f"  Equity value / share   ${ev['per_share']:.2f}")
    print(f"  Premium to $14 offer    {ev['premium_to_offer']:+.1%}")
    print(f"  (Gordon TV cross-check  ${terminal_value_gordon(a):,.0f} m)")

    rule("DCF — SENSITIVITY (equity value / share, $)")
    print(per_share_grid(a).to_string())

    rule("TRADING COMPS")
    tc = trading_comps(a)
    print(tc["table"].to_string(index=False))
    print(f"  Implied equity/share (6.0-7.5x): ${tc['ps_low']:.1f} - ${tc['ps_high']:.1f}")

    rule("PRECEDENT TRANSACTIONS")
    pc = precedent_transactions(a)
    print(pc["table"].to_string(index=False))
    print(f"  Implied equity/share (7.0-9.0x): ${pc['ps_low']:.1f} - ${pc['ps_high']:.1f}")

    rule("PURCHASE PRICE ALLOCATION (US$ mm)")
    for k, v in ppa(a).items():
        print(f"  {k:<20} {v:,.0f}")

    rule("ACCRETION / (DILUTION)")
    acc = accretion(a)
    print(acc.to_string(index=False, formatters={"accretion": lambda x: f"{x:+.1%}"}))

    rule("ORGANON HISTORICALS + RATIOS")
    hist = add_ratios(load_organon_financials())
    print(hist.to_string(index=False))
    print(f"  Revenue CAGR 2021-25: {cagr(hist['revenue']):+.2%}")

    if charts:
        outdir = os.path.join(os.path.dirname(__file__), "..", "06_Visuals", "python")
        from src.charts import generate_all
        paths = generate_all(a, outdir)
        rule("CHARTS WRITTEN")
        for p in paths:
            print("  " + os.path.normpath(p))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--charts", action="store_true", help="regenerate PNG charts")
    main(**vars(ap.parse_args()))
