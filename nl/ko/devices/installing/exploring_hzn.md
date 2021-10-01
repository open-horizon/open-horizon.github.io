---

copyright:
years: 2019
lastupdated: "2019-11-17"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# hzn 명령 탐색
{: #exploring-hzn}

{{site.data.keyword.horizon}} 에지 노드에서는 `hzn` 명령을 사용하여 에지 노드 외부에 있는 더 큰 {{site.data.keyword.edge_devices_notm}} 에코시스템 또는 로컬 시스템의 다양한 상태 측면을 조사하십시오. `hzn` 명령을 사용하면 시스템과 상호작용하고 소유하는 리소스의 상태를 변경할 수 있습니다.

모든 하위 명령 레벨에서 `--help`(또는 `-h`) 플래그를 사용하여 모든 하위 명령에 대한 세부사항을 포함하여 `hzn` 명령에 대한 도움말을 얻을 수 있습니다. 예를 들어, 다음 명령을 시도하십시오.

```
hzn --help
hzn node --help
hzn exchange pattern --help
```
{: codeblock}

`hzn` 명령에서 `--verbose`(또는 `-v`) 플래그를 사용하여 자세한 출력을 제공할 수 있습니다. 대부분의 경우 `hzn` 명령은 {{site.data.keyword.horizon}} 컴포넌트에서 제공되는 REST API를 통한 편의 랩퍼이며 일반적으로 `--verbose` 플래그는 이면의 REST 상호작용에 대한 세부사항을 표시합니다. 예를 들어 다음을 시도하십시오.

```
  hzn node list -v
```  
{: codeblock}

해당 명령의 출력에는 로컬 {{site.data.keyword.horizon}} 에이전트가 REST 요청에 응답하는 `localhost` URL에 대한 두 개의 REST `GET` 메소드 호출이 표시됩니다.

예를 들면, 다음과 같습니다.

```
[verbose] GET http://localhost:8510/node
[verbose] HTTP code: 200
...
[verbose] GET http://localhost:8510/status
[verbose] HTTP code: 200
```  
{: codeblock}
