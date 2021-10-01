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

일반적으로 에지 클러스터에서 실행할 서비스를 개발하는 것은 에지 디바이스에서 실행되는 에지 서비스를 개발하는 것과
유사하지만, 에지 서비스를 배치하는 방식은 다릅니다. 에지 클러스터에 컨테이너화된 에지 서비스를 배치하려면 개발자가 Kubernetes 클러스터에서 컨테이너화된 에지 서비스를 배치하는 Kubernetes 연산자를 먼저 빌드해야 합니다. 연산자가 작성되고 테스트된 후에 개발자가 IBM Edge Application Manager(IEAM) 서비스로 연산자를 작성하고 공개합니다. 이 프로세스는 정책 또는 패턴과 함께 IEAM 서비스에 대해 수행되는 방식처럼 IEAM 관리자가 연산자 서비스를 배치하도록 합니다.

배치 정책을 사용하여 IEAM Exchange에서 이미 공개한 `ibm.operator` 서비스를 사용하여
클러스터에서 `helloworld` 컨테이너화된 서비스를 실행하려면
[Horizon Operator 예제 에지 서비스 ![새 탭에 열림](../../images/icons/launch-glyph.svg "새 탭에 열림")](https://github.com/open-horizon/examples/tree/master/edge/services/operator#horizon-operator-example-edge-service)를 참조하십시오.
