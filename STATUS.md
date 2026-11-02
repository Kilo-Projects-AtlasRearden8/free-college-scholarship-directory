# Status

## What was built

A static "Freebies Directory" site of free scholarship and financial aid resources, published by Asdale Dynamics, LLC (Indiana, formed October 2026), founded by Dylan Asdale — registered nurse turned AI author of *The Massive AI Manual* and hub site dylanasdale.github.io. Written plainly, step by step, never condescending, like a friend explaining it to you. Local-first: open the HTML directly, no account, no signup, no tracking.

Files:
- `src/index.md` — landing page: directory overview and how to use it
- `src/scholarships.md` — federal grants (Pell, FSEOG, TEACH, Iraq/Afghanistan Service) and national scholarships with official links, award amounts, eligibility, typical deadlines
- `src/application-tips.md` — FAFSA, FSA ID, organization, searching smart, avoiding scams, after you apply
- `src/essay-help.md` — common essay prompts, a simple structure that works, do's and don'ts, pre-submit checklist
- `src/deadline-tracker.md` — FAFSA, CSS Profile, state, and scholarship deadlines plus a blank tracker table to copy
- `src/aid-offices.md` — how to find and contact your college financial aid office, what to ask, FSA ID help
- `build.py` — regenerates `site/` from `src/` using Python 3 plus the `markdown` package
- `site/*.html` — six generated static pages with shared navigation, footer, copyright, and client-side search on every page
- `site/style.css`, `site/app.js` — responsive styles and vanilla-JS client-side search (no external dependencies)
- `site/search.js` — inline search index; works with or without a local server
- `test_build.py` — automated verification: build runs, pages exist, assets exist, LICENSE/README copyright, search index valid, internal links resolve, no secrets
- `LICENSE` — MIT License, `Copyright (c) 2026 Asdale Dynamics, LLC`
- `README.md` — credits Asdale Dynamics, LLC; run instructions; regeneration; verification; about; license; disclaimer
- `STATUS.md` — this file

## How to run

No build step required to view. The `site/` folder is ready:

**Option 1 — open directly (works offline):**
```bash
open site/index.html
```
Or double-click `site/index.html`. Client-side search works without a server.

**Option 2 — serve locally:**
```bash
python3 -m http.server -d site 8080
```
Then visit http://localhost:8080.

**Regenerate from Markdown** (after editing `src/`):
```bash
python3 build.py
```
Requires Python 3 and `pip install markdown`.

**Verify the build:**
```bash
python3 test_build.py
```

## Verification results

- `python3 build.py` builds all 6 pages plus `app.js`, `style.css`, `search.js` into `site/` — passes
- `python3 test_build.py` — all checks pass:
  - build.py exits 0
  - all 6 expected pages exist
  - all 3 assets (style.css, app.js, search.js) exist
  - LICENSE contains exact line `Copyright (c) 2026 Asdale Dynamics, LLC`
  - README credits Asdale Dynamics, LLC and contains the copyright line
  - search.js is valid JSON and covers all 6 pages
  - every page footer contains the copyright line
  - every page includes client-side search (`search-results`)
  - all internal links resolve (pages + assets); no broken links
  - no secrets/API-key patterns in source Markdown
- Live server check: all 6 pages + 3 assets return HTTP 200 under `python3 -m http.server -d site`
- Outbound links point only to official program/government sources (studentaid.gov, fafsa.gov, collegeboard.org, program official sites)
- No `.github/workflows` or `.github` directory; no push; no remote created; no secrets/personal data

## Known gaps

- Award amounts and deadlines are typical values captured at build time; users must confirm on official pages before applying (noted in disclaimers).
- Deadline tracker is a static table to copy into a personal planner; no persistent/local-storage tracking in the browser.
- Search matches title and excerpt text only; no filters by state or award type.
- Site is not deployed anywhere (no remote repo, no publishing, per instructions).
