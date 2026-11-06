from zipfile import ZipFile
from pathlib import Path
from xml.etree import ElementTree as ET
import json

base=Path(__file__).parent
ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
for name in ['root-6.docx','01_통합전략보고서.docx']:
    with ZipFile(base/name) as z:
        media=[i for i in z.namelist() if i.replace('\\','/').startswith('word/media/')]
        parts=[]
        for member in z.namelist():
            normalized=member.replace('\\','/')
            if normalized=='word/document.xml' or normalized.startswith(('word/header','word/footer','word/footnotes','word/endnotes','word/comments')) and normalized.endswith('.xml'):
                root=ET.fromstring(z.read(member))
                paras=[''.join(p.itertext()) if False else ''.join(t.text or '' for t in p.findall('.//w:t',ns)) for p in root.findall('.//w:p',ns)]
                parts.append('PART '+normalized+'\n'+'\n'.join(paras))
        out=base/(name+'.extracted.txt')
        out.write_text('MEDIA COUNT '+str(len(media))+'\n'+json.dumps(media,ensure_ascii=False)+'\n'+'\n'.join(parts),encoding='utf-8')
        print(name, 'media',len(media), 'chars',out.stat().st_size, 'output',str(out))
        for member in media:
            target=base/(name+'.media')/Path(member.replace('\\','/')).name
            target.parent.mkdir(exist_ok=True)
            target.write_bytes(z.read(member))
