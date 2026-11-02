#!/usr/bin/env python3
"""Build the static HTML site from Markdown sources."""

import json
import re
import shutil
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
SITE = ROOT / "site"

MARKDOWN_EXTENSIONS = ["tables", "fenced_code", "toc", "md_in_html"]

PAGES = [
    ("index.md", "index.html", "Home"),
    ("scholarships.md", "scholarships.html", "Scholarships & Grants"),
    ("application-tips.md", "application-tips.html", "Application Tips"),
    ("essay-help.md", "essay-help.html", "Essay Help"),
    ("deadline-tracker.md", "deadline-tracker.html", "Deadline Tracker"),
    ("aid-offices.md", "aid-offices.html", "Financial Aid Offices"),
]

NAV = [
    ("index.html", "Home"),
    ("scholarships.html", "Scholarships & Grants"),
    ("application-tips.html", "Application Tips"),
    ("essay-help.html", "Essay Help"),
    ("deadline-tracker.html", "Deadline Tracker"),
    ("aid-offices.html", "Financial Aid Offices"),
]

COPYRIGHT = "Copyright (c) 2026 Asdale Dynamics, LLC"


def strip_html(text: str) -> str:
    text = re.sub(r"<[^>]+>", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def build_search_index() -> list[dict]:
    index = []
    for src_name, html_name, title in PAGES:
        md = (SRC / src_name).read_text(encoding="utf-8")
        html = markdown.markdown(md, extensions=MARKDOWN_EXTENSIONS)
        text = strip_html(html)
        index.append(
            {
                "title": title,
                "url": html_name,
                "excerpt": text[:400],
            }
        )
    return index


def page_template(title: str, active: str, body: str, search_script: str, search_box: str = "") -> str:
    nav_items = "".join(
        f'<li><a href="{url}" class={"active" if url == active else ""}>{label}</a></li>'
        for url, label in NAV
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — Free College Scholarships & Financial Aid Directory</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
<header class="site-header">
<div class="container">
<h1 class="site-title"><a href="index.html">Free College Scholarships &amp; Financial Aid Directory</a></h1>
<p class="site-tagline">Official links only. Education only. Published by Asdale Dynamics, LLC.</p>
</div>
</header>
<nav class="site-nav">
<div class="container">
<ul>{nav_items}</ul>
</div>
</nav>
<main class="container">
{search_box}
<article>
{body}
</article>
</main>
<footer class="site-footer">
<div class="container">
<p>{COPYRIGHT}. All rights reserved. Education only — not financial advice.</p>
</div>
</footer>
{search_script}
</body>
</html>"""


def main() -> None:
    if SITE.exists():
        shutil.rmtree(SITE)
    SITE.mkdir(parents=True)

    # Copy static assets
    shutil.copy(ROOT / "style.css", SITE / "style.css")
    shutil.copy(ROOT / "app.js", SITE / "app.js")

    search_index = build_search_index()
    (SITE / "search.js").write_text(
        "window.SEARCH_INDEX = " + json.dumps(search_index, indent=2) + ";\n",
        encoding="utf-8",
    )

    for src_name, html_name, title in PAGES:
        md = (SRC / src_name).read_text(encoding="utf-8")
        body = markdown.markdown(md, extensions=MARKDOWN_EXTENSIONS)
        active = html_name
        search_script = (
            '<script defer src="search.js"></script>'
            '<script defer src="app.js"></script>'
            if html_name == "index.html"
            else ""
        )
        search_box = (
            '<section id="search">'
            '<label for="search-input">Search this directory</label>'
            '<input type="text" id="search-input" placeholder="Search scholarships, deadlines, essays...">'
            '<button type="button" id="search-button">Search</button>'
            '<div id="search-results"></div>'
            "</section>"
            if html_name == "index.html"
            else ""
        )
        html = page_template(title, active, body, search_script, search_box)
        (SITE / html_name).write_text(html, encoding="utf-8")

    print(f"Built {len(PAGES)} pages into {SITE}")


if __name__ == "__main__":
    main()
