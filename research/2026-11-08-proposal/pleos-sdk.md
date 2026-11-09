# 말문이 트립! — Pleos Connect SDK·UI 기술 근거

조사일: 2026-11-08 (Asia/Seoul). 이 문서는 공개된 **Pleos 공식 문서**를 읽은 결과다. SDK 다운로드·Gradle 빌드·APK 실행·마이크·실제 차량 또는 태블릿 동작은 시험하지 않았다. `확인`은 문서에 명시된 사실, `설계`는 제안하는 구현, `미확인`은 계정·장비 또는 실행 검증이 필요한 항목이다. S01~S41은 이 파일 안의 출처 ID다.

## 1. 제안서에 바로 반영할 결론

1. 앱 실행 플랫폼은 **Pleos Connect**, 개발 포털·SDK·에뮬레이터 환경은 **Pleos Playground**다. AAOS 기반 Android 앱으로 만들며 Kotlin/Java를 사용한다. [S01](https://document.pleos.ai/en/docs/connect/guide/connect), [S02](https://document.pleos.ai/en/docs/connect/guide/getting-started/application-development/setup-connect-sdk-emulator)
2. **운전자 대상 소셜 대화가 음성이라는 이유만으로 주행 허용되는 것은 아니다.** Social/Communication 카테고리는 존재하지만 카테고리 가이드의 제한적 주행 허용 예시는 Music/Audio, Maps/Navigation, Mobility Services다. 주차 중에 설문·AI 대화·사람 간 통화·추천·참여·만남 동의·경로 변경을 완료하는 MVP가 근거에 맞는다. 주행 중은 앱의 대화·매칭 입력을 잠그고 기존 약속 상태만 유지한다. 짧은 상태 음성도 별도 허용 확인 전에는 기본값을 무음으로 둔다. [S03](https://document.pleos.ai/en/docs/pleos-only/vehicle-app-planning-guide/app-category)
3. **Gleo Interface와 자체 LLM 서버를 구분해야 한다.** 공식 Emulator v2.1.0 릴리스에는 “End of support for LLM SDK”라고 명시되어 있다. 오래된 SDK 소개 페이지의 LLM SDK를 현재 MVP 의존성으로 제시하면 안 된다. Gleo는 승인된 앱 기능을 음성 명령으로 호출하는 선택 입력 인터페이스로 설계하고, 설문 구조화·대화 주제 생성은 별도 서버의 LLM 기능으로 구분한다. [S04](https://document.pleos.ai/en/docs/pleos-only/release-note/emulator-release-note), [S05](https://document.pleos.ai/docs/pleos-only/app-integration-guide/guide/core-concepts)
4. **NaviHelper의 목적지·경유지·이벤트 존재는 확인됐지만, 전체 도로 경로 polyline을 얻어 정확한 겹침률과 우회분을 계산할 수 있다고 확정할 근거는 부족하다.** 경로 도형이 확보되기 전에는 사용자가 고른 넓은 여행 권역·시간대 기반 추천으로 시연하고, 실제 도로 우회시간은 검증한 별도 경로 엔진을 붙이거나 제외한다. [S06](https://document.pleos.ai/docs/pleos-only/connect-sdk-pleos/NaviHelper/intro), [S07](https://document.pleos.ai/en/docs/pleos-only/connect-sdk-pleos/NaviHelper/event-listeners)
5. **두 사람의 실시간 음성 연결은 STT/TTS가 아니다.** Pleos STT는 음성을 텍스트로, TTS는 텍스트를 차량 음성으로 바꾼다. 통화는 별도의 WebRTC 계열 미디어 전송·시그널링·릴레이 설계가 필요하다. Pleos의 소셜 음성통화용 공개 SDK나 해당 제3자 미디어 스택의 실기 지원을 이번 공식 문서에서 확인하지 못했다. 따라서 1주차에 반드시 실기 마이크 경로를 검증한다. [S08](https://document.pleos.ai/en/docs/pleos-only/connect-sdk-pleos/SpeechToText/intro), [S09](https://document.pleos.ai/en/docs/pleos-only/connect-sdk-pleos/TextToSpeech/intro)
6. **일반 Android 태블릿과 Pleos 개발장비를 동일시하면 안 된다.** 일반 태블릿에서 자체 UI·서버·음성 통신을 시험하는 것과 Pleos 서비스·차량 신호·Gleo를 시험하는 것은 별개다. 배포받을 장비의 이미지·ADB·서명·마이크·네트워크·차량 상태 입력 방식을 아직 확인하지 못했다. 공식 Devbox 소개가 있는 것은 장비 호환·대여·설치 권한의 보장이 아니다. [S10](https://pleos.ai/playground/develop?focus=fleet_api), [S11](https://document.pleos.ai/en/docs/pleos-only/vehicle-app-planning-guide/platform-api-architecture)

## 2. 버전과 공개 접근 상태 — 서로 다른 사실을 섞지 않기

| 항목 | 확인한 공식 문서 상태 | 제안서·개발 적용 |
|---|---|---|
| Emulator | 2026-10-19 공식 릴리스 `v2.1.0`; LLM SDK·CRN·Bluetooth dongle integration 지원 종료 | 신규 기준은 2.1.0. 옛 CRN 등록 화면이나 2.0 마이크 화면은 현재 설치 요구사항의 증거로 쓰지 않는다. [S04](https://document.pleos.ai/en/docs/pleos-only/release-note/emulator-release-note) |
| Vehicle SDK | **한국어** 릴리스는 `v2.3.2`, **영어** 같은 날짜 릴리스는 `v2.3.1` | 언어판 불일치가 실제로 존재한다. 제품에 사용할 버전은 다운로드 가능한 artifact와 장비 서비스 호환성으로 pin한다. 본 서비스에는 불필요한 차량 제어를 넣지 않는다. [S12-KO](https://document.pleos.ai/docs/pleos-only/release-note/sdk-release-note), [S12-EN](https://document.pleos.ai/en/docs/pleos-only/release-note/sdk-release-note) |
| NaviHelper | 양쪽 릴리스·import 안내 모두 `3.0.5` | MVP 차량 연동 후보. 현재 Maven 예시는 `ai.pleos.playground:NaviHelper:3.0.5`. [S13](https://document.pleos.ai/en/docs/pleos-only/connect-sdk-pleos/NaviHelper/importing-sdk) |
| TextToSpeech / SpeechToText | 양쪽 릴리스·현재 가이드 모두 `3.3.1` | 버전 문서 존재와 실제 계정 승인·실기 사용 성공을 구분한다. [S08](https://document.pleos.ai/en/docs/pleos-only/connect-sdk-pleos/SpeechToText/intro), [S09](https://document.pleos.ai/en/docs/pleos-only/connect-sdk-pleos/TextToSpeech/intro) |
| FusedLocation | 한국어 릴리스 `1.1.3`, 영어 릴리스·영어 소개 `1.1.2` | 좌표 추적을 MVP 필수로 만들지 않는다. 사용하면 `isSupported()`와 null·error 처리를 먼저 구현한다. [S12-KO](https://document.pleos.ai/docs/pleos-only/release-note/sdk-release-note), [S14](https://document.pleos.ai/en/docs/pleos-only/connect-sdk-pleos/FusedLocation/intro) |
| SDK 신청 페이지 | Vehicle State·NaviHelper는 즉시 사용 가능, FusedLocation·TTS·STT·Vehicle Control은 준비 중이라고 표기. 별도 제휴가 필요한 상태도 존재 | 위 릴리스 문서와 접근 안내가 일치하지 않는다. **출시 안 됨**이나 **모두 누구나 사용 가능** 어느 쪽도 단정하지 않는다. 참가 계정의 상태·다운로드·서비스 응답을 별도로 기록한다. [S15](https://document.pleos.ai/en/docs/pleos-only/create-my-project) |
| 차량별 호환 | NaviHelper는 내비 장착 차량, Vehicle은 capability, FusedLocation은 `isSupported` 확인. AAOS property 접근성도 차량별로 다름 | 버전 숫자·차종명만으로 동작을 판정하지 않는다. [S16](https://document.pleos.ai/en/docs/pleos-only/vehicle-app-planning-guide/api-compatibility-availability) |

Maven 저장소: `https://nexus-playground.pleos.ai/repository/maven-releases/`. 이 주소와 dependency 예시는 문서 확인이며 실제 네트워크 다운로드 성공을 의미하지 않는다. [S13](https://document.pleos.ai/en/docs/pleos-only/connect-sdk-pleos/NaviHelper/importing-sdk)

## 3. 주차 판정과 잠금 — 기어·속도와 UX 허용은 다른 층위

**확인:** Pleos는 속도·기어·브레이크 등과 지역 규정으로 주행 제한을 결정한다. DO(Distraction Optimization)를 선언하지 않은 앱은 기본적으로 주차 때 사용 가능, 주행 때 사용 불가다. DO를 선언하더라도 필요한 기능별 제한을 앱이 적용해야 한다. [S17](https://document.pleos.ai/en/docs/pleos-only/vehicle-app-planning-guide/driving-restiction-policy)

**확인:** UX 기준은 `CarUxRestrictionsManager.registerListener()` → `onUxRestrictionsChanged()` → `CarUxRestrictions`와 active flags다. `isRequiresDistractionOptimization()` 하나만 확인하거나 화면 창 위치만으로 예외를 가정하면 안 된다. Pleos의 상세 UX 제한 Figma 명세는 공개하지 않는다고 적혀 있다. [S18](https://document.pleos.ai/en/docs/pleos-only/vehicle-app-developer-guide/driving-restriction-development-guide)

**확인:** 속도·기어는 AAOS Car API 쪽 표준 데이터다. 속도는 `CarPropertyManager`의 `PERF_VEHICLE_SPEED` 경로를 Pleos FAQ가 안내한다. 반면 이번 조사에서는 기어의 구체 property ID·권한·콜백 시그니처를 Pleos 본문만으로 확정하지 않았으므로 그대로 구현 완료처럼 쓰지 않는다. SDK의 옛 `VehicleSpeedListener/onSpeedUpdated`는 최신 릴리스에서 삭제됐다. [S19](https://document.pleos.ai/en/docs/pleos-only/vehicle-app-planning-guide/pleos-connect-sdk-api), [S20](https://document.pleos.ai/en/docs/pleos-only/vehicle-app-developer-guide/vehicle-app-faq), [S12-KO](https://document.pleos.ai/docs/pleos-only/release-note/sdk-release-note)

**설계:** `parkedConfirmed && uxRestrictionsKnown && relevantRestrictionsCleared`일 때만 설문·사람/AI 대화·추천 선택·만남 동의·내비 변경을 연다. 정차 중 D, 신호대기, 센서 0값, 과거에 저장한 P 상태는 충분조건이 아니다. 현재값 불명·연결 단절·복귀 직후에는 잠근다. 정확한 주차 상태를 얻지 못하는 장비에서는 `주차 확인 모의`라고 표시한 테스트만 한다. 제품용 잠금을 수동 체크박스로 우회하지 않는다.

**설계 상태:** `UNKNOWN_LOCKED → PARKED_READY → SURVEY/MATCH/VOICE/MEETUP_CONSENT`; 어느 활성 상태에서도 제한 활성·주차 해제·포커스 상실 시 `PAUSED_LOCKED`. 음성 송수신·STT 요청·TTS를 중단하고 민감 카드와 입력을 닫는다. 재주차 후 사용자가 재개해야 하며 새로운 매칭이나 만남 동의를 자동 승인하지 않는다. OS 자체 제한은 그대로 따르며 자체 상태 머신은 추가 보호다.

**제품 문구:** “주행 중에는 대화와 만남 선택이 일시정지됩니다. 안전한 곳에 주차한 뒤 이어가세요.” AI가 차량 상태를 판단하거나 잠금을 해제하지 않는다. 주행 중 소셜 음성 대화는 6주 MVP 제외다.

## 4. NaviHelper에서 확인한 API·권한·콜백

| 기능 | 문서상 API/권한/결과 | 말문이 트립! 적용 |
|---|---|---|
| 초기화 | `NaviHelper(applicationContext)`; `initialize(onConnected, onFailed)`; 최초 연결 성공 또는 초기 재시도 소진 결과 | 연결 전 기능 비활성화. 이 두 callback을 지속적인 모든 연결 상태 보장으로 확대 해석하지 않는다. 사용 종료에 listener 제거와 `release()`. [S21](https://document.pleos.ai/en/docs/pleos-only/connect-sdk-pleos/NaviHelper/initialization-and-release) |
| 조회 | `pleos.car.permission.NAVI_ROUTE`: `get*Info()`, `requestTrip()` | 사용자가 동의한 자기 여정만 읽고 권역·잔여시간 등 최소 파생값을 추천에 사용. 전체 이력·즐겨찾기 조회는 제외. [S22](https://document.pleos.ai/en/docs/pleos-only/connect-sdk-pleos/NaviHelper/declaring-permissions) |
| 목적지·경로 | `requestRoute`, `cancelRoute`, `requestReRoute`, `addWaypoint`, `removeWaypoint`, `requestRouteWithWaypoints`는 `NAVI_ROUTE_SEARCH` | 주차 중, 상호 동의 완료 후 **본인 확인 버튼**으로 공공장소를 경유지에 연결. 최종 목적지를 상대에게 보내지 않는다. [S22](https://document.pleos.ai/en/docs/pleos-only/connect-sdk-pleos/NaviHelper/declaring-permissions) |
| 화면 요청 | `requestNavigationScreen()`는 `NAVI_CUSTOM_MAP` | MVP에서 필요 없으면 해당 권한도 제외한다. 이 API가 제3자 앱에 자유로운 지도 타일·동료 위치 레이어를 제공한다는 뜻은 아니다. [S22](https://document.pleos.ai/en/docs/pleos-only/connect-sdk-pleos/NaviHelper/declaring-permissions) |
| 경유지 포함 요청 | `RouteInfo`, `RequestWaypointInfo`, `RouteWithWaypointsRequest`로 최종 목적지+경유지 전달. 결과 `onRouteStarted`, `onRoutingCompleted`, `onError` | 함수 호출 즉시 약속·경로 성공으로 표시하지 않고 완료/오류를 반영. 기존 최종 목적지를 보존하는 절차와 경유지 수·중복·취소 복구를 실기에서 검증. [S23](https://document.pleos.ai/en/docs/pleos-only/connect-sdk-pleos/NaviHelper/route-with-waypoints) |
| 변화 감지 | `NaviHelperEventListener`; `onDestinationChanged`, `onReRouteEnded`, `onDestinationArrived`, `onTripInfo`, `onCurrentLocationInfo`, `onDestinationInfo`, `onRouteStateInfo`, `onError`; `addListener/removeListener` | 여정 변경 때 기존 추천을 만료하고 다음 주차 시 재확인. 도착 이벤트 하나만으로 인간의 실제 여행 종료·연락처 공개 동의를 확정하지 않는다. 실제 전달 이벤트는 내비 구현에 따라 다르다. [S07](https://document.pleos.ai/en/docs/pleos-only/connect-sdk-pleos/NaviHelper/event-listeners) |

**버전 주의:** 3.0.5는 생성자 좌표 순서가 `latitude, longitude`로 바뀌었고, 목적지·경유지 잔여값은 `remainDistance/remainTime`, 내비 상태는 `NavigationStatus`, 경로 완료는 `onRoutingCompleted`를 사용하도록 안내한다. 예전 예제를 그대로 복사하지 말고 pin한 버전의 시그니처를 확인한다. [S12-KO](https://document.pleos.ai/docs/pleos-only/release-note/sdk-release-note)

**미확인인 세부사항:** `TripInfo/TripSummary/RouteStateInfo` API Reference 주소는 찾았으나 조사 도구가 읽은 페이지 본문에는 모델 필드·단위·nullability가 나타나지 않았다. 따라서 완전한 도로 polyline, 경유지 전 구간 geometry, 잔여시간 단위, 데이터 갱신 주기, 이벤트 보장, 우회 전후 비교 API는 검증되지 않았다. 문서 열람 한계를 API 부재로 단정하지도 않는다. [S24](https://document.pleos.ai/en/docs/pleos-only/connect-sdk-pleos/NaviHelper/navi-helper/ai.pleos.playground.navi.data/trip-info/entry)

**설계 경계:** 6주 MVP는 `공개 활동 권역 + 시간 창 + 관심사 + voice-only/meetup opt-in`을 규칙으로 교집합 계산한다. 장소는 사전에 검수한 공공장소 whitelist 3~5곳이다. 경로 도형을 얻지 못하면 ‘실제 경로 87% 일치’나 ‘정확히 7분 우회’라고 표시하지 않는다. 공개 카드에는 ‘강릉권·오후·카페 60분’처럼 동의한 범위만 쓰며 상대의 내비 지도·실시간 좌표·최종 목적지는 표시하지 않는다.

## 5. 실시간 사람 음성, STT/TTS, AI 대화의 역할 분리

| 층위 | 확인 또는 설계 | 검증 대상 |
|---|---|---|
| 사람↔사람 음성 | **설계:** 별도 미디어 transport, 시그널링 서버, 만료 room token, 릴레이 사용을 검토. STT/TTS SDK가 통화 상대를 연결해주지 않는다. | Pleos 장비의 앱 마이크 취득, 출력 라우팅, echo cancellation, 동시 마이크 점유, 방화벽/UDP/릴레이, 백그라운드·잠금 전환. Pleos 공식 지원 확정 전 라이브 통화 성공으로 주장 금지. |
| Pleos STT | **확인:** `ai.pleos.playground.stt.SpeechToText`; `request/stop`, `ResultListener`; `HYBRID/SERVER/ON_DEVICE`. ON_DEVICE만 쓰면 서버 앱 등록 불필요, HYBRID/SERVER는 My Project 등록 필요. STT는 명령 실행을 제공하지 않는다. [S08](https://document.pleos.ai/en/docs/pleos-only/connect-sdk-pleos/SpeechToText/intro) | 주차 중 짧은 버튼 발화만. `onUpdated(stt, completed)`의 completed=true에서만 설문 구조화를 확정한다. `onReady/onStartedRecognition/onEndedRecognition/onError`와 동일 listener 해제를 처리. [S25](https://document.pleos.ai/en/docs/pleos-only/connect-sdk-pleos/SpeechToText/result-listeners) |
| Pleos TTS | **확인:** `ai.pleos.playground.tts.TextToSpeech`; `initialize`, `addEventListener`, `speak`, `stop`; 세 모드. SERVER는 네트워크 실패 시 on-device로 자동 전환하지 않음. [S09](https://document.pleos.ai/en/docs/pleos-only/connect-sdk-pleos/TextToSpeech/intro) | `onReady/onStart/onDone/onStop/onError`를 사용해 응답 상태를 관리. 사전 녹음 fallback은 실시간 합성으로 표현하지 않는다. [S26](https://document.pleos.ai/en/docs/pleos-only/connect-sdk-pleos/TextToSpeech/event-listeners) |
| 서비스 권한 | **확인:** `pleos.car.permission.STT_SERVICE`, `pleos.car.permission.TTS_SERVICE`를 각각 manifest 선언. 권한 오류는 runtime 상태도 확인. [S27](https://document.pleos.ai/en/docs/pleos-only/connect-sdk-pleos/SpeechToText/declaring-permissions), [S28](https://document.pleos.ai/en/docs/pleos-only/connect-sdk-pleos/TextToSpeech/declaring-permissions) | 이 권한이 별도 WebRTC/raw microphone 권한까지 허용한다고 해석하지 않는다. `RECORD_AUDIO` 등 일반 Android 권한·raw capture 허용은 실제 배포 장비와 공식 지원 답변으로 별도 확정한다. |
| AI 대화 | **설계:** 주차 확인 → 버튼 발화/선택지 → STT → 자체 서버 LLM → 구조/길이/허용ID 검증 → TTS. 질문은 관심사·오늘의 기분·활동 시간 정도로 제한 | 성격·안전성 점수, 사람의 감정 진단, 상대 설득, 자동 매칭 수락은 제외. timeout/잘못된 JSON은 고정 선택지로 전환. 실제 사용자 음성 전체를 기본 녹음·서버 저장하지 않는다. |

STT의 `sendAudio(ByteArray)`는 **ON_DEVICE에서 앱이 공급한 PCM을 인식하는 기능**이다. 사람 간 통화 스트림 SDK라는 근거가 아니다. `completeAudioSend()`로 입력 종료하며 문서의 3,200-byte/100ms는 16kHz·16bit·mono 예시다. [S29](https://document.pleos.ai/en/docs/pleos-only/connect-sdk-pleos/SpeechToText/sending-audio-data)

오디오 재생 전에 `AudioAttributes + AudioFocusRequest`로 포커스를 요청해야 한다. Pleos는 focus 변화 처리도 요구하며 Gleo가 유발한 transient loss에서는 즉시 재생을 멈추도록 안내한다. 제안하는 통화 오디오의 context를 음악이나 내비로 위장하지 않는다. CALL/VOICE_COMMUNICATION 라우팅 등 실제 분류는 지원팀·장비에서 확인한다. 잠금·포커스 상실 시 송신까지 중단하는 것은 앱의 보수적 설계다. [S30](https://document.pleos.ai/en/docs/pleos-only/vehicle-app-developer-guide/audio-focus-development-guide/audio-focus-development)

## 6. Gleo 기능 호출 — 3개 이하, 결과는 7초 안에

**확인:** Gleo Interface는 등록된 App Schema를 바탕으로 LLM이 function call을 생성하고 앱의 callback을 받아 응답하는 구조다. 앱이 Gleo에 임의의 프롬프트를 보내 범용 생성 LLM으로 사용하는 API라는 뜻이 아니다. [S05](https://document.pleos.ai/docs/pleos-only/app-integration-guide/guide/core-concepts)

**확인:** `actionCalls`는 최대 **3개**. `component=activity`는 `startActivity`, `component=service`는 `sendBroadcast` 방식이다. function name은 대문자/밑줄, 설명은 영어, 제한된 parameter type을 사용한다. `required`를 적어도 값이 모두 채워지는 것을 보장하지 않는다. 이 숫자는 한 턴의 tool call 제한이 아니라 스키마에 등록할 기능 목록 제한이다. [S31](https://document.pleos.ai/docs/pleos-only/app-integration-guide/guide/app-capability)

**확인:** `assets/schema.json`과 manifest action filter가 필요하고, 스키마 검토 승인 후 통합이 활성화된다. ADB 또는 앱 마켓 설치 시 스키마를 읽는 절차는 있지만, 이것이 검토 승인을 생략한다는 뜻은 아니다. [S32](https://document.pleos.ai/docs/pleos-only/app-integration-guide/guide/deliver-schema)

**확인:** callback은 `functionName`, `status=success/asking/fail`, 영어 `message`, 선택 `data`와 `mode=voice/beep/silent`. Gleo는 **7초 후 action을 취소**한다고 안내한다. 오래 걸리는 매칭·통화 연결을 그 시간 안에 성공한 것처럼 반환하면 안 된다. `success`는 실제 완료된 로컬 작업에만 사용하고, 누락 인자·확인은 `asking`, 제한·실패는 `fail`로 처리한다. [S33](https://document.pleos.ai/docs/pleos-only/app-integration-guide/guide/action_callback)

**확인 및 문서 불일치:** 예제는 입력을 `ACTION_PARAM` JSON string extra로 받고 결과를 `ai.pleos.playground.intent.action.APP_ACTION_RESPONSE` broadcast에 `packageName`, `response` extra로 보낸다. 같은 페이지 설명에는 key-value를 개별 extra로 넣는다고도 적혀 있다. 입력 구조를 실측해 parser를 확정해야 하며 사용자 ID·목적지·연락처를 broadcast나 callback에 넣지 않는다. [S34](https://document.pleos.ai/docs/pleos-only/app-integration-guide/guide/examples)

**선택 구현(승인 가능할 때만):** `OPEN_TRIP_SETUP`, `READ_TRIP_STATUS`, `END_VOICE_SESSION`의 3개 이하. 각 action은 UI 입력과 같은 주차·권한·세션 검사 함수를 거친다. 주행 중 설정/대화/동의는 거절하고, 안전한 종료는 idempotent하게 처리한다. `READ_TRIP_STATUS`도 현재 허용 상태와 공개 가능한 파생값만 반환한다. 필수 MVP는 직접 UI로 완결되며 Gleo 승인 실패는 `미연동`으로 명확히 표시한다. 승인 기능을 adb broadcast 모의만으로 성공했다고 발표하지 않는다.

## 7. 익명성·여정 종료 규칙의 기술 설계

이 절은 플랫폼이 기본 제공하는 기능이 아닌 **말문이 트립! 자체 설계**다.

- 가입 식별자는 서버 내부 계정과 분리한 일회성 trip pseudonym을 쓴다. 상대에게 공개하는 필드는 별명·선택 관심사·선택 활동·넓은 권역·시간 창뿐이다. 이름·얼굴·전화·SNS·차량번호·VIN/CRN·정확한 출발지·최종 목적지·이동 이력은 상대 payload에 포함하지 않는다.
- `voice-only`를 선택하면 만남 제안·친구 추가를 자동 표시하지 않는다. `optional-meetup`도 기본값은 미동의이며 공개 장소·시간·30/60/90분 활동·취소 가능성을 보고 각자 별도 수락해야 한다. 상대의 거절 이유는 전달하지 않는다.
- 최종 목적지는 가능하면 단말 내에 두고 공개 권역·일정 가능 시간만 파생한다. 현재 경로와 만남 경유지 연결은 본인 단말에서만 수행한다. 서버에 정밀 여정이 꼭 필요해진다면 목적·보관기간·삭제·접근 통제를 다시 설계해야 한다.
- 지도에는 본인 이동과 합의한 공공 만남 장소만 허용한다. 다른 참가자의 정확한 좌표·속도·차량 방향·실시간 ETA는 보여주지 않는다. 소수 인원이 있는 장소·시간도 재식별 단서가 되므로 공개 범위는 최소화한다.
- 종료는 `본인 여정 종료/중단`을 명시적으로 처리하고 방 token·미디어 접근·추가 매칭을 만료시킨다. `onDestinationArrived`는 경유지 도착·목적지 수정·재탐색과 구분해 검증해야 한다. 서버 TTL도 둬 앱 강제종료/네트워크 단절에 방이 영구 유지되지 않게 한다.
- **MVP는 여정 종료 후에도 신원·연락처·정확 목적지를 자동 공개하지 않는다.** 후속 연결 기능을 추가하더라도 여정 종료가 공개 동의를 대신할 수 없다.
- 목소리 자체나 현실에서 만나는 행동에는 식별 단서가 있다. 따라서 ‘완전 익명 보장’이라고 표현하지 않는다. 라이브 음성에서 발화 후 개인정보를 STT로 탐지하는 것만으로 발화를 사전에 차단할 수 없으므로 그런 보장도 하지 않는다. 앱 UI·API에서 연락처 입력/전송을 제공하지 않고 신고·차단·즉시 나가기를 둔다.

보안 공식 근거는 민감 데이터 최소 저장·암호화·로그 노출 방지·HTTPS/TLS·불필요한 권한 제거·외부 component 최소 노출·정식 배포 서명 요구다. 제안한 세부 token/TTL 구조가 Pleos에서 이미 구현돼 있다는 의미는 아니다. [S35](https://document.pleos.ai/en/docs/pleos-only/app-registration-guide/app-security-guide)

## 8. 실제 Pleos UI 참고와 앱 화면 적용

**확인:** 화면은 시스템 status bar, driving view, GNB, application window로 구성된다. 앱은 한 창 또는 두 창에 표시되고 landscape/portrait에 대응해야 한다. 시스템 키보드·패널은 앱 위를 가릴 수 있다. Connect-S는 17/14.6/12.9인치 유형, Connect-W는 더 넓은 유형이다. [S36](https://document.pleos.ai/en/docs/connect/guide/docs-design/getting-started/layout)

**확인:** Connect-S는 두 앱 1:1, 하나 앱 2:0, Connect-W는 2:1 또는 1:2 배치가 안내된다. 앱이 화면에서 밀려도 종료되는 것은 아니다. Connect-W의 동승자측 App Library에서 연 앱이 passenger window에만 실행되는 규칙은 있지만, 이 앱은 혼자 운전하는 사용자용이므로 그 창을 주행 허용 우회로 쓰지 않는다. [S37](https://document.pleos.ai/en/docs/connect/guide/docs-design/getting-started/window)

공식 원문에 포함된 이미지 URL을 확보했다. 아래는 **플랫폼의 실제 공개 가이드 그림·스크린샷 참조**이며 말문이 트립!의 실행 화면이 아니다. 일부 SVG는 조사 도구에서 렌더링하지 못했으므로 구체 dp/색값을 이미지로 검증했다고 주장하지 않는다.

| 용도 | 공식 원문·직접 이미지 | 활용 경계 |
|---|---|---|
| 전체 화면 anatomy | [Display Layout 원문](https://document.pleos.ai/en/docs/connect/guide/docs-design/getting-started/layout), [공식 layout SVG](https://document.pleos.ai/en/assets/images/pleos_connect_deisgnguide_displaylayout_01-e9fac8ec763b8ea5e68aeb709aa8668d.svg) | 시스템 driving view/GNB를 앱 자체 기능처럼 다시 그리지 않는다. |
| Connect-S 창 배치 | [공식 window-policy-1 PNG](https://document.pleos.ai/en/assets/images/window-policy-1-380137ecc779345d4dc94e9ce2a3dc24.png) | 두 창에서 앱 가용 영역이 줄어드는 상황을 디자인한다. |
| Connect-W 창 배치 | [공식 window-policy-2 PNG](https://document.pleos.ai/assets/images/window-policy-2-7cd02739b6c19962f8c20d17b58c805d.png), [window-policy-3 PNG](https://document.pleos.ai/assets/images/window-policy-3-ca0ef4c47bbaf1cb00fdc386d1737f0c.png) | 공개 가이드의 배치 참조. 모든 차량의 픽셀 크기 보장 아님. |
| 기본 내비 창 | [공식 window-policy-4 PNG](https://document.pleos.ai/en/assets/images/window-policy-4-8d75fbd8a827ca9fdb9f02d505ac32a8.png) | 내비와 우리 앱이 별도 앱임을 제안서 목업에서 구분한다. |
| GNB 편집 실제 화면 | [GNB 원문](https://document.pleos.ai/en/docs/connect/guide/docs-design/components/gnb), [공식 gnb_edit PNG](https://document.pleos.ai/en/assets/images/gnb_edit-720361fdd4e40b755a9520b21d3f293d.png) | 시스템 고정 내비·최근 앱·앱 라이브러리 위치 참고. |
| 마이크 설정 참고 | [현재 Emulator 설정 원문](https://document.pleos.ai/en/docs/connect/guide/getting-started/application-development/configure-pleos-connect-emulator), [공식 mic PNG](https://document.pleos.ai/assets/images/portal-mic2-db355066463b2d5a5e134ce66d219b9b.png) | 이미지에는 이전 2.0 환경이 보일 수 있으므로 현재 2.1 요구는 본문으로 확인한다. |

**설계 화면 6개:** ① 주차 확인/개인정보 원칙 ② 설문(voice-only 또는 optional meetup, 가능한 시간, 관심사, 공개 범위) ③ 익명 추천 카드(선택 근거·후보 없음 포함) ④ 주차 중 음성방(자기 mic 상태·나가기·신고·차단) ⑤ 선택형 공공 만남 카드(30/60/90분·각자 수락·본인 내비 확인) ⑥ 잠금/종료(재주차 후 재개 또는 여정 끝내기). 옆 창이 좁아지면 카드 하나와 주 행동 하나 중심의 단일열로 바꾸고, 가로 창은 요약/상세 2열로 확장한다. 목업은 실기 해상도 미정임을 표기한다.

## 9. 에뮬레이터·개발장비·일반 태블릿의 검증 구분

| 환경 | 공개 문서로 확인 | 아직 확인해야 할 것 |
|---|---|---|
| 개발 PC/AVD | minSdk API28+, Gradle8+, Kotlin/Java. API34 Pleos system image 2.1.0, RAM4GB, cold boot. Windows/Linux repository XML 제공. cold boot가 아니면 VHAL 사용 불가라고 안내. [S02](https://document.pleos.ai/en/docs/connect/guide/getting-started/application-development/setup-connect-sdk-emulator), [S38](https://document.pleos.ai/en/docs/connect/guide/getting-started/application-development/configure-pleos-connect-emulator) | 실제 PC GPU·가상화·storage, SDK artifact download, 서비스 연결, 음성 엔진·인증. |
| 차량 상태 모의 | Virtual Console 2.1.0+; gear/brake 등 상태 설정. `adb forward tcp:8088 tcp:8088` 뒤 `http://127.0.0.1:8088/`. [S39](https://document.pleos.ai/en/docs/connect/guide/getting-started/application-development/use-vehicle-emulator) | 각각의 P/D·속도·브레이크 조합이 전달하는 UX flags와 우리 앱의 실제 잠금. |
| 마이크 | Emulator Extended Controls의 Microphone에서 입력 설정. [S38](https://document.pleos.ai/en/docs/connect/guide/getting-started/application-development/configure-pleos-connect-emulator) | PC OS mic 허용, emulator 전달, STT_SERVICE와 raw capture 허용의 차이, 한국어 인식, echo, focus. |
| ADB 설치 | 공식 가이드에 `adb devices`, APK 설치·실행·캡처 절차가 있음. [S40](https://document.pleos.ai/en/docs/pleos-only/vehicle-app-developer-guide/adb-command-reference-guide) | 대여장비에서 developer options/USB debugging이 열려 있는지, PC 허가, install policy, package/signature 조건, 제공 케이블·드라이버. 공개 명령이 장비 관리자 권한을 보장하지 않음. |
| Devbox | 공식 소개는 17인치, 2560×1440, USB 3.0+2.0, Wi-Fi/Bluetooth/GPS/Ethernet/Mic, 앱 마켓 download/update를 소개. [S10](https://pleos.ai/playground/develop?focus=fleet_api) | 실제 지급 모델·OS·서비스 버전, ADB install 허용, 계정, network egress, 마이크 routing, P/D를 줄 인터페이스, navigation seed. |
| 일반 Android 태블릿 | Pleos hardware/service가 있다고 확인할 공식 근거 없음 | 자체 화면·백엔드 테스트 가능 여부를 별도로 검사. Pleos 신호는 mock adapter로만 재현하고 `모의` 표시. Pleos SDK 실증 장비로 주장하지 않음. |
| 배포 빌드 | 제품은 minSdk28+; 보안 가이드는 정식 release certificate와 debugging 비활성화 요구. [S02](https://document.pleos.ai/en/docs/connect/guide/getting-started/application-development/setup-connect-sdk-emulator), [S35](https://document.pleos.ai/en/docs/pleos-only/app-registration-guide/app-security-guide) | 대회용 debug APK 허용 여부, 최종 제출 APK/AAB 형식, 조직 서명·keystore·lineage 절차, 배포·업데이트 경로는 담당자/최신 제출지침으로 확정. |

폼팩터는 공식 FormFactorConsole + Host Display Bridge로 portrait/landscape·display preset·dp/DPI/px를 확인할 수 있다. Go1.22+, ports8095/8096, 별도 Emulator window가 필요하고 Android Studio embedded/headless에서는 virtual display가 보이지 않는다고 안내한다. 이 검증은 실물의 터치거리·반사·마이크·차량 오디오 검증을 대신하지 않는다. [S41](https://document.pleos.ai/en/docs/pleos-only/app-test-guide/form-factor-test-guide)

실제 장비 인수 때 받아야 할 답은 **장비명/OS image/SDK service versions, ADB·설치·서명 정책, 네트워크 사용법 및 외부 HTTPS/미디어 relay 허용, mic privacy/권한/audio route, 차량 상태 신호·UX restriction 재현법, 내비/Gleo account·service 초기 상태**다. 지금은 어느 항목도 성공했다고 표시하지 않는다.

## 10. 6주 개발 범위 — 문서 검증에서 작동 증거까지

아래는 계획·목표이며 성능 실적이 아니다. 2~3인 팀, Android 앱 1개·최소 백엔드 1개, parked 사용자 2명·단일 여행 권역을 가정한다. 실사용 모집·운영 확장은 제외하고 참가자 동의하의 통제된 테스트를 한다.

| 주차 | 범위·산출물 | 통과 기준 / 실패 시 범위 조정 |
|---|---|---|
| 1주 | 계정·SDK pin·Emulator2.1 설치; 대여장비 사양 확인; UX restriction adapter; 마이크/외부 HTTPS/짧은 음성 loopback spike | 실제 장비 또는 AVD의 SDK 초기화·권한·callback 로그와 화면을 기록. P→D·제한 모름에서 입력/녹음이 잠겨야 함. raw mic 통화 경로 불가면 사람 음성은 별도 모바일 테스트 또는 녹음 mock이라고 명시하고 차량 라이브 통화 완료로 주장하지 않음. |
| 2주 | 익명 trip ID·여정 시작/종료·survey 4단계·공개 payload schema·규칙 추천(voice-only/meetup 분리) | 적합 후보/후보 없음/모드 불일치/차단 상대 제외 테스트. 상대 API 응답·로그·분석 event에 이름/연락처/최종 목적지/좌표가 없어야 함. 설문은 parked에서만 변경 가능. |
| 3주 | 주차 중 1:1 사람 음성방(실기 지원 시), mute/end/report/block; AI icebreaker는 별도 경로 | 2개 클라이언트에서 join/leave·token expiry·재연결. 제한 이벤트 후 mic capture/미디어 송신·재생 중단을 확인. 녹음 기본 off. peer IP 노출·relay 정책도 확인. 실패 시 기능 상태를 미지원/모의로 표시하고 원인 기록. |
| 4주 | NaviHelper 자기 여정 조회·변경 이벤트; 공공장소 3~5곳·30/60/90분 optional meetup·상호 동의·본인 내비 연결 | 한쪽만 수락해 장소 공유/경로 변경되지 않아야 함. 두쪽 수락 후에도 본인 확인 전 route request 없음. route 완료/오류가 상태에 반영. 목적지 변경 시 추천 만료, 상대에게 최종 목적지 노출 없음. geometry 미확보이면 권역 추천을 유지. |
| 5주 | AI survey 구조화/질문 생성 최소 기능, STT/TTS 가용 모드 연결, timeout/오프라인 fallback; Gleo 선택 연동 | 잘못된 JSON·미허용 장소 ID·중복 요청·timeout을 거절. 사용자 의사·주차 잠금은 LLM과 무관하게 적용. Gleo 승인된 경우에만 3개 이하 action과 7초 callback을 실증. 승인 전 기능은 선택 UI로 완결. |
| 6주 | FormFactorConsole·실물 parked UX·오디오 포커스·강제종료·망 단절·익명성 회귀; 시연 패키지/제출문서 | 아래 acceptance 시나리오 전부 실행, 장비별 결과·미지원·모의 여부 기록. 핵심 실패를 영상 편집으로 감추지 않음. 출시용 계정·서명·정책 심사 통과와 공모전 prototype 시연을 구분. |

### 최종 acceptance 시나리오

1. **설문 분기:** voice-only A는 60분 meetup B와 자동으로 만남 매칭되지 않는다. 관심사·시간이 맞지 않으면 후보 없음이 정상 결과다.
2. **주행 잠금:** 설문·AI 발화·사람 음성·만남 선택 각각에서 P→D, 제한 활성, 신호 연결 단절을 주입한다. 다음 처리 사이클에 input/capture/send/playback을 중단하고 재주차 후 명시적 재개 전까지 재시작하지 않는다. event 수신→중단 지연은 실제 측정해 기록한다. 목표값은 장비 측정 후 정한다.
3. **익명 payload:** 수동 검사뿐 아니라 response schema allowlist로 identity/contact/finalDestination/exactPeerLocation 필드 유출을 막는다. 로그·crash report·Gleo callback·push event도 검사한다. 이름 등을 사용자가 말하는 현실의 식별 가능성은 별도 한계로 설명한다.
4. **음성 품질:** parked 2명, mic 거절/철회·상대 종료·일시 네트워크 단절·포커스 상실·앱 background에서 mute/end 상태가 사실과 일치한다. 실제 음성 전송과 사전 녹음 시연을 분리해 기록한다.
5. **만남 동의:** 각자 opt-in + 장소/시간/길이 상호 수락 + 본인 내비 확인의 순서가 필요하다. 중복 이벤트·뒤늦은 수락·취소된 방의 route 요청을 거절한다. 만남 거절이 identity 공개나 불이익으로 이어지지 않는다.
6. **Navi 진실성:** init failure·permission error·내비 없음·조회 null·route error를 사용자 상태로 반영한다. 실제 callback을 받기 전 route success로 표시하지 않는다. 좌표 위도/경도 순서를 검증한 known point로 확인한다.
7. **종료:** 여정 완료/중단·TTL·force stop 이후 상대 token으로 다시 join/read하지 못한다. 새 여정에 이전 매칭·정밀 경로·mic 상태를 상속하지 않는다. 여행 종료가 개인정보 공개를 자동 승인하지 않는다.
8. **화면:** 대표 12.9/14.6/17인치 preset 및 portrait/landscape에서 주요 동의·종료 버튼, 시스템 바·키보드 overlap, resize 중 상태 유지 검사. 실기 화면이 다르면 실제 dp를 기준으로 조정한다.

## 11. 제안서에 쓸 수 있는 기술 문장

> 말문이 트립!은 Pleos Connect의 주차·UX 제한 상태를 확인한 뒤 설문, 익명 대화와 만남 선택을 제공한다. NaviHelper의 자기 여정 정보와 변경 이벤트는 추천의 유효성 확인 및 본인이 승인한 공공장소의 경유지 연결에 활용할 계획이다. 사람 간 음성 전송과 생성형 AI는 별도 서비스 계층으로 구현하며, Gleo는 승인되는 경우 앱 기능을 여는 음성 입력으로 연동한다. 주행 중 소셜 대화는 MVP에서 제공하지 않는다. 상대에게 신원·연락처·최종 목적지·정확한 실시간 위치를 노출하지 않으며, 공개 SDK 문서와 참가 계정·장비의 실제 사용 가능 범위는 개발 첫 주에 나누어 검증한다.

위 문장은 구현 계획이다. “차량 데이터 연동 완료”, “실기 음성 연결 검증 완료”, “Gleo 탑재 승인”, “정확한 경로 겹침 계산”으로 바꿀 때는 각각 실제 증거가 필요하다.
