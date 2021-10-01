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

# 为集群创建您自己的 Hello world
{: #creating_hello_world}

要将容器化边缘服务部署到边缘集群，第一步是构建在 Kubernetes 集群中部署容器化边缘服务的 Kubernetes 操作程序。

使用此示例来了解如何：

* 使用 `operator-sdk` 创建 Ansible 操作程序
* 使用操作程序以将服务部署到边缘集群
* 在边缘集群上公开可使用 `curl` 命令在外部进行访问的端口

请参阅[创建自己的操作程序边缘服务![在新的标签页中打开](../images/icons/launch-glyph.svg "在新的标签页中打开")](https://github.com/open-horizon/examples/blob/v2.27/edge/services/hello-operator/CreateService.md#creating-your-own-operator-edge-service)。

要运行已发布的 `hello-operator` 服务，请参阅[使用含有部署策略的操作程序示例边缘服务![在新的标签页中打开](../images/icons/launch-glyph.svg "在新的标签页中打开")](https://github.com/open-horizon/examples/tree/v2.27/edge/services/hello-operator#-using-the-operator-example-edge-service-with-deployment-policy)。
