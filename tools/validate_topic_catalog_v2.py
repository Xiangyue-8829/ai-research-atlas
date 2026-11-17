"""Validate topic catalog against existing ai_research_atlas_data_2026.json."""
from pathlib import Path
import json,re,sys
root=Path(__file__).resolve().parents[1]
a=json.loads((root/'ai_research_atlas_data_2026.json').read_text(encoding='utf8'))
c=json.loads((root/'data/topic_catalog_v1.json').read_text(encoding='utf8'))
all_keys={f"{d['id']}::{name}" for d in a['domains'] for name in d['topics']}
errors=[]
for k,v in c['topics'].items():
 if k not in all_keys:errors.append(f'Unknown curated topic: {k}')
 for link in v.get('related',[]):
  if link not in all_keys:errors.append(f'Broken relation {k} -> {link}')
 for p in v.get('papers',[]):
  if not re.match(r'^https://',p['url']):errors.append(f'Non-HTTPS literature URL {k} -> {p["url"]}')
slug=lambda n:re.sub(r'^-|-$','',re.sub('[^a-z0-9]+','-',n.lower()))
for d in a['domains']:
 seen={}
 for title in d['topics']:
  s=slug(title)
  if s in seen:errors.append(f'Slug collision {d["id"]}: {title!r} / {seen[s]!r}')
  seen[s]=title
print(f'Atlas: {len(a["domains"])} domains, {len(all_keys)} topic entries, {len(c["topics"])} curated dossiers, {len(c["glossary"])} glossary terms')
for err in errors:print('ERROR:',err)
sys.exit(1 if errors else 0)
