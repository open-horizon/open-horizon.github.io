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

# 安装 cloudctl、kubectl 和 oc
{: #cloudctl_oc_cli}

遵循这些步骤以安装管理 {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) 管理中心和边缘集群的各个方面所需的命令行工具：

## cloudctl

1. 浏览 {{site.data.keyword.ieam}} Web UI：`https://<CLUSTER_URL>/common-nav/cli`

2. 展开 **IBM Cloud Pak CLI** 部分并选择您的**操作系统**。

3. 复制显示的 **curl** 命令并运行以下载 **cloudctl** 二进制文件。

4. 使文件可执行并将其移至 **/usr/local/bin**：
  
   ```bash
   chmod 755 cloudctl-*
   sudo mv cloudctl-* /usr/local/bin/cloudctl
   ```
   {: codeblock}

5. 确保 **/usr/local/bin** 位于您的路径中，然后验证 **cloudctl** 是否正常运行：
  
   ```bash
   cloudctl --help
   ```
   {: codeblock}

## oc

1. 从 [OpenShift 客户机 CLI (oc) ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://mirror.openshift.com/pub/openshift-v4/clients/ocp/latest/) 下载 {{site.data.keyword.open_shift_cp}} CLI tar 文件。 选择适合您的操作系统的 **openshift-client-\*-\*.tar.gz** 文件。

2. 查找下载的 tar 文件并解压缩：
  
   ```bash
   tar -zxvf openshift-client-*-*.tar.gz
   ```
   {: codeblock}

3. 将 **oc** 命令移至 **/usr/local/bin**：
  
   ```bash
   sudo mv oc /usr/local/bin/
   ```
   {: codeblock}

4. 确保 **/usr/local/bin** 位于您的路径中，然后验证 **oc** 是否正常运行：
  
   ```bash
   oc --help
   ```
   {: codeblock}

或者，使用 [homebrew ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://brew.sh/) 在 {{site.data.keyword.macOS_notm}} 上安装 **oc**：
  
   ```bash
   brew install openshift-cli
   ```
   {: codeblock}

## Kubectl

遵循[安装和设置 kubectl ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://kubernetes.io/docs/tasks/tools/install-kubectl/) 中的指示信息。
