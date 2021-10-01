---

copyright:
years: 2019
lastupdated: "2019-07-04"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 部署模式示例
{: #deploy_pattern_ex}

为帮助您进一步了解 {{site.data.keyword.edge_devices_notm}} 部署模式入门信息，您可以装入示例程序以作为部署模式。
{:shortdesc}

请尝试注册其中每个预先构建的部署模式示例，以进一步了解如何使用部署模式。

要为以下任何部署模式示例注册边缘节点，必须先移除边缘节点的任何现有部署模式注册。 在边缘节点上运行以下命令，即可移除任何部署模式注册：
```
 hzn unregister
 hzn node list | jq .configstate.state
```
{: codeblock}

输出示例：
```
"unconfigured"
```
{: codeblock}

如果命令输出显示 `"unconfiguring"` 而不是 `"unconfigured"`，请稍候几分钟，然后重新运行该命令。 通常此命令只需几秒即可完成。 请重试该命令，直到输出显示 `"unconfigured"` 为止。

## 示例
{: #pattern_examples}

* [Hello, world ![在新选项卡中打开](../../images/icons/launch-glyph.svg "在新选项卡中打开")](https://github.com/open-horizon/examples/blob/master/edge/services/helloworld) 最小化的 `"Hello, world."` 示例介绍 {{site.data.keyword.edge_devices_notm}} 部署模式。

* [主机 CPU 负载百分比](cpu_load_example.md) 这个部署模式示例使用 CPU 负载百分比数据，并通过 {{site.data.keyword.message_hub_notm}} 提供该数据。

* [软件定义的无线电](software_defined_radio_ex.md) 这个功能齐全的示例使用无线电台音频，提取语音，并将提取的语音转换为文本。 此示例对该文本完成情感分析，通过用户界面提供数据和结果，在该界面中，您可以查看每个边缘节点的数据详细信息。 使用此示例可进一步了解边缘处理。
