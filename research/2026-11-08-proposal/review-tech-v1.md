# 서비스 기획서 기술 검수 v1

검수 대상: `tmp/proposal-2026-11-08/build_proposal.py`, 최종 DOCX의 실제 `word/document.xml` 3·5절과 표, DOCX에 포함된 architecture.png, 새 S05B/S06B/S10/S12/S13/S13B/S14/S15/S16/S16B/S21 및 portrait 이미지. 파일 수정은 하지 않았다.

확인한 DOCX SHA-256: `a0cc4b806b944c45902810d62caedb40383be076ecc1ec39caae924ca37ddd82`. DOCX의 `word/media/image33.png`가 출력 폴더의 architecture.png와 SHA-256이 일치했다. 검수는 문서·화면 시안의 일관성에 한하며 SDK 실행 시험이 아니다.

## 수정할 실질 이슈 2건

### [P2] 최종 목적지의 비전송 경계를 정확히 한정하기

- 위치: `build_proposal.py` 약 336행 「백엔드와 익명 데이터의 개발 범위」의 “최종 목적지는 MVP에서 단말 안에 두고”, architecture.png 양쪽의 “목적지·경로는 단말 안에서 처리”.
- 문제: 앱의 매칭 서버·상대에게 목적지를 보내지 않는 설계와, 내비게이션이 목적지·경로를 단말 내부에서만 처리한다는 보장은 서로 다르다. 후자는 공개 문서로 확인하지 않았다. 또한 공식 `requestRouteWithWaypoints()`는 **최종 목적지 `RouteInfo`와 경유지 목록**을 `RouteWithWaypointsRequest`로 내비에 전달하는 API다. 목적지를 아예 읽거나 전달하지 않으면서 기존 여정을 보존하는 구현으로 오해할 수 있다.
- 수정 문구 제안: “최종 목적지와 정밀 경로는 자체 매칭·AI·미디어 서버 및 상대에게 보내지 않는다. 경유지를 추가할 때는 본인 단말에서 현재 목적지를 확인해 기존 목적지와 합의한 공공 경유지를 내비 서비스에 요청한다. 내비 서비스 자체의 통신·처리는 해당 플랫폼 정책을 따른다.”
- architecture 양쪽 문구 제안: “정밀 여정은 매칭 서버·상대에게 미전송” 및 “경유지 요청은 본인 단말에서 내비 서비스로”. 가운데 백엔드의 “정확한 최종 목적지는 전달·저장하지 않음”은 그대로 유지해도 된다.
- 출처: [공식 경유지 포함 요청](https://document.pleos.ai/en/docs/pleos-only/connect-sdk-pleos/NaviHelper/route-with-waypoints). 표에 있는 기존 목적지 보존·위경도 순서·callback 결과 검증은 적절하다. 목적지가 없는 상태·조회 불가·내비 오류에서는 경유지 요청을 중단하는 fallback도 한 문장으로 명시하면 구현 조건이 완결된다.

### [P2] STT/TTS API 행에 각 서비스 권한을 명시하기

- 위치: `build_proposal.py` 약 329행, 「사용할 API와 권한의 구체적 매핑」의 「AI 질문과 짧은 입력」 행. 실제 DOCX 표도 동일하다.
- 문제: 이 표는 API와 필요한 권한의 매핑인데 이 행에는 STT/TTS 메서드만 있고 필수 Pleos 서비스 권한이 빠져 있다. 음성 통신 행의 `android.permission.RECORD_AUDIO`가 Pleos Speech Service 권한도 대신하는 것처럼 읽힐 수 있다.
- 추가할 문자열: `pleos.car.permission.STT_SERVICE`, `pleos.car.permission.TTS_SERVICE`.
- 확인 조건: 해당 SDK를 실제 쓰는 build에서 각 manifest 권한과 서비스 초기화·권한 오류를 검증한다. `HYBRID/SERVER`를 쓰면 앱 등록/서버 연결 조건도 별도 확인하며, 녹음 질문·버튼 설문 fallback은 구분한다.
- 출처: [STT 권한](https://document.pleos.ai/en/docs/pleos-only/connect-sdk-pleos/SpeechToText/declaring-permissions), [TTS 권한](https://document.pleos.ai/en/docs/pleos-only/connect-sdk-pleos/TextToSpeech/declaring-permissions).

## 이번 패스에서 재확인한 범위

기존 UI 지적은 새 시안에 반영됐다: 내비 선택 동의·수동 권역 선택(S05B), 마이크 사전 안내(S06B), 송신 상태·음소거(S10), 만남 의사와 장소·시간 확정 분리(S12/S13/S13B), 주행 시 마이크·송수신 중단(S14), 구체 재확인 시각(S15), 휴대폰 코드 확인(S16), 만남 진행·종료·신고(S16B), 별도의 여행 종료·접근 만료(S21). 세로 시안은 모의 UI 표기가 있다.

3·5절은 P와 UX 제한을 별도로 확인하고 UNKNOWN·신호 단절을 잠그며, 최신 AAOS 구독 API와 API34의 차이, WebRTC 권한과 실기 호환의 차이, TURN relay, LLM SDK 지원 종료와 선택 Gleo 승인, install 계획과 실제 검증 미완료를 구분하고 있다. 설치·통화·SDK 성공 실적이나 주행 소셜 대화를 이미 검증했다는 표현은 발견하지 못했다. 접수/PT 일정은 root가 별도 확인한 전제를 따랐으며 이 검수에서 재조사하지 않았다.
