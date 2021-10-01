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

通常，开发要在边缘集群中运行的服务与开发在边缘设备上运行的边缘服务相似，但区别在于边缘服务的部署方式。要将容器化边缘服务部署到边缘集群，开发人员必须先构建在 Kubernetes 集群中部署容器化边缘服务的 Kubernetes 操作程序。 在编写并测试此操作程序后，开发者创建此操作程序并将其作为 IBM Edge Application Manager (IEAM) 服务进行发布。此流程使 IEAM 管理员能够像部署任何 IEAM 服务一样使用策略或模式来部署操作程序服务。

要通过部署策略使用已在 IEAM Exchange 中发布的 `ibm.operator` 服务在集群上运行 `helloworld` 容器化服务，请参阅 [Horizon Operator Example Edge Service ![在新选项卡中打开](../../images/icons/launch-glyph.svg "在新选项卡中打开")](https://github.com/open-horizon/examples/tree/master/edge/services/operator#horizon-operator-example-edge-service)。
