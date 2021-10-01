---

copyright:
years: 2019
lastupdated: "2019-07-05"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 개발 세부사항
{: #developing}

다음 컨텐츠는 {{site.data.keyword.edge_notm}}({{site.data.keyword.ieam}}) 개발을 위한 소프트웨어 개발 사례 및 개념에 대한 세부사항을 제공합니다.
{:shortdesc}

## 소개
{: #developing_intro}

{{site.data.keyword.edge_notm}}({{site.data.keyword.ieam}})는 [Open Horizon - EdgeX 프로젝트 그룹 ![새 탭에서 열림](../../images/icons/launch-glyph.svg "새 탭에서 열림")](https://wiki.edgexfoundry.org/display/FA/Open+Horizon+-+EdgeX+Project+Group) 오픈 소스 소프트웨어에 빌드됩니다.

{{site.data.keyword.ieam}}을 사용하여 에지 머신에 대해 원하는 서비스 컨테이너를 개발할 수 있습니다. 그런 다음, 코드를 암호화 서명하고 공개할 수 있습니다. 마지막으로 소프트웨어 설치, 모니터링, 업데이트를 제어하기 위해 {{site.data.keyword.edge_deploy_pattern}} 내에 정책을 지정할 수 있습니다. 이러한 태스크를 완료한 후 {{site.data.keyword.horizon_agents}} 및 {{site.data.keyword.horizon_agbots}}이 소프트웨어 라이프사이클 관리를 위해 협업하도록 계약을 형성하는 것을 볼 수 있습니다. 그런 다음, 이러한 컴포넌트가 각 에지 노드에 대해 등록된 배치 패턴을 기반으로 {{site.data.keyword.edge_nodes}}에서 소프트웨어 라이프사이클 세부사항을 완전히 자율적으로 관리합니다. 또한 {{site.data.keyword.ieam}}은 정책을 사용하여 서비스 및 머신 학습 모델을 자율적으로 배치하는 장소와 시기를 판별합니다. 정책은 배치 패턴의 대안입니다.

{{site.data.keyword.ieam}} 내의 소프트웨어 배치 프로세스는 에지 노드에서 활성 소프트웨어를 관리하는 데 필요한 노력을 크게 단순화하는 동시에 머신 보안 및 무결성을 유지보수하는 데 중점을 둡니다. 또한 {{site.data.keyword.ieam}}은 정책을 사용하여 서비스 및 머신 학습 모델을 자율적으로 배치하는 장소와 시기를 판별합니다. 정책은 배치 패턴의 대안입니다. {{site.data.keyword.ieam}} 공개 프로시저를 지속적 통합 및 배치 파이프라인으로 빌드할 수 있습니다. 분산 자율 에이전트가 소프트웨어 또는 정책에서(예: {{site.data.keyword.edge_deploy_pattern}} 또는 배치 정책 내에서) 공개된 변경사항을 발견하면 자율 에이전트가 에지 머신의 위치에 관계없이 전체 에지 머신에서 소프트웨어를 업데이트하거나 정책을 적용하기 위해 독립적으로 작동합니다.

## 서비스 및 배치 패턴
{: #services_deploy_patterns}

{{site.data.keyword.edge_services}}는 배치 패턴의 구성 요소입니다. 각 서비스에는 하나 이상의 Docker 컨테이너가 포함될 수 있습니다. 각 Docker 컨테이너에는 차례로 하나 이상의 장기 실행 프로세스가 포함될 수 있습니다. 이러한 프로세스는 거의 모든 프로그래밍 언어로 작성되고 모든 라이브러리 또는 유틸리티를 사용할 수 있습니다. 그러나 이 프로세스는 Docker 컨테이너의 컨텍스트로 개발되고 실행되어야 합니다. 이 유연성은 {{site.data.keyword.ieam}}이 관리할 수 있는 코드에 대한 제한조건이 거의 없음을 의미합니다. 컨테이너가 실행될 때 컨테이너는 보안 샌드박스로 제한됩니다. 이 샌드박스는 하드웨어 디바이스, 일부 운영 체제 서비스, 호스트 파일 머신 및 호스트 에지 머신 네트워크에 대한 액세스를 제한합니다. 샌드박스 제한조건에 대한 정보는 [샌드박스](#sandbox)를 참조하십시오.

`cpu2evtstreams` 예제 코드는 두 개의 다른 로컬 에지 서비스를 사용하는 Docker 컨테이너로 구성됩니다. 이러한 로컬 에지 서비스는 HTTP REST API를 사용하여 로컬 사설 Docker 가상 네트워크를 통해 연결됩니다. 이러한 서비스의 이름은 `cpu` 및 `gps`입니다. 에이전트가 서비스에 대한 종속성을 선언한 각 서비스와 함께 별도의 사설 네트워크에 각 서비스를 배치합니다. 하나의 네트워크가 `cpu2evtstreams` 및 `cpu`용으로 작성되고 다른 네트워크가 `cpu2evtstreams` 및 `gps`용으로 작성됩니다. 이 배치 패턴에 `cpu` 서비스를 공유하고 있는 네 번째 서비스가 있는 경우 `cpu` 및 네 번째 서비스 전용으로 다른 사설 네트워크가 작성됩니다. {{site.data.keyword.ieam}}에서 이 네트워크 전략은 다른 서비스가 공개된 경우 서비스에 대한 액세스를 `requiredServices`에 나열된 다른 서비스만으로 제한합니다. 다음 다이어그램은 패턴이 에지 노드에서 실행되는 경우 `cpu2evtstreams` 배치 패턴을 보여줍니다.

<img src="../../images/edge/07_What_is_an_edge_node.svg" width="70%" alt="패턴의 서비스">

참고: IBM Event Streams 설정은 일부 예제를 위해서만 필요합니다.

`cpu2evtstreams` 서비스 컨테이너가 두 개의 가상 네트워크를 사용하여 `cpu` 및 `gps` 서비스 컨테이너에서 제공되는 REST API에 액세스할 수 있습니다. 이러한 두 개의 컨테이너는 운영 체제 서비스 및 하드웨어 디바이스에 대한 액세스를 관리합니다. REST API가 사용되지만 서비스가 데이터 및 제어를 공유할 수 있도록 하는 데 사용할 수 있는 다른 많은 통신 양식이 있습니다.

종종 에지 노드에 대한 가장 효과적인 코딩 패턴에는 여러 개의 작고 독립적으로 구성 가능하며 배치 가능한 서비스를 배치하는 것이 포함됩니다. 예를 들어, IoT(Internet of Things) 패턴에는 센서 또는 작동기(actuator)와 같은 에지 노드 하드웨어에 대한 액세스가 필요한 하위 레벨 서비스가 있습니다. 이러한 서비스는 다른 서비스가 사용할 수 있도록 이 하드웨어에 대한 공유 액세스를 제공합니다.

이 패턴은 하드웨어에서 유용한 기능을 제공하기 위해 독점 액세스가 필요한 경우에 유용합니다. 하위 레벨 서비스가 이 액세스를 적절히 관리할 수 있습니다. `cpu` 및 `gps` 서비스 컨테이너의 역할은 원칙적으로 호스트 운영 체제의 디바이스 드라이버 소프트웨어 역할과 유사하지만 더 높은 레벨입니다. 코드를 독립적인 작은 서비스(일부는 하위 레벨 하드웨어 액세스를 전문으로 함)로 세그먼트화하면 관심사항을 명확하게 분리할 수 있습니다. 각 컴포넌트는 자유롭게 진화하고 현장에서 독립적으로 업데이트됩니다. 또한 선택적으로 특정 하드웨어 또는 다른 서비스에 액세스할 수 있도록 하여 기존의 전용 임베디드 소프트웨어 스택과 함께 서드파티 애플리케이션을 안전하게 배치할 수 있습니다.

예를 들어, 산업용 제어기 배치 패턴은 전력 사용량 센서를 모니터하기 위한 하위 레벨 서비스 및 기타 하위 레벨 서비스로 구성될 수 있습니다. 이러한 기타 하위 레벨 서비스는 모니터되는 디바이스에 전원을 공급하기 위해 작동기의 제어를 사용으로 설정하는 데 사용될 수 있습니다. 배치 패턴에는 센서 및 작동기의 서비스를 이용하는 다른 최상위 레벨 서비스 컨테이너가 있을 수도 있습니다. 이 최상위 레벨 서비스는 비정상 소비전력 표시값이 발견될 때 서비스를 사용하여 운영자에게 경보를 보내거나 자동으로 디바이스 전원을 끌 수 있습니다. 이 배치 패턴에는 센서 및 작동기 데이터와 데이터에 대한 완전한 분석을 기록하고 아카이브하는 히스토리 서비스가 포함될 수도 있습니다. 이러한 배치 패턴의 다른 유용한 컴포넌트는 GPS 위치 서비스입니다.

이 디자인을 사용하여 각 개별 서비스 컨테이너를 독립적으로 업데이트할 수 있습니다. 코드 변경 없이 각 개별 서비스를 재구성하고 다른 유용한 배치 패턴으로 구성할 수도 있습니다. 필요한 경우 서드파티 분석 서비스를 패턴에 추가할 수 있습니다. 이 서드파티 서비스에는 특정 읽기 전용 API 세트에 대한 액세스만 부여될 수 있으므로 서비스가 플랫폼의 작동기와 상호작용하는 것이 제한됩니다.

또는 이 산업용 제어기 예제의 모든 태스크가 단일 서비스 컨테이너 내에서 실행될 수 있습니다. 일반적으로 더 작은 독립적이고 상호 연결된 서비스의 콜렉션을 사용하면 소프트웨어 업데이트가 보다 빠르고 유연해지기 때문에 이 대안은 일반적으로 최상의 접근 방식이 아닙니다. 소규모 서비스의 콜렉션은 현장에서 더 강력할 수 있습니다. 배치 패턴을 디자인하는 방법에 대한 자세한 정보는 [에지 네이티브 개발 사례](best_practices.md)를 참조하십시오.

## 샌드박스
{: #sandbox}

배치 패턴이 실행되는 샌드박스는 서비스 컨테이너에서 제공되는 API에 대한 액세스를 제한합니다. 명시적으로 서비스에 대한 종속성을 언급하는 다른 서비스에만 액세스가 허용됩니다. 일반적으로 호스트의 기타 프로세스는 이러한 서비스에 액세스하지 않습니다. 마찬가지로, 서비스가 명시적으로 포트를 호스트의 외부 네트워크 인터페이스에 공개하지 않으면 일반적으로 다른 원격 호스트가 이러한 서비스에 액세스할 수 없습니다.

## 다른 서비스를 사용하는 서비스
{: #using_services}

에지 서비스는 종종 다른 에지 서비스에서 제공되는 다양한 API 인터페이스를 사용하여 해당 서비스에서 데이터를 가져오거나 해당 서비스에 제어 명령을 전달합니다. 일반적으로 이러한 API 인터페이스는 `cpu2evtstreams` 예제의 하위 레벨 `cpu` 및 `gps` 서비스에서 제공되는 것과 같은 HTTP REST API입니다. 그러나 이러한 인터페이스는 실제로 공유 메모리, TCP 또는 UDP와 같이 사용자가 원하는 모든 것이 될 수 있고 암호화되거나 암호화되지 않을 수 있습니다. 이와 같은 통신은 일반적으로 단일 에지 노드 내에서 발생하여 메시지가 이 호스트를 벗어나지 않기 때문에 종종 암호화가 필요하지 않습니다.

REST API에 대한 대안으로, MQTT에서 제공되는 인터페이스와 같은 발행 및 구독 인터페이스를 사용할 수 있습니다. 서비스가 간헐적으로만 데이터를 제공하는 경우, REST API가 제한시간을 초과할 수 있으므로 REST API를 반복적으로 폴링하는 것보다 공개 및 등록 인터페이스가 보통 더 간단합니다. 예를 들어, 하드웨어 단추를 모니터하고 다른 서비스가 단추 누름이 발생했는지 여부를 감지할 수 있는 API를 제공하는 서비스가 있다고 가정하십시오. REST API가 사용되는 경우 호출자는 REST API를 호출하고 단추를 누르면 오는 응답을 대기할 수 없습니다. 단추가 눌리지 않은 상태로 너무 오래 유지되면 REST API가 제한시간을 초과할 수 있습니다. 대신, API 제공자가 오류를 피하기 위해 즉시 응답해야 할 수 있습니다. 짧은 단추 누름을 놓치지 않으려면 호출자가 반복적으로 자주 API를 호출해야 합니다. 더 나은 솔루션은 호출자가 발행/구독 서비스 및 블록에서 적절한 토픽을 구독하는 것입니다. 그런 다음, 호출자가 향후에 발생할 수 있는 항목이 발행될 때까지 대기할 수 있습니다. API 제공자가 주의하여 단추 누름을 모니터한 후 `button pressed` 또는 `button released`와 같은 해당 토픽에 대한 상태 변경사항만 공개할 수 있습니다.

MQTT는 사용할 수 있는 가장 인기 있는 발행 및 구독 도구 중 하나입니다. MQTT 브로커를 에지 서비스로 배치하고 발행자 및 구독자 서비스에서 이를 필요로 하도록 할 수 있습니다. MQTT는 흔히 클라우드 서비스로도 사용됩니다. 예를 들어, IBM Watson IoT Platform은 MQTT를 사용하여 IoT 디바이스와 통신합니다. 자세한 정보는 [IBM Watson IoT Platform ![새 탭에서 열림](../../images/icons/launch-glyph.svg "새 탭에서 열림")](https://www.ibm.com/cloud/watson-iot-platform)을 참조하십시오. 일부 {{site.data.keyword.horizon_open}} 프로젝트 예제에서 MQTT를 사용합니다. 자세한 정보는 [{{site.data.keyword.horizon_open}} 예제](https://github.com/open-horizon/examples)를 참조하십시오.

인기 있는 다른 발행 및 구독 도구는 흔히 클라우드 서비스로도 사용되는 Apache Kafka입니다. `cpu2evtstreams` 예제에서 {{site.data.keyword.cloud_notm}}에 데이터를 전송하는 데 사용되는 {{site.data.keyword.message_hub_notm}}도 Kafka를 기반으로 합니다. 자세한 정보는 [{{site.data.keyword.message_hub_notm}} ![새 탭에서 열림](../../images/icons/launch-glyph.svg "새 탭에서 열림")](https://www.ibm.com/cloud/event-streams)의 내용을 참조하십시오.

모든 에지 서비스 컨테이너는 동일한 호스트의 다른 로컬 에지 서비스 및 로컬 LAN의 인근 호스트에서 제공되는 에지 서비스를 제공하거나 이용할 수 있습니다. 컨테이너는 원격 기업 또는 클라우드 제공자 데이터 센터의 중앙 집중식 시스템과 통신할 수 있습니다. 서비스 작성자가 서비스와 통신하는 대상과 방법을 판별합니다.

`cpu2evtstreams` 예제를 다시 검토하여 예제 코드가 다른 두 개의 로컬 서비스를 사용하는 방법을 확인하는 것이 유용할 수 있습니다. 예를 들어, 예제 코드가 두 개의 로컬 서비스에 대한 종속성을 지정하고, 구성 변수를 선언하여 사용하고, Kafka와 통신하는 방법입니다. 자세한 정보는 [`cpu2evtstreams` 예제](cpu_msg_example.md)를 참조하십시오.

## 서비스 정의
{: #service_definition}

참고: 명령 구문에 대한 자세한 정보는 [이 문서에서 사용된 규칙](../../getting_started/document_conventions.md)을 참조하십시오.

모든 {{site.data.keyword.ieam}} 프로젝트에 `horizon/service.definition.json` 파일이 있습니다. 이 파일은 두 가지 이유로 에지 서비스를 정의합니다. 한 가지 이유는 {{site.data.keyword.horizon_agent}}에서 실행되는 방법과 유사하게 `hzn dev` 도구를 통한 서비스 실행을 시뮬레이션할 수 있도록 하는 것입니다. 이 시뮬레이션은 포트 바인딩 및 하드웨어 디바이스 액세스와 같이 사용자에게 필요할 수 있는 특수 배치 지시사항을 수행하는 데 유용합니다. 또한 시뮬레이션은 에이전트가 작성하는 Docker 가상 사설망(VPN)에서 이루어지는 서비스 컨테이너 간 통신을 확인하는 데 유용합니다. 이 파일의 다른 이유는 서비스를 {{site.data.keyword.horizon_exchange}}에 공개할 수 있도록 하는 것입니다. 제공된 예제에서 `horizon/service.definition.json` 파일은 예제 GitHub 저장소 내에서 제공되거나 `hzn dev service new` 명령에 의해 생성됩니다.

예제 서비스 구현(예: [cpu2evtstreams](https://github.com/open-horizon/examples/blob/master/edge/evtstreams/cpu2evtstreams/horizon/service.definition.json))에 대한 {{site.data.keyword.horizon}} 메타데이터가 포함된 `horizon/service.definition.json` 파일을 여십시오.

{{site.data.keyword.horizon}}에서 공개된 모든 서비스에는 조직 내에서 서비스를 고유하게 식별하는 `url`이 있어야 합니다. 이 필드는 URL이 아닙니다. 대신 `url` 필드는 조직 이름과 특정 구현 `version` 및 `arch` 필드와 함께 결합될 때 GUID(Globally Unique Identifier)를 형성합니다. `horizon/service.definition.json` 파일을 편집하여 `url` 및 `version`에 적절한 값을 제공할 수 있습니다. `version` 값에는 시맨틱 버전화 스타일 값을 사용하십시오. 서비스 컨테이너를 푸시, 서명 및 공개할 때 새로운 값을 사용하십시오. 또는 `horizon/hzn.json` 파일을 편집할 수 있습니다. 그러면 도구가 `horizon/service.definition.json` 파일에서 사용된 변수 참조 대신 이 파일에서 찾은 변수값을 대체합니다.

`horizon/service.definition.json` 파일의 `requiredServices` 섹션에는 이 컨테이너가 사용하는 다른 에지 서비스와 같은 서비스 종속 항목이 항목별로 작성됩니다. `hzn dev dependency fetch` 도구를 사용하면 이 목록에 종속 항목을 추가할 수 있으므로, 목록을 수동으로 편집할 필요가 없습니다. 종속 항목을 추가한 후 에이전트가 컨테이너를 실행하는 경우, 기타 `requiredServices`도 자동으로 실행됩니다(예를 들어 `hzn dev service start`를 사용하거나 이 서비스가 포함되는 배치 패턴이 있는 노드를 등록하는 경우). 필수 서비스에 대한 자세한 정보는 [cpu2evtstreams](cpu_msg_example.md)를 참조하십시오.

`userInput` 섹션에서는 해당 서비스가 특정 배치에 맞게 자체를 구성하기 위해 이용할 수 있는 구성 변수를 선언합니다. 여기에 변수 이름, 데이터 유형 및 기본값을 제공하며 각각에 대한 사용자가 읽을 수 있는 설명을 제공할 수도 있습니다. `hzn dev service start`를 사용하거나 이 서비스를 포함하는 배치 패턴에 에지 노드를 등록하는 경우 기본값이 없는 변수에 대해 값을 정의하기 위해 `userinput.json` 파일을 제공해야 합니다. `userInput` 구성 변수 및 `userinput.json` 파일에 대한 자세한 정보는 [cpu2evtstreams](cpu_msg_example.md)를 참조하십시오.

`horizon/service.definition.json` 파일에는 파일의 끝부분에 `deployment` 섹션이 포함되어 있습니다. 이 섹션의 필드는 논리 서비스를 구현하는 각 Docker 컨테이너 이미지에 이름을 지정합니다. 여기서 사용되는 `services` 배열의 각 레코드 이름은 다른 컨테이너가 공유 가상 사설망(VPN)에서 컨테이너를 식별하는 데 사용하는 이름입니다. 이 컨테이너가 다른 컨테이너에서 이용할 REST API를 제공하는 경우 `curl http://<name>/<your-rest-api-uri>`를 사용하여 이용하는 컨테이너 내에서 이 REST API에 액세스할 수 있습니다. 각 이름의 `image` 필드는 해당 Docker 컨테이너 이미지에 대한 참조를 제공합니다(예: DockerHub 또는 일부 사설 컨테이너 레지스트리 내부). `deployment` 섹션의 다른 필드는 에이전트가 Docker에 컨테이너를 실행하도록 표시하는 방법을 변경하는 데 사용될 수 있습니다. 자세한 정보는 [{{site.data.keyword.horizon}} deployment strings ![새 탭에서 열림](../../images/icons/launch-glyph.svg "새 탭에서 열림")](https://github.com/open-horizon/anax/blob/master/doc/deployment_string.md)를 참조하십시오.

## {{site.data.keyword.horizon_exchange}}와의 상호작용
{: #horizon_exchange}

예제 프로그램을 빌드하고 공개할 때 {{site.data.keyword.horizon_exchange}}와 상호작용하여 서비스, 정책 및 배치 패턴을 공개합니다. 또한 {{site.data.keyword.horizon_exchange}}를 사용하여 특정 배치 패턴을 실행하도록 에지 노드를 등록합니다. {{site.data.keyword.horizon_exchange}}는 공유 정보에 대한 저장소 역할을 하며, 이를 통해 {{site.data.keyword.ieam}}의 다른 컴포넌트와 간접적으로 통신할 수 있습니다. 개발자는 {{site.data.keyword.horizon_exchange}}에 대해 작업하는 방법을 이해해야 합니다.

이 다이어그램은 모든 에지 노드 내부에서 실행 중이어야 하는 에이전트와 일반적으로 클라우드 또는 중앙 집중식 기업 데이터 센터에서 모든 배치 패턴에 대해 구성되어야 하는 agbot을 보여줍니다.

{{site.data.keyword.ieam}} 개발자는 일반적으로 `hzn` 명령을 사용하여 {{site.data.keyword.horizon_exchange}}와 상호작용합니다. 특히 `hzn exchange` 명령은 {{site.data.keyword.horizon_exchange}}와의 모든 상호작용에 사용됩니다. `hzn exchange --help`를 입력하면 명령행에서 `hzn exchange` 다음에 올 수 있는 모든 하위 명령을 볼 수 있습니다. 그런 다음, `hzn exchange <subcommand> --help`를 사용하여 선택한 `<subcommand>`에 대한 세부사항을 가져올 수 있습니다.

다음 명령은 {{site.data.keyword.horizon_exchange}}를 조사하는 데 유용합니다.

* 사용자 인증 정보가 {{site.data.keyword.horizon_exchange}}에서 작동하는지 확인: `hzn exchange user list`
* {{site.data.keyword.horizon_exchange}} 소프트웨어 버전 확인: `hzn exchange version`
* 현재 {{site.data.keyword.horizon_exchange}} 상태 확인: `hzn exchange status`
* 조직 아래에 작성된 모든 에지 노드 나열: `hzn exchange node list`
* 특정 에지 노드에 대한 세부사항 검색: `hzn exchange node list <node-id>`.
  `<node-id>`를 에지 노드의 ID 값으로 바꾸십시오.
* 조직 아래에 공개된 모든 서비스 나열: `hzn exchange service list`
* 조직 아래에 공개된 모든 공용 서비스 나열: `hzn exchange service list '<org>/*'`
* 공개된 특정 서비스에 대한 세부사항 검색: `hzn exchange service list <org/service>`
* 조직 아래에 공개된 모든 배치 패턴 나열: `hzn exchange pattern list`
* 조직 아래에 공개된 모든 공용 배치 패턴 나열: `hzn exchange pattern list '<org>/*'`
* 공개된 특정 서비스에 대한 모든 세부사항 나열: `hzn exchange pattern list <org/pattern>`

## 에이전트 및 agbot
{: #agents_agbots}

에이전트 및 agbot의 역할과 에이전트와 agbot이 통신하는 정확한 방식을 이해하는 것은 중요합니다. 이 지식은 문제점이 발생했을 때 문제점을 진단하고 수정하는 데 도움이 될 수 있습니다.

에이전트와 agbot은 서로 직접 통신하지 않습니다. 각 에지 노드의 에이전트가 {{site.data.keyword.horizon_switch}}에 자체 메일함을 설정하고 {{site.data.keyword.horizon_exchange}}에 노드 리소스를 작성해야 합니다. 그런 다음, 특정 배치 패턴을 실행하려고 할 때 {{site.data.keyword.horizon_exchange}}에 있는 이 패턴에 자체적으로 등록합니다.

agbot은 패턴을 모니터하고 {{site.data.keyword.horizon_exchange}}를 지속적으로 검색하여 패턴에 대해 등록하는 에지 노드를 찾습니다. 새 에지 노드가 패턴을 사용하기 위해 등록하는 경우 agbot은 해당 에지 노드의 로컬 에이전트에 접속합니다. agbot이 {{site.data.keyword.horizon_switch}}를 통해 접속합니다. 이제 agbot이 에이전트에 대해 알 수 있는 것은 공개 키뿐입니다. agbot은 에지 노드의 IP 주소 또는 에지 노드가 특정 배치 패턴에 등록되었다는 사실 이외에 에지 노드에 대한 다른 어떤 것도 알지 못합니다. agbot은 {{site.data.keyword.horizon_switch}}를 통해 에이전트에 통신하여 이 에지 노드에 대한 이 배치 패턴의 소프트웨어 라이프사이클을 관리하기 위해 협업하도록 제안합니다.

각 에지 노드의 에이전트가 {{site.data.keyword.horizon_switch}}를 모니터하여 메일함에 메시지가 있는지 확인합니다. 에이전트가 agbot으로부터 제안을 받으면 에지 노드가 구성될 때 에지 노드 소유자가 설정한 정책을 기반으로 이 제안을 평가하여 제안을 수락할지 또는 거부할지 여부를 선택합니다.

배치 패턴 제안이 수락되면 에이전트가 적절한 Docker 레지스트리에서 적절한 서비스 컨테이너를 가져오고, 서비스 서명을 확인하고, 서비스를 구성하고, 서비스를 실행합니다.

{{site.data.keyword.horizon_switch}}를 통과하는 에이전트와 agbot 간의 모든 통신은 두 참가자에 의해 암호화됩니다. 이러한 메시지는 중앙 {{site.data.keyword.horizon_switch}}에 저장되지만 {{site.data.keyword.horizon_switch}}는 해당 대화를 복호화하고 도청할 수 없습니다.

## 서비스 소프트웨어 업데이트 배치
{: #deploy_edge_updates}

에지 노드 집합에 소프트웨어를 배치한 후 코드를 업데이트할 수 있습니다. {{site.data.keyword.ieam}}을 사용하여 소프트웨어 업데이트를 수행할 수 있습니다. 일반적으로 에지 노드에서 실행되는 소프트웨어를 업데이트하기 위해 에지 노드에서 아무것도 수행할 필요가 없습니다. 업데이트에 서명하고 공개하자마자 각 에지 노드에서 실행되는 agbot과 에이전트가 업데이트된 배치 패턴에 등록된 모든 에지 노드에 최신 버전의 배치 패턴을 배치하도록 조정합니다. {{site.data.keyword.ieam}}의 주요 이점 중 하나는 에지 노드까지의 소프트웨어 업데이트 파이프라인을 용이하게 한다는 점입니다.

새 버전의 소프트웨어를 릴리스하려면 다음 단계를 완료하십시오. 

* 이 업데이트에 대해 원하는 대로 서비스 코드를 편집하십시오.
* 코드의 시맨틱 버전 번호를 편집하십시오.
* 서비스 컨테이너를 다시 빌드하십시오.
* 업데이트된 서비스 컨테이너를 적절한 Docker 레지스트리에 푸시하십시오.
* 업데이트된 서비스에 서명하고 {{site.data.keyword.horizon_exchange}}에 다시 공개하십시오.
* {{site.data.keyword.horizon_exchange}}에서 배치 패턴을 다시 공개하십시오. 동일한 이름을 사용하고 새 서비스 버전 번호를 참조하십시오.

{{site.data.keyword.horizon}} agbot은 배치 패턴 변경사항을 빠르게 발견합니다. 그런 다음, agbot은 에지 노드가 배치 패턴을 실행하도록 등록된 각 에이전트에 접속합니다. agbot 및 에이전트가 연계하여 새 컨테이너를 다운로드하고 이전 컨테이너를 중지 및 제거하며 새 컨테이너를 시작합니다.

이 프로세스로 인해 업데이트된 배치 패턴을 빠르게 실행하도록 등록된 모든 에지 노드가 지리적 위치에 관계없이 새 서비스 컨테이너 버전을 실행합니다.

## 다음에 수행할 작업
{: #developing_what_next}

에지 노드 코드 개발에 대한 자세한 정보는 다음 문서를 검토하십시오.

[에지 네이티브 개발 사례](best_practices.md)

{{site.data.keyword.ieam}} 소프트웨어 개발의 경우 에지 서비스 개발을 위한 중요한 원칙 및 우수 사례를 검토하십시오.

[{{site.data.keyword.cloud_registry}} 사용](container_registry.md)

{{site.data.keyword.ieam}}을 사용하면 선택적으로 공용 Docker 허브 대신 IBM 개인용 보안 컨테이너 레지스트리에 서비스 컨테이너를 배치할 수 있습니다. 예를 들어, 공용 레지스트리에 포함하기에 적합하지 않은 자산이 포함된 소프트웨어 이미지가 있는 경우 {{site.data.keyword.cloud_registry}}와 같은 개인용 Docker 컨테이너 레지스트리를 사용할 수 있습니다.

[ API](../installing/edge_rest_apis.md)

{{site.data.keyword.ieam}}은 컴포넌트가 협업하고 조직의 개발자와 사용자가 컴포넌트를 제어할 수 있도록 RESTful API를 제공합니다.
