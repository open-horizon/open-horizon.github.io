---

copyright:
years: 2019
lastupdated: "2019-07-04"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 배치 패턴 예제
{: #deploy_pattern_ex}

{{site.data.keyword.edge_devices_notm}} 배치 패턴 시작하기에 대해 자세히 알아보는 데 도움이 되도록 배치 패턴으로 로드할 수 있는 예제 프로그램이 제공됩니다.
{:shortdesc}

배치 패턴을 사용하는 방법에 대해 자세히 알아보려면 이러한 사전 빌드된 예제 배치 패턴 각각을 등록해 보십시오.

다음 배치 패턴 예제 중 하나에 대해 에지 노드를 등록하려면 먼저 에지 노드에 대한 기존 배치 패턴 등록을 제거해야 합니다. 배치 패턴 등록을 제거하려면 에지 노드에서 다음 명령을 실행하십시오.
```
 hzn unregister
 hzn node list | jq .configstate.state
```
{: codeblock}

출력 예:
```
"unconfigured"
```
{: codeblock}

명령 출력에 `"unconfigured"` 대신 `"unconfiguring"`이 표시되는 경우 몇 분 동안 기다린 후 명령을 다시 실행하십시오. 일반적으로 이 명령을 완료하는 데 몇 초 정도밖에 걸리지 않습니다. 출력에 `"unconfigured"`가 표시될 때까지 명령을 재시도하십시오.

## 예제
{: #pattern_examples}

* [Hello, world ![새 탭에서 열림](../../images/icons/launch-glyph.svg "새 탭에서 열림")](https://github.com/open-horizon/examples/blob/master/edge/services/helloworld)
  최소의 `"Hello, world."` {{site.data.keyword.edge_devices_notm}} 배치 패턴에 도입하기 위한 최소 `"Hello, world"` 예제입니다.

* [호스트 CPU 로드 비율](cpu_load_example.md)
  CPU 로드 비율 데이터를 이용하고 {{site.data.keyword.message_hub_notm}}를 통해 사용할 수 있도록 하는 예제 배치 패턴입니다.

* [소프트웨어 정의 라디오](software_defined_radio_ex.md)
  라디오 스테이션 오디오를 이용하고 음성을 추출하며 추출된 음성을 텍스트로 변환하는 모든 기능을 갖춘 예제입니다. 이 예제는 텍스트에 대한 감성 분석을 완료하고 각 에지 노드에 대한 데이터의 세부사항을 볼 수 있는 사용자 인터페이스를 통해 데이터 및 결과를 사용할 수 있도록 합니다. 에지 처리에 대해 자세히 알아보려면 이 예제를 사용하십시오.
