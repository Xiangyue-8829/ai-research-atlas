#!/usr/bin/env python3
"""Add the 29 research URLs and knowledge graph to an existing sitemap.xml, idempotently."""
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path(__file__).resolve().parents[1]
file=ROOT/'sitemap.xml'
if not file.exists():
    raise SystemExit(f'No sitemap.xml found in {ROOT}. Merge patch into the existing repository before running.')
NS='http://www.sitemaps.org/schemas/sitemap/0.9'
ET.register_namespace('',NS)
tree=ET.parse(file)
root=tree.getroot()
existing={x.text.strip() for x in root.findall(f'.//{{{NS}}}loc') if x.text}
base='https://xiangyue-8829.github.io/ai-research-atlas'
ids=['A1','A2','A3','A4','A5','A6','B1','B2','B3','B4','B5','C1','C2','C3','C4','C5','C6','D1','D2','D3','D4','D5','E1','E2','E3','F1','F2','G1','G2']
urls=[f'{base}/knowledge-graph.html']+[f'{base}/research/{id_}/' for id_ in ids]
added=0
for url in urls:
    if url in existing:continue
    row=ET.SubElement(root,f'{{{NS}}}url')
    ET.SubElement(row,f'{{{NS}}}loc').text=url
    added+=1
ET.indent(tree,space='  ')
tree.write(file,encoding='utf-8',xml_declaration=True)
print(f'Sitemap updated: {added} new URLs; {len(urls)-added} already present.')
