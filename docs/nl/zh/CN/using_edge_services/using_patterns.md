---

copyright:
  years: 2020
lastupdated: "2020-05-10"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 使用模式
{: #using_patterns}

通常，开发者在 Horizon Exchange 中发布边缘服务后，可以将服务部署模式发布到 {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) 中心。

hzn CLI 提供了在 {{site.data.keyword.horizon_exchange}} 中列出和管理模式的功能，包括用于列出、发布、验证、更新和移除服务部署模式的命令。 它还提供了一种方法，用于列出和移除与特定部署模式关联的密钥。

要获取 CLI 命令和更多详细信息的完整列表：

```
hzn exchange pattern -h
```
{: codeblock}

## 示例

在 {{site.data.keyword.horizon_exchange}} 中签署并创建（或更新）模式资源：

```
hzn exchange pattern publish --json-file=JSON-FILE [<flags>]
```
{: codeblock}

## 使用部署模式

使用部署模式，可以简单、方便地将服务部署到边缘节点。 指定要部署到边缘节点的一个或多个顶级服务，{{site.data.keyword.ieam}} 处理其余服务，包括部署顶级服务可能具有的任何从属服务。

创建并向 {{site.data.keyword.ieam}} Exchange 添加服务后，需要创建 `pattern.json` 文件，类似于：

```
{
  "IBM/pattern-ibm.cpu2evtstreams": {
    "owner": "root/root",
    "label": "Edge ibm.cpu2evtstreams Service Pattern for arm architectures",
    "description": "Pattern for ibm.cpu2evtstreams sending cpu and gps info to the IBM Event Streams",
    "public": true,
    "services": [
      {
        "serviceUrl": "ibm.cpu2evtstreams",
      "serviceOrgid": "IBM",
      "serviceArch": "arm",
      "serviceVersions": [
        {
            "version": "1.4.3",
            "priority": {},
            "upgradePolicy": {}
          }
        ],
        "dataVerification": {
          "metering": {}
        },
        "nodeHealth": {
          "missing_heartbeat_interval": 1800,
          "check_agreement_status": 1800
        }
      }
    ],
    "agreementProtocols": [
      {
        "name": "Basic"
      }
    ],
    "lastUpdated": "2020-10-24T14:46:44.341Z[UTC]"
  }
}
```
{: codeblock}

此代码是用于 `arm` 设备的 `ibm.cpu2evtstreams` 服务的 `pattern.json` 文件示例。 如此处所示，不需要指定 `cpu_percent` 和 `gps`（`cpu2evtstreams` 的从属服务）。 该任务由 `service_definition.json` 文件处理，因此成功注册的边缘节点会自动运行这些工作负载。

使用 `pattern.json` 文件，可在 `serviceVersions` 部分中定制回滚设置。 您可以指定多个较旧版本的服务，并为每个版本提供边缘节点的优先级，以在新版本发生错误的情况下回滚。 除了将优先级分配到每个回滚版本，您可以在退回到指定服务的较低优先级版本前指定重新尝试次数和持续时间之类的内容。

您还可以通过将服务包括在 `userInput` 部分底部附近，来设置在发布部署模式时确保服务正确地集中运行所需的任何配置变量。 发布 `ibm.cpu2evtstreams` 服务时，会为其传递发布数据到 IBM Event Streams 所需的凭证，可通过以下命令完成：

```
hzn exchange pattern publish -f pattern.json
```
{: codeblock}

发布模式后，您可以向其注册一个 arm 设备：

```
hzn register -p pattern-ibm.cpu2evtstreams-arm
```
{: codeblock}

此命令将 `ibm.cpu2evtstreams` 和任何从属服务部署到节点。

注：`userInput.json` 文件不会传递到上述 `hzn register` 命令，就像您在执行 [Using the CPU To IBM Event Streams Edge Service with Deployment Pattern ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://github.com/open-horizon/examples/tree/master/edge/evtstreams/cpu2evtstreams#-using-the-cpu-to-ibm-event-streams-edge-service-with-deployment-pattern) 存储库示例中的步骤时那样。 由于用户输入已随模式本身传递，因此任何自动注册的边缘节点都可访问这些环境变量。

通过注销可以停止所有 `ibm.cpu2evtstreams` 工作负载：

```
hzn unregister -fD
```
{: codeblock}
