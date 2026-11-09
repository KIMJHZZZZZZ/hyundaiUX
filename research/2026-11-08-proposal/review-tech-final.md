# 최종 기술 수정 확인 — PASS

범위: `review-tech-v1.md`의 두 지적 사항, 버전 표를 대체한 두 문단, 최신 architecture.png와 재생성 DOCX의 일치만 확인했다. 재조사·SDK 실행·앱 설치·전체 문서 재검수는 하지 않았다. root 파일은 수정하지 않았다.

검수한 DOCX: `output/2026-11-08_말문이트립/말문이_트립_02_서비스_기획서.docx`

- DOCX SHA-256: `c5725a4e18f83c2c153107186babe949ed49fe34e819a1493baccf68065f999f`
- 최신 architecture.png SHA-256: `674b6fcb660c4c521b0fca7efb8e83129d180a6a065d040e7cc1f4e06e16b307`
- DOCX `word/media/image33.png`가 위 architecture asset과 byte hash 일치.

## 수정 확인

1. **목적지 경계: PASS.** 현재 script와 DOCX 실제 XML은 자체 매칭·AI·미디어 서버 및 상대에게 정밀 최종 목적지를 보내지 않는다고 한정한다. 기존 목적지를 포함한 `RouteInfo`가 내비 서비스에 전달된다는 설명이 추가됐다. 최신 architecture도 “단말 안에서만 처리” 대신 자체 매칭 서버와 상대에게 미전송이라는 범위로 바뀌었다. 본문과 그림 사이에 새 모순이 없다.
2. **STT/TTS 서비스 권한: PASS.** 현재 script와 DOCX API 표 모두 `pleos.car.permission.STT_SERVICE`, `pleos.car.permission.TTS_SERVICE`를 포함한다. `RECORD_AUDIO`가 SDK 서비스 권한을 대신하지 않는다는 설명도 확인했다.
3. **버전 표 대체 문단: PASS.** NaviHelper 3.0.5, STT/TTS 3.3.1, Vehicle 한국어 2.3.2/영어 2.3.1, FusedLocation 1.1.3/1.1.2 차이와 실제 artifact·장비 검증 조건이 보존됐다. SDK 신청 안내와 릴리스 기록의 차이, FusedLocation 선택 범위도 유지됐다. 별도 문단에 Emulator 2.1.0의 LLM SDK 지원 종료, Gleo 승인 기능 호출, 별도 LLM/준비 질문, 음성 SDK fallback과 실제 사람 통화 구현의 구분이 남아 있다.

이 수정 범위에 남은 기술 지적 사항은 없다. 이 PASS는 기획 문서의 정정 확인이며 SDK·장비 동작 성공 판정이 아니다.
