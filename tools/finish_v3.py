#!/usr/bin/env python3
"""Finalize AI Research Atlas V3 in a local checkout of the OFFICIAL repository.

Run this from the repo root AFTER copying the V3 files. Safe to re-run.
- Switch old preview URL/repo strings to permanent official URL.
- Add opt-in visual polish to original research/topic/community pages.
- Generate a conservative, canonical, navigable sitemap.
- Keep the existing 29 dossier URLs/data and all published Git history intact.
"""
from __future__ import annotations

import html
import re
from pathlib import Path

BASE = "https://xiangyue-8829.github.io/ai-research-atlas/"
OLD_URL = "https://xiangyue-8829.github.io/ai-research-atlas/"
OLD_REPO = "Xiangyue-8829/ai-research-atlas"
NEW_REPO = "Xiangyue-8829/ai-research-atlas"
ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {".git", ".venv", "node_modules", "__pycache__", ".pytest_cache"}
TEXT_SUFFIXES = {".html", ".xml", ".md", ".json", ".js", ".css", ".py", ".svg", ".txt", ".yml", ".yaml"}


def text_files():
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        if any(part in SKIP_DIRS for part in path.relative_to(ROOT).parts):
            continue
        # Do not modify binary / deeply archived files.
        if path.stat().st_size > 1_500_000:
            continue
        yield path


def normalize_all():
    changed = []
    for path in text_files():
        original = path.read_text(encoding="utf-8")
        new = original.replace(OLD_URL, BASE).replace(OLD_REPO, NEW_REPO)
        # Preserve the subpage visual layer when future runs regenerate all 29 dossiers.
        if path.relative_to(ROOT).as_posix() == "tools/build_pages.py":
            original_line = '<link rel="stylesheet" href="../../assets/research-profile.css">'
            if 'dossier-v3.css' not in new and original_line in new:
                new = new.replace(original_line, original_line + '\n<link rel="stylesheet" href="../../assets/dossier-v3.css">')
        # New page resources are relative to the repository root.
        rel = path.relative_to(ROOT)
        if path.suffix.lower() == ".html" and (path.name in {"topic.html", "community.html"} or
                                                 (len(rel.parts) == 3 and rel.parts[0] == "research" and rel.name == "index.html")):
            asset = "../../assets/dossier-v3.css" if rel.parts[0] == "research" else "./assets/dossier-v3.css"
            icon = "../../favicon.svg" if rel.parts[0] == "research" else "./favicon.svg"
            if "dossier-v3.css" not in new and "</head>" in new:
                new = new.replace("</head>", f'<link rel="stylesheet" href="{asset}">\n</head>', 1)
            if "favicon.svg" not in new and "</head>" in new:
                new = new.replace("</head>", f'<link rel="icon" type="image/svg+xml" href="{icon}">\n</head>', 1)
        if new != original:
            path.write_text(new, encoding="utf-8")
            changed.append(str(rel))
    return changed


def update_sitemap():
    # Only include stable server-addressable HTML pages. Client-rendered query
    # dossiers do not get SEO promises until proper prerendering exists.
    pages = ["", "research-index.html", "about.html", "changelog.html", "community.html",
             "research-framework.html", "research-framework-en.html"]
    pages += [f"research/{p.name}/" for p in sorted((ROOT / "research").iterdir())
              if p.is_dir() and (p / "index.html").exists()]
    # Do not write false change dates; GitHub pages deployment time != page update time.
    entries = [f"  <url><loc>{html.escape(BASE + p)}</loc></url>" for p in pages if not p or (ROOT / p).exists()]
    document = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(entries) + "\n</urlset>\n"
    (ROOT / "sitemap.xml").write_text(document, encoding="utf-8")
    return len(entries)


def main():
    if not (ROOT / "ai_research_atlas_data_2026.json").exists():
        raise SystemExit("ERROR: Run from a complete AI Research Atlas checkout. Original data JSON is missing.")
    if not (ROOT / "index.html").exists() or not (ROOT / "assets" / "atlas-v3.js").exists():
        raise SystemExit("ERROR: Copy the V3 package into the repository root first.")
    changed = normalize_all()
    n = update_sitemap()
    robots = f"User-agent: *\nAllow: /\n\nSitemap: {BASE}sitemap.xml\n"
    (ROOT / "robots.txt").write_text(robots, encoding="utf-8")
    print("V3 FINISH COMPLETE")
    print(f"  Normalized files: {len(changed)}")
    print(f"  Sitemap URLs: {n}")
    print(f"  Public homepage: {BASE}")
    print("  Existing /research/{ID}/ paths have been preserved.")
    print("  Next: python tools/check_v3.py")


if __name__ == "__main__":
    main()
