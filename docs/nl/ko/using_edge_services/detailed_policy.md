---

copyright:
years: 2019, 2020
lastupdated: "2020-01-22"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 에지 서비스 개발
{: #detailed_deployment_policy}

정책 또는 패턴을 사용하여 {{site.data.keyword.edge_notm}} {{site.data.keyword.ieam}} 정책을 개발할 수 있습니다. 다양한 시스템 컴포넌트의 보다 포괄적인 개요는 [{{site.data.keyword.edge}} 개요](../getting_started/overview_ieam.md) 및 [배치 정책 유스 케이스](policy_user_cases.md)를 참조하십시오. 실천적인 정책 예에 대해서는 [에지 서비스에 대한 CI-CD 프로세스](../developing/cicd_process.md)를 참조하십시오.

참고: 관리 콘솔에서 배치 정책 또는 패턴을 작성하고 관리할 수도 있습니다. [관리 콘솔 사용](../console/accessing_ui.md)을 참조하십시오.

이 절에서는 정책 및 패턴 개념을 논의하며 유스 케이스 시나리오를 포함합니다.

관리자가 수 천개의 에지 노드를 동시에 관리할 수 없기 때문에 수 만개 이상으로 확장하면 불가능한 상황이 만들어집니다. 이 스케일링 수준을 달성하기 위해 {{site.data.keyword.edge_notm}}는 정책을 사용하여 서비스 및 머신 학습 모델을 자율적으로 배치하는 장소와 시기를 판별합니다. 

정책은 모델, 노드, 서비스 및 배치 정책에 적용되는 탄력적인 정책 언어를 통해 표현됩니다. 정책 언어가 속성(`특성`이라고 부름)과 자산 특정 요구사항(`제한조건`이라고 함)을 정의합니다. 이것은 시스템의 각 부분이 {{site.data.keyword.edge_notm}} 배치 엔진에 입력을 제공할 수 있게 합니다. 서비스를 배치할 수 있기 전에, 모델, 노드, 서비스 및 배치 정책 제한조건을 점검하여 모든 요구사항이 만족되는지 확인합니다.

노드(서비스가 배치되는 장소)가 요구사항을 표현할 수 있다는 사실로 인해서, {{site.data.keyword.edge_notm}} 정책을 양방향 정책 시스템이라고 설명합니다. 노드는 {{site.data.keyword.edge_notm}} 정책 배치 시스템에서 노예가 아닙니다. 결과적으로, 정책은 패턴보다 서비스 및 모델 배치에 대한 더 세분화된 제어를 제공합니다. 정책이 사용 중일 때, {{site.data.keyword.edge_notm}}는 주어진 서비스를 배치할 수 있는 노드를 검색하고 기존 노드를 분석하여 계속 준수하는지(정책에 있어서) 여부를 확인합니다. 노드는 원래 서비스를 배치한 노드, 서비스 및 배치 정책이 계속 효력을 갖고 있을 때 또는 해당 정책 중 하나에 대한 변경사항이 정책 호환성에 영향을 주지 않을 때 정책을 준수합니다. 정책 사용은 에지 노드 소유자, 서비스 개발자 및 비즈니스 소유자가 독립적으로 자신의 정책을 분명하게 표현할 수 있게 함으로써 문제점을 더 잘 구분하게 합니다.

정책은 배치 패턴의 대안입니다. 개발자가 Horizon Exchange에 에지 서비스를 공개한 후에 {{site.data.keyword.ieam}} 허브에 패턴을 공개할 수 있습니다. hzn CLI는 서비스 배치 패턴 나열, 공개, 확인, 업데이트 및 제거 명령을 포함하여 Horizon Exchange에서 패턴을 나열하고 관리하는 기능을 제공합니다. 또한 특정 배치 패턴과 연관된 암호화 키를 나열하고 제거하는 방법도 제공합니다.

* [배치 정책 유스 케이스](policy_user_cases.md)
* [패턴 사용](using_patterns.md)
