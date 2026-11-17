# AI Research Atlas — Knowledge Graph & Research Profiles MVP

**发布日期**：2026-11-17（本地交付，不代表线上部署）  
**适用仓库**：`Xiangyue-8829/ai-research-atlas`  
**原站**：https://xiangyue-8829.github.io/ai-research-atlas/

## 做了什么

本补丁**只新增文件**，默认不改原仓库的 `index.html`、既有 JSON、已有研究页面或网站配置：

- `knowledge-graph.html`：互动知识图谱，依托原有 **29 个方向、66 条领域关系、12 个研究瓶颈**；提供双语、关系类型、领域筛选、搜索、缩放、拖动、选中邻域和进入档案链接。
- `research/<ID>/index.html`：29 个固定研究领域 URL，例如 `research/A5/`，即使领域标题变化也不需要更换地址。
- `assets/research-profile.js`：从原有 `ai_research_atlas_data_2026.json`、双语数据、`research_profiles_2026.json` 等动态填充全部 29 个领域页面。**只有 D5、E1、A5 拥有已有的专题试点内容**；对其他领域展示现有概览及研究主题，不假装有完整专题文章。
- `data/knowledge_contract_v1.json`：统一领域、瓶颈、专题、文献和关系 ID 的版本约定。
- `data/relation_evidence_v1.json`：可扩展的逐关系证据登记簿；默认为 `editorial_unverified`，**未完成逐边文献核验**。
- `tools/validate_atlas.py`：验证领域、链接、瓶颈、双语数据和 29 条 URL 的引用完整性。
- `tools/update_sitemap.py`：幂等地向原有 `sitemap.xml` 补充 29 个研究 URL 与 1 个图谱 URL。

## 部署前步骤

1. **在现有仓库新建开发分支**，不要覆盖 `main` 上已有网站。比如：

   ```bash
   git clone https://github.com/Xiangyue-8829/ai-research-atlas.git
   cd ai-research-atlas
   git checkout -b feature/kg-profiles-v1
   ```

2. 解压此补丁 ZIP，**把 ZIP 中的文件和子文件夹合并到仓库根目录**。不要把 ZIP 作为一个单独的顶层文件夹放进仓库。
3. 验证真实数据引用，检查报错后再继续：

   ```bash
   python tools/validate_atlas.py .
   python tools/update_sitemap.py .
   python -m http.server 8000
   ```

4. 浏览器依次检查：
   - `http://localhost:8000/knowledge-graph.html`
   - `http://localhost:8000/research/A5/` — 概率与贝叶斯 ML，包含**摊销 / 模拟推断**专题
   - `http://localhost:8000/research/D5/` — 世界模型专题
   - `http://localhost:8000/research/E1/` — 可信可解释 AI，包含**机制可解释性**专题
   - `http://localhost:8000/research/A1/` — 尚无专题档案，保留原始领域信息
   - 语言切换、搜索、缩放、研究瓶颈模式、图谱与档案双向跳转。

5. 在已有 `index.html` 的适当导航栏中增加一个真实链接，例如：

   ```html
   <a href="./knowledge-graph.html">知识图谱 / Knowledge Graph</a>
   ```

   本补丁**不自动修改既有 113 KB 首页**，避免破坏其当前布局与中英文切换逻辑。请按原站实际导航结构集成，而不是简单往 `<body>` 插入浮层。

6. 验证无误后提交与合并，再由仓库既有 GitHub Pages 发布流程上线：

   ```bash
   git add knowledge-graph.html assets/ data/ research/ tools/ sitemap.xml
   git commit -m "feat: add research knowledge graph and stable field profiles"
   git push --set-upstream origin feature/kg-profiles-v1
   ```

   在 GitHub 开 Pull Request 检查差异，合并后检查 `https://xiangyue-8829.github.io/ai-research-atlas/knowledge-graph.html` 是否真的可以访问。**推送开发分支本身不代表公开站点已更新。**

## 数据约定与学术质量

- 研究方向的唯一 ID 保持原样：`A1` 至 `G2`，不用中文或英文显示名称作为外键。
- 研究瓶颈使用既有 `P1` 至 `P12`。
- 每条已有关系获得基于领域 ID 和关系类型的稳定 ID，形如 `R-A5--G1--intersection`。若将来出现同一对领域存在多条同类型关系，应扩展稳定的人工 ID，而非依赖 JSON 数组序号。
- `research_profiles_2026.json` 中的三个试点研究对象比对应的 **A5/E1/D5 一级领域更窄**。页面将其显示为“专题研究档案”并保留各自局限与证据标签。
- 所有旧领域关系默认 `editorial_unverified`。只有完成证据核验，才应在 `data/relation_evidence_v1.json` 中标记 `source_supported`。
- 现阶段 323 个细分主题显示为标签，**没有**生成 323 个独立主题图节点或研究档案；下一阶段再按需求分层展开。
- 评论系统暂不启用，因为 giscus 需要完成 Github Discussions 配置、版主管理政策与登录体验评估。

## 验收标准

| 测试 | 目标 |
| --- | --- |
| 原始数据 | 29 方向、323 主题、12 瓶颈、66 关系完整读取 |
| 页面覆盖 | `research/<ID>/` 共 29 页均可打开 |
| 试点质量 | D5/E1/A5 专题内容、来源链接与证据类别保留 |
| 交互 | 点击、搜索、筛选、拖拽、缩放与返回双向链接可用 |
| 语言 | 中英展示；缺失英文翻译不伪造内容 |
| 数据校验 | `validate_atlas.py` 检查通过 |
| 兼容性 | 原 `index.html` 和已有页面继续正常运行 |
| 证据质量 | 全部新扩展关系遵循证据状态；不把编辑判断当成经验证据 |

## 下一阶段

1. 用稳定 ID 将 323 个细分主题逐步变成可选择的二级图节点；明确与父研究方向的 `has_topic` 关系。
2. 在 66 条跨领域关联中选高价值的 15–20 条，逐条补论文、定性论证、争议点和最近审查时间。
3. 将 Research Discussion 接到各稳定 URL；新增社区贡献需要人工审核，不能直接自动变成档案内容。
4. 考虑把概览核心内容在构建时预渲染到 HTML，以改善无需 JavaScript 的可读性与搜索引擎抓取（当前 MVP 采用客户端 JSON 填充）。

**注意**：这是可合并补丁，不是线上完成部署的确认。只有在实际仓库合并、构建和浏览器验收后才能称为已上线。
