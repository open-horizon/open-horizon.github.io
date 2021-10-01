---

copyright:
years: 2020
lastupdated: "2020-02-5" 

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 소프트웨어 정의 라디오 에지 처리
{: #defined_radio_ex}

이 예제에서는 소프트웨어 정의 라디오(SDR)를 에지 처리의 예제로 사용합니다. SDR을 사용하면 처리를 위해 클라우드 서버에 전체 라디오 스펙트럼의 원시 데이터를 전송할 수 있습니다. 에지 노드가 로컬로 데이터를 처리한 후 추가 처리를 위해 더 적은 볼륨의 고부가 가치 데이터를 클라우드 처리 서비스에 전송합니다.
{:shortdesc}

이 다이어그램은 이 SDR 예제에 대한 아키텍처를 표시합니다.

<img src="../OH/docs/images/edge/08_sdrarch.svg" style="margin: 3%" alt="Example architecture">

SDR 에지 처리는 라디오 스테이션 오디오를 이용하고 음성을 추출하며 추출된 음성을 텍스트로 변환하는 모든 기능을 갖춘 예제입니다. 이 예제는 텍스트에 대한 감성 분석을 완료하고 각 에지 노드에 대한 데이터의 세부사항을 볼 수 있는 사용자 인터페이스를 통해 데이터 및 결과를 사용할 수 있도록 합니다. 에지 처리에 대해 자세히 알아보려면 이 예제를 사용하십시오.

SDR은 컴퓨터 CPU의 디지털 회로를 통해 무선 신호를 수신하여 일련의 특수 아날로그 회로가 필요한 작업을 처리합니다. 일반적으로 이 아날로그 회로는 수신할 수 있는 전파 스펙트럼의 폭에 따라 제한됩니다. 예를 들어, FM 라디오 스테이션을 수신하도록 빌드된 아날로그 라디오 수신기는 라디오 스펙트럼의 다른 위치에서 무선 신호를 수신할 수 없습니다. SDR은 대부분의 스펙트럼에 액세스할 수 있습니다. SDR 하드웨어가 없는 경우 모의 데이터를 사용할 수 있습니다. 모의 데이터를 사용하는 경우 인터넷 스트림의 오디오가 FM을 통해 브로드캐스트되고 에지 노드에 수신된 것처럼 처리합니다.

이 태스크를 수행하기 전에 [에이전트 설치](registration.md)의 단계를 수행하여 에지 디바이스를 등록 및 등록 취소하십시오.

해당 코드는 이러한 기본 컴포넌트를 포함합니다.

|컴포넌트|설명|
|---------|-----------|
|[sdr 서비스](https://github.com/open-horizon/examples/tree/master/edge/services/sdr)|하위 레벨 서비스가 에지 노드의 하드웨어에 액세스함|
|[ssdr2evtstreams 서비스](https://github.com/open-horizon/examples/tree/master/edge/evtstreams/sdr2evtstreams)|상위 레벨 서비스는 하위 레벨 sdr 서비스에서 데이터를 수신하고 에지 노드에서 로컬 데이터 분석을 완료합니다. 그런 다음 sdr2evtstreams 서비스가 처리된 데이터를 클라우드 백엔드 소프트웨어로 전송합니다.|
|[클라우드 백엔드 소프트웨어](https://github.com/open-horizon/examples/tree/master/cloud/sdr)|클라우드 백엔드 소프트웨어는 추가 분석을 위해 에지 노드에서 데이터를 수신합니다. 그런 다음, 백엔드 구현이 웹 기반 UI 내에 에지 노드의 맵 등을 제공할 수 있습니다.|
{: caption="표 1. {{site.data.keyword.message_hub_notm}} 기본 컴포넌트에 대한 소프트웨어 정의 라디오" caption-side="top"}

## 디바이스 등록

에지 디바이스에서 모의 데이터를 사용하여 이 서비스를 실행할 수 있지만 SDR 하드웨어와 함께 Raspberry Pi와 같은 에지 디바이스를 사용하는 경우 먼저 SDR 하드웨어를 지원하도록 커널 모듈을 구성하십시오. 수동으로 이 모듈을 구성해야 합니다. Docker 컨테이너가 해당 컨텍스트에서 다른 Linux 배포를 설정할 수 있지만 컨테이너가 커널 모듈을 설치할 수 없습니다. 

이 모듈을 구성하려면 다음 단계를 완료하십시오.

1. 루트 사용자로 `/etc/modprobe.d/rtlsdr.conf`라는 파일을 작성하십시오.
   ```
   sudo nano /etc/modprobe.d/rtlsdr.conf
   ```
   {: codeblock}

2. 다음 행을 파일에 추가하십시오.
   ```
   blacklist rtl2830      blacklist rtl2832      blacklist dvb_usb_rtl28xxu
   ```
   {: codeblock}

3. 파일을 저장한 후 계속하기 전에 다시 시작하십시오.
   ```
   sudo reboot
   ```
   {: codeblock}   

4. 사용자 환경에서 다음 {{site.data.keyword.message_hub_notm}} API 키를 설정하십시오. 이 키는 이 예제에 사용하기 위해 작성되고 IBM 소프트웨어 정의 라디오 UI에 대해 에지 노드에서 수집한 처리 데이터를 피드하는 데 사용됩니다.
   ```
   export EVTSTREAMS_API_KEY=X2e8cSjbDAMk-ztJLaoi3uffy8qsQTnZttUjcHCfm7cp     export EVTSTREAMS_BROKER_URL=broker-3-y420pyyyvhhmttz0.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-5-y420pyyyvhhmttz0.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-4-y420pyyyvhhmttz0.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-1-y420pyyyvhhmttz0.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-0-y420pyyyvhhmttz0.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-2-y420pyyyvhhmttz0.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093
   ```
   {: codeblock}

5. 에지 노드에서 sdr2evtstreams 서비스 예제를 실행하려면 IBM/pattern-ibm.sdr2evtstreams 배치 패턴을 사용하여 에지 노드를 등록해야 합니다. [SDR 대 IBM Event Streams 예제 에지 서비스 사용을 위한 전제조건](https://www.ibm.com/links?url=https%3A%2F%2Fgithub.com%2Fopen-horizon%2Fexamples%2Ftree%2Fmaster%2Fedge%2Fevtstreams%2Fsdr2evtstreams)의 단계를 수행하십시오.

6. 예제 웹 UI에서 에지 노드가 결과를 전송하고 있는지 확인하십시오. 

## SDR 구현 세부사항

### sdr 하위 레벨 서비스
{: #sdr}

이 서비스에 대한 소프트웨어 스택의 최하위 레벨에는 `sdr` 서비스 구현이 포함됩니다. 이 서비스는 인기 있는 `librtlsdr` 라이브러리와 파생된 `rtl_fm` 및 `rtl_power` 유틸리티를 `rtl_rpcd` 디먼과 함께 사용하여 로컬 소프트웨어 정의 라디오 하드웨어에 액세스합니다. `librtlsdr` 라이브러리에 대한 자세한 정보는 [librtlsdr](https://github.com/librtlsdr/librtlsdr)을 참조하십시오.

`sdr` 서비스는 소프트웨어 정의 라디오 하드웨어를 직접 제어하여 전송된 데이터를 수신하거나 지정된 스펙트럼에서 신호 강도를 측정하기 위해 하드웨어를 특정 주파수에 맞게 조정합니다. 서비스의 일반 워크플로우를 특정 주파수에 맞게 조정하여 해당 주파수의 스테이션에서 데이터를 수신하도록 할 수 있습니다. 그런 다음, 서비스가 수집된 데이터를 처리할 수 있습니다.

### sdr2evtstreams 상위 레벨 서비스
{: #sdr2evtstreams}

`sdr2evtstreams` 상위 레벨 서비스 구현은 로컬 사설 가상 Docker 네트워크를 통해 `sdr` 서비스 REST API 및 `gps` 서비스 REST API를 모두 사용합니다. `sdr2evtstreams` 서비스는 `sdr` 서비스로부터 데이터를 수신하고 데이터에 대한 일부 로컬 추론을 완료하여 음성에 가장 적합한 스테이션을 선택합니다. 그런 다음, `sdr2evtstreams` 서비스가 Kafka를 사용하여 {{site.data.keyword.message_hub_notm}}를 통해 오디오 클립을 클라우드에 발행합니다.

### IBM Functions
{: #ibm_functions}

IBM Functions는 예제 소프트웨어 정의 라디오 애플리케이션의 클라우드 측을 오케스트레이션합니다. IBM Functions는 OpenWhisk를 기반으로 하며 서버리스 컴퓨팅을 사용합니다. 서버리스 컴퓨팅은 운영 체제 또는 프로그래밍 언어 시스템과 같은 지원 인프라 없이 코드 컴포넌트를 배치할 수 있음을 의미합니다. IBM Functions를 사용하면 사용자 고유의 코드에 집중하고 다른 모든 항목의 스케일링, 보안 및 지속적인 유지보수는 IBM에서 처리하도록 할 수 있습니다. 프로비저닝할 하드웨어, VM 및 컨테이너가 필요하지 않습니다.

서버리스 코드 컴포넌트는 이벤트에 대한 응답으로 트리거(실행)되도록 구성됩니다. 이 예제에서는 에지 노드가 {{site.data.keyword.message_hub_notm}}에 오디오 클립을 게시할 때마다 {{site.data.keyword.message_hub_notm}}의 에지 노드로부터 메시지를 수신하는 것이 트리거 이벤트입니다. 예제 조치는 데이터를 수집하고 데이터에 대한 조치를 수행하기 위해 트리거됩니다. 예제 조치에서는 IBM Watson Speech-To-Text(STT) 서비스를 사용하여 수신 오디오 데이터를 텍스트로 변환합니다. 그런 다음, 텍스트에 포함된 각 명사에 표시되는 감성을 분석하기 위해 해당 텍스트가 IBM Watson Natural Language Understanding(NLU) 서비스로 전송됩니다. 자세한 정보는 [IBM Functions 조치 코드](https://github.com/open-horizon/examples/blob/master/cloud/sdr/data-processing/ibm-functions/actions/msgreceive.js)를 참조하십시오.

### IBM 데이터베이스
{: #ibm_database}

IBM Functions 조치 코드는 계산된 감성 결과를 IBM 데이터베이스로 저장하여 완성됩니다. 그런 다음, 웹 서버 및 클라이언트 소프트웨어가 이 데이터를 데이터베이스에서 사용자 웹 브라우저에 제공하는 작업을 수행합니다.

### 웹 인터페이스
{: #web_interface}

소프트웨어 정의 라디오 애플리케이션의 웹 사용자 인터페이스를 사용하면 사용자가 IBM 데이터베이스에서 제공되는 감성 데이터를 찾아볼 수 있습니다. 또한 이 사용자 인터페이스는 데이터를 제공한 에지 노드를 표시하는 맵을 렌더링합니다. 맵은 IBM 제공 `gps` 서비스의 데이터로 작성되며, 이 서비스는 `sdr2evtstreams` 서비스에 대한 에지 노드 코드에서 사용됩니다. `gps` 서비스는 위치에 대해 GPS 하드웨어와 인터페이스하거나 디바이스 소유자로부터 정보를 수신할 수 있습니다. GPS 하드웨어 및 디바이스 소유자 위치가 둘 다 없으면 `gps` 서비스가 에지 노드 IP 주소로 지리적 위치를 찾아서 에지 노드 위치를 추정할 수 있습니다. 서비스가 오디오 클립을 전송할 때 `sdr2evtstreams`가 이 서비스를 사용하여 클라우드에 위치 데이터를 제공할 수 있습니다. 자세한 정보는 [소프트웨어 정의 라디오 애플리케이션 웹 UI 코드](https://github.com/open-horizon/examples/tree/master/cloud/sdr/ui/sdr-app)를 참조하십시오.

고유한 소프트웨어 정의 비율 예제 웹 UI를 작성하려는 경우 선택적으로 IBM Functions, IBM 데이터베이스, 웹 UI 코드를 배치할 수 있습니다. [유료 계정을 작성](https://cloud.ibm.com/login)한 후에 하나의 명령으로 이를 수행할 수 있습니다. 자세한 정보는 [배치 저장소 컨텐츠](https://www.ibm.com/links?url=https%3A%2F%2Fgithub.com%2Fopen-horizon%2Fexamples%2Ftree%2Fmaster%2Fcloud%2Fsdr%2Fdeploy%2Fibm)를 참조하십시오. 

**참고**: 이 배치 프로세스를 수행하려면 {{site.data.keyword.cloud_notm}} 계정에 비용이 부과되는 유료 서비스가 필요합니다.

## 다음에 수행할 작업

고유한 소프트웨어를 에지 노드에 배치하려는 경우 고유한 에지 서비스, 연관 배치 패턴 또는 배치 정책을 작성해야 합니다. 자세한 정보는 [디바이스를 위한 에지 서비스 개발](../OH/docs/developing/developing.md)을 참조하십시오.
