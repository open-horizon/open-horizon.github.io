---

copyright:
  years: 2019, 2020
lastupdated: "2020-2-06"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Hello World
{: #policy}

{{site.data.keyword.edge_devices_notm}} 使用策略来建立和管理服务和模型部署，这为管理员提供了处理大量边缘节点所需的灵活性和可伸缩性。 {{site.data.keyword.edge_devices_notm}} 策略是部署模式的替代方法。 它提供了更大的问题分离，使边缘节点所有者、服务代码开发者和业务所有者可以独立阐明策略。

这是最小化的“Hello, world”示例，向您介绍 {{site.data.keyword.edge_devices_notm}} 部署策略。

Horizon 策略类型：

* 节点策略（由节点所有者在注册时提供）
* 服务策略（可应用于 Exchange 中已发布的服务）
* 部署策略（有时也称为业务策略，大致对应于部署模式）

策略为在边缘节点上的 Horizon 代理程序与 Horizon AgBot 之间定义协议提供更多控制权。

## 使用策略来运行 Hello world 样本
{: #helloworld_policy}

请参阅 [Using the Hello World Example Edge Service with Deployment Policy ![在新选项卡中打开](../../images/icons/launch-glyph.svg "在新选项卡中打开")](https://github.com/open-horizon/examples/blob/master/edge/services/helloworld/PolicyRegister.md#using-the-hello-world-example-edge-service-with-deployment-policy)。

## 相关信息

* [部署边缘服务](../using_edge_devices/detailed_policy.md)
* [部署策略用例](../using_edge_devices/policy_user_cases.md)
