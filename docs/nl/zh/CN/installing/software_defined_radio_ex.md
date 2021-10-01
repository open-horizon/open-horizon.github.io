---

copyright:
years: 2020
lastupdated: "2020-02-5" 

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 软件定义的无线电边缘处理
{: #defined_radio_ex}

本示例使用软件定义的无线电 (SDR) 作为边缘处理示例。 利用 SDR，可以将完整无线电频谱内的原始数据发送到云服务器进行处理。 边缘节点在本地处理数据，然后将较少量的更高价值数据发送到云处理服务以进行额外处理。
{:shortdesc}

此图显示此 SDR 示例的体系结构：

<img src="../images/edge/08_sdrarch.svg" style="margin: 3%" alt="示例体系结构">

SDR 边缘处理是一个功能齐全的示例，它使用无线电台音频，提取语音，并将提取的语音转换为文本。 此示例对该文本完成情感分析，通过用户界面提供数据和结果，在该界面中，您可以查看每个边缘节点的数据详细信息。 使用此示例可进一步了解边缘处理。

SDR 通过使用计算机 CPU 中的数字电路来接收无线电信号，以处理需要一组专用模拟电路的工作。 该模拟电路通常受到它所能接收的无线电频谱宽度的限制。 例如，为接收 FM 广播电台而构建的模拟无线电接收器，无法接收来自无线电频谱上任何其他位置的无线电信号。 SDR 可以访问大部分频谱。 如果没有 SDR 硬件，您可以使用模拟数据。 使用模拟数据时，来自因特网流的音频被视为通过 FM 广播，并在边缘节点上接收。

执行此任务之前，请通过执行[安装代理程序](registration.md)中的步骤来注册和注销边缘设备。

此代码包含以下主要组件。

|组件|描述|
|---------|-----------|
|[sdr 服务 ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://github.com/open-horizon/examples/tree/master/edge/services/sdr)|较低级别的服务访问边缘节点上的硬件。|
|[ssdr2evtstreams 服务 ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://github.com/open-horizon/examples/tree/master/edge/evtstreams/sdr2evtstreams)|较高级别的服务从较低级别的 sdr 服务接收数据并完成边缘节点上的数据的本地分析。 然后，sdr2evtstreams 服务将已处理的数据发送到云后端软件。|
|[云后端软件 ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://github.com/open-horizon/examples/tree/master/cloud/sdr)|云后端软件接收来自边缘节点的数据以进一步分析。 然后，后端实施可在基于 Web 的 UI 中呈现边缘节点图和更多内容。|
{: caption="表 1. 软件定义无线电到 {{site.data.keyword.message_hub_notm}} 主要组件" caption-side="top"}

## 注册设备

尽管通过在任何边缘设备上使用模拟数据可运行此服务，但如果要使用像带有 SDR 硬件的 Raspberry Pi 之类的边缘设备，请先配置内核模块以支持 SDR 硬件。 您必须手动配置此模块。 Docker 容器可以在其上下文中建立不同的 Linux 分布，但该容器无法安装内核模块。 

完成以下步骤以配置此模块：

1. 以 root 用户身份，创建名为 `/etc/modprobe.d/rtlsdr.conf` 文件。
   ```
   sudo nano /etc/modprobe.d/rtlsdr.conf
   ```
   {: codeblock}

2. 将下列各行添加到该文件中：
   ```
   blacklist rtl2830
     blacklist rtl2832
     blacklist dvb_usb_rtl28xxu
   ```
   {: codeblock}

3. 保存该文件，重新启动，然后继续操作：
   ```
   sudo reboot
   ```
   {: codeblock}   

4. 在您的环境中设置以下 {{site.data.keyword.message_hub_notm}} API 密钥。 创建此密钥是为了与本示例配合使用，并用于为 IBM 软件定义的无线电 UI 提供由边缘节点收集的已处理数据。
   ```
   export EVTSTREAMS_API_KEY=X2e8cSjbDAMk-ztJLaoi3uffy8qsQTnZttUjcHCfm7cp
    export EVTSTREAMS_BROKER_URL=broker-3-y420pyyyvhhmttz0.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-5-y420pyyyvhhmttz0.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-4-y420pyyyvhhmttz0.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-1-y420pyyyvhhmttz0.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-0-y420pyyyvhhmttz0.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-2-y420pyyyvhhmttz0.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093
   ```
   {: codeblock}

5. 要在边缘节点上运行 sdr2evtstreams 服务示例，必须向 IBM/pattern-ibm.sdr2evtstreams 部署模式注册边缘节点。 执行 [Preconditions for Using the SDR To IBM Event Streams Example Edge Service![在新的选项卡中打开](../images/icons/launch-glyph.svg "在新的选项卡中打开")](https://www.ibm.com/links?url=https%3A%2F%2Fgithub.com%2Fopen-horizon%2Fexamples%2Ftree%2Fmaster%2Fedge%2Fevtstreams%2Fsdr2evtstreams) 中的步骤。

6. 检查示例 Web UI，确定边缘节点是否在发送结果。 

## SDR 实现详细信息

### sdr 低级服务
{: #sdr}

此服务的软件堆栈的最低级别包含 `sdr` 服务实施。 此服务通过通过使用热门 `librtlsdr` 库和派生的 `rtl_fm` 与 `rtl_power` 实用程序以及 `rtl_rpcd` 守护程序来访问本地软件定义的无线电硬件。 有关 `librtlsdr` 库的更多信息，请参阅 [librtlsdr ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://github.com/librtlsdr/librtlsdr)。

`sdr` 服务直接控制软件定义的无线电硬件，以将硬件调整至特定频率来接收传输的数据，或者跨指定频谱测量信号强度。 该服务的典型工作流程可以是调整至特定频率以按该频率从电台接收数据。 然后，该服务可以处理收集的数据。

### sdr2evtstreams 高级服务
{: #sdr2evtstreams}

`sdr2evtstreams` 高级服务实施通过本地专用虚拟 Docker 网络使用 `sdr` 服务 REST API 和 `gps` 服务 REST API。 `sdr2evtstreams` 服务接收来自 `sdr` 服务的数据，并完成对数据的一些本地推论以选择最佳语音电台。 然后，`sdr2evtstreams` 服务使用 Kafka 来通过 {{site.data.keyword.message_hub_notm}} 将音频剪辑发布到云。

### IBM Functions
{: #ibm_functions}

IBM Functions 编排软件定义的无线电应用程序示例的云端。 IBM Functions 基于 OpenWhisk 并启用无服务器计算。 无服务器计算意味着可在没有任何支持基础结构（例如操作系统或编程语言系统）的情况下部署代码组件。 通过使用 IBM Functions，您可以专注于自己的代码，并将其他所有事务的缩放、安全性和正在进行的维护交由 IBM 为您处理。 未供应任何硬件；无 VM，并且无需任何容器。

无服务器代码组件配置为应对事件而触发（运行）。 在此示例中，只要音频剪辑由边缘节点发布到 {{site.data.keyword.message_hub_notm}}，触发事件即是来自 {{site.data.keyword.message_hub_notm}} 中边缘节点的消息的回执。 触发示例操作旨在采集数据并处理该数据。 它们使用 IBM Watson Speech-To-Text (STT) 服务将入局音频数据转换为文本。 然后，该文本将发送到 IBM Watson Natural Language Understanding (NLU) 服务，以分析向其包含的每个名词表达的观点。 有关更多信息，请参阅 [IBM Functions 操作代码 ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://github.com/open-horizon/examples/blob/master/cloud/sdr/data-processing/ibm-functions/actions/msgreceive.js)。

### IBM 数据库
{: #ibm_database}

IBM Functions 操作代码通过将计算的观点结果存储到 IBM 数据库中来得出结论。 然后，Web 服务器和客户机软件致力于从数据库向用户 Web 浏览器呈现此数据。

### Web 界面
{: #web_interface}

通过软件定义的无线电应用程序的 Web 用户界面，用户可以浏览从 IBM 数据库呈现的观点数据。 此用户界面还会呈现一张显示已提供数据的边缘节点的图。 该图使用来自 IBM 提供的 `gps` 服务的数据进行创建，此服务供边缘节点代码用于 `sdr2evtstreams` 服务。 `gps` 服务可与 GPS 硬件进行交互，或者从设备所有者接收有关位置的信息。 如果同时缺少 GPS 硬件和设备所有者位置，那么 `gps` 服务可以通过使用边缘节点 IP 地址查找地理位置来估算边缘节点位置。 通过使用此服务，`sdr2evtstreams` 可以在服务发送音频剪辑时将位置数据提供给云。 有关更多信息，请参阅[软件定义的无线电应用程序 Web UI 代码 ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://github.com/open-horizon/examples/tree/master/cloud/sdr/ui/sdr-app)。

（可选）如果要创建您自己的软件定义的无线电示例 Web UI，可在 IBM Cloud 中部署 IBM Functions、IBM 数据库和 web UI 代码。 您可以在[创建付费帐户 ![在新的选项卡中打开](../images/icons/launch-glyph.svg "在新的选项卡中打开")](https://cloud.ibm.com/login) 后使用单个命令来执行此操作。 有关更多信息，请参阅[部署存储库内容 ![在新的选项卡中打开](../images/icons/launch-glyph.svg "在新的选项卡中打开")](https://www.ibm.com/links?url=https%3A%2F%2Fgithub.com%2Fopen-horizon%2Fexamples%2Ftree%2Fmaster%2Fcloud%2Fsdr%2Fdeploy%2Fibm)。 

**注**：此部署过程需要用于对 {{site.data.keyword.cloud_notm}} 帐户收取费用的付费服务。

## 后续操作

如果您想将自己的软件部署到边缘节点，必须创建自己的边缘服务以及关联的部署模式或部署策略。 有关更多信息，请参阅[为设备开发边缘服务](../developing/developing.md)。
