# AI Research Atlas · V3.0 Public Experience

**目标：把现有官网升级为专业、可持续更新的科研导航平台，同时始终保留官网地址与既有研究档案路径。**

正式官网：<https://xiangyue-8829.github.io/ai-research-atlas/>
仓库：<https://github.com/Xiangyue-8829/ai-research-atlas>
目标分支：`feature/atlas-v3`（从 `main` 创建）

## 这次已经写好的功能

1. 新版首页 `index.html`：双语旗舰首屏、视觉研究网络、研究数字、交互知识图谱、六个推荐领域和可信研究说明。
2. 全局研究检索：点击导航的搜索按钮或按 `Ctrl+K` / `⌘K`，搜索领域、细分主题和已整理专题。
3. 新版领域目录 `research-index.html`：按 A–G 学术层次过滤、关键词检索、只显示已有整理内容的领域，以及展开全部主题的链接。
4. `about.html`：学科分类与关系的含义、论文证据标准、内容完整性、项目路线图、反馈渠道。
5. `changelog.html`：公开记录版本和计划，不把开发中的功能描述成已上线。
6. SEO：正式官网 canonical、OG 分享元数据、favicon、`robots.txt`、Sitemap 生成与正式域名替换。
7. 原 29 个领域档案与研究专题/社区增量统一配色（由脚本自动注入 CSS，不覆盖正文和原始数据）。
8. 质量检查：站点路径、29 个领域、323 个主题基线、已整理文献键、Sitemap 和内部链接。

**刻意没有做**：论文自动抓取、每日更新、论文语义散点图、独立社区账号。这些属于 V3.2/V4，首页标记为 PLANNED，不伪造功能。

## 你现在怎么部署（推荐 GitHub Desktop）

**全程不在 main 上操作，直到最终 PR 通过。**

### 1. 准备正式仓库

1. 安装 [GitHub Desktop](https://desktop.github.com/) 并登录你的账号。
2. 选择 `File → Clone repository`，克隆 `Xiangyue-8829/ai-research-atlas` 到电脑。例如 `D:\Projects\ai-research-atlas`。
3. `Current Branch → New Branch`，从 `main` 创建 **`feature/atlas-v3`**，确保新分支是当前分支。

### 2. 拷贝 V3 文件

1. 解压 `AI_Research_Atlas_V3_Upgrade.zip`。
2. 把 ZIP 里面的文件和文件夹拷贝到你刚刚克隆的 **仓库根目录**，允许覆盖同名的 `index.html` 和 `research-index.html`，以及新建 `assets/`、`tools/` 和 `.github/workflows/` 下的新文件。
3. **不要删除或覆盖** 原本的 `ai_research_atlas_data_2026.json`、`atlas_en_2026.json`、`research_profiles_2026.json`、`research_profiles_en_2026.json`、`data/topic_catalog_v1.json`、`assets/atlas-kg.js`、`assets/topic.js`、29 个 `research/<ID>/` 文件夹等。
4. 确认 `.bat` 放在仓库根目录、`tools/finish_v3.py` 在 `tools/` 下。

ZIP 是**增量升级包**，不是包含全部研究数据的完整仓库。

### 3. 本地正式化和校验

在 Windows 双击 `PREPARE_V3_WINDOWS.bat`，等待 `SUCCESS`。或在仓库根目录运行：

```powershell
py -3 tools/finish_v3.py
py -3 tools/check_v3.py
```

执行后脚本会：

- 将项目中旧的 `/ai-research-atlas-preview/` 地址替换为正式地址；
- 把 GitHub 社区链接从旧仓库名字更新为正式仓库；
- 调整旧的 29 个研究领域页面的规范网址与视觉样式；
- 修改未来自动生成研究页面的脚本，避免样式更新失效；
- 重新生成只包含正式 URL 的 `sitemap.xml`；
- 生成 `robots.txt`。

脚本不会执行 `git push`，不会删除历史提交，重复执行不会重复插入 CSS。

### 4. 本地预览

在 **仓库根目录** 打开 PowerShell：

```powershell
py -3 -m http.server 8000
```

打开 <http://localhost:8000/>。建议同时检查：

- `http://localhost:8000/`
- `http://localhost:8000/research-index.html`
- `http://localhost:8000/research/A5/`
- `http://localhost:8000/topic.html?domain=A5&slug=gmrf-spde`
- `http://localhost:8000/about.html`
- `http://localhost:8000/changelog.html`
- `http://localhost:8000/community.html`

浏览器按 `F12` 进入设备模拟检查手机版。主页按 `Ctrl+K` 测试快捷搜索。

### 5. 发布到 feature 分支，审查后合并 main

1. GitHub Desktop 查看更改清单，确认**没有删除研究原始 JSON**。
2. Commit message 写 `feat: launch AI Research Atlas V3 public experience`。
3. 点 `Commit to feature/atlas-v3`，然后点 `Push origin`。
4. 在 GitHub 网页打开 `Compare & pull request`，目标为 `main`。确认 Actions 中的 **Validate AI Research Atlas V3** 检查成功。
5. PR 确认后再 `Merge pull request`。GitHub Pages 完成部署后，官网**同一个固定网址**立即使用 V3。

正式网站在第 5 步之前依然使用原来的 `main`，不会因为你编辑 `feature/atlas-v3` 而下线。

## 设计和验证声明

- 本 ZIP 中**没有**人工伪造的真实论文记录或新的自动抓取结果。
- 本轮浏览器截图和交互测试使用与现有 Atlas 相同数据结构的**合成测试数据**（用于 UI 验证），不代表已经在你 GitHub 正式站部署或端到端验证全部真实数据。
- 浏览器测试覆盖：桌面图谱节点、快捷搜索与主题链接、双语切换、领域目录筛选、About 页面、390px 手机宽度和 JavaScript 异常。
- 由于 GitHub 插件写入权限返回 `403 Resource not accessible by integration`，这次没有创建远程分支、提交代码或修改线上 `main`。

## 今后怎么更新且保持地址不变

- 永远保留 `Xiangyue-8829/ai-research-atlas` 仓库名称、`main` 发布设置和 `/research/<ID>/` 等已公开 URL。
- 每次新内容先开 `feature/*` 分支，测试后通过 PR 合并到 main。
- 增加页面时更新 sitemap；重写网站框架时对旧路径提供兼容或重定向。
- 搜索引擎收录需在 [Google Search Console](https://search.google.com/search-console/welcome) 单独验证和提交 `sitemap.xml`，代码配置不保证自动被 Google 收录。
