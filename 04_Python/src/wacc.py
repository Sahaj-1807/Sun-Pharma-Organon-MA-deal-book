"""WACC and beta utilities."""
from __future__ import annotations
import numpy as np


def cost_of_equity(risk_free: float, beta: float, erp: float) -> float:
    """CAPM cost of equity."""
    return risk_free + beta * erp


def after_tax_cost_of_debt(pretax: float, tax: float) -> float:
    return pretax * (1 - tax)


def wacc(a) -> float:
    """Weighted average cost of capital (base case, incl. company premium)."""
    ke = cost_of_equity(a.risk_free, a.beta, a.equity_risk_premium)
    kd = after_tax_cost_of_debt(a.pretax_cost_of_debt, a.tax_rate)
    capm_wacc = a.weight_equity * ke + a.weight_debt * kd
    return capm_wacc + a.company_premium


def wacc_breakdown(a) -> dict:
    ke = cost_of_equity(a.risk_free, a.beta, a.equity_risk_premium)
    kd = after_tax_cost_of_debt(a.pretax_cost_of_debt, a.tax_rate)
    capm_wacc = a.weight_equity * ke + a.weight_debt * kd
    return {
        "cost_of_equity": ke,
        "after_tax_cost_of_debt": kd,
        "wacc_capm": capm_wacc,
        "company_premium": a.company_premium,
        "wacc_base": capm_wacc + a.company_premium,
    }


def estimate_beta(stock_returns: np.ndarray, market_returns: np.ndarray) -> float:
    """Levered beta via OLS slope of stock vs market returns.

    Falls back to raising if inputs are empty; callers should guard for data.
    """
    x = np.asarray(market_returns, dtype=float)
    y = np.asarray(stock_returns, dtype=float)
    if x.size < 2 or y.size != x.size:
        raise ValueError("need aligned return series of length >= 2")
    cov = np.cov(y, x)
    return float(cov[0, 1] / cov[1, 1])
