'use strict';
let category = 'All guides';
const search = document.querySelector('#search');
function filterGuides() {
 const query = (search?.value || '').trim().toLowerCase();
 let count = 0;
 document.querySelectorAll('.guide-card').forEach(card => {
  const show = (category === 'All guides' || card.dataset.category === category) && card.dataset.search.toLowerCase().includes(query);
  card.hidden = !show; if(show) count++;
 });
 const empty = document.querySelector('#empty'); if(empty) empty.hidden = count !== 0;
 const status = document.querySelector('#result-count'); if(status) status.textContent = `${count} guide${count === 1 ? '' : 's'} found`;
}
document.querySelectorAll('[data-filter]').forEach(button => button.addEventListener('click', () => {
 category = button.dataset.filter;
 document.querySelectorAll('[data-filter]').forEach(b => b.setAttribute('aria-pressed', String(b === button)));
 filterGuides();
}));
search?.addEventListener('input', filterGuides);
const boxes = [...document.querySelectorAll('[data-save]')];
function updateProgress(){
 const first = boxes.filter(b => b.dataset.save.startsWith('first-week-'));
 const count = first.filter(b => b.checked).length;
 const progress = document.querySelector('#progress');
 if(progress){progress.value=count; progress.textContent=`${count} of ${first.length}`;document.querySelector('#progress-text').textContent=`${count} of ${first.length} complete`;}
}
function saveBox(box){try{localStorage.setItem('nthu-fieldnotes-v1:'+box.dataset.save,String(box.checked));}catch{const s=document.querySelector('#save-status');if(s)s.textContent=' Storage unavailable; checks last for this visit only.';}}
boxes.forEach(box=>{try{box.checked=localStorage.getItem('nthu-fieldnotes-v1:'+box.dataset.save)==='true';}catch{}box.addEventListener('change',()=>{saveBox(box);updateProgress();});});
document.querySelector('#reset-checklist')?.addEventListener('click',()=>{boxes.filter(b=>b.dataset.save.startsWith('first-week-')).forEach(box=>{box.checked=false;saveBox(box);});updateProgress();});
updateProgress();
