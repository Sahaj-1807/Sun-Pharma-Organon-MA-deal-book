"""Merger accretion / dilution model (acquirer = Sun Pharma)."""
from __future__ import annotations
import pandas as pd


def ppa(a) -> dict:
    equity_purchase = a.offer_price * a.shares
    excess = equity_purchase - 700.0                      # less est. book equity
    dtl = a.ppa_intangible_stepup * a.tax_rate
    goodwill = excess - a.ppa_intangible_stepup + dtl
    amort_pretax = a.ppa_intangible_stepup / a.intangible_life
    return dict(equity_purchase=equity_purchase, excess=excess,
                intangible_stepup=a.ppa_intangible_stepup, dtl=dtl,
                goodwill=goodwill, amort_pretax=amort_pretax,
                amort_aftertax=amort_pretax * (1 - a.tax_rate))


def accretion(a) -> pd.DataFrame:
    t = a.tax_rate
    organon_prefin = a.organon_adj_net_income + a.organon_existing_interest * (1 - t)
    new_int = a.new_acq_debt * a.debt_rate * (1 - t)
    forgone = a.cash_used * a.forgone_rate * (1 - t)
    amort = ppa(a)["amort_aftertax"]
    rows = []
    for yr, ph in enumerate(a.synergy_phasing, start=1):
        syn = a.synergy_run_rate * ph * (1 - t)
        pf_ni = a.sun_net_income + organon_prefin - new_int - forgone - amort + syn
        std_eps = a.sun_net_income / a.sun_shares
        pf_eps = pf_ni / a.sun_shares
        rows.append(dict(year=yr, pro_forma_ni=pf_ni,
                         sun_eps_usd=std_eps, pf_eps_usd=pf_eps,
                         sun_eps_inr=std_eps * a.fx_inr_usd,
                         pf_eps_inr=pf_eps * a.fx_inr_usd,
                         accretion=pf_eps / std_eps - 1))
    return pd.DataFrame(rows)
