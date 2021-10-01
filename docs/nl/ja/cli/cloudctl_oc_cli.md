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

以下のステップに従って、{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) 管理ハブおよびエッジ・クラスターの各種側面を管理するために必要なコマンド・ライン・ツールをインストールします。

## cloudctl

1. {{site.data.keyword.ieam}} Web UI (`https://<CLUSTER_URL>/common-nav/cli`) をブラウズします。

2. **「IBM Cloud Pak CLI」**セクションを展開し、ご使用の **OS** を選択します。

3. 表示されている **curl** コマンドをコピーして実行し、**cloudctl** バイナリーをダウンロードします。

4. 以下のように、ファイルを実行可能にし、**/usr/local/bin** に移動します。
  
   ```bash
   chmod 755 cloudctl-*
   sudo mv cloudctl-* /usr/local/bin/cloudctl
   ```
   {: codeblock}

5. **/usr/local/bin** が PATH に含まれていることを確認してから、以下のように、**cloudctl** が動作していることを確認します。
  
   ```bash
   cloudctl --help
   ```
   {: codeblock}

## oc

1. {{site.data.keyword.open_shift_cp}} CLI tar ファイルを [OpenShift クライアント CLI (oc)](https://mirror.openshift.com/pub/openshift-v4/clients/ocp/latest/) からダウンロードします。 ご使用のオペレーティング・システムのファイル **openshift-client-\*-\*.tar.gz** を選択します。

2. ダウンロードした tar ファイルを見つけ、以下のように解凍します。
  
   ```bash
   tar -zxvf openshift-client-*-*.tar.gz
   ```
   {: codeblock}

3. 以下のように、**oc** コマンドを **/usr/local/bin** に移動します。
  
   ```bash
   sudo mv oc /usr/local/bin/
   ```
   {: codeblock}

4. **/usr/local/bin** が PATH に含まれていることを確認してから、以下のように、**oc** が動作していることを確認します。
  
   ```bash
   oc --help
   ```
   {: codeblock}

あるいは、[homebrew](https://brew.sh/) を使用して **oc** を {{site.data.keyword.macOS_notm}} にインストールします。
  
   ```bash
   brew install openshift-cli
   ```
   {: codeblock}

## Kubectl

『[Install and Set Up kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)』の手順に従います。
