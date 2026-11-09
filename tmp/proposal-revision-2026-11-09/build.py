from pathlib import Path
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor
from PIL import Image, ImageDraw, ImageFont

root = Path.cwd()
qa = root / 'tmp' / 'proposal-revision-2026-11-09'
qa.mkdir(parents=True, exist_ok=True)
out = root / 'output' / '2026-11-09_말문이_트립_통합_개정'
out.mkdir(parents=True, exist_ok=True)
destination = out / '말문이_트립_서비스_기획서_통합_개정본.docx'
doc = Document(root / '말문이 트립! 서비스 기획서-1·2장 개정본.docx')
reference = next(p for p in doc.paragraphs if p.text.strip() == '참고 자료')
reference.paragraph_format.page_break_before = True

def move(element):
    reference._p.addprevious(element)

def paragraph(text, style=None, *, page=False, keep=False):
    p = doc.add_paragraph(text, style=style)
    if style is None:
        p.paragraph_format.line_spacing = 1.06
        p.paragraph_format.space_after = Pt(6)
    elif style == 'Heading 3':
        p.paragraph_format.space_before = Pt(9)
        p.paragraph_format.space_after = Pt(3)
    if page:
        p.paragraph_format.page_break_before = True
    if keep:
        p.paragraph_format.keep_with_next = True
    move(p._p)
    return p

def chapter(text):
    paragraph(text, 'Heading 2', page=True)

def sub(text, *, page=False):
    paragraph(text, 'Heading 3', page=page)

def caption(text):
    p = paragraph(text)
    p.paragraph_format.space_after = Pt(5)
    p.paragraph_format.space_before = Pt(1)
    for run in p.runs:
        run.font.size = Pt(9)
        run.font.color.rgb = RGBColor.from_string('465364')

def table(headers, widths, rows):
    t = doc.add_table(rows=1, cols=len(headers))
    t.style = doc.tables[0].style
    t.autofit = False
    for col, width in zip(t.columns, widths):
        col.width = Inches(width)
    for i, values in enumerate([headers, *rows]):
        row = t.rows[0] if i == 0 else t.add_row()
        trpr = row._tr.get_or_add_trPr()
        trpr.append(OxmlElement('w:cantSplit'))
        if i == 0:
            trpr.append(OxmlElement('w:tblHeader'))
        for j, (cell, width, value) in enumerate(zip(row.cells, widths, values)):
            cell.width = Inches(width)
            cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
            tcpr = cell._tc.get_or_add_tcPr()
            shd = OxmlElement('w:shd')
            shd.set(qn('w:fill'), 'EAF0F7' if i == 0 else 'F6F8FB' if i % 2 == 0 else 'FFFFFF')
            tcpr.append(shd)
            p = cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(3)
            p.paragraph_format.space_after = Pt(3)
            p.paragraph_format.line_spacing = 1.02
            if i == 0:
                p.paragraph_format.keep_with_next = True
            r = p.add_run(value)
            r.font.size = Pt(10.5)
            r.bold = i == 0 or j == 0
    move(t._tbl)
    return t

def make_choice_preview():
    img = Image.new('RGB', (1580, 490), '#101926')
    draw = ImageDraw.Draw(img)
    regular = 'C:/Windows/Fonts/NotoSansKR-Regular.ttf'
    bold = 'C:/Windows/Fonts/NotoSansKR-Bold.ttf'

    def label(x, y, value, size, fill='#F4F8FD', weight=False):
        draw.text((x, y), value, font=ImageFont.truetype(bold if weight else regular, size), fill=fill, anchor='lt')

    def rect(box, color, radius=20, outline=None):
        draw.rounded_rectangle(box, radius=radius, fill=color, outline=outline, width=2)

    for x in (28, 804):
        rect((x, 24, x + 748, 466), '#192638', 25)
        rect((x+32, 52, x+74, 89), '#294D55', 12)
        label(x+45, 59, 'P', 23, '#AAF4D9', True)
    label(118, 57, '04  동행 결정', 24, '#B4C9DF', True)
    label(894, 57, '05  정보 공개', 24, '#B4C9DF', True)

    x = 28
    label(x+32, 117, '남은 여행을 함께할까요?', 44, weight=True)
    label(x+32, 187, '귤빛드라이버 · 협재에서 만남', 29, '#C5D5E5')
    rect((x+32, 248, x+363, 330), '#25384E', outline='#65819A')
    rect((x+385, 248, x+716, 330), '#25384E', outline='#65819A')
    label(x+169, 271, '같이', 34, weight=True)
    label(x+522, 271, '각자', 34, weight=True)
    label(x+32, 368, '서로 ‘같이’를 선택하면 동행이 확정돼요.', 27, '#B4C9DF')
    x = 804
    label(x+32, 117, '무엇을 공유할까요?', 44, weight=True)
    label(x+32, 187, '동행 확정 · 선택한 정보만 상대에게 보여요.', 27, '#C5D5E5')
    rect((x+34, 250, x+63, 279), '#91E4C7', 6)
    draw.line([(x+40, 263), (x+47, 271), (x+58, 257)], fill='#17342C', width=4, joint='curve')
    label(x+80, 246, '인스타그램', 29)
    rect((x+397, 250, x+426, 279), '#192638', 6, '#9DB7D1')
    label(x+443, 246, '전화번호', 29)
    rect((x+32, 332, x+366, 409), '#91E4C7')
    rect((x+385, 332, x+716, 409), '#25384E', outline='#65819A')
    label(x+108, 355, '선택 정보 공유', 30, '#16332C', True)
    label(x+460, 355, '공유 없이 계속', 30, weight=True)
    path = qa / 'choice-preview.png'
    img.save(path)
    return path

chapter('3 앱 주요 기능 및 차량 특화 요소')
sub('지금 함께할 수 있는 여행자를 연결합니다')
paragraph('앱을 열면 이번 여행용 닉네임과 대화 가능 시간, 노을·카페·사진 같은 관심사를 고릅니다. 말만 나누고 싶다면 ‘대화만’, 잠깐 만날 가능성도 열어 두고 싶다면 ‘만남도 열어두기’를 선택합니다. 앱은 넓은 여행 권역과 방향, 겹치는 시간대를 기준으로 후보를 찾고 두 사람이 수락하면 음성을 연결합니다. AI 에이전트는 공통 관심사에서 첫 질문을 꺼내고, 이어지는 대화는 두 여행자가 나눕니다.')
table(('사용자가 고르는 순간', '앱이 해 주는 일'), (1.65, 4.85), [
    ('잠깐 만나기', '두 사람 모두 만남 가능성을 열어 둔 대화에서 제안할 수 있습니다. 둘 다 만나고 싶다고 답하면 공개 장소와 시간을 추천하고, 같은 제안을 수락한 뒤 각자 내비에 경유지를 추가합니다.'),
    ('같이 또는 각자', '만남 뒤 각자 한 번 선택합니다. 두 사람 모두 ‘같이’를 고르면 동행을 확정합니다. 그 외에는 서로의 선택이나 이유를 알려 주지 않고 각자의 여행으로 돌아갑니다.'),
    ('공유할 정보', '동행이 확정되면 인스타그램·전화번호를 항목별로 고릅니다. 기본은 비공개이며 ‘공유 없이 계속’도 선택할 수 있습니다.'),
])
sub('Pleos에서는 대화와 내비 여정이 이어집니다')
paragraph('주차(P) 상태에서 앱을 열면 본인 동의하에 내비 여정을 넓은 권역과 시간대로 바꿔 매칭에 씁니다. 이용자가 직접 권역을 고를 수도 있습니다. 약속이 잡히면 합의한 장소만 본인 내비에 추가해 기존 목적지를 향한 여정을 이어갑니다. 주행을 시작하면 대화와 선택 화면을 닫고, 경로가 바뀌면 다음 주차 때 약속을 다시 확인합니다.')
sub('언제든 각자의 여행으로 돌아갈 수 있습니다')
paragraph('상대에게는 여행용 닉네임·공통 관심사·넓은 권역만 보여 줍니다. 정확한 위치, 최종 목적지, 실명·사진·차량번호는 상대에게 전달하는 정보에서 제외합니다. 두 사람이 합의한 공개 장소와 시각은 약속 카드에 표시합니다. 대화와 만남은 언제든 끝낼 수 있고, 불편한 상대는 종료 후에도 차단하거나 신고할 수 있습니다.')

chapter('4 주요 사용 시나리오')
paragraph('제주 여행 둘째 날, 서윤은 애월 카페에 차를 세웁니다. 노을을 보러 출발하기까지 한 시간이 남았습니다. 오늘 본 풍경을 누군가와 이야기하고 싶어 Pleos에서 말문이 트립!을 엽니다.')
sub('16:40 애월에서 말을 틉니다')
paragraph('서윤은 ‘사진·노을’, ‘20분’, ‘만남도 열어두기’를 고릅니다. 제주 서부에서 주차 중인 ‘귤빛드라이버’도 연결을 수락합니다. AI가 “오늘 노을은 어디서 보세요?”라고 묻자 두 사람은 오늘 찍은 사진 이야기를 시작합니다. 대화하다 보니 둘 다 협재에서 노을을 보고 싶다는 걸 알게 됩니다.')
sub('17:10 각자의 차로 협재에 갑니다')
paragraph('두 사람 모두 ‘잠깐 만나기’를 눌러 18:00 협재 해변 카페 제안을 받습니다. 같은 장소와 시간을 확인한 뒤 각자 ‘내비에 추가’를 눌러 출발합니다. 이동 중에는 내비 안내를 따르고, 18:00 카페에서 차에서 내리기 전에 확인한 일회용 만남 코드를 맞춰 봅니다.')
sub('18:30 만남을 마치고 다음 여행을 고릅니다')
paragraph('노을 사진 이야기를 마치고 각자 주차된 차로 돌아와 ‘같이’와 ‘각자’ 중 하나를 고릅니다. 둘 다 ‘같이’를 고르자 동행이 확정됩니다. 서윤은 인스타그램만 공유하고, 다음 날 새벽 두 사람은 새별오름에서 다시 만납니다.')
pic = doc.add_paragraph()
pic.alignment = WD_ALIGN_PARAGRAPH.CENTER
pic.paragraph_format.keep_with_next = True
pic.paragraph_format.space_after = Pt(2)
shape = pic.add_run().add_picture(str(make_choice_preview()), width=Inches(6.5))
shape._inline.docPr.set('descr', 'Pleos 앱 창의 두 화면. 왼쪽은 같이와 각자 버튼을 보여 주는 동행 결정, 오른쪽은 인스타그램만 선택한 동행 확정 후 정보 공개 화면.')
move(pic._p)
caption('그림 2. 만남 후 동행 결정과 항목별 정보 공개 화면 시안. 1장 그림 1의 이후 단계입니다.')
paragraph('한 사람이 대화만 원하면 두 사람은 인사를 나누고 출발합니다. 만남을 취소하면 약속 카드를 닫습니다. 만남 뒤 ‘각자’를 고르거나 응답 시간이 지나면 “각자의 여행을 이어가세요”로 마무리하고 정보는 비공개로 유지합니다.')

chapter('5 개발 계획')
paragraph('첫 시연은 클라이언트 두 대에서 익명 음성 연결, 공개 장소 합의, 내비 경유지 추가, 동행 결정, 항목별 공개까지 한 번에 보여 주는 것을 목표로 합니다. 같은 빌드에서 주행 전환과 한쪽의 거절도 확인합니다.')
sub('차량 앱과 서버의 역할을 나눕니다')
table(('개발 범위', '구현 계획'), (1.32, 5.18), [
    ('주차 상태', 'Pleos Connect용 Android 앱을 Kotlin으로 구현합니다. AAOS 기어(P)와 CarUxRestrictions를 함께 확인합니다. 주차가 해제되거나 차량 상태를 읽을 수 없으면 화면 입력과 마이크 캡처·송신·재생을 중단합니다.'),
    ('내비 연동', 'NaviHelper의 목적지·여정 변경 이벤트로 추천을 갱신합니다. 양쪽의 장소·시각 수락과 본인 확인 뒤 requestRouteWithWaypoints를 호출합니다. 성공 응답을 받아야 경유지 반영을 표시하고, 이용 거부나 호출 오류 때는 장소명과 시간을 확인해 직접 설정할 수 있게 합니다.'),
    ('매칭과 음성', '서버는 권역·여행 방향·시간대·관심사로 후보를 찾고, 수락한 두 사람에게 만료 시간이 있는 음성방 토큰을 발급합니다. WebRTC와 TURN 릴레이를 적용하고, 실기에서 마이크 권한·오디오 포커스·연결 중단을 확인합니다.'),
    ('AI 에이전트', '관심사와 넓은 권역을 입력으로 받아 첫 질문을 제안합니다. AI 서비스 지연 시 준비된 질문으로 시작합니다. 장소 합의와 동행 결정은 두 사용자의 버튼 입력으로만 확정합니다.'),
    ('동행과 공개', '약속이 확정되면 서버가 만남 시간에만 쓸 수 있는 코드를 발급합니다. 같은 약속에 대한 양쪽의 ‘같이’ 응답을 확인한 뒤에만 공개 기능을 엽니다. 발신자가 확인한 항목만 해당 상대에게 전달합니다.'),
])
sub('첫 빌드에 필요한 연동부터 확인합니다')
paragraph('장비에서 주차 신호·내비 권한·오디오 경로를 먼저 확인하고 사용할 SDK 버전을 고정합니다. 실시간 대화 원음과 전문은 저장하지 않고, AI에는 선택한 관심사와 권역만 전달합니다. Gleo 음성 진입은 핵심 흐름이 완성된 뒤 권한과 호환성을 확인해 추가합니다.')

sub('시안에서 두 사람의 실기 시연까지', page=True)
table(('목표 기간', '만들 것', '확인할 장면'), (1.28, 2.18, 3.04), [
    ('11/9~11/15', '시나리오 시안과 장비 검증', '주차 상태를 읽고 마이크·스피커와 내비 호출을 시험합니다. 화면 시안으로 대화에서 정보 공개까지 이어지는 흐름을 확인합니다.'),
    ('11/16~11/22', '두 사용자 연결과 주차 잠금', '두 사용자가 서로 수락해 통화합니다. 주차 해제·오디오 포커스 상실·연결 끊김 때 음성 송수신을 멈춥니다.'),
    ('11/23~11/30', '약속·경유지·동행 결정·공개', '장소와 시각을 함께 수락해 각자 경유지를 설정합니다. 만남 코드와 ‘같이/각자’ 선택, 항목별 공개를 연결합니다.'),
    ('12/1~12/2', '발표용 빌드와 실기 리허설', '두 대에서 정상 흐름과 거절·경로 오류를 재현합니다. 화면 폭이 좁아져도 주요 버튼과 종료 동작이 유지되는지 확인합니다.'),
])
sub('시연을 통과하는 세 가지 조건')
table(('시험 장면', '통과 기준'), (1.50, 5.00), [
    ('출발', '통화 중 P에서 D로 바뀌면 화면과 음성 송수신이 멈춥니다. 다음 주차에는 사용자 확인 뒤에만 대화를 다시 시작합니다.'),
    ('한쪽 거절·취소', '장소·시각에 한쪽만 수락하면 내비 요청이 발생하지 않습니다. 만남 뒤 ‘각자’·미응답·기한 만료가 있으면 공개 화면을 열지 않습니다. 취소된 제안의 늦은 수락도 무효로 처리합니다.'),
    ('항목별 공개', '동행이 확정되면 공개 선택 화면을 엽니다. 인스타그램만 공유하면 상대 화면에는 해당 계정만 표시됩니다. 매칭 응답·알림·로그에서 정밀 위치와 최종 목적지 노출이 0건인지 확인합니다.'),
])
paragraph('장비에서 지원을 확인하지 못한 연동은 모의 구간으로 표시합니다. 내비 연동이 어려우면 수동 권역 선택과 장소 카드로 흐름을 이어가고, 주차 상태가 불명확한 장비에서는 대화 기능을 잠급니다.')

chapter('6 기대효과 및 발전 가능성')
paragraph('주말이나 짧은 연차에 혼자 차로 떠나는 20~30대 직장인은 일정을 바꾸지 않고도 잠깐 대화하거나 만날 수 있습니다. 다음 여행에서도 그날의 여유 시간에 맞춰 다시 이용할 수 있습니다.')
sub('제주 서부의 주말부터 엽니다')
paragraph('첫 운영 후보는 애월–협재 구간입니다. 20~30명과 ‘각자’ 종료와 정보 공개를 테스트한 뒤, 렌터카 인수 안내와 카페 제휴를 통해 주말 오후 이용자를 모집합니다. 후보가 없으면 대기 종료를 안내합니다.')
table(('측정 항목', '무엇을 보고 결정할지'), (1.51, 4.99), [
    ('연결과 대기', '5분 안에 음성으로 이어진 유효 요청 비율과 후보 없음 비율'),
    ('부담 없는 종료', '대화·만남 종료 후 만족도, 공개 범위 이해도, 원치 않은 접촉'),
    ('다음 여행 재사용', '다음 혼행을 실제로 떠난 이용자 가운데 앱을 다시 쓴 비율'),
])
paragraph('첫 네 번의 주말 운영 후 5분 이내 연결률 60%를 확장 검토 기준으로 삼습니다. 공개 오류와 신고 대응을 점검한 뒤 제주 내 시간대를 먼저 넓히고, 다른 권역과 지역 코스 제휴를 검토합니다.')
sub('권역 운영 2개월차 사용 규모')
paragraph('MAU는 월간 유효 연결 요청 또는 음성 참여를 한 고유 이용자 수입니다. M+1 유지율은 첫 활성 이용자 중 다음 달 같은 행동을 한 비율입니다. 월 신규 도달 규모는 첫 두 달 동안 동일하다고 가정합니다.')
table(('계획 가정과 산정값', '보수', '기준', '확대'), (3.05, 1.15, 1.15, 1.15), [
    ('월 신규 타깃 도달 × 첫 활성 전환율', '600명 × 10%', '1,200명 × 15%', '2,400명 × 20%'),
    ('월 최초 활성 / M+1 유지율 가정', '60명 / 12%', '180명 / 20%', '480명 / 30%'),
    ('2개월차 예상 MAU', '67명', '216명', '624명'),
])
caption('2개월차 MAU = 월 최초 활성 × (1 + M+1 유지율). 표의 가정은 파일럿 결과로 갱신합니다.')

doc.save(destination)
print(destination)

