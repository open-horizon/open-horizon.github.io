---

copyright:
  years: 2020
lastupdated: "2020-05-9"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 에지 클러스터 서비스
{: #Edge_cluster_service}

일반적으로 에지 클러스터에서 실행할 서비스를 개발하는 것은 에지 디바이스에서 실행되는 에지 서비스를 개발하는 것과 유사하지만, 에지 서비스를 배치하는 방식은 다릅니다. 에지 클러스터에 컨테이너화된 에지 서비스를 배치하려면 개발자가 Kubernetes 클러스터에서 컨테이너화된 에지 서비스를 배치하는 Kubernetes 연산자를 먼저 빌드해야 합니다. 연산자가 작성되고 테스트된 후에 개발자가 {{site.data.keyword.edge_notm}}({{site.data.keyword.ieam}}) 서비스로 연산자를 작성하고 공개합니다. {{site.data.keyword.edge_notm}} 서비스와 마찬가지로 정책 또는 패턴을 사용하여 연산자 서비스를 에지 클러스터에 배치할 수 있습니다.

{{site.data.keyword.ieam}} Exchange에는 외부에서 `curl` 명령을 사용하여 액세스할 수 있는 에지 클러스터에 포트를 노출할 수 있도록 하는 `hello-operator`라는 서비스가 포함되어 있습니다. 에지 클러스터에 이 예제 서비스를 배치하려면 [Horizon Operator 예제 에지 서비스](https://github.com/open-horizon/examples/tree/v2.27/edge/services/hello-operator#-using-the-operator-example-edge-service-with-deployment-policy)를 참조하십시오.
