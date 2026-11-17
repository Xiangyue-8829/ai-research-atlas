# AI Research Atlas · 人工智能研究知识图谱

**Website / 在线网站：** https://xiangyue-8829.github.io/ai-research-atlas-preview/

A bilingual, interactive research atlas for prospective AI PhD students and researchers. It connects research fields, detailed topics, foundational papers, open questions and scholarly discussions.

AI Research Atlas 为有意攻读 AI 相关博士学位的读者和研究者提供可探索的研究知识地图、研究档案、专题论文入口与学术讨论空间。

## Explore / 网站入口

- [Knowledge Graph · 知识图谱](https://xiangyue-8829.github.io/ai-research-atlas-preview/)
- [Research Library · 研究档案](https://xiangyue-8829.github.io/ai-research-atlas-preview/research-index.html)
- [Research Community · 研究社区](https://xiangyue-8829.github.io/ai-research-atlas-preview/community.html)
- [AI Research Landscape · 中文研究框架](https://xiangyue-8829.github.io/ai-research-atlas-preview/research-framework.html)
- [AI Research Landscape · English](https://xiangyue-8829.github.io/ai-research-atlas-preview/research-framework-en.html)

## Structure / 项目结构

- `index.html`: main interactive knowledge graph / 研究知识图谱首页。
- `research-index.html`: directory of 29 research fields / 29 个主要研究领域入口。
- `research/<ID>/index.html`: stable field profiles / 各研究领域独立档案。
- `topic.html`: topic dossier viewer / 细分专题档案页面。
- `community.html`: research discussion UI / 学术讨论入口。
- `ai_research_atlas_data_2026.json`: research taxonomy / 领域分类和关系。
- `data/topic_catalog_v1.json`: curated topic notes / 首批专题内容及文献。
- `data/community_config_v1.json`: GitHub Issues data repository / 社区数据仓库配置。
- `sitemap.xml`: list of primary indexable pages.

## Research quality / 内容定位

Research maturity statements, suggested relations, and open problems are editorial syntheses, not official rankings or exhaustive systematic reviews. Refer to original publications for academic claims; hypotheses and community proposals are not automatically accepted as verified findings.

研究现状、跨领域关联与开放问题属于编辑性综合整理，并非官方评级。论文与研究判断应明确引用来源；社区讨论未经审查不自动写入正式档案。

## Community storage / 社区数据

The current forum uses public GitHub Issues in **[https://github.com/Xiangyue-8829/ai-research-atlas-preview](https://github.com/Xiangyue-8829/ai-research-atlas-preview/issues)**. Posting or replying requires a GitHub account. Updating the website does not erase issues, but deleting the issue-hosting repository does.

当前讨论记录保存在本仓库的 GitHub Issues；更新网页不会清空帖子，但删除 Issues 或所在仓库可能造成数据丢失。

## Maintenance / 维护

Keep the canonical URLs, `sitemap.xml`, and GitHub repository links aligned with https://xiangyue-8829.github.io/ai-research-atlas-preview/. Before renaming or deleting a repository, check Pages configuration, topic links, community backend, and search-engine properties.

See `README_DEPLOY.md` and `ROADMAP.md` for deployment and roadmap notes. This project remains under development; no open-source license has been selected yet.
