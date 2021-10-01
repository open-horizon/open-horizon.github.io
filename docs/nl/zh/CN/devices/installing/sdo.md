---

copyright:
years: 2020
lastupdated: "2020-4-24"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# SDO 代理程序安装和注册
{: #sdo}

**技术预览**：此时，SDO 支持只应该用于测试并熟悉 SDO 进程，以便规划在未来加以使用。在未来的发行版中，SDO 支持将可用于生产用途。

[SDO ![在新选项卡中打开](../../images/icons/launch-glyph.svg "在新选项卡中打开")](https://software.intel.com/en-us/secure-device-onboard) (Secure Device Onboard) 是 Intel 创造的一项技术，用于轻松、安全地配置边缘设备并将其与边缘管理中心相关联。{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) 添加了对启用 SDO 的设备的支持，以便代理程序将以零接触的方式安装在该设备上并注册到 {{site.data.keyword.ieam}} 管理中心（只需打开设备的电源即可）。

## SDO 概述
{: #sdo-overview}

SDO 包括以下四个组件：

1. 边缘设备上的 SDO 模块（通常由设备制造商安装在其中）
2. 所有权凭单（随物理设备提供给设备购买者的文件）
3. SDO 集中服务器（启用 SDO 的设备在首次引导时首次联系的已知服务器）
4. SDO 所有者服务（使用 {{site.data.keyword.ieam}} 管理中心运行的服务，用于将设备连接到此特定 {{site.data.keyword.ieam}} 实例）

### 技术预览中的差异
{: #sdo-tech-preview-differences}

- **启用 SDO 的设备：**对于 SDO 测试，提供了脚本以用于将 SDO 模块添加到 VM，以便它在引导时的行为与启用 SDO 的设备相同。这样一来，您可以使用 {{site.data.keyword.ieam}} 测试 SDO 集成，而无需购买启用 SDO 的设备。
- **所有权凭单：**通常您会从设备制造商收到所有权凭单。如果使用前一个项目符号中提到的脚本将 SDO 模块添加到 VM，还将在该 VM 上创建所有权凭单。从 VM 复制该凭单即表示“从设备制造商收到所有权凭单”。
- **集中服务器：**在生产中，引导设备将联系 Intel 的全球 SDO 集中服务器。对于此技术预览的开发和测试，您将使用与 SDO 所有者服务捆绑在一起的开发集中服务器。
- **SDO 所有者服务：**在此技术预览中，SDO 所有者服务不会自动安装在 {{site.data.keyword.ieam}} 管理中心上。我们会改为提供便捷脚本，以在具有对 {{site.data.keyword.ieam}} 管理中心的网络访问权并且可由 SDO 设备通过网络访问的任何服务器上启动 SDO 所有者服务。

## 使用 SDO
{: #using-sdo}

要试用 SDO 以及确保它自动安装 {{site.data.keyword.ieam}} 代理程序并将其注册到 {{site.data.keyword.ieam}} 管理中心，请遵循 [open-horizon/SDO-support 存储库 ![在新选项卡中打开](../../images/icons/launch-glyph.svg "在新选项卡中打开")](https://github.com/open-horizon/SDO-support/blob/master/README.md) 中的步骤。
