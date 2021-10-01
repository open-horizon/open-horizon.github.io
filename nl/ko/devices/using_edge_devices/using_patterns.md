---

copyright:
  years: 2020
lastupdated: "2020-05-10"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 패턴 사용
{: #using_patterns}

일반적으로 서비스 배치 패턴은 개발자가 Horizon Exchange에 에지 서비스를 공개한 후에 {{site.data.keyword.edge_notm}}({{site.data.keyword.ieam}}) 허브에 공개할 수 있습니다.

hzn CLI는 서비스 배치 패턴 나열, 공개, 확인, 업데이트 및 제거 명령을 포함하여 {{site.data.keyword.horizon_exchange}}에서 패턴을 나열하고 관리하는 기능을 제공합니다. 또한 특정 배치 패턴과 연관된 암호화 키를 나열하고 제거하는 방법도 제공합니다.

CLI 명령 목록과 추가 세부사항은 다음과 같습니다.

```
hzn exchange pattern -h
```
{: codeblock}

## 예제

{{site.data.keyword.horizon_exchange}}에서 패턴 소스를 서명하고 작성(또는 업데이트)하십시오.

```
hzn exchange pattern publish --json-file=JSON-FILE [<flags>]
```
{: codeblock}

## 배치 패턴 사용

배치 패턴을 사용하면 에지 노드에 서비스를 간단히 배치할 수 있습니다. 에지 노드에 배치할 최상위 레벨 서비스 또는 여러 개의 최상위 레벨 서비스를 지정하면 {{site.data.keyword.ieam}}은 사용자의 최상위 레벨 서비스에 있는 종속 서비스의 배치를 포함하여 나머지를 처리합니다.

서비스를 작성하여 {{site.data.keyword.ieam}} Exchange에 추가한 후에 `pattern.json` 파일을 작성해야 합니다. 다음과 유사합니다.

```
{
  "name": "pattern-ibm.cpu2evtstreams-arm",
  "label": "Edge ibm.cpu2evtstreams Service Pattern for arm",
  "description": "Pattern for ibm.cpu2evtstreams for arm",
  "public": true,
  "services": [
    {
      "serviceUrl": "ibm.cpu2evtstreams",
      "serviceOrgid": "IBM",
      "serviceArch": "arm",
      "serviceVersions": [
        {
          "version": "1.4.3",
          "priority": {
            "priority_value": 1,
            "retries": 1,
            "retry_durations": 1800,
            "verified_durations": 45
          }
        },
        {
          "version": "1.4.2",
          "priority": {
            "priority_value": 2,
            "retries": 1,
            "retry_durations": 3600
          }
        }
      ]
    }
  ],
  "userInput": [
    {
      "serviceOrgid": "IBM",
      "serviceUrl": "ibm.cpu2evtstreams",
      "serviceVersionRange": "[0.0.0,INFINITY)",
      "inputs": [
        {
          "name": "EVTSTREAMS_API_KEY",
          "value": "$EVTSTREAMS_API_KEY"
        },
        {
          "name": "EVTSTREAMS_BROKER_URL",
          "value": "$EVTSTREAMS_BROKER_URL"
        },
        {
          "name": "EVTSTREAMS_CERT_ENCODED",
          "value": "$EVTSTREAMS_CERT_ENCODED"
        }
      ]
    }
  ]
}
```
{: codeblock}

이 코드는 `arm` 디바이스의 `ibm.cpu2evtstreams` 서비스에 대한 `pattern.json` 파일의 예제입니다. 여기에 표시된 대로, `cpu_percent` 및 `gps`(`cpu2evtstreams`의 종속 서비스)를 지정할 필요가 없습니다. 해당 태스크는 `service_definition.json` 파일에서 수행하는 것이므로 등록된 에지 노드가 해당 워크로드를 자동으로 실행합니다.

`pattern.json` 파일을 사용하면 `serviceVersions` 섹션에서 롤백 설정을 사용자 정의할 수 있습니다. 서비스에 대해 여러 개의 이전 버전을 지정하고 새 버전에 오류가 있는 경우 롤백을 위해 에지 노드의 우선순위를 각 버전에 지정할 수 있습니다. 각 롤백 버전에 우선순위 지정 외에도 지정된 서비스의 낮은 우선순위 버전으로 폴백하기 전에 재시도 지속 기간 및 재시도 수와 같은 사항을 지정할 수 있습니다.

배치 패턴을 공개할 때 서비스가 중앙에서 올바르게 작동하는 데 필요한 구성 변수를 맨 아래 부분에 있는 `userInput` 섹션에 포함시켜 구성 변수를 설정할 수도 있습니다. `ibm.cpu2evtstreams` 서비스가 공개될 때 데이터를 IBM Event Streams에 공개하는 데 필요한 인증 정보가 함께 전달되며, 이는 다음 명령을 사용하여 수행될 수 있습니다.

```
hzn exchange pattern publish -f pattern.json
```
{: codeblock}

패턴이 공개되면 암 디바이스를 패턴에 등록할 수 있습니다.

```
hzn register -p pattern-ibm.cpu2evtstreams-arm
```
{: codeblock}

이 명령은 `ibm.cpu2evtstreams`와 종속 서비스를 노드에 배치합니다.

참고: `userInput.json` 파일은 위의 `hzn register` 명령에 전달되지 않습니다. [배치 패턴으로 CPU를 IBM Event Streams 에지 서비스에 사용 ![새 탭에서 열림](../../images/icons/launch-glyph.svg "새 탭에서 열림")](https://github.com/open-horizon/examples/tree/master/edge/evtstreams/cpu2evtstreams#-using-the-cpu-to-ibm-event-streams-edge-service-with-deployment-pattern) 저장소 예제에서 다음 단계를 수행하는 경우와 같습니다. 사용자 입력이 패턴과 함께 전달되었기 때문에 자동으로 등록하는 에지 노드는 해당 환경 변수에 대한 액세스 권한을 갖습니다.

다음과 같이 등록 취소하여 모든 `ibm.cpu2evtstreams` 워크로드를 중지할 수 있습니다.

```
hzn unregister -fD
```
{: codeblock}
