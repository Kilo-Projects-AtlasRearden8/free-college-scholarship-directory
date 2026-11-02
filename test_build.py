#!/usr/bin/env python3
"""Verify the scholarship directory builds cleanly and links resolve."""

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SITE = ROOT / "site"

EXPECTED_PAGES = [
    "index.html",
    "scholarships.html",
    "application-tips.html",
    "essay-help.html",
    "deadline-tracker.html",
    "aid-offices.html",
]

COPYRIGHT_LINE = "Copyright (c) 2026 Asdale Dynamics, LLC"

failures = []


def fail(msg):
    failures.append(msg)
    print(f"FAIL: {msg}")


def check(condition, msg):
    if condition:
        print(f"ok: {msg}")
    else:
        fail(msg)


def main() -> int:
    # 1. Run the build
    print("== Running build.py ==")
    result = subprocess.run(
        [sys.executable, str(ROOT / "build.py")],
        capture_output=True,
        text=True,
    )
    check(result.returncode == 0, "build.py exits 0")
    if result.stdout:
        print(result.stdout.strip())
    if result.returncode != 0:
        print(result.stderr)

    # 2. All expected pages exist
    print("\n== Pages exist ==")
    for page in EXPECTED_PAGES:
        check((SITE / page).exists(), f"{page} exists")

    # 3. Assets exist
    print("\n== Assets exist ==")
    for asset in ["style.css", "app.js", "search.js"]:
        check((SITE / asset).exists(), f"{asset} exists")

    # 4. LICENSE copyright line exact
    print("\n== License ==")
    license_text = (ROOT / "LICENSE").read_text(encoding="utf-8")
    check(COPYRIGHT_LINE in license_text, "LICENSE has exact copyright line")

    # 5. README credits Asdale Dynamics, LLC
    print("\n== README ==")
    readme_text = (ROOT / "README.md").read_text(encoding="utf-8")
    check("Asdale Dynamics, LLC" in readme_text, "README credits Asdale Dynamics, LLC")
    check(COPYRIGHT_LINE in readme_text, "README contains copyright line")

    # 6. Search index valid JSON with all pages
    print("\n== Search index ==")
    search_text = (SITE / "search.js").read_text(encoding="utf-8")
    index_json = search_text.split("=", 1)[1].rstrip(";\n").strip()
    try:
        index = json.loads(index_json)
    except json.JSONDecodeError as exc:
        fail(f"search.js is not valid JSON: {exc}")
        index = []
    if index:
        check(len(index) == len(EXPECTED_PAGES), f"search index has {len(EXPECTED_PAGES)} entries")
        indexed_urls = {e["url"] for e in index}
        check(indexed_urls == set(EXPECTED_PAGES), "search index covers all pages")

    # 7. Footer copyright on every page
    print("\n== Page footers ==")
    for page in EXPECTED_PAGES:
        html = (SITE / page).read_text(encoding="utf-8")
        check(COPYRIGHT_LINE in html, f"{page} footer contains copyright line")
        check('<div id="search-results"></div>' in html, f"{page} has client-side search")

    # 8. Internal links resolve (links between site pages and assets)
    print("\n== Internal links ==")
    page_set = set(EXPECTED_PAGES)
    asset_set = {"style.css", "app.js", "search.js"}
    valid_internal = page_set | asset_set
    link_re = re.compile(r'href="([^"]+)"')
    for page in EXPECTED_PAGES:
        html = (SITE / page).read_text(encoding="utf-8")
        for href in link_re.findall(html):
            if href.startswith("http") or href.startswith("#") or href.startswith("mailto"):
                continue  # external or anchor
            target = href.split("#")[0]
            if target and target not in valid_internal:
                fail(f"{page}: broken internal link -> {href}")
            else:
                print(f"ok: {page} -> {href} (internal)")

    # 9. No secrets / personal data patterns
    print("\n== Secrets scan ==")
    secret_patterns = [
        r"AKIA[0-9A-Z]{16}",
        r"sk-[A-Za-z0-9]{20,}",
        r"ghp_[A-Za-z0-9]{36,}",
        r"password\s*=\s*['\"]?\S+",
        r"api[_-]?key\s*=\s*['\"]?\S+",
    ]
    found_secret = False
    for path in (ROOT / "src").glob("*.md"):
        text = path.read_text(encoding="utf-8")
        for pat in secret_patterns:
            if re.search(pat, text, re.IGNORECASE):
                fail(f"{path.name}: possible secret ({pat})")
                found_secret = True
    if not found_secret:
        print("ok: no secrets in source Markdown")

    # Summary
    print("\n== Summary ==")
    if failures:
        print(f"{len(failures)} failure(s):")
        for f in failures:
            print(f"  - {f}")
        return 1
    print("All checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
