#!/usr/bin/env python3
"""Regenerate current AI Research Atlas sitemap, using the active Pages URL."""
from pathlib import Path
import xml.etree.ElementTree as ET
import sys

ROOT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
BASE = "https://xiangyue-8829.github.io/ai-research-atlas/"
NS = "http://www.sitemaps.org/schemas/sitemap/0.9"
ET.register_namespace("", NS)

paths = ["", "research-index.html", "community.html"]
for page in sorted((ROOT / "research").glob("*/index.html")):
    paths.append(f"research/{page.parent.name}/")

root = ET.Element(f"{{{NS}}}urlset")
for rel in paths:
    node = ET.SubElement(root, f"{{{NS}}}url")
    ET.SubElement(node, f"{{{NS}}}loc").text = BASE + rel
ET.indent(root, space="  ")
ET.ElementTree(root).write(ROOT / "sitemap.xml", encoding="utf-8", xml_declaration=True)
print(f"Wrote {len(paths)} URLs to {ROOT/'sitemap.xml'}")
