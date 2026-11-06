# 외부 근거 URL 확인 기록 — 2026-11-06 최종

이 기록은 외부자료 담당 agent가 실제 받은 결과와 읽은 범위를 적는다. 프로젝트 원본을 수정하지 않았다. 고정 목록77개 중 공모전 사이트·수상작 이미지·시스템XML17개는 다른 담당 범위이고, 외부60개(웹55URL·GitHub5저장소)는 모두 조회 결과를 받았다. 외부60개 중 미시도는0개다. **모든 본문·이미지를 읽었다는 뜻은 아니다.** 차단·추출한도·초록·이미지미확인 범위를 아래에 남겼다.

## 최종 집계

|구분|수량|실제 확인 범위|
|---|---:|---|
|고정 목록|77|각URL상태를 아래 표에 기록|
|다른 담당|17|공모전 사이트8URL·직접이미지8URL·시스템XML1URL|
|이 담당 외부URL 접근결과|60|웹55URL+GitHub5저장소|
|웹 본문 또는 인용 절 전체|38|KCA는자동차서비스절만,Herald는사이트표시영문AI번역본|
|웹 초록만|1|SAGE논문초록;논문본문·표는미확인|
|웹 제목·기간만|1|현대닷컴사전이벤트;상세콘텐츠미확인|
|이미지설명·라이선스·메타|2|Wikimedia파일페이지;사진직접미확인|
|PDF 해당부분|1|수원연구원186쪽 중서지·정책요약·전기차설문개요·만족도·불편표 등;전체186쪽완독아님|
|중복도메인 기사도입|1|HMG .co.kr 주소별도조회/도입확인;동명 .com 기사는본문전체읽음|
|웹접속·추출실패|11|403·cache miss·not accessible10개+Deloitte12MB크기한도1개|
|GitHub README 전체|4|Roadio·두차마고치·차곡;코드·실기·하위문서전체검증아님|
|GitHub 빈저장소|1|snd-carchestra메타확인,contents는empty404|
|실제 외부이미지 직접보기|0|alt/캡션을직접보기로집계하지않음|
|이 담당 미시도|0|접근실패를미시도와구분|

- 기존 부분본문6개(HMG저널·아시아경제·Rivian·Tesla충전기사·Aviva·NIO)는 누락구간을 보완해 기사본문 또는 고정페이지 본문을 읽었다. Roadio README도 저장된 원문의 잘렸던 뒷부분을 보완했다.
- 외부이미지6URL(Rivian3·Tesla기사1·파이낸셜뉴스2)을 직접 열었으나 모두 cache miss였다. 그 외 다수 기사·GitHub 이미지도 실제로 열지 않았다. 사진에 들어 있는 글자/도표/영상은 미확인이다.
- 이미지 대체확인용 Python 네트워크 읽기가 샌드박스DNS오류로 실패했고 require_escalated 재실행은 승인대기중 약21분 뒤 중단됐다. 자동승인거절/사용자거절 결과를 받은 적은 없다. 이후 shell·다운로드·승인요청 없이 웹도구의 텍스트 조회만 계속했다.
- 문서부록B의 추가7개는 root가 별도검토한 [appendix-sources-review.md](./appendix-sources-review.md)를 참조한다. 이 담당은 그7개를 직접열지않았다.
- 사이트footer·추천기사·저장소하위모든파일은추적하지않았다. 원문에 포함된 기능/실기검증 주장은 해당작성자의 설명으로 구분한다.

## 원문에서 확인된 사실·해석 차이

1. HMG2026-10-08 저널은 우수작16개가 아직 아이디어단계이고,4분기부터 개발가능성·출시여부검토,완성도높은아이디어의 프로토타입/2027전시가능성검토라고 한다.16개앱이 이미개발·출시됐다는 근거가 아니다.9월신규앱7종/총18종 보도자료는 실제앱마켓포트폴리오이고 공모전16개아이디어와다르다.
2. 공식수상작 차마고치와 공개저장소 카마고치(jwlee1008),차마고찌(sj-park-kr)는 이름이유사하지만 공식구현·동일팀연계가확인되지않았다.snd-carchestra는 빈저장소다.
3. 차곡README는 충전소후보가시연용목록,유가가오피넷형식스텁임을명시한다.Roadio도7개고정데모이야기를사용하며LLM콘텐츠파이프라인·다국어·영상은미완료,Gleo직접음성명령은미연동이라고한다.실제서비스완성주장과구분해야한다.
4. SAGE초록은의인화가신뢰·참여를높일수있다고하면서과도한의인화의과신·반자동화경계저하위험도함께제시한다.초록만읽었으며안전향상일반화의근거로단정하지않았다.
5. Aviva는2025-02-07~12 Censuswide의영국16세이상4000명조사다.한국운전자전체통계로일반화할수없다.39%는개성확장,19%는차가가족처럼느껴진다는항목이다.
6. Rivian은2024년북미R1T/R1S차주세션데이터로충전소A~F신뢰도를제공한사례다.Tesla충전기선정기사는2022년유럽·이스라엘초기도입보도이며60일성공90%이상등선정기준과14일성공70%미만등제외기준을설명한다.한국모든충전기의현재기능으로확대할수없다.
7. 파이낸셜뉴스/아시아경제83%는2023~2025년7월고속도로사망자중졸음·전방주시태만범주다.CO2원인사고83%나모든연중고속도로사망83%가아니다.의학·안전수치는기사주장으로확인했고1차연구대조는못했다.파이낸셜뉴스비교도해의표시출처는챗GPT다.
8. 뉴스핌차봇조사는2024년차봇앱사용자167명이다.84.5%는소모품교체를정비소에서한다는항목이고교체주기정확인지16.7%와구분된다.한국소비자원대기시간32.2%는전체이용자1500명중이아니라불만경험348명중112명이다.
9. 수원연구원PDF의전기차실사용자는56명,잠재구매자는301명이다.불편경험42명(75%),충전기부족26명은그42명중61.9%다.2023년수원표본을전국현재통계로일반화하지않았다.연합뉴스2024충전불편53.8%는별도의전국1000명조사다.한경2026기사는2025년GS차지비1400명이용자조사에서고장불편52.7%를인용하며충전기자체고장률52.7%를뜻하지않는다.
10. 데일리안수도권통근82분은왕복출퇴근합계이고자가용운전자에한정된통계가아니다.SKT일69분31초는TMAP고객이동데이터이고전국민운전평균이아니다.INRIX연17시간주차탐색은2017년미국자료다.
11. McKinsey는2022년12월15시장30978명,Cox는2022년신차구매계획217명,MobilityGlobal은2025년8개국8023차량소유자,Nielsen은2025년4개국4000명이상,SoundHound는2024년미국21~65세1136정기운전자다.표본·연도·국가를통합한하나의한국운전자현재수요통계로볼수없다.서로상이한조건의구독/구매의향도구분해야한다.
12. EuroNCAP은자발적안전등급평가이며ETSC기사는입법과구분한다.ViBilägare는2022년12차종4과제비교이고음성제어를제외했다.본문MG44.6초/표44.9초차이가있어인용시주의가필요하다.AAA주의분산실험은2017년30차종120명이다.IIHS평가는2024년특정14시스템·차종·당시SW한정이다.
13. 현재NHTSA주의분산페이지는2024년미국사망3208명/부상315167명을표시한다.예전연도수치와섞으면안된다.열사병보도자료는2025-05-01자료로2024년아동사망39명을언급한다.
14. NIO페이지는EVE비전콘셉트다.현재양산차NOMI기능전체의제원근거로단정할수없다.Jalopnik은기자직접체험이지만현대지원출장을공개했고영어미지원으로Gleo를직접써보지못했다고명시한다.
15. Tesla2025/2026기사의향후차종확대·지역지원표현은기자예측과확정사항이섞여있다.사진을직접확인하지않았으므로시각디자인분석완료를주장하지않는다.Wikimedia Model3사진은2020.48.25,ModelY Juniper사진은2025-07-25촬영메타이며둘다CC BY-SA4.0이다.

## 고정77개 URL별 상태

'본문읽음'은기사문자본문범위이며사진·도표내텍스트·영상내용까지확인했다는뜻이아니다.타담당17개완료여부는그담당보고서를참조한다.

|번호|URL|상태|읽은 범위·이미지·한계|
|---:|---|---|---|
|1|<https://www.hyundaimotorgroup.com/ko/story/hyundai-motor-company-pleos-connect-app-idea-contest>|본문 읽음|2026-10-08기사27–134행전체(누락인터뷰61–87행보완).공모16아이디어/심사50·30·20/아이디어단계개발검토명시.이미지alt/캡션만읽음,실제이미지미확인.|
|2|<https://appdevchallenge.auto-hmg.io/>|다른 담당 범위|공모전 사이트·수상작 이미지·시스템 XML. 이 보고서는 해당 담당의 완료를 대신 주장하지 않음.|
|3|<https://appdevchallenge.auto-hmg.io/guide>|다른 담당 범위|공모전 사이트·수상작 이미지·시스템 XML. 이 보고서는 해당 담당의 완료를 대신 주장하지 않음.|
|4|<https://appdevchallenge.auto-hmg.io/guide/submission>|다른 담당 범위|공모전 사이트·수상작 이미지·시스템 XML. 이 보고서는 해당 담당의 완료를 대신 주장하지 않음.|
|5|<https://www.freightwaves.com/?p=566413>|접속 실패|웹 도구 Cache miss. 본문·이미지 미확인.|
|6|<https://rivian.com/stories/software-spotlight-charging-reliability>|본문 읽음|2024-04-15기사21–49행전체.신뢰도A~F/차주데이터/우선A·B배차,미평가충전소존재와결제문제등원인명시.실제이미지미확인(3URLcache miss).|
|7|<https://www.notateslaapp.com/news/1112/tesla-to-add-reliable-third-party-chargers-to-their-in-car-navigation>|본문 읽음|2022-12-26기사31–55행전체.60일내호환1커넥터이상·4일당최소사용·성공90%이상,14일무충전또는성공70%미만제외.유럽/이스라엘초기도입기사.사진미확인.|
|8|<https://view.asiae.co.kr/article/2026071212260421354>|본문 읽음|2026-07-12기사157–172 및182행본문전체(앞누락보완).83%의분모2023~2025년7월고속도로사망자.사진미확인.의학·안전수치는기사주장이며1차원자료미대조.|
|9|<https://www.fnnews.com/news/202607130849571928>|본문 읽음|113–144행 기사 본문 전체. 대표 이미지와 비교도해 URL 직접 열기 모두 Cache miss; 실제 이미지 미확인.|
|10|<https://appdevchallenge.auto-hmg.io/notice/c0a1a000-2026-4923-8000-000000000001>|다른 담당 범위|공모전 사이트·수상작 이미지·시스템 XML. 이 보고서는 해당 담당의 완료를 대신 주장하지 않음.|
|11|<https://www.newspim.com/news/view/20240507000554>|본문 읽음|기사295–310행 전체. 차봇 앱 사용자167명 대상2024조사, 정확한 교체주기 인지16.7%, 정비소 교체84.5%. 일반 전체 운전자 확률표본으로 확인되지 않음. 이미지 미확인.|
|12|<https://www.kca.go.kr/webzine/board/view?div=kca_2601&linkId=964&menuId=MENU00307>|인용 절 본문 읽음|NEWS01 자동차 수리 서비스 절70–109행 전체 확인. 불만 경험23.2%(348/1500), 대기시간32.2%는 불만 경험자348명 중112명. 웹진 나머지 텍스트도 수신. 이미지 속 추가 정보 미확인.|
|13|<https://www.suwon.re.kr/data/file/research_reports/3535263116_HvBl8DYa_d9583dc8e963415683a1b0557501d7baeda55f65.pdf>|PDF 일부 본문·표 읽음|186페이지/3706행 추출 인덱스 확보. 서지·정책제안P2–9, 이용자 설문P88–89, 만족도표P99–101와 검색결과 일부 확인. 전체186쪽 읽지 않음.2023조사 전기차 이용자56/잠재301; 불편42명(75%), 충전기 부족26명은 불편42명중61.9%. 도표 이미지 미확인.|
|14|<https://www.yna.co.kr/view/AKR20240524092700530>|본문 읽음|기사76–132행 전체. 전국17시도 전기차 사용자1000명,2023-12-19~2024-01-04 인터넷 조사. 충전소부족 불편53.8%, 재구매의향70.4%. 이미지 미확인.|
|15|<https://www.yna.co.kr/view/AKR20260326051900003>|본문 읽음|기사76–90행 전체.2025년 리콜시정률90.2%; 리콜시행일부터18개월 이내 조치 비율. 방문리콜/OTA통지 확대. 이미지 미확인.|
|16|<https://www.hyundaimotorgroup.co.kr/ko/story/hyundai-motor-company-pleos-connect-app-idea-contest>|도입 본문 확인|실제 .co.kr 주소 조회 성공. .com과 제목·날짜·앞부분 내용 일치 확인. 나머지는 .com 부분검토 범위 참조, 전체본문 읽음 주장하지 않음. 이미지 미확인.|
|17|<https://appdevchallenge.auto-hmg.io/guide/judging-awards>|다른 담당 범위|공모전 사이트·수상작 이미지·시스템 XML. 이 보고서는 해당 담당의 완료를 대신 주장하지 않음.|
|18|<https://www.aviva.co.uk/insurance/motor/car-insurance/miles-of-memories/>|본문 읽음|기사14–197행전체·각주방법론보완.2025-02-07~12 Censuswide영국16세이상4000명.차가가족19%/인격확장39%등통계.그림수치와본문차이(스티커30%/alt32%)있음.실제이미지미확인.|
|19|<https://journals.sagepub.com/doi/10.1177/10711813251357934>|초록 읽음|제목·저자·2025-09-20 출판 정보 및 초록32–35행 전체. 본문·도표·PDF 미확인.|
|20|<https://doi.org/10.1080/10447318.2025.2477744>|접속 실패|웹 도구403 Forbidden. 제목·초록·본문·도표 미확인.|
|21|<https://www.nio.io/visioncar-experience>|본문 읽음|고정페이지89–236행전체.EVE비전콘셉트·NOMI디지털동반자·능동유리·공간·군집주행등설명.현재양산NOMI전체기능의현황근거로일반화불가.이미지미확인.|
|22|<https://appdevchallenge.auto-hmg.io/guide/schedule>|다른 담당 범위|공모전 사이트·수상작 이미지·시스템 XML. 이 보고서는 해당 담당의 완료를 대신 주장하지 않음.|
|23|<https://github.com/WhoisHOO/pleos-app-challenge>|메타·루트목록·README 읽음|저장된README 누락뒷부분보완전체읽음.Roadio경로오디오도슨트,데모7개고정이야기.콘텐츠LLM파이프라인/다국어/영상미완료로표시.Gleo직접명령미연동.코드·APK·하위문서·이미지미확인.|
|24|<https://github.com/argtkdals12-eng/snd-carchestra>|메타 확인·빈 저장소|저장소 메타 조회는 성공. contents API404는 This repository is empty. README·코드·이미지 없음으로 반환됨. 개발/출시 완료 근거로 볼 수 없음.|
|25|<https://www.instagram.com/p/Db8HMJblJVb/>|접속 실패|웹 도구Cache miss. 캡션·이미지 미확인.|
|26|<https://github.com/tlatlsgksp/pleos_pj>|메타·루트목록·README 읽음|차곡: 자동 차계부·관리주기·충전소 경유지. 충전소 후보는 시연용 목록, 유가는 오피넷 형식 스텁이라고 명시. README 이미지5장 실제로 열지 못함. 코드·앱·하위문서 미확인.|
|27|<https://github.com/jwlee1008/carmagotchi>|메타·루트목록·README 읽음|카마고치: 3×5 차량센서 융합, 평상시 무음 펫·위기시 음성/공조제어, 주행종료 성적표 설명. 이는 저장소 자체 주장으로 실기 검증하지 않음. 코드·APK·하위문서·목업 미확인.|
|28|<https://github.com/sj-park-kr/appdevchallenge-apk>|메타·루트목록·README 읽음|차마고찌: 차량신호 기반 펫 성장·도감·추억앨범. 상세화면 P단 제한, 기기 내 암호화 저장 등을 설명. 실기·코드 검증하지 않음. 하위문서·이미지 미확인.|
|29|<https://www.hyundaimotorgroup.com/image/upload/asset_library/MDA00000000000085390/807ec35bdfa44f54a0d79e827897f1d4.jpg>|다른 담당 범위|공모전 사이트·수상작 이미지·시스템 XML. 이 보고서는 해당 담당의 완료를 대신 주장하지 않음.|
|30|<https://www.hyundaimotorgroup.com/image/upload/asset_library/MDA00000000000085442/13770591703c4622915cf13f4c441ba8.jpg>|다른 담당 범위|공모전 사이트·수상작 이미지·시스템 XML. 이 보고서는 해당 담당의 완료를 대신 주장하지 않음.|
|31|<https://www.hyundaimotorgroup.com/image/upload/asset_library/MDA00000000000085443/7924f99c42264f598e857d6016c25d08.jpg>|다른 담당 범위|공모전 사이트·수상작 이미지·시스템 XML. 이 보고서는 해당 담당의 완료를 대신 주장하지 않음.|
|32|<https://www.hyundaimotorgroup.com/image/upload/asset_library/MDA00000000000085445/3201e1cea6184652b654d680b2d1acae.jpg>|다른 담당 범위|공모전 사이트·수상작 이미지·시스템 XML. 이 보고서는 해당 담당의 완료를 대신 주장하지 않음.|
|33|<https://www.hyundaimotorgroup.com/image/upload/asset_library/MDA00000000000085446/545be380c2c342789a7685ac4607718c.jpg>|다른 담당 범위|공모전 사이트·수상작 이미지·시스템 XML. 이 보고서는 해당 담당의 완료를 대신 주장하지 않음.|
|34|<https://www.hyundaimotorgroup.com/image/upload/asset_library/MDA00000000000085447/48a703f7dc1846f7a7f5aa9804c9df54.jpg>|다른 담당 범위|공모전 사이트·수상작 이미지·시스템 XML. 이 보고서는 해당 담당의 완료를 대신 주장하지 않음.|
|35|<https://www.hyundaimotorgroup.com/image/upload/asset_library/MDA00000000000085448/4747db8d71f643138dea5b926784d509.jpg>|다른 담당 범위|공모전 사이트·수상작 이미지·시스템 XML. 이 보고서는 해당 담당의 완료를 대신 주장하지 않음.|
|36|<https://www.hyundaimotorgroup.com/image/upload/asset_library/MDA00000000000085449/fbf7678e5e8449b48ccca81f20bdb045.jpg>|다른 담당 범위|공모전 사이트·수상작 이미지·시스템 XML. 이 보고서는 해당 담당의 완료를 대신 주장하지 않음.|
|37|<https://www.hyundaimotorgroup.com/ko/news/hyundai-motor-company-pleos-connect-app-best-customer-idea>|본문 읽음|기사 본문 29–47행 전체. 2026-10-01 보도자료. 대표 사진은 alt만 확인.|
|38|<https://www.hyundai.com/kr/ko/event/event-pleos-connect-pre-202606>|제목·기간만 확인|제목과 모든회원 2026-06-05~06-15 메타데이터 수신. 이벤트 상세 본문·포스터 미확인.|
|39|<https://nexus-playground.pleos.ai/repository/raw-releases/connect-avd/2.x/crp-sys-img.xml>|다른 담당 범위|공모전 사이트·수상작 이미지·시스템 XML. 이 보고서는 해당 담당의 완료를 대신 주장하지 않음.|
|40|<https://appdevchallenge.auto-hmg.io/faq>|다른 담당 범위|공모전 사이트·수상작 이미지·시스템 XML. 이 보고서는 해당 담당의 완료를 대신 주장하지 않음.|
|41|<https://appdevchallenge.auto-hmg.io/notice>|다른 담당 범위|공모전 사이트·수상작 이미지·시스템 XML. 이 보고서는 해당 담당의 완료를 대신 주장하지 않음.|
|42|<https://www.automotiveworld.com/news/fewer-physical-vehicle-controls-and-more-problematic-touchscreen-make-infotainment-system-a-modern-catch-all-drawer-j-d-power-finds/>|접속 실패|웹 도구403 Forbidden. 본문·이미지 미확인.|
|43|<https://www.automotiveworld.com/news/ai-based-technologies-improve-customer-experience-but-present-new-challenges-j-d-power-finds/>|접속 실패|웹 도구403 Forbidden. 본문·이미지 미확인.|
|44|<https://www.automotiveworld.com/news/fewer-failed-charging-attempts-signal-progress-in-ev-infrastructure-j-d-power-finds/>|접속 실패|웹 도구403 Forbidden. 본문·이미지 미확인.|
|45|<https://www.vibilagare.se/english/physical-buttons-outperform-touchscreens-new-cars-test-finds>|본문 읽음|2022기사24–109행 본문·표·4개과제 전체.110km/h12차종 비교, 음성제어 제외. MG수치 본문44.6초/표44.9초 내부차이 있음. V70 10초. 이미지 미확인.|
|46|<https://phys.org/news/2017-10-vehicle-infotainment-distractions-wheel.html>|본문 읽음|AAA Foundation 제공2017기사59–135행 전체.2017년30차량,21~36세120명, 내비입력평균40초; 모든 최신2026차량 결과로 일반화 불가. 이미지 미확인.|
|47|<https://etsc.eu/euro-ncap-new-2026-protocols-target-distraction-impairment-and-speeding/>|본문 읽음|2026-01-12기사106–124행 전체. EuroNCAP 자발적 안전등급 변경/물리조작 권고와 입법 차이 명시. 이미지 미확인.|
|48|<https://www.mckinsey.com/industries/automotive-and-assembly/our-insights/how-do-consumers-perceive-in-car-connectivity-and-digital-services>|본문 읽음|웹본문15–74행 전체.2022-12 온라인15시장30978명; 기존연결서비스만족17%, CarPlay유사서비스보유자85% 선호.웹의 차트이미지/PDF8쪽 미확인.|
|49|<https://www.fnnews.com/news/202607281338101369>|본문 읽음|2026-07-28기사135–141행 전체.15분휴식50~500원 상당 포인트; 모든휴식500원 확정 아님. 이미지 미확인.|
|50|<https://www.newsseoul.co.kr/news/view/1065594018625461>|접속 실패|웹 도구not accessible. 본문·이미지 미확인.|
|51|<https://www.nhtsa.gov/risky-driving/distracted-driving>|본문 읽음|Overview·정의·결과·참여안내·정책안내69–138행. 현재표시2024년미국사망3208명/부상315167명. 다른연도숫자와 구분 필요. 이미지 미확인.|
|52|<https://southjersey.aaa.com/news/aaa-fear-self-driving-vehicles-persists>|본문 읽음|2025-02-25기사51–72행 본문·방법론 전체.미국운전자6/10두려움,안전개선78%; 조사1095인터뷰 중888적격/오차4.4%p. 이미지 미확인.|
|53|<https://www.iihs.org/news/detail/first-partial-driving-automation-safeguard-ratings-show-industry-has-work-to-do>|본문 읽음|2024-03-12기사10–54행 전체.14시스템1acceptable/2marginal/11poor.테스트특정차종·당시SW 한정,모든현재차량으로 일반화불가. 영상 미시청.|
|54|<https://news.umich.edu/motion-sickness-in-autonomous-cars-don-t-read-and-ride>|접속 실패|웹 도구403 Forbidden. 본문·이미지 미확인.|
|55|<https://www.dailian.co.kr/news/view/1443575/%EC%88%98%EB%8F%84%EA%B6%8C-%EC%A7%81%EC%9E%A5%EC%9D%B8-%EC%B6%9C%ED%87%B4%EA%B7%BC-%EB%A7%A4%EC%9D%BC-1%EC%8B%9C%EA%B0%84-2-2024>|본문 읽음|2024-12-20기사103–155행전체.가명결합1220만명 이동정보;수도권출퇴근합계82분,전국73.9분.자동차운전만의 통근시간으로 한정되지 않음. 이미지 미확인.|
|56|<https://inrix.com/press-releases/parking-pain-us/>|본문 읽음|2017-07-12보도자료95–130행전체.미국평균연17시간주차탐색/10미국도시약6000명설문;한국현재수치아님. 표이미지 미확인.|
|57|<https://www.hankyung.com/article/202603189825i>|본문 읽음|2026-03-18기사79–86행전체.GS차지비2025전기차이용자1400명설문에서고장52.7%,부족47%;전체충전기의고장률52.7%아님. 이미지 미확인.|
|58|<https://www.nhtsa.gov/press-releases/nhtsa-urges-public-help-prevent-child-heatstroke>|본문 읽음|2025-05-01보도자료54–69행전체.2024년미국차량열사병아동사망39/2023년29.열상승온도는미국원문단위맥락(화씨)주의. 별도그림 없음.|
|59|<https://www.coxautoinc.com/insights/car-buyers-balk-at-paying-monthly-fees-for-features-and-services/>|본문 읽음|2022-04-21기사11–38행전체.2022-01-19~26 향후2년내신차구매계획217명.3/4구독지불거부;기능별의향80%는지불가능25%하위집단.인포그래픽미확인.|
|60|<https://www.deloitte.com/content/dam/assets-shared/docs/industries/consumer/2026/global-automotive-consumer-study-2026.pdf>|추출 실패·크기 한도|웹 도구400 Content length too large:12084769바이트. PDF본문·표·이미지 미확인. 다운로드 재시도하지 않음.|
|61|<https://www.mobilityglobal.com/en-us/automotive-insights/blog/what-consumers-value-in-human-machine-interface-technologies>|본문 읽음|2026-02-12웹기사37–86행전체.2025HMI조사8개국8023차량소유자;하이브리드조작48%,음성인식가끔이상80%. 부속유료보고서·차트이미지 미확인.|
|62|<https://www.jdpower.com/business/press-releases/2024-us-automotive-performance-execution-and-layout-apeal-study>|본문 읽음|2024미국APEAL보도자료123–174행전체.신차90일소유99144명;순정805/AndroidAuto832/CarPlay840;복잡한오디오입력문제.차트이미지미확인.|
|63|<https://japan.jdpower.com/en/node/12691>|접속 실패|웹 도구Cache miss. 본문·이미지 미확인.|
|64|<https://www.nielsen.com/news-center/2025/consumer-attitudes-toward-in-car-entertainment-and-media-preferences-highlighted-in-new-gracenote-automotive-report/>|본문 읽음|2025-10-15보도자료25–43행전체.미·독·일·한4000명이상설문;94%는순정시스템개선시전환고려,실제전환율아님.하위보고서·이미지미확인.|
|65|<https://www.silicon.co.uk/press-release/research-finds-76-of-u-s-drivers-likely-to-use-voice-generative-ai-capabilities-in-their-vehicles>|본문 읽음|SoundHound의BusinessWire보도자료전재56–111행.2024-09미국21~65세정기운전자1136명/주운행2018이후모델.76%의향,74%는요금또는광고조건복합.이미지미확인.|
|66|<https://news.sktelecom.com/217654>|본문 읽음|2025-12-24기사53–114행전체.기준기간1/1~11/24,MAU3분기1562만명.고객평균일52.268km/69분31초는TMAP이용자데이터이며전체국민자동차평균아님.다수지도/차트이미지미확인.|
|67|<https://mobile.newsis.com/view/NISX20260128_0003493411>|접속 실패|웹 도구not accessible. 본문·이미지 미확인.|
|68|<https://mbiz.heraldcorp.com/article/10815843>|표시된 번역 본문 읽음|2026-07-22기사42–56행 AI영문번역본.고령운전자면허반납2025년2.51%;농업인94.8%는65세이상면허보유농업인설문하위집단.한국어원문링크·사진미확인.|
|69|<https://www.hyundaimotorgroup.com/ko/story/pleos-connect-next-generation-infotainment-system>|본문 읽음|2026-04-30기사27–137행전체.하이브리드제어·정보영역분리·Gleo·SDK/앱마켓·OTA.서드파티Gleo연동은향후계획표현.이미지/영상미확인.|
|70|<https://www.hyundaimotorgroup.com/ko/news/42dot-pleos-connect-app-market-new-apps>|본문 읽음|2026-09-09기사29–49행전체.국내신규7앱/총18,그랜저·아반떼등지원.특정시점·시장한정.표7앱명 확인.이미지미확인.|
|71|<https://www.jalopnik.com/2253248/hyundai-pleos-connect-infotainment-system-technology-review/>|본문 읽음|2026-09-09체험기사80–124행전체.기자가직접체험한원기고.현대지원출장공개/영어미지원으로Gleo미체험명시.메뉴·손지지·통풍구조작불편과물리버튼/슬림화면장점.이미지미확인.|
|72|<https://notateslaapp.com/news/2042/a-look-at-the-22-unlisted-changes-in-teslas-2024-14-update>|본문 읽음·www대체 성공|원주소Cache miss후 www동일경로 대체조회성공.2024-05-28기사31–234행전체.22변경설명,미디어플레이어·상태바·회생제동계등.이미지/연결영상미확인.|
|73|<https://www.notateslaapp.com/news/3996/first-look-at-teslas-new-visualizations-in-update-202614-video>|본문 읽음|2026-04-17기사29–60행전체.주차비주얼모델/조명개선,당시Highland·Juniper확인,향후모델확대는기자예측.이미지·영상미확인.|
|74|<https://www.notateslaapp.com/news/4670/first-look-at-tesla-update-202632-photos>|본문 읽음|2026-09-09기사29–47행전체.휠설정UI·AppleMusic라이브러리검색·EU OTA리콜설명.이미지미확인,실차검증없음.|
|75|<https://www.notateslaapp.com/news/3388/tesla>|본문 읽음|해당고정URL은2025-12-06 Holiday Update기사로반환.본문29–178행전체.내비Grok·주차추천·3D충전사이트맵·셀피·랩핑등.기사의예측/차종제약구분.이후자동추천기사는검토대상제외.이미지/영상미확인.|
|76|<https://commons.wikimedia.org/wiki/File:Tesla_Model_3_Screen_Dec_2020.jpg>|이미지 설명·메타 읽음|파일설명·라이선스·이력·EXIF·구조화메타120–295행 확인.2020-12-31,2020.48.25 SW,작가SirAsdof/CC BY-SA4.0.사진직접보기미수행.|
|77|<https://commons.wikimedia.org/wiki/File:Tesla_Model_Y_Juniper_Long_Range_AWD_White_%2B_Black_03.jpg>|이미지 설명·메타 읽음|파일설명·라이선스·이력·EXIF·구조화메타119–279행 확인.2025-07-25,작가EthanLlamas/CC BY-SA4.0.사진직접보기미수행.|
