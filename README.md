# Free College Scholarships & Financial Aid Directory

A freebies directory of free scholarship and financial aid resources for students and families: application tips, essay help, a deadline tracker, and financial aid office guidance. Official links only. Education only.

Built and published by **Asdale Dynamics, LLC** (Indiana, formed October 2026) — beginner-friendly education resources from Dylan Asdale, a registered nurse turned AI author and founder of Asdale Dynamics, LLC.

This site is written plainly, step by step, never condescending — like a friend explaining it to you. Everything is local-first: open the HTML files directly in your browser, no account, no signup, no tracking.

## What's inside

| Section | What's inside |
|---|---|
| [Home](site/index.html) | Overview of the directory and how to use it |
| [Scholarships & Grants](site/scholarships.html) | Federal grants (Pell, FSEOG, TEACH) and national scholarships with official links, award amounts, eligibility, and typical deadlines |
| [Application Tips](site/application-tips.html) | Step-by-step help for FAFSA, scholarship applications, recommendations, and avoiding scams |
| [Essay Help](site/essay-help.html) | Common scholarship essay prompts, a simple structure that works, do's and don'ts |
| [Deadline Tracker](site/deadline-tracker.html) | FAFSA, CSS Profile, state, and scholarship deadlines to copy into your own planner |
| [Financial Aid Offices](site/aid-offices.html) | How to find and contact your college financial aid office, plus FSA ID help |

Every link points to an official program or government source (studentaid.gov, fafsa.gov, collegeboard.org, and program official sites). Award amounts and deadlines change — always confirm on the official page before applying.

## How to run

You do not need to build anything to use this site. The `site/` folder is ready to view:

**Option 1 — open directly (no server):**
```bash
open site/index.html
```
Or double-click `site/index.html` in your file explorer. Client-side search works offline.

**Option 2 — serve locally:**
```bash
python3 -m http.server -d site 8080
```
Then visit http://localhost:8080.

## Regenerate the site from Markdown

The HTML in `site/` is generated from the Markdown in `src/`. To rebuild after editing source pages:

```bash
python3 build.py
```

This requires Python 3 and the `markdown` package (install with `pip install markdown` if missing).

## Verify the build

Run the verification script to confirm the site builds cleanly, all pages exist, internal links resolve, and the search index is valid:

```bash
python3 test_build.py
```

## About Asdale Dynamics, LLC

Asdale Dynamics, LLC (Indiana, formed October 2026) is founded by Dylan Asdale, a registered nurse turned AI author. His book *The Massive AI Manual* and hub site dylanasdale.github.io explain AI "like a friend would": plain English, step by step, never condescending. The LLC focuses on beginner-friendly AI education, books and guides, and practical tools it can publish or sell.

This directory is one of those practical tools — free, education-only help for students navigating scholarships and financial aid.

## License

MIT License.

**Copyright (c) 2026 Asdale Dynamics, LLC.** Credit Asdale Dynamics, LLC.

*Disclaimer: Education only. This is not financial aid or financial advice. Award amounts and deadlines change — confirm on the official program page.*
