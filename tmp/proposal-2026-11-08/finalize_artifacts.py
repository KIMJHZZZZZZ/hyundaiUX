from pathlib import Path
from zipfile import ZipFile,ZIP_DEFLATED
import json,math,hashlib,re
from docx import Document
from pypdf import PdfReader
from PIL import Image
from lxml import etree

BASE=Path(r'C:\ssafy\hyundaiUX')
OUT=BASE/'output'/'2026-11-08_말문이트립'
ASSETS=OUT/'assets';QA=OUT/'qa'
RESEARCH=BASE/'research'/'2026-11-08-proposal'
TMP=BASE/'tmp'/'proposal-2026-11-08'
DOC=OUT/'말문이_트립_02_서비스_기획서.docx'
PDF=QA/'proposal-v3.pdf'
ARCHIVE=OUT/'말문이_트립_데모_이미지_자료.zip'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
doc=Document(DOC)
headers=[p.text for p in doc.paragraphs if p.style.name=='Heading 1']
expected=['1 앱 한 줄 소개','2 기획 배경','3 앱 주요 기능 및 차량 특화 요소','4 주요 사용 시나리오','5 개발 계획','6 기대효과 및 발전 가능성']
assert headers==expected,headers
ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main','wp':'http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing','r':'http://schemas.openxmlformats.org/officeDocument/2006/relationships'}
with ZipFile(DOC) as z:
 assert z.testzip() is None
 root=etree.fromstring(z.read('word/document.xml'))
 text=''.join(root.xpath('.//w:t/text()',namespaces=ns))
 figures=root.xpath('.//wp:docPr',namespaces=ns)
 assert len(figures)==33 and all(f.get('descr') for f in figures)
 assert not re.search(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}',text)
 assert '참가 기본정보' not in text and '대표자·팀원 별 동의' not in text
 assert 'pleos.car.permission.STT_SERVICE' in text and 'pleos.car.permission.TTS_SERVICE' in text
 assert 'RouteInfo가 내비 서비스로 전달' in text
 media_hash={hashlib.sha256(z.read(n)).hexdigest() for n in z.namelist() if n.startswith('word/media/')}
 assert sha(ASSETS/'architecture.png') in media_hash
 assert sha(ASSETS/'persona_seoyun.png') in media_hash
 assert sha(ASSETS/'persona_junho.png') in media_hash
 assert len(root.xpath('.//m:oMath',namespaces={'m':'http://schemas.openxmlformats.org/officeDocument/2006/math'}))==4
 for st in ['Heading 1','Heading 2','Heading 3','Title']:
  assert str(doc.styles[st].font.color.rgb)=='000000'
manifest=json.loads((ASSETS/'screen_manifest.json').read_text(encoding='utf-8'))
ids={s['id'] for s in manifest}
assert ids=={f'S{i:02d}' for i in range(1,22)}|{'S04B','S05B','S06B','S13B','S16B'}
assert len(manifest)==26 and not any(s['overflow'] for s in manifest)
for s in manifest:
 for suffix,size in [('.png',(2560,1440)),('_app.png',(1733,1135))]:
  p=ASSETS/(s['file']+suffix)
  with Image.open(p) as im: assert im.size==size,(p,im.size);im.verify()
  if suffix=='_app.png':assert sha(p) in media_hash,p
 for suffix in ['.html','.png','_app.png']:assert (ASSETS/(s['file']+suffix)).is_file()
assert (ASSETS/'index.html').exists() and (ASSETS/'README.md').exists()
forecasts=[]
for name,A,lam,u,a,expected3,expected12 in [('낮음',80,.25,.5,.90,96,138),('기준',275,.50,.6,.95,407,859),('높음',780,.80,.65,.97,1384,3691)]:
 q=1-math.exp(-lam*u)
 mau=lambda t:A*(1+q*sum(a**k for k in range(1,t)))
 assert round(mau(3))==expected3 and round(mau(12))==expected12
 forecasts.append({'scenario':name,'MAU3':round(mau(3)),'MAU12':round(mau(12)),'Mplus1':round(q*a*100,2),'Mplus3':round(q*a**3*100,2),'measured':False})
src=json.loads((TMP/'source-index.json').read_text(encoding='utf-8'))
assert len(src)==len({s['id'] for s in src})==52
assert all(s['url'].startswith('https://') for s in src)
reader=PdfReader(PDF)
assert len(reader.pages)==31
assert len(list(QA.glob('v3-page-*.png')))==31
assert all(len(p.extract_text() or '')>100 for p in reader.pages)
assert DOC.stat().st_mtime<=PDF.stat().st_mtime
sourcecheck=json.loads((QA/'source-current-check.json').read_text(encoding='utf-8'))
assert sourcecheck['page']['sameBody'] and sourcecheck['comments']=={'sameComments':True,'count':4}
reviews=['review-content-v1.md','review-tech-final.md','review-ui-v1.md','review-layout-final.md']
assert all((RESEARCH/f).exists() for f in reviews)
with ZipFile(ARCHIVE,'w',ZIP_DEFLATED,compresslevel=6) as z:
 for f in sorted(ASSETS.rglob('*')):
  if f.is_file():z.write(f,Path('말문이트립_화면자료')/f.relative_to(ASSETS))
with ZipFile(ARCHIVE) as z:
 assert z.testzip() is None
 entries=z.namelist()
 assert sum(n.endswith('_app.png') for n in entries)==26
 assert sum(n.endswith('.png') and '/S' in n and not n.endswith('_app.png') for n in entries)==26
audit={
 'status':'verified','scope':'공식 02 영역 항목 1부터 6','date':'2026-11-08',
 'docx':str(DOC),'docx_sha256':sha(DOC),'docx_bytes':DOC.stat().st_size,
 'image_archive':str(ARCHIVE),'image_archive_sha256':sha(ARCHIVE),'image_archive_bytes':ARCHIVE.stat().st_size,'archive_entries':len(entries),
 'pages':31,'first_level_sections':headers,'figures':33,'ui_states':26,'personas':2,'cited_sources':52,
 'root_visual_inspection_pages':list(range(1,32)),
 'independent_visual_inspection_pages':list(range(1,10))+list(range(23,32)),
 'independent_reviews':[str(RESEARCH/f) for f in reviews],
 'requirements':[
  {'requirement':'Notion 내용과 댓글 확인','evidence':['research/2026-11-08-proposal/notion-snapshot.json','research/2026-11-08-proposal/notion-comments.xml','qa/source-current-check.json'],'result':'본문 동일·댓글 네 건 최종 재확인'},
  {'requirement':'가독성 있는 DOC 기획서 02 항목 1부터 6','evidence':['DOCX six Heading1 values','31 Word-rendered page PNGs','review-layout-final.md'],'result':'31쪽 전부 시각 확인·빈 페이지 없음'},
  {'requirement':'설문부터 종료까지 단계별 화면 자료','evidence':['S01–S21 plus five branch states','screen_manifest.json','52 UI PNGs in ZIP'],'result':'26개 상태·음성 전용/선택형 만남/예외/여행 종료 포함'},
  {'requirement':'실제 근거 기반 배경','evidence':['B01–B06','review-content-v1.md'],'result':'통계 모집단·날짜·한계와 가설 구분'},
  {'requirement':'차량 특화 핵심 조사','evidence':['section3','T05–T07 and T02–T04'],'result':'실제 내비 여정과 안전한 주차 순간을 핵심으로 제시'},
  {'requirement':'페르소나 이미지와 구체적 시나리오','evidence':['persona_seoyun.png','persona_junho.png','DOCX pages6–7'],'result':'가상임을 표시한 두 페르소나와 시간·상황별 행동'},
  {'requirement':'직접 SDK 문서 확인과 상세 개발 범위','evidence':['section5','pleos-sdk.md','aaos-addendum.md','review-tech-final.md'],'result':'권한·API·버전 불일치·실기 미확인·PT 이전 구현 계획 명시'},
  {'requirement':'기존 만남·소개팅 앱 조사','evidence':['8-service matrix','B08–B21','source-demand.json'],'result':'공식 제품 문서 기반 비교와 적용/비적용 판단'},
  {'requirement':'고객·예상 MAU·재방문율·확장 계획','evidence':['section6','forecast-audit.json','research questionnaire and KPI table'],'result':'측정된 배경과 가정 모델 분리·독립 산술 검증'},
  {'requirement':'실제 Pleos 인터페이스 참고와 파일 저장','evidence':['official window PNG and layout SVG','T19–T20','UI full-frame and portrait assets'],'result':'시안과 실기 실행을 구분·원본과 확대본 ZIP 저장'},
  {'requirement':'에이전트의 반복 검수','evidence':reviews,'result':'수요·산술·SDK·개인정보·UI·최종 Word 배치를 여러 단계로 검토'}
 ],
 'forecast_scenarios':forecasts,
 'limits':'실제 이용자 조사·APK 빌드·실물 Pleos 설치·통화 성공·운영 MAU를 달성했다는 주장은 없음. 요청한 결과물은 기획서와 데모 이미지 자료.'
}
(QA/'completion-audit.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({k:audit[k] for k in ['status','pages','ui_states','personas','figures','cited_sources','archive_entries','docx_bytes','image_archive_bytes','docx','image_archive']},ensure_ascii=False))
