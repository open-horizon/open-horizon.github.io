---

copyright:
years: 2019
lastupdated: "2019-09-27"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 역할 기반 액세스 제어
{: #rbac}

{{site.data.keyword.edge_notm}}({{site.data.keyword.ieam}})에서는 여러 역할을 지원합니다. 역할은 사용자가 수행할 수 있는 조치를 결정합니다.
{:shortdesc}

## 조직
{: #orgs}

{{site.data.keyword.ieam}}에서는 각 테넌트가 고유한 조직을 소유하는 조직을 통해 멀티테넌시의 일반 개념을 지원합니다. 조직은 리소스를 분리합니다. 따라서 각 조직 내 사용자는 다른 조직에서 리소스를 작성하거나 수정할 수 없습니다. 또한 조직의 리소스는 해당 조직의 사용자만 볼 수 있습니다(리소스가 공용으로 표시되지 않는 한). 공용으로 표시된 리소스는 조직에서 볼 수 있는 유일한 리소스입니다.

IBM 조직은 사전 정의된 서비스와 패턴을 제공합니다. 해당 조직의 리소스는 공용이지만, {{site.data.keyword.ieam}} 관리 허브에서 모든 공용 컨텐츠를 보유하도록 의도된 것은 아닙니다.

기본적으로 조직은 선택한 이름으로 {{site.data.keyword.ieam}} 설치 중에 작성됩니다. 필요한 경우 추가 조직을 작성할 수 있습니다. 관리 허브에 조직을 추가하는 방법에 대한 자세한 정보는 [멀티테넌시](../admin/multi_tenancy.md)를 참조하십시오.

## ID
{: #ids}

{{site.data.keyword.ieam}}에는 네 가지 유형의 ID가 있습니다.

* IAM(Identity and Access Management) 사용자. IAM 사용자는 모든 {{site.data.keyword.ieam}} 컴포넌트(UI, Exchange, **hzn** CLI, **cloudctl** CLI, **oc** CLI, **kubectl** CLI)에서 인식됩니다.
  * IAM에서 LDAP 플러그인을 제공하므로, IAM에 연결된 LDAP 사용자가 IAM 사용자와 같이 동작합니다.
  * IAM API 키(**hzn** 명령과 함께 사용)는 IAM 사용자와 같이 동작합니다.
* Exchange 전용 사용자: Exchange 루트 사용자가 이 예에 해당합니다. 일반적으로 다른 로컬 Exchange 전용 사용자는 작성하지 않아도 됩니다. 우수 사례로, IAM에서 사용자를 관리하고 {{site.data.keyword.ieam}}에 인증하기 위해 사용자 인증 정보 또는 해당 사용자와 연관된 API 키를 사용하십시오.
* Exchange 노드(에지 디바이스 또는 에지 클러스터)
* Exchange agbots

### 역할 기반 액세스 제어(RBAC)
{: #rbac_roles}

{{site.data.keyword.ieam}}에는 다음 역할이 포함되어 있습니다.

| **역할**    | **액세스**    |  
|---------------|--------------------|
| IAM 사용자 | IAM을 통해 이러한 관리 허브 역할(클러스터 관리자, 관리자, 운영자, 편집자, 뷰어)을 제공할 수 있습니다. IAM 역할은 IAM 팀에 추가할 때 사용자 또는 사용자 그룹에 지정됩니다. 리소스에 대한 팀 액세스는 Kubernetes 네임스페이스를 통해 제어할 수 있습니다. IAM 사용자는 **hzn exchange** CLI를 사용하여 아래 Exchange 역할을 지정할 수 있습니다. |
| Exchange 루트 사용자 | Exchange에서 무제한 권한이 있습니다. 이 사용자는 Exchange 구성 파일에 정의됩니다. 원하는 경우 사용 안함으로 설정할 수 있습니다. |
| Exchange 허브 관리자 사용자 | 조직의 목록을 보고, 조직에서 사용자를 보며, 조직을 작성 또는 삭제할 수 있습니다. |
| Exchange 조직 관리자 사용자 | 조직에서 무제한 Exchange 권한을 보유합니다. |
| Exchange 사용자 | 조직에 Exchange 리소스(노드, 서비스, 패턴, 정책)를 작성할 수 있습니다. 이 사용자가 소유한 리소스를 업데이트하거나 삭제할 수 있습니다. 조직의 모든 서비스, 패턴 및 정책과 다른 조직의 공용 서비스 및 패턴을 읽을 수 있습니다. 이 사용자가 소유한 노드를 읽을 수 있습니다. |
| Exchange 노드 | Exchange의 고유 노드를 읽고, 조직의 모든 서비스, 패턴 및 정책과 다른 조직의 공용 서비스와 패턴을 읽을 수 있습니다. 이 역할에는 에지 노드를 작동하는 데 필요한 최소 권한이 있으므로 에지 노드에 저장되어야 하는 유일한 인증 정보입니다.|
| Exchange agbots | IBM 조직의 Agbot은 모든 조직의 모든 노드, 서비스, 패턴 및 정책을 읽을 수 있습니다. |
{: caption="표 1. RBAC 역할" caption-side="top"}
