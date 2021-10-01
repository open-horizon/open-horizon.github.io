---

copyright:
  years: 2020
lastupdated: "2020-5-11"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 安装 hzn CLI
{: #using_hzn_cli}

在边缘节点上安装 {{site.data.keyword.ieam}} 代理程序软件时，会自动安装 **hzn** CLI。但您还可以不使用代理程序安装 **hzn** CLI。例如，边缘管理员可能希望查询 {{site.data.keyword.ieam}} Exchange，边缘开发者希望使用 **hzn dev** 命令进行测试。

1. 从管理中心管理员获取 **agentInstallFiles-&lt;edge-device-type&gt;.tar.gz** 文件，其中 **&lt;edge-device-type&gt;** 与您将在其中安装 **hzn** 的主机相匹配。管理员应该已在[为边缘设备收集必要的信息和文件](../../hub/gather_files.md#prereq_horizon)部分中进行了创建。 将此文件复制到您将在其中安装 **hzn** 的主机。

2. 在环境变量中为后续步骤设置文件名：

   ```bash
   export AGENT_TAR_FILE=agentInstallFiles-<edge-device-type>.tar.gz
   ```
   {: codeblock}

3. 从 tar 文件中解压缩 horizon CLI 软件包：

   ```bash
   tar -zxvf $AGENT_TAR_FILE 'horizon-cli*'
   ```
   {: codeblock}

   * 确认软件包版本与[组件](../getting_started/components.md)中列出的设备代理程序相同。

4. 安装 **horizon-cli** 软件包：

   * 在基于 debian 的分发版上：

     ```bash
     sudo apt update && sudo apt install horizon-cli*.deb
     ```
     {: codeblock}

   * 在 {{site.data.keyword.macOS_notm}} 上：

     ```bash
     sudo installer -pkg horizon-cli-*.pkg -target /
     ```
     {: codeblock}

     注：在 {{site.data.keyword.macOS_notm}} 上，还可以从“访达”安装 horizon-cli 软件包文件：双击该文件以打开安装程序。如果您收到一条错误消息，指示程序“由于来自不明开发者，无法打开”，请右键单击该文件并选择**打开**。系统提示“确定要打开么”时，再次单击**打开**。. 然后，按照提示安装 CLI horizon 软件包，并确保您的标识具有管理员特权。

## 卸载 hzn CLI

如果要从主机移除 **horizon-cli** 软件包：

* 从基于 debian 的分发版卸载 **horizon-cli**：

  ```bash
  sudo apt-get remove horizon-cli
  ```
  {: codeblock}

* 或者从 {{site.data.keyword.macOS_notm}} 卸载 **horizon-cli**：

  * 打开 hzn 客户机文件夹 (/usr/local/bin)，并将 `hzn` 应用程序拖到 “回收站”（在 Dock 末尾）。
