# GitHub Deployment — Step-by-Step

This file walks you through publishing `Project_Osprey_RR_Valuation` to your public GitHub.
Total time: **~3 minutes**. No surprises.

---

## Step 0 — Prerequisites (one-time)

You need:
- Git installed (check with `git --version`). If missing, install from <https://git-scm.com/download/win>.
- A GitHub account signed in to <https://github.com> in Chrome.
- (Optional but recommended) GitHub CLI: <https://cli.github.com/> — removes one manual step.

---

## Step 1 — Move the project folder to your Desktop

Open File Explorer, drag the entire `Project_Osprey_RR_Valuation` folder from your downloads
location onto your **Desktop**. The path should now look like:

```
C:\Users\amogh\Desktop\Project_Osprey_RR_Valuation\
```

---

## Step 2 — Create the public repo on GitHub.com

Open Chrome to <https://github.com/new> and fill in:

| Field | Value |
|---|---|
| Repository name | `rolls-royce-valuation-model` |
| Description | `Institutional DCF valuation of Rolls-Royce Holdings plc (LSE: RR.) — Excel model, IC memo, pitch deck, and Streamlit dashboard.` |
| Visibility | **Public** |
| Initialize with README | **Leave unticked** (we already have one) |
| Add .gitignore | **None** (we already have one) |
| Add a license | **MIT** (optional but recommended for portfolio repos) |

Click **Create repository**.

On the next page, GitHub will show a remote URL like:
```
https://github.com/<your-username>/rolls-royce-valuation-model.git
```
Copy it. You'll paste it in Step 3.

---

## Step 3 — Initialise local Git and push (PowerShell)

Open **PowerShell** (Win+X → "Terminal" or "PowerShell") and run these commands one block at a time.

> Replace `<your-username>` with your actual GitHub username before running the final `git remote add` line.

```powershell
# 1. Navigate to the project root
cd "$env:USERPROFILE\Desktop\Project_Osprey_RR_Valuation"

# 2. Set your identity (one-time, if not already done globally)
git config --global user.email "amoghmallikarjun0321@gmail.com"
git config --global user.name  "Amogh H. H."
git config --global init.defaultBranch main

# 3. Initialise the repo and stage everything (.gitignore is already in place)
git init
git add .

# 4. Make the initial commit
git commit -m "Feat: Initial institutional valuation model and documentation for Rolls-Royce Plc"

# 5. Link to the remote you created in Step 2
git remote add origin https://github.com/<your-username>/rolls-royce-valuation-model.git

# 6. Push to GitHub
git branch -M main
git push -u origin main
```

When git asks for credentials, use a **Personal Access Token** (Settings → Developer settings →
Tokens → Generate new token (classic), `repo` scope is sufficient). Do not paste your password.

---

## Step 3 (alternative) — One-shot with GitHub CLI

If you installed `gh`:

```powershell
cd "$env:USERPROFILE\Desktop\Project_Osprey_RR_Valuation"
git init
git add .
git commit -m "Feat: Initial institutional valuation model and documentation for Rolls-Royce Plc"
gh auth login                 # one-time browser flow
gh repo create rolls-royce-valuation-model --public --source=. --remote=origin --push
```

This single `gh repo create` line creates the GitHub repo AND pushes in one go. Cleaner.

---

## Step 4 — Verify

In Chrome, refresh `https://github.com/<your-username>/rolls-royce-valuation-model`. You should see:

- The README rendering with badges, the headline thesis table, methodology, and run instructions.
- All four subfolders (`01_Source_Data`, `02_Financial_Models`, `03_IC_Deliverables`, `04_Interactive_Dashboard`).
- The Excel, Word, PPTX, and `app.py` files.

If `.docx`/`.xlsx`/`.pptx` files appear as raw binaries (they will — GitHub doesn't preview them inline well), that's expected. Recruiters will download them.

---

## Step 5 — Add it to your portfolio

Once live, add the repo to your portfolio site (`amogh-h-h-portfolio.vercel.app`) with a card linking to:
1. The GitHub repo (`https://github.com/<your-username>/rolls-royce-valuation-model`)
2. A one-line "Live demo" instruction (`pip install -r requirements.txt && streamlit run app.py`)

For LinkedIn featured section, **pin this repo** as a project — recruiters scan the Featured panel first.

---

## Optional polish (do these after the first push lands)

1. **Add a hero image** — open `RR_Strategic_Summary.pptx`, screenshot slide 1, save as `assets/hero.png`, embed at the top of the README.
2. **Add a `LICENSE` file** — paste the [MIT license text](https://opensource.org/license/mit) into `LICENSE`.
3. **Deploy the Streamlit app live** via <https://streamlit.io/cloud> — free for public repos. Once deployed, add the URL as a badge at the top of the README. This is the killer move: recruiters can click and *interact* with your model without cloning anything.
4. **Pin the repo** on your GitHub profile (`github.com/<your-username>` → Customize your pins).

---

## Troubleshooting

| Symptom | Fix |
|---|---|
| `error: src refspec main does not match any` | You didn't commit. Re-run `git add .` then `git commit -m "..."`. |
| `Permission denied (publickey)` | You're using SSH instead of HTTPS. Use the `https://github.com/...` remote URL. |
| `Updates were rejected` | Remote already has commits. Run `git pull origin main --rebase` then `git push`. |
| Large file warning (>50MB) | You shouldn't have any in this repo — but if so, `git rm --cached <file>` and add it to `.gitignore`. |
