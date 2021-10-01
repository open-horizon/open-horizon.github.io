---

copyright:
years: 2019
lastupdated: "2020-2-25"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Watson Speech to Text
{: #watson-speech}

此服务侦听单词 Watson。 检测到该单词时，此服务就会捕获音频剪辑，并将其发送到 Speech to Text 实例。  停止词会移除（可选），转录文本会发送到 {{site.data.keyword.event_streams}}。

## 准备工作

确保系统满足下列要求：

* 必须通过执行[准备边缘设备](adding_devices.md)中的步骤进行注册和注销。
* 在 Raspberry Pi 上安装 USB 声卡和麦克风。 

此服务需要 {{site.data.keyword.event_streams}} 实例和 IBM Speech to Text 才能正常运行。 有关如何部署事件流实例的指示信息，请参阅[主机 CPU 负载百分比示例 (cpu2evtstreams)](../using_edge_services/cpu_load_example.md)。  

确保设置必需的 {{site.data.keyword.event_streams}} 环境变量：

```
echo "$EVTSTREAMS_API_KEY, $EVTSTREAMS_BROKER_URL"
```
{: codeblock}

在缺省情况下，此样本所用的事件流主题为 `myeventstreams`，但您可以通过设置以下环境变量来使用任何主题：

```
export EVTSTREAMS_TOPIC=<your-topic-name>
```
{: codeblock}

## 部署 IBM Speech to Text 实例
{: #deploy_watson}

如果当前已部署实例，请获取访问信息并设置环境变量，或者执行以下步骤：

1. 浏览至 IBM Cloud。
2. 单击**创建资源**。
3. 在搜索框中输入 `Speech to Text`。
4. 选择 `Speech to Text` 磁贴。
5. 选择区域，选择定价计划，输入服务名称，然后单击**创建**以供应该实例。
6. 供应完成后，请单击该实例并记下凭证 API 密钥和 URL，然后将它们导出为下列环境变量：

    ```
    export STT_IAM_APIKEY=<speech-to-text-api-key>
    export STT_URL=<speech-to-text-url>
    ```
    {: codeblock}

7. 转至“入门”部分，以获取有关如何测试 Speech to Text 服务的指示信息。

## 注册边缘设备
{: #watson_reg}

要在边缘节点上运行 watsons2text 服务示例，必须向 `IBM/pattern-ibm.watsons2text-arm` 部署模式注册该边缘节点。 请执行自述文件的 [Using Watson Speech to Text to IBM Event Streams Service with Deployment Pattern![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://github.com/open-horizon/examples/tree/master/edge/evtstreams/watson_speech2text#-using-the-ibm-watson-speech-to-text-to-ibm-event-streams-service-with-deployment-pattern) 部分中的步骤。

## 其他信息

`processtect` 示例源代码也以 {{site.data.keyword.edge_notm}} 开发示例的形式在 Horizon GitHub 存储库中提供。 这些源代码包括在本示例的边缘节点上运行的全部四个服务的代码。 

这些服务包括：

* [hotworddetect ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://github.com/open-horizon/examples/tree/master/edge/services/hotword_detection) 服务侦听并检测热词 Watson，然后记录音频剪辑并将其发布到 mqtt 代理。
* [watsons2text ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://github.com/open-horizon/examples/tree/master/edge/evtstreams/watson_speech2text) 服务接收音频剪辑并将其发送到 IBM Speech to Text 服务，然后将解码文本发布到 mqtt 代理。
* [stopwordremoval ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://github.com/open-horizon/examples/tree/master/edge/services/stopword_removal) 服务以 WSGI 服务器形式运行，它接收 JSON 对象，例如 {"text": "how are you today"}，然后移除常用停止词并返回 {"result": "how you today"}。
* [mqtt2kafka ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://github.com/open-horizon/examples/tree/master/edge/services/mqtt2kafka) 服务在其预订的 mqtt 主题上收到内容时，将数据发布到 {{site.data.keyword.event_streams}}。
* [mqtt_broker ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://github.com/open-horizon/examples/tree/master/edge/services/mqtt_broker) 负责所有容器间通信。

## 后续操作

* 有关构建和发布您自己的“脱机语音助手边缘服务”版本的指示信息，请参阅[脱机语音助手边缘服务 ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://github.com/open-horizon/examples/blob/master/edge/evtstreams/watson_speech2text/CreateService.md#-building-and-publishing-your-own-version-of-the-watson-speech-to-text-to-ibm-event-streams-service)。 请完成 Open Horizon 示例存储库的 `watson_speech2text` 目录中的步骤。

* 请参阅 [Open Horizon 示例存储库 ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://github.com/open-horizon/examples)。
