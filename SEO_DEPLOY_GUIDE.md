# AI Research Atlas — SEO 与站点迁移指南

**当前公开站点：** https://xiangyue-8829.github.io/ai-research-atlas-preview/

**GitHub 仓库：** https://github.com/Xiangyue-8829/ai-research-atlas-preview

## 1. Canonical 与站点地址

所有主页面的 `<link rel="canonical">` 应与其真正 URL 一致，不要再指向已弃用的旧仓库网站。

- 首页：`https://xiangyue-8829.github.io/ai-research-atlas-preview/`
- 研究档案：`https://xiangyue-8829.github.io/ai-research-atlas-preview/research-index.html`
- 研究社区：`https://xiangyue-8829.github.io/ai-research-atlas-preview/community.html`
- 领域：`https://xiangyue-8829.github.io/ai-research-atlas-preview/research/A5/`（示例）
- 静态研究框架：`https://xiangyue-8829.github.io/ai-research-atlas-preview/research-framework.html`、`research-framework-en.html`

`knowledge-graph.html` 是旧图谱链接兼容页面；不应在 Sitemap 中作为第二个独立首页。
细分专题页面有动态参数，不能将不带参数的 `topic.html` 一律作为完整研究档案提交。

## 2. Sitemap

在 GitHub Pages 根目录维护 `sitemap.xml`。包括当前主页、领域目录、研究社区、29 个领域页面。

运行：

```bash
python tools/update_sitemap.py .
```

此脚本将统一采用当前发布站点 URL，并避免把已退役网址重新写入。

## 3. Google Search Console / Bing Webmaster Tools

为 `https://xiangyue-8829.github.io/ai-research-atlas-preview/` 建立对应的 URL-prefix 属性，按站长平台给出的验证方式确认所有权；提交：

`https://xiangyue-8829.github.io/ai-research-atlas-preview/sitemap.xml`

如已有旧属性，不要误以为新路径会自动继承原地址的所有验证和收录记录。

## 4. GitHub About / Website

在仓库首页右侧的 About → Edit，填写当前网站网址 `https://xiangyue-8829.github.io/ai-research-atlas-preview/`。

## 5. 内容与权限

公开网站、robots/sitemap 与 GitHub 仓库是不同的资源；不要把仓库路径修改理解成旧外部链接永久自动重定向。
研究社区内容保存在 GitHub Issues；不要在未迁移讨论记录前删除当前 Issues 仓库。

## 6. 遗留页面注意

旧版静态页面 `research-framework.html`、`research-framework-en.html` 和 `research_profiles.html` 如果继续用于搜索收录，仍需后续单独更新其旧版 Canonical、Open Graph 与 JSON-LD 元信息。
本次补丁针对当前 V2.2 活跃入口和 29 个领域档案，不以简化页面覆盖旧版研究内容。
