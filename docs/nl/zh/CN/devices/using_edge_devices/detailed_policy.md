---

copyright:
years: 2019, 2020
lastupdated: "2020-01-22"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 部署边缘服务
{: #detailed_deployment_policy}

您可以使用策略或模式来部署 {{site.data.keyword.edge_notm}} {{site.data.keyword.ieam}} 策略。 有关各种系统组件的更全面的概述，请参阅 [{{site.data.keyword.edge}} 概述](../../getting_started/overview_ieam.md)和[部署策略用例](policy_user_cases.md)。有关实践策略示例，请参阅[边缘服务的 CI-CD 流程](../developing/cicd_process.md)。

注：您还可以从管理控制台创建和管理部署策略或模式。 请参阅[使用管理控制台](../getting_started/accessing_ui.md)。

此部分讨论策略和模式概念并包含用例场景。

由于管理员无法同时管理数以千计的边缘节点，因此向上扩展至数万或以上不切实际。 要实现此级别的扩展，{{site.data.keyword.edge_devices_notm}} 使用策略来确定自动部署服务和机器学习模型的位置和时间。 

策略通过应用于模型、节点、服务和部署策略的灵活策略语言来表示。 策略语言定义属性（称为 `properties`）并声明特定需求（称为 `constraints`）。 这允许系统的每个部分向 {{site.data.keyword.edge_devices_notm}} 部署引擎提供输入。 在可部署服务之前，将检查模型、节点、服务和部署策略约束，以确保满足所有需求。

由于节点（部署了服务）可以表示需求，因此 {{site.data.keyword.edge_devices_notm}} 策略被描述为双向策略系统。 节点在 {{site.data.keyword.edge_devices_notm}} 策略部署系统中不是从属项。 因此，策略提供比模式更精细的服务和模型部署控制。 使用策略时，{{site.data.keyword.edge_devices_notm}} 搜索可部署给定服务的节点，并分析现有节点以确保它们保持兼容性（在策略中）。 如果最初部署服务的节点、服务和部署策略仍然有效，或者对其中一个策略所作的更改不影响策略兼容性，节点将处于策略中。 使用策略提供了更大的问题分离，使边缘节点所有者、服务开发者和业务所有者可以独立阐明其策略。

策略是部署模式的替代方法。 当开发者在 Horizon Exchange 中发布边缘服务后，您可以将模式发布到 {{site.data.keyword.ieam}} 中心。 hzn CLI 提供了在 Horizon Exchange 中列出和管理模式的功能，包括用于列出、发布、验证、更新和移除服务部署模式的命令。 它还提供了一种方法，用于列出和移除与特定部署模式关联的密钥。

* [部署策略用例](policy_user_cases.md)
* [使用模式](using_patterns.md)
