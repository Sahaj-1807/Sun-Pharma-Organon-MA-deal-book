# Assumptions Log

This mirrors the `Assumptions` tab of `02_Excel_Model/Sun_Pharma_Organon_Integrated_Model.xlsx` — the single input sheet that the DCF, Sources & Uses, PPA, Debt Schedule and Accretion tabs all link to. If a number below changes, change it here (and in the workbook) and every dependent figure across the model updates; the narrative chapters should then be re-checked against the recomputed outputs (see `CHANGELOG.md` for why that check matters).

Status tags: **Disclosed** = stated in a company filing or deal press release · **Derived** = arithmetic on disclosed figures · **Estimated** = analyst assumption, flagged as such in the relevant chapter.

## Organon — operating assumptions (US$ mm unless noted)

| Input | Value | Status |
|---|---|---|
| Base revenue, FY2025 | 6,216 | Disclosed |
| EBITDA margin (forecast) | 30% | Estimated (vs. 30.7% FY25 actual — slight erosion assumed) |
| D&A | 300 | Estimated |
| Capex | 160 | Estimated (~2.5% of revenue) |
| Change in net working capital | 40 (outflow) | Estimated |
| Tax rate | 19% | Estimated (Organon's low effective rate) |
| Terminal exit multiple | 6.0x EV/EBITDA | Estimated |
| Revenue growth, Yr 1-5 | -2%, -1%, 0%, +1%, +1% | Estimated |

## WACC build

| Input | Value | Status |
|---|---|---|
| Risk-free rate (US 10-yr) | 4.5% | Market data |
| Equity risk premium | 5.5% | Estimated |
| Beta (levered) | 1.05 | Estimated |
| Cost of equity (CAPM) | 10.275% (~10.3%) | Derived |
| Pre-tax cost of debt | 7.0% | Estimated |
| After-tax cost of debt | 5.67% (~5.7%) | Derived |
| Target weights (equity / debt) | 65% / 35% | Estimated |
| WACC (CAPM) | 8.66% (~8.7%) | Derived |
| Company-specific premium | +0.34% (~0.3%) | Estimated (decline / governance) |
| **WACC - base case** | **9.00%** | **Derived** |

## Capitalisation

| Input | Value | Status |
|---|---|---|
| Shares outstanding | ~260m | Disclosed - confirmed exact at 260,315,650 against the FY2025 10-K (see `05_Data/raw/Organon_Primary_Source_Verification.docx`) |
| Net debt | ~$8,100m | Derived (gross debt $8,628m - cash $574m = $8,054m; the model carries a lightly-rounded ~$8,100m) |
| Offer price | $14.00/share | Disclosed |

## Merger inputs

| Input | Value | Status |
|---|---|---|
| FX (INR per USD, FY25) | 85.5 | Estimated reference rate |
| Sun standalone net income | $1,278m (₹10,929cr ÷ 85.5) | Derived |
| Sun shares outstanding | 2,399.3m | Disclosed |
| Organon adjusted net income | $954m | Disclosed |
| Organon existing pre-tax interest (added back) | $450m | Estimated |
| Sun EBITDA | $1,765m | Derived from ₹153.0bn ÷ 85.5 |
| Organon EBITDA | $1,910m | Disclosed |
| New acquisition debt | $9,500m | Estimated (within the disclosed ~$9.25-9.75bn range) |
| Blended new-debt rate | 6.0% | Estimated |
| Sun cash used (accruals) | $2,240m | **Derived - balancing plug** (Total sources - new debt - Organon cash); do not hand-enter this, it must foot to Total uses |
| Forgone rate on cash used | 4.0% | Estimated |
| Synergy run-rate | $350m | Disclosed (company guidance, "up to ~$500m") |
| Synergy phasing (Yr1 / Yr2 / Yr3) | 30% / 70% / 100% | Estimated |
| PPA intangible step-up | $2,000m | Estimated |
| Intangible amortisation life | 15 years | Estimated |
| Organon book equity (est.) | $700m | Estimated |
| Equity purchase price | $3,640m (= 260m x $14.00) | Derived |
| FCF available for debt sweep | $1,800m/yr | Estimated (flat; illustrative, not a forecast) |

## Notes on precision

- **Equity purchase price is exactly $3,640m** in the model (260m shares x $14.00). Using Organon's exact diluted share count (260,315,650) instead of the rounded ~260m gives ~$3,644m - a $4m difference, immaterial, but the reason two "precise-looking" numbers ($3,640m and $3,644m) can both appear defensible depending on which share count is used.
- **Sun internal accruals ($2,240m) is a plug**, not an independent input - it is whatever balances Total sources to Total uses. If the new-debt amount, Organon cash, or the equity purchase price changes, this figure changes with it; it should never be hand-typed into a chapter without recomputing.
- Chapter-level footnotes (each chapter's own "Assumptions & sources" section) are the authoritative record of what's disclosed vs. estimated *for that chapter's specific claims* (e.g. synergy magnitude, regulatory timeline). This log is the authoritative record of the *quantitative model inputs*. Where the two overlap, this log and the Excel workbook win - see `CHANGELOG.md`.
