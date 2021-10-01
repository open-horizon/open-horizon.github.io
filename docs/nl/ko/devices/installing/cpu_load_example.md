---

copyright:
years: 2020
lastupdated: "2020-02-06"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# {{site.data.keyword.message_hub_notm}}에 대한 CPU 사용량
{: #cpu_load_ex}

호스트 CPU 로드 백분율은 CPU 로드 백분율 데이터를 사용하고 이를 IBM Event Streams를 통해 사용할 수 있도록 하는 예제 배치 패턴입니다.

이 에지 서비스는 반복해서 에지 디바이스 CPU 로드를 조회하고 결과 데이터를 [IBM Event Streams ![새 탭에서 열림](../../images/icons/launch-glyph.svg "새 탭에서 열림")](https://www.ibm.com/cloud/event-streams)로 보냅니다. 이 에지 서비스는 특수 센서 하드웨어가 필요하지 않으므로 모든 에지 노드에서 실행할 수 있습니다.

이 태스크를 수행하기 전에 [에지 디바이스에서 Horizon 에이전트 설치 및 hello world 예제에 등록](registration.md)의 단계를 수행하여 등록 및 등록 취소하십시오.

좀 더 현실적인 시나리오를 경험할 수 있도록 이 cpu2evtstreams 예제에서는 다음을 포함하여 일반 에지 서비스의 더 많은 측면에 대해 설명합니다.

* 동적 에지 디바이스 데이터 조회
* 에지 디바이스 데이터 분석(예: `cpu2evtstreams`가 CPU 로드의 이동 평균 계산)
* 중앙 데이터 수집 서비스로 처리된 데이터 전송
* 데이터 전송을 안전하게 인증할 수 있도록 이벤트 스트림 인증 정보의 취득 자동화

## 시작하기 전에
{: #deploy_instance}

cpu2evtstreams 에지 서비스를 배치하기 전에 해당 데이터 수신을 위해 클라우드에서 실행 중인 {{site.data.keyword.message_hub_notm}}의 인스턴스가 필요합니다. 조직의 모든 구성원이 하나의 {{site.data.keyword.message_hub_notm}} 인스턴스를 공유할 수 있습니다. 인스턴스가 배치되면 액세스 정보를 얻어 환경 변수를 설정하십시오.

### {{site.data.keyword.cloud_notm}}에 {{site.data.keyword.message_hub_notm}} 배치
{: #deploy_in_cloud}

1. {{site.data.keyword.cloud_notm}}로 이동하십시오.

2. **리소스 작성**을 클릭하십시오.

3. 검색 상자에 `Event Streams`를 입력하십시오.

4. **Event Streams** 타일을 선택하십시오.

5. **Event Streams**에 서비스 이름을 입력하고 위치를 선택하고 가격 플랜을 선택하고 **작성**을 클릭하여 인스턴스를 프로비저닝하십시오.

6. 프로비저닝이 완료되면 인스턴스를 클릭하십시오.

7. 주제를 작성하려면 + 아이콘을 클릭한 다음 인스턴스의 이름을 `cpu2evtstreams`로 지정하십시오.

8. 터미널에서 인증 정보를 작성하거나, 이미 작성되어 있는 경우 이 인증 정보를 얻을 수 있습니다. 인증 정보를 작성하려면 **서비스 인증 정보 > 새 인증 정보**를 클릭하십시오. 다음 코드 블록과 유사하게 형식화된 새 인증 정보를 가진 `event-streams.cfg` 파일을 작성하십시오. 이러한 인증 정보는 한 번만 작성하면 되지만, {{site.data.keyword.event_streams}} 액세스가 필요할 수 있는 본인 또는 기타 팀 구성원이 이후에 사용할 수 있도록 이 파일을 저장하십시오.

   ```
   EVTSTREAMS_API_KEY="<the value of api_key>"
   EVTSTREAMS_BROKER_URL="<all kafka_brokers_sasl values in a single string, separated by commas>"
   ```
   {: codeblock}
        
   예를 들어, 인증 정보 분할창에서 다음을 수행하십시오.

   ```
   EVTSTREAMS_BROKER_URL=broker-4-x7ztkttrm44911kc.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-3-  x7ztkttrm44911kc.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-2-x7ztkttrm44911kc.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-0-x7ztkttrm44911kc.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-1-x7ztkttrm44911kc.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-5-x7ztkttrm44911kc.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093
   ```
   {: codeblock}

9. `event-streams.cfg`를 작성한 후 쉘에서 이러한 환경 변수를 설정하십시오.

   ```
   eval export $(cat event-streams.cfg)
   ```
   {: codeblock}

### {{site.data.keyword.cloud_notm}}에서 {{site.data.keyword.message_hub_notm}} 테스트
{: #testing}

1. `kafkacat`(https://linuxhostsupport.com/blog/how-to-install-apache-kafka-on-ubuntu-16-04/)을 설치하십시오.

2. 하나의 터미널에 다음을 입력하여 `cpu2evtstreams` 주제를 구독하십시오.

    ```
    kafkacat -C -q -o end -f "%t/%p/%o/%k: %s\n" -b $EVTSTREAMS_BROKER_URL -X api.version.request=true -X security.protocol=sasl_ssl -X sasl.mechanisms=PLAIN -X sasl.username=token -X sasl.password=$EVTSTREAMS_API_KEY -t cpu2evtstreams
    ```
    {: codeblock}

3. 두 번째 터미널에서는 `cpu2evtstreams` 주제에 테스트 컨텐츠를 공개하여 원래 콘솔에 표시하십시오. 예를 들면, 다음과 같습니다.

    ```
    echo 'hi there' | kafkacat -P -b $EVTSTREAMS_BROKER_URL -X api.version.request=true -X security.protocol=sasl_ssl -X sasl.mechanisms=PLAIN -X sasl.username=token -X sasl.password=$EVTSTREAMS_API_KEY -t cpu2evtstreams
    ```
    {: codeblock}

## 에지 디바이스 등록
{: #reg_device}

에지 노드에서 cpu2evtstreams 서비스 예제를 실행하려면 `IBM/pattern-ibm.cpu2evtstreams` 배치 패턴을 사용하여 에지 노드를 등록해야 합니다. [Horizon CPU To {{site.data.keyword.message_hub_notm}} ![새 탭에서 열림](../../images/icons/launch-glyph.svg "새 탭에서 열림")](https://github.com/open-horizon/examples/blob/master/edge/evtstreams/cpu2evtstreams/README.md)에 있는 **첫 번째** 절의 단계를 수행하십시오.

## 추가 정보
{: #add_info}

CPU 예제 소스 코드는 [{{site.data.keyword.horizon_open}} 예제 저장소 ![새 탭에서 열림](../../images/icons/launch-glyph.svg "새 탭에서 열림")](https://github.com/open-horizon/examples)에서 {{site.data.keyword.edge_devices_notm}} 에지 서비스 배치의 예제로 사용할 수 있습니다. 이 소스에는
이 예제의 에지 노드에서 실행되는 세 개의 모든 서비스에 대한 코드가 포함되어 있습니다.

  * 로컬 사설 Docker 네트워크에서 CPU 로드 비율 데이터를 REST 서비스로 제공하는 cpu 서비스. 자세한 정보는 [Horizon CPU Percent Service ![새 탭에서 열림](../../images/icons/launch-glyph.svg "새 탭에서 열림")](https://github.com/open-horizon/examples/tree/master/edge/services/cpu_percent)를 참조하십시오.
  * GPS 하드웨어의 위치 정보(가능한 경우) 또는 에지 노드 IP 주소에서 산정된 위치를 제공하는 gps 서비스. 위치 데이터는 로컬 사설 Docker 네트워크에서 REST 서비스로 제공됩니다. 자세한 정보는 [Horizon GPS Service ![새 탭에서 열림](../../images/icons/launch-glyph.svg "새 탭에서 열림")](https://github.com/open-horizon/examples/tree/master/edge/services/gps)를 참조하십시오.
  * 다른 두 개의 서비스에서 제공되는 REST API를 사용하는 cpu2evtstreams 서비스. 이 서비스는 결합된 데이터를 클라우드의 {{site.data.keyword.message_hub_notm}} kafka 브로커에 전송합니다. 이 서비스에 대한 자세한 정보는 [{{site.data.keyword.horizon}} CPU To {{site.data.keyword.message_hub_notm}} Service ![새 탭에서 열림](../../images/icons/launch-glyph.svg "새 탭에서 열림")](https://github.com/open-horizon/examples/blob/master/edge/evtstreams/cpu2evtstreams/cpu2evtstreams.md)를 참조하십시오.
  * {{site.data.keyword.message_hub_notm}}에 대한 자세한 정보는 [Event Streams - 개요 ![새 탭에서 열림](../../images/icons/launch-glyph.svg "새 탭에서 열림")](https://www.ibm.com/cloud/event-streams?mhsrc=ibmsearch_a&mhq=event%20streams)를 참조하십시오.

## 다음에 수행할 작업
{: #cpu_next}

고유한 소프트웨어를 에지 노드에 배치하려는 경우 고유한 에지 서비스, 연관 배치 패턴 또는 배치 정책을 작성해야 합니다. 자세한 정보는 [{{site.data.keyword.edge_devices_notm}}로 에지 서비스 개발](../developing/developing.md)을 참조하십시오.
