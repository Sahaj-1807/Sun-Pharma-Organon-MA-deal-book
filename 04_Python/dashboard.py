#!/usr/bin/env python3
"""Optional interactive Streamlit dashboard.

Run:  streamlit run dashboard.py
Sliders drive the DCF live; the football field, sensitivity grid and accretion
recompute on every change. Requires: streamlit (see requirements.txt).
"""
try:
    import streamlit as st
except Exception:  # pragma: no cover
    raise SystemExit("Streamlit not installed. Run: pip install streamlit")

from src import Assumptions
from src.dcf import enterprise_value
from src.sensitivity import per_share_grid
from src.merger import accretion

st.set_page_config(page_title="Sun Pharma / Organon — Valuation", layout="wide")
st.title("Sun Pharma / Organon — Interactive Valuation")
st.caption("Analyst estimates for educational purposes. See research report Ch.7-8.")

a = Assumptions()
c1, c2, c3 = st.columns(3)
a.terminal_exit_multiple = c1.slider("Terminal EV/EBITDA exit", 4.5, 8.0, 6.0, 0.1)
a.beta = c2.slider("Beta", 0.6, 1.4, 1.05, 0.05)
a.ebitda_margin = c3.slider("EBITDA margin", 0.24, 0.34, 0.30, 0.005)
g = st.slider("Annual revenue growth (flat rate applied to all 5 years)", -0.05, 0.03, 0.0, 0.005)
a.revenue_growth = [g] * 5

ev = enterprise_value(a)
m1, m2, m3, m4 = st.columns(4)
m1.metric("Enterprise value", f"${ev['ev']:,.0f}m")
m2.metric("Equity / share", f"${ev['per_share']:.2f}")
m3.metric("vs $14 offer", f"{ev['premium_to_offer']:+.1%}")
m4.metric("WACC", f"{ev['wacc']:.2%}")

st.subheader("DCF sensitivity — equity value / share ($)")
st.dataframe(per_share_grid(a).style.format("${:.1f}").background_gradient(cmap="RdYlGn"))

st.subheader("Accretion / (dilution)")
st.dataframe(accretion(a).style.format({"accretion": "{:+.1%}"}))
