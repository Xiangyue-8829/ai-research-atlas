# AI Research Atlas V2.2 — Knowledge Graph + Research Library + Research Community

## 这次升级解决什么

1. **首页是唯一的知识图谱** (`index.html`)，`knowledge-graph.html` 仅保留兼容跳转，不再有两张重复图。
2. 全站主要导航统一为 **知识图谱 / 研究档案 / 研究社区**。更改 `index.html`、`research-index.html`、`topic.html`，以及对应的 JS；所有 `research/<ID>/` 由共享 `research-profile.js` 自动生成第三个导航入口，**不必覆盖 29 个研究档案的 HTML**。
3. 新增 `/community.html`：浏览 GitHub 公开议题、按学术讨论类型筛选、发起新的研究问题或论文推荐等；从领域和细分主题带入上下文。
4. 社区后端目前使用 **当前网站仓库** `Xiangyue-8829/ai-research-atlas-preview` 的公开 GitHub Issues；GitHub Pages 不需要服务器数据库，发帖和回复需要 GitHub 账号。所有内容公开，不会自动成为经核验的档案结论。

## 需要上传的文件（仅 12 个）

请先**下载并解压本 ZIP**，将解压后的文件及目录结构放到现有的 GitHub 预览仓库根目录：

`https://github.com/Xiangyue-8829/ai-research-atlas-preview`

确保在 `main` 分支。合并并替换已有的同名文件：

- `index.html`
- `knowledge-graph.html`
- `research-index.html`
- `topic.html`
- `community.html`（新增）
- `assets/atlas-kg.js`
- `assets/research-profile.js`
- `assets/topic.js`
- `assets/community.css`（新增）
- `assets/community.js`（新增）
- `data/community_config_v1.json`（新增）
- `README_V2_2_COMMUNITY.md`（此文档）

**请勿删除**现有 Atlas 主 JSON 数据、29 个研究档案目录、`topic_catalog_v1.json`、CSS、SEO 文件等。上传后检查 GitHub Pages Actions 构建完成，再访问：

- `https://xiangyue-8829.github.io/ai-research-atlas-preview/` → 知识图谱
- `https://xiangyue-8829.github.io/ai-research-atlas-preview/research-index.html` → 研究档案
- `https://xiangyue-8829.github.io/ai-research-atlas-preview/community.html` → 研究社区
- `/research/A5/` → 领域档案顶部可见“研究社区”，带领域信息跳转
- `/topic.html?domain=A5&slug=gmrf-spde` → 细分专题的讨论链接带领域和主题信息

## GitHub Issues beta 如何工作

站内近期讨论区只读取公开 Issues API；**只有**以 `[Research Question]`、`[Paper Recommendation]`、`[Methodological Critique]`、`[Cross-field Connection]`、`[Correction]` 为前缀的议题会显示在站内。所有讨论仍可从“在 GitHub 查看所有讨论”打开。

访客在网站填写内容后，点击“前往 GitHub 完成发布”，会打开**预填写的 GitHub Issue 编辑页**；只有访客在 GitHub 页面最终提交，内容才真正发布。关闭页面或取消不会发布。

讨论目前归属于 `Xiangyue-8829/ai-research-atlas-preview` 的 Issues。后续若更名或迁移仓库，需先核对社区配置与历史数据。

## GitHub Discussions / giscus 的下一阶段

当前正式及预览仓库的 `Discussions` 尚未启用。若需要**直接嵌入站内评论**，下一阶段：

1. 到正式仓库 `Settings → General → Features` 勾选 **Discussions**。GitHub Docs: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/enabling-or-disabling-github-discussions-for-a-repository
2. 按研究讨论分类设置 Discussions 分类和社区规范。
3. 在 `https://giscus.app/` 配置 GitHub App、存储库、分类及 URL 映射，将其提供的特定配置接入每份档案。
4. 迁移前明确历史 Issues 是否保留、关闭还是转为 Discussions；**不能假定会自动迁移**。

本补丁**不会假装 GitHub Discussions 或 giscus 已经启用**。现阶段已经可以用 GitHub Issues 开启公开研究议题，站内评论嵌入需另行配置。

## 部署限制

当前 ChatGPT 侧 GitHub 写操作曾返回 `403 Resource not accessible by integration`，因此这里交付的是**可直接上传的代码补丁**，不会自动修改你正在运行的网站。
