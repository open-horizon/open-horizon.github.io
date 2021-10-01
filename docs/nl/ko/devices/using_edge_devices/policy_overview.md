---

copyright:
years: 2020
lastupdated: "2020-4-24"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 정책 개요
{: #policy_overview}

정책에 포함된 일부를 표시하는 그래픽을 추가하십시오(예: 노드, 서비스 및 비즈니스 정책, 제한조건, 특성). 

이 절에서는 정책 개념을 설명합니다. 

다양한 시스템 컴포넌트의 보다 포괄적인 개요는 [IBM Edge Application Manager for Devices가 작동하는 방법의 개요](../getting_started/overview.md)를 참조하십시오. 실천적인 정책 예에 대해서는 [Hello world](../getting_started/policy.md)를 참조하십시오.

관리자가 수 천개의 에지 노드를 동시에 관리할 수 없기 때문에 수 만개 이상으로 확장하면 불가능한 상황이 만들어집니다. 이 스케일링 수준을 달성하기 위해 {{site.data.keyword.edge_devices_notm}}는 정책을 사용하여 서비스 및 머신 학습 모델을 자율적으로 배치하는 장소와 시기를 판별합니다. 정책은 배치 패턴의 대안입니다.

정책은 모델, 노드, 서비스 및 배치 정책에 적용되는 탄력적인 정책 언어를 통해 표현됩니다. 정책 언어가 속성(`특성`이라고 부름)과 자산 특정 요구사항(`제한조건`이라고 함)을 정의합니다. 이것은 시스템의 각 부분이 {{site.data.keyword.edge_devices_notm}} 배치 엔진에 입력을 제공할 수 있게 합니다. 서비스를 배치할 수 있기 전에, 모델, 노드, 서비스 및 배치 정책 제한조건을 점검하여 모든 요구사항이 만족되는지 확인합니다.

노드(서비스가 배치되는 장소)가 요구사항을 표현할 수 있다는 사실로 인해서, {{site.data.keyword.edge_devices_notm}} 정책을 양방향 정책 시스템이라고 설명합니다. 노드는 {{site.data.keyword.edge_devices_notm}} 정책 배치 시스템에서 노예가 아닙니다. 결과적으로, 정책은 패턴보다 서비스 및 모델 배치에 대한 더 세분화된 제어를 제공합니다. 정책이 사용 중일 때, {{site.data.keyword.edge_devices_notm}}는 주어진 서비스를 배치할 수 있는 노드를 검색하고 기존 노드를 분석하여 계속 준수하는지(정책에 있어서) 여부를 확인합니다. 노드는 원래 서비스를 배치한 노드, 서비스 및 배치 정책이 계속 효력을 갖고 있을 때 또는 해당 정책 중 하나에 대한 변경사항이 정책 호환성에 영향을 주지 않을 때 정책을 준수합니다. 정책 사용은 에지 노드 소유자, 서비스 개발자 및 비즈니스 소유자가 독립적으로 자신의 정책을 분명하게 표현할 수 있게 함으로써 문제점을 더 잘 구분하게 합니다.

다음 4가지 정책 유형이 있습니다.

* 노드
* 서비스
* 배치
* 모델
