# Pleos 공식 개발 문서 확인 기록

- 확인일: 2026-11-06, Asia/Seoul.
- 담당 범위: 프로젝트에서 인용한 Pleos 공식 개발 문서와 일부 직접 연결 가이드. 원본 프로젝트 문서는 수정하지 않았다.
- **전체 페이지·모든 텍스트·모든 이미지를 확인한 상태가 아니다.** 아래 상태가 실제 도구 출력에서 읽은 범위다.
- 페이지 URL은 말미 `/`와 같은 문서의 중복 전달을 합쳐 **32개**로 집계했다. 추가 web 재확인 후 **32개 모두 접근 시도**, **27개 본문 전체 확인**, **5개 본문 추출 실패**다. 미접근 및 일부만 읽은 URL은 남아 있지 않다. 추출 실패를 정상 페이지나 404로 단정하지 않는다.
- 본문 이미지 링크 **9개 접근 시도**: 5개는 이미지 URL 메타데이터만, 4개는 Cache miss 오류. **실제 시각 확인한 이미지 0개**다. alt 텍스트·이미지 URL 확인을 이미지 시각 검토로 계산하지 않았다.
- 추가 텍스트 열람에서 이미지 참조 21개를 더 발견했지만 요청에 따라 접근을 재시도하거나 다운로드하지 않았다. 따라서 본문 출력에서 발견한 이미지 참조는 총 30개이며, 모두 시각 미확인이다. 원본 페이지 렌더링을 통한 이미지 전수 목록은 아니다.
- SDK API 클래스·멤버 전체 전수, 전역 footer의 외부 링크, 계정 로그인 이후 콘솔은 조사하지 않았다.

## 실제 본문을 읽은 페이지

| 번호 | URL | 텍스트 확인 상태 | 본문 이미지 상태 | 읽은 내용 / 남은 한계 |
| --- | --- | --- | --- | --- |
| 1 | https://developers.pleos.ai/playground | 전체 출력 확인, 총 99줄 | background, code-image 2개 링크 시도 모두 Cache miss | 개발 단계와 Vehicle/NaviHelper/TTS SDK 소개. 링크가 버튼으로 추출되어 일부 실제 대상 URL은 확인하지 못함. |
| 2 | https://document.pleos.ai/en/docs/pleos-only/app-test-guide/virtual-console-guide | 전체 본문 확인, 총 149줄. 잔여 116~119줄까지 추가 열람 | Emulation Controls 1개 URL 메타데이터만 | Vehicle/Motion/ADAS/Convenience/Safety/Energy/Climate 제어 표를 읽음. Defroster, 16~30°C 목표온도, 시트 온도, Air Cleaner 항목까지 확인. |
| 3 | https://document.pleos.ai/docs/pleos-only/connect-sdk-pleos/Vehicle/intro | 전체 본문 확인, 총 131줄 | 구성도 1개 URL 메타데이터만 | SDK v2.3.2 / Vehicle Service v2.3.21, 도메인·capability/get/set/callback·IPC 생명주기·설치 및 다음 단계 링크 확인. |
| 4 | https://document.pleos.ai/docs/pleos-only/connect-sdk-pleos/NaviHelper/intro | 전체 본문 확인, 총 135줄 | 구성도 1개 Cache miss | SDK v3.0.5, 목적지·경로·경유지·이벤트, 초기화/리스너/해제 순서, 개발환경 및 다음 단계 링크 확인. |
| 5 | https://document.pleos.ai/en/docs/pleos-only/create-my-project | 전체 본문 확인, 총 119줄 | 3개 중 2개 URL 메타데이터만, 1개 Cache miss | 가입·프로젝트 생성·프로젝트 키·SDK별 요청 상태 확인. 아래 SDK 가용성 근거. |
| 6 | https://document.pleos.ai/docs/pleos-only/app-integration-guide/guide/core-concepts | 전체 본문 확인, 총 77줄 | action_callback 1개 URL 메타데이터만 | Gleo function calling, App Schema 등록 및 Action/Callback 역할 확인. |
| 7 | https://document.pleos.ai/docs/pleos-only/app-integration-guide/guide/app-capability | 전체 본문 확인, 총 251줄 | 텍스트 추출에 본문 이미지 링크 없음. 브라우저 렌더 검증 안 함 | actionCalls 최대 3개, Activity/Broadcast 방식, 이름/description/parameter 제한과 예시 확인. |
| 8 | https://document.pleos.ai/docs/pleos-only/vehicle-app-planning-guide/driving-restiction-policy | 전체 본문 확인, 총 177줄 | 텍스트 추출에 본문 이미지 링크 없음. 브라우저 렌더 검증 안 함 | 북미·유럽·그외 지역의 주행 제한 표와 DO 미선언 동작 확인. |
| 9 | https://document.pleos.ai/docs/pleos-only/vehicle-app-developer-guide/driving-restriction-development-guide | 전체 본문 확인, 총 107줄 | 텍스트 추출에 본문 이미지 링크 없음. 브라우저 렌더 검증 안 함 | CarUxRestrictionsManager listener, ActiveRestrictions, NO_VIDEO 코드 확인. |
| 10 | https://document.pleos.ai/en/docs/pleos-only/vehicle-app-planning-guide/security-privacy | 전체 본문 확인, 총 85줄 | 텍스트 추출에 본문 이미지 링크 없음. 브라우저 렌더 검증 안 함 | 계정 전환/로그아웃, Keystore, 최소 수집·동의·로그 마스킹, 식별자 가명화, 주행 행동 데이터 마케팅 분리 확인. |

## 추가 재확인으로 본문 전체를 읽은 8개 페이지

처음에는 제목·URL·총 줄 수만 반환됐으나, 이후 URL을 직접 다시 열어 아래 본문을 모두 읽었다. 이미지 픽셀은 확인하지 않았다.

| 번호 | URL | 제목 / 줄 수 / 확인 내용 |
| --- | --- | --- |
| 11 | https://document.pleos.ai/docs/pleos-only/app-integration-guide/guide/action_callback | Callback Schema Writing Guide / 231줄. success/asking/fail, voice/beep/silent, 7초 Action timeout, data JSON 배열 문자열 확인. 본문 이미지 참조 없음. |
| 12 | https://document.pleos.ai/docs/pleos-only/app-integration-guide/guide/examples | Code Details with Examples / 320줄. ACTION_PARAM 수신, Activity/Broadcast 예시, APP_ACTION_RESPONSE Broadcast 응답 코드 확인. 본문 이미지 참조 없음. |
| 13 | https://document.pleos.ai/docs/pleos-only/app-integration-guide/guide/deliver-schema | Delivering the Schema to Gleo / 102줄. assets/schema.json, 검토·승인, Manifest action filter, 부팅·설치/삭제 스키마 갱신 설명 확인. 이미지 참조 1개 미확인. |
| 14 | https://document.pleos.ai/docs/pleos-only/app-integration-guide/use-cases/radio-app | How to Integrate Radio App with Gleo AI / 352줄. SWITCH_BAND/SEARCH_STATION/PLAY_FREQUENCY 스키마와 수신·응답 예시 확인. 본문 이미지 참조 없음. |
| 15 | https://document.pleos.ai/docs/pleos-only/connect-sdk-pleos/Vehicle/project-setup | Importing Vehicle SDK / 161줄. Maven 저장소 및 Vehicle:2.3.2 의존성의 Kotlin/Groovy 양쪽 코드 확인. 본문 이미지 참조 없음. |
| 16 | https://document.pleos.ai/docs/pleos-only/connect-sdk-pleos/NaviHelper/importing-sdk | Importing NaviHelper SDK / 161줄. Maven 저장소 및 NaviHelper:3.0.5 의존성의 Kotlin/Groovy 양쪽 코드 확인. 본문 이미지 참조 없음. |
| 17 | https://document.pleos.ai/en/docs/pleos-only/vehicle-app-planning-guide/api-compatibility-availability | API Compatibility & Availability / 91줄. 모델별 capability, 내비 탑재 차량 조건, AAOS 지원 여부 확인 정책 읽음. 본문 이미지 참조 없음. |
| 18 | https://document.pleos.ai/en/docs/pleos-only/vehicle-app-planning-guide/pleos-connect-sdk-api | SDK API Policy / 93줄. AAOS 표준우선·확장 API·최소 2 major 버전 하위호환 정책 확인. 이미지 참조 1개 미확인. |

## 추가 전달 URL 14개 접근 결과

구 경로를 포함해 모든 URL을 직접 web open했다. 도구에 보인 URL을 그대로 기록하며, 실제 HTTP 리디렉션 체인은 조사하지 않았다. 9개는 본문 전체를 읽고 5개는 아래 오류로 본문을 읽지 못했다.

| 번호 | URL | 텍스트 및 이미지 확인 상태 |
| --- | --- | --- |
| 19 | https://document.pleos.ai/docs/connect/guide/getting-started/application-development/setup-connect-sdk-emulator | 본문 전체 155줄. API28 이상/Gradle8 이상/Emulator2.1.0, 시스템 이미지 추가, AVD·Cold boot·4GB RAM·API34 설치 과정 확인. 이미지 참조 10개 미확인. |
| 20 | https://document.pleos.ai/docs/pleos-only/connect-sdk-pleos/ | 본문 전체 96줄. 5개 SDK·AAOS alignment·capability 및 퍼미션 승인/심사 정책 확인. 이미지 참조 1개 미확인. |
| 21 | https://document.pleos.ai/docs/pleos-only/tutorial/vehicle-sdk | 0 readable lines 반환. 본문·이미지 미확인. 404라고 단정하지 않음. |
| 22 | https://document.pleos.ai/api-reference/connect-sdk-pleos/ | 0 readable lines 반환. 본문·이미지 미확인. 404라고 단정하지 않음. |
| 23 | https://document.pleos.ai/docs/pleos-only/distribute/app-review-guide | 본문 전체 78줄. 안전/성능/주의분산/등록정보/개인정보·보안 심사 항목 확인. 본문 이미지 참조 없음. |
| 24 | https://document.pleos.ai/docs/pleos-only/distribute/app-review-guide/review-driver-distraction-elements | 본문 전체 95줄. 여기서 미디어 앱은 동영상·게임·브라우저를 뜻함. 주차 중만 사용, 주행 시작 시 UI 숨김/중단, 헤드업 알림 금지, 브라우저 비밀번호·결제 보호 확인. 본문 이미지 참조 없음. |
| 25 | https://document.pleos.ai/docs/connect/guide/docs-design/Introduction/intro | 본문 전체 166줄. 기본 원칙·텍스트 길이·글자 물리 크기·4.5:1 대비·0.25초 입력반응/지연안내·음성·반응형 설계 확인. 본문 이미지 참조 없음. 다운로드 리소스는 미확인. |
| 26 | https://document.pleos.ai/docs/connect/guide/docs-design/getting-started/layout | 본문 전체 101줄. status/driving view/GNB/app window, 상위 시스템 UI 레이어, S/W/WF, portrait·landscape 대응 확인. 이미지 참조 3개 미확인. |
| 27 | https://document.pleos.ai/docs/connect/guide/docs-design/foundations/colors | 2회 모두 (400) Timeout fetching. 본문·이미지 미확인. |
| 28 | https://document.pleos.ai/docs/pleos-only/vehicle-app-planning-guide/driver-distraction-guideline | 본문 전체 110줄. CarUxRestrictions 기반 축소/비활성, 영상 재개 금지, 오디오 포커스, 시선·터치 최소화 및 음성·최근항목·프리셋 우선 확인. 본문 이미지 참조 없음. |
| 29 | https://document.pleos.ai/en/docs/connect/guide/docs-design/getting-started/window | 본문 전체 118줄. S 1:1/2:0, W 2:1/1:2 창 정책, 시작·종료·이동·멀티윈도, 승객창·딥링크 동작 확인. 이미지 참조 5개 미확인. |
| 30 | https://document.pleos.ai/en/docs/pleos-only/vehicle-app-planning-guide/app-structure-screen-model | 본문 전체 103줄. Driving view 고정, 최대2앱, Manifest 화면 방향, foreground 복원·background 정리·상태저장 확인. 본문 이미지 참조 없음. |
| 31 | https://document.pleos.ai/api-reference/connect-sdk-pleos/Vehicle/intro | 0 readable lines 반환. 본문·이미지 미확인. 404라고 단정하지 않음. |
| 32 | https://document.pleos.ai/api-reference/connect-sdk-pleos/NaviHelper/intro | 0 readable lines 반환. 본문·이미지 미확인. 404라고 단정하지 않음. |

`https://document.pleos.ai/api-reference/connect-sdk-pleos`는 22번의 말미 슬래시 변형으로 합쳤다. API reference 경로와 docs 경로는 서로 같은 내용인지 확인하지 못했으므로 별도 URL로 유지했다.

## 확인된 핵심 차이와 구현 시 해석

### SDK 소개와 실제 이용 상태

프로젝트 생성 가이드의 상태 표 기준:

- Vehicle **State** 및 NaviHelper: Ready to Use, 신청 없이 즉시 사용 가능.
- Vehicle **Control**, FusedLocation, TextToSpeech, SpeechToText: Not Available Yet, 신청 불가, 준비 중 배지.
- Request Required는 신청 후 Under Review를 거쳐 승인되면 Ready to Use가 된다. Affiliation Required는 웹 신청이 아닌 제휴 계약이 필요하다.
- Client ID/Secret은 TTS/STT 등 서버 연결 SDK용이며, Emulator 2.1.0 이상은 CRN이 불필요하다고 설명한다.

Vehicle 소개 문서에 제어 API가 기술되어 있고 Playground가 TTS 기능을 소개하더라도, 이를 현재 일반 개발자가 해당 API를 이용할 수 있다는 근거로 해석할 수 없다. **기능 설명과 접근 상태는 구분해야 한다.** 현재 연결 계정의 실제 콘솔 상태는 확인하지 않았다.

API Compatibility 문서는 TTS/STT를 차량 호환성 차원에서 Fully compatible로 기재한다. 이는 프로젝트 생성 가이드의 접근 준비 상태와 다른 축이다. Vehicle은 checkXXXCapabilities, FusedLocation은 isSupported로 실제 지원 여부를 확인하며 NaviHelper는 내비게이션 탑재 차량에 한정된다. SDK Overview는 필요한 퍼미션의 사전 협의·승인 범위 외 선언/호출이 앱 심사를 통과하지 못한다고 설명한다.

근거: https://document.pleos.ai/en/docs/pleos-only/create-my-project 및 Vehicle/NaviHelper 소개 페이지.

### Gleo

- App Schema의 `actionCalls`는 최대 3개다. 화면에서 사용하는 앱 기능 전체가 3개로 제한된다는 뜻은 아니다.
- function 이름은 대문자와 밑줄, description은 영어, parameter는 string/number/boolean/array로 제한된다. 문자열 enum만 허용하며 nullable type 배열은 지원하지 않는다.
- `required`를 명시해도 Gleo가 모든 필수 parameter를 채운다고 보장하지 않는다. 앱 측 검증이 필요하다는 구현상 해석이 가능하다.
- component `activity`는 startActivity, `service`는 sendBroadcast 방식으로 설명된다.
- **스키마 검토·승인 확인:** deliver-schema 본문은 파일을 `assets/schema.json`에 두고 가이드라인 검토를 거쳐 승인 후 통합이 자동 활성화된다고 설명한다. 각 function의 Manifest action filter도 필요하다. 부팅 시 스캔과 설치/삭제 시 데이터베이스 갱신 설명도 읽었다. 실제 제출 콘솔에서 수행하지는 않았다.
- Callback 본문은 Gleo가 7초 후 Action을 취소한다고 설명한다. 상태는 success/asking/fail, 출력 mode는 voice/beep/silent다. 앱 자체 안내 재생은 silent를 고려하고 결과 data는 필요한 문맥만 반환하도록 안내한다.

근거: https://document.pleos.ai/docs/pleos-only/app-integration-guide/guide/core-concepts , https://document.pleos.ai/docs/pleos-only/app-integration-guide/guide/app-capability , https://document.pleos.ai/docs/pleos-only/app-integration-guide/guide/deliver-schema , https://document.pleos.ai/docs/pleos-only/app-integration-guide/guide/action_callback .

### 주행 제한

- DO 미선언 앱은 주차 시 사용 가능하고 주행 시 사용 불가다.
- DO 선언 앱도 CarUxRestrictions와 ActiveRestrictions를 받아 기능별 UX 제한을 직접 적용해야 한다.
- 지역표에서 북미는 주행 중 키보드·다이얼패드·내비 검색이 제한되고 통합 검색은 음성 한정이다. 유럽은 키보드·다이얼패드·통합/내비 검색이 허용된다. 그외 지역은 미디어 로그인/설정/검색도 허용되는 표다. 디지털키·도어·시트·차량 설정, 동영상, QR 로그인, 대용량 매뉴얼은 모든 지역에서 주행 중 제한된다.
- 실제 앱 동작은 지역을 임의로 추정하기보다 플랫폼이 통지하는 ActiveRestrictions에 맞춰야 한다. 문서는 플랫폼 버전·양산 차량에 따라 정책 차이가 날 수 있다고 명시한다.
- 공개되지 않은 UX 규제 Figma 사양서는 확인하지 않았다.

근거: https://document.pleos.ai/docs/pleos-only/vehicle-app-planning-guide/driving-restiction-policy 및 https://document.pleos.ai/docs/pleos-only/vehicle-app-developer-guide/driving-restriction-development-guide.

## 이미지 접근 기록

| 이미지 URL | 결과 |
| --- | --- |
| https://document.pleos.ai/assets/images/action_callback-fb82919ad6c042cb8fb199754d4fff8d.png | URL 메타데이터 반환, 픽셀 미확인 |
| https://document.pleos.ai/assets/images/vehicle-sdk-diagram-9c2c1d6739316101e282f1543f1976b0.png | URL 메타데이터 반환, 픽셀 미확인 |
| https://document.pleos.ai/assets/images/navi-helper-509b526aa25dda110c7187abe640b76e.png | Cache miss, 미확인 |
| https://document.pleos.ai/en/assets/images/vehicle-emulator-emulation-controls-184fc74a83bacece476a402f7652caa6.png | URL 메타데이터 반환, 픽셀 미확인 |
| https://document.pleos.ai/en/assets/images/create-connect-project-en-8647ff995c29948d88df91dba21b739d.png | Cache miss, 미확인 |
| https://document.pleos.ai/en/assets/images/my-project-info-en-093ff54eeebcc8aefa52042a44617ace.png | URL 메타데이터 반환, 픽셀 미확인 |
| https://document.pleos.ai/en/assets/images/sdk-need-to-apply-en-a7556e017d02b3f3d797c668b5f36c67.png | URL 메타데이터 반환, 픽셀 미확인 |
| https://static.playground.umos.ai/builds/developers-web/261029.0925b3c3/_next/static/media/home_bg.f56281f9.png | Cache miss, 미확인 |
| https://static.playground.umos.ai/builds/developers-web/261029.0925b3c3/_next/static/media/code.e1bc50a5.png | Cache miss, 미확인 |

## 도구 제약과 남은 링크 범위

- 초기 web 도구의 일부 다중 click 결과는 제목/라인수만 표시했다. 이후 해당 8개 URL과 추가 14개 URL을 직접 다시 열어 텍스트를 읽었다. Virtual Console 잔여도 다시 읽었다.
- shell Python requests로 원문을 읽으려던 요청은 document.pleos.ai DNS 조회 오류로 실패했다. 지침에 따라 네트워크 권한 재요청을 수행했으나 승인대기 후 작업이 중단되어 실행 결과를 받지 못했다. 오케스트레이터가 작업을 중단했으며, 사용자에 의한 중단이나 권한 거절로 단정하지 않는다.
- 중단된 호출의 결과는 집계하지 않았고, 이후 승인 요청 없이 web 도구만으로 재확인했다. shell·다운로드·이미지 재시도는 하지 않았다.
- 미확인 본문 URL: **5개** = 0 readable lines 4개 + 색상 가이드 timeout 1개. 나머지 27개는 출력된 본문 전체를 읽었다. 본문 이미지 참조 30개는 모두 시각 미확인이다.
- 아래는 실제 읽은 페이지에서 발견한 하위 링크지만, 위 목록 외에는 대상으로 추적하지 못했다: Vehicle 도메인 획득·Permission·Error code·API Reference·샘플앱의 현재 링크, NaviHelper 권한·초기화·이벤트·목적지·경로·경유지·오류처리·API Reference, 별도 Emulator 설정/Virtual Console 셋업/마이크 설정 문서, App Security Guide, AAOS CarUxRestrictionsManager/CarUxRestrictions 및 JSON Schema 원문, Design Resources 다운로드. 이 하위 링크 집합의 고유 URL 총수는 추출하지 못했으므로 숫자를 추정하지 않는다.
- 따라서 **명시 대상 32개 URL의 접근 시도는 완료했지만, 모든 본문과 하위 페이지·이미지를 전수 검토했다는 결론은 지원되지 않는다.**
