# Status

## What was built

A static "Freebies Directory" site of free scholarship and financial aid resources, published by Asdale Dynamics, LLC.

Files:
- `src/index.md` — landing page with section overview
- `src/scholarships.md` — directory of federal grants and national scholarships with official links, award amounts, eligibility, and typical deadlines
- `src/application-tips.md` — step-by-step application guidance
- `src/essay-help.md` — scholarship essay prompts, structure, do's and don'ts
- `src/deadline-tracker.md` — FAFSA, CSS Profile, state, and scholarship deadlines plus a blank tracker table
- `src/aid-offices.md` — how to find and contact college financial aid offices, FSA ID help
- `build.py` — regenerates `site/` from `src/` using only Python standard library plus `markdown` (already installed)
- `site/*.html` — generated static pages with shared navigation, footer, and copyright
- `site/style.css`, `site/app.js` — styles and vanilla-JS client-side search
- `site/search.js` — inline search index (works with or without a local server; no external dependencies)
- `LICENSE` — MIT License, `Copyright (c) 2026 Asdale Dynamics, LLC`
- `README.md` — project credits Asdale Dynamics, LLC; run instructions
- `STATUS.md` — this file

## How to run

Option 1 (no server): open `site/index.html` directly in a browser. Client-side search works offline.

Option 2 (local server):

```bash
python3 -m http.server -d site 8080
```

Then visit http://localhost:8080.

To regenerate the site from Markdown:

```bash
python3 build.py
```

## Verification results

- `python3 build.py` builds all 6 pages plus `app.js`, `style.css`, and `search.js` into `site/` — OK
- All 6 pages plus assets return HTTP 200 under `python3 -m http.server` — OK
- `site/search.js` parses as valid JSON and contains all 6 pages — OK
- Navigation links resolve across pages; all outbound links point to official program/government sources (studentaid.gov, fafsa.gov, collegeboard.org, program official sites) — OK
- `LICENSE` contains exactly `Copyright (c) 2026 Asdale Dynamics, LLC`; README and page footers credit Asdale Dynamics, LLC — OK
- Scan for secrets/API keys/personal data: none found — OK
- No `.github/workflows` or `.github` directory — OK

## Known gaps

- Award amounts and deadlines are typical values captured at build time; users must confirm on official pages before applying (noted in disclaimers).
- Deadline tracker is a static table for copying into a personal planner; no persistent/local-storage tracking in the browser.
- Search matches title and excerpt text only; no filters by state/award type.
- Site is not deployed anywhere (no remote repo, no publishing, per instructions).
