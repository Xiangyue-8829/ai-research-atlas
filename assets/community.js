/* Public research community for AI Research Atlas.
   Read public issues using GitHub REST; user-submitted content is sent to GitHub
   only after the user deliberately opens the prefilled issue composer. */
(() => {
  'use strict';
  const FALLBACK_REPO='Xiangyue-8829/ai-research-atlas';
  const params=new URLSearchParams(location.search);
  const state={lang:params.get('lang')==='en'?'en':'zh',repo:FALLBACK_REPO,issues:[],domain:params.get('domain')||'',topic:params.get('topic')||'',loaded:false,apiError:false,atlas:null};
  const categories=[
    {id:'research-question',zh:'研究问题',en:'Research Question',prefix:'Research Question'},
    {id:'paper-recommendation',zh:'论文推荐',en:'Paper Recommendation',prefix:'Paper Recommendation'},
    {id:'methodological-critique',zh:'方法批评',en:'Methodological Critique',prefix:'Methodological Critique'},
    {id:'cross-field-connection',zh:'跨领域联系',en:'Cross-field Connection',prefix:'Cross-field Connection'},
    {id:'correction',zh:'纠错与补充',en:'Correction / Supplement',prefix:'Correction'}
  ];
  const strings={
    zh:{graph:'知识图谱',library:'研究档案',community:'研究社区',title:'研究社区',intro:'围绕值得研究的问题展开有依据的讨论：提出研究想法、推荐论文、质疑方法假设，并连接不同 AI 研究领域。',note:'当前讨论由 GitHub Issues 承载。阅读无需登录，发帖与回复需要 GitHub 账号；所有讨论内容公开。',feed:'最近讨论',all:'在 GitHub 查看所有讨论 ↗',filter:'按类型筛选',allTypes:'全部研究讨论',compose:'发起研究讨论',type:'讨论类型',titleLabel:'主题标题',titlePlaceholder:'例如：INLA-SPDE 如何用于在线推断？',body:'研究问题或观点',bodyPlaceholder:'研究背景、具体问题、拟议方法、现有证据与局限…',source:'参考论文 DOI / URL（可选）',evidence:'证据性质',hypothesis:'探索性假设 / 想法',literature:'引用文献的研究主张',question:'尚待验证的问题',submit:'前往 GitHub 完成发布 ↗',hint:'本站不会直接保存表单内容。点击后会打开 GitHub 的公开议题编辑页，你可以检查并决定是否正式提交。',rules:'学术交流原则',rulesList:['陈述研究主张时尽量提供原始文献或 DOI。','区分事实、研究假设与个人判断。','批评方法而非人；禁止骚扰与垃圾信息。','未经审查的社区讨论不自动写入正式档案。'],next:'研究档案与讨论如何连接？',nextDesc:'从任一研究领域或细分专题进入这里时，系统会自动携带对应主题，方便讨论聚焦到具体问题。正式研究档案仍由维护者核验后更新。',loading:'正在载入 GitHub 公开讨论…',empty:'暂时没有该类型的公开研究讨论。你可以发布第一条。',error:'当前无法从 GitHub 加载讨论列表，可能是网络限制或 API 频率限制；仍可直接前往 GitHub 查看和发帖。',context:'当前讨论主题',comments:'条回复',updated:'更新',footer:'社区讨论公开可见，不能直接作为已核验学术结论。',invalid:'请填写讨论标题和研究问题后继续。',formTitle:'研究讨论'},
    en:{graph:'Knowledge Graph',library:'Research Library',community:'Research Community',title:'Research Community',intro:'Discuss research questions with evidence: propose new ideas, recommend papers, critique assumptions and connect AI research fields.',note:'The current forum is hosted on GitHub Issues. Reading does not require signing in; posting and replying require a GitHub account. All discussions are public.',feed:'Recent discussions',all:'All discussions on GitHub ↗',filter:'Filter by type',allTypes:'All research discussions',compose:'Start a research discussion',type:'Contribution type',titleLabel:'Discussion title',titlePlaceholder:'For example: Can INLA-SPDE support online inference?',body:'Research question or argument',bodyPlaceholder:'Background, specific question, proposed methodology, available evidence and limitations…',source:'Reference DOI / URL (optional)',evidence:'Evidence status',hypothesis:'Exploratory hypothesis / idea',literature:'Literature-supported claim',question:'Open question',submit:'Continue on GitHub to publish ↗',hint:'This site does not save the form directly. Clicking opens a public GitHub issue editor where you can review and decide whether to publish.',rules:'Scholarly discussion principles',rulesList:['Whenever possible, support research claims with source papers or DOIs.','Separate established facts, hypotheses and personal interpretations.','Critique methods, not people; no harassment or spam.','Unreviewed discussions do not automatically become formal Atlas content.'],next:'How do dossiers connect to discussions?',nextDesc:'When visiting from a field or topic dossier, this page preserves the topic context. Research dossier edits remain subject to editorial review.',loading:'Loading public GitHub discussions…',empty:'No public discussions of this type yet. You can start one.',error:'GitHub discussion data is temporarily unavailable (network or API limit). You can still open GitHub directly to browse or post.',context:'Current research context',comments:'replies',updated:'updated',footer:'Public discussion is not automatically verified evidence.',invalid:'Provide a title and a substantive research question before continuing.',formTitle:'Research discussion'}
  };
  const $=id=>document.getElementById(id);
  const msg=k=>strings[state.lang][k];
  const category=id=>categories.find(x=>x.id===id)||categories[0];
  const githubBase=()=>`https://github.com/${state.repo}/issues`;
  const plain=(v,max=300)=>String(v||'').replace(/<[^>]+>/g,'').replace(/[`*_~#>\[\]()]/g,' ').replace(/\s+/g,' ').slice(0,max);
  const aNode=(title,url,cls)=>{const a=document.createElement('a');a.textContent=title;a.href=url;a.className=cls||'';a.target='_blank';a.rel='noopener noreferrer';return a;};
  const titleCategory=title=>categories.find(x=>title.startsWith(`[${x.prefix}]`))||null;
  function translate(){
    document.documentElement.lang=state.lang==='zh'?'zh-CN':'en';
    $('lang').textContent=state.lang==='zh'?'EN':'中文';
    $('nav-graph').textContent=msg('graph');$('nav-graph').href='./index.html?lang='+state.lang;
    $('nav-library').textContent=msg('library');$('nav-library').href='./research-index.html?lang='+state.lang;
    $('nav-community').textContent=msg('community');
    $('page-title').textContent=msg('title');$('page-intro').textContent=msg('intro');$('platform-note').textContent=msg('note');
    $('feed-heading').textContent=msg('feed');$('all-threads').textContent=msg('all');
    $('filter-label').textContent=msg('filter');$('compose-heading').textContent=msg('compose');
    $('type-label').textContent=msg('type');$('title-label').textContent=msg('titleLabel');$('body-label').textContent=msg('body');
    $('source-label').textContent=msg('source');$('evidence-label').textContent=msg('evidence');$('submit').textContent=msg('submit');
    $('discussion-title').placeholder=msg('titlePlaceholder');$('discussion-body').placeholder=msg('bodyPlaceholder');$('compose-hint').textContent=msg('hint');
    $('rules-heading').textContent=msg('rules');$('rules').replaceChildren(...msg('rulesList').map(s=>{const li=document.createElement('li');li.textContent=s;return li;}));
    $('next-heading').textContent=msg('next');$('next-description').textContent=msg('nextDesc');$('footer-note').textContent=msg('footer');
    const typeSel=$('contribution-type'), filterSel=$('filter');
    const selectedType=typeSel.value,selectedFilter=filterSel.value;
    for(const sel of [typeSel,filterSel]){
      sel.replaceChildren();
      if(sel===filterSel){const opt=new Option(msg('allTypes'),'all');sel.append(opt);}
      categories.forEach(c=>sel.append(new Option(state.lang==='zh'?c.zh:c.en,c.id)));
      sel.value=sel===typeSel?selectedType:selectedFilter;
    }
    const es=$('evidence-status'), old=es.value;
    es.replaceChildren(new Option(msg('hypothesis'),'hypothesis'),new Option(msg('literature'),'literature'),new Option(msg('question'),'question'));es.value=old||'hypothesis';
    $('all-threads').href=githubBase();renderContext();renderFeed();
  }
  function renderContext(){
    const host=$('context');host.hidden=true;host.textContent='';
    if(!state.domain||!state.atlas?.domains)return;
    const d=state.atlas.domains.find(d=>d.id===state.domain);if(!d)return;
    const name=state.lang==='zh'?d.zh:d.en;
    let context=`${msg('context')}：${d.id} · ${name}`;
    if(state.topic && d.topics.includes(state.topic))context+=' / '+state.topic;
    host.textContent=context;host.hidden=false;
  }
  function renderFeed(){
    const host=$('thread-feed');host.replaceChildren();
    if(!state.loaded){const n=document.createElement('div');n.className='empty-state';n.textContent=msg('loading');host.append(n);return;}
    if(state.apiError){const n=document.createElement('div');n.className='empty-state';n.textContent=msg('error');n.append(document.createTextNode(' '),aNode(msg('all'),githubBase()));host.append(n);return;}
    const filter=$('filter').value;
    const items=state.issues.filter(issue=>{const cat=titleCategory(issue.title);return cat && (filter==='all'||cat.id===filter);});
    if(!items.length){const n=document.createElement('div');n.className='empty-state';n.textContent=msg('empty');host.append(n);return;}
    for(const issue of items.slice(0,25)){
      const card=document.createElement('article');card.className='thread-card';
      const tag=document.createElement('div');tag.className='thread-type';const c=titleCategory(issue.title);tag.textContent=state.lang==='zh'?c.zh:c.en;card.append(tag);
      const url=new URL(issue.html_url);if(url.hostname!=='github.com')continue;
      card.append(aNode(issue.title,url.href));
      const date=new Date(issue.updated_at), meta=document.createElement('div');meta.className='thread-meta';meta.textContent=`@${issue.user?.login||'GitHub'} · ${Number(issue.comments)||0} ${msg('comments')} · ${msg('updated')} ${date.toLocaleDateString(state.lang==='zh'?'zh-CN':'en-GB')}`;card.append(meta);
      if(issue.body){const preview=document.createElement('p');preview.textContent=plain(issue.body);card.append(preview);}
      host.append(card);
    }
  }
  function issueLink(){
    const type=$('contribution-type').value,c=category(type);
    const raw=$('discussion-title').value.trim(),title=raw.slice(0,150);
    const desc=$('discussion-body').value.trim();const source=$('discussion-source').value.trim();
    const status=$('evidence-status').value;
    const field=state.atlas?.domains?.find(d=>d.id===state.domain);
    const topic=field?.topics?.includes(state.topic)?state.topic:'';
    const context=[field?`${field.id} · ${field.en}`:'General AI research',topic].filter(Boolean).join(' / ');
    const prefix=`[${c.prefix}]`;
    const body=`## Research context\n${context}\n\n## Contribution\n${desc}\n\n## Source / DOI\n${source||'Not yet provided'}\n\n## Evidence status\n${status}\n\n## Notes on limitations or unresolved assumptions\nPlease specify where applicable.\n\n---\nSubmitted via AI Research Atlas Research Community; this is a public discussion, not a verified Atlas finding.`;
    const label=field?field.id:'';
    const ghTitle=`${prefix} ${label?label+' · ':''}${title}`;
    return githubBase()+'/new?'+new URLSearchParams({title:ghTitle,body}).toString();
  }
  async function load(){
    try{const [conf,atlas]=await Promise.all([
      fetch('./data/community_config_v1.json').then(r=>r.ok?r.json():null).catch(()=>null),
      fetch('./ai_research_atlas_data_2026.json').then(r=>r.ok?r.json():null).catch(()=>null)]);
      if(conf && /^[A-Za-z0-9_.-]+\/[A-Za-z0-9_.-]+$/.test(conf.repository))state.repo=conf.repository;
      state.atlas=atlas;renderContext();$('all-threads').href=githubBase();
      const r=await fetch(`https://api.github.com/repos/${state.repo}/issues?state=open&sort=updated&direction=desc&per_page=75`,{headers:{Accept:'application/vnd.github+json'}});
      if(!r.ok)throw Error('GitHub API '+r.status);
      const issues=await r.json();if(!Array.isArray(issues))throw Error('Unexpected issues response');
      state.issues=issues.filter(x=>!x.pull_request);state.apiError=false;
    }catch(e){state.apiError=true;console.warn('Community feed unavailable:',e);}
    state.loaded=true;renderFeed();
  }
  $('lang').addEventListener('click',()=>{state.lang=state.lang==='zh'?'en':'zh';const p=new URLSearchParams(location.search);p.set('lang',state.lang);history.replaceState(null,'',location.pathname+'?'+p.toString());translate();});
  $('filter').addEventListener('change',renderFeed);
  $('discussion-form').addEventListener('submit',e=>{e.preventDefault();if(!$('discussion-title').value.trim()||!$('discussion-body').value.trim()){alert(msg('invalid'));return;}window.location.assign(issueLink());});
  translate();load();
})();
