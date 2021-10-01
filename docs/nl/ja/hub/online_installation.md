---

copyright:
  years: 2020
lastupdated: "2020-10-28"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# {{site.data.keyword.ieam}} のインストール
{: #hub_install_overview}

{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) ノードのタスクを開始する前に、管理ハブをインストールして構成する必要があります。

## インストールの要約
{: #sum}

* ここでは、以下のコンポーネントをデプロイするためのステップについて説明します。
  * [IBM Cloud プラットフォーム共通サービス 3.6.x](https://www.ibm.com/docs/en/cpfs)。
  * {{site.data.keyword.edge_notm}} Management Hub オペレーター。
  * {{site.data.keyword.edge_notm}} Exchange API。
  * {{site.data.keyword.edge_notm}} agbot。
  * {{site.data.keyword.edge_notm}} Cloud Sync Service (CSS)。
  * {{site.data.keyword.edge_notm}} ユーザー・インターフェース。
  * {{site.data.keyword.edge_notm}} セキュア・デバイス・オンボード (SDO)。
  * {{site.data.keyword.edge_notm}} シークレット・マネージャー (ボールト)。

**注:** 前のバージョンからアップグレードしようとしている場合は、[アップグレード資料](upgrade.md)を参照してください。

## 前提条件
{: #prereq}

### {{site.data.keyword.ocp_tm}}
適切なストレージ・クラスがクラスター内でインストールされていて動作していることも含め、[適切なサイズ](cluster_sizing.md)のサポートされている {{site.data.keyword.open_shift_cp}} 4.6 インストール済み環境があることを確認します。

IBM Cloud 管理対象 {{site.data.keyword.open_shift_cp}} 4.6 クラスターのプロビジョンについて詳しくは、以下を参照してください。

* [{{site.data.keyword.ocp_tm}} on {{site.data.keyword.cloud}}](https://www.ibm.com/cloud/openshift)

お客様独自の管理対象 {{site.data.keyword.open_shift_cp}} クラスターの作成について詳しくは、{{site.data.keyword.open_shift}} 資料を参照してください。

* [{{site.data.keyword.open_shift_cp}} 4.6 資料](https://docs.openshift.com/container-platform/4.6/welcome/index.html)

**注:** デフォルトでは、ローカルで開発したシークレット・マネージャーおよび開発データベースが、オペレーターのデプロイメントの一部としてプロビジョンされます。独自のプロビジョンしたデータベースへの接続およびその他の構成オプションについて詳しくは、『[構成](configuration.md)』を参照してください。

すべての永続データのバックアップとリストアはお客様の責任で行ってください。[バックアップおよびリストア](../admin/backup_recovery.md)を参照してください。

## ブラウザー・インストール・プロセス
{: #process}

1. クラスター管理者特権を使用して、{{site.data.keyword.open_shift_cp}} Web UI を介してログインします。 **「Storage」**ページに移動し、以下のように、サポートされる **Default** ストレージ・クラスが定義されていることを確認します。

   <img src="../images/edge/hub_install_storage_class.png" style="margin: 3%" alt="Default ストレージ・クラス" width="75%" height="75%" align="center">

   **注**: デフォルト以外のストレージ・クラスの使用について詳しくは、『[構成](configuration.md)』ページを参照してください。

2. IBM Operator Catalog Source を作成します。これにより、**IEAM Management Hub** バンドルをインストールできるようになります。 以下のイメージに表示されている、インポートの正符号を選択した後に、このテキストをコピーして貼り付けます。 テキストを貼り付けた後に、**「Create」**をクリックします。

   ```
   apiVersion: operators.coreos.com/v1alpha1
   kind: CatalogSource
   metadata:
     name: ibm-operator-catalog
     namespace: openshift-marketplace
   spec:
     displayName: IBM Operator Catalog
     publisher: IBM
     sourceType: grpc
     image: icr.io/cpopen/ibm-operator-catalog:latest
     updateStrategy:
       registryPoll:
         interval: 45m
   ```
   {: codeblock}

   <img src="../images/edge/hub_install_ibm_catalog.png" style="margin: 3%" alt="IBM Catalog Source の作成" align="center">

3. IBM Common Services Operator Catalog Source を作成します。 これにより、**IEAM Management Hub** で追加的にインストールする Common Service オペレーターのスイートが提供されます。 以下のイメージに表示されている、インポートの正符号を選択した後に、このテキストをコピーして貼り付けます。 テキストを貼り付けた後に、**「Create」**をクリックします。
   ```
   apiVersion: operators.coreos.com/v1alpha1
   kind: CatalogSource
   metadata:
     name: opencloud-operators
     namespace: openshift-marketplace
   spec:
     displayName: IBMCS Operators
     publisher: IBM
     sourceType: grpc
     image: quay.io/opencloudio/ibm-common-service-catalog:3.6
     updateStrategy:
       registryPoll:
         interval: 45m
   ```
   {: codeblock}

   <img src="../images/edge/hub_install_cs_catalog.png" style="margin: 3%" alt="IBM CS Catalog Source の作成">

4. **「Projects」**ページに移動し、オペレーターをインストールするプロジェクトを作成します。

   <img src="../images/edge/hub_install_create_project.png" style="margin: 3%" alt="プロジェクトの作成">

5. IBM Entitled Registry に認証するための **ibm-entitlement-key** という名前のイメージ・プル・シークレットを定義します。

   **注**:
   * [「My IBM Key」](https://myibm.ibm.com/products-services/containerlibrary)でライセンス・キーを入手し、以下のコンテンツで示されている各フィールドに入力します。
   * 前のステップで作成したのと同じプロジェクトにこのリソースが作成されたことを確認します。

   <img src="../images/edge/hub_install_pull_secret.png" style="margin: 3%" alt="イメージ・プル・シークレットの作成">

6. **「OperatorHub」**ページに移動し、**IEAM Management Hub** を検索します。

7. **IEAM Management Hub** カードをクリックし、**「Install」**をクリックします。

8. オペレーターをインストールします。プロジェクトがステップ 4 で作成したものに一致していることを確認してください。

   **注:** これは、**IEAM Management Hub** オペレーターがインストール後に監視する唯一のプロジェクトです。

   <img src="../images/edge/hub_install_operator.png" style="margin: 3%" alt="IEAM オペレーターのインストール">

9. ステップ 4 で作成した**プロジェクト**に再び変更し、ステップ 7 で表示された**「Provided APIs」**列の **EamHub** をクリックし、**「Create EamHub」**をクリックします。

   <img src="../images/edge/hub_install_create_eamhub.png" style="margin: 3%" alt="EamHub CR" width="75%" height="75%">

10. 管理ハブを定義および構成する **EamHub** カスタム・リソースを作成します。カスタマイズ・オプションについて詳しくは、[構成](configuration.md)を参照してください。プロジェクトがステップ 4 で作成したものに一致していることを確認してください。

   * **「Accept License」**トグルをクリックし、**「Create」**をクリックしてライセンスを受け入れます。

   <img src="../images/edge/hub_install_create_cr_45.png" style="margin: 3%" alt="EamHub CR 4.5 の作成" width="75%" height="75%">

オペレーターにより、ステップ 4 で指定したプロジェクトに、定義済みのワークロードがデプロイされ、**ibm-common-services** プロジェクトに、必要な {{site.data.keyword.common_services}}ワークロードがデプロイされます。

## 次に行うこと

[インストール後](post_install.md)のステップを実行して、新規管理ハブのセットアップを続行します。
