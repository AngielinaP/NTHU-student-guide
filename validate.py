from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import json,re,datetime
p=Path(__file__).parent
guides=json.loads((p/'content/guides.json').read_text());slugs=set();numbers=set()
required={'slug','short','title','category','icon','summary','intro','steps','tips','checklist','sources','updated'}
for g in guides:
 assert required <= set(g), 'Missing content field'
 assert re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',g['slug']) and g['slug'] not in slugs
 slugs.add(g['slug']);assert g['icon'] not in numbers;numbers.add(g['icon'])
 assert g['category'] in ['Academics','Campus life','Daily essentials']
 assert 3<=len(g['steps'])<=6 and 2<=len(g['tips'])<=4 and 3<=len(g['checklist'])<=6
 assert all(len(s)==2 and all(s) for s in g['steps'])
 assert g['sources'] and all(len(s)==2 and s[1].startswith('https://') for s in g['sources'])
 datetime.date.fromisoformat(g['updated'])
class Page(HTMLParser):
 def __init__(self):super().__init__();self.links=[];self.ids=set();self.h1=0
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='h1':self.h1+=1
  if 'id' in a:assert a['id'] not in self.ids;self.ids.add(a['id'])
  for key in ['href','src']:
   if a.get(key):self.links.append(a[key])
  if a.get('target')=='_blank':assert 'noopener' in a.get('rel','')
pages={}
for f in (p/'dist').rglob('*.html'):
 parser=Page();parser.feed(f.read_text());assert parser.h1==1;pages[f.resolve()]=parser
for f,parser in pages.items():
 for link in parser.links:
  u=urlsplit(link)
  if u.scheme or u.netloc:continue
  target=(f.parent/unquote(u.path)).resolve() if u.path else f
  assert target.exists(),f'Missing {link} from {f}'
  if u.fragment and target in pages:assert u.fragment in pages[target].ids,f'Missing anchor {link}'
print(f'PASS: {len(guides)} guide schemas; {len(pages)} pages; all local files and anchors; one h1 per page.')
