---

copyright:
years: 2019
lastupdated: "2019-11-12"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 脱机语音助手
{: #offline-voice-assistant}

脱机语音助手每分钟记录 5 秒钟的音频剪辑，在边缘设备本地将该音频剪辑转换为文本，然后指示主机执行命令并播放输出。 

## 准备工作
{: #before_beginning}

确保系统满足下列要求：

* 必须通过执行[准备边缘设备](../installing/adding_devices.md)中的步骤进行注册和注销。
* 在 Raspberry Pi 上安装 USB 声卡和麦克风。 

## 注册边缘设备
{: #reg_edge_device}

要在边缘节点上运行 `processtext` 服务示例，必须向 `IBM/pattern-ibm.processtext` 部署模式注册该边缘节点。 

执行自述文件的“Using the Offline Voice Assistant Example Edge Service with Deployment Pattern”[Using the Offline Voice Assistant Example Edge Service with Deployment Pattern ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://github.com/open-horizon/examples/tree/master/edge/services/processtext#-using-the-offline-voice-assistant-example-edge-service-with-deployment-pattern) 部分中的步骤。

## 其他信息
{: #additional_info}

`processtext` 示例源代码也以 {{site.data.keyword.edge_notm}} 开发示例的形式在 Horizon GitHub 存储库中提供。 这些源代码包括在本示例的边缘节点上运行的全部服务的代码。 

这些 [Open Horizon 示例 ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://github.com/open-horizon/examples/tree/master/edge/services/voice2audio) 服务包括：

* [voice2audio ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://github.com/open-horizon/examples/tree/master/edge/services/voice2audio) 服务记录 5 秒钟的音频剪辑，并将其发布到 mqtt 代理。
* [audio2text ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://github.com/open-horizon/examples/tree/master/edge/services/audio2text) 服务使用该音频剪辑，并使用 pocket sphinx 将其脱机转换为文本。
* [processtext ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://github.com/open-horizon/examples/tree/master/edge/services/processtext) 服务使用该文本，并尝试执行记录的命令。
* [text2speech ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://github.com/open-horizon/examples/tree/master/edge/services/text2speech) 服务通过扬声器播放该命令的输出。
* [mqtt_broker ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://github.com/open-horizon/examples/tree/master/edge/services/mqtt_broker) 管理所有容器间通信。

## 后续操作
{: #what_next}

有关构建和发布自己版本的 Watson Speech to Text 的指示信息，请参阅 [Open Horizon 示例 ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://github.com/open-horizon/examples/blob/master/edge/services/processtext/CreateService.md#-building-and-publishing-your-own-version-of-the-offline-voice-assistant-edge-service) 存储库中的 `processtext` 目录步骤。 
