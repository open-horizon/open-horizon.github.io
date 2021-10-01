---

copyright:
years: 2020
lastupdated: "2020-05-11"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# {{site.data.keyword.edge_notm}} 개요
{: #overviewofedge}

이 절에서는 {{site.data.keyword.edge_notm}}({{site.data.keyword.ieam}})의 개요를 제공합니다.

## {{site.data.keyword.ieam}} 기능
{: #capabilities}

{{site.data.keyword.ieam}}은 허브 클러스터의 워크로드를 관리하고 OpenShift Container Platform 또는 기타 Kubernetes 기반 클러스터의 원격 인스턴스 및 에지 디바이스에 배치하는 데 도움이 되는 에지 컴퓨팅 기능을 제공합니다.

## 아키텍처

에지 컴퓨팅의 목표는 하이브리드 클라우드 컴퓨팅용으로 작성된 원칙을 활용하여 에지 컴퓨팅 기능의 원격 오퍼레이션을 지원하는 것입니다. {{site.data.keyword.ieam}}은 이 목적으로 디자인되었습니다.

{{site.data.keyword.ieam}}의 배치에는 데이터 센터에 설치된 OpenShift Container Platform의 인스턴스에서 실행되는 관리 허브가 포함됩니다. 관리 허브는 모든 원격 에지 노드(에지 디바이스 및 에지 클러스터)의 관리가 수행되는 위치입니다.

이러한 에지 노드를 원격 온프레미스 위치에 설치하여 애플리케이션 워크로드를 중요한 비즈니스 오퍼레이션이 실제로 발생하는 위치(예: 작업 현장, 창고, 소매점, 물류 센터 등)에 로컬로 만들 수 있습니다.

다음 다이어그램은 일반 에지 컴퓨팅 설정에 대한 상위 레벨 토폴로지를 보여줍니다.

<img src="../OH/docs/images/edge/01_OH_overview.svg" style="margin: 3%" alt="IEAM overview">

{{site.data.keyword.ieam}} 관리 허브는 배치 위험을 최소화하고 에지 노드의 서비스 소프트웨어 라이프사이클을 완전히 자율적으로 관리하기 위해 특별히 에지 노드 관리용으로 디자인되었습니다. 클라우드 설치 프로그램은 {{site.data.keyword.ieam}} 관리 허브 컴포넌트를 설치 및 관리합니다. 소프트웨어 개발자는 에지 서비스를 개발하여 관리 허브에 공개합니다. 관리자는 에지 서비스가 배치되는 위치를 제어하는 배치 정책을 정의합니다. {{site.data.keyword.ieam}}에서는 이외 모든 사항을 처리합니다.

# 컴포넌트
{: #components}

{{site.data.keyword.ieam}}에 번들된 컴포넌트에 대한 자세한 정보는 [컴포넌트](components.md)를 참조하십시오.

## 다음 수행할 작업

{{site.data.keyword.ieam}} 사용 및 에지 서비스 개발에 대한 자세한 정보는 {{site.data.keyword.edge_notm}}({{site.data.keyword.ieam}}) [시작 페이지](../kc_welcome_containers.html)에 나열된 주제를 검토하십시오.
