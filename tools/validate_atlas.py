#!/usr/bin/env python3
"""Validate the existing site's 2026 data against this additive graph/profile package.
Usage: python tools/validate_atlas.py /path/to/full/repository/root
"""
import json
import sys
from pathlib import Path

ROOT=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path(__file__).resolve().parents[1]

def load(name, required=True):
    f=ROOT/name
    if not f.exists():
        if required: raise FileNotFoundError(f'Missing {f}; merge the patch with the existing AI Research Atlas root first')
        return None
    return json.loads(f.read_text(encoding='utf-8'))

def main():
    data=load('ai_research_atlas_data_2026.json')
    assert len(data['layers'])==7, 'Unexpected layer count'
    dom={d['id']:d for d in data['domains']}
    assert len(dom)==len(data['domains']), 'Duplicate field IDs'
    assert len(dom)==29, 'Unexpected number of core directions; review page-generation script before migrating'
    probs={p['id']:p for p in data['problems']}
    assert len(probs)==len(data['problems']), 'Duplicate bottleneck IDs'
    for d in dom.values():
        assert d['layer'] in {l['id'] for l in data['layers']}, f'Unknown layer {d["id"]}'
        assert (ROOT/'research'/d['id']/'index.html').exists(), f'Profile route missing for {d["id"]}'
    for i,l in enumerate(data['links']):
        assert l['a'] in dom and l['b'] in dom, f'Broken relation {i}: {l}'
        assert l['a']!=l['b'], f'Self relation {i}'
        assert l['type'] in {'theory','method','enables','dependency','intersection'}, f'Unknown relation type {l["type"]}'
    for p in probs.values():
        assert set(p['areas'])<=dom.keys(), f'Broken bottleneck {p["id"]}'
    profiles=load('research_profiles_2026.json',False)
    en=load('atlas_en_2026.json',False)
    profiles_en=load('research_profiles_en_2026.json',False)
    if profiles:
        for p in profiles['profiles']:
            assert p['id'] in dom, f'Pilot specializes an unknown field {p["id"]}'
    if en:
        assert set(en['domains'].keys())==set(dom), 'English domain IDs not aligned'
    if profiles_en:
        assert set(profiles_en['profiles'].keys())<=set(dom), 'English pilot ID mismatch'
    print(f'PASS: {len(dom)} domains, {sum(len(d.get("topics",[])) for d in data["domains"])} nested topics, {len(probs)} bottlenecks, {len(data["links"])} edges, {len(profiles["profiles"]) if profiles else 0} rich pilot dossiers.')

if __name__=='__main__':
    main()
