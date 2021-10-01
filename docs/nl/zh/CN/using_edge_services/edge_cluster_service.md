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

# 边缘集群服务
{: #Edge_cluster_service}

通常，开发要在边缘集群中运行的服务与开发在边缘设备上运行的边缘服务相似，但区别在于边缘服务的部署方式。 要将容器化边缘服务部署到边缘集群，开发人员必须先构建在 Kubernetes 集群中部署容器化边缘服务的 Kubernetes 操作程序。 在编写并测试此操作程序后，开发人员创建此操作程序并将其作为 {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) 服务进行发布。 可以使用与任何 {{site.data.keyword.edge_notm}} 服务一样的策略或模式将操作程序服务部署到边缘集群。

{{site.data.keyword.ieam}} Exchange 包含一个名为 `hello-operator` 的服务，允许您在边缘集群上公开可在外部使用 `curl` 命令访问的端口。 要将此示例服务部署到边缘集群，请参阅 [Horizon操作程序示例边缘服务 ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://github.com/open-horizon/examples/tree/v2.27/edge/services/hello-operator#-using-the-operator-example-edge-service-with-deployment-policy)。
