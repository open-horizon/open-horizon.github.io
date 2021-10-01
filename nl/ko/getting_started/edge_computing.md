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

# 에지 컴퓨팅 개요
{: #overviewofedge}

## {{site.data.keyword.edge_notm}} 기능
{: #capabilities}

{{site.data.keyword.edge_notm}}(IEAM)는 Docker 및 Kubernetes와 같은 널리 사용되는 표준 및 오픈 테크놀로지로 최적화된 다중 티어 및 업계에 분포되어 있습니다. 여기에는 컴퓨팅 플랫폼(개인용 클라우드 및 엔터프라이즈 환경 모두), 네트워크 컴퓨팅 공간 및 온프레미스 게이트웨이, 컨트롤러 및 서버, 지능형 디바이스가 포함됩니다.

<img src="../images/edge/01_IEAM_overview.svg" width="100%" alt="IEAM 개요">

중앙에서 하이퍼 스케일 공용 클라우드, 하이브리드 클라우드, 공동 배치된 관리형 데이터 센터, 기존 엔터프라이즈 데이터 센터는 지속적으로 데이터, 분석, 백엔드 데이터 처리를 위한 집계 지점 역할을 지원합니다.

공용, 개인용, 컨텐츠 전달 네트워크는 단순한 파이프에서 에지 네트워크 클라우드 형태의 애플리케이션을 위한 고부가 가치의 호스팅 환경으로 바뀌고 있습니다. {{site.data.keyword.ieam}}의 일반적인 유스 케이스는 다음과 같습니다.

* 하이브리드 클라우드 컴퓨팅
* 5G 네트워킹 
* 에지 서버 배치
* 에지 서버 컴퓨팅 오퍼레이션 용량
* IoT 디바이스 지원 및 최적화

IBM Multicloud Management Core 1.2에서는 온프레미스에서 에지에 이르기까지 일관된 대시보드로 여러 공급업체의 클라우드 플랫폼을 통합합니다. {{site.data.keyword.ieam}}은 에지 네트워크를 넘어 에지 게이트웨이 및 에지 디바이스로 워크로드의 분산과 관리를 가능하게 하는 자연스러운 확장입니다. IBM Multicloud Management Core 1.2는 에지 컴포넌트, 개인용 및 하이브리드 클라우드 환경, 공용 클라우드에서 엔터프라이즈 애플리케이션의 워크로드를 인식합니다. 여기에서 IBM Edge Computing Manager는 중요한 데이터 소스에 도달하기 위해 분산된 AI를 위한 새로운 실행 환경을 제공합니다.

또한 IBM Multicloud Manager-CE에서는 가속화된 딥 러닝, 시각 및 음성 인식, 비디오 및 청각 분석을 위한 AI 도구를 제공합니다. 이를 통해 모든 해상도와 대부분의 비디오와 오디오 대화 서비스 및 검색 형식에서 추론이 가능해집니다.

## {{site.data.keyword.edge_notm}} 위험 및 해결
{: #risks}

{{site.data.keyword.ieam}}은 고유한 기회를 창출하지만, 과제도 안고 있습니다. 예를 들어, 클라우드 데이터 센터의 물리적 경계를 초월하므로, 보안, 주소 지정, 관리, 소유권, 규제 준수의 문제에 노출될 수 있습니다. 더욱 중요한 점은, 클라우드 기반 관리 기술의 확장 문제로 배가됩니다.

에지 네트워크는 차수만큼 컴퓨팅 노드 수를 늘립니다. 에지 게이트웨이는 또 다른 차수만큼 이를 더 늘립니다. 에지 디바이스는 3 - 4의 차수만큼 이 수를 늘립니다. DevOps(지속적 딜리버리 및 지속적 배치)는 하이퍼 스케일 클라우드 인프라를 관리하는 데 중요한 역할을 하며, Zero-Ops(사람의 개입이 없는 오퍼레이션)는 {{site.data.keyword.ieam}}에서 대표하는 대규모 관리에 중요합니다.

사람의 개입 없이 에지 컴퓨팅 공간을 배치, 업데이트, 모니터링, 복구하는 것이 중요합니다. 이러한 활동과 프로세스는 모두 다음 조건을 충족해야 합니다.

* 완전히 자동화됨
* 작업 할당에 대한 독립적인 의사결정이 가능함
* 개입 없이 조건 변경을 인식하고 복구할 수 있음 

이러한 모든 활동은 안전하고 추적 가능하며 방어 가능해야 합니다.

<!--{{site.data.keyword.edge_devices_notm}} delivers edge node management that minimizes deployment risks and manages the service software lifecycle on edge nodes fully autonomously. This function creates the capacity to achieve meaningful insights more rapidly from data that is captured closer to its source. {{site.data.keyword.edge_notm}} is available for infrastructure or servers, including distributed devices.
{:shortdesc}

Intelligent devices are being integrated into the tools that are used to conduct business at an ever-increasing rate. Device compute capacity is creating new opportunities for data analysis where data originates and actions are taken. {{site.data.keyword.edge_notm}} innovations fuel improved quality, enhance performance, and drive deeper, more meaningful user interactions. 

{{site.data.keyword.edge_notm}} can:

* Solve new business problems by using Artificial Intelligence (AI)
* Increase capacity and resiliency
* Improve security and privacy protections
* Leverage 5G networks to reduce latency

{{site.data.keyword.edge_notm}} can capture the potential of untapped data that is created by the unprecedented growth of connected devices, which opens new business opportunities, increases operational efficiency, and improves customer experiences. {{site.data.keyword.edge_notm}} brings Enterprise applications closer to where data is created and actions need to be taken, and it allows Enterprises to leverage AI and analyze data in near-real time.

## {{site.data.keyword.edge_notm}} benefits
{: #benefits}

{{site.data.keyword.edge_notm}} helps solve speed and scale challenges by using the computational capacity of edge devices, gateways, and networks. This function retains the principles of dynamic allocation of resources and continuous delivery that are inherent to cloud computing. With {{site.data.keyword.edge_notm}}, businesses have the potential to virtualize the cloud beyond data centers. Workloads that are created in the cloud can be migrated towards the edge, and where appropriate, data that is generated at the edge can be cleansed and optimized and brought back to the cloud.

{{site.data.keyword.edge_devices_notm}} spans industries and multiple tiers that are optimized with open technologies and prevailing standards like Docker and Kubernetes. This includes computing platform, both private cloud and Enterprise environments, network compute spaces and on-premises gateways, controllers and servers, and intelligent devices.

Centrally, the hyper-scale public clouds, hybrid clouds, colocated managed data centers and traditional Enterprise data centers continue to serve as aggregation points for data, analytics, and back-end data processing.

Public, private, and content-delivery networks are transforming from simple pipes to higher-value hosting environments for applications in the form of the edge network cloud.

{{site.data.keyword.edge_devices_notm}} offers: 

* Integrated offerings that provide faster insights and actions, secure and continuous operations.
* The industry's first policy-based, autonomous edge computing platform
that intelligently manages workload life cycles in a secure and flexible way.
* Open technology and ecosystems compatibility to provide robust support and innovation for industry-wide ecosystems and partners.
* Scalable solutions for wide-ranging deployment on edge devices, servers, gateways, and network elements.

## {{site.data.keyword.edge_notm}} capabilities
{: #capabilities}

* Hybrid cloud computing
* 5G networking 
* Edge server deployment
* Edge servers compute operations capacity
* IoT devices support and optimization

## {{site.data.keyword.edge_notm}} risks and resolution
{: #risks}

Although {{site.data.keyword.edge_notm}} creates unique opportunities, it also presents challenges. For example, it transcends cloud data center's physical boundaries, which can expose security, addressability, management, ownership, and compliance issues. More importantly, it multiplies the scaling issues of cloud-based management techniques.

Edge networks increase the number of compute nodes by an order of magnitude. Edge gateways increase that by another order of magnitude. Edge devices increase that number by 3 to 4 orders of magnitude. If DevOps (continuous delivery and continuous deployment) is critical to managing a hyper-scale cloud infrastructure, then zero-ops (operations with no human intervention) is critical to managing at the massive scale that {{site.data.keyword.edge_notm}} represents.

It is critical to deploy, update, monitor, and recover the edge compute space without human intervention. All of these activities and processes must be fully automated, capable of making decisions independently about work allocation, and able to recognize and recover from changing conditions without intervention. All of these activities must be secure, traceable, and defensible.

## Extending multi-cloud deployments to the edge
{: #extend_deploy}

{{site.data.keyword.mcm_core_notm}} unifies cloud platforms from multiple vendors into a consistent dashboard from on-premises to the edge. {{site.data.keyword.edge_devices_notm}} is a natural extension that enables the distribution and management of workloads beyond the edge network to edge gateways and edge devices.

{{site.data.keyword.mcm_core_notm}} recognizes workloads from Enterprise applications with edge components, private and hybrid cloud environments, and public cloud; where {{site.data.keyword.edge_notm}} provides a new execution environment for distributed AI to reach critical data sources.

{{site.data.keyword.mcm_ce_notm}} delivers AI tools for accelerated deep learning, visual and speech recognition, and video and acoustic analytics, which enables inferencing on all resolutions and most formats of video and audio conversation services and discovery.

## {{site.data.keyword.edge_devices_notm}} architecture
{: #iec4d_arch}

Other edge computing solutions typically focus on one of the following architectural strategies:

* A powerful centralized authority for enforcing edge node software compliance.
* Passing the software compliance responsibility down to the edge node owners, who are required to monitor for software updates, and manually bring their own edge nodes into compliance.

The former focuses authority centrally, creating a single point of failure, and a target that attackers can exploit to control the entire fleet of edge nodes. The latter solution can result in large percentages of the edge nodes not having the latest software updates installed. If edge nodes are not all on the latest version or have all of the available fixes, the edge nodes can be vulnerable to attackers. Both approaches also typically rely upon the central authority as a basis for the establishment of trust.

<p align="center">
<img src="../images/edge/overview_illustration.svg" width="70%" alt="Illustration of the global reach of edge computing.">
</p>

In contrast to those solution approaches, {{site.data.keyword.edge_devices_notm}} is decentralized. {{site.data.keyword.edge_devices_notm}} manages service software compliance automatically on edge nodes without any manual intervention. On each edge node, decentralized and fully autonomous agent processes run governed by the policies that are specified during the machine registration with {{site.data.keyword.edge_devices_notm}}. Decentralized and fully autonomous agbot (agreement bot) processes typically run in a central location, but can run anywhere, including on edge nodes. Like the agent processes, the agbots are governed by policies. The agents and agbots handle most of the edge service software lifecycle management for the edge nodes and enforce software compliance on the edge nodes.

For efficiency, {{site.data.keyword.edge_devices_notm}} includes two centralized services, the exchange and the switchboard. These services have no central authority over the autonomous agent and agbot processes. Instead, these services provide simple discovery and metadata sharing services (the exchange) and a private mailbox service to support peer-to-peer communications (the switchboard). These services support the fully autonomous work of the agents and agbots.

Lastly, the {{site.data.keyword.edge_devices_notm}} console helps administrators set policy and monitor the status of the edge nodes.

Each of the five {{site.data.keyword.edge_devices_notm}} component types (agents, agbots, exchange, switchboard, and console) has a constrained area of responsibility. Each component has no authority or credentials to act outside their respective area of responsibility. By dividing responsibility and scoping authority and credentials, {{site.data.keyword.edge_devices_notm}} offers risk management for edge node deployment.

WRITER NOTE: content from https://www-03preprod.ibm.com/support/knowledgecenter/SSFKVV_4.1/hub/offline_installation.html

Merge the content in this section with the above content.

## {{site.data.keyword.edge_devices_notm}}
{: #edge_devices}

{{site.data.keyword.edge_devices_notm}} provides you with a new architecture for edge node management. It is designed specifically to minimize the risks that are inherent in the deployment of either a global or local fleet of edge nodes. You can also use {{site.data.keyword.edge_devices_notm}} to manage the service software lifecycle on edge nodes fully autonomously.
{:shortdesc}

{{site.data.keyword.edge_devices_notm}} is built on the {{site.data.keyword.horizon_open}} project. For more information about the project, see [{{site.data.keyword.horizon_open}} ![Opens in a new tab](../../images/icons/launch-glyph.svg "Opens in a new tab")](https://github.com/open-horizon).-->

{{site.data.keyword.edge_notm}} 사용 및 에지 서비스 개발에 대한 자세한 정보는 다음 주제 및 주제 그룹을 검토하십시오.

* [관리 허브 설치](../hub/offline_installation.md) {{site.data.keyword.edge_devices_notm}} 인프라를 설치 및 구성하고 에지 서비스를 추가하는 데 필요한 파일을 수집하는 방법을 학습합니다.

* [에지 노드 설치](../devices/installing/installing_edge_nodes.md) {{site.data.keyword.edge_devices_notm}} 인프라를 설치 및 구성하고 에지 서비스를 추가하는 데 필요한 파일을 수집하는 방법을 학습합니다.
  
* [에지 서비스 사용](../devices/developing/using_edge_services.md)
  {{site.data.keyword.edge_notm}} 에지 서비스 사용에 대해 학습합니다.

* [에지 서비스 개발](../devices/developing/developing_edge_services.md)
  {{site.data.keyword.edge_notm}} 에지 서비스 사용에 대해 학습합니다.

* [관리](../devices/administering_edge_devices/administering.md)
  {{site.data.keyword.edge_notm}} 에지 서비스 관리 방법을 학습합니다. 
  
* [보안](../devices/user_management/security.md)
  {{site.data.keyword.edge_notm}}이 공격에 대해 보안을 유지보수하고 참가자 개인 정보를 보호하는 방법에 대해 자세히 알아봅니다.

* [관리 콘솔 사용](../devices/getting_started/accessing_ui.md)
  자주 묻는 질문(FAQ)을 검토하여 {{site.data.keyword.edge_notm}}에 대한 주요 정보를 빠르게 학습할 수 있습니다.

* [CLI 사용](../devices/getting_started/using_cli.md)
  자주 묻는 질문(FAQ)을 검토하여 {{site.data.keyword.edge_notm}}에 대한 주요 정보를 빠르게 학습할 수 있습니다.

* [API](../devices/installing/edge_rest_apis.md)
  자주 묻는 질문(FAQ)을 검토하여 {{site.data.keyword.edge_notm}}에 대한 주요 정보를 빠르게 학습할 수 있습니다.

* [문제점 해결](../devices/troubleshoot/troubleshooting.md)
  {{site.data.keyword.edge_devices_notm}}를 설정하거나 사용하는 중에 문제점이 발생하는 경우 발생할 수 있는 공통 문제 및 문제를 해결하는 데 도움이 될 수 있는 팁을 검토하십시오.
