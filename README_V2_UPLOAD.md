# AI Research Atlas V2 — 预览版升级包

**适用仓库：** `Xiangyue-8829/ai-research-atlas-preview`（已经建立的 GitHub Pages 预览仓库）。

**本包是增量覆盖包，不是整个网站。** 必须在已经含有 `research/A1/` 到 `research/G2/`、原始 2026 JSON 的预览仓库中使用。

## 本次改动

- 新 `index.html` 即交互知识图谱，导航不再返回旧版首页。
- 新增 `research-index.html`：7 层、29 方向的档案索引。
- 原有 29 个 `research/<ID>/` 档案页面通过共享 JS 直接获得可点击的全部 323 个细分主题入口（无需改写 29 个 HTML）。
- `topic.html` / `assets/topic.js` / `assets/topic.css`：支持 `?domain=A5&slug=gmrf-spde&lang=zh` 的可分享二级专题地址。
- 15 个细分主题有编辑性中英文解释、核心研究问题、17 个精选原始文献链接；其余细分主题可点击，但明确标注“待完善”，不伪造论文。
- 24 个鼠标悬停／键盘聚焦术语卡；发现文本中的对应研究主题／领域名称时可点击跳转（对重名主题避免猜测目标，仍可在相关主题区链接）。
- 每个专题有按新到旧搜索 arXiv 的入口，这是**未经人工审核的外部搜索结果**，与站内精选论文分开。
- 讨论阶段一：研究档案与细分专题包含 GitHub Issues 讨论入口。需要访客有 GitHub 账号；尚未是站内的嵌入式论坛。后续可转 GitHub Discussions + giscus，需要仓库所有者启用 Discussions 并安装 giscus。

## 将文件覆盖到预览仓库（无需 localhost）

1. 建议先在预览仓库页面使用 **Code → Download ZIP** 备份当前版本。
2. 在 `https://github.com/Xiangyue-8829/ai-research-atlas-preview` 的 **main** 分支，点击 **Add file → Upload files**。
3. 解压本包，将**包内文件与 assets、data、tools 子文件夹**拖拽上传，保持原始路径。**不要把 ZIP 作为单个文件上传，也不要创建套娃文件夹。**
4. 上传时，GitHub 若提示同名文件将被替换，按此次改动覆盖；**不得删除旧的四份主 JSON、原来的 `research/` 目录和其他图片 / SEO 文件**。
5. 提交变更后打开 `https://xiangyue-8829.github.io/ai-research-atlas-preview/`，按 Ctrl+Shift+R 刷新，等待 GitHub Pages 发布状态显示成功。
6. 验收以下关键页面：
   - 根目录 `/`：直接显示新版交互知识图谱。
   - `/research-index.html`：29 个研究方向入口。
   - `/research/A5/`：细分主题由纯文本改成可点击卡片。
   - `/topic.html?domain=A5&slug=gmrf-spde&lang=zh`：SPDE 专题、论文、关联研究与术语解释。
   - `/topic.html?domain=E1&slug=mechanistic-interpretability&lang=zh`：机制可解释性专题。

**当前网站以 `https://xiangyue-8829.github.io/ai-research-atlas-preview/` 为实际站点。旧仓库计划退役；请勿按旧说明将文件再合并回已废弃的原仓库。**

## 学术标记与维护

- `data/topic_catalog_v1.json` 是本次新增的人工维护专题层，使用 `领域ID::原始主题名` 做键，与已有 29 方向的主题列表一一对应。
- 17 条链接包含奠基文献、综述、2025 年代表研究，不保证各专题完整或反映截至今天所有最新论文。
- 关联关系仍为编辑性综合判断，需逐边补论文证据，不自动归类为已验证因果关系。
- 后续扩充论文应记录 DOI / 公开地址、作者、年份、是否同行评审、审阅时间、研究问题、局限及关联证据。
- Github Issues 反馈未经核验不能自动写入学术档案，应由管理员审核与标注来源。

### 扩展验证

完整仓库下可以运行 `python tools/validate_topic_catalog_v2.py`，检查专题和跨领域链接是否存在、URL 是否有效格式以及主题 URL 是否发生别名碰撞；此项只检查结构，不保证每篇论文的学术内容正确。

**测试边界：** 已通过静态 JavaScript 语法检查，以及隔离浏览器内的页面交互测试（领域 → 专题、论文、悬浮术语、关联链接、语言切换、首页导航）。尚未在用户正式 GitHub Pages 服务器上做真实部署后的验收。
