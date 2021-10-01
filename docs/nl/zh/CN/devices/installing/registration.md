---

copyright:
years: 2020
lastupdated: "2020-02-03"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 安装代理程序
{: #registration}

在边缘设备上安装 {{site.data.keyword.horizon}} 代理程序软件时，可以向 {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) 注册该边缘设备，以将该设备添加到边缘计算管理域中并运行边缘服务。
{:shortdesc}

Helloworld 是一个极简示例，用于向您介绍 {{site.data.keyword.ieam}} 边缘服务和部署模式。

## 准备工作
{: #before_begin}

您必须完成[准备边缘设备](adding_devices.md)中的步骤。

## 安装和注册边缘设备
{: #installing_registering}

提供了四种不同的方法来安装代理程序和注册边缘设备，每种方法用于不同的情况：

* [自动代理程序安装和注册](automated_install.md) - 通过最少的步骤安装并注册一个边缘设备。**用户首次执行此操作时，建议使用此方法。**
* [高级手动代理程序安装和注册](advanced_man_install.md) - 自行执行每个步骤以安装并注册一个边缘设备。如果需要执行某些特殊操作，并且方法 1 中使用的脚本不具备所需的灵活性，请使用此方法。如果要准确了解设置边缘设备所需的内容，也可以使用此方法。
* [批量代理程序安装和注册](many_install.md#batch-install) - 一次安装并注册许多边缘设备。
* [SDO 代理程序安装和注册](sdo.md) - 使用 SDO 设备自动安装。

## 问题与故障诊断
{: #questions_ts}

如果您对任何这些步骤有任何困难，请查看提供的故障诊断和常见问题主题。 有关更多信息，请参阅：
  * [故障诊断](../troubleshoot/troubleshooting.md)
  * [常见问题](../getting_started/faq.md)
