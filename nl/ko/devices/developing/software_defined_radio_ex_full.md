---

copyright:
years: 2019
lastupdated: "2019-06-26"

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

***작성자 참고: Troy가 결합되면 이는 software_defined_radio_ex.md와 병합됩니다.***

이 예제에서는 소프트웨어 정의 라디오(SDR)를 에지 처리의 예제로 사용합니다. SDR을 사용하면 처리를 위해 클라우드 서버에 전체 라디오 스펙트럼의 원시 데이터를 전송할 수 있습니다. 에지 노드가 로컬로 데이터를 처리한 후 추가 처리를 위해 더 적은 볼륨의 고부가 가치 데이터를 클라우드 처리 서비스에 전송합니다.
{:shortdesc}

이 다이어그램은 이 SDR 예제에 대한 아키텍처를 표시합니다.

<img src="../../images/edge/08_sdrarch.svg" width="70%" alt="예제 아키텍처">

SDR 에지 처리는 라디오 스테이션 오디오를 이용하고 음성을 추출하며 추출된 음성을 텍스트로 변환하는 모든 기능을 갖춘 예제입니다. 이 예제는 텍스트에 대한 감성 분석을 완료하고 각 에지 노드에 대한 데이터의 세부사항을 볼 수 있는 사용자 인터페이스를 통해 데이터 및 결과를 사용할 수 있도록 합니다. 에지 처리에 대해 자세히 알아보려면 이 예제를 사용하십시오.

SDR은 컴퓨터 CPU의 디지털 회로를 통해 무선 신호를 수신하여 일련의 특수 아날로그 회로가 필요한 작업을 처리합니다. 일반적으로 이 아날로그 회로는 수신할 수 있는 전파 스펙트럼의 폭에 따라 제한됩니다. 예를 들어, FM 라디오 스테이션을 수신하도록 빌드된 아날로그 라디오 수신기는 라디오 스펙트럼의 다른 위치에서 무선 신호를 수신할 수 없습니다. SDR은 대부분의 스펙트럼에 액세스할 수 있습니다. SDR 하드웨어가 없는 경우 모의 데이터를 사용할 수 있습니다. 모의 데이터를 사용하는 경우 인터넷 스트림의 오디오가 FM을 통해 브로드캐스트되고 에지 노드에 수신된 것처럼 처리합니다.

이 태스크를 수행하기 전에 [에지 디바이스에서 Horizon 에이전트 설치 및 hello world 예제에 등록](registration.md)의 단계를 수행하여 에지 디바이스를 등록 및 등록 취소할 수 있습니다.

해당 코드는 이러한 기본 컴포넌트를 포함합니다.

|컴포넌트|설명|
|---------|-----------|
|[sdr 서비스 ![새 탭에서 열림](../../images/icons/launch-glyph.svg "새 탭에서 열림")](https://github.com/open-horizon/examples/tree/master/edge/services/sdr)|하위 레벨 서비스가 에지 노드의 하드웨어에 액세스함|
|[ssdr2evtstreams 서비스 ![새 탭에서 열림](../../images/icons/launch-glyph.svg "새 탭에서 열림")](https://github.com/open-horizon/examples/tree/master/edge/evtstreams/sdr2evtstreams)|상위 레벨 서비스는 하위 레벨 sdr 서비스에서 데이터를 수신하고 에지 노드에서 로컬 데이터 분석을 완료합니다. 그런 다음 sdr2evtstreams 서비스가 처리된 데이터를 클라우드 백엔드 소프트웨어로 전송합니다.|
|[클라우드 백엔드 소프트웨어 ![새 탭에서 열림](../../images/icons/launch-glyph.svg "새 탭에서 열림")](https://github.com/open-horizon/examples/tree/master/cloud/sdr)|클라우드 백엔드 소프트웨어는 추가 분석을 위해 에지 노드에서 데이터를 수신합니다. 그런 다음, 백엔드 구현이 웹 기반 UI 내에 에지 노드의 맵 등을 제공할 수 있습니다.|
{: caption="표 1. {{site.data.keyword.message_hub_notm}} 기본 컴포넌트에 대한 소프트웨어 정의 라디오" caption-side="top"}

## 디바이스 등록

이 서비스는 에지 디바이스에서 모의 데이터를 사용하여 실행할 수 있지만 SDR 하드웨어와 함께 Raspberry Pi와 같은 에지 디바이스를 사용하는 경우 먼저 SDR 하드웨어를 지원하도록 커널 모듈을 구성하십시오. 수동으로 이 모듈을 구성해야 합니다. Docker 컨테이너가 해당 컨텍스트에서 다른 Linux 배포를 설정할 수 있지만 컨테이너가 커널 모듈을 설치할 수 없습니다. 

이 모듈을 구성하려면 다음 단계를 완료하십시오.

1. 루트 사용자로 `/etc/modprobe.d/rtlsdr.conf`라는 파일을 작성하십시오.

   ```
     sudo nano /etc/modprobe.d/rtlsdr.conf
   ```
   {: codeblock}

2. 다음 행을 파일에 추가하십시오.

   ```
     blacklist rtl2830
     blacklist rtl2832
     blacklist dvb_usb_rtl28xxu
   ```
   {: codeblock}

3. 파일을 저장한 후 계속하기 전에 다시 시작하십시오.
   ```
    sudo reboot
   ```
   {: codeblock}   

4. 사용자 환경에서 다음 {{site.data.keyword.message_hub_notm}} API 키를 설정하십시오. 이 키는 이 예제에 사용하기 위해 작성되고 IBM 소프트웨어 정의 라디오 UI에 대해 에지 노드에서 수집한 처리 데이터를 피드하는 데 사용됩니다.

   ```
    export EVTSTREAMS_API_KEY=X2e8cSjbDAMk-ztJLaoi3uffy8qsQTnZttUjcHCfm7cp
    export EVTSTREAMS_BROKER_URL=broker-3-y420pyyyvhhmttz0.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-5-y420pyyyvhhmttz0.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-4-y420pyyyvhhmttz0.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-1-y420pyyyvhhmttz0.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-0-y420pyyyvhhmttz0.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-2-y420pyyyvhhmttz0.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093
   ```
   {: codeblock}

5. 에지 노드에서 sdr2evtstreams 서비스 예제를 실행하려면 IBM/pattern-ibm.sdr2evtstreams 배치 패턴을 사용하여 에지 노드를 등록해야 합니다. [SDR 대 IBM Event Streams 예제 에지 서비스 사용을 위한 전제조건![새 탭에서 열림](../../images/icons/launch-glyph.svg "새 탭에서 열림")](https://www.ibm.com/links?url=https%3A%2F%2Fgithub.com%2Fopen-horizon%2Fexamples%2Ftree%2Fmaster%2Fedge%2Fevtstreams%2Fsdr2evtstreams)의 단계를 수행하십시오.

6. 예제 웹 UI에서 에지 노드가 결과를 전송하고 있는지 확인하십시오. 자세한 정보는 [소프트웨어 정의 라디오 예제 웹 UI ![새 탭에서 열림](../../images/icons/launch-glyph.svg "새 탭에서 열림")](https://sdr-poc-sdr-poc-app-delightful-leopard.mybluemix.net)를 참조하십시오. 해당 인증 정보로 로그인하십시오.

   * 사용자 이름: guest@ibm.com
   * 비밀번호: guest123

## 클라우드에 배치

고유한 소프트웨어 정의 비율 예제 웹 UI를 작성하려는 경우 선택적으로 IBM Functions, IBM 데이터베이스, 웹 UI 코드를 배치할 수 있습니다. [유료 계정 작성 ![새 탭에서 열림](../../images/icons/launch-glyph.svg "새 탭에서 열림")](https://cloud.ibm.com/login) 후에 하나의 명령으로 이를 수행할 수 있습니다.

배치 코드는 examples/cloud/sdr/deploy/ibm 저장소에 있습니다. 자세한 정보는 [배치 저장소 컨텐츠 ![새 탭에서 열림](../../images/icons/launch-glyph.svg "새 탭에서 열림")](https://www.ibm.com/links?url=https%3A%2F%2Fgithub.com%2Fopen-horizon%2Fexamples%2Ftree%2Fmaster%2Fcloud%2Fsdr%2Fdeploy%2Fibm)의 내용을 참조하십시오. 

이 코드는 자세한 지시사항이 포함된 README.md 파일과 워크로드를 처리하는 deploy.sh 스크립트로 구성됩니다. 저장소에는 deploy.sh 스크립트에 대한 다른 인터페이스인 Makefile도 포함되어 있습니다. SDR 예제에 대한 사용자 고유의 클라우드 백엔드 배치에 대해 자세히 알아보려면 저장소 지시사항을 검토하십시오.

참고: 이 배치 프로세스에는 {{site.data.keyword.cloud_notm}} 계정에 비용을 부과하는 유료 서비스가 필요합니다.

## 다음에 수행할 작업

고유한 소프트웨어를 에지 노드에 배치하려는 경우 고유한 에지 서비스, 연관 배치 패턴 또는 배치 정책을 작성해야 합니다. 자세한 정보는 [IBM Edge Application Manager for Devices로 에지 서비스 개발](../developing/developing.md)을 참조하십시오.
