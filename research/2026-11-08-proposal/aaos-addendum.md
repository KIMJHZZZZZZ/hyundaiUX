# AAOS 추가 검증 — 기어·UX 제한·마이크

확인일: 2026-11-08. 출처는 아래 Android Developers 공식 문서만 사용했다. **공개 API 명칭을 확인한 것이며 Pleos SDK 빌드·앱 실행·장비 호환성 검증은 아니다.** 현재 Android 문서의 최신 API가 Pleos API34 이미지에 모두 존재한다고 가정하지 않는다.

## 1. 선택 기어와 권한

| 항목 | 공식 문서에서 확인한 정확한 이름·의미 |
|---|---|
| 사용자 선택 기어 | `android.car.VehiclePropertyIds.GEAR_SELECTION` = `289408000 / 0x11400400`; Integer, GLOBAL, ONCHANGE, read-only. [A01](https://developer.android.com/reference/android/car/VehiclePropertyIds#GEAR_SELECTION) |
| 기어 값 | `android.car.VehicleGear.GEAR_PARK`와 `GEAR_DRIVE` 등을 비교한다. `CURRENT_GEAR`는 실제 변속단으로 선택 레버 상태와 다를 수 있으므로 P/D 판정 목적과 구분한다. [A01](https://developer.android.com/reference/android/car/VehiclePropertyIds#CURRENT_GEAR), [A02](https://developer.android.com/reference/android/car/VehicleGear) |
| 읽기 권한 | `Car.PERMISSION_POWERTRAIN`의 manifest 문자열은 **`android.car.permission.CAR_POWERTRAIN`**, Android 문서상 protection은 **normal**이다. `CONTROL_CAR_POWERTRAIN`을 요청할 이유가 없다. [A03](https://developer.android.com/reference/android/car/Car#PERMISSION_POWERTRAIN) |
| area | GLOBAL property의 area ID는 `0`. 다른 property에 이를 무조건 적용하지 않는다. [A04](https://developer.android.com/reference/android/car/hardware/CarPropertyValue#getAreaId()) |
| 속도(필요할 경우) | `PERF_VEHICLE_SPEED`: Float, m/s, GLOBAL, CONTINUOUS, read-only. `Car.PERMISSION_SPEED` = **`android.car.permission.CAR_SPEED`**, **dangerous** 권한. 속도 0만으로 P나 UX 허용 상태를 판정할 수 없다. [A01](https://developer.android.com/reference/android/car/VehiclePropertyIds#PERF_VEHICLE_SPEED), [A03](https://developer.android.com/reference/android/car/Car#PERMISSION_SPEED) |

### 초기 조회와 변경 구독

- manager 경로: `Car.getCarManager(Car.PROPERTY_SERVICE)` → `android.car.hardware.property.CarPropertyManager`. `Car.PROPERTY_SERVICE` 값은 `property`다. 일반 Android 태블릿에서 Car API가 보장되지 않는다. `Car`는 `FEATURE_AUTOMOTIVE` 장치용이다. [A03](https://developer.android.com/reference/android/car/Car)
- 현재값: `getProperty(Integer.class, VehiclePropertyIds.GEAR_SELECTION, 0)` 또는 `getIntProperty(propertyId, areaId)`. 동기 조회는 수 초 걸릴 수 있어 main thread에서 실행하지 않는다. `getCarPropertyConfig(propertyId)`가 null이면 미지원 또는 권한 부족일 수 있다. 예외·null·0을 정상 주차값으로 대체하지 않는다. [A05](https://developer.android.com/reference/android/car/hardware/property/CarPropertyManager)
- **현재 문서 권장:** `subscribePropertyEvents(int propertyId, float updateRateHz, CarPropertyEventCallback callback)`와 `unsubscribePropertyEvents(int propertyId, callback)` 또는 callback 전체 해제. `registerCallback/unregisterCallback`은 현재 문서에서 deprecated다. 기어는 ONCHANGE이므로 rate로 polling 주기를 보장하지 않는다. [A05](https://developer.android.com/reference/android/car/hardware/property/CarPropertyManager#subscribePropertyEvents(int,float,android.car.hardware.property.CarPropertyManager.CarPropertyEventCallback))
- callback: `CarPropertyManager.CarPropertyEventCallback.onChangeEvent(CarPropertyValue<T> value)`. 새 subscription에는 초기값 또는 unavailable/error 상태도 전달된다. `onErrorEvent(propertyId, areaId[, errorCode])`는 최근 **setProperty 실패**에 대한 callback이므로 모든 read/연결 실패 통지로 해석하지 않는다. [A06](https://developer.android.com/reference/android/car/hardware/property/CarPropertyManager.CarPropertyEventCallback)
- 상태: 현재 `CarPropertyValue` 문서는 `getPropertyStatus()`와 `STATUS_AVAILABLE/UNAVAILABLE/ERROR`를 안내하며 `getStatus()`는 deprecated다. `getValue()`는 available일 때만 사용한다. Pleos에 배포된 Car API가 이전 메서드만 제공한다면 해당 버전에 맞춘 adapter를 사용한다. [A04](https://developer.android.com/reference/android/car/hardware/CarPropertyValue#getPropertyStatus())

**구현 경계:** 제안서에는 “CarPropertyManager로 선택 기어의 초기값과 변경 이벤트를 확인할 계획”이라고 쓴다. 소스 호환은 target image의 `android.car` API로 compile하고 AVD에서 확인한다. 최신 문서의 메서드명을 무검증 상태로 복사해 “API34 실행 코드”라고 제시하지 않는다. 연결 재시작 때 subscription과 현재값을 재설정하고, 유효한 값이 확인되기 전 앱은 잠긴 상태로 둔다.

## 2. 현재 CarUxRestrictionsManager API

`Car.getCarManager(Car.CAR_UX_RESTRICTION_SERVICE)`로 manager를 얻는 경로를 사용할 수 있다. 서비스 상수 값은 `uxrestriction`. [A03](https://developer.android.com/reference/android/car/Car#CAR_UX_RESTRICTION_SERVICE)

| 목적 | 확인한 시그니처 |
|---|---|
| 현재 제한 조회 | `CarUxRestrictionsManager.getCurrentCarUxRestrictions()` → `CarUxRestrictions` |
| 변경 구독 | `registerListener(CarUxRestrictionsManager.OnUxRestrictionsChangedListener listener)` |
| 변경 callback | `onUxRestrictionsChanged(CarUxRestrictions restrictionInfo)` |
| 해제 | `unregisterListener()`; 기존 listener를 교체하려면 먼저 해제해야 한다. |

manager 메서드의 공식 근거: [A07](https://developer.android.com/reference/android/car/drivingstate/CarUxRestrictionsManager). callback 공식 근거: [A08](https://developer.android.com/reference/android/car/drivingstate/CarUxRestrictionsManager.OnUxRestrictionsChangedListener).

`CarUxRestrictions.isRequiresDistractionOptimization()`이 true이면 `getActiveRestrictions()`로 현재 제한 집합을 확인해야 한다. false일 때는 distraction optimization이 요구되지 않는다. **GEAR_SELECTION=P와 UX 제한 해제는 같은 API나 같은 보장이 아니다.** 앱의 보수적 조건은 `유효한 주차 상태 && 현재 UX 제한 확인 및 허용`이며, 미확인·서비스 끊김에서는 대화·입력을 잠근다. 이 조합은 앱 설계이고 Android가 이 소셜 앱의 주행 사용을 승인했다는 뜻이 아니다. [A09](https://developer.android.com/reference/android/car/drivingstate/CarUxRestrictions)

## 3. RECORD_AUDIO와 실시간 음성통신의 경계

- **확인:** `android.Manifest.permission.RECORD_AUDIO`의 정확한 문자열은 **`android.permission.RECORD_AUDIO`**, protection level은 **dangerous**다. manifest 선언과 runtime grant가 필요하다. 사전 안내 화면의 “사용” 버튼 자체는 OS 권한 승인이 아니다. [A10](https://developer.android.com/reference/android/Manifest.permission#RECORD_AUDIO), [A11](https://developer.android.com/training/permissions/requesting)
- **확인:** 사용자 행동 맥락에서 요청하고, 거절/철회 시 해당 음성 기능을 비활성화하면서 가능한 기능은 계속 제공한다. 권한을 얻기 전 마이크를 열지 않는다. [A11](https://developer.android.com/training/permissions/requesting)
- **확인:** Android for Cars App Library에는 `CarAppService`/`CarAudioRecord`를 이용한 차량 마이크 예제가 있다. `CarAudioRecord.create(carContext)`, `startRecording`, `read`, `stopRecording`과 RECORD_AUDIO runtime 권한을 안내한다. 이는 그 App Library 경로의 문서이며, 임의 Pleos Activity 앱에서 WebRTC의 native audio capture가 동작한다는 보장이 아니다. [A12](https://developer.android.com/training/cars/apps/library/car-microphone)
- **확인:** Android의 동시 audio capture는 우선순위에 따라 한 앱이 silence를 받을 수 있다. 따라서 “RECORD_AUDIO granted”와 “실제 유효한 마이크 프레임 수신”은 별도로 측정한다. STT·Gleo·전화와 함께 시험해야 한다. [A13](https://developer.android.com/media/platform/sharing-audio-input)
- **조건부:** foreground service로 마이크를 계속 사용한다면 Android14+ 규칙에 맞춰 `android:foregroundServiceType="microphone"`, `FOREGROUND_SERVICE`, `FOREGROUND_SERVICE_MICROPHONE` 및 RECORD_AUDIO runtime 권한 조건을 검토해야 한다. while-in-use/background 시작 제한도 있다. 이 앱은 MVP에서 주차 상태·포그라운드 중심으로 제한하며 background 통화를 임의 허용하지 않는다. [A14](https://developer.android.com/develop/background-work/services/fgs/service-types#microphone), [A15](https://developer.android.com/develop/background-work/services/fgs/restrictions-bg-start)

**WebRTC 관련 미확인:** 위 Android 공식 문서는 Pleos용 WebRTC ABI·라이브러리 버전, audio input/output 라우팅, echo cancellation, 네트워크 relay, OEM 승인 또는 사회적 음성통화 카테고리 허용을 보증하지 않는다. 통신 라이브러리와 STT/TTS는 별개다. 실제 Pleos 장비에서 parked 두 단말의 송수신·mute·즉시 종료·권한 철회·다른 음성 서비스의 mic 선점·UX restriction 전환을 시험하기 전에는 “WebRTC 호환 확인”이라고 쓰지 않는다.

**혼동 금지:** Google의 “Build calling experiences for Android Auto”는 Android Auto/Telecom/App Library 통화 경험 문서다. 그 내용만으로 AAOS 기반 Pleos에서 운전자 소셜 대화가 주행 허용된다고 주장할 수 없다. [A16](https://developer.android.com/training/cars/communication/calling)

### 제안서용 확정 문장

> 기어는 AAOS의 GEAR_SELECTION을 CarPropertyManager로 조회·구독하고, CarUxRestrictionsManager의 현재값과 변경 이벤트를 별도로 확인할 계획이다. 마이크는 RECORD_AUDIO의 사용자 승인을 받은 뒤 사용하며, 실제 음성 전송의 Pleos 장비 호환성은 별도 검증한다. 모든 사람·AI 대화와 동의 입력은 주차 및 UX 제한 해제가 확인될 때만 제공한다.
