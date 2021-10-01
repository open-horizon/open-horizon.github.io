---

copyright:
  years: 2020
lastupdated: "2020-04-8"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 배치 정책 유스 케이스
{: #developing_edge_services}

이 절은 정책 유형이 설명되는 실질적인 시나리오를 강조표시합니다.

<img src="../../images/edge/04_Defining_an_edge_policy.svg" width="90%" alt="에지 정책 정의">

절도를 감지하기 위해 ATM 카메라를 설치한 고객을 고려하십시오(고객은 다른 유형의 에지 노드도 갖고 있습니다). 고객은 워크업(walk-up, 보도 쪽으로 낸) ATM 및 드라이브스루(drive-through, 차에 탄 채로 이용 가능한) ATM의 조합을 사용합니다. 이 경우에 두 개의 서드파티 서비스를 사용할 수 있습니다. 각 서비스는 ATM에서 의심스러움 행동을 감지할 수 있지만, 고객 테스트가 서비스 atm1이 워크업 ATM에서 의심스러운 행동을 더 신뢰성 있게 감지하고 서비스 atm가 드라이브스루 ATM에서 의심스러운 행동을 더 신뢰성 있게 감지한다고 판별했습니다.

다음이 정책이 원하는 서비스 및 모델 배치를 달성하기 위해 표현되는 방법입니다.

* 모든 워크업 ATM에 대한 노드 정책에서 특성 설정: 특성: `sensor: camera`, `atm-type: walk-up`
* 모든 드라이브스루 ATM에 대한 노드 정책에서 특성 설정: 특성: `sensor: camera`, `atm-type: drive-thru`
* atm1 및 atm2 모두의 서드파티 개발자에 의한 서비스 정책에서 제한조건 설정: 제한조건: `sensor == camera`
* atm1 서비스에 대해 고객이 설정한 배치 정책에서 제한조건 설정: 제한조건: `atm-type == walk-up`
* atm2 서비스에 대해 고객이 설정한 배치 정책에서 제한조건 설정: 제한조건: `atm-type == drive-thru`

참고: `hzn` 명령은 배치 정책을 참조할 때 비즈니스 정책이라는 용어를 사용하는 경우가 있습니다.

노드 정책(ATM을 설정하는 기술자가 설정)이 각 노드에 관한 사실을 명시합니다. 예를 들어, ATM에 카메라가 있는지 여부 및 ATM이 있는 위치의 유형입니다. 이 정보는 기술자가 판별하고 지정하기 쉽습니다.

서비스 정책은 서비스가 올바르게 동작하기 위해 필요한 사항(이 경우에는 카메라)에 관한 선언입니다. 서드파티 서비스 개발자는 어떤 고객이 이를 사용 중인지 모른다고 하더라도 이 정보를 알고 있습니다. 고객이
카메라가 없는 다른 ATM을 보유하는 경우, 이들 서비스는 이 제한조건 때문에 해당 ATM에 배치되지 않습니다.

배치 정책은 고객 CIO(또는 이 에지 패브릭을 관리 중인 누군가)에 의해 정의됩니다. 이것은 비즈니스를 위한 전체적인 서비스 배치를 정의합니다. 이 경우에 CIO는 atm1이 워크업 ATM에 사용되어야 하고 atm2가 드라이브스루 ATM에 사용되어야 한다는 원하는 서비스 배치 결과를 표현합니다.

## 노드 정책
{: #node_policy}

정책을 노드에 연결할 수 있습니다. 노드 소유자는 등록 시에 이것을 제공할 수 있으며, 정책은 언제든지 노드에서 직접 또는 {{site.data.keyword.edge_devices_notm}} 관리자에 의해 중앙집중식으로 변경될 수 있습니다. 노드 정책이 중앙집중식으로 변경될 때는 다음에 노드가 관리 허브에 하트비트를 전송할 때 노드에 반영됩니다. 노드 정책이 노드에서 직접 변경될 때는 변경사항이 관리 허브에 즉시 반영되어 서비스 및 모델 배치를 즉시 재평가할 수 있습니다. 기본적으로 노드는 메모리, 아키텍처 및 CPU 수를 반영하는 몇 가지 [기본 제공 특성](#node_builtins)을 갖습니다. 이것은 선택적으로 임의 특성(예를 들어, 제품 모델, 접속된 디바이스, 소프트웨어 구성 또는 노드 소유자가 관련된다고 생각하는 사항)을 포함할 수 있습니다. 노드 정책 제한조건을 사용하여 이 노드에서 실행하도록 허용되는 서비스를 제한할 수 있습니다. 각 노드는 해당 노드에 지정된 모든 특성과 제한조건을 포함하는 단 하나의 정책만을 갖습니다.

## 서비스 정책
{: #service_policy}

참고: 서비스 정책은 선택적 기능입니다.

노드처럼, 서비스는 정책을 표현할 수 있는 몇 가지 [기본 제공 특성](#service_builtins)도 갖습니다. 이 정책은 exchange에서 공개된 서비스에 적용되며 서비스 개발자에 의해 작성됩니다. 서비스 정책 특성은 노드 정책 작성자가 관련된다고 생각할 수 있는 서비스 코드의 특성을 명시할 수 있습니다.서비스 정책 제한조건을 사용하여 이 서비스가 실행할 수 있는 장소 및 서비스의 유형을 제한할 수 있습니다. 예를 들어, 서비스 개발자가 이 서비스는 CPU/GPU 제한조건, 메모리 제한조건, 특정 센서, 액츄에이터 또는 기타 주변 장치 같은 특정 하드웨어 설정이 필요하다고 주장할 수 있습니다. 일반적으로, 특성과 제한조건은 서비스 구현의 측면을 설명하기 때문에 서비스의 수명 동안 일정합니다. 예상되는 사용 시나리오에서, 이들 중 하나에 대한 변경은 대개 새 서비스 버전이 필요한 코드 변경과 일치합니다. 배치 정책이 비즈니스 요구사항에서 발생하는 서비스 배치의 더 동적인 측면을 캡처하는 데 사용됩니다.

## 배치 정책
{: #deployment_policy}

배치 정책은 서비스 배치를 구동합니다. 다른 정책 유형처럼, 특성 및 제한조건 세트를 포함하지만 다른 것도 포함합니다. 예를 들어, 배치될 서비스를 명시적으로 식별하며, 구성 변수 값, 서비스 롤백 버전 및 노드 성능 상태 구성 정보를 선택적으로 포함할 수 있습니다. 구성 값에 대한 배치 정책 접근은 이 오퍼레이션이 에지 노드에 직접 연결할 필요없이 중앙집중식으로 수행될 수 있기 때문에 강력합니다.

관리자가 배치 정책을 작성할 수 있고, {{site.data.keyword.edge_devices_notm}}는 해당 정책을 사용하여 정의된 제한조건과 일치하는 모든 디바이스를 찾고, 정책에서 구성된 서비스 변수를 사용하여 해당 디바이스에 특정 서비스를 배치합니다. 서비스 롤백 버전은 {{site.data.keyword.edge_devices_notm}}에 상위 버전의 서비스가 배치하는 데 실패하는 경우 배치해야 하는 서비스 버전을 지시합니다. 노드 성능 상태 구성은 {{site.data.keyword.edge_devices_notm}}가 노드가 정책을 벗어났다고 판별하기 전에 노드의 성능 상태(하트비트 및 관리 허브 통신)을 측정하는 방법을 나타냅니다.

배치 정책이 더 동적이고 비즈니스형 서비스 특성과 제한조건을 캡처하기 때문에 서비스 정책보다 더 자주 변경될 것으로 예상됩니다. 해당 라이프사이클은 해당 정책이 참조하는 서비스와 독립적이어서, 정책 관리자에게 특정 서비스 버전 또는 버전 범위를 명시하는 능력을 부여합니다. {{site.data.keyword.edge_devices_notm}}는 그런 다음 서비스 정책과 배치 정책을 병합한 후 그의 정책이 호환 가능한 노드를 찾으려고 시도합니다.

## 모델 정책
{: #model_policy}

기계 학습(ML) 기반 서비스는 특정 모델 유형이 올바르게 동작해야 하며, {{site.data.keyword.edge_devices_notm}} 고객이 해당 서비스가 배치된 동일한 노드 또는 노드의 서브세트에 특정 모델을 배치할 수 있어야 합니다. 모델 정책의 목적은 주어진 서비스가 배치되는 노드 세트를 더욱 좁히는 것이며, 이것은 해당 노드의 서브세트가 [모델 관리를 사용하는 Hello world](../developing/model_management_system.md)를 통해 특정 모델 오브젝트를 수신할 수 있게 합니다.

## 확장된 정책 유스 케이스
{: #extended_policy_use_case}

ATM 예제에서, 고객은 자주 사용되지 않는 시골 지역에 워크업 ATM을 운영합니다. 고객은 시골의 ATM이 지속적으로 실행하길 원하지 않으며, 인접 오브젝트를 인지할 때마다 ATM을 켜기를 원하지 않습니다. 따라서, 서비스 개발자가 atm1 서비스에 접근하는 사람을 식별하는 경우 ATM을 켜는 ML 모델을 추가합니다. ML 모델을 시골의 ATM에 특정하게 배치하기 위해서 다음 정책을 구성합니다.

* 시골의 워크업 ATM에 대한 노드 정책: 특성: `sensor: camera`, `atm-type: walk-up`, `location:  rural`
* atm1에 대해 서드파티 개발자가 설정하는 서비스 정책 제한조건은 동일하게 유지: 제한조건: `sensor == camera`
* atm1 서비스에 대해 고객이 설정하는 배치 정책도 동일하게 유지: 제한조건: `atm-type == walk-up`
* 모델 정책 제한조건이 atm1 서비스를 위해 MMS 오브젝트에서 서드파티 개발자에 의해 다음과 같이 설정됩니다.

```
"destinationPolicy": {
  "constraints": [ "location == rural"  ],
  "services": [
       { "orgID": "$HZN_ORG_ID",
         "serviceName": "atm1",
         "arch": "$ARCH",  
         "version": "$VERSION"
       }
  ]
}
```
{: codeblock}

MMS 오브젝트 내에서 모델 정책은 오브젝트(이 경우에는 atm1)에 액세스할 수 있는 서비스(또는 서비스 목록)를 선언하고 {{site.data.keyword.edge_devices_notm}}가 시골 지역의 ATM에 오브젝트의 적절한 배치를 추가로 좁힐 수 있게 하는 특성 및 제한조건을 선언합니다. ATM에서 실행하는 기타 서비스는 해당 오브젝트에 액세스할 수 없습니다.

## 특성
{: #properties}

특성은 본질적으로 name=value 쌍으로 표현되는 사실의 선언입니다. 특성은 또한 입력되므로, 강력한 표현식을 생성하는 방법을 제공합니다. 다음 표는 {{site.data.keyword.edge_devices_notm}}가 지원하는 특성 값 유형과 기본 제공 노드 및 서비스 정책 특성을 보여줍니다. 노드 소유자, 서비스 개발자 및 배치 정책 관리자가 자신의 필요에 맞는 개별 특성을 정의할 수 있습니다. 특성이 중앙 저장소에서 정의될 필요는 없습니다. 즉, 필요에 따라 설정되고 참조됩니다(제한조건 표현식에서).

|허용되는 특성 값 유형|
|-----------------------------|
|버전 - 1, 2 또는 3 파트를 지원하는 점 분리 10진수 표현식(예: 1.2, 2.0.12 등)|
|문자열 *|
|문자열 목록(쉼표로 구분된 문자열)|
|정수|
|부울|
|float|
{: caption="표 1. 허용되는 특성 값 유형"}

*공백을 포함하는 문자열 값은 따옴표로 묶어야 합니다.

기본 제공 특성은 공통 특성에 대해 잘 정의된 이름을 제공하므로 제한조건이 모두 동일한 방식으로 특성을 참조할 수 있습니다. 예를 들어, 서비스가 적절하게 또는 효율적으로 실행하기 위해 `x`개의 CPU가 필요한 경우 제한조건에서 `openhorizon.cpu` 특성을 사용할 수 있습니다. 이들 특성의 대부분은 설정할 수 없지만, 대신 기본 시스템에서 읽어지며 사용자가 설정한 모든 값을 무시합니다.

### 노드 기본 제공 특성
{: #node_builtins}

|이름|유형|설명|정책 유형|
|----|----|-----------|-----------|
|openhorizon.cpu|정수|CPU 수|노드|
|openhorizon.memory|정수|MB 단위의 메모리 양|노드|
|openhorizon.arch|문자열|노드 하드웨어 아키텍처(예: amd64, armv6 등)|노드|
|openhorizon.hardwareId|문자열|linux API를 통해 사용 가능한 경우 노드 하드웨어 일련 번호. 그렇지 않으면 노드 등록 기간 동안 변하지 않는 암호화 보안 난수입니다.|노드|
|openhorizon.allowPrivileged|부울|컨테이너가 권한을 갖고 실행하거나 호스트 네트워크가 컨테이너에 접속되도록 하는 권한 있는 기능을 사용하도록 허용합니다.|노드|
{: caption="표 2. 노드 기본 제공 특성"}

### 서비스 기본 제공 특성
{: #service_builtins}

|이름|유형|설명|정책 유형|
|----|----|-----------|-----------|
|openhorizon.service.url|문자열|서비스의 고유한 이름|서비스|
|openhorizon.service.org|문자열|서비스가 정의되는 다중 테넌트 조직*|서비스|
|openhorizon.service.version|버전|동일한 시맨틱 버전 구문을 사용하는 서비스의 버전(예: 1.0.0)|서비스|
{: caption="표 3. 서비스 기본 제공 특성"}

제한조건에서 service.url이 지정되지만 service.org가 생략되는 경우 org는 제한조건을 정의하는 노드 또는 배치 정책의 org로 기본 설정됩니다.

## 제한조건
{: #constraints}

{{site.data.keyword.edge_devices_notm}}에서 노드, 서비스 및 배치 정책이 제한조건을 정의할 수 있습니다. 제한조건은 단순 텍스트 양식의 술어로서 표현되며 특성과 해당 값 또는 가능한 값의 범위를 말합니다. 제한조건은 또한 더 긴 절을 형성하기 위해 특성 및 값의 표현식 사이에서 AND(&&), OR(||) 같은 부울 연산자를 포함할 수도 있습니다. 예: `openhorizon.arch == amd64 && OS == Mojave`. 마지막으로, 소괄호를 사용하여 단일 표현식 안에서 평가 우선순위를 작성할 수 있습니다.

|특성 값 유형|지원되는 연산자|
|-------------------|-------------------|
|정수|==, <, >, <=, >=, =, !=|
|문자열*|==, !=, =|
|문자열 목록|in|
|부울|==, =|
|버전|==, =, in**|
{: caption="표 4. 제한조건"}

문자열 유형의 경우 그 안에 쉼표로 구분된 문자열이 있는 인용된 문자열은 허용 가능한 값의 목록을 제공합니다. 예를 들어, `hello == "beautiful, world"`는 hello가 "beautiful" 또는 "world"인 경우에 참입니다.

** 버전 범위의 경우, `==` 대신 `in`을 사용하십시오.

## 정책 유스 케이스 추가 확장
{: #extended_policy_use_case_more}

정책의 양방향 본성의 전체적인 성능을 보여주려면 이 절의 실세계 예제를 고려하고 노드에 몇 가지 제한조건을 추가하십시오. 본 예제에서 시골의 워크업 ATM의 일부가 다른 워크업 ATM이 사용하는 기존 atm1 서비스가 처리할 수 없는 눈부심을 만드는 물가 위치에 있는 경우입니다. 이 경우 해당되는 소수의 ATM에 대해 눈부심을 더 잘 처리할 수 있는 세 번째 서비스가 필요하며, 정책은 다음과 같이 구성됩니다.

* 물가의 워크업 ATM에 대한 노드 정책: 특성: `sensor: camera`, `atm-type: walk-up`; 제한조건: `feature == glare-correction`
* atm3에 대해 서드파티 개발자가 설정한 서비스 정책: 제한조건: `sensor == camera`
* atm3 서비스에 대해 고객이 설정한 배치 정책: 제한조건: `atm-type == walk-up`; 특성: `feature: glare-correction`  

다시, 노드 정책이 노드에 관한 사실을 명시하지만 이 경우에는 물가의 ATM을 설정한 기술자가 이 노드에 배치할 서비스는 눈부심 방지 기능을 가져야 한다는 제한조건을 지정했습니다.

atm3에 대한 서비스 정책은 ATM에 카메라가 필요하다는 다른 정책과 동일한 제한조건을 갖습니다.

고객이 atm3 서비스가 눈부심을 더 잘 처리한다고 알고 있으므로 atm3와 연관된 배치 정책에서 이 제한조건을 설정하며, 이는 노드에 설정된 특성을 충족하며 이 서비스가 물가에 있는 ATM에 배치되도록 합니다.

## 정책 명령
{: #policy_commands}

|명령|설명|
|-------|-----------|
|`hzn policy list`|이 에지 노드의 정책.|
|`hzn policy new`|채울 수 있는 빈 노드 정책 템플리트.|
|hzn policy update --input-file=INPUT-FILE|노드의 정책을 업데이트합니다. 노드의 기본 제공 특성이 입력 정책에 없으면 자동으로 추가됩니다.|
|`hzn policy remove [<flags>]`|노드의 정책을 제거합니다.|
|`hzn exchange node listpolicy [<flags>`] <node>|Horizon Exchange에서 노드 정책을 표시합니다.|
|`hzn exchange node addpolicy --json-file=JSON-FILE [<flags>`] <node>|Horizon Exchange에서 노드 정책을 추가하거나 바꿉니다.|
|`hzn exchange node updatepolicy --json-file=JSON-FILE [<flags>`] <node>|Horizon Exchange에서 이 노드의 정책 속성을 업데이트합니다.|
|`hzn exchange node removepolicy [<flags>`] <node>|Horizon Exchange에서 노드 정책을 제거합니다.|
|`hzn exchange service listpolicy [<flags>`] <service>|Horizon Exchange에서 서비스 정책을 표시합니다.|
|`hzn exchange service newpolicy`|입력할 수 있는 빈 서비스 정책 템플리트를 표시합니다.|
|`hzn exchange service addpolicy --json-file=JSON-FILE [<flags>`] <service>|Horizon Exchange에서 서비스 정책을 추가하거나 바꿉니다.|
|`hzn exchange service removepolicy [<flags>`] <service>|Horizon Exchange에서 서비스 정책을 제거합니다.|
|`hzn exchange business listpolicy [<flags>] [<policy>]`|Horizon Exchange에서 비즈니스 정책을 표시합니다.|
|`hzn exchange business new`|입력할 수 있는 빈 배치 정책 템플리트를 표시합니다.|
|`hzn exchange business addpolicy --json-file=JSON-FILE [<flags>`] <policy>|Horizon Exchange에서 배치 정책을 추가하거나 바꿉니다. 빈 배치 정책 템플리트에 'hzn exchange business new'를 사용합니다.|
|`hzn exchange business updatepolicy --json-file=JSON-FILE [<flags>`] <policy>|Horizon Exchange에서 기존 배치 정책의 속성 하나를 업데이트합니다. 지원되는 속성은 명령 'hzn exchange business new'에서 표시된 대로 정책 정의의 최상위 레벨 속성입니다.|
|`hzn exchange business removepolicy [<flags>`] <policy>|Horizon Exchange에서 배치 정책을 제거합니다.|
|`hzn dev service new [<flags>`]|새 서비스 프로젝트를 작성합니다. 이 명령은 서비스 정책 템플리트를 포함한 모든 IEC 서비스 메타데이터 파일을 생성합니다.|
|`hzn deploycheck policy [<flags>`]|노드, 서비스 및 배치 정책 사이의 정책 호환성을 검사합니다. 'hzn deploycheck all'을 사용하여 올바른 서비스 변수 구성을 확인할 것을 권장합니다.|
{: caption="표 5. 정책 개발 도구"}

`hzn` 명령 사용에 대한 자세한 정보는 [hzn 명령 탐색](../installing/exploring_hzn.md)을 참조하십시오.
