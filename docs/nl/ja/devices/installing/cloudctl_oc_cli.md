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

# cloudctl、kubectl、および oc のインストール
{: #cloudctl_oc_cli}

これらのコマンド・ライン・ツールは、{{site.data.keyword.edge_notm}} 管理ハブおよびエッジ・クラスターの多くの側面を管理するために必要です。 これらをインストールするには、以下のステップを実行します。

* **cloudctl および kubectl:** IBM Cloud Pak CLI (**cloudctl**) および kubernetes CLI (**kubeclt**) を {{site.data.keyword.edge_notm}} Web UI (`https://<CLUSTER_URL>/common-nav/cli`) から入手します。

  * {{site.data.keyword.macOS_notm}} での **kubectl** のインストールの代替方法は、[homebrew ![新しいタブで開く](../../images/icons/launch-glyph.svg "新しいタブで開く")](https://brew.sh/) を使用することです。
  
    ```bash
    brew install kubernetes-cli`
    ```
    {: codeblock}

* **oc:** {{site.data.keyword.open_shift_cp}} CLI を [OpenShift client CLI (oc) ![新しいタブで開く](../../images/icons/launch-glyph.svg "新しいタブで開く")](https://mirror.openshift.com/pub/openshift-v4/clients/ocp/latest/) から入手します。

  * {{site.data.keyword.macOS_notm}} での **oc** のインストールの代替方法は、[homebrew ![新しいタブで開く](../../images/icons/launch-glyph.svg "新しいタブで開く")](https://brew.sh/) を使用することです。
  
    ```bash
    brew install openshift-cli`
    ```
    {: codeblock}
