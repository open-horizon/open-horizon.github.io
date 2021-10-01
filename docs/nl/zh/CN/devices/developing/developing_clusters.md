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

# 为集群开发边缘服务
{: #developing_clusters}

{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) 边缘集群功能为您提供边缘计算功能，帮助您管理工作负载并将其从管理中心集群部署到 OpenShift® Container Platform 4.2 或其他基于 Kubernetes 的集群的远程实例。 边缘集群是作为 Kubernetes 集群的 {{site.data.keyword.ieam}} 边缘节点。 边缘集群启用位于边缘的用例，这要求计算与业务运营共存，或要求可伸缩性、可用性和计算功能多于边缘设备可支持的范围。此外，边缘集群提供支持在边缘设备上运行的服务所需的应用程序服务并不少见，因为它们非常接近边缘设备，从而形成多层边缘应用程序。{{site.data.keyword.ieam}} 通过 Kubernetes 操作程序将边缘服务部署到边缘集群，以启用与边缘设备配合使用的相同自主部署机制。 Kubernetes 作为容器管理平台的全部功能可用于由 {{site.data.keyword.ieam}} 部署的边缘服务。

<img src="../../images/edge/03b_Developing_edge_service_for_cluster.svg" width="80%" alt="为集群开发边缘服务">

* [开发 Kubernetes 操作程序](service_operators.md)
* [为集群创建您自己的 Hello world](creating_hello_world.md)
