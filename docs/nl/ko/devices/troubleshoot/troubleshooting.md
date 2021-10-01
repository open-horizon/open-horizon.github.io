---

copyright:
years: 2019
lastupdated: "2019-06-25"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 문제점 해결
{: #troubleshooting}

문제점 해결 팁과 {{site.data.keyword.edge_notm}}({{site.data.keyword.ieam}})에 발생할 수 있는 공통 문제를 검토하여 발생하는 문제를 해결하는 데 도움을 받으십시오.
{:shortdesc}

다음 문제점 해결 안내서에서는 {{site.data.keyword.ieam}} 시스템의 기본 컴포넌트 및 포함된 인터페이스를 조사하여 시스템의 상태를 판별하는 방법에 대해 설명합니다.

## 문제점 해결 도구
{: #ts_tools}

{{site.data.keyword.ieam}}에 포함된 많은 인터페이스에서 문제점을 진단하는 데 사용할 수 있는 정보를 제공합니다. 이 정보는 {{site.data.keyword.gui}}, HTTP REST API, {{site.data.keyword.linux_notm}} 쉘 도구, `hzn`을 통해 사용 가능합니다.

에지 머신에서는 호스트 문제, Horizon 소프트웨어 문제, Docker 문제 또는 서비스 컨테이너의 코드나 구성 문제를 해결해야 할 수 있습니다. 에지 머신 호스트 문제는 이 문서에서 다루지 않습니다. Docker 문제를 해결해야 하는 경우 많은 Docker 명령과 인터페이스를 사용할 수 있습니다. 자세한 정보는 Docker 문서를 참조하십시오.

실행 중인 서비스 컨테이너가 메시징을 위해 {{site.data.keyword.message_hub_notm}}(Kafka에 기반함)를 사용하는 경우 수동으로 {{site.data.keyword.ieam}}에 대한 Kafka 스트림에 연결하여 문제점을 진단할 수 있습니다. {{site.data.keyword.message_hub_notm}}에서 수신하는 내용을 관찰하기 위해 메시지 주제를 구독하거나 다른 디바이스로 메시지를 시뮬레이션하기 위해 메시지 주제에 공개할 수 있습니다. `kafkacat` {{site.data.keyword.linux_notm}} 명령은 {{site.data.keyword.message_hub_notm}}를 공개하거나 등록하는 쉬운 방식입니다. 이 도구의 최신 버전을 사용하십시오. 또한 {{site.data.keyword.message_hub_notm}}는 몇 가지 정보에 액세스하는 데 사용할 수 있는 그래픽 웹 페이지를 제공합니다.

{{site.data.keyword.horizon}}이 설치된 머신의 경우 `hzn` 명령을 사용하여 로컬 {{site.data.keyword.horizon}} 에이전트 및 원격 {{site.data.keyword.horizon_exchange}}에서 문제를 디버깅하십시오. 내부적으로 `hzn` 명령은 제공된 HTTP REST API와 상호작용합니다. `hzn` 명령은 액세스를 단순화하고 REST API 자체보다 더 나은 사용자 경험을 제공합니다. `hzn` 명령은 종종 출력에서 보다 자세한 텍스트 설명을 제공하며, 여기에는 기본 제공 온라인 도움말 시스템이 포함됩니다. 도움말 시스템을 사용하여 사용할 명령에 대한 정보 및 세부사항과 명령 구문 및 인수에 대한 세부사항을 확보하십시오. 이 도움말 정보를 보려면 `hzn --help` 또는 `hzn \<subcommand\> --help` 명령을 실행합니다.

{{site.data.keyword.horizon}} 패키지가 지원 또는 설치되지 않은 노드에서는 대신, 기본 HTTP REST API와 직접 상호작용할 수 있습니다. 예를 들어, `curl` 유틸리티 또는 기타 REST API CLI 유틸리티를 사용할 수 있습니다. 또한 REST 조회를 지원하는 언어로 프로그램을 작성할 수도 있습니다. 

## 문제점 해결 팁
{: #ts_tips}

특정 문제를 해결하는 데 도움을 얻으려면 다음 주제에서 시스템 상태에 대한 질문 및 연관된 팁을 검토하십시오. 각 질문마다 질문이 시스템 문제점 해결과 관련된 이유에 대한 설명이 제공됩니다. 일부 질문의 경우 시스템에 대한 관련 정보를 얻는 방법을 알아보기 위한 팁 또는 자세한 안내서가 제공됩니다.

이러한 질문은 디버깅 문제의 특성에 기반하여 다양한 환경과 관련되어 있습니다. 예를 들어, 에지 노드의 문제점을 해결할 때 노드에 대한 전체 액세스 권한 및 제어가 필요할 수 있습니다. 그러면 정보를 수집하고 볼 수 있는 기능이 늘어날 수 있습니다.

* [문제점 해결 팁](troubleshooting_devices.md)

  {{site.data.keyword.ieam}} 사용 시 발생할 수 있는 공통 문제를 검토하십시오.
