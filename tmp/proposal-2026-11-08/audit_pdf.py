from pathlib import Path
import json,sys
from pypdf import PdfReader
from PIL import Image,ImageOps,ImageDraw,ImageFont
ROOT=Path(r'C:\ssafy\hyundaiUX\output\2026-11-08_말문이트립\qa')
version=sys.argv[1] if len(sys.argv)>1 else '1'
r=PdfReader(ROOT/('proposal-v'+version+'.pdf'))
pages=[]
for i,p in enumerate(r.pages):
 t=p.extract_text() or ''
 lines=[x.strip() for x in t.splitlines() if x.strip()]
 compact=''.join(t.split())
 pages.append({'page':i+1,'chars':len(t),'first':lines[:4],'last':lines[-4:],'compact':compact})
 print(i+1,len(t),compact[:80],' ... ',compact[-60:])
(ROOT/('pdf-v'+version+'-audit.json')).write_text(json.dumps(pages,ensure_ascii=False,indent=2),encoding='utf-8')
font=ImageFont.truetype(r'C:\Windows\Fonts\malgun.ttf',22)
files=sorted(ROOT.glob('v'+version+'-page-*.png'))
for start in range(0,len(files),9):
 sheet=Image.new('RGB',(1350,2010),'#e4e9ed');d=ImageDraw.Draw(sheet)
 for j,f in enumerate(files[start:start+9]):
  im=Image.open(f).convert('RGB');im.thumbnail((430,620))
  x=(j%3)*450+10;y=(j//3)*670+35
  sheet.paste(im,(x,y));d.text((x,y-28),f.name,fill='black',font=font)
 sheet.save(ROOT/('contact-v'+version+'-'+str(start//9+1)+'.jpg'),quality=90)
