# Organon & Co. — Primary-Source Verification (SEC EDGAR)

**Purpose:** validate the key model inputs against Organon's *actual* SEC filings, replacing the earlier estimates. All figures below are from Organon's structured XBRL data on SEC EDGAR (CIK 0001821825), cross-checked to the filing that reported them.

## Verified anchor figures (FY2025, year ended 31 Dec 2025)

| Input | Model used | 10-K actual | Source (accession / form) | Match? |
|---|---:|---:|---|:--:|
| Shares outstanding | ~260m | **260,315,650** (as of 17 Feb 2026) | 0001628280-26-011125 · FY2025 10-K (filed 24 Feb 2026) | ✅ exact |
| Cash & equivalents | $574m | **$574m** (31 Dec 2025) | 0001628280-26-011125 · FY2025 10-K | ✅ exact |
| Long-term debt (noncurrent) | ~$8.64bn | **$8,628m** (31 Dec 2025) | 0001628280-26-011125 · FY2025 10-K | ✅ ~exact |
| **Net debt** | **~$8.1bn** | **~$8.05bn** ($8,628m − $574m) | derived | ✅ |

**Conclusion:** every headline input in the DCF, merger model, and valuation (shares 260m; net debt ~$8.1bn) is confirmed against the primary 10-K. No model change required; the earlier "to be confirmed from proxy" flags are now resolved.

## Verified 5-year balance-sheet series (US$ m, per 10-K/10-Q XBRL)

| Year-end | Cash & equiv. | Long-term debt (noncurrent) | Net debt (approx.) |
|---|---:|---:|---:|
| 2021 | 737 | 9,125 | 8,388 |
| 2022 | 706 | 8,905 | 8,199 |
| 2023 | 693 | 8,751 | 8,058 |
| 2024 | 675 | 8,860 | 8,185 |
| 2025 | 574 | 8,628 | 8,054 |

*(Chapter 6 used lightly rounded figures for 2023–24 cash; the differences are <$40m and immaterial. The FY2025 anchors are exact.)*

## Source URLs (SEC EDGAR, CIK 0001821825)

- Filing index (all Organon filings): https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001821825&type=&dateb=&owner=include&count=100
- Shares outstanding (XBRL): https://data.sec.gov/api/xbrl/companyconcept/CIK0001821825/dei/EntityCommonStockSharesOutstanding.json
- Cash (XBRL): https://data.sec.gov/api/xbrl/companyconcept/CIK0001821825/us-gaap/CashAndCashEquivalentsAtCarryingValue.json
- Long-term debt (XBRL): https://data.sec.gov/api/xbrl/companyconcept/CIK0001821825/us-gaap/LongTermDebtNoncurrent.json
- FY2025 10-K accession: 0001628280-26-011125 (filed 24 Feb 2026)

*Still to pull for a full upgrade: the Sun/Organon merger proxy (PREM14A/DEFM14A) for the deal's exact diluted-share and net-debt bridge and any fairness-opinion projections. The above confirms the balance-sheet anchors used throughout the book.*
