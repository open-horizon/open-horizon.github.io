{:shortdesc: .shortdesc}
{:new_window: target="_blank"}

# 词汇表
*上次更新时间：2020 年 3 月 12 日*

本词汇表提供 {{site.data.keyword.edge}} 的术语和定义。
{:shortdesc}

本词汇表中使用了以下交叉引用：

- *请参阅*为您指示非首选术语的首选术语或者缩写的完整拼写形式。
- *另请参阅*为您指示相关或对照术语。

<!--If you do not want letter links at the top of your glossary, delete the text between these comment tags.-->

[A](#glossa)
[B](#glossb)
[C](#glossc)
[D](#glossd)
[E](#glosse)
[F](#glossf)
[G](#glossg)
[H](#glossh)
[I](#glossi)
[K](#glossk)
[L](#glossl)
[M](#glossm)
[N](#glossn)
[O](#glosso)
[P](#glossp)
[R](#glossr)
[S](#glosss)
[T](#glosst)
[V](#glossv)
[W](#glossw)

<!--end letter link tags-->

## A
{: #glossa}

### API 密钥 (API key)
{: #x8051010}

传递到 API 以标识调用应用程序或用户的唯一代码。 API 密钥用于对 API 的使用进行跟踪和控制，例如，防止恶意使用或滥用 API。

### 应用程序 (application)
{: #x2000166}

一个或多个计算机程序或软件组件，其提供功能来直接支持特定业务流程。

### 可用性区域 (availability zone)
{: #x7018171}

分配操作员、功能独立的网络基础结构部分。

## B
{: #glossb}

### 引导节点 (boot node)
{: #x9520233}

用于运行安装、配置、节点水平伸缩和集群升级的节点。

## C
{: #glossc}

### 目录 (catalog)
{: #x2000504}

可用于在集群中浏览和安装软件包的集中位置。

### 集群 (cluster)
{: #x2017080}

一组资源、工作程序节点、网络和存储设备，它们可保持应用程序高度可用且准备好在容器中部署。

### 容器 (container)
{: #x2010901}

允许用户同时运行单独的逻辑操作系统实例的系统构造。 容器使用文件系统层以使映像大小降至最低并促进复用。 另请参阅[映像 (image)](#x2024928)、[层 (layer)](#x2028320) 和[注册表 (registry)](#x2064940)。

### 容器映像 (container image)
{: #x8941555}

在 Docker 中，可用于运行应用程序的独立可执行软件（包括代码和系统工具）。

### 容器编排 (container orchestration)
{: #x9773849}

管理容器的生命周期的过程，包括供应、部署和可用性。

## D
{: #glossd}

### 部署 (deployment)
{: #x2104544}

这是检索软件包或映像并将它们安装在已定义位置以便可进行测试或运行的过程。

### DevOps
{: #x5784896}

与应用程序开发和 IT 原因集成的一种软件方法，以便团队可以更快将代码投入生产并根据市场反馈持续迭代。

### Docker
{: #x7764788}

开发人员和系统管理员可用于构建、装运和运行分布式应用程序的开放式平台。

## E
{: #glosse}

### 计算边缘 (edge computing)
{: #x9794155}

利用传统和云数据中心外部可用的计算的分布式计算模型。 边缘计算模型使工作负载更接近于创建关联数据的位置以及执行操作以响应此数据分析的位置。 将数据和工作负载放置在边缘设备上可降低等待时间、降低网络带宽需求、提高敏感信息的隐私并且支持网络中断期间操作。

### 边缘设备 (edge device)
{: #x2026439}

一件具有集成的计算能力从而可执行有意义的工作以及收集或生成数据的设备，例如，厂房中的组合机器、ATM、智能相机或汽车。

### 边缘网关 (edge gateway)
{: #x9794163}

边缘集群包含执行网络功能的服务，例如，协议转换、网络终端、隧道、防火墙保护或无线连接。 边缘网关充当边缘设备或边缘集群与云或更大型网络之间的连接点。

### 边缘节点 (edge node)
{: #x8317015}

发生边缘计算的任何边缘设备、边缘集群或边缘网关。

### 边缘集群 (edge cluster)
{: #x2763197}

远程运营设施中的计算机，其运行企业应用程序工作负载和共享服务。 边缘集群可用于连接到边缘设备、连接到另一个边缘进群或者充当边缘网关以连接到云或更大的网络。

### 边缘服务 (edge service)
{: #x9794170}

专门设计以在边缘集群、边缘网关或边缘设备上部署的服务。 视觉识别、声音洞察和语音识别全都是潜在边缘服务的示例。

### 边缘工作负载 (edge workload)
{: #x9794175}

在边缘节点上运行时执行有意义工作的任何服务、微服务或软件片段。

### 端点 (endpoint)
{: #x2026820}

由 Kubernetes 资源（例如，服务和入口）公开的网络目标地址。

## F
{: #glossf}

## G
{: #glossg}

### Grafana
{: #x9773864}

用于监视、搜索、分析和可视化度量的开放式源代码分析和可视化平台。

## H
{: #glossh}

### HA
{: #x2404289}

请参阅[高可用性 (high availability)](#x2284708)。

### Helm chart
{: #x9652777}

Helm 软件包，其中包含用于将一组 Kubernetes 资源安装到 Kubernetes 集群的信息。

### Helm 发行版 (Helm release)
{: #x9756384}

在 Kubernetes 集群中运行的 Helm Chart 的实例。

### Helm 存储库 (Helm repository)
{: #x9756389}

Chart 集合。

### 高可用性 (high availability, HA)
{: #x2284708}

IT 服务承受所有中断并持续提供处理能力（根据某些预定义的服务级别）的能力。 涵盖的中断包括计划内事件（例如，维护和备份）和计划外事件（例如，软件故障、硬件故障、电源故障和灾难）。 另请参阅[容错 (fault tolerance)](#x2847028)。

## I
{: #glossi}

### IBM Cloud Pak
{: #x9773840}

一个或多个企业级、安全且生命周期受管的 IBM Certified Container 产品软件包，它们在 IBM Cloud 环境中打包在一起并进行集成。

### 映像 (image)
{: #x2024928}

在容器运行时中用来创建容器的文件系统及其执行参数。 文件系统包含在运行时组合的一系列层，它们在后续更新构建映像时创建。 在容器执行时，映像不保留状态。 另请参阅[容器 (container)](#x2010901)、[层 (layer)](#x2028320) 和[注册表 (registry)](#x2064940)。

### 映像注册表 (image registry)
{: #x3735328}

用于管理映像的集中位置。

### 入口 (ingress)
{: #x7907732}

允许建立到 Kubernetes 集群服务的入站连接的规则集合。

### 隔离 (isolation)
{: #x2196809}

将工作负载部署限制为专用虚拟和物理资源以实现多租户支持的过程。

## K
{: #glossk}

### Klusterlet
{: #x9773879}

在 IBM Multicloud Manager 中，是指负责单 Kubernetes 集群的代理程序。

### Kubernetes
{: #x9581829}

用于容器的开放式源代码编排工具。

## L
{: #glossl}

### 层 (layer)
{: #x2028320}

父映像的已更改版本。 映像由层组成，其中已更改的版本位于父映像顶层以创建新映像。 另请参阅[容器 (container)](#x2010901) 和[映像 (image)](#x2024928)。

### 负载均衡器 (load balancer)
{: #x2788902}

在一组服务器上分发工作负载以确保服务器不超负荷的软件或硬件。 如果初始服务器发生故障，那么负载均衡器还会将用户定向到另一他服务器。

## M
{: #glossm}

### 管理控制台 (management console)
{: #x2398932}

{{site.data.keyword.edge_notm}} 的图形用户界面。

### 管理中心 (management hub)
{: #x3954437}

托管 {{site.data.keyword.edge_notm}} 中心组件的集群。

### 市场 (marketplace)
{: #x2118141}

用户可通过其供应资源的已启用服务的列表。

### 主节点 (master node)
{: #x4790131}

提供管理服务且控制集群中的工作程序节点的节点。 负责资源分配、状态维护、调度和监视的进程托管在主节点上。

### 微服务 (microservice)
{: #x8379238}

一组小型的独立体系结构组件，每个具有单独的用途，在公共轻量级 API 上进行通信。

### 多云 (multicloud)
{: #x9581814}

云计算模型，其中企业可使用本地、私有云和公共云体系结构的组合。

## N
{: #glossn}

### 名称空间 (namespace)
{: #x2031005}

Kubernetes 集群中可用于跨多个用户组织和划分资源的虚拟集群。

### 网络文件系统 (Network File System, NFS)
{: #x2031282}

允许计算机通过网络访问文件的协议，就如同文件位本地磁盘一样。

### NFS
{: #x2031508}

请参阅[网络文件系统 (Network File System)](#x2031282)。

## O
{: #glosso}

### org
{: #x7470494}

请参阅[组织 (organization)](#x2032585)。

### 组织 (organization, org)
{: #x2032585}

表示客户对象的 {{site.data.keyword.edge_notm}} 基础结构中的最顶级元对象。

## P
{: #glossp}

### 持久卷 (persistent volume)
{: #x9532496}

管理员供应的集群中的联网存储器。

### 持久卷声明 (persistent volume claim)
{: #x9520297}

集群存储器请求。

### 部署策略 (deployment policy)
{: #x7244520}

定义边缘服务应在何处运行的策略。

### pod
{: #x8461823}

在 Kubernetes 集群上运行的一组容器。 Pod 是可运行工作单元，可以是独立应用程序或微服务。

### pod 安全策略 (pod security policy)
{: #x9520302}

用于设置针对 pod 可执行的操作或可访问的内容的集群级别控制的策略。

### Prometheus
{: #x9773892}

开放式源代码监视和警报工具箱。

### 代理节点 (proxy node)
{: #x6230938}

将外部请求传输到在集群中创建的服务的节点。

## R
{: #glossr}

### RBAC
{: #x5488132}

请参阅[基于角色的访问控制 (role-based access control)](#x2403611)。

### 注册表 (registry)
{: #x2064940}

公用或专用容器映像存储和分发服务。 另请参阅[容器 (container)](#x2010901) 和[映像 (image)](#x2024928)。

### repo
{: #x7639721}

请参阅[存储库 (repository)](#x2036865)。

### 存储库 (repository, repo)
{: #x2036865}

数据和其他应用资源的持久存储区域。

### 资源 (resource)
{: #x2004267}

可针对应用程序或服务实例供应或保留的物理或逻辑组件。 资源示例包括数据库、帐户和处理器、内存以及存储限制。

### 基于角色的访问控制 (role-based access control, RBAC)
{: #x2403611}

基于用户认证、角色和许可权限制系统的整体组件的过程。

## S
{: #glosss}

### 服务代理 (service broker)
{: #x7636561}

服务组件，其实施一个产品和服务计划目录，并解释用于供应和取消供应、绑定和解除绑定的调用。

### 存储节点 (storage node)
{: #x3579301}

用于提供后端存储器和文件系统以在系统中存储数据的节点。

### 系统日志 (syslog)
{: #x3585117}

请参阅[系统日志 (system log)](#x2178419)。

### 系统日志 (system log, syslog)
{: #x2178419}

Cloud Foundry 组件生成的日志。

## T
{: #glosst}

### 团队 (team)
{: #x3135729}

对用户和资源进行分组的实体。

## V
{: #glossv}

### VSAN
{: #x4592600}

请参阅[虚拟存储区域网络 (virtual storage area network)](#x4592596)。

## W
{: #glossw}

### 工作程序节点 (worker node)
{: #x5503637}

在集群中，承载构成应用程序的部署和服务的物理或虚拟机。

### 工作负载 (workload)
{: #x2012537}

执行客户定义的共同目标的虚拟服务器的集合。 工作负载通常可视为多层应用程序。 每个工作负载都与一组定义性能和能源消耗目标的策略相关联。