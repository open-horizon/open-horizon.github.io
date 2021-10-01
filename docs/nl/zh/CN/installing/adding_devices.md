---

copyright:
years: 2019, 2020
lastupdated: "2020-10-28"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 准备边缘设备
{: #installing_the_agent}

下列指示信息指导您完成在边缘设备上安装必需软件并使用 {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) 进行注册的过程。

## 受支持的体系结构和操作系统
{: #suparch-horizon}

{{site.data.keyword.ieam}} 支持采用以下硬件体系结构的体系结构和操作系统：

* x86_64
   * {{site.data.keyword.linux_bit_notm}} 设备或虚拟机，运行 Ubuntu 20.x (focal)、Ubuntu 18.x (bionic)、Debian 10 (buster) 或 Debian 9 (stretch)
   * Red Hat Enterprise Linux&reg; 8.2
   * Fedora Workstation 32
   * CentOS 8.2
   * SuSE 15 SP2
* ppc64le（仅 {{site.data.keyword.ieam}} {{site.data.keyword.semver}}）
   * Red Hat Enterprise Linux&reg; 7.9
* ARM（32 位）
   * {{site.data.keyword.linux_notm}} on ARM（32 位），例如，运行 Raspbian buster 或 stretch 的 Raspberry Pi
* ARM（64 位）
   * {{site.data.keyword.linux_notm}} on ARM（64 位），例如，运行 Ubuntu 18.x (bionic) 的 NVIDIA Jetson Nano、TX1 或 TX2
* Mac
   * {{site.data.keyword.macOS_notm}}

**注**： 

* 仅[高级手动代理程序安装和注册](../installing/advanced_man_install.md)方法支持安装使用 Fedora 或 SuSE 的边缘设备。
* CentOS 和 Red Hat Enterprise Linux&reg; 目前仅支持 Docker 作为 IEAM 4.2 中的容器引擎。

## 调整大小
{: #size}

代理程序需要：

* 100 MB 随机存取存储器 (RAM)，包括 Docker。 RAM 增长为比此数量高出大约每个协议 100 K，加上在设备上运行的工作负载所需的任何额外内存。
* 400 MB 磁盘（包括 Docker）。 磁盘增长为高出此数量的值基于工作负载使用的容器映像的大小以及部署到设备的模型对象的大小（乘以 2）。

# 安装代理程序
{: #installing_the_agent}

下列指示信息指导您完成在边缘设备上安装必需软件并使用 {{site.data.keyword.ieam}} 进行注册的过程。

## 过程
{: #install-config}

要安装和配置边缘设备，请单击表示边缘设备类型的链接：

* [{{site.data.keyword.linux_bit_notm}} 设备或虚拟机](#x86-machines)
* [{{site.data.keyword.linux_ppc64le_notm}} 设备或虚拟机](#ppc64le-machines)（仅 {{site.data.keyword.ieam}} {{site.data.keyword.semver}}）
* [{{site.data.keyword.linux_notm}} on ARM（32 位）](#arm-32-bit)；例如，运行 Raspbian 的 Raspberry Pi
* [{{site.data.keyword.linux_notm}} on ARM（64 位）](#arm-64-bit)；例如，NVIDIA Jetson Nano、TX1 或 TX2
* [{{site.data.keyword.macOS_notm}}](#mac-os-x)

## {{site.data.keyword.linux_bit_notm}} 设备或虚拟机
{: #x86-machines}

### 硬件需求
{: #hard-req-x86}

* 64 位 Intel&reg; 或 AMD 设备或虚拟机
* 设备的因特网连接（有线或 Wi-Fi）
* （可选）传感器硬件：许多 {{site.data.keyword.horizon}} 边缘服务需要专门的传感器硬件。

### 过程
{: #proc-x86}

通过安装 Debian、Red Hat Enterprise Linux&reg; 或 Ubuntu {{site.data.keyword.linux_notm}} 来准备设备。此内容中的指示信息基于使用 Ubuntu 18.x 的设备。

在设备上安装最新版本的 Docker。 有关更多信息，请参阅[安装 Docker ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://docs.docker.com/engine/install/ubuntu/)。

现在，您的边缘设备已准备好，继续[安装代理程序](registration.md)。

## {{site.data.keyword.linux_ppc64le_notm}} 设备或虚拟机（仅 {{site.data.keyword.ieam}} {{site.data.keyword.semver}}）
{: #ppc64le-machines}

### 硬件需求
{: #hard-req-ppc64le}

* ppc64le 设备或虚拟机
* 设备的因特网连接（有线或 Wi-Fi）
* （可选）传感器硬件：许多 {{site.data.keyword.horizon}} 边缘服务需要专门的传感器硬件。

### 过程
{: #proc-ppc64le}

通过安装 Red Hat Enterprise Linux&reg; 来准备设备。

在设备上安装最新版本的 Docker。 

现在，您的边缘设备已准备好，继续[安装代理程序](registration.md)。

## {{site.data.keyword.linux_notm}} on ARM（32 位）
{: #arm-32-bit}

### 硬件需求
{: #hard-req-pi}

* Raspberry Pi 3A+、3B、3B+ 或 4（首选）
* Raspberry Pi A+、B+、2B、Zero-W 或 Zero-WH
* MicroSD 闪存卡（最好 32 GB）
* 适合于设备的电源（最好 2 安培或更高）
* 设备的因特网连接（有线或 Wi-Fi）。
  **注**：某些设备需要额外的硬件才能支持 Wi-Fi。
* （可选）传感器硬件：许多 {{site.data.keyword.horizon}} 边缘服务需要专门的传感器硬件。

### 过程
{: #proc-pi}

1. 准备 Raspberry Pi 设备。
   1. 将 [Raspbian ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://www.raspberrypi.org/downloads/raspbian/) {{site.data.keyword.linux_notm}} 映像闪存到 MicroSD 卡。

      有关如何从多个操作系统闪存 MicroSD 映像的更多信息，请参阅 [Raspberry Pi Foundation ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://www.raspberrypi.org/documentation/installation/installing-images/README.md)。
      下列指示信息使用 Raspbian 进行 Wi-Fi 和 SSH 配置。  

      **警告：**将映像闪存到 MicroSD 卡会永久擦除该卡上已有的任何数据。

   2. （可选）如果您计划使用 Wi-Fi 来连接设备，请编辑新闪存的映像，以提供适当的 WPA2 Wi-Fi 凭证。 

      如果您计划使用有线网络连接，那么无需完成此步骤。  

      在 MicroSD 卡上，在 Wi-Fi 凭证所在的根级别文件夹中创建名为 `wpa_supplicant.conf` 的文件。 这些凭证包括网络 SSID 名称和口令。 文件格式如下所示： 
      
      ```
      country=US
      ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev update_config=1
      network={
      ssid=“<your-network-ssid>”
      psk=“<your-network-passphrase”
      key_mgmt=WPA-PSK>
      }
      ```
      {: codeblock}

   3. （可选）如果您希望或需要运行没有监视器或键盘的 Raspberry Pi 设备，那么需要启用对该设备的 SSH 连接访问。 缺省情况下，SSH 访问不可用。

      要启用 SSH 连接，请在 MicroSD 卡上创建一个名为 `ssh` 的空文件。 请将此文件放在卡的根级别文件夹中。 通过包括此文件，您就能够使用缺省凭证来连接到设备。 

   4. 卸载 MicroSD 卡。 务必从您用来编辑该卡的设备安全地弹出该卡，以便写入所有更改。

   5. 将该 MicroSD 卡插入 Raspberry Pi 设备中。 连接任何可选的传感器硬件，并接通该设备的电源。

   6. 启动该设备。

   7. 更改该设备的缺省密码。 在 Raspbian 闪存映像中，缺省帐户使用登录名 `pi` 和缺省密码 `raspberry`。

      登录该帐户。 使用标准的 {{site.data.keyword.linux_notm}} `passwd` 命令来更改缺省密码：

      ```
      passwd
      Enter new UNIX password:  
      Retype new UNIX password:
      passwd: password updated successfully
      ```
      {: codeblock}
     
   8. 在设备上安装最新版本的 Docker。 有关更多信息，请参阅[安装 Docker ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://docs.docker.com/engine/install/debian/)。 

现在，您的边缘设备已准备好，继续[安装代理程序](registration.md)。

## {{site.data.keyword.linux_notm}} on ARM（64 位）
{: #arm-64-bit}

### 硬件需求
{: #hard-req-nvidia}

* NVIDIA Jetson Nano 或 TX2（建议）
* NVIDIA Jetson TX1
* HDMI 商用监视器、USB 集线器、USB 键盘和 USB 鼠标
* 存储空间：至少 10 GB（建议使用 SSD）
* 设备的因特网连接（有线或 Wi-Fi）
* （可选）传感器硬件：许多 {{site.data.keyword.horizon}} 边缘服务需要专门的传感器硬件。

### 过程
{: #proc-nvidia}

1. 准备 NVIDIA Jetson 设备。
   1. 在设备上安装最新的 NVIDIA JetPack。 有关更多信息，请参阅：
      * (TX1) [Jetson TX1 ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://elinux.org/Jetson_TX1)
      * (TX2) [利用 Jetson TX2 Developer Kit 为边缘配备 AI ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://developer.nvidia.com/embedded/jetson-tx2-developer-kit)
      * (Nano) [开始使用 Jetson Nano Developer Kit ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit)

      必须先安装此软件和任何必备软件，然后再安装 {{site.data.keyword.horizon}} 软件。

   2. 更改缺省密码。 在 JetPack 安装过程中，缺省帐户使用登录名 `nvidia` 和缺省密码 `nvidia`。 

      登录该帐户。 使用标准的 {{site.data.keyword.linux_notm}} `passwd` 命令来更改缺省密码：

      ```
      passwd
      Enter new UNIX password:  
      Retype new UNIX password:
      passwd: password updated successfully
      ```
      {: codeblock}
      
   3. 在设备上安装最新版本的 Docker。 有关更多信息，请参阅[安装 Docker ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://docs.docker.com/engine/install/debian/)。 

现在，您的边缘设备已准备好，继续[安装代理程序](registration.md)。

## {{site.data.keyword.macOS_notm}}
{: #mac-os-x}

### 硬件需求
{: #hard-req-mac}

* 2010 或更高版本的 64 位 {{site.data.keyword.intel}} Mac 设备
* 需要 MMU 虚拟化。
* MacOS X V10.11（“El Capitan”）或更高版本
* 机器的因特网连接（有线或 Wi-Fi）
* （可选）传感器硬件：许多 {{site.data.keyword.horizon}} 边缘服务需要专门的传感器硬件。
### 过程
{: #proc-mac}

1. 准备该设备。
   1. 在设备上安装最新版本的 Docker。 有关更多信息，请参阅[安装 Docker ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://docs.docker.com/docker-for-mac/install/)。

   2. **安装 socat**。 您可以使用以下任一种方法来安装 socat：

      * [使用 Homebrew 来安装 socat ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://brewinstall.org/install-socat-on-mac-with-brew/)。
   
      * 如果已安装 MacPorts，请使用其来安装 socat：
        ```
        sudo port install socat
        ```
        {: codeblock}

## 下一步是什么

* [安装代理程序](registration.md)
* [更新代理程序](updating_the_agent.md)

## 相关信息

* [安装 {{site.data.keyword.ieam}}](../hub/online_installation.md)
* [代理程序的高级手动安装和注册](advanced_man_install.md)
