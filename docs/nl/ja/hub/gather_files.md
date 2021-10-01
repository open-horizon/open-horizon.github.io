---

copyright:
years: 2020
lastupdated: "2020-05-18"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# エッジ・ノード・ファイルの収集
{: #prereq_horizon}

エッジ・デバイスおよびエッジ・クラスターに {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) エージェントをインストールし、それらを {{site.data.keyword.ieam}} に登録するには、いくつかのファイルが必要です。 ここでは、エッジ・ノードで必要なファイルをバンドルする方法について説明します。 {{site.data.keyword.ieam}} 管理ハブに接続されている管理ホストでこれらのステップを実行してください。

以下のステップでは、[IBM Cloud Pak CLI (**cloudctl**) および OpenShift クライアント CLI (**oc**)](../cli/cloudctl_oc_cli.md) コマンドがインストールされていること、および解凍したインストール・メディアのディレクトリー **ibm-eam-{{site.data.keyword.semver}}-bundle** 内からステップを実行していることを前提としています。 このスクリプトは、**agent/edge-packages-{{site.data.keyword.semver}}.tar.gz** ファイル内で必要な {{site.data.keyword.horizon}} パッケージを検索し、必要なエッジ・ノード構成および証明書ファイルを作成します。

1. 管理者資格情報と、{{site.data.keyword.ieam}} をインストールした名前空間を使用して、管理ハブ・クラスターにログインします。
   ```bash
   cloudctl login -a <cluster-url> -u <cluster-admin-user> -p <cluster-admin-password> -n <namespace> --skip-ssl-validation
   ```
   {: codeblock}

2. 次の環境変数を設定します。

   ```bash
   export CLUSTER_URL=https://$(oc get cm management-ingress-ibmcloud-cluster-info -o jsonpath='{.data.cluster_ca_domain}')
   oc --insecure-skip-tls-verify=true -n kube-public get secret ibmcloud-cluster-ca-cert -o jsonpath="{.data.ca\.crt}" | base64 --decode > ieam.crt
   export HZN_MGMT_HUB_CERT_PATH="$PWD/ieam.crt"
   export HZN_FSS_CSSURL=${CLUSTER_URL}/edge-css
   ```
   {: codeblock}

   独自の **ENTITLEMENT_KEY** を提供する、次の Docker 認証環境変数を定義します。
   ```
   export REGISTRY_USERNAME=cp
   export REGISTRY_PASSWORD=<ENTITLEMENT_KEY>
   ```
   {: codeblock}

   **注:** [「My IBM Key」](https://myibm.ibm.com/products-services/containerlibrary)でライセンス・キーを入手します。

3. 以下のように、**edge-packages-{{site.data.keyword.semver}}.tar.gz** が配置されている **agent** ディレクトリーに移動します。

   ```bash
   cd agent
   ```
   {: codeblock}

4. **edgeNodeFiles.sh** スクリプトを使用してエッジ・ノードのインストールのためのファイルを収集する方法として、2 つの方法があります。 必要に応じて、次のいずれかの方法を選択します。

   * **edgeNodeFiles.sh** スクリプトを実行して、必要なファイルを収集し、モデル管理システム (MMS、Model Management System) の CSS Cloud Sync Service (CSS) コンポーネントに配置します。

     **注**: **edgeNodeFiles.sh スクリプト**は、horizon-cli パッケージの一部としてインストールされており、パスに含まれている必要があります。

     ```bash
     HZN_EXCHANGE_USER_AUTH='' edgeNodeFiles.sh ALL -c -p edge-packages-{{site.data.keyword.semver}} -r cp.icr.io/cp/ieam
     ```
     {: codeblock}

     各エッジ・ノードで、**agent-install.sh** の **-i 'css:'** フラグを使用して、必要なファイルを CSS から取得します。

     **注**: [SDO 対応エッジ・デバイス](../installing/sdo.md)を使用する予定の場合は、この形式の `edgeNodeFiles.sh` コマンドを実行する必要があります。

   * あるいは、以下のように **edgeNodeFiles.sh** を使用して、ファイルを tar ファイルにバンドルします。

     ```bash
     edgeNodeFiles.sh ALL -t -p edge-packages-{{site.data.keyword.semver}} -r cp.icr.io/cp/ieam
     ```
     {: codeblock}

     tar ファイルを各エッジ・ノードにコピーし、**agent-install.sh** の **-z** フラグを使用して、必要なファイルを tar ファイルから取得します。

     まだ **horizon-cli** パッケージが当該ホストにインストールされていない場合は、ここでインストールします。 このプロセスの例については、『[インストール後の構成](post_install.md#postconfig)』を参照してください。

     **horizon-cli** パッケージの一部としてインストールされた **agent-install.sh** および **agent-uninstall.sh** スクリプトを見つけます。    これらのスクリプトは、セットアップ時に各エッジ・ノードで必要になります (現在、**agent-uninstall.sh** ではエッジ・クラスターのみがサポートされます)。
    * {{site.data.keyword.linux_notm}} の例:

     ```
     ls /usr/horizon/bin/agent-{install,uninstall}.sh
     ```
     {: codeblock}

    * macOS の例:

     ```
     ls /usr/local/bin/agent-{install,uninstall}.sh
     ```
     {: codeblock}

**注**: **edgeNodeFiles.sh** には、収集するファイルおよびその配置場所を制御するためのフラグがさらに存在します。 使用可能なすべてのフラグを表示するには、**edgeNodeFiles.sh -h** を実行します。

## 次の作業

エッジ・ノードのセットアップ前に、ユーザーまたはノード技術者が API 鍵を作成し、他の環境変数の値を収集する必要があります。 [API 鍵の作成](prepare_for_edge_nodes.md)の手順に従ってください。
