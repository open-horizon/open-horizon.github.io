---

copyright:
years: 2020
lastupdated: "2020-03-30"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 롤백으로 에지 서비스 업데이트
{: #service_rollback}

에지 노드의 서비스는 일반적으로 중요한 기능을 수행하므로 에지 서비스의 새 버전이 다수의 에지 노드로 롤아웃되면 배치의 성공을 모니터하는 것이 중요하며 에지 노드에서 실패하는 경우 에지 서비스의 이전 버전으로 노드를 다시 되돌리십시오. {{site.data.keyword.edge_notm}}({{site.data.keyword.ieam}})에서는 이를 자동으로 수행할 수 있습니다. 패턴 또는 배치 정책에서 새 서비스 버전이 실패하는 경우 사용해야 하는 이전 서비스 버전 또는 버전을 정의할 수 있습니다.

다음 컨텐츠는 패턴 또는 배치 정책에서 롤백 설정 업데이트를 위한 소프트웨어 배치 우수 사례 및 기존 에지 서비스의 새 버전을 롤아웃하는 방법에 대한 추가 세부사항을 제공합니다.

## 새 에지 서비스 정의 작성
{: #creating_edge_service_definition}

[디바이스에 대한 에지 서비스 개발](../OH/docs/developing/developing.md) 및 [개발 세부사항](../developing/developing_details.md) 섹션에 설명된 대로 에지 서비스의 새 버전을 릴리스하는 기본 단계는 다음과 같습니다.

- 새 버전에 필요한 경우 에지 서비스 코드를 편집하십시오.
- **hzn.json** 구성 파일의 서비스 버전 변수에서 코드의 시맨틱 버전 번호를 편집하십시오.
- 서비스 컨테이너를 다시 빌드하십시오.
- Horizon Exchange에 새 에지 서비스 버전을 서명하고 공개하십시오.

## 패턴 또는 배치 정책에서 롤백 설정 업데이트
{: #updating_rollback_settings}

새 에지 서비스는 서비스 정의의 `버전` 필드에서 해당 버전 번호를 지정합니다.

패턴 또는 배치 정책은 어떤 서비스가 어떤 에지 노드에 배치되는지 판별합니다. 에지 서비스 롤백 기능을 사용하려면 패턴 또는 배치 정책 구성 파일의 **serviceVersions** 섹션에서 새 서비스 버전의 참조를 추가해야 합니다.

에지 서비스가 패턴 또는 정책의 결과로 에지 노드에 배치되는 경우 에이전트가 상위 우선순위 값이 있는 서비스 버전을 배치합니다.

예를 들면, 다음과 같습니다.

```json
 "serviceVersions": 
[
 {
   "version": "2.3.1",
   "priority": {
    "priority_value": 2,
    "retries": 1,
    "retry_durations": 1800
   }
 },
 {
   "version": "1.0.0",
   "priority": {
    "priority_value": 6,
    "retries": 1,
    "retry_durations": 2400
   }
  },
  {
   "version": "2.3.0",
   "priority": {
    "priority_value": 4,
    "retries": 1,
    "retry_durations": 3600
   }
  }
]
```
{: codeblock}

추가 변수는 우선순위 섹션에서 제공됩니다. `priority_value` 특성은 먼저 시도할 서비스 버전의 순서를 설정하며, 낮은 숫자일수록 먼저 시도합니다. `재시도` 변수값은 다음 가장 높은 우선순위 버전으로 롤백하기 전에 Horizon이 `retry_durations`에서 지정한 시간 범위 내에서 이 서비스 버전을 시작하려고 시도하는 횟수를 정의합니다. `retry_durations` 변수는 특정 시간 간격(초)을 정의합니다. 예를 들어, 1개월 동안 three번의 서비스 실패는 서비스를 이전 버전으로 롤백하지 않을 수도 있지만, 5분 동안 3번의 실패는 새 서비스 버전에 문제가 있다는 표시일 수 있습니다.

그런 다음 배치 패턴을 다시 공개하거나 Horizon Exchange에서 **serviceVersion** 섹션 변경사항으로 배치 정책을 업데이트하십시오.

CLI `deploycheck` 명령으로 배치 정책 또는 패턴 설정 업데이트의 기능을 확인할 수도 있음을 참고하십시오. 추가 세부사항은 다음을 실행하십시오.

```bash
hzn deploycheck -h
```
{: codeblock}

{{site.data.keyword.ieam}} agbot은 배치 패턴 또는 배치 정책 변경사항을 신속하게 발견합니다. agbot은 에지 노드가 배치 패턴을 실행하도록 등록되고 업데이트된 배치 정책과 호환 가능한 각 에이전트에 접속합니다. agbot 및 에이전트가 연계하여 새 컨테이너를 다운로드하고 이전 컨테이너를 중지 및 제거하며 새 컨테이너를 시작합니다.

결과적으로 업데이트된 배치 패턴을 실행하도록 등록되었거나 배치 정책과 빠르게 호환 가능한 에지 노드는 에지 노드의 지리적 위치에 관계없이 상위 우선순위 값이 있는 새 에지 서비스 버전을 실행합니다.  

## 롤아웃되는 새 서비스 버전의 진행상태 보기
{: #viewing_rollback_progress}

`agreement_finalized_time` 및 `agreement_execution_start_time` 필드를 채울 때까지 디바이스 계약을 반복적으로 조회하십시오. 

```bash
hzn agreement list
```
{: codeblock}

나열된 계약은 서비스와 연관된 버전을 표시하며 날짜-시간 값은 변수에 나타남(예제: "agreement_creation_time": "",)을 참고하십시오.

또한 버전 필드는 상위 우선순위 값이 있는 새(및 운영) 서비스 버전으로 채워집니다.

```json
[
  {
    …
    "agreement_creation_time": "2020-04-01 11:55:08 -0600 MDT",
    "agreement_accepted_time": "2020-04-01 11:55:17 -0600 MDT",
    "agreement_finalized_time": "2020-04-01 11:55:18 -0600 MDT",
    "agreement_execution_start_time": "2020-04-01 11:55:20 -0600 MDT",
    "agreement_data_received_time": "",
    "agreement_protocol": "Basic",
    "workload_to_run": {
      "url": "ibm.helloworld",
      "org": "ibm",
      "version": "2.3.1",
      "arch": "amd64"
    }
  }
]
```
{: codeblock}

추가 세부사항에 대해 CLI 명령으로 현재 노드의 이벤트 로그를 조사할 수 있습니다.

```bash
hzn eventlog list
```
{: codeblock}

마지막으로 [관리 콘솔](../console/accessing_ui.md)을 사용하여 롤백 배치 버전 설정을 수정할 수도 있습니다. 새 배치 정책을 작성하는 경우 또는 롤백 설정을 포함하여 기존 정책 세부사항을 보고 편집하여 이를 수행할 수 있습니다.UI의 롤백 섹션에서 “시간 범위” 용어는 CLI의 “retry_durations”와 동일함을 참고하십시오.
