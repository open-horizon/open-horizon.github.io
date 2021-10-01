---

copyright:
years: 2020
lastupdated: "2020-03-30"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 使用回滚更新边缘服务
{: #service_rollback}

边缘节点上的服务通常执行关键功能，因此在向许多边缘节点推出边缘服务的新版本时，监视部署是否成功是非常重要，如果在任何边缘节点上失败了，请将此节点还原为边缘服务的先前版本。 {{site.data.keyword.edge_notm}} 可自动执行此操作。 在模式或部署策略中，您可以定义在新服务版本失败时应使用哪些先前服务版本。

以下内容提供了有关如何推出现有边缘服务的新版本的更多详细信息，以及在模式和部署策略中更新回滚设置的软件开发最佳实践。

## 创建新的边缘服务定义
{: #creating_edge_service_definition}

如[使用 {{site.data.keyword.edge_notm}} 开发边缘服务](../developing/developing.md)和[开发详细信息](../developing/developing_details.md)部分中所述，发行边缘服务的新版本的主要步骤是：

- 根据需要为新版本编辑边缘服务代码。
- 在 **hzn.json** 配置文件中编辑服务版本变量中代码的语义版本号。
- 重新构建服务容器。
- 签署新边缘服务版本并将其发布到 Horizon exchange。

## 更新模式或部署策略中的回滚设置
{: #updating_rollback_settings}

新边缘服务在服务定义的 `version` 字段中指定其版本号。

模式和部署策略确定将哪些服务部署到哪些边缘节点。 要使用边缘服务回滚功能，您需要在模式或部署策略配置文件中的 **serviceVersions** 部分中添加新服务版本号的引用。

在将边缘服务部署到边缘节点作为模式或策略的结果时，代理程序部署具有最高优先级值的服务版本。

例如：

```json
 "serviceVersions": 
[
 {
   "version": "2.3.1",
   "priority": {
    "priority_value": 2,
    "retries": 1,
    "retry_durations": 1800
   }
 },
      {
        "version": "1.0.0",
   "priority": {
    "priority_value": 6,
    "retries": 1,
    "retry_durations": 2400
   }
  },
      {
        "version": "2.3.0",
   "priority": {
    "priority_value": 4,
    "retries": 1,
    "retry_durations": 3600
   }
  }
]
```
{: codeblock}

其他变量在优先级部分中提供。`priority_value` 属性设置首先尝试的服务版本的顺序，实际上就是说数字越小优先级越高。 `retries` 变量值定义在回滚到下一个最高优先级版本前，Horizon 在 `retry_durations` 指定的时间范围内将尝试启动此服务版本的次数。`retry_durations` 变量定义具体时间间隔（以秒为单位）。 例如，在一个月时间内服务失败 3 次可能无法保证将服务回滚到较低版本，但是在 5 分钟内失败 3 次则可能表示新服务版本有问题。

然后，重新发布部署模式或使用 Horizon Exchange 中 **serviceVersion** 部分的更改来更新部署策略。

请注意，您还可以使用 CLI `deploycheck` 命令来验证部署策略或模式设置更新的兼容性。 要查看更多详细信息，请发出以下命令：

```bash
hzn deploycheck -h
```
{: codeblock}

{{site.data.keyword.ieam}} agbot 快速检测部署模式或部署策略更改。 然后，agbot 联系其边缘节点已注册以运行部署模式或与更新的部署策略兼容的每个代理程序。 Agbot 和代理程序进行协调以下载新容器、停止和移除旧容器，并启动新容器。

因此，已注册以运行更新的部署模式或与部署策略兼容的边缘节点快速运行具有最高优先级值的新边缘服务版本，而不考虑边缘节点所在的地理位置。

## 查看正在推出的新服务版本的进度
{: #viewing_rollback_progress}

重复查询设备协议，直至填满 `agreement_finalized_time` 和 `agreement_execution_start_time` 字段： 

```bash
hzn agreement list
```
{: codeblock}

请注意，列出的协议显示与此服务相关联的版本，并且日期时间值出现在变量中（例如，"agreement_creation_time": "",）

此外，版本字段中填充具有最高优先级值的新的（且可运行的）服务版本：

```json
[
  {
    …
    "agreement_creation_time": "2020-04-01 11:55:08 -0600 MDT",
    "agreement_accepted_time": "2020-04-01 11:55:17 -0600 MDT",
    "agreement_finalized_time": "2020-04-01 11:55:18 -0600 MDT",
    "agreement_execution_start_time": "2020-04-01 11:55:20 -0600 MDT",
    "agreement_data_received_time": "",
    "agreement_protocol": "Basic",
    "workload_to_run": {
      "url": "ibm.helloworld",
      "org": "ibm",
      "version": "2.3.1",
      "arch": "amd64"
    }
  }
]
```
{: codeblock}

有关其他详细信息，您可以使用 CLI 命令检查当前节点的事件日志：

```bash
hzn eventlog list
```
{: codeblock}

最后，您还可以使用[管理控制台](../getting_started/accessing_ui.md)来修改回滚部署版本设置。您可以在创建新部署策略时执行此操作，或通过查看和编辑包含回滚设置的现有策略详细信息来执行。请注意，UI 的回滚部分中“时间范围”一词等同于 CLI 中的“retry_durations”。
