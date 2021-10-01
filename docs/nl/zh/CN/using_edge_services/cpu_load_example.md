---

copyright:
years: 2020
lastupdated: "2020-02-06"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# CPU 使用量到 {{site.data.keyword.message_hub_notm}}
{: #cpu_load_ex}

主机 CPU 负载百分比是使用 CPU 负载百分比数据并通过 IBM Event Streams 提供数据的部署模式示例。

此边缘服务反复查询边缘设备 CPU 负载，并将生成的数据发送到 [IBM Event Streams ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://www.ibm.com/cloud/event-streams)。 该边缘服务可以在任何边缘节点上运行，因为它不需要专门的传感器硬件。

在执行此任务之前，通过执行[在边缘设备上安装 Horizon 代理程序](../installing/registration.md)中的步骤，进行注册和注销

为获取更现实场景的体验，此 cpu2evtstreams 示例阐述典型边缘服务的更多方面，包括：

* 查询动态边缘设备数据
* 分析边缘设备数据（例如，`cpu2evtstreams` 计算 CPU 负载的窗口平均值）
* 将已处理的数据发送到中心数据采集服务
* 自动获取事件流凭证以安全地认证数据传输

## 准备工作
{: #deploy_instance}

在部署 cpu2evtstreams 边缘服务之前，您需要在云中运行的 {{site.data.keyword.message_hub_notm}} 实例以接收其数据。 组织的每个成员都可以共享一个 {{site.data.keyword.message_hub_notm}} 实例。 如果已部署实例，那么获取访问权信息并设置环境变量。

### 在 {{site.data.keyword.cloud_notm}} 中部署 {{site.data.keyword.message_hub_notm}}
{: #deploy_in_cloud}

1. 浏览至 {{site.data.keyword.cloud_notm}}。

2. 单击**创建资源**。

3. 在搜索框中输入 `Event Streams`。

4. 选择 **Event Streams** 磁贴。

5. 在 **Event Streams** 中，输入服务名称，选择区域，选择定价计划，然后单击**创建**以供应实例。

6. 在供应完成后，单击实例。

7. 要创建主题，请单击 + 图标，然后将实例命名为 `cpu2evtstreams`。

8. 您可以在终端中创建凭证，或者获取凭证（如果已创建）。 要创建凭证，请单击**服务凭证 > 新建凭证**。 使用格式与以下代码块类似的新凭证，创建名为 `event-streams.cfg` 的文件。 虽然只需要创建这些凭证一次，但请保存此文件以供您自己或可能需要 {{site.data.keyword.event_streams}} 访问权的其他团队成员未来使用。

   ```
   EVTSTREAMS_API_KEY="<the value of api_key>"
   EVTSTREAMS_BROKER_URL="<all kafka_brokers_sasl values in a single string, separated by commas>"
   ```
   {: codeblock}
        
   例如，从“查看凭证”窗格：

   ```
   EVTSTREAMS_BROKER_URL=broker-4-x7ztkttrm44911kc.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-3-  x7ztkttrm44911kc.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-2-x7ztkttrm44911kc.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-0-x7ztkttrm44911kc.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-1-x7ztkttrm44911kc.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-5-x7ztkttrm44911kc.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093
   ```
   {: codeblock}

9. 创建 `event-streams.cfg` 后，在 shell 中设置以下环境变量：

   ```
   eval export $(cat event-streams.cfg)
   ```
   {: codeblock}

### 在 {{site.data.keyword.cloud_notm}} 中测试 {{site.data.keyword.message_hub_notm}}
{: #testing}

1. 安装 `kafkacat` (https://linuxhostsupport.com/blog/how-to-install-apache-kafka-on-ubuntu-16-04/)。

2. 在终端上，输入以下命令以预订 `cpu2evtstreams` 主题：

    ```
    kafkacat -C -q -o end -f "%t/%p/%o/%k: %s\n" -b $EVTSTREAMS_BROKER_URL -X api.version.request=true -X security.protocol=sasl_ssl -X sasl.mechanisms=PLAIN -X sasl.username=token -X sasl.password=$EVTSTREAMS_API_KEY -t cpu2evtstreams
    ```
    {: codeblock}

3. 在另一个终端上，将测试内容发布到 `cpu2evtstreams` 主题以在原始控制台上显示。 例如：

    ```
    echo 'hi there' | kafkacat -P -b $EVTSTREAMS_BROKER_URL -X api.version.request=true -X security.protocol=sasl_ssl -X sasl.mechanisms=PLAIN -X sasl.username=token -X sasl.password=$EVTSTREAMS_API_KEY -t cpu2evtstreams
    ```
    {: codeblock}

## 注册边缘设备
{: #reg_device}

要在边缘节点上运行 cpu2evtstreams 服务示例，必须向 `IBM/pattern-ibm.cpu2evtstreams` 部署模式注册边缘节点。 执行 [Horizon CPU To {{site.data.keyword.message_hub_notm}} ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://github.com/open-horizon/examples/blob/master/edge/evtstreams/cpu2evtstreams/README.md) 的**第一**部分中的步骤。

## 其他信息
{: #add_info}

CPU 示例源代码位于 [{{site.data.keyword.horizon_open}} 示例存储库 ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://github.com/open-horizon/examples) 中，作为 {{site.data.keyword.edge_notm}} 边缘服务开发的示例。 此源包含在此示例的边缘节点上运行的所有三个服务的代码：

  * cpu 服务，它作为本地专用 Docker 网络上的 REST 服务，提供 CPU 负载百分比数据。 有关更多信息，请参阅 [Horizon CPU Percent Service![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://github.com/open-horizon/examples/tree/master/edge/services/cpu_percent)。
  * gps 服务，它提供来自 GPS 硬件（如果有）或者从边缘节点 IP 地址估算的位置的位置信息。 位置数据以本地专用 Docker 网络上的 REST 服务形式提供。 有关更多信息，请参阅 [Horizon GPS Service![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://github.com/open-horizon/examples/tree/master/edge/services/gps)。
  * cpu2evtstreams 服务，它使用另外两个服务所提供的 REST API。 此服务将组合后的数据发送给云中的 {{site.data.keyword.message_hub_notm}} kafka 代理。 有关此服务的更多信息，请参阅 [{{site.data.keyword.horizon}} CPU To {{site.data.keyword.message_hub_notm}} Service![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://github.com/open-horizon/examples/blob/master/edge/evtstreams/cpu2evtstreams/cpu2evtstreams.md)。
  * 有关 {{site.data.keyword.message_hub_notm}} 的更多信息，请参阅[Event Streams - 概述 ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://www.ibm.com/cloud/event-streams?mhsrc=ibmsearch_a&mhq=event%20streams)。

## 后续操作
{: #cpu_next}

如果您想将自己的软件部署到边缘节点，必须创建自己的边缘服务以及关联的部署模式或部署策略。 有关更多信息，请参阅[使用 {{site.data.keyword.edge_notm}} 开发边缘服务](../developing/developing.md)。
