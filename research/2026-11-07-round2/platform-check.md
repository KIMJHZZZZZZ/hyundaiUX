# Pleos 공개 범위 재점검 — 2026-11-07

전부 주차형으로 제한했던 이전 판단은 수정해야 한다. **주행 오디오는 가능 범주이고, 동승자 창은 실제 문서화되어 있다.** 다만 허용되는 기능·화면·권한을 따로 검증해야 한다.

- **주행 Music/Audio:** 팟캐스트·오디오북·라디오와 단순 재생 조작이 범위에 들어간다. 차량 미디어 컨트롤과 MediaSession, 백그라운드 재생이 필요하다. 쇼핑·영상·게임이 주기능인데 오디오 카테고리를 붙이는 우회는 부적합하다. CarUxRestrictions는 제한되는 기능을 잠그는 기준이지 모든 오디오를 일괄 중단하는 신호가 아니다. 실제 오디오 중단·감쇠는 오디오 포커스 정책에 따른다.[1]
- **동승자 화면:** Connect-W는 양쪽 App library와 passenger window를 제공한다. 동승자 측에서 실행한 앱은 그 창에만 실행된다. 이 사실을 활용할 수 있다. 그러나 별도 조수석·후석 디스플레이 접근 API, 운전자에게 보이지 않는 프라이버시 화면, 주행 영상·게임 예외 권한은 이번 공개 문서에서 확인하지 못했다. 창 위치만으로 제한을 해제하면 안 된다.[2]
- **Gleo:** 승인된 스키마로 앱 기능을 호출하는 입력 인터페이스다. 앱이 Gleo를 범용 생성 LLM으로 호출하는 공개 엔드포인트는 확인하지 못했다. 별도 LLM 백엔드의 비용·상태·도구 호출은 자체 설계다. Schema 문서는 최대 3개 actionCalls, 음악 가이드는 3~5개 추가 기능을 언급해 차이가 있다. MVP는 3개로 두고 승인 시 확인한다.[3]
- **경로·좌표·ETA:** NaviHelper에 현재 위치·목적지·경로 상태 요청과 이벤트가 있다. 2026-10-19 릴리스는 CurrentLocationInfo 좌표 순서, remainTime/remainDistance, onTripInfo를 확인해준다. 다만 정확한 좌표 필드·갱신 주기·정밀도·전체 경로 polyline 반환 범위는 열람한 본문만으로 확정하지 못했다. 요청 API 존재와 실차 데이터 제공을 구분한다.[4]
- **SDK 상태:** 10/19 릴리스에 TTS/STT/FusedLocation 버전이 있어 ‘아직 출시되지 않았다’고 단정할 수 없다. 반면 신청 안내에는 준비 중 상태로 적혀 있어 문서 간 상태 차이가 있다. 참가 계정의 실제 제공·권한과 에뮬레이터 동작으로 판정해야 한다.[5]
- **카메라·블랙박스:** 직접 센서 접근은 금지된다. 앱 심사서의 ‘카메라 권한’ 언급이나 내비의 CameraAlert는 차량 영상 취득 API의 근거가 아니다. CameraAlert는 단속카메라 관련 정보다. 타사 앱의 차량 카메라·블랙박스 캡처 권한은 확인하지 못했으므로 자동촬영은 후순위로 둔다.[6]

MVP 검증은 ①실제 NaviHelper 이벤트 ②차량 미디어 재생/포커스 ③주행 시 시각 기능 제한 ④동승자 창 배치 순서로 진행한다. 구현·문서·승인 필요·모의를 화면에서 구분한다. 네트워크 오류 시 로컬 콘텐츠, ETA 소실 시 고정 길이, 미확인 화면 권한 시 주차 편집 또는 동승자 폰으로 전환한다. 위치·사진 전송과 거래 실행은 사용자 동의를 받는다.

근거 링크(공식 본문 열람):

[1] [Music/Audio 가이드](https://document.pleos.ai/en/docs/pleos-only/vehicle-app-developer-guide/music-audio-app-developement-guide), [카테고리별 주행 허용](https://document.pleos.ai/en/docs/pleos-only/vehicle-app-planning-guide/app-category)

[2] [Window Policy](https://document.pleos.ai/en/docs/connect/guide/docs-design/getting-started/window)

[3] [Gleo App Schema](https://document.pleos.ai/docs/pleos-only/app-integration-guide/guide/app-capability)

[4] [NaviHelper 이벤트](https://document.pleos.ai/en/docs/pleos-only/connect-sdk-pleos/NaviHelper/event-listeners), [2026-10-19 릴리스](https://document.pleos.ai/en/docs/pleos-only/release-note/sdk-release-note)

[5] [프로젝트·SDK 신청](https://document.pleos.ai/docs/pleos-only/create-my-project)

[6] [하드웨어 접근 정책](https://document.pleos.ai/en/docs/pleos-only/vehicle-app-planning-guide/platform-api-architecture)
