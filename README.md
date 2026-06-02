# Project Osprey — Rolls-Royce Holdings plc Valuation Model

> Institutional-grade DCF valuation, IC memo, pitch deck and interactive dashboard for **Rolls-Royce Holdings plc (LSE: RR.)** following the FY2025 results (released 26-Feb-2026).

[![Made with Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)](#)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.32%2B-FF4B4B?logo=streamlit&logoColor=white)](#)
[![Excel Model](https://img.shields.io/badge/Excel-DCF%20%2B%20Sensitivity-217346?logo=microsoftexcel&logoColor=white)](#)
[![License](https://img.shields.io/badge/license-MIT-lightgrey)](#license)

---

## Headline thesis

| | |
|---|---|
| **Recommendation** | **HOLD** with bias-to-trim |
| **Implied price (base case)** | **898p** (WACC 9.5%, g 2.25%) |
| **Spot price** | 1,208p (21-May-2026) |
| **Implied upside / (downside)** | **(26%)** |
| **Re-engagement level** | 900–950p (FY28 FCF yield ≥ 5.5%) |

The market has re-rated RR. from c.150p (Jan-2023) to 1,208p — an 8x move that prices in flawless execution of the upgraded £5.0–5.3bn FY28 FCF target. On a strict DCF basis the current price is only justified at WACC below 8.5%, i.e. the market is pricing this as an investment-grade utility rather than a cyclical aerospace OEM with c.40% civil exposure. The £7–9bn buyback authorisation signals a credible FCF-yield floor but does not mechanically set one at spot.

---

## Repository structure

```
Project_Osprey_RR_Valuation/
├── 01_Source_Data/
│   └── RR_2025_Raw_Figures.txt          # Raw figures extracted from FY25 results
├── 02_Financial_Models/
│   └── RR_LBO_DCF_Model.xlsx            # 3-tab DCF model (Cover, Assumptions, DCF)
├── 03_IC_Deliverables/
│   ├── RR_Investment_Memo.docx          # 2-page institutional IC memo
│   └── RR_Strategic_Summary.pptx        # 3-slide IC pitch deck
├── 04_Interactive_Dashboard/
│   ├── app.py                           # Streamlit DCF sandbox
│   └── requirements.txt                 # Python dependencies
├── .gitignore
└── README.md                            # This file
```

---

## Methodology

### Free Cash Flow projection

Five-year explicit forecast (2026E–2030E) bridging FY25 actual £3.3bn to the upgraded management mid-point of £5.15bn in FY28 (corridor £5.0–5.3bn), then tapering FCF growth as the engine LLP flywheel matures.

| Year | FCF (£bn) | YoY |
|---|---|---|
| 2025A | 3.30 | — |
| 2026E | 3.70 | +12.1% |
| 2027E | 4.40 | +18.9% |
| 2028E | 5.15 | +17.0% |
| 2029E | 5.45 | +5.8% |
| 2030E | 5.70 | +4.6% |

FY26 and FY28 anchored to management guidance mid-points; intervening years interpolated against a margin walk from 17.3% to 20.5% underlying operating margin.

### WACC build

WACC is constructed bottom-up using a UK-anchored CAPM with a target capital structure consistent with RR.'s current investment-grade profile:

| Component | Value | Source |
|---|---|---|
| Risk-free rate (UK 10Y Gilt) | 4.5% | Bloomberg, May-2026 |
| Equity risk premium | 5.0% | Damodaran mature-market ERP |
| Levered beta | 1.10 | 5Y weekly vs FTSE 100 |
| **Cost of equity (Ke)** | **10.00%** | Rf + β × ERP |
| Pre-tax cost of debt (Kd) | 5.0% | RR senior unsecured notes |
| Tax rate | 25% | UK statutory |
| After-tax Kd | 3.75% | Kd × (1 − t) |
| Equity weight | 92% | Net cash / IG credit profile |
| Debt weight | 8% | |
| **WACC (base case)** | **9.50%** | |

### Terminal value

Gordon-growth perpetuity applied to FY30 FCF:

$$
TV_{2030} = \frac{FCF_{2030} \times (1 + g)}{WACC - g}
$$

Base case `g = 2.25%` (UK long-run CPI plus modest real growth). Mid-year discount convention applied throughout.

### Equity bridge

```
PV of explicit FCF (2026-2030)
+ PV of Terminal Value
= Enterprise Value
+ Net Cash (£1.9bn, 31-Dec-2025)
= Equity Value
÷ Shares Outstanding (~8.30bn)
= Implied Share Price
```

### Sensitivity grid

Two-way Data Table in the Excel model and the Streamlit dashboard cross WACC (8.0–11.0%) against terminal growth (1.5–3.0%). Current price 1,208p is only reachable in the top-left quadrant (WACC ≤ 8.5%) — supporting the rerating-fatigue thesis.

---

## Running the interactive dashboard

The Streamlit app re-runs the DCF in real time as the user adjusts WACC and terminal growth via sliders, and displays a live KPI card with the implied share price.

### Prerequisites
- Python 3.10+
- `pip` or `uv`

### Setup

```bash
# Clone the repo
git clone https://github.com/<your-username>/rolls-royce-valuation-model.git
cd rolls-royce-valuation-model

# (Recommended) create a virtual environment
python -m venv .venv
source .venv/bin/activate     # macOS/Linux
.venv\Scripts\activate        # Windows PowerShell

# Install dependencies
pip install -r 04_Interactive_Dashboard/requirements.txt
```

### Run

```bash
cd 04_Interactive_Dashboard
streamlit run app.py
```

The dashboard will open at `http://localhost:8501`. Adjust the sidebar sliders to stress-test the valuation:

- **WACC / Cost of Equity:** 6.0% – 14.0% (base 9.5%)
- **Terminal growth rate:** 1.0% – 4.0% (base 2.25%)

The script reads FCF projections, net cash, share count and spot price directly from `02_Financial_Models/RR_LBO_DCF_Model.xlsx` so any change to the Excel model flows through to the dashboard.

---

## Key files at a glance

| File | What it is |
|---|---|
| `RR_LBO_DCF_Model.xlsx` | Institutional 3-tab Excel model. Blue hardcodes / black formulas / green cross-sheet links. 117 live formulas, zero errors. Includes 2-way WACC × g sensitivity table. |
| `RR_Investment_Memo.docx` | 2-page IC memo. Erginbilgic turnaround verdict, buyback floor analysis, FY28 execution risk decomposition, four-point action list. |
| `RR_Strategic_Summary.pptx` | 3-slide pitch deck. Executive recommendation, FCF trajectory + buyback math, sensitivity heatmap. |
| `app.py` | Streamlit dashboard reading the xlsx and re-running the DCF on demand. |

---

## Sources

- Rolls-Royce Holdings plc — [2025 Full Year Results](https://www.rolls-royce.com/~/media/Files/R/Rolls-Royce/documents/investors/results/2025-full-year-results/rr-holdings-plc-2025-full-year-results-press-release.pdf) (26-Feb-2026)
- Rolls-Royce Holdings plc — [Interim Share Buyback Programme](https://www.rolls-royce.com/media/press-releases/2025/16-12-2025-interim-share-buyback-programme.aspx) (16-Dec-2025)
- London Stock Exchange — [RR. company page](https://www.londonstockexchange.com/stock/RR./rolls-royce-holdings-plc/company-page)
- Hargreaves Lansdown — [RR. share price](https://www.hl.co.uk/shares/shares-search-results/r/rolls-royce-holdings-plc-ordinary-20p)
- A. Damodaran — Equity Risk Premium dataset (NYU Stern)

---

## License

MIT — see `LICENSE` if added. Prepared for portfolio and educational purposes. Not investment advice.

---

## Author

**Amogh H. H.** — MSc Business Analytics, University of Essex
[LinkedIn](https://linkedin.com/in/amogh-hh-34129a1b9)  |  [Portfolio](https://amogh-h-h-portfolio.vercel.app)
