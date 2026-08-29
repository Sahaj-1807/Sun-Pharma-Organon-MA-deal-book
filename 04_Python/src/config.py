"""Central assumptions for the Sun Pharma / Organon valuation toolkit.

All inputs mirror the research report (Ch.6-8) and the Excel models so the
Python re-derivation is an independent cross-check. Edit values here only.
Figures are analyst assumptions anchored on FY2025 actuals; see report Ch.7.
"""
from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class Assumptions:
    # --- Target base year (Organon FY2025, US$ mm) ---
    base_revenue: float = 6216.0
    ebitda_margin: float = 0.30
    d_and_a: float = 300.0
    capex: float = 160.0
    delta_nwc: float = 40.0
    tax_rate: float = 0.19
    revenue_growth: List[float] = field(default_factory=lambda: [-0.02, -0.01, 0.0, 0.01, 0.01])

    # --- Terminal value ---
    terminal_exit_multiple: float = 6.0          # EV/EBITDA
    terminal_growth: float = 0.005               # for Gordon cross-check

    # --- WACC build ---
    risk_free: float = 0.045
    equity_risk_premium: float = 0.055
    beta: float = 1.05
    pretax_cost_of_debt: float = 0.07
    weight_equity: float = 0.65
    weight_debt: float = 0.35
    company_premium: float = 0.0034              # decline / governance premium

    # --- Capitalisation ---
    shares: float = 260.0                        # mm, target diluted (inferred)
    net_debt: float = 8100.0                     # US$ mm
    offer_price: float = 14.00                   # US$/share

    # --- Merger inputs (acquirer = Sun Pharma) ---
    fx_inr_usd: float = 85.5
    sun_net_income: float = 1278.0               # US$ mm
    sun_shares: float = 2399.3                   # mm
    organon_adj_net_income: float = 954.0
    organon_existing_interest: float = 450.0     # pre-tax
    new_acq_debt: float = 9500.0
    debt_rate: float = 0.06
    cash_used: float = 2250.0
    forgone_rate: float = 0.04
    synergy_run_rate: float = 350.0
    synergy_phasing: List[float] = field(default_factory=lambda: [0.30, 0.70, 1.00])
    ppa_intangible_stepup: float = 2000.0
    intangible_life: float = 15.0


# Illustrative peer / precedent multiples (tie to filings before use)
TRADING_COMPS: Dict[str, float] = {
    "Viatris": 6.0, "Teva": 7.2, "Hikma": 7.8, "Dr Reddy's": 11.0, "Cipla": 12.5,
}
TRADING_RELEVANT_RANGE = (6.0, 7.5)   # ex-India Western generics/mature brands

PRECEDENTS: Dict[str, float] = {
    "Mylan+Upjohn -> Viatris (2020)": 5.5,
    "STADA / Bain-Cinven (2017)": 8.0,
    "Teva / Allergan Generics (2016)": 10.0,
}
PRECEDENT_RELEVANT_RANGE = (7.0, 9.0)

# Palette (deal-book theme)
PALETTE = dict(navy="#1F3864", blue="#2E5496", steel="#8FA9C9",
               grey="#808080", lgrey="#BFBFBF", ink="#222222",
               green="#1E5B34", red="#8B1A1A")
