---

copyright:
years: 2020
lastupdated: "2020-04-27"

---

{:shortdesc: .shortdesc}
{:new_window: target="_blank"}
{:codeblock: .codeblock}
{:pre: .pre}
{:screen: .screen}
{:tip: .tip}
{:download: .download}

# 开发 Kubernetes 操作程序
{: #kubernetes_operator}

通常，开发要在边缘集群中运行的服务与开发在边缘设备上运行的边缘服务相似。边缘服务使用[边缘本机开发最佳实践](best_practices.md)开发进行开发，并打包在容器中。 差别在于部署边缘服务的方式。

要将容器化边缘服务部署到边缘集群，开发人员必须先构建在 Kubernetes 集群中部署容器化边缘服务的 Kubernetes 操作程序。 在编写并测试此操作程序后，开发人员创建此操作程序并将其作为 {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) 服务进行发布。 此流程使 {{site.data.keyword.ieam}} 管理员能够像部署任何 {{site.data.keyword.ieam}} 服务一样使用策略或模式来部署操作程序服务。 不需要为边缘服务创建 {{site.data.keyword.ieam}} 服务定义。 当 {{site.data.keyword.ieam}} 管理员部署操作程序服务时，操作程序部署边缘服务。

在编写 Kubernetes 操作程序时，有多个选项可用。 首先，阅读 [Kubernetes 概念 - 操作程序模式 ![在新选项卡中打开](../../images/icons/launch-glyph.svg "在新选项卡中打开")](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/)。 此站点是了解操作程序的好资源。 在熟悉操作程序概念后，通过使用[操作程序框架 ![在新的选项卡中打开](../../images/icons/launch-glyph.svg "在新的选项卡中打开")](https://github.com/operator-framework/getting-started) 来完成操作程序编写。 此文章提供了关于什么是操作程序的更多详细信息并展示了创建简单操作程序和使用操作程序软件开发包 (SDK) 的过程。

## 为 {{site.data.keyword.ieam}} 开发操作程序时的注意事项

最佳做法是自由使用操作程序的状态功能，因为 {{site.data.keyword.ieam}} 将操作程序创建的任何状态都报告到 {{site.data.keyword.ieam}} 管理中心。 编写操作程序时，操作程序框架为此操作程序生成 Kubernetes 定制资源定义 (CRD)。 每个操作程序 CRD 都具有状态对象，此对象应填充操作程序及其要部署的边缘服务的状态的相关重要状态信息。 此操作不是 Kubernetes 自动完成的；它需要由操作程序开发人员写入到操作程序实施。 边缘集群中的 {{site.data.keyword.ieam}} 代理程序定期收集操作程序状态并将其报告到管理中心。

如果需要，操作程序可以将特定于服务的 {{site.data.keyword.ieam}} 环境变量附加到它启动的任何服务。启动操作程序后，{{site.data.keyword.ieam}} 代理程序创建名为 `hzn-env-vars` 且包含特定于服务的环境变量的 Kubernetes 配置图。（可选）操作程序可将配置图附加到它创建的任何部署，这样将使它启动的服务能够识别相同的特定服务的环境变量。 这些是插入到在边缘设备上运行的服务的相同环境变量。 唯一的例外是 ESS* 环境变量，因为边缘集群服务尚不支持模型管理系统 (MMS)。

如果需要，由 {{site.data.keyword.ieam}} 部署的操作程序可以部署到除缺省名称以外的名称空间。 操作程序开发人员通过修改操作程序 yaml 文件以指向此名称空间来完成此操作。 有两种方法可完成此操作：

 * 修改操作程序的部署定义（通常名为 **./deploy/operator.yaml**）以指定名称空间

或者

* 在操作程序的 yaml 定义文件中包含名称空间定义 yaml 文件；例如，在操作程序项目的 **./deploy** 目录中。

注：将操作系统部署到非缺省名称空间时，如果此名称空间不存在，{{site.data.keyword.ieam}} 创建此名称空间并在 {{site.data.keyword.ieam}} 取消部署此操作程序时将其移除。

## 为 {{site.data.keyword.ieam}} 编写操作程序

编写并测试操作程序后，需要将其打包以供 {{site.data.keyword.ieam}} 部署：

1. 确保此操作程序已打包以作为部署在集群中运行。这表示此操作程序已构建为容器并在 {{site.data.keyword.ieam}} 部署时推送到从中检索该容器的容器注册表中。通常，通过使用后跟 **docker push** 的命令 **operator-sdk build** 构建操作程序来完成。 这在[操作程序框架 ![在新选项卡中打开](../../images/icons/launch-glyph.svg "在新选项卡中打开")](https://github.com/operator-framework/getting-started#1-run-as-a-deployment-inside-the-cluster) 中进行了描述。

2. 确保由操作程序部署的服务容器还推送到操作程序将从中部署容器的注册表中。

3. 创建包含来自操作系统项目的操作系统 yaml 定义文件的归档：

   ```bash
   cd <operator-project>/<operator-name>/deploy
    tar -zcvf <archive-name>.tar.gz
   ```
   {: codeblock}

4. 使用 {{site.data.keyword.ieam}} 服务创建工具为操作系统服务创建服务定义，例如，按照以下步骤：

   1. 创建新项目：

      ```bash
      hzn dev service new -V <a version> -s <a service name> -c cluster
      ```
      {: codeblock}

   2. 编辑 **horizon/service.definition.json** 文件以指向步骤 3 中创建的操作程序 yaml 归档。

   3. 创建或使用已存在的服务签名密钥。

   4. 发布服务

      ```
      hzn exchange service publish -k <signing key> -f ./horizon/service.definition.json
      ```
      {: codeblock}

5. 创建部署策略或模式以将操作程序服务部署到边缘集群。
