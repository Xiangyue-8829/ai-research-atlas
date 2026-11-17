# AI Research Atlas · SEO & Preview Update (2026-11-15)

## What this upgrade includes

- **index.html**: fixes UAI / ICML / other citation IDs that previously sent users to nonexistent `/uai` paths; preserves current fullscreen + Chinese/English functionality; adds SEO title/description, canonical URL, social preview metadata, and a link to a new search-readable framework page.
- **research_profiles.html**: adds page-specific meta title, description, canonical URL, and social-preview metadata.
- **research-framework.html**: public Chinese static research framework with 7 layers and 29 fields.
- **research-framework-en.html**: public English framework, separate URL with hreflang alternatives.
- **sitemap.xml**: four actual page URLs. Submit to Google Search Console and Bing Webmaster Tools; it does not guarantee indexing.
- **AI_Research_Atlas_preview.png**: existing atlas screenshot used as OG preview image; can also be uploaded to repository Settings → Social preview.
- **README.md**: prominently displays clickable live website and bilingual research framework links.

## Deployment

Upload extracted files into the root of the existing `Xiangyue-8829/ai-research-atlas` repository on `main` (NOT the ZIP itself). Replace the existing `index.html`, `research_profiles.html`, and `README.md`; add the two static guide files, `sitemap.xml`, and `AI_Research_Atlas_preview.png`. Keep all other JSON, SVG and research files. Check Actions → pages build and deployment (green check).

If GitHub web upload refuses replacing existing files, open the existing file, click Edit (pencil), paste the new full content, and commit; or use GitHub Desktop to copy and commit all files together.

## GitHub About / Preview website link

Go to Repository → Code → About (right sidebar) → gear/Edit → Website → `https://xiangyue-8829.github.io/ai-research-atlas/` → Save. Fill Description and add Topics such as `artificial-intelligence`, `research-map`, `machine-learning`, `knowledge-graph`, `ai-research`.

GitHub's repository **Social preview** is a *picture* for sharing a GitHub repo URL; upload `AI_Research_Atlas_preview.png` through Settings → Social preview. Its image is not a way to create a clickable site link. The clickable Website field belongs in the About section.

## Submit sitemap for discovery

- Google Search Console: create a **URL-prefix property** `https://xiangyue-8829.github.io/ai-research-atlas/`; verify ownership using an HTML verification file uploaded to the repo root or a meta tag provided by Google (do not fabricate tokens); submit `https://xiangyue-8829.github.io/ai-research-atlas/sitemap.xml` in Sitemaps; URL inspection → Request indexing.
- Bing Webmaster Tools: add/verify the website; submit the same sitemap. URL submission is also available.
- Baidu Search Resource Platform: add/verify when available, submit links; GitHub Pages accessibility from mainland China varies, so successful crawl/indexing cannot be guaranteed.

**Caveat:** A GitHub Pages *project site* cannot normally set the host-root `https://xiangyue-8829.github.io/robots.txt` from its `/ai-research-atlas/` repository. A `robots.txt` under the project path is not a substitute for the host-root robots.txt. Submit the XML sitemap explicitly in the webmaster tools.

**SEO limitations:** SEO metadata and sitemap do not ensure ranking, indexing or discovery. Google recommends distinct URLs for localized language versions; this package adds Chinese and English static framework URLs. The main interactive atlas still switches language client-side. Much of the canvas content is JS-rendered, so these static pages make domain terms easier to crawl. Rankings depend on crawlability, content quality, citations, incoming links, and search intent.
