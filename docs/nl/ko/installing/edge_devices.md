---

copyright:
years: 2020
lastupdated: "2020-4-8"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 에지 디바이스
{: #edge_devices}

에지 디바이스는 엔터프라이즈 또는 서비스 제공자 코어 네트워크에 시작점을 제공합니다. 예제에는 스마트폰, 보안 카메라 또는 인터넷에 연결된 전자 레인지도 포함됩니다.

{{site.data.keyword.edge_notm}}({{site.data.keyword.ieam}})는 분산된 디바이스를 포함하여 관리 허브 또는 서버에 사용 가능합니다. 에지 디바이스에 {{site.data.keyword.ieam}} 경량 에이전트를 설치하는 방법에 대한 자세한 정보는 다음 절을 참조하십시오.

* [에지 디바이스 준비](../installing/adding_devices.md)
* [에이전트 설치](../installing/registration.md)
* [에이전트 업데이트](../installing/updating_the_agent.md)

모든 에지 디바이스(에지 노드)에서는 {{site.data.keyword.horizon_agent}} 소프트웨어를 설치해야 합니다. {{site.data.keyword.horizon_agent}}도 [Docker](https://www.docker.com/) 소프트웨어에 따라 다릅니다. 

에지 디바이스를 중심으로 다음 다이어그램은 에지 디바이스를 설정하기 위해 수행하는 단계 플로우 및 시작 후 에이전트가 수행하는 작업을 표시합니다.

<img src="../OH/docs/images/edge/05a_Installing_edge_agent_on_device.svg" style="margin: 3%" alt="{{site.data.keyword.horizon_exchange}}, agbots and agents">
