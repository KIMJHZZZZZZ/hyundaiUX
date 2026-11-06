# 나만의 AI 차량 에이전트 — 차량 다마고치·동반자 벤치마크

조사일: 2026-11-06 · 목적: 신규 기획에 앞서 유사 사례와 기존 기능의 중복 범위를 파악한다.

## 1. 먼저 확인한 결론

**차량 상태를 캐릭터의 감정으로 표현하거나, 함께 이동하며 캐릭터를 키우는 구상은 이미 여러 형태로 공개되어 있다.** 현대차 수상작을 기준으로 공개 개발 프로젝트 2개, 양산 차량의 동반자 기능 3개, 과거 콘셉트카 2개, 운전 행동의 성장 보상 사례 1개를 비교했다. 아래 사실과 출처가 근거이며, 차별화에 대한 평가는 조사자의 해석이다.

가장 먼저 볼 대상은 다음 세 곳이다.

- **차마고찌(sj-park-kr)**: 육성·꾸미기·추억 축적이 어디까지 이미 구현 대상으로 잡혀 있는지 비교하기 좋다. [개발자 README](https://github.com/sj-park-kr/appdevchallenge-apk/blob/main/README.md)
- **카마고치(jwlee1008)**: 차량 상태에 반응하는 펫과 운전 코칭·차량 제어의 결합을 비교하기 좋다. [개발자 README](https://github.com/jwlee1008/carmagotchi/blob/main/README.md)
- **NIO NOMI**: 실제 차량에서 동반자가 편의 기능을 수행하는 방식을 비교하기 좋다. [ET5 공식 매뉴얼](https://www.nio.com/cdn-static/www/user-instructions/en_EU/ET5/index.html)

## 2. 기준점: 현대자동차 우수작 ‘차마고치’

현대차의 2026-10-08 공식 소개에서 확인되는 범위는 **주유·충전 상태와 기어 상태를 활용해 차량 관리를 동반자 키우기 게임으로 바꾸는 아이디어**다. 당시 우수작 16개는 아이디어 단계이며, 실제 서비스 개발 가능성과 출시 여부를 검토한다고 명시되어 있다. 이 자료로 출시·실차 적용을 단정할 수 없다. [현대차 공식 소개](https://www.hyundaimotorgroup.com/ko/story/hyundai-motor-company-pleos-connect-app-idea-contest)

따라서 기본적으로 겹치는 영역은 ‘차량 에너지·운행 상태 → 펫의 상태 → 돌봄과 애착’이다. 반면 장기 대화 기억, 개별 운전자 학습, 자유 대화, 외부 서비스 실행은 이 공식 설명만으로 확인되지 않는다.

**이름이 비슷한 아래 GitHub 프로젝트 2개를 이 수상작의 공식 구현 또는 동일 제안자의 작업으로 연결할 근거는 확인하지 못했다.** 별개의 공개 사례로 취급한다.

## 3. 벤치마크 비교표

‘미확인’은 이번에 읽은 출처에서 확인하지 못했다는 뜻이며, 제품 전체에 해당 기능이 없다는 뜻은 아니다.

| 사례 | 공개·제공 단계 | 확인된 핵심 기능 | ‘나만의’ 경험을 만드는 방식 | 분석할 포인트 |
|---|---|---|---|---|
| [카마고치 — jwlee1008](https://github.com/jwlee1008/carmagotchi) | 공모전 출품 프로토타입으로 소개 | 운전·환경 센서 반응, 표정·복장, 음성 코칭, 공조 등 제어 호출, 운전 성적표 | 운전 행동과 차량 상태가 펫 반응을 바꿈 | 펫을 통한 차량 상태 전달과 개입 |
| [차마고찌 — sj-park-kr](https://github.com/sj-park-kr/appdevchallenge-apk) | 공개 개발 프로젝트 | 부화·성장·교감·꾸미기, 길동무 도감, 장소 도장, 추억 앨범, 공유 카드 | 함께한 날짜·이동 경험·저장된 추억·외형 조합 | 지속 사용과 개인별 이력 |
| [NIO NOMI](https://www.nio.com/cdn-static/www/user-instructions/en_EU/ET5/index.html) | 양산 차량의 공식 매뉴얼에 기능 기재 | 탑승 인사, 음성 호출, 공조·창문·조명·내비·미디어 제어 | 차량 안에서 계속 만나는 동반자 | 캐릭터가 실제 일을 수행하는 경험 |
| [MINI Spike](https://faq.mini.com.au/s/article/Intelligent-Personal-Assistant-MINI-Spike-Benefits-NqMIq) | OS 9·Connected 패키지 등 조건부 제공 | 불도그의 표정·동작·감정, 습관 학습과 상황별 기능·설정 예상 | 사용 습관에 따른 적응 | 감정 표현과 실용적 개인화의 결합 |
| [smart Companion](https://media.smart.com/en-CEU/260668-smart-offers-optimizations-with-free-over-the-air-update/) | 유럽 #1·#3 OTA 1.4.0 제공 사례 | 여우·치타 선택, 움직임·정적 표시 선택, 선택값 저장 | 선호 캐릭터와 표시 방식 선택 | 캐릭터 선택과 성장의 차이 |
| [Toyota × Sony pod](https://media.toyota.co.uk/future-shock/) | 2001년 콘셉트카 | 운전·생체 신호 반응, 얼굴 색·꼬리 등 감정 표현, 선호·습관 학습 구상 | 차 자체가 관계를 맺는 존재로 표현됨 | 차량 의인화의 오래된 선행 사례 |
| [Toyota LQ / Yui](https://global.toyota/en/newsroom/corporate/30063126.html) | 2019년 콘셉트카 발표 | 운전자 감정·각성 상태에 맞춘 음성·시트·조명·공조·향기·음악 연동 | 사람의 선호와 필요를 배우고 반응 | 감정 인식에서 공간의 반응으로 연결 |
| [Nissan LEAF Eco Tree](https://www.nissan-global.com/EN/INNOVATION/TECHNOLOGY/ARCHIVE/EV_IT/) | 과거 LEAF 기술의 공식 아카이브 | 친환경 운전 결과를 나무 성장으로 표현, 운전·전비·나무 이력 조회 | 자신의 운전 결과가 누적되는 시각적 보상 | 행동 변화와 성장 보상의 연결 |

## 4. 기존 기능 상세 분석

### 4.1 카마고치 — 운전 행동에 반응하는 펫

**확인한 기능:** README는 승차감·집중력·방어운전 평가와 온도·환기·소음·와이퍼·에너지 상태의 결합을 설명한다. 평상시에는 표정·복장으로 반응하고, 특정 조건에서는 음성 안내와 공조·시트·열선·조명 제어를 실행하도록 구성한다. 도착 시 운전 성적표를 제공한다. [README](https://github.com/jwlee1008/carmagotchi/blob/main/README.md)

**코드에서 확인한 범위:** ViewModel에는 환경·운전 이벤트에 따른 상태 전환, 정해진 음성 문장, 제어 계층 호출이 있다. 에너지 잔량 20% 이하의 배고픔 표현과 10% 이하의 음성 안내도 조건문으로 구현되어 있다. 확인한 로직은 규칙 기반이며, 해당 파일만으로 자유 대화·장기 학습의 존재를 입증할 수 없다. [상태·개입 코드](https://github.com/jwlee1008/carmagotchi/blob/main/app/src/main/java/ai/pleos/carmagotchi/domain/CarmagotchiViewModel.kt)

**분석:** ‘운전을 거칠게 하면 펫이 힘들어함’, ‘비가 오면 우비’, ‘배터리가 부족하면 배고픔’, ‘도착 후 운전 평가’는 직접적인 중복 후보다. README의 개입 비율·가중치·임계값은 개발자의 설계값이며 검증된 안전·의학 기준으로 취급하지 않는다. APK 실행이나 실차 제어 성공은 이번 조사에서 검증하지 않았다.

### 4.2 차마고찌 — 함께한 경험이 쌓이는 차량 펫

**확인한 기능:** 개발자는 부화·교감·성장·꾸미기, 도감·앨범·공유 카드와 차량 신호 연동을 설명한다. 주행·날씨·동승·충전 경험이 기록으로 남고, 상세 화면은 P단에서 사용하며 주행 중 숨긴다고 명시한다. 기억의 기기 내 암호화 저장과 장소 정보 삭제 기능도 설명되어 있다. [README](https://github.com/sj-park-kr/appdevchallenge-apk/blob/main/README.md)

**코드에서 확인한 범위:** 알·아기·어린이·어른·단짝 성장 단계, 함께한 날짜와 애정 기반 성장 표시, VIN 해시 기반 외형 조합, 이벤트·추억 기록 로직을 확인했다. [성장 코드](https://github.com/sj-park-kr/appdevchallenge-apk/blob/main/app/src/main/java/com/carmagotchi/app/domain/Growth.kt), [상태 엔진](https://github.com/sj-park-kr/appdevchallenge-apk/blob/main/app/src/main/java/com/carmagotchi/app/domain/StateEngine.kt)

Gleo 응답에는 기분·거리·감사 기능이 정의되어 있다. 확인한 앱 측 응답은 상태와 조건에 따라 준비된 대사를 선택한다. 저장된 여행 추억은 존재하지만, 이를 생성형 대화의 장기 기억과 동일하게 볼 수는 없다. [대사 선택](https://github.com/sj-park-kr/appdevchallenge-apk/blob/main/app/src/main/java/com/carmagotchi/app/domain/Dialogue.kt), [Gleo 응답](https://github.com/sj-park-kr/appdevchallenge-apk/blob/main/app/src/main/java/com/carmagotchi/app/gleo/GleoAnswers.kt)

**분석:** ‘내 차만의 외형’, ‘함께 성장’, ‘여행 기억’, ‘장소 수집’, ‘음성으로 펫 상태 묻기’까지 이미 비교해야 한다. 단순히 기억 기능을 추가했다는 설명만으로는 차이가 선명하지 않다.

### 4.3 NIO NOMI — 실제 일을 수행하는 차량 동반자

**확인한 기능:** ET5 매뉴얼에는 탑승 인사, 음성 호출, 작업 종료 후 대기 전환이 기재되어 있다. 명령 예시는 공조, 조명, 시트 열선, 창문, 미디어, 전화, 충전소·배터리 교환소 검색 등을 포함한다. [ET5 공식 매뉴얼](https://www.nio.com/cdn-static/www/user-instructions/en_EU/ET5/index.html)

NIO의 현재 기술 소개는 NOMI Intelligence 4.0, NOMI GPT 기반 개인화, 여러 탑승자와의 대화 및 여러 명령 처리를 설명한다. 이 최신 소개와 구형 ET5 매뉴얼의 기능을 모든 차종·지역에서 동시에 제공되는 하나의 사양으로 합치지는 않았다. [NIO 기술 소개](https://www.nio.io/innovation)

**분석:** 캐릭터와 대화하고 차를 조작하는 경험은 이미 양산 차량의 비교 대상이다. 반면 확인한 자료만으로 먹이·레벨·진화 중심의 육성 게임을 주장할 근거는 없다. 사용자는 펫을 돌보기보다 동반자에게 일을 맡기는 쪽에 가깝다. 효과·만족도·장기 이용률은 별도로 확인하지 않았다.

### 4.4 MINI Spike — 동물 캐릭터를 입힌 개인 비서

**확인한 기능:** MINI 공식 FAQ는 불도그 형태의 Spike가 음성 명령에 표정·동작·몸짓으로 반응하고 호기심·즐거움·집중 등의 감정을 표현한다고 설명한다. 개인 습관을 배우고 상황에 맞는 기능과 설정을 예상한다고 명시한다. OS 9와 Connected 패키지 등 적용 조건이 있다. [공식 FAQ](https://faq.mini.com.au/s/article/Intelligent-Personal-Assistant-MINI-Spike-Benefits-NqMIq)

공식 차량 소개에는 음성으로 내비·전화·라디오·온도를 조작하고 날씨를 묻거나 간단한 대화·농담을 하는 기능이 소개되어 있다. [MINI 디지털 경험](https://www.mini.com.sg/en_SG/home/range/all-electric-mini-cooper/digital-experience.html)

**분석:** ‘귀여운 동물형 AI + 차량 제어 + 습관 기반 개인화’도 기존 영역이다. 다만 공식 설명에 있는 습관 학습을 캐릭터의 육성·진화나 무제한 장기 대화 기억으로 확대해서 해석하지 않는다. 캐릭터가 어떤 요청을 듣고 처리하는지 드러내는 표현을 비교하기 좋다.

### 4.5 smart Companion — 내 취향의 동반자를 선택

**확인한 기능:** 2024-07-05 유럽 공식 발표는 OTA 1.4.0으로 smart #1·#3의 아바타를 여우 또는 치타로 선택하고, 애니메이션 또는 정적 이미지로 표시하며, 선택을 저장할 수 있다고 설명한다. [공식 업데이트 발표](https://media.smart.com/en-CEU/260668-smart-offers-optimizations-with-free-over-the-air-update/)

**분석:** 고를 수 있는 외형과 움직임 설정만으로도 소유감을 만드는 사례다. 다만 이 발표에서 성장·육성·추억 앨범·장기 대화 기억은 확인되지 않는다. ‘나만의 캐릭터’가 외형 선택을 뜻하는지, 사용자를 배우는 존재를 뜻하는지 분리해야 한다. 움직임을 끌 수 있다는 점은 차내 캐릭터 표현의 강도를 사용자가 조절하는 참고점이다.

### 4.6 Toyota × Sony pod — 차 자체를 반려 존재로 표현

**확인한 기능:** 2001년 공식 발표의 콘셉트카다. 조향·가감속의 부드러움으로 운전 숙련도를 가늠하고, 평소와 다른 운전·맥박·땀 등의 신호로 조급함을 파악해 주의를 권하는 구상이다. 얼굴의 색, 눈물, 꼬리 움직임 등으로 감정을 표현하고 관계가 진행되면 운전자의 선호·습관을 학습한다고 설명한다. [Toyota 공식 발표](https://media.toyota.co.uk/future-shock/)

**분석:** ‘차를 돌보면 정서적 반응을 돌려주는 관계’는 오래된 차량 의인화 주제다. 새 AI 기술로 구현 범위가 달라질 수 있지만, 차가 살아 있는 것처럼 반응한다는 발상 자체만으로 신규성을 주장하기는 어렵다. 양산 서비스나 현대적인 생성형 AI의 구현 사례로 분류하지 않는다.

### 4.7 Toyota LQ / Yui — 사람을 배우고 차량 공간으로 반응

**확인한 기능:** 2019년 LQ 콘셉트카 발표는 Yui가 운전자의 감정·각성 상태와 선호에 맞춰 음성, 시트, 조명, 공조, 향기 등으로 반응하고, 주행 환경에 따라 음악과 관심 정보를 제공한다고 설명한다. 사전 스마트폰 앱 입력으로 관심·선호를 제공하는 체험 계획도 발표했다. [Toyota 공식 발표](https://global.toyota/en/newsroom/corporate/30063126.html)

**분석:** 표정 변화에서 더 나아가 차량 공간 전체가 사용자를 위해 반응하는 에이전트의 참고 사례다. ‘피곤함 감지 → 말 걸기·시트·공조 연동’ 역시 선행 구상이 있다. 해당 발표는 콘셉트와 당시 계획의 근거이며, 현재 양산 제공이나 효과 검증의 근거는 아니다.

### 4.8 Nissan LEAF Eco Tree — 운전 결과를 성장 보상으로

**확인한 기능:** Nissan 공식 기술 아카이브는 친환경 운전의 결과를 나무 성장으로 보여주고, 운전 이력·평균 전비·전력 소비 순위와 나무 이력을 컴퓨터·휴대전화에서 확인하는 기능을 소개한다. [Nissan 공식 기술 아카이브](https://www.nissan-global.com/EN/INNOVATION/TECHNOLOGY/ARCHIVE/EV_IT/)

**분석:** 캐릭터 대화나 AI 없이도 ‘실제 운전 → 성과 가시화 → 성장 결과 확인’이라는 반복 구조가 성립한다. 차량 펫을 만들 때 성장의 근거가 단순 주행량인지, 원하는 행동의 개선인지 비교하는 데 유용하다. 과거 기술 사례이므로 현재 NissanConnect의 모든 지역에서 계속 지원된다고 해석하지 않는다.

## 5. 기능별 중복 범위

아래는 앞 절의 확인 결과를 다시 묶은 비교다. 기능의 효과나 완성도가 같다는 의미는 아니다.

| 구상 중인 기능 | 이미 확인한 유사 사례 | 현재 판단 |
|---|---|---|
| 주유·충전 상태를 펫과 연결 | 현대차 차마고치, jwlee1008, sj-park-kr | 기존 핵심 구조와 직접 겹침 |
| 연료·배터리가 줄면 배고픈 펫 | jwlee1008, sj-park-kr | 배고픔 표현도 공개 코드에서 확인 |
| 와이퍼·날씨에 따른 옷·반응 | jwlee1008의 우비, sj-park-kr의 날씨 경험 | 환경 반응만으로는 차이가 약함 |
| 거친 운전으로 펫이 힘들어함·평가 | jwlee1008 | 운전 코칭 결합도 이미 비교 대상 |
| 함께 지낸 시간에 따른 성장 | sj-park-kr | 알→성장 단계만으로는 차이가 약함 |
| 외형 꾸미기·내 캐릭터 선택 | sj-park-kr, smart Companion | 외형 개인화가 이미 존재 |
| 장소 도장·여행 추억·앨범 | sj-park-kr | 기억의 단순 축적만으로는 차이가 약함 |
| 캐릭터와 음성으로 이야기·차량 조작 | NIO NOMI, MINI Spike | 양산 차량 수준의 비교가 필요 |
| 사용 습관에 맞춘 기능 예상 | MINI Spike의 공식 설명 | ‘습관 학습’이라는 표현 자체로 차별화하기 어려움 |
| 상태에 맞춘 공조·시트·조명 반응 | jwlee1008, Toyota Yui | 제어 대상이 많다는 것만으로 차이가 생기지는 않음 |
| 좋은 운전이 성장 보상으로 이어짐 | Nissan LEAF Eco Tree | 행동과 성장의 연결도 선행 사례 존재 |

## 6. ‘나만의 AI’라고 할 때 구분할 네 가지

다음은 위 기능 비교에 대한 **조사자의 해석**이다.

1. **외형의 개인화:** 내가 동물·이름·의상을 고른다. smart와 공개 펫 앱이 참고점이다.
2. **상태와 성장의 개인화:** 내 차의 상태·경험으로 표정과 성장 단계가 바뀐다. 두 공개 펫 앱이 참고점이다.
3. **기억의 개인화:** 나와 함께한 사건을 저장하고 이후에 다시 활용한다. 여행 앨범의 사건 기록과 생성형 대화 기억은 별도로 평가해야 한다.
4. **행동의 개인화:** 사용자에 맞춰 적절한 도움을 선택하고 실제 기능을 수행한다. NOMI·Spike·Yui를 비교해야 한다.

이 구분으로 보면 **‘캐릭터를 만들고 충전·운전에 반응시키는 것’과 ‘나를 이해하고 맡긴 일을 수행하는 에이전트’ 사이에 어떤 경험을 더할지**가 다음 기획의 핵심이다.

이번에 확인한 자료에서는 사용자가 맡긴 개인 목표를 장기간 관리하고, 실행 결과를 확인해 다음 행동까지 바꾸는 전체 흐름이 충분히 드러나지 않았다. 이는 추가 조사할 차별화 가설이지, 시장에 그런 기능이 전혀 없다는 결론은 아니다. 지금 단계에서는 새로운 기능안을 확정하지 않는다.

## 7. 조사 범위와 한계

- 기존 로컬 자료의 외부 검토 기록과 링크를 출발점으로 삼고, 제조사 공식 발표·FAQ·매뉴얼 및 개발자 공개 저장소를 다시 확인했다.
- 제조사 기능은 서로 다른 국가·차종·소프트웨어 버전에 해당한다. 최신 기술 소개와 과거 매뉴얼을 합쳐 모든 차량의 공통 사양으로 제시하지 않았다.
- GitHub 2개는 README와 일부 핵심 소스만 읽었다. 앱 빌드·APK 설치·에뮬레이터·실차 실행·전체 코드 감사는 하지 않았다. 코드 존재와 실사용 검증을 구분한다.
- sj-park-kr의 `docs/PRD.md`는 열어 보니 차량 운행기록부 TrueLog라는 다른 주제의 문서였다. 이 PRD로 펫 기능을 입증하지 않고, README와 실제 펫 소스를 근거로 삼았다.
- 안전운전 개선, 멀미·피로 감소, 정서적 애착, 이용 지속률, 매출에 대한 비교 실험이나 사용자 지표는 확보하지 못했다. 위 분석은 기능 벤치마크다.
- 실제 화면을 실행해 시각·상호작용 품질을 평가하거나 영상을 시청한 조사는 아니다. 공식 발표의 기능 설명과 일부 소스 로직을 분석했다.
- 현대차 수상작의 개발 진행 현황은 확인한 2026-10-08 발표 범위다. 그 이후 출시·구현 여부는 이 문서에서 확정하지 않는다.

## 8. 원문을 보는 추천 순서

1. [현대차 차마고치 공식 소개](https://www.hyundaimotorgroup.com/ko/story/hyundai-motor-company-pleos-connect-app-idea-contest) — 기존 수상 아이디어의 기준 범위
2. [sj-park-kr 차마고찌 README](https://github.com/sj-park-kr/appdevchallenge-apk/blob/main/README.md) — 성장·추억·꾸미기 중복 범위
3. [jwlee1008 카마고치 README](https://github.com/jwlee1008/carmagotchi/blob/main/README.md) — 센서·운전 코칭·차량 제어 중복 범위
4. [NIO ET5 매뉴얼](https://www.nio.com/cdn-static/www/user-instructions/en_EU/ET5/index.html) — 실제 차량 명령과 작업 수행
5. [MINI Spike FAQ](https://faq.mini.com.au/s/article/Intelligent-Personal-Assistant-MINI-Spike-Benefits-NqMIq) — 감정 표현·습관 기반 개인화
6. [smart OTA 공식 발표](https://media.smart.com/en-CEU/260668-smart-offers-optimizations-with-free-over-the-air-update/) — 동반자 선택과 표시 제어
7. [Toyota pod](https://media.toyota.co.uk/future-shock/) / [Toyota Yui](https://global.toyota/en/newsroom/corporate/30063126.html) — 차량 의인화와 적응형 공간의 선행 구상
8. [Nissan LEAF Eco Tree](https://www.nissan-global.com/EN/INNOVATION/TECHNOLOGY/ARCHIVE/EV_IT/) — 행동을 성장 보상으로 바꾸는 구조
