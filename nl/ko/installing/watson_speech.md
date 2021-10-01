---

copyright:
years: 2019
lastupdated: "2020-2-25"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Watson 음성-문자 변환
{: #watson-speech}

이 서비스는 Watson 단어를 청취합니다. 해당 단어가 발견되면 서비스가 오디오 클립을 캡처하여 Speech to Text 인스턴스에 전송합니다.  중지 단어가 제거되고(선택사항) 기록된 텍스트가 {{site.data.keyword.event_streams}}에 전송됩니다.

## 시작하기 전에

시스템이 해당 요구사항을 충족하는지 확인하십시오.

* [에지 디바이스 준비](adding_devices.md)의 단계를 수행하여 등록 및 등록 취소해야 합니다.
* USB 사운드 카드 및 마이크로폰이 Raspberry Pi에 설치됩니다. 

이 서비스에서 {{site.data.keyword.event_streams}} 및 IBM Speech to Text의 인스턴스가 모두 올바르게 실행되어야 합니다. 이벤트 스트림 인스턴스를 배치하는 방법에 대한 지시사항은 [호스트 CPU 로드 백분율 예제(cpu2evtstreams)](../using_edge_services/cpu_load_example.md)를 참조하십시오.  

필수 {{site.data.keyword.event_streams}} 환경 변수가 설정되었는지 확인하십시오.

```
echo "$EVTSTREAMS_API_KEY, $EVTSTREAMS_BROKER_URL"
```
{: codeblock}

이 샘플이 사용하는 이벤트 스트림 주제는 기본적으로 `myeventstreams`이지만 다음 환경 변수를 설정하여 주제를 사용할 수 있습니다.

```
export EVTSTREAMS_TOPIC=<your-topic-name>
```
{: codeblock}

## IBM Speech to Text의 인스턴스 배치
{: #deploy_watson}

현재 인스턴스가 배치된 경우 액세스 정보를 얻고 환경 변수를 설정하거나 해당 단계를 따르십시오.

1. IBM 클라우드를 탐색하십시오.
2. **리소스 작성**을 클릭하십시오.
3. 검색 상자에 `Speech to Text`를 입력하십시오.
4. `Speech to Text` 타일을 선택하십시오.
5. 지역을 선택하고 가격 플랜을 선택한 후 서비스 이름을 입력하고 **작성**을 클릭하여 인스턴스를 프로비저닝하십시오.
6. 프로비저닝이 완료된 후 인스턴스를 클릭하고 인증 정보 API 키 및 URL을 메모하여 다음 환경 변수로 내보내십시오.

    ```
    export STT_IAM_APIKEY=<speech-to-text-api-key>     export STT_URL=<speech-to-text-url>
    ```
    {: codeblock}

7. Speech to Text 서비스를 테스트하는 방법에 대한 지시사항을 보려면 시작하기 섹션으로 이동하십시오.

## 에지 디바이스 등록
{: #watson_reg}

에지 노드에서 watsons2text 서비스 예제를 실행하려면 `IBM/pattern-ibm.watsons2text-arm` 배치 패턴을 사용하여 에지 노드를 등록해야 합니다. readme 파일의 [Watson Speech to Text 대 배치 패턴이 있는 IBM Event Streams Service 사용](https://github.com/open-horizon/examples/tree/master/edge/evtstreams/watson_speech2text#-using-the-ibm-watson-speech-to-text-to-ibm-event-streams-service-with-deployment-pattern) 절의 단계를 수행하십시오.

## 추가 정보

`processtect` 예제 소스 코드는 Horizon GitHub 저장소에서 {{site.data.keyword.edge_notm}} 개발에 대한 예제로 사용할 수도 있습니다. 이 소스에는 이 예제의 에지 노드에서 실행되는 네 개의 모든 서비스에 대한 코드가 포함되어 있습니다. 

이러한 서비스는 다음과 같습니다.

* [hotworddetect](https://github.com/open-horizon/examples/tree/master/edge/services/hotword_detection) 서비스는 핫워드 Watson을 청취 및 감지한 후 오디오 클립을 기록하고 mqtt 브로커에 공개합니다.
* [watsons2text](https://github.com/open-horizon/examples/tree/master/edge/evtstreams/watson_speech2text) 서비스는 오디오 클립을 수신하여 IBM Speech to Text 서비스로 전송하고 암호 해독된 텍스트를 mqtt 브로커에 공개합니다.
* WSGI 서버가 JSON 오브젝트(예: {"text": "how are you today"})를 사용하고 공통 중지 단어를 제거하고 {"result": "how you today"}를 리턴하도록 [stopwordremoval](https://github.com/open-horizon/examples/tree/master/edge/services/stopword_removal) 서비스가 실행됩니다.
* [mqtt2kafka](https://github.com/open-horizon/examples/tree/master/edge/services/mqtt2kafka) 서비스는 등록된 mqtt 주제에서 임의 항목을 수신할 때 {{site.data.keyword.event_streams}}에 데이터를 공개합니다.
* [mqtt_broker](https://github.com/open-horizon/examples/tree/master/edge/services/mqtt_broker)는 모든 컨테이너 간 통신을 담당합니다.

## 다음에 수행할 작업

* 오프라인 음성 지원 에지 서비스의 고유한 버전 빌드 및 공개에 대한 지시사항은 [오프라인 음성 지원 에지 서비스](https://github.com/open-horizon/examples/blob/master/edge/evtstreams/watson_speech2text/CreateService.md#-building-and-publishing-your-own-version-of-the-watson-speech-to-text-to-ibm-event-streams-service)를 참조하십시오. Open Horizon 예제 저장소의 `watson_speech2text` 디렉토리에 있는 단계를 따르십시오.

* [Open Horizon 예제 저장소](https://github.com/open-horizon/examples)를 참조하십시오.
