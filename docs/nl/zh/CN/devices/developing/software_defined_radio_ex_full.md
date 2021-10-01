---

copyright:
years: 2019
lastupdated: "2019-06-26"

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

***作者注释：当 Troy 组合时，这将与 software_defined_radi_ex.md 合并。***

本示例使用软件定义的无线电 (SDR) 作为边缘处理示例。 利用 SDR，可以将完整无线电频谱内的原始数据发送到云服务器进行处理。 边缘节点在本地处理数据，然后将较少量的更高价值数据发送到云处理服务以进行额外处理。
{:shortdesc}

此图显示此 SDR 示例的体系结构：

<img src="../../images/edge/08_sdrarch.svg" width="70%" alt="示例体系结构">

SDR 边缘处理是一个功能齐全的示例，它使用无线电台音频，提取语音，并将提取的语音转换为文本。 此示例对该文本完成情感分析，通过用户界面提供数据和结果，在该界面中，您可以查看每个边缘节点的数据详细信息。 使用此示例可进一步了解边缘处理。

SDR 通过使用计算机 CPU 中的数字电路来接收无线电信号，以处理需要一组专用模拟电路的工作。 该模拟电路通常受到它所能接收的无线电频谱宽度的限制。 例如，为接收 FM 广播电台而构建的模拟无线电接收器，无法接收来自无线电频谱上任何其他位置的无线电信号。 SDR 可以访问大部分频谱。 如果没有 SDR 硬件，您可以使用模拟数据。 使用模拟数据时，来自因特网流的音频被视为通过 FM 广播，并在边缘节点上接收。

在执行此任务之前，通过执行[在边缘设备上安装 Horizon 代理程序并向 Hello world 示例注册](registration.md)中的步骤，注册和注销您的边缘设置。

此代码包含以下主要组件。

|组件|Description|
|---------|-----------|
|[sdr 服务 ![在新选项卡中打开](../../images/icons/launch-glyph.svg "在新选项卡中打开")](https://github.com/open-horizon/examples/tree/master/edge/services/sdr)|较低级别的服务访问边缘节点上的硬件。|
|[ssdr2evtstreams 服务 ![在新选项卡中打开](../../images/icons/launch-glyph.svg "在新选项卡中打开")](https://github.com/open-horizon/examples/tree/master/edge/evtstreams/sdr2evtstreams)|较高级别的服务从较低级别的 sdr 服务接收数据并完成边缘节点上的数据的本地分析。 然后，sdr2evtstreams 服务将已处理的数据发送到云后端软件。|
|[云后端软件 ![在新选项卡中打开](../../images/icons/launch-glyph.svg "在新选项卡中打开")](https://github.com/open-horizon/examples/tree/master/cloud/sdr)|云后端软件接收来自边缘节点的数据以进一步分析。 然后，后端实施可在基于 Web 的 UI 中呈现边缘节点图和更多内容。|
{: caption="表 1. 软件定义无线电到 {{site.data.keyword.message_hub_notm}} 主要组件" caption-side="top"}

## 注册设备

尽管通过在任何边缘设备上使用模拟数据可运行此服务，但如果要使用带有 SDR 硬件的 Raspberry Pi，请先配置内核模块以支持 SDR 硬件。 您必须手动配置此模块。 Docker 容器可以在其上下文中建立不同的 Linux 分布，但该容器无法安装内核模块。 

请完成下列步骤以配置此模块：

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

4. 在您的环境中设置以下 {{site.data.keyword.message_hub_notm}} API 密钥。 创建此密钥是为了与本示例配合使用，以便为 IBM 软件定义的无线电 UI 提供由您的边缘节点收集的已处理的数据。

   ```
   export EVTSTREAMS_API_KEY=X2e8cSjbDAMk-ztJLaoi3uffy8qsQTnZttUjcHCfm7cp
    export EVTSTREAMS_BROKER_URL=broker-3-y420pyyyvhhmttz0.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-5-y420pyyyvhhmttz0.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-4-y420pyyyvhhmttz0.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-1-y420pyyyvhhmttz0.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-0-y420pyyyvhhmttz0.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-2-y420pyyyvhhmttz0.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093
   ```
   {: codeblock}

5. 要在边缘节点上运行 sdr2evtstreams 服务示例，必须向 IBM/pattern-ibm.sdr2evtstreams 部署模式注册边缘节点。 执行 [Preconditions for Using the SDR To IBM Event Streams Example Edge Service![在新的选项卡中打开](../../images/icons/launch-glyph.svg "在新的选项卡中打开")](https://www.ibm.com/links?url=https%3A%2F%2Fgithub.com%2Fopen-horizon%2Fexamples%2Ftree%2Fmaster%2Fedge%2Fevtstreams%2Fsdr2evtstreams) 中的步骤。

6. 检查示例 Web UI，确定边缘节点是否在发送结果。 有关更多信息，请参阅[软件定义的无线电示例 Web UI ![在新选项卡中打开](../../images/icons/launch-glyph.svg "在新选项卡中打开")](https://sdr-poc-sdr-poc-app-delightful-leopard.mybluemix.net)。 使用这些凭证登录：

   * 用户名：guest@ibm.com
   * 密码：guest123

## 在云端部署

（可选）如果要创建您自己的软件定义的无线电示例 Web UI，可在 IBM Cloud 中部署 IBM Functions、IBM 数据库和 web UI 代码。 您可以在[创建付费帐户 ![在新的选项卡中打开](../../images/icons/launch-glyph.svg "在新的选项卡中打开")](https://cloud.ibm.com/login) 后使用单个命令来执行此操作。

部署代码位于 examples/cloud/sdr/deploy/ibm 存储库中。 有关更多信息，请参阅[部署存储库内容 ![在新的选项卡中打开](../../images/icons/launch-glyph.svg "在新的选项卡中打开")](https://www.ibm.com/links?url=https%3A%2F%2Fgithub.com%2Fopen-horizon%2Fexamples%2Ftree%2Fmaster%2Fcloud%2Fsdr%2Fdeploy%2Fibm)。 

此代码由包含详细指示信息的 README.md 文件和用于处理工作负载的 deploy.sh 脚本组成。 存储库还将 Makefile 作为另一个接口包含到 deploy.sh 脚本中。 复审存储库指示信息以了解有关为 SDR 示例部署您自己的云后端的更多信息。

注：此部署过程需要用于对 {{site.data.keyword.cloud_notm}} 帐户收取费用的付费服务。

## 后续操作

如果您想将自己的软件部署到边缘节点，必须创建自己的边缘服务以及关联的部署模式或部署策略。 有关更多信息，请参阅[使用 IBM Edge Application Manager for Devices 开发边缘服务](../developing/developing.md)。
