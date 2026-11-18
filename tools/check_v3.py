#!/usr/bin/env python3
"""Check V3 source content, links, taxonomy invariants and permanent SEO URLs."""
from __future__ import annotations

import json
import re
import sys
import urllib.parse
from pathlib import Path
from html.parser import HTMLParser
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent
OFFICIAL = "https://xiangyue-8829.github.io/ai-research-atlas/"


def slug(x):
    import unicodedata
    return re.sub(r"(^-+|-+$)", "", re.sub(r"[^a-z0-9]+", "-", unicodedata.normalize("NFKD", x.lower())))


class Extractor(HTMLParser):
    def __init__(self):
        super().__init__(); self.urls = []; self.ids = set()

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if "id" in d:
            if d["id"] in self.ids: raise AssertionError("Duplicate id: " + d["id"])
            self.ids.add(d["id"])
        for attr in ("href", "src"):
            if d.get(attr): self.urls.append((attr, d[attr]))


def main():
    errors = []
    def check(cond, text):
        if not cond: errors.append(text)
    files = ["index.html", "research-index.html", "about.html", "changelog.html", "topic.html", "community.html", "robots.txt", "sitemap.xml", "favicon.svg", "assets/atlas-v3.js", "assets/atlas-v3.css", "assets/library-v3.css", "assets/research-index-v3.js", "assets/pages-v3.js", "assets/pages-v3.css", "assets/dossier-v3.css"]
    for f in files: check((ROOT/f).exists(), "Missing file "+f)
    if not (ROOT/"ai_research_atlas_data_2026.json").exists(): errors.append("Original Atlas JSON missing")
    if errors: print("\n".join(errors)); return 1
    atlas = json.loads((ROOT/"ai_research_atlas_data_2026.json").read_text(encoding="utf-8"))
    domains=atlas["domains"];topics=sum(len(d.get("topics",[])) for d in domains)
    keys=set(); slugs=set()
    for d in domains:
        check(d["id"] not in keys,"Duplicate field ID "+d["id"]); keys.add(d["id"])
        check((ROOT/"research"/d["id"]/"index.html").exists(),"Missing domain page "+d["id"])
        for t in d.get("topics",[]):
            ident=(d["id"],slug(t));check(ident not in slugs,"Ambiguous topic slug "+str(ident));slugs.add(ident)
    catalog=json.loads((ROOT/"data"/"topic_catalog_v1.json").read_text(encoding="utf-8"))
    for k in catalog.get("topics",{}):
        if "::" not in k: errors.append("Invalid curated topic key "+k); continue
        did,name=k.split("::",1);check(any(d["id"]==did and name in d.get("topics",[]) for d in domains),"Unmatched curated topic "+k)
    check(len(domains)>=29,"Expected at least 29 fields, got "+str(len(domains)))
    check(topics>=323,"Expected at least 323 topics, got "+str(topics))
    sitemap=ET.fromstring((ROOT/"sitemap.xml").read_text(encoding="utf-8"))
    locations=[n.text for n in sitemap.iter() if n.tag.endswith("loc")]
    check(len(locations)>=34,"Too few entries in sitemap: "+str(len(locations)))
    check(all(u.startswith(OFFICIAL) and "preview" not in u for u in locations),"Sitemap contains non-official URL")
    for p in ROOT.rglob("*.html"):
        if ".git" in p.parts: continue
        rel=p.relative_to(ROOT); txt=p.read_text(encoding="utf-8")
        if "ai-research-atlas-preview" in txt: errors.append("preview URL in "+str(rel))
        try:
            parser=Extractor();parser.feed(txt)
        except Exception as e: errors.append(str(rel)+" parse/id problem: "+str(e));continue
        for attr,url in parser.urls:
            if not url or url.startswith(("http:","https:","mailto:","data:","javascript:","#")): continue
            if url.startswith("/"):continue
            target=urllib.parse.urlsplit(url).path
            if not target: continue
            loc=(p.parent / urllib.parse.unquote(target)).resolve()
            if target.endswith("/"):loc=loc/"index.html"
            if not loc.is_file():errors.append(f"Broken local {attr} in {rel}: {url}")
    print(f"Checked {len(domains)} fields, {topics} topics, {len(catalog.get('topics',{}))} curated records and {len(locations)} sitemap URLs")
    if errors:
        print("FAILED (%s issues)"%len(errors))
        print("\n".join(" - "+e for e in errors[:65]))
        return 1
    print("PASS: V3 repository and main internal links are consistent")
    return 0


if __name__ == "__main__": sys.exit(main())
