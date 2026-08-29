# Methodology

How this deal book is built, so a reader (or a reviewer) can judge how much weight to put on any given number. This note is the single explanation of *method*; chapter-level judgment calls live in each chapter's own "Assumptions & sources" footnote, and the full input list lives in [`assumptions_log.md`](assumptions_log.md).

## 1. Fiscal-year and currency normalisation

Sun Pharma reports in INR to a 31 March year-end; Organon reports in USD to a 31 December year-end. The two are treated as roughly contemporaneous "FY2025" for comparison purposes, which is a simplification — a ~3-month lag, not a true calendar match. Two consequences follow:

- **FX.** Sun Pharma's INR figures are converted to USD at a single FY2025 reference rate of **₹85.5/USD** wherever a USD figure is shown for Sun. This is a point conversion for illustration, not a precise average-rate or spot-rate translation of each line item — treat cross-currency comparisons as directional, not exact.
- **No calendar-quarter reconciliation.** The model does not restate either company onto a common quarter-end; it compares full fiscal years labelled "FY2025" for both, understanding they end ~3 months apart.

## 2. Adjusted vs. GAAP figures

Organon's "Adjusted EBITDA" and "adjusted net income" are **management-defined** non-GAAP measures (they exclude IPR&D charges, restructuring, and purchase-accounting step-up amortisation, among other items). GAAP net income is shown separately wherever it materially diverges — see Chapter 6 — because the gap itself is a diligence flag (Organon's GAAP net income fell to $187m in FY2025 against $954m adjusted). Sun Pharma's figures are reported (Ind-AS) with no comparable adjusted/GAAP split called out.

## 3. Data hierarchy

1. **Primary** — company filings (Organon 10-K/10-Q/8-K on SEC EDGAR; Sun Pharma results and annual report) and deal-specific press releases. Used wherever available; this is what the DCF, merger model and valuation are anchored to.
2. **High-reliability aggregators** — used for speed (e.g. cross-checks against Macrotrends/StockAnalysis) then tied back to the filing before being treated as an input.
3. **Analyst estimates** — anything not disclosed (synergy phasing detail, WACC inputs, terminal multiple, peer set) is built by the analyst and explicitly flagged as such in the chapter it appears in. These are the numbers a reviewer should stress-test hardest.

Every chapter ends with an "Assumptions & sources" section that tags each figure as disclosed, inferred, or estimated. `05_Data/DATA_SOURCES.docx` maps every dataset used to its source, reliability tier, and update frequency. `05_Data/raw/Organon_Primary_Source_Verification.docx` is a later pass that re-derived Organon's core balance-sheet inputs directly from SEC EDGAR XBRL and confirmed them against the figures used throughout the book (see the changelog).

## 4. Valuation methodology (Chapter 7)

Three methods are triangulated, deliberately not averaged into a single point estimate:

- **DCF.** Standalone, unlevered, 5-year explicit forecast (2026–2030) off FY2025 actuals, plus a terminal value. Exit-multiple terminal value (6.0x EV/EBITDA) is used in preference to a Gordon-growth perpetuity, cross-checked against it, because an ex-growth, declining-brands asset is better anchored to a peer-implied exit multiple than to a long-run growth assumption. WACC is built bottom-up (CAPM cost of equity, pre-tax cost of debt, 65/35 target weights) plus a small company-specific premium for the decline/governance profile — see the build in Chapter 7.2 and the live `Assumptions` tab of the Excel model.
- **Trading comparables.** A peer set of diversified generics/specialty companies with comparable off-patent and biosimilars exposure (Viatris, Teva, Sandoz, Hikma, Dr Reddy's, Cipla, Lupin). Indian peers are shown for context but excluded from the applied range because of a materially different growth/market profile.
- **Precedent transactions.** Prior pharma M&A at comparable multiples, used as the upper anchor — precedent multiples typically embed a control premium and/or synergy value that a standalone DCF does not.

The **football field** (Chapter 7.7) and the **scenario/tornado analysis** (Chapters 7.8 and 9.3) are how the three methods and the key swing variables (terminal exit multiple, revenue trajectory, margin, WACC) are reconciled into a single view of where $14.00/share sits.

## 5. Merger model methodology (Chapter 8)

All-cash, debt-funded, no new Sun shares issued — so accretion/dilution collapses to a single question: does Organon's after-tax earnings yield exceed the after-tax cost of the capital used to buy it? The model:

- Builds **Sources & Uses** and a **purchase-price allocation** (book equity written off, an intangible step-up amortised over 15 years, a deferred-tax liability on the step-up, goodwill as the plug) directly off the Excel `Assumptions` tab — those figures, not independently rounded prose, are the source of truth (see the changelog for a reconciliation pass that aligned the two).
- Computes interest on the **opening** debt balance each year (not the average or closing balance) specifically to avoid a circular reference between interest, cash flow, and paydown — a standard simplification; the live workbook notes where an iterative-calculation toggle would be needed to relax it.
- Treats the resulting EPS accretion (~+60% in Year 1) as a **by-product of leverage and scale**, not a scorecard for whether the deal creates value — the chapter is explicit that the binding tests are Organon's free-cash-flow durability and the bridge refinancing, not the headline accretion number.

## 6. Live model vs. narrative chapters

The Excel workbook (`02_Excel_Model/Sun_Pharma_Organon_Integrated_Model.xlsx`) is formula-linked end-to-end (Assumptions → Historicals → DCF → Sources & Uses → PPA → Debt Schedule → Accretion → Football Field), and its `Assumptions` tab is the single input sheet everything else derives from. The Word chapters narrate and interpret those outputs. Where the two must agree exactly (e.g. Sources & Uses totals, the PPA goodwill plug), the chapters are written to match the workbook's computed values, not independently re-rounded — see `CHANGELOG.md` for the pass that reconciled a rounding drift between the two.
