# AI Research Atlas — 当前部署与维护指南

**当前 GitHub 仓库：** https://github.com/Xiangyue-8829/ai-research-atlas-preview

**当前公开网站：** https://xiangyue-8829.github.io/ai-research-atlas-preview/

## 页面结构

| 模块 | 页面 |
|---|---|
| 知识图谱 | `https://xiangyue-8829.github.io/ai-research-atlas-preview/` |
| 研究档案 | `https://xiangyue-8829.github.io/ai-research-atlas-preview/research-index.html` |
| 研究社区 | `https://xiangyue-8829.github.io/ai-research-atlas-preview/community.html` |
| 领域页面 | `https://xiangyue-8829.github.io/ai-research-atlas-preview/research/A5/`（以 A5 为例） |
| 细分专题 | `https://xiangyue-8829.github.io/ai-research-atlas-preview/topic.html?domain=A5&slug=gmrf-spde`（以 GMRF/SPDE 为例） |

- `knowledge-graph.html` 保留用于兼容旧链接，通常会跳转至 `index.html`。
- 29 个领域页面由 `research/<ID>/index.html` 提供稳定 URL。
- 核心 Atlas 数据与论文专题数据独立于显示页面维护。

## 上传静态页面

1. 在 GitHub 打开 https://github.com/Xiangyue-8829/ai-research-atlas-preview，确认在 `main` 分支。
2. 进入 **Add file → Upload files**，上传需要替换的文件和文件夹，保持与本 ZIP 一致的路径。
3. **不要删除** `assets/`、`data/`、`research/` 下其他文件或覆盖你已完成的社区配置。
4. 提交 Commit，等待 Actions 中 Pages 部署显示 `success`。
5. 重新打开网站，使用 `Ctrl + Shift + R` 刷新并验收三个模块。

## 讨论数据与长期保留

社区目前以 `https://github.com/Xiangyue-8829/ai-research-atlas-preview/issues` 作为存储位置。
`data/community_config_v1.json` 和 `assets/community.js` 的 fallback 地址必须与该仓库一致。
只更新 Pages 静态文件不会删除已有 Issues；迁移仓库时应先备份讨论记录。

## SEO

- 页面 `rel=canonical`、研究领域档案以及 `sitemap.xml` 应全部指向当前站点。
- 如要重新生成领域页面，先确认 `tools/build_pages.py` 的 `BASE_URL` 是当前站点。
- 如要生成 Sitemap，使用 `python tools/update_sitemap.py .`，避免旧 URL 重新出现。
- 遗留的 `research-framework*.html` 和 `research_profiles.html` 如仍保持旧版内容，需要另行检查元数据与内部链接。

## 删除旧仓库之前

确认旧网站已停止承担任何外部依赖，包括 GitHub Issues、独立站链接、GitHub Pages 自定义域名、站长工具和个人主页入口。
旧仓库 `Xiangyue-8829/ai-research-atlas` 与本仓库独立，删除前宜备份并逐项确认。
