"""Data access: bundled historicals (offline) + optional live prices.

Live market data (yfinance) is optional and wrapped so the toolkit runs fully
offline from the bundled CSVs in ``04_Python/data``.
"""
from __future__ import annotations
import os
import pandas as pd

_HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(_HERE, "data")


def load_organon_financials() -> pd.DataFrame:
    """Organon FY2021-2025 historicals (US$ mm)."""
    return pd.read_csv(os.path.join(DATA_DIR, "organon_financials.csv"))


def load_peers() -> pd.DataFrame:
    return pd.read_csv(os.path.join(DATA_DIR, "peers.csv"))


def get_prices(ticker: str, period: str = "2y"):
    """Optional live prices via yfinance; returns None if unavailable."""
    try:
        import yfinance as yf
        df = yf.Ticker(ticker).history(period=period)
        return df if not df.empty else None
    except Exception:
        return None
