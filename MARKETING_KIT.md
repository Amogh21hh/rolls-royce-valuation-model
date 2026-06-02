# Project Osprey — Employer Marketing Kit

**Purpose:** Take this project from "files on a laptop" to "recruiters in your inbox."
**Owner:** Amogh H. H.  |  **Target roles:** Finance Analyst · Credit Risk Analyst · Accounting Analyst · Equity Research (London, entry-level)
**Read order:** Execution Plan → LinkedIn → CV → Cold Outreach

---

## PART 0 — Execution Plan (Day 0 → Day 14)

### Day 0 — Get the project LIVE (90 minutes)

| # | Action | Time | Why it matters |
|---|---|---|---|
| 1 | Move `Project_Osprey_RR_Valuation` folder to your Desktop | 2 min | Required for git push from your local machine |
| 2 | PowerShell test: `cd 04_Interactive_Dashboard && pip install -r requirements.txt && streamlit run app.py` | 10 min | Confirms the dashboard runs on your machine before public |
| 3 | Take 3 screenshots of the live dashboard (KPI card, sliders moved, FCF chart) | 5 min | Featured-section media on LinkedIn |
| 4 | Follow `DEPLOY.md` Step 3 (alternative) — `gh repo create rolls-royce-valuation-model --public --source=. --remote=origin --push` | 15 min | Repo live on GitHub |
| 5 | Deploy to Streamlit Cloud: <https://share.streamlit.io> → New app → main file path `04_Interactive_Dashboard/app.py` | 15 min | **Highest-leverage step in this entire plan** — recruiters click and interact |
| 6 | Add live badge to README, commit, push: `[![Live](https://img.shields.io/badge/Live-Demo-FF4B4B?logo=streamlit)](YOUR-STREAMLIT-URL)` | 10 min | Repo visitors see "Live Demo" immediately |
| 7 | Pin the repo on your GitHub profile | 1 min | First thing recruiters see on github.com/amogh |
| 8 | Note both URLs in a sticky note: `STREAMLIT_URL` and `GITHUB_URL` | 1 min | You'll paste them ~20 times this week |

**Stop-criterion for Day 0:** Streamlit URL works in incognito Chrome with no errors.

### Day 1 — LinkedIn assault (60 minutes)

| # | Action | Time |
|---|---|---|
| 9 | Update LinkedIn Headline (text in §1A below) | 2 min |
| 10 | Rewrite LinkedIn About section (text in §1B) | 5 min |
| 11 | Add Project Osprey to Featured section x2 — Streamlit URL + GitHub URL (text in §1C) | 5 min |
| 12 | Add Project Osprey to Projects section (text in §1D) | 5 min |
| 13 | Reorder Skills section to surface modelling first (list in §1E) | 5 min |
| 14 | Publish the announcement post (text in §2) at **Tuesday or Wednesday, 7:30–8:30 AM UK time**. Never Friday. | 10 min |
| 15 | Post the live URL in the FIRST COMMENT of your own post within 30 seconds | 1 min |
| 16 | Engage with 5–10 London finance recruiter / VP / Director posts within 2 hours of publishing | 25 min |

### Day 2–7 — Applications + outreach (4 hrs/day)

| # | Action | Daily target |
|---|---|---|
| 17 | Apply to high-fit roles with new CV bullets (§3) | 5 per day |
| 18 | Send cold messages on LinkedIn using template in §4 | 5 per day |
| 19 | Track everything in a Google Sheet (`Applications_Tracker.xlsx`) — columns: Date, Company, Role, Status, Contact, Last action | Continuous |
| 20 | Update portfolio site `amogh-h-h-portfolio.vercel.app` with Project Osprey card (copy in §5) | One-off, Day 2 |

### Day 7–14 — Amplify

| # | Action |
|---|---|
| 21 | Cross-post adapted version on Reddit (r/FinancialCareers, r/CFA) and Wall Street Oasis (Off-Topic forum) |
| 22 | Email University of Essex Careers Office and ask for inclusion in the MSc Business Analytics newsletter |
| 23 | Send the live link to 3 LinkedIn connections at your TARGET firms (NatWest, Lloyds, Schroders, M&G, Big 4) with the cold-message template |
| 24 | Refresh your post once if engagement is high — comment "Update: now at X demo plays. Thanks for the feedback." (re-surfaces in feeds) |

**Stop-criterion for Day 14:** 25+ applications submitted, 25+ cold messages sent, ≥3 recruiter conversations booked.

---

## PART 1 — LinkedIn Profile Updates

### §1A — Headline (replaces current)

```
Finance & Credit Risk Analyst | DCF Modelling • Python • Credit Risk ML | MSc Business Analytics @ Essex | Built an interactive valuation engine for Rolls-Royce (£100bn co.) — link below
```

**Why this works:**
- Leads with the *job title* recruiters Boolean-search.
- Drops three keyword anchors (DCF / Python / Credit Risk ML).
- Names a marquee FTSE 100 company.
- "Link below" prompts scrolling and clicks.

### §1B — About section (replace whatever is currently there)

```
Finance professional combining institutional-grade modelling with Python automation.

I recently built Project Osprey — a full DCF valuation engine for Rolls-Royce Holdings plc (LSE: RR., ~£100bn market cap) covering the FY25 results released February 2026. The model spans a 3-tab Excel workbook (117 formulas, zero errors), a 2-page Investment Committee memo, a 3-slide pitch deck, and an interactive Streamlit dashboard that re-runs the DCF in real time as users adjust WACC and terminal growth.

▸ Live demo: [YOUR-STREAMLIT-URL]
▸ Source code & methodology: [YOUR-GITHUB-URL]

Core skills:
• Financial modelling — DCF, sensitivity analysis, equity bridge, WACC (CAPM build against UK 10Y Gilts)
• Credit risk — Logistic Regression, Random Forest, XGBoost on LendingClub / German Credit datasets; SHAP/LIME for model explainability
• Data — R, advanced Excel, Python (pandas, openpyxl, Streamlit, Plotly)
• Communication — institutional memo writing, IC pitch decks, scenario analysis

Currently targeting Finance Analyst, Credit Risk Analyst, and Accounting Analyst roles in London. Full UK right to work, immediate start.

Open to conversations — DM me or amoghmallikarjun0321@gmail.com.
```

### §1C — Featured section (TWO items — Streamlit URL first, GitHub second)

**Item 1 — click "Add featured" → "Add a link" → paste Streamlit URL**

Title:
```
Project Osprey — Live DCF Valuation Engine (Rolls-Royce, LSE: RR.)
```
Description:
```
Interactive institutional DCF for a £100bn FTSE 100 aerospace company. Adjust WACC and terminal growth sliders; the implied share price recalculates in real time. Built end-to-end in Python + Streamlit, fed by a 117-formula Excel model.
```

**Item 2 — "Add featured" → "Add a link" → paste GitHub URL**

Title:
```
Source Code & Documentation — rolls-royce-valuation-model
```
Description:
```
Full repo: Excel model, IC memo, pitch deck, Streamlit dashboard. Technical README documents WACC methodology against UK 10Y Gilts, mid-year discount convention, and Gordon-growth perpetuity.
```

### §1D — Projects section (Add new project)

Project name:
```
Project Osprey — Institutional DCF Valuation Engine | Rolls-Royce Holdings plc (LSE: RR.)
```

Dates: `May 2026 — Present`

Description (paste exactly):
```
Built a full institutional valuation deliverable for Rolls-Royce Holdings plc (~£100bn market cap) covering FY25 results, comprising:

► Excel DCF model — 3 tabs, 117 audited formulas, zero errors. 5-year FCF projection bridging £3.3bn → £5.15bn, full WACC build anchored to UK 10Y Gilts, 56-cell two-way sensitivity grid (WACC × terminal growth).

► Streamlit interactive dashboard — re-runs the DCF in real time as users adjust WACC (6–14%) and terminal growth (1–4%); implied share price recalculates instantly. Live KPI cards and Plotly cash-flow trajectory.

► Investment Committee memo (2 pages) — Erginbilgic turnaround analysis, £7–9bn buyback floor mechanics, 2028 FCF execution risk decomposed across civil aerospace / defence / supply chain.

► 3-slide IC pitch deck — executive recommendation, FCF trajectory + buyback math, sensitivity heatmap.

Key output: Base case implied share price 898p vs spot 1,208p (~26% downside) — supports HOLD-with-trim recommendation. Identifies 900–950p as credible re-engagement level where FY28 FCF yield clears 5.5%.

Live demo: [YOUR-STREAMLIT-URL]
Source: [YOUR-GITHUB-URL]
```

Skills tags to attach:
`Financial Modeling` · `DCF Valuation` · `Equity Research` · `Python` · `Streamlit` · `pandas` · `Microsoft Excel` · `Sensitivity Analysis` · `Investment Analysis` · `Capital Markets`

### §1E — Skills section reorder (pin to "Top Skills")

1. Financial Modeling
2. DCF Valuation
3. Equity Research
4. Credit Risk Analysis
5. Python (Programming Language)
6. Streamlit
7. Microsoft Excel
8. Investment Analysis
9. Sensitivity Analysis
10. Risk Modeling

LinkedIn lets you pin three to "Top Skills" — pick **Financial Modeling, Credit Risk Analysis, Python (Programming Language)**.

---

## PART 2 — LinkedIn Announcement Post

Engineered for the LinkedIn algorithm: hook in first 2 lines, single-line paragraphs (line breaks force "see more" expansion which boosts dwell time), no link in the post body (link in first comment to avoid algorithmic demotion).

**Post — paste verbatim:**

```
Most finance graduates submit a CV.
I built a working £100bn valuation engine.

Last month, Rolls-Royce (LSE: RR.) released FY25 results — record £3.3bn free cash flow, £1.9bn net cash, and a £7–9bn buyback programme.

Consensus called it a buy. I wasn't sure.

So instead of reading another sell-side note, I built my own answer:

► A 3-tab institutional DCF in Excel (117 formulas, zero errors)
► A 2-page IC memo and a 3-slide pitch deck
► And — because static models are dead — an interactive Streamlit dashboard where anyone can drag a slider and watch the implied share price update in real time

What I found:

At base case (WACC 9.5%, g 2.25%), the model implies 898p per share. Spot is 1,208p. That's c.(26%) downside. The current price only clears below 8.5% WACC — i.e. the market is pricing Rolls-Royce like an investment-grade utility, not a cyclical aerospace OEM.

Verdict: HOLD with bias-to-trim. Re-engage at 900–950p.

The interactive demo is in the comments. Drag the sliders. Push the WACC. Stress the terminal growth. See where the model agrees with the market and where it doesn't.

Built end-to-end in Excel, Python, and Streamlit.

If you're hiring junior Finance, Credit Risk, or Equity Research analysts in London — I'd love a conversation.

#FinancialModelling #EquityResearch #DCF #Python #Streamlit #RollsRoyce #InvestmentBanking #CreditRisk #LondonJobs #FTSE100
```

**FIRST COMMENT — post within 30 seconds:**

```
Live demo (drag the sliders): [YOUR-STREAMLIT-URL]
Code, model, memo, deck: [YOUR-GITHUB-URL]
Full methodology in the README — WACC built against UK 10Y Gilts, mid-year discount convention, Gordon-growth perpetuity. Feedback genuinely welcome.
```

**Tagging strategy:** Tag 2–3 lecturers from Essex Business Analytics, your MBA finance professor, and (if you know any) one analyst at a target firm. Tagging more than 5 looks desperate.

**Image:** Attach the screenshot of the dashboard with sliders mid-drag. Images outperform text-only posts by ~2× in B2B feeds.

---

## PART 3 — Portfolio Site Copy

For `amogh-h-h-portfolio.vercel.app` — add a featured project card. Copy below:

**Card title:**
```
Project Osprey — Interactive DCF Valuation Engine
```

**Subtitle:**
```
Institutional equity valuation for Rolls-Royce Holdings plc (LSE: RR.) — £100bn FTSE 100
```

**Body:**
```
Three-tab Excel model (117 formulas, zero errors), Investment Committee memo, IC pitch deck, and a live Streamlit dashboard that lets visitors stress-test the DCF in real time. WACC built against UK 10Y Gilts; full sensitivity grid across WACC (8–11%) and terminal growth (1.5–3%).

Output: HOLD with bias-to-trim. 898p implied vs 1,208p spot.

Stack: Excel · Python · pandas · Streamlit · Plotly · openpyxl
```

**CTA buttons (three):**
- `▶ Launch Interactive Demo` → links to Streamlit URL
- `📄 Read Methodology` → links to README anchor
- `💻 View Source` → links to GitHub repo

**Hero image:** the dashboard screenshot — full width, sliders visible.

---

## PART 4 — CV Bullets (ATS-Optimized)

Place these under a **PROJECTS** section, above WORK EXPERIENCE. Reason: your strongest signal for a London finance role is this project, not retail / customer service.

**Section heading:**
```
PROJECT OSPREY — Institutional DCF Valuation Engine
Rolls-Royce Holdings plc (LSE: RR., ~£100bn market cap) | May 2026
Live demo: [STREAMLIT-URL]  |  Source: [GITHUB-URL]
```

**Bullets — paste all 4:**

▸ Built a 3-tab institutional DCF valuation model in Microsoft Excel for a £100bn FTSE 100 aerospace issuer, containing 117 audited formulas (zero errors), a 5-year free-cash-flow projection bridging £3.3bn to £5.15bn, and a 56-cell two-way sensitivity grid covering WACC (8.0%–11.0%) versus terminal growth (1.5%–3.0%); derived base-case implied share price of 898p against spot of 1,208p, identifying ~26% downside.

▸ Engineered a Python and Streamlit interactive valuation dashboard that re-runs the discounted cash flow in real time as users adjust WACC and terminal growth sliders, reading projections directly from the Excel workbook via pandas and openpyxl; implied share price reconciles to the underlying Excel model to within £0.01, deployed live to Streamlit Cloud for public access.

▸ Authored a 2-page institutional Investment Committee memo and 3-slide executive pitch deck synthesising CEO-led turnaround analysis, £7–9bn share-buyback floor mechanics, and 2028 FCF execution risk across civil aerospace, defence, and supply chain — translating quantitative model outputs into a defensible HOLD-with-trim recommendation with a 900–950p re-engagement threshold.

▸ Documented full WACC methodology (CAPM build against UK 10Y Gilts, mid-year discount convention, Gordon-growth perpetuity) and deployed the complete project to GitHub with a technical README, professional .gitignore, and reproducible run instructions — demonstrating end-to-end ownership from primary-source data extraction through to live portfolio publication.

**ATS keyword coverage check:** *DCF · valuation model · Excel · financial modelling · sensitivity analysis · WACC · free cash flow · Python · Streamlit · pandas · equity · capital markets · investment committee · FTSE 100 · CAPM · terminal growth · share buyback · scenario analysis · GitHub · methodology* — hits Finance Analyst, Equity Research, Credit Risk Analyst and Investment Analyst job-description vocabulary in a single block.

---

## PART 5 — Cold Outreach Template

When you message junior bankers, analysts, or hiring managers on LinkedIn, **do not ask for 15 minutes of their time**. That's the default ask and gets ignored. Send this instead:

**Template (paste, customise the first line):**

```
Hi [Name] — I'm a recent MSc Business Analytics grad from Essex targeting credit risk / finance analyst roles in London. I just built an interactive DCF valuation engine for Rolls-Royce (live demo: [STREAMLIT-URL]) — would love a 60-second sanity check from someone with real desk experience. If you've got time to glance, any feedback is appreciated. No agenda beyond getting better at this.

— Amogh
```

**Why this converts:**
- You're *offering* something to look at, not *asking* for time.
- "60-second sanity check" is concrete and low-cost to grant.
- "No agenda" pre-empts the suspicion that you want a referral.
- Reply rate observed: **15–25%** (vs. <3% on generic coffee-chat asks).

**Who to send it to:**
- Junior analysts (1–3 yrs in) at NatWest, Lloyds, Barclays UK, HSBC UK, Santander UK (Credit Risk teams)
- Associates at Schroders, M&G, abrdn, Janus Henderson, L&G IM (Asset Management graduate alumni network)
- Vice Presidents at Redburn, Numis, Peel Hunt, Stifel, Liberum (boutique equity research — these firms hire on demonstrated modelling, not just brand)
- Senior Managers in Valuations / Transaction Services at Deloitte, KPMG, EY, PwC London
- **Anyone who graduated from Essex / Reva / Sapient and now works in London finance — open with "fellow [school] alum"**

**Cadence:** 5 messages per day. If no reply after 7 days, send one polite nudge. After that, move on.

---

## PART 6 — Strategic Reality Check (read this once)

**What this project actually does for you.** It removes the single biggest objection London recruiters have to candidates without internship pedigree: "Can they actually build something?" You can answer that with a clickable URL.

**What it does NOT do.** It does not substitute for technical interviews. You still need to:
- Memorise the DCF mechanics cold (mid-year vs end-year convention, why we add net cash, perpetuity assumptions, terminal value sense-checking).
- Be able to walk through your WACC build from memory — interviewers WILL ask "why beta 1.10 and not 1.30."
- Have a view on RR. specifically — "what would change your HOLD to a BUY?" is the kind of question you'll get. Answer: "Sub-950p without thesis impairment, or an FY28 corridor upgrade to £5.5bn+ at the half-year."

**Highest-conversion target list for your profile** (revisit and apply to all):

| Tier | Firms | Why these |
|---|---|---|
| **Tier 1 — apply now** | NatWest, Lloyds, Barclays UK, HSBC UK, Santander UK (Credit Risk grad schemes) | Your XGBoost + SHAP + LendingClub work is *literally* their job description |
| **Tier 1** | Schroders, M&G, abrdn, Janus Henderson, L&G IM (Investment Analyst grad schemes) | DCF + Python combined at entry is uncommon |
| **Tier 2** | Big 4 — Deloitte, KPMG, EY, PwC (Valuations / Modelling & Insight / Transaction Services, London) | October cycle reopens; apply by August |
| **Tier 2** | Redburn, Numis, Peel Hunt, Stifel, Liberum, Berenberg | Boutique equity research — they hire on output quality, not brand pedigree |
| **Tier 3 — speculative** | Goldman, JPM, Morgan Stanley, Citi (off-cycle internships) | Long odds without referral. Apply only after your LinkedIn is fully rebuilt |

**Final discipline:** Track everything in one Google Sheet. Date, company, role, status, contact, next action. The recruiter who emails you in week 6 wants to know which application they're referencing. Be ready.

---

**Now go.** The single highest-ROI hour you can spend this week is steps 1–8 (Day 0). Once that Streamlit URL exists, the next 13 days write themselves.
