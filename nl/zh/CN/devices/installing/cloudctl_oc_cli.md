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

需要命令行工具来管理 {{site.data.keyword.edge_notm}} 管理中心和边缘集群的各个方面。 使用以下步骤进行安装：

* **cloudctl 和 kubectl：**从以下 {{site.data.keyword.edge_notm}} Web UI 获取 IBM Cloud Pak CLI (**cloudctl**) 和 kubernetes CLI (**kubeclt**)：`https://<CLUSTER_URL>/common-nav/cli`

  * 在 {{site.data.keyword.macOS_notm}} 上安装 **kubectl** 的替代方法是，使用 [homebrew ![在新选项卡中打开](../../images/icons/launch-glyph.svg "在新选项卡中打开")](https://brew.sh/)：
  
    ```bash
    brew install kubernetes-cli`
    ```
    {: codeblock}

* **oc**：从 [OpenShift 客户机 CLI (oc) ![在新选项卡中打开](../../images/icons/launch-glyph.svg "在新选项卡中打开")](https://mirror.openshift.com/pub/openshift-v4/clients/ocp/latest/) 获取 {{site.data.keyword.open_shift_cp}} CLI。

  * 在 {{site.data.keyword.macOS_notm}} 上安装 **oc** 的替代方法是，使用 [homebrew ![在新选项卡中打开](../../images/icons/launch-glyph.svg "在新选项卡中打开")](https://brew.sh/)：
  
    ```bash
    brew install openshift-cli`
    ```
    {: codeblock}
