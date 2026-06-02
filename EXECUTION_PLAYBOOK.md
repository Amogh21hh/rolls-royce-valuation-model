# Project Osprey — Granular Execution Playbook

> The step-by-step manual. Every click, every command, every URL.
> Read with `MARKETING_KIT.md` open alongside — text blocks live there.

**Time investment:** ~6 hours of focused work spread across Day 0 → Day 7. After that, ~3 hours/day of applications and outreach.

---

## TABLE OF CONTENTS

- [PHASE A — Day 0: Get the project LIVE (90 min)](#phase-a)
  - [A1. Move the folder to Desktop (2 min)](#a1)
  - [A2. Install prerequisites — Git, Python, GitHub CLI (15 min)](#a2)
  - [A3. Test the Streamlit dashboard locally (10 min)](#a3)
  - [A4. Take screenshots (5 min)](#a4)
  - [A5. Push to GitHub (15 min)](#a5)
  - [A6. Deploy live to Streamlit Cloud (15 min)](#a6)
  - [A7. Add live badge + pin repo (15 min)](#a7)
- [PHASE B — Day 1: LinkedIn rebuild (60 min)](#phase-b)
  - [B1. Update Headline (3 min)](#b1)
  - [B2. Rewrite About section (5 min)](#b2)
  - [B3. Add two Featured items (8 min)](#b3)
  - [B4. Add Project Osprey to Projects (8 min)](#b4)
  - [B5. Reorder Skills (5 min)](#b5)
  - [B6. Publish the announcement post (15 min)](#b6)
  - [B7. Post-publish engagement loop (15 min)](#b7)
- [PHASE C — Day 2–14: Applications (4 hrs/day)](#phase-c)
  - [C1. Build your tracker (15 min, one-off)](#c1)
  - [C2. Where to find roles — exact URLs and filters](#c2)
  - [C3. How to apply — workflow per application](#c3)
- [PHASE D — Day 2–14: Cold outreach (1 hr/day)](#phase-d)
  - [D1. Build your prospect list (Day 2, 45 min)](#d1)
  - [D2. The daily outreach routine](#d2)
  - [D3. Follow-up cadence](#d3)
- [PHASE E — Portfolio site update (Day 2, 30 min)](#phase-e)
- [PHASE F — Interview preparation (parallel from Day 3)](#phase-f)
- [PHASE G — Maintenance & amplification (Day 7+)](#phase-g)
- [APPENDIX 1 — Troubleshooting](#apx1)
- [APPENDIX 2 — Recruiter / hiring manager search strings](#apx2)
- [APPENDIX 3 — Daily / weekly checklist](#apx3)

---

<a id="phase-a"></a>
# PHASE A — DAY 0: GET THE PROJECT LIVE (90 minutes)

This is the single most important block in the playbook. Until the Streamlit URL exists, nothing else can fire. Do this in one sitting, no breaks.

<a id="a1"></a>
## A1. Move the folder to your Desktop (2 min)

**Why:** Git must run on a path you control. The Cowork session path is sandboxed and you can't push from there.

**Steps:**
1. Open **File Explorer** (Win+E).
2. In the address bar at the top, paste: `C:\Users\amogh\AppData\Roaming\Claude\local-agent-mode-sessions\93818b96-87c1-46f2-b57e-e7699b726ec2\7cd2824f-664b-40f9-941c-2389f884bb91\local_e2eb7371-3c99-49c7-9ff8-0ec07bca7906\outputs` and press Enter.
3. You'll see the folder `Project_Osprey_RR_Valuation`. Right-click → **Copy** (not Cut — leave the original as a backup).
4. In the address bar, paste: `C:\Users\amogh\Desktop` and press Enter.
5. Right-click in the empty space → **Paste**.
6. Confirm the folder now lives at `C:\Users\amogh\Desktop\Project_Osprey_RR_Valuation\`.

**Verify:** Open the folder. You should see `README.md`, `DEPLOY.md`, `MARKETING_KIT.md`, `.gitignore`, and 4 subfolders (`01_Source_Data`, `02_Financial_Models`, `03_IC_Deliverables`, `04_Interactive_Dashboard`).

<a id="a2"></a>
## A2. Install prerequisites — Git, Python, GitHub CLI (15 min)

You may already have some of these. Check first, then install only what's missing.

### A2a. Check what's already installed

1. Press **Win+R**, type `powershell`, press Enter. A blue terminal window opens.
2. Run these three commands, one at a time:
   ```powershell
   git --version
   python --version
   gh --version
   ```
3. For each command:
   - If you see a version number (e.g. `git version 2.45.0`), it's installed — skip the matching install step below.
   - If you see "not recognized as an internal or external command" or similar, install it.

### A2b. Install Git (if missing)

1. Open Chrome → go to <https://git-scm.com/download/win>.
2. The download starts automatically. When done, double-click the `.exe`.
3. Click **Next** through every screen — **accept all defaults**. Do NOT change settings on the "Adjusting your PATH environment" screen; the default "Git from the command line and also from 3rd-party software" is what you want.
4. Click **Install**. Wait ~2 minutes. Click **Finish**.
5. **Close PowerShell and reopen it** (this refreshes the PATH so `git` works).
6. Verify: `git --version` should now print a version number.

### A2c. Install Python (if missing or version <3.10)

1. Chrome → <https://www.python.org/downloads/windows/>.
2. Click the top yellow button — "Download Python 3.x.x".
3. Double-click the `.exe` to install.
4. **CRITICAL**: On the very first installer screen, tick the box **"Add python.exe to PATH"** at the bottom. If you skip this, nothing else works.
5. Click **Install Now**. Wait ~3 minutes.
6. Close PowerShell, reopen, verify: `python --version` → should print `Python 3.12.x` or similar.

### A2d. Install GitHub CLI (recommended — saves you ~10 minutes later)

1. Chrome → <https://cli.github.com/>.
2. Click the **Download for Windows** button.
3. Run the `.msi` installer → Next → Install → Finish.
4. Close PowerShell, reopen, verify: `gh --version` → version number.

### A2e. Create a GitHub account if you don't have one

1. Chrome → <https://github.com/signup>.
2. Email: `amoghmallikarjun0321@gmail.com`. Username: something professional like `amogh-hh` or `amoghmallikarjun` — this becomes part of your repo URL forever, so pick carefully.
3. Verify your email by clicking the link GitHub sends you.

<a id="a3"></a>
## A3. Test the Streamlit dashboard locally (10 min)

**Goal:** confirm `streamlit run app.py` opens a working dashboard in your browser before you push anything public.

1. In PowerShell, run:
   ```powershell
   cd "$env:USERPROFILE\Desktop\Project_Osprey_RR_Valuation\04_Interactive_Dashboard"
   ```
2. Install the Python dependencies (one-off):
   ```powershell
   pip install -r requirements.txt
   ```
   This downloads streamlit, pandas, openpyxl, plotly. Takes ~2 minutes. Ignore the "Scripts is installed in ... which is not on PATH" warning — it doesn't matter.
3. Launch the dashboard:
   ```powershell
   streamlit run app.py
   ```
4. Within 5 seconds, Chrome should auto-open `http://localhost:8501`. If it doesn't, copy the **Local URL** that PowerShell prints and paste it into Chrome manually.

**Verification checklist** — confirm all four:
- [ ] The navy header bar reads "PROJECT OSPREY" with "Rolls-Royce Holdings plc — DCF Sandbox" below it.
- [ ] The left sidebar has two sliders: "WACC / Cost of Equity (%)" and "Terminal Growth Rate (%)".
- [ ] The big KPI card in the centre shows **~898p** when sliders are at default (WACC 9.5%, g 2.25%).
- [ ] Dragging the WACC slider down to 8.0% causes the implied price to JUMP upward (toward £10+).

If all four pass: **stop the server** in PowerShell by pressing **Ctrl+C**, then **Y** if prompted.

If anything fails: see Appendix 1.

<a id="a4"></a>
## A4. Take screenshots (5 min)

You'll embed these on LinkedIn, your portfolio site, and the README.

**Restart the dashboard:** `streamlit run app.py` (from the dashboard folder).

**Three screenshots to capture** (use **Win+Shift+S** to launch Snipping Tool):

1. **Hero shot** — Default sliders, full dashboard visible. Make sure the KPI card "IMPLIED SHARE PRICE 898p" is in frame. Save as `screenshot-1-hero.png` on your Desktop.
2. **Bull case** — Drag WACC slider down to 8.0%, terminal growth up to 3.0%. The implied price should be ~£12.63 / 1,263p. Screenshot. Save as `screenshot-2-bull.png`.
3. **Bear case** — Drag WACC up to 11.0%, terminal growth down to 1.5%. Implied price ~£7.05 / 705p. Screenshot. Save as `screenshot-3-bear.png`.

Stop the server (Ctrl+C).

<a id="a5"></a>
## A5. Push to GitHub (15 min)

I strongly recommend the GitHub CLI path. It's one command versus six.

### A5a. One-time identity setup

In PowerShell:
```powershell
git config --global user.email "amoghmallikarjun0321@gmail.com"
git config --global user.name  "Amogh H. H."
git config --global init.defaultBranch main
```

### A5b. Authenticate the GitHub CLI

```powershell
gh auth login
```

Answer the prompts:
- "What account do you want to log into?" → **GitHub.com** (press Enter).
- "What is your preferred protocol for Git operations on this host?" → **HTTPS** (press Enter).
- "Authenticate Git with your GitHub credentials?" → **Y**.
- "How would you like to authenticate GitHub CLI?" → **Login with a web browser** (press Enter).
- It will print an 8-character code, e.g. `ABCD-1234`. **Copy it.** Press Enter — Chrome opens to <https://github.com/login/device>.
- Paste the code, click **Continue**, click **Authorize github**.
- Return to PowerShell — you should see "✓ Authentication complete".

### A5c. Initialise, commit, and push — one block

```powershell
cd "$env:USERPROFILE\Desktop\Project_Osprey_RR_Valuation"
git init
git add .
git commit -m "Feat: Initial institutional valuation model and documentation for Rolls-Royce Plc"
gh repo create rolls-royce-valuation-model --public --source=. --remote=origin --push
```

The final `gh repo create` line creates the public repo on GitHub AND pushes your code in one shot.

**Verify:** Chrome → `https://github.com/<your-username>/rolls-royce-valuation-model`. You should see all your files. **Copy this URL** — paste it in a sticky note. Call it `GITHUB_URL`.

<a id="a6"></a>
## A6. Deploy live to Streamlit Cloud (15 min)

**This is the highest-leverage step of the entire playbook.** A clickable live URL is what converts CV scrolling into recruiter interest.

1. Chrome → <https://share.streamlit.io>.
2. Click **Sign up** (or **Sign in** if you've used Streamlit before) → **Continue with GitHub**.
3. Click **Authorize streamlit** when GitHub asks.
4. You'll land on the Streamlit Cloud dashboard. Click the blue **"Create app"** button (top right).
5. Choose **"Deploy a public app from GitHub"**.
6. Fill in:
   - **Repository:** `<your-username>/rolls-royce-valuation-model` (autocomplete will find it)
   - **Branch:** `main`
   - **Main file path:** `04_Interactive_Dashboard/app.py`
   - **App URL (custom subdomain):** `amogh-rolls-royce` (or similar — this becomes part of the public URL, so make it clean)
7. Click **Deploy!**.
8. A black log panel appears. Wait **2–4 minutes** while Streamlit installs your dependencies and boots the app. You'll see:
   - "Installing dependencies..." → ~90 seconds
   - "Starting up..." → ~30 seconds
   - "Your app is in the oven 🍕" → final step
9. When done, the dashboard renders in the panel. Click the small "Open in new tab" icon (top-right of the panel).
10. **Copy the URL from the address bar.** It will look like `https://amogh-rolls-royce.streamlit.app`. **This is your money URL.** Save it in your sticky note as `STREAMLIT_URL`.

**Verify in incognito mode** (Ctrl+Shift+N in Chrome) — paste the URL. If it loads and the sliders work, you're golden.

<a id="a7"></a>
## A7. Add live badge to README and pin the repo (15 min)

### A7a. Edit README to show the Live Demo badge at the top

1. Open `C:\Users\amogh\Desktop\Project_Osprey_RR_Valuation\README.md` in **Notepad** (right-click → Open with → Notepad).
2. Find the line near the top that starts with `[![Made with Python]...`.
3. Add this line ABOVE it (so it's the first badge users see):
   ```markdown
   [![Live Demo](https://img.shields.io/badge/▶_Live_Demo-Streamlit-FF4B4B?logo=streamlit&logoColor=white)](YOUR-STREAMLIT-URL)
   ```
4. Replace `YOUR-STREAMLIT-URL` with the actual URL from your sticky note (e.g. `https://amogh-rolls-royce.streamlit.app`).
5. Save (Ctrl+S). Close Notepad.

### A7b. Commit and push the update

In PowerShell:
```powershell
cd "$env:USERPROFILE\Desktop\Project_Osprey_RR_Valuation"
git add README.md
git commit -m "Docs: add live Streamlit demo badge to README"
git push
```

### A7c. Pin the repo on your GitHub profile

1. Chrome → `https://github.com/<your-username>` (your profile page).
2. Below your avatar, click **"Customize your pins"**.
3. In the popup, **tick the box next to `rolls-royce-valuation-model`**. If you have ≤6 repos this is the only one available.
4. Click **Save pins**.

### A7d. Final verification

Hard-refresh (Ctrl+F5) the GitHub repo page:
- [ ] "Live Demo" badge appears at the top of the README.
- [ ] Clicking the badge opens the Streamlit dashboard.
- [ ] All folders and files are visible: `01_Source_Data/`, `02_Financial_Models/`, `03_IC_Deliverables/`, `04_Interactive_Dashboard/`, `README.md`, `.gitignore`, `DEPLOY.md`, `MARKETING_KIT.md`, `EXECUTION_PLAYBOOK.md`.
- [ ] The repo is pinned on your profile page.

**🛑 STOP HERE FOR DAY 0.** Take a screenshot of the live dashboard. Sleep on it. Tomorrow you launch on LinkedIn.

---

<a id="phase-b"></a>
# PHASE B — DAY 1: LINKEDIN REBUILD (60 min)

Open `MARKETING_KIT.md` to a second window — you'll be copy-pasting from it.

**Best time to do this:** Monday evening, so you're ready to publish your announcement post Tuesday 7:30 AM.

<a id="b1"></a>
## B1. Update Headline (3 min)

1. Chrome → <https://www.linkedin.com>. Sign in.
2. Click your **profile picture** (top right of the nav bar) → click **View Profile**.
3. Below your name and current headline, hover over the **pencil icon** at the top-right of the intro card → click it. A pop-up appears titled "Edit intro".
4. Find the **Headline** field. Select all existing text, delete it.
5. Paste the headline from `MARKETING_KIT.md` §1A:
   ```
   Finance & Credit Risk Analyst | DCF Modelling • Python • Credit Risk ML | MSc Business Analytics @ Essex | Built an interactive valuation engine for Rolls-Royce (£100bn co.) — link below
   ```
6. Click **Save** (blue button, bottom right of the pop-up).

**Verify:** Your headline on the profile page now reads exactly that.

<a id="b2"></a>
## B2. Rewrite About section (5 min)

1. On your profile page, scroll down to the **About** section.
2. Click the **pencil icon** in the top right of the About card.
3. **Select all (Ctrl+A) and delete** your current About text.
4. Copy the entire About block from `MARKETING_KIT.md` §1B and paste.
5. **Critical edit:** replace `[YOUR-STREAMLIT-URL]` and `[YOUR-GITHUB-URL]` with your real URLs from your sticky note.
6. Click **Save**.

<a id="b3"></a>
## B3. Add two Featured items (8 min)

The Featured section sits between your intro card and your About section. If you don't see it, you need to enable it first.

### B3a. Enable Featured section (if not visible)

1. On your profile, click **"Add profile section"** (button near the top, below intro card).
2. Expand **"Recommended"**.
3. Click **"Add featured"**.

### B3b. Add the Streamlit URL as Featured Item #1

1. In the Featured section, click the **+** (plus) icon → **"Add a link"**.
2. **Link:** paste your `STREAMLIT_URL`.
3. Click **"Add link"**. LinkedIn fetches a preview.
4. Replace the auto-generated **Title** with:
   ```
   Project Osprey — Live DCF Valuation Engine (Rolls-Royce, LSE: RR.)
   ```
5. Replace the **Description** with the §1C Item 1 text from the kit.
6. **Custom thumbnail (recommended):** click the small image icon and upload `screenshot-1-hero.png` from your Desktop. A custom image massively outperforms LinkedIn's default page-preview.
7. Click **Save**.

### B3c. Add the GitHub URL as Featured Item #2

1. Click the **+** icon in Featured again → **"Add a link"**.
2. Paste `GITHUB_URL`.
3. Title:
   ```
   Source Code & Documentation — rolls-royce-valuation-model
   ```
4. Description: from kit §1C Item 2.
5. Upload `screenshot-2-bull.png` as thumbnail.
6. Save.

**Verify:** Both items appear side by side in your Featured section. Click each — the live URLs open correctly.

<a id="b4"></a>
## B4. Add Project Osprey to the Projects section (8 min)

### B4a. Enable Projects section if missing

1. Click **"Add profile section"** → **"Additional"** → **"Add projects"**.

### B4b. Add the project

1. In the Projects card, click the **+** (or **"Add project"**).
2. **Project name:**
   ```
   Project Osprey — Institutional DCF Valuation Engine | Rolls-Royce Holdings plc (LSE: RR.)
   ```
3. **From:** `May 2026`. Tick **"I am currently working on this project"**.
4. **Associated with:** select your most recent education entry (University of Essex MSc Business Analytics) so it pins to that experience.
5. **Description:** paste the entire §1D block from the kit. Replace `[YOUR-STREAMLIT-URL]` and `[YOUR-GITHUB-URL]` with real URLs.
6. **Add media:** click "Add media" → upload `screenshot-1-hero.png` and `screenshot-3-bear.png`.
7. **Contributors:** leave blank (solo project).
8. **Skills:** click "Add skills" and add these 10 (the kit lists them in §1D):
   - Financial Modeling
   - DCF Valuation
   - Equity Research
   - Python (Programming Language)
   - Streamlit
   - pandas
   - Microsoft Excel
   - Sensitivity Analysis
   - Investment Analysis
   - Capital Markets
9. Click **Save**.

<a id="b5"></a>
## B5. Reorder Skills (5 min)

1. Scroll to the **Skills** section of your profile.
2. Click **"Show all"** to expand.
3. Click the **pencil icon** (edit) in the top right of the Skills section.
4. **Pin top 3:** find each of these in your list and click the small **pin icon** next to it:
   - Financial Modeling
   - Credit Risk Analysis
   - Python (Programming Language)
5. **Add if missing** (click "Add new skill" at the top):
   - DCF Valuation
   - Equity Research
   - Streamlit
   - Sensitivity Analysis
   - Investment Analysis
   - Risk Modeling
6. Click **Save**.

<a id="b6"></a>
## B6. Publish the announcement post (15 min)

**Critical timing:** Post **Tuesday or Wednesday between 7:30 AM and 8:30 AM UK time**. LinkedIn's algorithm rewards posts published when professionals start their workday. Never Friday — engagement drops by ~40%.

### B6a. Compose the post

1. From your LinkedIn home feed, click **"Start a post"** (top centre).
2. A composer pops up. **Do not click any of the "Photo / Video / Document" buttons yet** — paste text first.
3. Open `MARKETING_KIT.md` §2 in another tab. **Copy the entire post body** (starts with "Most finance graduates submit a CV." ends with the hashtag line).
4. Paste into the composer.
5. **Critical:** LinkedIn collapses line breaks. After pasting, scroll through and verify each line break is preserved. If they merge, manually re-insert by pressing **Shift+Enter** at the end of each line (Shift+Enter = soft line break; Enter alone = new paragraph). Both work, but check the preview.

### B6b. Attach an image

1. In the composer toolbar (bottom of the pop-up), click the **photo icon** (small camera).
2. Upload `screenshot-1-hero.png` from your Desktop.
3. Click **Done**.

### B6c. Tag people (optional but high-impact)

1. In the composer body, type `@` and then start typing the name of:
   - One Essex MSc Business Analytics lecturer (e.g., your dissertation supervisor)
   - One MBA Finance professor from Reva
   - Optionally, one analyst you know at a London bank
2. Click their name from the dropdown to tag.
3. **Do not tag more than 3 people.** More than that looks spammy and triggers algorithmic suppression.

### B6d. Publish

1. Click the blue **"Post"** button at the bottom right.
2. The post appears in your feed within 5 seconds.

### B6e. Drop the live URL in the FIRST COMMENT — within 30 seconds

This is critical. LinkedIn's algorithm suppresses posts with external URLs in the body but doesn't punish URLs in comments.

1. Find your post in the feed (refresh if needed). Click into it.
2. In the comment box at the bottom, paste the §2 "First Comment" text from the kit:
   ```
   Live demo (drag the sliders): YOUR-STREAMLIT-URL
   Code, model, memo, deck: YOUR-GITHUB-URL
   Full methodology in the README — WACC built against UK 10Y Gilts, mid-year discount convention, Gordon-growth perpetuity. Feedback genuinely welcome.
   ```
3. Replace the placeholder URLs with real ones.
4. Click **Post**.

<a id="b7"></a>
## B7. Post-publish engagement loop (15 min)

For the next 90 minutes after publishing, the LinkedIn algorithm is sampling whether your post deserves wider reach. Your engagement during this window literally determines distribution.

### B7a. Reply to your own comment (immediately)

Reply to your first-comment with one more comment 2–3 minutes after the original:
```
For anyone interested in the sensitivity grid specifically — current spot price (1,208p) is only justified at WACC below 8.5%. The market is pricing this like an investment-grade utility, not a cyclical OEM. Open to push-back.
```

This bumps comment count and adds substance.

### B7b. Engage with 10 other posts (this is the real lift)

Within 2 hours of publishing, leave **thoughtful comments** on 10 other posts in your feed. Quality > quantity. NOT "Great post!" — actual sentences.

**Where to find good targets:**
1. Search bar at the top of LinkedIn → search for any of these, then click **Posts** filter:
   - `equity research London`
   - `credit risk analyst graduate`
   - `Rolls-Royce earnings`
   - `FTSE 100 valuation`
   - `Streamlit finance`
2. Scroll the **#FinancialModelling** hashtag feed: `https://www.linkedin.com/feed/hashtag/financialmodelling/`.
3. Look for posts from London finance recruiters, VPs at banks, professors of finance. Their commenters often include hiring managers who will then see your name.

### B7c. Reply to every single comment on your own post

If anyone comments on your announcement, reply within 1 hour. Every reply triggers a re-surfacing in their network's feed.

---

<a id="phase-c"></a>
# PHASE C — DAY 2–14: APPLICATIONS (4 hrs/day)

**Daily target: 5 applications.** Quality over quantity — these are tailored, not spray-and-pray.

<a id="c1"></a>
## C1. Build your tracker (15 min, one-off)

1. Chrome → <https://sheets.google.com> → blank sheet.
2. Name it `Applications_Tracker_2026`.
3. In row 1, paste these column headers (across columns A–L):

| A | B | C | D | E | F | G | H | I | J | K | L |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Date Applied | Company | Role Title | Source | Job URL | Application Method | CV Version | Cover Letter? | Contact Name | Contact LinkedIn | Status | Next Action |

4. Status column dropdown values (use Data → Data validation):
   - Applied
   - Acknowledged
   - Phone screen
   - First interview
   - Technical interview
   - Final round
   - Offer
   - Rejected
   - Withdrawn
5. Bookmark this sheet — you'll open it every time you apply.

<a id="c2"></a>
## C2. Where to find roles — exact URLs and filters

### C2a. LinkedIn (highest volume, lowest signal — apply with referrals when possible)

URL: <https://www.linkedin.com/jobs/search/>

**Filters to set:**
- Keywords: rotate daily through `Finance Analyst`, `Credit Risk Analyst`, `Investment Analyst`, `Equity Research Analyst`, `Graduate Finance`, `Accounting Analyst`, `Junior Analyst`
- Location: `London, England, United Kingdom`
- Date posted: **Past 24 hours** (do this fresh each day — older postings are >80% already filled)
- Experience level: `Entry level` and `Internship`
- Job type: `Full-time` and `Internship`

Sort by **Most recent**. Apply to anything where:
- The job description doesn't require ≥2 years experience
- You're not blocked by visa requirements (you have full RTW — most won't be)
- The company is on your Tier 1 or Tier 2 list (see MARKETING_KIT.md Part 6)

### C2b. eFinancialCareers (London finance-specific — high signal)

URL: <https://www.efinancialcareers.co.uk/jobs/london>

**Filters:**
- Job function: `Credit Risk`, `Equity Research`, `Investment Banking`, `Asset Management`, `Finance/Accounting`
- Experience: `Entry-Level`, `0-2 Years`
- Sort: Most recent

**This is the highest-signal job board for London finance.** Recruiters often message proactively if your profile is set up.

### C2c. Bright Network (UK graduate-focused)

URL: <https://www.brightnetwork.co.uk/graduate-jobs/finance-banking/>

Free to sign up. Many UK retail bank grad schemes (Lloyds, NatWest, Santander, HSBC UK) post here.

### C2d. Specific firm career pages — bookmark these

Tier 1 — apply directly on these every week, even if no current vacancy (some have rolling intake):

| Firm | URL |
|---|---|
| NatWest careers | <https://jobs.natwestgroup.com/> |
| Lloyds Banking Group | <https://www.lloydsbankinggroup.com/careers.html> |
| HSBC UK careers | <https://www.hsbc.com/careers> |
| Barclays UK | <https://home.barclays/careers/> |
| Santander UK | <https://www.santanderukgraduates.com/> |
| Schroders | <https://www.schroders.com/en-gb/uk/people/careers/> |
| M&G | <https://www.mandgplc.com/careers/working-with-us> |
| abrdn | <https://www.abrdn.com/en-gb/corporate/careers> |
| Janus Henderson | <https://www.janushenderson.com/en-gb/investor/career/> |
| L&G Investment Management | <https://group.legalandgeneral.com/en/careers/> |
| Deloitte UK | <https://www2.deloitte.com/uk/en/pages/careers/articles/early-careers.html> |
| KPMG UK | <https://www.kpmgcareers.co.uk/> |
| EY UK | <https://www.ey.com/en_uk/careers> |
| PwC UK | <https://www.pwc.co.uk/careers.html> |
| Redburn Atlantic | <https://www.redburnatlantic.com/careers> |
| Numis (Deutsche Numis) | <https://www.dbnumis.com/careers> |
| Peel Hunt | <https://www.peelhunt.com/careers/> |
| Stifel | <https://www.stifel.com/careers> |
| Liberum | <https://www.liberum.com/careers/> |
| Berenberg | <https://www.berenberg.com/en-uk/career> |

### C2e. Indeed UK (low signal but high volume — apply only to bookmarked target firms)

URL: <https://uk.indeed.com>. Set up email alerts for each Tier 1 firm.

<a id="c3"></a>
## C3. How to apply — workflow per application (15-20 min each)

1. Find a role you'll apply to. Click into the job description.
2. **Read the full description.** Highlight any company-specific keywords (e.g. "stress testing", "IFRS 9", "LGD modelling").
3. **Tailor your CV** — open your master CV file, save a copy as `CV_<CompanyName>_<RoleTitle>.docx`. Edit:
   - Top "Projects" section: leave the Project Osprey bullets unchanged.
   - Skills section: bring 2–3 of the role's specific keywords to the top of your skills list if you have them.
4. **Write a 4-paragraph cover letter** in a separate file:
   - Para 1 (hook): "I'm a recent MSc Business Analytics graduate from the University of Essex applying for [role]. I'm writing because of [one specific thing about the firm — recent news, a deal, a team focus]."
   - Para 2 (proof of skill): "I've built end-to-end financial models, most recently Project Osprey — an institutional DCF valuation of Rolls-Royce Holdings plc with an interactive Python/Streamlit dashboard. Live demo at [STREAMLIT_URL]."
   - Para 3 (match to role): "Three reasons I'd add value to your team..." — list 3 specific things from the JD.
   - Para 4 (close): "Available immediately, full UK right to work. Happy to share the source code or walk through the methodology."
5. **Find the hiring manager / team lead on LinkedIn.** Search the firm + role keyword (e.g. "Credit Risk Manager NatWest"). Note their name in your tracker.
6. **Apply** through the firm's portal or LinkedIn Easy Apply.
7. **Within 2 hours of applying**, send the hiring manager a LinkedIn connection request with this note (max 200 chars):
   ```
   Hi [Name] — just applied to the [Role] role on your team. I lead with a live DCF project on Rolls-Royce (link in my profile). Would value the chance to learn more about the team. — Amogh
   ```
8. **Log everything in the tracker.** Row for every application.

---

<a id="phase-d"></a>
# PHASE D — DAY 2–14: COLD OUTREACH (1 hr/day)

Parallel to applications. The goal is to convert cold connections into referrals or insider intelligence.

<a id="d1"></a>
## D1. Build your prospect list (Day 2, 45 min one-off)

You're going to build a list of **100 target people** to message over the next 4 weeks (5/day × 5 days/week × 4 weeks).

1. Open a new tab of your tracker → second sheet, name it `Outreach`.
2. Columns: `Date Sent`, `Name`, `Company`, `Role`, `LinkedIn URL`, `Message Sent?`, `Replied?`, `Follow-up Sent?`, `Notes`.
3. Use LinkedIn Sales Navigator if you have a free trial; otherwise standard search works. **LinkedIn search bar → People filter** → use these searches:

**Search 1 — Junior analysts at target banks (50 prospects):**
- Search: `Credit Risk Analyst NatWest` → People filter → London → Save 5 names
- Repeat for: `Credit Risk Analyst Lloyds`, `Credit Risk Analyst Barclays`, `Credit Risk Analyst HSBC`, `Credit Risk Analyst Santander UK`
- Then: `Investment Analyst Schroders`, `Investment Analyst M&G`, `Investment Analyst abrdn`, `Investment Analyst Janus Henderson`, `Investment Analyst Legal & General`

**Search 2 — Boutique equity research analysts (20 prospects):**
- Search: `Equity Research Analyst Redburn`, `Equity Research Analyst Numis`, `Equity Research Analyst Peel Hunt`, `Equity Research Analyst Stifel`, `Equity Research Analyst Liberum`

**Search 3 — Big 4 valuations (15 prospects):**
- Search: `Valuations Analyst Deloitte London`, `Valuations Senior Associate KPMG London`, `Transaction Services Associate EY London`, `Deals Analyst PwC London`

**Search 4 — Essex alumni in London finance (15 prospects):**
- LinkedIn search bar → search `University of Essex` → click the school → click **Alumni** tab → filter by **Where they live: London** and **What they do: Finance**. Save 15 names.

For each name: right-click → **Open in new tab** → copy their profile URL → paste into your `Outreach` sheet.

<a id="d2"></a>
## D2. The daily outreach routine (1 hr/day)

**Time:** anytime between 8 AM and 11 AM UK on weekdays.

1. Open your `Outreach` sheet. Find the next 5 unsent rows.
2. For each:
   - Click their LinkedIn URL → click **Connect** (top of their profile, sometimes hidden under "More").
   - Click **"Add a note"**.
   - Paste this (200 char limit, this is exactly 198):
     ```
     Hi [FirstName] — recent Essex MSc Business Analytics grad targeting credit risk/finance analyst roles. Built a live DCF engine on Rolls-Royce (link in my profile). 60-sec sanity check from you would mean a lot.
     ```
   - Customise `[FirstName]` only. Don't get cute.
   - For Essex alumni: change first 6 words to: `Hi [FirstName] — fellow Essex alum, just finished MSc Business Analytics...`
   - Click **Send**.
3. Mark "Message Sent?" = Yes in your sheet.
4. Move on. **Total time per message: ~90 seconds.** Five takes ~8 minutes plus prospecting fills the hour.

<a id="d3"></a>
## D3. Follow-up cadence

When someone accepts your connection but doesn't reply:

**Day 0 (acceptance):** within 1 hour, send a message:
```
Thanks for connecting, [Name]. If you've 60 seconds, the live DCF demo is at [STREAMLIT_URL] — happy to receive any reaction, good or bad. No agenda.
```

**Day 7 (no reply yet):** one polite nudge:
```
[Name] — circling back briefly. If now's not a good time, totally understood. Quick question if you ever have a moment: what's the one skill you wish you'd built BEFORE joining [firm]? Would help me prioritise. — Amogh
```

**Day 14 (still no reply):** move on. Do not message again.

---

<a id="phase-e"></a>
# PHASE E — PORTFOLIO SITE UPDATE (Day 2, 30 min)

You already have `amogh-h-h-portfolio.vercel.app`. Add Project Osprey as the hero / featured project.

**How depends on what tech your portfolio uses.** If it's a React/Next.js site deployed via Vercel:

1. Open your portfolio repo locally.
2. Add a new project component or extend your existing projects array with:
   - Title: `Project Osprey — Interactive DCF Valuation Engine`
   - Subtitle: `Institutional equity valuation for Rolls-Royce Holdings plc (LSE: RR.)`
   - Body: paste §3 portfolio copy from `MARKETING_KIT.md`
   - Hero image: use `screenshot-1-hero.png`
   - CTA buttons:
     - `▶ Launch Demo` → `STREAMLIT_URL`
     - `💻 View Code` → `GITHUB_URL`
     - `📄 Read Methodology` → `GITHUB_URL#methodology` (anchor link in README)
3. Push the change. Vercel auto-deploys.

If it's a Notion / Webflow / static portfolio: replicate the same content structure in whatever editor you use. **The project should be the FIRST item visitors see** — move it above your prior credit risk work.

---

<a id="phase-f"></a>
# PHASE F — INTERVIEW PREPARATION (parallel from Day 3)

You WILL get interviews. Be ready.

## F1. Memorise these — they will come up

**DCF mechanics:**
- Mid-year vs end-year discount convention — why does mid-year typically give a higher value? (Because cash flows are received throughout the year, not at the end.)
- Why do you add net cash, not subtract net debt? (Because RR has net cash. If a company had net debt, you'd subtract.)
- Gordon growth perpetuity formula and when it breaks (when WACC ≈ g, or when g > long-run nominal GDP).
- Sense-check: what % of your DCF value comes from the terminal? (For RR Osprey: ~74%. Most analysts get nervous above 70%, very nervous above 80%.)

**Your specific WACC build — be able to defend every input:**
- Rf 4.5% — UK 10Y Gilt yield, why use the long bond? (Match the perpetual horizon of the DCF.)
- ERP 5.0% — Damodaran's mature equity risk premium for the UK. Be ready to say "I could see arguments for 5.5%".
- Beta 1.10 — 5Y weekly against FTSE 100. Why 1.10 and not 1.30? "Post-rerating, RR has stabilised — its volatility profile is closer to large-cap industrials than to pre-2023 distressed RR. Sensitivity-tested at 1.30 in the model."
- Equity weight 92% — driven by net cash + IG credit profile. RR is barely a leveraged co. today.

**Your view on RR:**
- Bull case: 2028 corridor upgraded at H1, multiple holds → £14+.
- Bear case: civil aerospace demand softens, supply chain bottleneck on castings, missed 2028 corridor → £7.
- Probability-weighted FY28 FCF: £4.85bn (vs management £5.0-5.3bn corridor).
- What would change you to BUY? Sub-950p without thesis impairment, or FY28 corridor upgrade to £5.5bn+ at the interim.

## F2. Behavioural questions — prepare 5 stories using STAR

Pick 5 specific stories from your background. For each:
- **S**ituation: what was the context?
- **T**ask: what were you responsible for?
- **A**ction: what did YOU specifically do?
- **R**esult: what was the outcome, quantified?

**Mandatory stories to prepare:**
1. "Tell me about a time you spotted a data quality issue" (use your credit risk modelling project)
2. "Describe a project where you had to learn something quickly" (Streamlit dashboard — went from zero to deployment)
3. "Tell me about working under deadline pressure" (MSc dissertation)
4. "When have you had to explain something technical to a non-technical audience" (any teaching / Carelon)
5. "Describe a time you made a mistake and what you learned"

## F3. Numerical reasoning practice

Many UK grad schemes use **SHL/Cognify/Aon Cut-e tests**. Practise free at:
- <https://www.shldirect.com/en/practice-tests>
- <https://www.assessmentday.co.uk/free-aptitude-tests/>

Spend 30 min/day for 5 days. Numerical reasoning is the most common screen-out filter for UK retail bank grad schemes.

---

<a id="phase-g"></a>
# PHASE G — MAINTENANCE & AMPLIFICATION (Day 7+)

## G1. Cross-post the announcement

Use the LinkedIn post body, lightly adapted, on:

- **Reddit r/FinancialCareers** (<https://reddit.com/r/financialcareers>) — title: "I'm a recent grad — built a live interactive DCF on Rolls-Royce. Roast it." Tone down the recruiter-pitch language; up the "feedback wanted" framing.
- **Wall Street Oasis "Off Topic" forum** (<https://www.wallstreetoasis.com/forum/off-topic>) — similar tone. WSO has thousands of London IB analysts who lurk.
- **Hacker News** (<https://news.ycombinator.com/submit>) — submit your Streamlit URL as a Show HN: "Interactive DCF valuation engine for Rolls-Royce (Streamlit + Python)". Title format: `Show HN: Interactive DCF on Rolls-Royce — drag sliders, see implied price`. Lower hit rate but if it hits, you get 5,000+ visitors.

## G2. Reach out to your university careers office

Email template to <careers@essex.ac.uk> (and your MSc cohort lead):
```
Subject: Project worth sharing with the MSc Business Analytics cohort

Hi [Careers Officer / Cohort Lead],

I recently completed Project Osprey — an interactive DCF valuation engine for Rolls-Royce Holdings plc, built in Excel, Python, and Streamlit. Live demo: [STREAMLIT_URL].

I think this could be useful for current and incoming MSc Business Analytics students as an example of how to bridge analytics into finance careers. If there's an Essex Careers newsletter, alumni feature, or LinkedIn page where this could be shared, I'd be grateful for the visibility.

Happy to write a short student-perspective blog post if helpful.

Best,
Amogh H. H.
MSc Business Analytics, Class of 2026
LinkedIn: linkedin.com/in/amogh-hh-34129a1b9
```

## G3. Update your post once if engagement is strong

If your original announcement post gets >50 reactions or >10 comments, post a follow-up 7–14 days later:
```
Update on the Rolls-Royce DCF project.

The live demo has now had [X] plays. A few things I learned from your feedback:

1. Several people pushed back on my 1.10 beta. Fair point — I've added a beta-sensitivity to the next iteration.
2. Two senior analysts flagged the terminal value contribution (~74% of value) as too high. Working on a 10-year explicit forecast.
3. Three people asked about extending the framework to Babcock and BAE Systems. Coming soon.

Link to demo: [STREAMLIT_URL]. New post when v2 ships.

Thanks for engaging. This is why publishing your work matters more than perfecting it.
```

This re-surfaces you in feeds and demonstrates iteration, which is what hiring managers actually look for.

---

<a id="apx1"></a>
# APPENDIX 1 — TROUBLESHOOTING

| Problem | Cause | Fix |
|---|---|---|
| `git: command not found` | Git not installed or PATH not refreshed | Close PowerShell, reopen. If still fails, reinstall Git, ensure "from command line" option ticked. |
| `python: command not found` | Python installer didn't add to PATH | Reinstall Python, TICK "Add python.exe to PATH" on first screen. |
| `pip install` returns SSL errors | Corporate network or VPN blocking PyPI | Add `--trusted-host pypi.org --trusted-host files.pythonhosted.org` to the command. Or switch off VPN. |
| Streamlit dashboard opens but shows "ModuleNotFoundError: openpyxl" | Dependencies not installed | Run `pip install -r requirements.txt` from the dashboard folder. |
| Streamlit dashboard shows "FileNotFoundError: RR_LBO_DCF_Model.xlsx" | You ran `streamlit run app.py` from the wrong folder | `cd` into `04_Interactive_Dashboard` BEFORE running. The script looks for the xlsx one folder up. |
| `gh auth login` won't open the browser | Default browser not set or firewall blocking | Manually go to <https://github.com/login/device> and paste the code. |
| `Updates were rejected` when running `git push` | Remote already has commits (e.g. you created a README on GitHub.com first) | Run `git pull origin main --rebase` then `git push`. |
| Streamlit Cloud "Error installing requirements" | Python version mismatch | In Streamlit Cloud → app settings → Python version → set to `3.10`. |
| Streamlit Cloud "App in the oven" forever (>10 min) | Almost always means a dependency conflict | Click "Manage app" → check the logs. Usually requires editing `requirements.txt` to pin a specific version. |
| LinkedIn post hidden after publishing | You included a link in the body | Delete the post. Repost without the link. Put link in first comment within 30 seconds. |
| LinkedIn "Add a link" doesn't fetch the Streamlit preview | Streamlit Cloud has a slow first-load that LinkedIn's crawler times out | Wait 5 minutes after your first Streamlit load, then try again. Or upload custom thumbnail instead. |

---

<a id="apx2"></a>
# APPENDIX 2 — RECRUITER / HIRING MANAGER SEARCH STRINGS

Use these in LinkedIn's search bar (top of the page). Filter results by **People** then **London**.

**For Credit Risk:**
- `"Credit Risk" graduate hiring NatWest`
- `"Credit Risk Manager" Lloyds London`
- `"Risk Analyst" "hiring" Barclays UK`
- `"Credit Risk Analyst" early careers HSBC`

**For Asset Management:**
- `"Investment Analyst" graduate Schroders`
- `"Junior Analyst" M&G`
- `"Graduate" "Investment" abrdn`
- `"Associate" Janus Henderson London`

**For Equity Research:**
- `"Equity Research" graduate Redburn`
- `"Research Associate" Numis`
- `"Research Analyst" Peel Hunt`

**For Big 4 Valuations:**
- `"Valuations" "Senior Manager" Deloitte London`
- `"Transaction Services" KPMG London`
- `"Deals" Associate EY London`

**For generalist:**
- `"University of Essex" finance London`
- `MSc "Business Analytics" hiring`
- `"graduate scheme" finance London 2026`

When you find someone with "hiring" or "recruiting" in their headline or bio: send a connection request with the cold message template.

---

<a id="apx3"></a>
# APPENDIX 3 — DAILY / WEEKLY CHECKLIST (PRINT THIS)

## Daily (Monday–Friday)

```
[ ] 08:00 — Open Applications_Tracker and Outreach sheets
[ ] 08:30 — Apply to 5 roles (tailored CV + cover letter per role)
[ ] 10:30 — Send 5 LinkedIn cold messages
[ ] 11:00 — Reply to any LinkedIn DMs / comments
[ ] 12:00 — Lunch (break)
[ ] 13:00 — 30 min numerical reasoning practice
[ ] 13:30 — 1 hour technical study: DCF mechanics, WACC, RR financials
[ ] 14:30 — Read 1 FT / Bloomberg article relevant to your target sectors
[ ] 15:00 — Update Project Osprey: 1 small commit (v2 features, bug fix, sensitivity addition)
[ ] 16:00 — Comment thoughtfully on 5 LinkedIn posts in finance feed
[ ] 17:00 — Day end: review tracker, plan tomorrow's 5 roles
```

## Weekly (Sunday review, 30 min)

```
[ ] Count applications sent this week (target: 25)
[ ] Count cold messages sent (target: 25)
[ ] Count replies received (track conversion rate)
[ ] Count interviews booked
[ ] Re-engage any "stale" applications (no acknowledgement after 7 days): send follow-up email to hiring manager
[ ] Update LinkedIn — small addition each week (skill endorsement, new contact, recommendation request)
[ ] Plan one technical "v2" feature to ship to Project Osprey
[ ] Cross-post to one new platform (Reddit, WSO, Hacker News, etc.)
```

## Monthly (1st of each month)

```
[ ] Audit Applications_Tracker — calculate response rate. If <5%, the CV bullets need a rewrite.
[ ] Audit Outreach — calculate connection acceptance rate. If <20%, the message template needs softening.
[ ] Refresh LinkedIn headline with one new keyword
[ ] Ship one major Project Osprey upgrade (extend to BAE / Babcock, add Monte Carlo, add scenario presets)
[ ] Republish announcement post with v2 update
```

---

# CLOSING DISCIPLINE

You will get rejected. Bank graduate schemes have <2% acceptance rates. Boutique research desks hire 2–4 people a year. This is normal. The candidates who win are the ones who keep shipping work, keep messaging people, and keep showing up — not the ones with the most polished cover letters.

**Three weeks from now**, you should have:
- 60+ applications submitted
- 60+ cold messages sent
- 5+ recruiter conversations booked
- A v2 of Project Osprey shipped (maybe extending to BAE Systems for a head-to-head DCF)
- A second LinkedIn post out

If you hit those numbers, interviews will follow. The job won't.

**Execute, don't optimise.**

— Plan ends.
