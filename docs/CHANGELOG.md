# Changelog

Dates reflect when each pass was made to the project's files.

## 2026-08-29 - Data-consistency pass + docs/ populated

Prompted by a full error/misprint review ahead of publishing this project to GitHub. Findings and fixes:

- **Sun Pharma FY2025 revenue corrected.** The README and `05_Data/DATA_SOURCES.docx` stated Sun Pharma's FY2025 revenue as ₹545.4bn (~$6.4bn) - that figure is actually Sun's *total income including other income*. Every analysis chapter that uses Sun's revenue (Ch.3, Ch.6, and the Excel model) consistently uses **revenue from operations, ₹520.4bn**, which converts to ~$6.1bn at the model's own ₹85.5/USD reference rate (not ~$6.2bn, which was a conversion slip). Fixed in `README.md`, `05_Data/DATA_SOURCES.docx`, and `01_Research_Report/Chapter 3 - Company Analysis/03_Company_Analysis.docx`.
- **Sources & Uses / PPA reconciled to the live Excel model.** Chapter 5 (Deal Structure) and Chapter 8 (Merger Model) narrated an equity purchase price of $3,650m / accruals of $2,250m / totals of $12,000m - but the linked `Assumptions` tab of `02_Excel_Model/Sun_Pharma_Organon_Integrated_Model.xlsx` computes $3,640m (260m shares x $14.00 exactly), a $2,240m balancing-plug for accruals, and totals of $11,990m. The PPA table (allocable excess, goodwill) inherited the same $10m drift. Chapters 5 and 8 are now updated to match the workbook exactly - the workbook was correct throughout; the narrative prose had drifted from it.
- **Merger-model accretion table footed.** Chapter 8's Year 2/Year 3 after-tax synergy line items were adjusted by $1m each (199 to 198, 284 to 283) so the printed components sum exactly to the printed "Pro forma net income" totals ($2,152m / $2,237m) - a pure rounding-presentation fix with no effect on any conclusion.
- **`docs/` populated.** The README had promised methodology notes, an assumptions log (`docs/assumptions_log.md`) and this changelog, but the folder was empty. `methodology.md`, `assumptions_log.md` and this file were added.
- **Broken file references fixed.** Chapter 1 (Executive Summary) and the README pointed to `05_Data/DATA_SOURCES.md` - the actual file is `05_Data/DATA_SOURCES.docx`. Corrected.
- **README rewritten** to be a fuller front door to the project: chapter-by-chapter contents, tooling/tech stack, and how the pieces cross-check each other.

No changes were made to any modelling *judgment* (growth rates, WACC, synergy sizing, multiples, scenario cases) - this pass only reconciled numbers that should have matched each other exactly and didn't, and fixed stale file references.

## 2026-08-25 - Primary-source verification

Organon's core model inputs (shares outstanding, cash, long-term debt, net debt) were re-derived directly from SEC EDGAR XBRL data (CIK 0001821825, FY2025 10-K, filed 24 Feb 2026) and checked against the figures already in use throughout the book. All four anchors matched (shares outstanding matched exactly at 260,315,650; net debt matched within ~$50m, an immaterial, pre-existing rounding gap). See `05_Data/raw/Organon_Primary_Source_Verification.docx` and the accompanying `organon_balance_sheet_series_EDGAR.csv` for the 5-year series pulled alongside it. No model changes were required.

## 2026-07-27 - Initial build

Research report (Chapters 1-10), the integrated Excel model (14 tabs / 236 formulas), the Python valuation toolkit, the data-sourcing map, the exported chart set, and the 17-slide pitchbook were built out.
