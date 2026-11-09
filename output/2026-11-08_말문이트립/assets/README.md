# 말문이 트립 화면 자료

2026년 11월 8일 작성한 서비스 기획서의 시안 원본입니다. 실제 APK 실행 화면이나 실제 이용자의 조사 응답이 아닙니다.

## 열어보기

`index.html`을 브라우저로 열면 화면별 이미지를 볼 수 있습니다. 각 화면 제목을 누르면 해당 정적 HTML 시안이 열립니다. 계정 인증·마이크·서버·결제·내비 API는 연결되지 않은 시각 자료입니다. PNG는 별도 프로그램 없이 열 수 있습니다.

## 파일 구성

- `Sxx_*.png`: Pleos의 시스템 문맥을 참고한 전체 태블릿 시안 26개. 출력 2560×1440 px.
- `Sxx_*_app.png`: 같은 화면의 앱 창 확대본 26개. DOCX에 가독성을 위해 사용했습니다.
- `Sxx_*.html`: 화면을 재현하는 정적 HTML 원본. Noto Sans KR 또는 기본 한국어 글꼴을 사용합니다.
- `screen_manifest.json`: 화면 ID, 이름, 목적, 시안 영역과 overflow 검사 기록.
- `persona_seoyun.png`, `persona_junho.png`: AI로 생성한 가상 페르소나. 실제 조사 참여자가 아닙니다.
- `architecture.png`: 사람 간 음성 전송과 AI 질문 보조를 분리한 제안 구조도.
- `responsive_portrait.png`: 두 앱 배치의 좁은 앱 창 대응 제안.
- `pleos_official_windows.png`: Pleos 공식 Window Policy의 창 배치 참고 이미지.
- `pleos_official_layout.svg`, `pleos_official_layout.png`: Pleos 공식 화면 유형 도식과 래스터 사본.

## 흐름 읽기

기본은 S01 → S02 → S03 → S04 → S05 → S05B → S06 → S06B → S07 → S08 → S09 → S10 → S11의 음성 전용 경로입니다. S04B는 처음에 만남도 검토한다고 선택한 사람에게만 추가합니다.

선택형 만남 예시는 S12 → S13 → S13B → S14 → S15 → S16 → S16B → S17입니다. 이 예시는 초기 만남 선호를 선택한 별도 상황이며, 음성 전용 선택을 만남으로 자동 전환하지 않습니다. S13은 구체 장소·시각의 제안, S13B는 양쪽의 확인 뒤 본인 내비 요청 단계입니다.

S18은 연결 후 피드백입니다. S21은 실제 본인 여행을 마칠 때의 별도 확인이며, 대화·만남 종료가 곧 여행 종료라는 뜻은 아닙니다. S19는 후보 없음, S20은 즉시 중단·차단 뒤 신고 경로입니다. 예외나 동의 거절은 정상적인 이용 결과입니다.

모든 선택·별명·계정 상태·시간·차량 수치는 모의 데이터입니다. 선택 표시가 있는 화면은 사용자가 해당 선택을 한 예시이며 기본 동의 상태를 뜻하지 않습니다. 실제 구현에서는 권한과 필수·선택 동의를 분리하고, 주차와 현재 UX 제한이 확인되기 전 대화·조작을 허용하지 않습니다.

## 공식 화면 출처

- [Pleos Display Layout](https://document.pleos.ai/en/docs/connect/guide/docs-design/getting-started/layout)
- [Pleos Window Policy](https://document.pleos.ai/en/docs/connect/guide/docs-design/getting-started/window)
- [공식 창 배치 PNG](https://document.pleos.ai/en/assets/images/window-policy-1-380137ecc779345d4dc94e9ce2a3dc24.png)

공식 그림은 플랫폼 참고 자료로 구분했습니다. 자체 시안의 픽셀 크기와 여백은 공식 고정 해상도나 실기 dp 규격 준수의 증거가 아닙니다. 시스템 주행 정보·공조·독은 앱 개발 범위가 아닙니다.
