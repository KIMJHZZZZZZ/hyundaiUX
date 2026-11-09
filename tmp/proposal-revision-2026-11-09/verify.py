from pathlib import Path
from re import fullmatch
from zipfile import ZipFile
from lxml import etree
from docx import Document
from docx.oxml.ns import qn
from pypdf import PdfReader

root=Path('.')
original=root/'말문이 트립! 서비스 기획서-1·2장 개정본.docx'
final=next((root/'output'/'2026-11-09_말문이_트립_통합_개정').glob('*.docx'))
ref='참고 자료'
a,b=Document(original),Document(final)
elements=lambda d:list(d.element.body)
text=lambda e:''.join(e.xpath('.//w:t/text()')).strip()
before,after=elements(a),elements(b)
split_a=next(i for i,e in enumerate(before) if text(e)==ref)
split_b=next(i for i,e in enumerate(after) if text(e)==ref)
serialize=lambda items:[etree.tostring(e,method='c14n') for e in items]
assert serialize(before[:split_a])==serialize(after[:split_a]),'Chapters 1–2 were modified'
assert serialize(before[split_a+1:])==serialize(after[split_b+1:]),'Source list or section definition changed'
new=[text(e) for e in after[split_a:split_b]]
heads=[p.text.strip() for p in b.paragraphs if p.style.name=='Heading 2']
assert [int(h[0]) for h in heads if fullmatch(r'[1-6] .+',h)]==list(range(1,7)),heads
assert len(b.inline_shapes)==len(a.inline_shapes)+1
with ZipFile(original) as z1, ZipFile(final) as z2:
    assert z2.testzip() is None
    for name in z1.namelist():
        if name.startswith('word/media/'):
            assert z1.read(name)==z2.read(name),name
    assert serialize([etree.fromstring(z1.read('word/styles.xml'))])==serialize([etree.fromstring(z2.read('word/styles.xml'))])
assert [round(n*c*(1+r)) for n,c,r in [(600,.10,.12),(1200,.15,.20),(2400,.20,.30)]]==[67,216,624]
for word in ('만남 코드','같이','각자','인스타그램','requestRouteWithWaypoints','5분 이내 연결률','2개월차 예상 MAU'):
    assert word in ' '.join(new),word
q=Path('tmp/proposal-revision-2026-11-09/final-v4')
pages=PdfReader(q/'integrated.pdf').pages
front=PdfReader(q.parent/'front-original.pdf').pages
print('1·2장 원본 본문 XML, 그림 원본, 스타일, 참고표 일치')
print('6개 장 순서, 4장 신규 시안, 사용 규모 67/216/624 산식 확인')
for i,(prev,cur) in enumerate(zip(front[:6],pages[:6]),1):
    assert prev.extract_text()==cur.extract_text(),i
assert len(list(q.glob('page-*.png')))==len(pages)
for i,p in enumerate(pages,1):
    lines=[l.strip() for l in p.extract_text().splitlines() if l.strip()]
    assert len(lines)>=10,(i,lines)
    print(i,len(lines),lines[0], '→', lines[-1])

