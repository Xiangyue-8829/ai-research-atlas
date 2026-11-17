# AI Research Atlas — Roadmap / 建设路线图

## V1 — Public interactive atlas (ready for GitHub Pages)
- [x] 7 editorial layers and 29 research areas
- [x] 323 subtopics, 12 shared bottlenecks, 66 cross-disciplinary relationships
- [x] Overview, branch exploration, bottleneck views, search, export
- [x] Static GitHub Pages publication package
- [x] Public JSON source separate from the HTML (with offline fallback)

## V1.1 — Evidence and quality control
- [ ] Add one complete research card per subtopic (definition, question, assumptions, methods, milestones)
- [ ] Add dated, direct citations for each status claim and open problem
- [ ] Separate evidence-supported relationship from hypothesis and editorial analogy
- [ ] Add source type, publication year, DOI/URL, verification date, and owner
- [ ] Add an explicit version/change-log and correction workflow

## V1.2 — Navigation and accessibility
- [ ] Topic-level deep links and dedicated research pages
- [ ] Filter by topic, maturity, bottleneck, math tools, application area
- [ ] Keyboard navigation, high-contrast modes and mobile improvements
- [ ] Language toggle (Chinese/English) with consistent terminology

## V2 — Research knowledge graph
- [ ] Nodes: area / subfield / method / research problem / paper / benchmark / dataset
- [ ] Typed edges: depends-on / applies-to / shares-assumption / improves-on / overlaps-with / contradicts
- [ ] Versioned evidence: URL/DOI, date, confidence, editor, rationale
- [ ] Structured review process via issues and pull requests
- [ ] Automated link checks and schema validation on pull requests

## V3 — Sustainable update workflow
- [ ] Regular literature ingestion from public metadata and conferences (human reviewed)
- [ ] New-papers feed and timeline, de-duplication and topic tagging
- [ ] Topic owners, evidence audits and contribution policies
- [ ] Mirrored hosting or CDN strategy after verifying regional access

## Suggested evidence standard / 证据规范

For each domain, maintain:
1. **What it studies** — precise research question and boundary.
2. **Mathematical formulation** — variables, objective, assumptions.
3. **Classical results** — landmark methods, with citations.
4. **Current advances** — dated findings supported by direct sources.
5. **Known bottlenecks** — theoretical, empirical, compute, data, evaluation.
6. **Related domains** — typed relationship, rationale and counterexamples.
7. **Verification** — last-reviewed date and responsible reviewer.

Recommended evidence tags: `theory_proven`, `empirical_replicated`, `empirical_single_study`, `survey_consensus`, `editorial_hypothesis`. Avoid presenting speculative links as established facts.

## Scope
The atlas is method- and research-centric, rather than primarily LLM-architecture-centric. It does not preselect any particular user's long-term research specialization.
