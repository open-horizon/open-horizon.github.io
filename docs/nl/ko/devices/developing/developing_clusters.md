---

copyright:
  years: 2020
lastupdated: "2020-04-9"

---

{:shortdesc: .shortdesc}
{:new_window: target="_blank"}
{:codeblock: .codeblock}
{:pre: .pre}
{:screen: .screen}
{:tip: .tip}
{:download: .download}

# 클러스터에 대한 에지 서비스 개발
{: #developing_clusters}

{{site.data.keyword.edge_notm}}({{site.data.keyword.ieam}}) 에지 클러스터 기능은 허브 클러스터의 워크로드를 관리하고 OpenShift® Container Platform 또는 기타 Kubernetes 기반 클러스터의 원격 인스턴스에 배치하는 데 도움이 되는 에지 컴퓨팅 기능을 제공합니다. 에지 클러스터는 Kubernetes 클러스터인 {{site.data.keyword.ieam}} 에지 노드입니다. 에지 클러스터는 에지에서 비즈니스 운영을 포함하는 컴퓨팅 코로케이션을 요구하는 유스 케이스를 사용하도록 하거나, 에지 디바이스에서 지원할 수 있는 것보다 더 큰 확장성, 가용성 및 컴퓨팅 기능을 요구하는 유스 케이스를 사용하도록 합니다. 또한 에지 디바이스에 대한 밀접 접근성으로 인해 에지 클러스터가 에지 디바이스에서 실행되는 서비스를 지원하는 데 필요한 애플리케이션 서비스를 제공하는 것은 드문 경우가 아닙니다(멀티티어 에지 애플리케이션이 됨). {{site.data.keyword.ieam}}에서는 에지 디바이스와 함께 사용된 동일한 자율 배치 메커니즘을 사용으로 설정하여 Kubernetes 연산자를 통해 에지 클러스터에 에지 서비스를 배치합니다. 컨테이너 관리 플랫폼인 풀파워 Kubernetes를 {{site.data.keyword.ieam}}에서 배치한 에지 서비스에 사용할 수 있습니다.

<img src="../../images/edge/03b_Developing_edge_service_for_cluster.svg" width="80%" alt="클러스터에 대한 에지 서비스 개발">

* [Kubernetes 연산자 개발](service_operators.md)
* [클러스터에 대한 고유한 Hello World 작성](creating_hello_world.md)
