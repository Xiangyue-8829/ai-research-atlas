#!/usr/bin/env python3
"""Generate immutable field-ID routes. Run from any working directory.
No external libraries or internet access are required.
"""
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parents[1]
BASE_URL = "https://xiangyue-8829.github.io/ai-research-atlas-preview"
FIELDS = [
    ('A1','统计学习理论','Statistical Learning Theory'),
    ('A2','机器学习优化','Optimization for Machine Learning'),
    ('A3','机器学习范式','Learning Paradigms'),
    ('A4','表示、迁移与持续学习','Representation, Transfer & Continual Learning'),
    ('A5','概率与贝叶斯机器学习','Probabilistic & Bayesian ML'),
    ('A6','因果学习与推断','Causal Learning & Inference'),
    ('B1','深度网络架构','Deep Neural Architectures'),
    ('B2','生成模型','Generative Modeling'),
    ('B3','图与结构化学习','Graph & Structured Learning'),
    ('B4','基础模型','Foundation Models'),
    ('B5','符号与神经符号 AI','Symbolic & Neuro-symbolic AI'),
    ('C1','计算机视觉','Computer Vision'),
    ('C2','自然语言处理','Natural Language Processing'),
    ('C3','语音与音频智能','Speech & Audio Intelligence'),
    ('C4','多模态学习','Multimodal Learning'),
    ('C5','知识发现、检索与推荐','Knowledge Discovery, IR & Recsys'),
    ('C6','时间序列与结构化数据','Time Series & Structured Data'),
    ('D1','推理、搜索与规划','Reasoning, Search & Planning'),
    ('D2','强化学习与控制','Reinforcement Learning & Control'),
    ('D3','智能体与多智能体','AI Agents & Multi-agent Systems'),
    ('D4','机器人与具身智能','Robotics & Embodied AI'),
    ('D5','世界模型与模拟','World Models & Simulation'),
    ('E1','可信、可解释与可靠 AI','Trustworthy, Interpretable & Reliable AI'),
    ('E2','评价、基准与数据中心 AI','Evaluation, Benchmarks & Data-centric AI'),
    ('E3','以人为中心与社会技术 AI','Human-centered & Socio-technical AI'),
    ('F1','高效 AI 与机器学习系统','Efficient AI & ML Systems'),
    ('F2','隐私保护与分布式学习','Privacy-preserving & Distributed Learning'),
    ('G1','科学机器学习与 AI for Science','Scientific ML & AI for Science'),
    ('G2','神经 AI 与认知系统','NeuroAI & Cognitive Systems'),
]


def page(id_, cn, en):
    return f'''<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#081425">
<meta name="description" content="{escape(en,quote=True)} / {escape(cn,quote=True)} — Research fields, open questions, methods and related research in AI Research Atlas.">
<link rel="canonical" href="{BASE_URL}/research/{id_}/">
<link rel="stylesheet" href="../../assets/research-profile.css">
<title>{escape(cn)} · {escape(en)} · AI Research Atlas</title>
<script defer src="../../assets/research-profile.js"></script>
</head>
<body data-domain="{id_}">
<header class="header"><a class="brand" href="../../index.html">◎ AI Research Atlas</a><nav class="nav" aria-label="Site navigation"><a id="home-link" href="../../index.html">全景地图</a><a id="graph-link" class="graph-link" href="../../knowledge-graph.html">知识图谱</a><button id="lang" type="button" aria-label="Switch language">EN</button></nav></header>
<main class="shell">
<div class="breadcrumb"><a class="graph-link" href="../../knowledge-graph.html">AI Research Atlas</a> / <span id="breadcrumb">{id_}</span></div>
<section class="hero"><p id="eyebrow" class="eyebrow">RESEARCH FIELD · {id_}</p><h1 id="title">{escape(cn)}</h1><h2 id="subtitle">{escape(en)}</h2><p id="summary" class="summary">Research overview, questions and connections are loaded from the Atlas's maintained research taxonomy.</p><div class="meta"><span id="profile-layer">{id_[0]}</span><span id="profile-updated">Atlas 2026</span><span>Stable ID: {id_}</span></div></section>
<div class="layout"><div class="main-column"><div id="state-text" role="status" aria-live="polite">正在加载研究档案…</div><div id="field-sections"></div></div>
<aside class="aside"><div class="aside-card"><h3 id="related-label">相关领域</h3><div class="related-links" id="related"></div></div><div class="aside-card"><h3 id="problems-label">跨领域瓶颈</h3><div class="related-links" id="problems"></div></div><div class="aside-card"><p id="relation-caveat" class="notice">领域关联由编辑整理，证据核验正在进行。</p></div></aside></div>
<a id="back" class="back-link graph-link" href="../../knowledge-graph.html">← 返回知识图谱</a>
</main><footer>AI Research Atlas · Editorial research synthesis · Stable research ID {id_}</footer>
<noscript><p style="margin:30px;line-height:1.7">{escape(cn)} ({escape(en)}) is an AI Research Atlas research field. Enable JavaScript to view research questions, relationships and literature maintained in the Atlas data.</p></noscript>
</body></html>
'''


def main():
    for field in FIELDS:
        dest = ROOT / 'research' / field[0] / 'index.html'
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(page(*field), encoding='utf-8')
    print(f'Generated {len(FIELDS)} stable URL pages under {ROOT / "research"}')


if __name__ == '__main__':
    main()
