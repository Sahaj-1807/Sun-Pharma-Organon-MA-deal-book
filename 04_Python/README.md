# Part 3 — Python Valuation Toolkit

An independent, reproducible re-derivation of the Sun Pharma / Organon valuation.
Runs fully offline from bundled data; live market data (yfinance) is optional.
Every output should tie to the research report (Ch.6-8) and the Excel models — if
Python and Excel disagree, that is an error flag.

## Layout

```
04_Python/
├── run_valuation.py     # console report: WACC, DCF, sensitivity, comps, PPA, accretion, ratios
├── dashboard.py         # optional Streamlit app (sliders drive the DCF live)
├── Launch_Dashboard.command  # macOS: double-click to launch the dashboard, no terminal typing
├── requirements.txt
├── data/
│   ├── organon_financials.csv   # FY2021-25 historicals (US$ mm)
│   └── peers.csv                # trading-comp multiples
└── src/
    ├── config.py        # all assumptions (single source of truth) — edit here
    ├── data.py          # bundled historicals + optional yfinance prices
    ├── ratios.py        # margins, growth, leverage, CAGR
    ├── wacc.py          # CAPM cost of equity, after-tax cost of debt, WACC, beta (OLS)
    ├── dcf.py           # unlevered FCF projection + EV / equity / per-share
    ├── comps.py         # trading comps + precedent transactions
    ├── sensitivity.py   # WACC x exit-multiple per-share grid
    ├── merger.py        # PPA/goodwill + accretion / dilution
    └── charts.py        # deal-book-themed football field, sensitivity, DCF build
```

## Quick start

```bash
cd "04_Python"
pip install -r requirements.txt          # pandas/numpy/matplotlib are the only hard deps
python run_valuation.py                  # full console report
python run_valuation.py --charts         # also writes PNGs to ../06_Visuals/python
streamlit run dashboard.py               # optional interactive app
```

**macOS shortcut:** double-click `Launch_Dashboard.command` in Finder instead of typing the
`streamlit run` command — it opens a Terminal window, installs any missing packages on first
run, and launches the dashboard in your browser. Close the window (or press Ctrl+C) to stop it.
If Finder ever refuses to run it ("unidentified developer"), right-click the file and choose
Open once — it will run normally after that.

## What it reproduces

- **WACC** \~9.0% (CAPM + company-specific premium)
- **DCF**: EV \~$12.4bn, equity \~$16.5/share, \~+18% vs the $14.00 offer
- **Sensitivity**: WACC 8-10% x exit 5.0-7.0x
- **Comps / precedents**: implied per-share ranges
- **Merger**: goodwill \~$1.3bn, \~+60% Year-1 EPS accretion
- **Ratios**: Organon FY21-25 margins, growth, leverage

## Notes

- `src/config.py` holds every assumption; change inputs there and re-run.
- Live prices/beta via `data.get_prices()` / `wacc.estimate_beta()` are optional and
  degrade gracefully offline.
- All figures are analyst estimates anchored on FY2025 actuals; sources in
  `05_Data/DATA_SOURCES.docx`.
