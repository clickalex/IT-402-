/* IT 402 Study Hub — search, theme, progress (20 chapters), quiz, timer, checklists. */
const pages=[
['Home','index.html','Subject overview, marks table, unit dashboard, progress'],
['Syllabus & Paper Pattern','syllabus.html','2026-27 syllabus, weightage, section A B, sample pattern'],
['Part A · Employability Hub','part-a.html','Communication self-management ICT entrepreneurial green skills overview'],
['U1 · Communication Skills-II','chapters/pa-u1-communication.html','7 Cs cycle sender encoding feedback barriers verbal non-verbal'],
['U2 · Self-Management Skills-II','chapters/pa-u2-self-management.html','SMART goals stress OCEAN time management personality'],
['U3 · ICT Skills-II','chapters/pa-u3-ict.html','operating system files extensions odt ods odb backup antivirus password'],
['U4 · Entrepreneurial Skills-II','chapters/pa-u4-entrepreneurial.html','entrepreneur employee business plan risk myths qualities'],
['U5 · Green Skills-II','chapters/pa-u5-green.html','sustainable development Brundtland green jobs economy environment'],
['Unit 1 · Writer Hub','unit1-writer.html','Styles images ToC templates track changes overview'],
['Ch 1 · Styles','chapters/u1-ch1-styles.html','F11 fill format paragraph character page style new update load'],
['Ch 2 · Images','chapters/u1-ch2-images.html','anchor to page paragraph character wrap contour embed link group'],
['Ch 3 · ToC Templates Track Changes','chapters/u1-ch3-toc-templates-track.html','table of contents ott template comment compare manage index'],
['Unit 2 · Calc Hub','unit2-calc.html','Scenarios goal seek macros linking share review overview'],
['Ch 4 · Scenarios & Goal Seek','chapters/u2-ch4-scenarios-goal-seek.html','consolidate subtotal sort what-if FTV solver variable'],
['Ch 5 · Macros','chapters/u2-ch5-macros.html','record run organise basic function my macros security arguments'],
['Ch 6 · Linking Data','chapters/u2-ch6-linking.html','sheet reference hyperlink Ctrl K relative absolute F4 external data'],
['Ch 7 · Share & Review','chapters/u2-ch7-share-review.html','share shared conflicts record manage merge compare comment'],
['Unit 3 · DBMS Hub','unit3-dbms.html','Base tables relationships queries forms reports overview'],
['Ch 8 · DBMS Intro','chapters/u3-ch8-dbms-intro.html','data information models relational degree cardinality keys RDBMS'],
['Ch 9 · Base Tables','chapters/u3-ch9-base-tables.html','odb datatype wizard design view primary key autovalue sort'],
['Ch 10 · Relationships','chapters/u3-ch10-relationships.html','one-to-many junction referential integrity cascade foreign key'],
['Ch 11 · Queries','chapters/u3-ch11-queries.html','design view criterion wildcard LIKE FATSVC F5 aggregate group'],
['Ch 12 · Forms & Reports','chapters/u3-ch12-forms-reports.html','label textbox button combo wizard grouping title date'],
['Unit 4 · Safety Hub','unit4-safety.html','Health safety security ergonomics emergencies overview'],
['Ch 13 · HSS at Workplace','chapters/u4-ch13-hss.html','hazard physical electrical fire lifting control hierarchy policy'],
['Ch 14 · Quality & Ergonomics','chapters/u4-ch14-quality-ergonomics.html','50-70 eye level 20-20-20 posture air water cleanliness RSI'],
['Ch 15 · Accidents & Emergencies','chapters/u4-ch15-accidents-emergencies.html','fire triangle PASS evacuation lift stairs shock 101 102 108'],
['Question Bank','question-bank.html','MCQ quiz short long answers sample paper timer 50 marks'],
['Practical Lab','practical.html','15 practicals writer calc base project file viva'],
['PYQ Practice','pyq.html','previous year questions SQP marking scheme sample papers trends official'],
['Revision','revision.html','cheat sheet shortcuts paths numbers answer frame exam morning']
];
const $=s=>document.querySelector(s), $$=s=>document.querySelectorAll(s);
const TOTAL=20;
const prefix=()=>location.pathname.includes('/chapters/')?'../':'';
function init(){
  const theme=localStorage.getItem('it402-theme');
  if(theme==='dark')document.body.classList.add('dark');
  $('.theme-btn')?.addEventListener('click',()=>{document.body.classList.toggle('dark');localStorage.setItem('it402-theme',document.body.classList.contains('dark')?'dark':'light')});
  $('.menu-btn')?.addEventListener('click',()=>$('.sidebar')?.classList.toggle('open'));
  const file=location.pathname.split('/').pop()||'index.html';
  $$('.sidebar a').forEach(a=>{const h=a.getAttribute('href');if(h===file||h==='chapters/'+file)a.classList.add('active')});
  const grp=[...$$('.navgroup')].find(d=>d.querySelector('a.active'));
  if(grp)grp.open=true;
  $$('.sidebar a').forEach(a=>a.addEventListener('click',()=>$('.sidebar')?.classList.remove('open')));
  $$('[data-complete]').forEach(box=>{
    const key='complete-'+box.dataset.complete;
    box.checked=localStorage.getItem(key)==='yes';
    box.addEventListener('change',()=>{localStorage.setItem(key,box.checked?'yes':'no');updateProgress()});
  });
  $$('.check input[type=checkbox]').forEach((box,i)=>{
    const key='check-'+file+'-'+i;
    box.checked=localStorage.getItem(key)==='yes';
    box.addEventListener('change',()=>localStorage.setItem(key,box.checked?'yes':'no'));
  });
  updateProgress();setupSearch();setupBackTop();setupQuiz();setupChapterSelection();setupTimer();
}
function allProgress(){
  const all={};
  document.querySelectorAll('[data-complete]').forEach(b=>{all[b.dataset.complete]=b.checked});
  const saved=JSON.parse(localStorage.getItem('it402-progress')||'{}');
  Object.assign(saved,all);
  try{for(let i=0;i<localStorage.length;i++){const k=localStorage.key(i);if(k&&k.startsWith('complete-'))saved[k.slice(9)]=localStorage.getItem(k)==='yes';}}catch(e){}
  localStorage.setItem('it402-progress',JSON.stringify(saved));
  return saved;
}
function updateProgress(){
  const all=allProgress();
  const keys=Object.keys(all), done=keys.filter(k=>all[k]).length;
  const pct=Math.round(done/TOTAL*100);
  $$('[data-progress]').forEach(el=>el.style.width=pct+'%');
  $$('[data-progress-label]').forEach(el=>el.textContent=`${done} of ${TOTAL} chapters marked complete`);
  $$('[data-unit]').forEach(el=>{
    const pre=el.dataset.unit, tot=+el.dataset.total||0;
    const d=keys.filter(k=>k.startsWith(pre)&&all[k]).length;
    const bar=el.querySelector('[data-unit-bar]'), lab=el.querySelector('[data-unit-label]');
    if(bar)bar.style.width=(tot?Math.round(d/tot*100):0)+'%';
    if(lab)lab.textContent=`${d}/${tot} chapters`;
  });
}
function setupSearch(){
  const input=$('#siteSearch'), out=$('#searchResults');
  if(!input)return;
  document.addEventListener('keydown',e=>{
    if(e.key==='/'&&!/input|textarea/i.test(document.activeElement.tagName)){e.preventDefault();input.focus();}
  });
  input.addEventListener('input',()=>{
    const q=input.value.trim().toLowerCase(), px=prefix();
    if(!q){out.style.display='none';return}
    const hits=pages.filter(p=>(p[0]+' '+p[2]).toLowerCase().includes(q)).slice(0,10);
    out.innerHTML=hits.length?hits.map(p=>`<a class="result" href="${px}${p[1]}"><b>${p[0]}</b><br><small>${p[2]}</small></a>`).join(''):'<div class="result">No page found — try “macros”, “viva” or “ergonomics”.</div>';
    out.style.display='block';
  });
  document.addEventListener('click',e=>{if(!e.target.closest('.search'))out.style.display='none'});
}
function setupBackTop(){
  const b=$('.backtop');if(!b)return;
  addEventListener('scroll',()=>b.style.display=scrollY>400?'block':'none');
  b.onclick=()=>scrollTo({top:0,behavior:'smooth'});
}
function refreshQuizScore(box){
  const visible=Array.from(box.querySelectorAll('.quiz-question')).filter(q=>!q.hidden);
  const answered=visible.filter(q=>q.dataset.done);
  const correct=answered.filter(q=>q.dataset.correct==='1');
  box.querySelector('.quiz-score').textContent=`Score: ${correct.length}/${answered.length} answered (of ${visible.length} shown)`;
}
function setupQuiz(){
  $$('.quiz').forEach(box=>{
    refreshQuizScore(box);
    box.querySelectorAll('.quiz-question').forEach(q=>q.querySelectorAll('input').forEach(inp=>inp.addEventListener('change',()=>{
      if(q.dataset.done)return;
      q.dataset.done='1';
      q.dataset.correct=inp.value===q.dataset.answer?'1':'0';
      const fb=q.querySelector('.feedback');
      fb.setAttribute('role','status');
      fb.textContent=q.dataset.correct==='1'?'✓ Correct':'✗ Correct answer: '+q.dataset.answer;
      fb.style.color=q.dataset.correct==='1'?'#15803d':'#dc2626';
      q.querySelectorAll('input').forEach(input=>input.disabled=true);
      refreshQuizScore(box);
    })));
  });
}
function setupChapterSelection(){
  const select=$('#chapter-select');
  if(!select)return;
  const apply=()=>{
    const chapter=select.value;
    const items=$$('[data-chapter]');
    items.forEach(item=>item.hidden=chapter!=='all'&&item.dataset.chapter!==chapter);
    $$('.quiz').forEach(box=>{
      box.hidden=!Array.from(box.querySelectorAll('.quiz-question')).some(q=>!q.hidden);
      refreshQuizScore(box);
    });
    const shown=items.filter(item=>!item.hidden);
    const mcqs=shown.filter(item=>item.classList.contains('quiz-question')).length;
    $('#chapter-status').textContent=`${mcqs} MCQs and ${shown.length-mcqs} written questions shown. Answers are kept while switching chapters.`;
    $('#chapter-links').hidden=chapter==='all';
    const option=select.selectedOptions[0];
    if(chapter!=='all'){
      $('#chapter-notes').href=option.dataset.notes;
      $('#chapter-pyq').href='pyq.html#'+option.dataset.pyq;
    }
    const url=new URL(location.href);
    if(chapter==='all')url.searchParams.delete('chapter');
    else url.searchParams.set('chapter',chapter);
    history.replaceState(null,'',url);
  };
  const initial=new URLSearchParams(location.search).get('chapter');
  if(Array.from(select.options).some(o=>o.value===initial))select.value=initial;
  select.addEventListener('change',apply);
  apply();
}
function setupTimer(){
  const display=$('.timer-display');if(!display)return;
  let seconds=7200,interval=null;
  const show=()=>{display.textContent=String(Math.floor(seconds/3600)).padStart(2,'0')+':'+String(Math.floor(seconds%3600/60)).padStart(2,'0')+':'+String(seconds%60).padStart(2,'0')};
  show();
  $('#startTimer')?.addEventListener('click',()=>{if(interval)return;interval=setInterval(()=>{if(seconds>0){seconds--;show()}else clearInterval(interval)},1000)});
  $('#pauseTimer')?.addEventListener('click',()=>{clearInterval(interval);interval=null});
  $('#resetTimer')?.addEventListener('click',()=>{clearInterval(interval);interval=null;seconds=7200;show()});
}
document.addEventListener('DOMContentLoaded',init);
