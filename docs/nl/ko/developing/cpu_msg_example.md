---

copyright:
years: 2019, 2020
lastupdated: "2019-06-28"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# CPU 대 {{site.data.keyword.message_hub_notm}} 서비스
{: #cpu_msg_ex}

이 예제는 CPU 로드 비율 정보를 수집하여 {{site.data.keyword.message_hub_notm}}에 전송합니다. 이 예제를 사용하여 데이터를 클라우드 서비스에 전송하는 고유한 에지 애플리케이션을 개발하는 데 도움을 받을 수 있습니다.
{:shortdesc}

## 시작하기 전에
{: #cpu_msg_begin}

[에지 서비스 작성 준비](service_containers.md)의 전제조건 단계를 완료하십시오. 결과적으로 해당 환경 변수를 설정해야 하고 해당 명령을 설치해야 하며 해당 파일이 있어야 합니다.

```bash
echo "HZN_ORG_ID=$HZN_ORG_ID, HZN_EXCHANGE_USER_AUTH=$HZN_EXCHANGE_USER_AUTH, DOCKER_HUB_ID=$DOCKER_HUB_ID" which git jq make ls ~/.hzn/keys/service.private.key ~/.hzn/keys/service.public.pem cat /etc/default/horizon
```
{: codeblock}

## 프로시저
{: #cpu_msg_procedure}

이 예제는 [{{site.data.keyword.horizon_open}}](https://github.com/open-horizon/) 오픈 소스 프로젝트의 일부입니다. [CPU 대 IBM Event Streams 에지 서비스의 고유 버전 빌드 및 공개](https://github.com/open-horizon/examples/blob/master/edge/evtstreams/cpu2evtstreams/CreateService.md#-building-and-publishing-your-own-version-of-the-cpu-to-ibm-event-streams-edge-service)의 단계를 수행한 후 여기로 돌아오십시오.

## 이 예제에서 학습한 내용

### 필수 서비스

cpu2evtstreams 에지 서비스는 해당 태스크를 수행하기 위해 두 개의 다른 에지 서비스(**cpu** 및 **gps**)에 의존하는 서비스의 예입니다. **horizon/service.definition.json** 파일의 **requiredServices** 섹션 내에서 해당 종속성의 세부사항을 볼 수 있습니다.

```json
    "requiredServices": [         {
            "url": "ibm.cpu",             "org": "IBM",             "versionRange": "[0.0.0,INFINITY)",             "arch": "$ARCH"
        },
        {
            "url": "ibm.gps",             "org": "IBM",             "versionRange": "[0.0.0,INFINITY)",             "arch": "$ARCH"         }
    ],
```
{: codeblock}

### 구성 변수
{: #cpu_msg_config_var}

**cpu2evtstreams** 서비스를 실행하려면 몇 가지 구성이 필요합니다. 에지 서비스가 해당 유형을 언급하고 기본값을 제공하여 구성 변수를 선언할 수 있습니다. **userInput** 섹션의 **horizon/service.definition.json**에서 해당 구성 변수를 볼 수 있습니다.

```json  
    "userInput": [         {
            "name": "EVTSTREAMS_API_KEY",             "label": "The API key to use when sending messages to your instance of IBM Event Streams",             "type": "string",             "defaultValue": ""
        },
        {
            "name": "EVTSTREAMS_BROKER_URL",             "label": "The comma-separated list of URLs to use when sending messages to your instance of IBM Event Streams",             "type": "string",             "defaultValue": ""
        },
        {
            "name": "EVTSTREAMS_CERT_ENCODED",             "label": "The base64-encoded self-signed certificate to use when sending messages to your ICP instance of IBM Event Streams. Not needed for IBM Cloud Event Streams.",             "type": "string",             "defaultValue": "-"
        },
        {
            "name": "EVTSTREAMS_TOPIC",             "label": "The topic to use when sending messages to your instance of IBM Event Streams",             "type": "string",             "defaultValue": "cpu2evtstreams"
        },
        {
            "name": "SAMPLE_SIZE",             "label": "the number of samples to read before calculating the average",             "type": "int",             "defaultValue": "5"
        },
        {
            "name": "SAMPLE_INTERVAL",             "label": "the number of seconds between samples",             "type": "int",             "defaultValue": "2"
        },
        {
            "name": "MOCK",             "label": "mock the CPU sampling",             "type": "boolean",             "defaultValue": "false"
        },
        {
            "name": "PUBLISH",             "label": "publish the CPU samples to IBM Event Streams",             "type": "boolean",             "defaultValue": "true"
        },
        {
            "name": "VERBOSE",             "label": "log everything that happens",             "type": "string",             "defaultValue": "1"         }
    ],
```
{: codeblock}

이러한 사용자 입력 구성 변수는 에지 서비스가 에지 노드에서 시작될 때 값을 보유해야 합니다. 값은 다음과 같은 소스에서 올 수 있습니다(다음 우선순위대로).

1. **hzn register -f** 플래그와 함께 지정된 사용자 입력 파일
2. exchange에서 에지 노드 리소스의 **userInput** 섹션
3. exchange에서 패턴 또는 배치 정책 리소스의 **userInput** 섹션
4. exchange에서 서비스 정의 리소스에 지정된 기본값

이 서비스를 위한 에지 디바이스를 등록할 때 기본값이 없는 일부 구성 변수를 지정한 **userinput.json** 파일을 제공했습니다.

### 개발 팁
{: #cpu_msg_dev_tips}

서비스를 테스트하고 디버깅하는 데 도움이 되는 서비스에 구성 변수를 통합하는 것이 유용할 수 있습니다. 예를 들어, 이 서비스의 메타데이터(**service.definition.json**)와 코드(**service.sh**)는 다음 구성 변수를 사용합니다.

* **VERBOSE**는 이 코드가 실행되는 동안 로깅되는 정보의 양을 늘립니다.
* **PUBLISH**는 코드가 메시지를 {{site.data.keyword.message_hub_notm}}에 전송하려고 시도하는지 여부를 제어합니다.
* **MOCK**는 **service.sh**가 종속 항목(**cpu** 및 **gps** 서비스)의 REST API를 호출하거나 대신 모의 데이터 자체를 작성하려고 시도하는지 여부를 제어합니다.

사용자가 의존하는 서비스를 무시하는 기능은 선택사항이지만, 필수 서비스와 격리되어 컴포넌트를 개발 및 테스트하는 것은 유용할 수 있습니다. 이 방식은 또한 하드웨어 센서 또는 액츄에이터가 존재하지 않는 디바이스 유형에 대한 서비스 개발이 가능하게 만들 수도 있습니다.

불필요한 변경을 피하고 합성 devops 환경에서의 테스트를 용이하게 하도록 클라우드 서비스와의 상호작용을 끄는 기능은 개발 및 테스트 중에 편리할 수 있습니다.

## 다음에 수행할 작업
{: #cpu_msg_what_next}

* [{{site.data.keyword.edge_notm}}을(를) 사용하여 에지 서비스 개발](../OH/docs/developing/developing.md)에서 다른 에지 서비스 예제를 사용해 보십시오.
