# IBM&reg; Edge Application Manager

## 概要

IBM Edge Application Manager は、IoT デプロイメントで典型的な、エッジ・デバイスにデプロイされるアプリケーション向けに、エンドツーエンドの**アプリケーション管理プラットフォーム**を提供します。 このプラットフォームは、現場に配置された何千ものエッジ・デバイスでエッジ・ワークロードのリビジョンを安全にデプロイする作業を完全に自動化し、そういった作業からアプリケーション開発者を解放します。 アプリケーション開発者は、代わりに、個別にデプロイ可能な Docker コンテナーとしてアプリケーション・コードを任意のプログラミング言語で作成する作業に集中できます。 完全なビジネス・ソリューションをすべてのデバイスで Docker コンテナーのマルチレベル・オーケストレーションとして安全かつシームレスにデプロイするという負担をこのプラットフォームが担います。

https://www.ibm.com/cloud/edge-application-manager

## 前提条件

[前提条件](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.1/hub/offline_installation.html#prereq)を参照してください。

## Red Hat OpenShift SecurityContextConstraints の要件

デフォルトの `SecurityContextConstraints` (名前: [`restricted`](https://ibm.biz/cpkspec-scc)) がこのチャートのために検証済みです。 このリリースは、`kube-system` 名前空間へのデプロイメントに限定されていて、メイン・チャート用のサービス・アカウントと、デフォルトのローカル・データベース・サブチャート用の追加のサービス・アカウントが作成されます。

## チャートの詳細

この helm チャートは、IBM Edge Application Manager 認定コンテナーを OpenShift 環境にインストールして構成します。 以下のコンポーネントがインストールされます。

* IBM Edge Application Manager - Exchange
* IBM Edge Application Manager - AgBots
* IBM Edge Application Manager - Cloud Sync Service (モデル管理システムの一部)
* IBM Edge Application Manager - ユーザー・インターフェース (管理コンソール)

## 必要なリソース

[サイジング](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.1/hub/cluster_sizing.html)を参照してください。

## ストレージおよびデータベースの要件

IBM Edge Application Manager のコンポーネントのデータを保管するために、3 つのデータベース・インスタンスが必要です。

デフォルトで、チャートは、以下に示す量でサイズ設定された 3 つのパーシスタント・データベースを、定義されたデフォルトの (またはユーザーが構成した) kubernetes 動的ストレージ・クラスを使用してインストールします。 ボリューム拡張を許可しないストレージ・クラスを使用する場合、拡張を行うことを適切に許可してください。

**注:** これらのデフォルトのデータベースは、実動での使用を意図したものではありません。 独自の管理対象データベースを利用するには、下記の要件を参照し、『**リモート・データベースの構成**』セクションのステップに従ってください。

* PostgreSQL: Exchange データおよび AgBot データを保管します
  * それぞれが少なくとも 20 GB バイトのストレージを持つ 2 つの別々のインスタンスが必要です
  * インスタンスは少なくとも 100 の接続をサポートする必要があります
  * 実動使用の場合は、これらのインスタンスの可用性を高くする必要があります
* MongoDB: Cloud Sync Service データを保管します
  * 少なくとも 50 GB バイトのストレージを持つ 1 つのインスタンスが必要です。 **注:** 必要なサイズは、保管および使用するエッジ・サービス・モデルおよびファイルのサイズと数に大きく依存します。
  * 実動使用の場合は、このインスタンスの可用性を高くする必要があります

**注:** これらのデフォルト・データベースおよびお客様独自の管理対象データベースのバックアップの頻度/手順についてはお客様の責任です。
デフォルトのデータベース手順については、『**バックアップおよびリカバリー**』セクションを参照してください。

## リソースのモニター

IBM Edge Application Manager がインストールされると、kubernetes で実行される製品リソースの基本的なモニターが自動的にセットアップされます。 モニター・データは、管理コンソールの Grafana ダッシュボードの以下の場所で表示できます。

* `https://<MANAGEMENT_URL:PORT>/grafana/d/kube-system-ibm-edge-overview/ibm-edge-overview`

## 構成

#### リモート・データベースの構成

1. 独自の管理対象データベースを使用するには、`values.yaml` 内で以下の helm 構成パラメーターを検索して、値を `false` に変更します。

```yaml
localDBs:
  enabled: true
```

2. 以下のテンプレート・コンテンツから始まるファイル (例えば `dbinfo.yaml` という名前) を作成します。

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: ibm-edge-remote-dbs
  labels:
    release: ibm-edge
type: Opaque
stringData:
  # agbot postgresql connection settings
  agbot-db-host: "Single hostname of the remote database"
  agbot-db-port: "Single port the database runs on"
  agbot-db-name: "The name of the database to utilize on the postgresql instance"
  agbot-db-user: "Username used to connect"
  agbot-db-pass: "Password used to connect"
  agbot-db-ssl: "SSL Options: <disable|require|verify-full>"

  # exchange postgresql connection settings
  exchange-db-host: "Single hostname of the remote database"
  exchange-db-port: "Single port the database runs on"
  exchange-db-name: "The name of the database to utilize on the postgresql instance"
  exchange-db-user: "Username used to connect"
  exchange-db-pass: "Password used to connect"
  exchange-db-ssl: "SSL Options: <disable|require|verify-full>"

  # css mongodb connection settings
  css-db-host: "Comma separate <hostname>:<port>,<hostname2>:<port2>"
  css-db-name: "The name of the database to utilize on the mongodb instance"
  css-db-user: "Username used to connect"
  css-db-pass: "Password used to connect"
  css-db-auth: "The name of the database used to store user credentials"
  css-db-ssl: "SSL Options: <true|false>"

  trusted-certs: |-
    -----BEGIN CERTIFICATE-----
    ....
    -----END CERTIFICATE-----
    -----BEGIN CERTIFICATE-----
    ....
    -----END CERTIFICATE-----
```

3. `dbinfo.yaml` を編集して、プロビジョンしたデータベースのアクセス情報を指定します。 二重引用符で囲まれたすべての情報を埋めてください (値は引用符で囲まれたままにします)。 信頼される証明書を追加するときには、yaml ファイルを読みやすくするために各行を 4 スペース字下げしてください。 2 つ以上のデータベースが同じ証明書を使用する場合、その証明書を `dbinfo.yaml` 内で繰り返す必要は**ありません**。 ファイルを保存した後、以下を実行します。

```bash
oc --namespace kube-system apply -f dbinfo.yaml
```


#### 拡張構成

デフォルトの helm 構成パラメーターのいずれかを変更するには、下の `grep` コマンドを使用してパラメーターおよびその説明を検討し、その後で、`values.yaml` 内で対応する値を表示/編集します。

```bash
grep -v -E '(^ *#|__metadata)' ibm_cloud_pak/values-metadata.yaml
vi values.yaml   # or use any editor
```

## チャートのインストール

**注:**

* これは CLI のみのインストールであり、GUI からのインストールはサポートされていません。

* [IBM Edge Application Manager インフラストラクチャーのインストール - インストール・プロセス](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.1/hub/offline_installation.html#process)のステップを完了していることを確認してください。
* インストールされた IBM Edge Application Manager のインスタンスはクラスター当たり 1 つのみ存在でき、`kube-system` 名前空間にのみインストールできます。
* IBM Edge Application Manager 4.0 からのアップグレードはサポートされていません。

IBM Edge Application Manager をインストールするには、提供されているインストール・スクリプトを実行します。 このスクリプトによって実行される主なステップは、helm チャートのインストールと、インストール後の環境の構成 (Agbot、組織、およびパターン/ポリシーのサービスの作成) です。

```bash
ibm_cloud_pak/pak_extensions/support/ieam-install.sh
```

**注:** ネットワーク速度によっては、イメージをダウンロードし、チャート・リソースのすべてがデプロイされるまでに、数分かかります。

### チャートの検証

* 上記のスクリプトは、ポッドが実行中であり、Agbot と Exchange が応答していることを検証します。 インストールの終盤に「RUNNING」および「PASSED」メッセージを探してください。
* 「FAILED」の場合、出力には、特定のログで詳細情報を確認するようにという指示が示されます。
* 「PASSED」の場合、出力には、実行されたテストの詳細と、管理 UI の URL が示されます。
  * ログの末尾にある URL で IBM Edge Application Manager UI コンソールを参照します。
    * `https://<MANAGEMENT_URL:PORT>/edge`

## インストール後

[インストール後の構成](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.1/hub/post_install.html)の手順に従います。

## チャートのアンインストール

[管理ハブのアンインストール](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.1/hub/uninstall.html)の手順に従います。

## 役割ベースのアクセス権限

* この製品をインストールおよび管理するには、`kube-system` 名前空間内でのクラスター管理者権限が必要です。
* リリース名に基づいて、このチャートおよびサブチャート用のサービス・アカウント、役割、および役割バインディングが作成されます。
* Exchange 認証および役割:
  * Exchange のすべての管理者およびユーザーの認証は、`cloudctl` コマンドで生成される API 鍵を通して IAM によって提供されます。
  * Exchange の管理者には、Exchange 内での `admin` 特権が付与される必要があります。 この特権を持っていると、管理者は自分の Exchange 組織内のすべてのユーザー、ノード、サービス、パターン、およびポリシーを管理できます。
  * Exchange の管理者以外のユーザーは、自分が作成したユーザー、ノード、サービス、パターン、およびポリシーのみを管理できます。

## セキュリティー

* Ingress を介して OpenShift クラスターへ出入りするすべてのデータに対して TLS が使用されます。 このリリースでは、OpenShift クラスター**内部**ではノード間の通信のために TLS は使用されません。 必要な場合、マイクロサービス間の通信用に Red Hat OpenShift サービス・メッシュを構成してください。 [Understanding Red Hat OpenShift Service Mesh](https://docs.openshift.com/container-platform/4.4/service_mesh/service_mesh_arch/understanding-ossm.html#understanding-ossm) を参照してください。
* Data at Rest (保存されたデータ) の暗号化はこのチャートでは提供されません。  保存時ストレージ暗号化の構成は管理者の判断によります。

## バックアップおよびリカバリー

[バックアップおよびリカバリー](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.1/admin/backup_recovery.html)の手順に従います。

## 制限

* インストール制限: この製品は 1 回のみ、`kube-system` 名前空間にのみ、インストールできます。

## 資料

* 追加情報については、[インストール](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.1/hub/hub.html) Knowledge Center 資料を参照してください。

## 著作権

© Copyright IBM Corporation 2020. All Rights Reserved.
