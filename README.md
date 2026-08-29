# Sun Pharma / Organon — M&A Deal Book

**Cross-border acquisition of Organon & Co. (NYSE: OGN) by Sun Pharmaceutical Industries Ltd. (NSE/BSE: SUNPHARMA)**
$14.00 per share, all-cash · \~$11.75bn enterprise value · announced April 2026 · expected close early 2027

An institutional-grade M&A analysis package: a 10-chapter research report, a live formula-linked Excel model, an independent Python valuation toolkit, and a pitchbook — all built from public filings and disclosed deal terms, and cross-checked against each other.

> **Focus:** end-to-end M&A analysis — valuation, financial modelling, and cross-border (India-outbound) deal structuring.

---

## The deal in one paragraph

Sun Pharma, India's largest drugmaker (net cash \~$3.1bn at FY25), is acquiring Organon — a Merck women's-health / biosimilars / established-brands spin-off — for $14.00/share in cash. Because Organon carries \~$8.6bn of gross debt against only \~$3.6bn of equity value at the offer price, the \~$11.75bn enterprise value is overwhelmingly a **debt-assumption / refinancing** story rather than an equity purchase. Sun is funding via a $12bn committed bridge (Sun Pharma USA) plus internal accruals, targeting \~2.3x post-deal net leverage. This is the largest acquisition ever by an Indian pharma company, and the differentiator of this analysis is the **India-outbound financing and tax structuring** it requires.

## Why this deal is analytically interesting

1. **It's a leverage story, not a premium story.** The headline is a \~$3.6bn equity cheque, but the real capital at risk is the \~$8bn debt load being absorbed and refinanced.
2. **Cross-border structuring.** An Indian acquirer funding a US target through offshore vehicles (Sun Pharma USA), bridge-to-bond take-out, euro issuance, and the associated tax/treaty routing.
3. **A declining-asset base.** Organon's revenue is flat-to-declining (Established Brands in secular decline) — the model must test whether Women's Health + Biosimilars growth offsets it.
4. **Fiscal-year mismatch and FX.** Sun Pharma reports in INR to a March year-end; Organon in USD to a December year-end. Normalising these correctly is part of the craft — see `docs/methodology.md`.

## What's in this repo

The research report (`01_Research_Report/`) is ten chapters, each a standalone `.docx` with its own supporting charts:

| # | Chapter | What it covers |
|---|---|---|
| 1 | Executive Summary | One-page deal snapshot, key figures, investment highlights and risks, deal timeline |
| 2 | Industry Analysis | Global pharma, women's-health and biosimilars market sizing; Porter's Five Forces; SWOT |
| 3 | Company Analysis | Sun Pharma and Organon profiled — segments, management, ownership, FY2025 financial snapshot |
| 4 | Strategic Rationale | Why each side is doing the deal; synergy taxonomy (cost, revenue, financial, tax); deleveraging path |
| 5 | Deal Structure | Consideration, value bridge, Sources & Uses, financing and debt, regulatory approvals, timeline |
| 6 | Financial Analysis | Five-year historicals for both companies, balance sheet/leverage, comparative ratio dashboard |
| 7 | Valuation | DCF (with full WACC build), trading comps, precedent transactions, football field, scenarios |
| 8 | Merger Model | Sources & Uses, purchase-price allocation, debt schedule, accretion/dilution |
| 9 | Risk Analysis | Risk heatmap and register, tornado sensitivity, key-risk deep dives |
| 10 | Recommendation | Deal attractiveness, expected value creation, key assumptions, alternative scenarios, final verdict |

Chapters 6–9 each ship with their own live Excel workbook (`Financial_Analysis.xlsx`, `Valuation_Model.xlsx`, `Merger_Model.xlsx`, `Risk_Register.xlsx`) in addition to the fully integrated model in `02_Excel_Model/`.

## Repository structure

```
Project 1 - Sun Pharma-Organon MA/
├── README.md                     ← this file
├── 01_Research_Report/           ← Part 1: one folder per chapter, each with its .docx,
│                                    a /charts subfolder, and (Ch.6-9) a live Excel model
├── 02_Excel_Model/               ← Part 2: integrated .xlsx model (14 tabs, 236 formulas;
│                                    historicals → DCF → Sources & Uses → PPA → debt → accretion)
├── 03_Pitchbook/                 ← Part 6: 17-slide IB pitchbook (.pptx)
├── 04_Python/                    ← Part 3: independent valuation & automation toolkit (see its own README)
│   ├── src/                      ← reusable modules (data, ratios, dcf, comps, wacc, merger, charts)
│   ├── notebooks/                ← reserved for exploratory analysis notebooks
│   └── requirements.txt
├── 05_Data/                      ← Part 4: data layer
│   ├── raw/                      ← as-downloaded filings / primary-source verification
│   ├── processed/                ← cleaned CSV/Parquet used by the model & Python
│   └── DATA_SOURCES.docx         ← full sourcing map (mandatory/recommended/optional)
├── 06_Visuals/                   ← Part 7: exported charts (football field, waterfalls, etc.)
└── docs/                         ← methodology, the model's assumptions log, and this project's changelog
    ├── methodology.md
    ├── assumptions_log.md
    └── CHANGELOG.md
```

## How the components integrate

```
        05_Data (raw filings → processed CSVs)
                     │
        ┌────────────┼─────────────┐
        ▼            ▼             ▼
   04_Python     02_Excel      01_Research_Report
   (ratios,      (historicals, (narrative +
    DCF, comps,   forecast,     conclusions cite
    charts)       DCF, merger)  model outputs)
        │            │             │
        └──────┬─────┴──────┬──────┘
               ▼            ▼
          06_Visuals    03_Pitchbook
          (chart PNGs)  (deck pulls charts + numbers)
```

Single source of truth: the model inputs live in `02_Excel_Model`'s `Assumptions` tab and are mirrored in `docs/assumptions_log.md`. The Python toolkit re-derives the same valuation independently as a cross-check — if Excel and Python disagree, that's an error flag, same as if a chapter and the workbook it narrates disagree (see `docs/CHANGELOG.md` for a reconciliation pass that caught exactly this).

## Tooling & how to reproduce

The Python toolkit (`04_Python/`) is a standalone, offline-reproducible re-derivation of the valuation — it doesn't read the Excel file, it recomputes from the same assumptions independently, which is the point of the cross-check.

```bash
cd "04_Python"
pip install -r requirements.txt          # pandas, numpy, matplotlib, openpyxl are the hard deps
python run_valuation.py                  # console report: WACC, DCF, sensitivity, comps, PPA, accretion, ratios
python run_valuation.py --charts         # also writes PNGs to ../06_Visuals/python
streamlit run dashboard.py               # optional interactive app — sliders drive the DCF live
```

**macOS:** double-click `04_Python/Launch_Dashboard.command` in Finder to launch the interactive
dashboard directly — no terminal needed. See `04_Python/README.md` for details.

Every assumption the toolkit uses lives in `04_Python/src/config.py` — change an input there and every downstream number (DCF, sensitivity grid, merger model) recomputes. See `04_Python/README.md` for the module-by-module layout.

The Excel model (`02_Excel_Model/Sun_Pharma_Organon_Integrated_Model.xlsx`) needs no setup — open it in Excel or LibreOffice Calc; every tab after `Assumptions` is formula-linked, so changing an input there flows through to the DCF, Sources & Uses, PPA, debt schedule, accretion and football field automatically.

## Build status

| Part | Deliverable | Status |
|---|---|---|
| 1 | Research report — all 10 chapters (Ch.1–10) | ✅ Done |
| 2 | Integrated Excel model (`02_Excel_Model/`, 14 tabs, 236 formulas) | ✅ Done |
| — | Chapter Excel models (Ch.6 financials, Ch.7 valuation, Ch.8 merger, Ch.9 risk register) | ✅ Done |
| 3 | Python toolkit (`04_Python/`) | ✅ Done |
| 4 | Data-source map | ✅ Done |
| 5 | Repo structure + README | ✅ Done |
| 6 | Pitchbook (.pptx, 17 slides) | ✅ Done |
| 7 | Primary-source verification (Organon 10-K / SEC EDGAR) | ✅ Done |
| — | `docs/` methodology, assumptions log, changelog | ✅ Done |

**All parts complete.** See `docs/CHANGELOG.md` for the build history and the most recent data-consistency pass.

## Key figures (anchor data)

| Metric | Organon (FY2025, Dec-YE) | Sun Pharma (FY2025, Mar-YE) |
|---|---|---|
| Revenue | $6.2bn | ₹520.4bn revenue from operations (\~$6.1bn); total income incl. other income \~₹545bn |
| Adj. EBITDA | $1.91bn (30.7% margin) | ₹153.0bn (\~$1.8bn) |
| Adj. net income | $954m ($3.66/sh) | ₹120.0bn (\~$1.4bn) |
| Net debt / (cash) | \~+$8.1bn net debt | \~(-$3.1bn) net cash |

*FX (\~₹85.5/USD) and fiscal-period normalisation are documented in `docs/methodology.md`. All figures traceable to the filings listed in `05_Data/DATA_SOURCES.docx`.*

**Primary-source verification:** Organon's key model inputs are confirmed against its actual FY2025 10-K (SEC EDGAR, CIK 0001821825) — shares **260,315,650**, cash **$574m**, long-term debt **$8,628m** (net debt \~$8.05bn). See `05_Data/raw/Organon_Primary_Source_Verification.docx` and `organon_balance_sheet_series_EDGAR.csv`. The inferred inputs (\~260m shares, \~$8.1bn net debt) matched the filing.

## The bottom line (Chapter 10)

Three independent methods (DCF, trading comps, precedent transactions) triangulate Organon's standalone value; the $14.00 offer sits at the low end of DCF/comps and below precedents — base-case DCF implies \~$16.5/share, a \~15–20% margin of safety. The transaction is materially EPS accretive from Year 1 (\~+60%, rising to \~+75% by Year 3), but that accretion is leverage-driven and explicitly **not** the basis for the recommendation. The report's conclusion is **PROCEED**, conditional on (1) Organon's established-brands free cash flow holding up close to modelled and (2) terming out the $12bn bridge at a manageable spread — the two variables the risk chapter identifies as the deal's real, concentrated risk.
