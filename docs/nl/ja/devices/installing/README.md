# IBM Edge Computing Manager

## 概要

IBM Edge Computing Manager for Devices は、IoT デプロイメントで典型的な、エッジ・デバイスにデプロイされるアプリケーション向けに、エンドツーエンドの**アプリケーション管理プラットフォーム**を提供します。 このプラットフォームは、現場に配置された何千ものエッジ・デバイスでエッジ・ワークロードのリビジョンを安全にデプロイする作業を完全に自動化し、そういった作業からアプリケーション開発者を解放します。 アプリケーション開発者は、代わりに、個別にデプロイ可能な Docker コンテナーとしてアプリケーション・コードを任意のプログラミング言語で作成する作業に集中できます。 完全なビジネス・ソリューションをすべてのデバイスで Docker コンテナーのマルチレベル・オーケストレーションとして安全かつシームレスにデプロイするという負担をこのプラットフォームが担います。

## 前提条件

* Red Hat OpenShift Container Platform 4.2
* IBM Multicloud Management core 1.2
* 独自のデータベースをホストする場合、IBM Edge Computing Manager for Devices のコンポーネントのデータを保管するために、PostgreSQL の 2 つのインスタンスと、MongoDB の 1 つのインスタンスをプロビジョンしてください。 詳しくは、下の『**ストレージ**』セクションを参照してください
* インストールを駆動するための Ubuntu Linux または macOS ホスト。 以下のソフトウェアがインストールされている必要があります。
  * [Kubernetes CLI (kubectl)](https://kubernetes.io/docs/tasks/tools/install-kubectl/) バージョン 1.14.0 以降
  * [IBM Cloud Pak CLI (cloudctl)](https://www.ibm.com/support/knowledgecenter/SSFC4F_1.2.0/cloudctl/icp_cli.html)
  * [OpenShift CLI (oc)](https://docs.openshift.com/container-platform/4.2/cli_reference/openshift_cli/getting-started-cli.html)
  * [Helm CLI](https://helm.sh/docs/using_helm/#installing-the-helm-client) バージョン 2.9.1 以降
  * その他のソフトウェア・パッケージ:
    * jq
    * git
    * docker (バージョン 18.06.01 以降)
    * make

## Red Hat OpenShift SecurityContextConstraints の要件

デフォルトの `SecurityContextConstraints` (名前: [`restricted`](https://ibm.biz/cpkspec-scc)) がこのチャートのために検証済みです。 このリリースは、`kube-system` 名前空間へのデプロイメントに限定されていて、オプションのローカル・データベース・サブチャート用に独自のサービス・アカウントを作成することに加えて、`default` サービス・アカウントの両方を使用します。

## チャートの詳細

この helm チャートは、IBM Edge Computing Manager for Devices 認定コンテナーを OpenShift 環境にインストールして構成します。 以下のコンポーネントがインストールされます。

* IBM Edge Computing Manager for Devices - Exchange
* IBM Edge Computing Manager for Devices - AgBots
* IBM Edge Computing Manager for Devices - Cloud Sync Service (モデル管理システムの一部)
* IBM Edge Computing Manager for Devices - ユーザー・インターフェース (管理コンソール)

## 必要なリソース

必要なリソースについては、[インストール - サイジング](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.0/devices/installing/install.html#size)を参照してください。

## ストレージおよびデータベースの要件

IBM Edge Computing Manager for Devices のコンポーネントのデータを保管するために、3 つのデータベース・インスタンスが必要です。

デフォルトで、チャートは、以下に示す量でサイズ設定された 3 つのパーシスタント・データベースを、定義されたデフォルトの (またはユーザーが構成した) kubernetes 動的ストレージ・クラスを使用してインストールします。

**注:** これらのデフォルトのデータベースは、実動での使用を意図したものではありません。 独自の管理対象データベースを利用するには、下記の要件を参照し、『**リモート・データベースの構成**』セクションのステップに従ってください。

* PostgreSQL: Exchange データおよび AgBot データを保管します
  * それぞれが少なくとも 10 GB バイトのストレージを持つ 2 つの別々のインスタンスが必要です
  * インスタンスは少なくとも 100 の接続をサポートする必要があります
  * 実動使用の場合は、これらのインスタンスの可用性を高くする必要があります
* MongoDB: Cloud Sync Service データを保管します
  * 少なくとも 50 GB バイトのストレージを持つ 1 つのインスタンスが必要です。 **注:** 必要なサイズは、保管および使用するエッジ・サービス・モデルおよびファイルのサイズと数に大きく依存します。
  * 実動使用の場合は、このインスタンスの可用性を高くする必要があります

**注:** 独自の管理対象データベースを使用する場合、バックアップ/リストアの手順についてはお客様の責任です。
デフォルトのデータベース手順については、『**バックアップおよびリカバリー**』セクションを参照してください。

## リソースのモニター

IBM Edge Computing Manager for Devices がインストールされると、製品および製品が実行されるポッドのモニターが自動的にセットアップされます。 モニター・データは、管理コンソールの Grafana ダッシュボードの以下の場所で表示できます。

* `https://<MANAGEMENT_URL:PORT>/grafana/d/kube-system-edge-computing-overview/edge-computing-overview`
* `https://<MANAGEMENT_URL:PORT>/grafana/d/kube-system-edge-computing-pod-overview/edge-computing-pod-overview`

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
  name: edge-computing-remote-dbs
  labels:
    release: edge-computing
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
vi values.yaml   # or use your preferred editor
```

## チャートのインストール

**注:**

* これは CLI のみのインストールであり、GUI からのインストールはサポートされていません。

* [IBM Edge Computing Manager for Devices インフラストラクチャーのインストール - インストール・プロセス](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.0/devices/installing/install.html#process)のステップを既に完了している必要があります。
* インストールされた IBM Edge Computing Manager for Devices のインスタンスはクラスター当たり 1 つのみ存在でき、`kube-system` 名前空間にのみインストールできます。
* IBM Edge Computing Manager for Devices 3.2 からのアップグレードはサポートされていません。

IBM Edge Computing Manager for Devices をインストールするには、提供されているインストール・スクリプトを実行します。 このスクリプトによって実行される主なステップは、helm チャートのインストールと、インストール後の環境の構成 (Agbot、組織、およびパターン/ポリシーのサービスの作成) です。

```bash
ibm_cloud_pak/pak_extensions/full-install/install-edge-computing.sh
```

**注:** ネットワーク速度によっては、イメージをダウンロードし、ポッドが RUNNING 状態に移行し、すべてのサービスがアクティブになるまでに、数分かかります。

### チャートの検証

* 上記のスクリプトは、ポッドが実行中であり、Agbot と Exchange が応答していることを検証します。 インストールの終盤に「RUNNING」および「PASSED」メッセージを探してください。
* 「FAILED」の場合、出力には、特定のログで詳細情報を確認するようにという指示が示されます。
* 「PASSED」の場合、出力には、実行されたテストの詳細と、検証する必要のある他の 2 つの項目が示されます。
  * ログの末尾にある URL で IBM Edge Computing Manager UI コンソールを参照します。
    * `https://<MANAGEMENT_URL:PORT>/edge`

## インストール後

[インストール後の構成](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.0/devices/installing/install.html#postconfig)の手順に従います。

## チャートのアンインストール

**注:** 構成されたローカル・データベースと共にアンインストールする場合、**すべてのデータが削除されます**。 アンインストールの前にこのデータを保持したい場合は、下の『**バックアップ手順**』セクションを参照してください。

この README.md のロケーションに戻り、提供されているアンインストール・スクリプトを実行して、アンインストール・タスクを自動化します。 このスクリプトによってカバーされる主なステップは、helm チャートのアンインストールおよび秘密の削除です。 最初に、`cloudctl` を使用し、クラスター管理者としてクラスターにログインします。 その後、以下を実行します。

```bash
ibm_cloud_pak/pak_extensions/uninstall/uninstall-edge-computing.sh <cluster-name>
```

**注:** リモート・データベースをプロビジョンした場合、認証秘密は削除されますが、リモート・データベースからのデータの廃止/削除を行うためのタスクは実行されません。 データを削除したい場合は、この時点で行ってください。

## 役割ベースのアクセス権限

* この製品をインストールおよび管理するには、`kube-system` 名前空間内でのクラスター管理者権限が必要です。
* Exchange 認証および役割:
  * Exchange のすべての管理者およびユーザーの認証は、`cloudctl` コマンドで生成される API 鍵を通して IAM によって提供されます。
  * Exchange の管理者には、Exchange 内での `admin` 特権が付与される必要があります。 この特権を持っていると、管理者は自分の Exchange 組織内のすべてのユーザー、ノード、サービス、パターン、およびポリシーを管理できます。
  * Exchange の管理者以外のユーザーは、自分が作成したユーザー、ノード、サービス、パターン、およびポリシーのみを管理できます。

## セキュリティー

* Ingress を介して OpenShift クラスターへ出入りするすべてのデータに対して TLS が使用されます。 このリリースでは、OpenShift クラスター**内部**ではノード間の通信のために TLS は使用されません。 必要な場合、マイクロサービス間の通信用に Red Hat OpenShift サービス・メッシュを構成できます。 [Understanding Red Hat OpenShift Service Mesh](https://docs.openshift.com/container-platform/4.2/service_mesh/service_mesh_arch/understanding-ossm.html#understanding-ossm) を参照してください。
* Data at Rest (保存されたデータ) の暗号化はこのチャートでは提供されません。  ストレージ暗号化の構成は管理者の判断によります。

## バックアップおよびリカバリー

### バックアップ手順

これらのバックアップを保管するのに十分なスペースがある場所のクラスターに接続した後、以下のコマンドを実行します。


1. 下記のバックアップを保管するために使用されるディレクトリーを、必要に応じて調整して作成します。

```bash
export BACKUP_DIR=/tmp/edge-computing-backup/$(date +%Y%m%d_%H%M%S)
mkdir -p $BACKUP_DIR
```

2. 以下を実行して、認証/秘密をバックアップします。

```bash
oc -n kube-system get secret edge-computing -o yaml > $BACKUP_DIR/edge-computing-secret.yaml && \
oc -n kube-system get secret edge-computing-agbotdb-postgresql-auth-secret -o yaml > $BACKUP_DIR/edge-computing-agbotdb-postgresql-auth-secret-backup.yaml && \
oc -n kube-system get secret edge-computing-exchangedb-postgresql-auth-secret -o yaml > $BACKUP_DIR/edge-computing-exchangedb-postgresql-auth-secret-backup.yaml && \
oc -n kube-system get secret edge-computing-css-db-ibm-mongodb-auth-secret -o yaml > $BACKUP_DIR/edge-computing-css-db-ibm-mongodb-auth-secret-backup.yaml
```

3. 以下を実行して、データベースの内容をバックアップします。

```bash
oc -n kube-system exec edge-computing-exchangedb-keeper-0 -- bash -c "export PGPASSWORD=$(oc -n kube-system get secret edge-computing -o jsonpath="{.data.exchange-db-pass}" | base64 --decode) && pg_dump -U admin -h edge-computing-exchangedb-proxy-svc -F t postgres > /stolon-data/exchange-backup.tar" && \
oc -n kube-system cp edge-computing-exchangedb-keeper-0:/stolon-data/exchange-backup.tar $BACKUP_DIR/exchange-backup.tar
```

```bash
oc -n kube-system exec edge-computing-agbotdb-keeper-0 -- bash -c "export PGPASSWORD=$(oc -n kube-system get secret edge-computing -o jsonpath="{.data.agbot-db-pass}" | base64 --decode) && pg_dump -U admin -h edge-computing-agbotdb-proxy-svc -F t postgres > /stolon-data/agbot-backup.tar" && \
oc -n kube-system cp edge-computing-agbotdb-keeper-0:/stolon-data/agbot-backup.tar $BACKUP_DIR/agbot-backup.tar
```

```bash
oc -n kube-system exec edge-computing-cssdb-server-0 -- bash -c "mkdir -p /data/db/backup; mongodump -u admin -p $(oc -n kube-system get secret edge-computing -o jsonpath="{.data.css-db-pass}" | base64 --decode) --out /data/db/css-backup" && \
oc -n kube-system cp edge-computing-cssdb-server-0:/data/db/css-backup $BACKUP_DIR/css-backup
```

4. バックアップが検証されたら、ステートレス・コンテナーからバックアップを除去します。

```bash
oc -n kube-system exec edge-computing-exchangedb-keeper-0 -- bash -c "rm -f /stolon-data/exchange-backup.tar"
```

```bash
oc -n kube-system exec edge-computing-agbotdb-keeper-0 -- bash -c "rm -f /stolon-data/agbot-backup.tar"
```

```bash
oc -n kube-system exec edge-computing-cssdb-server-0 -- bash -c "rm -rf /data/db/css-backup"
```

### リストア手順

**注:** 新規クラスターにリストアする場合、そのクラスター名は、バックアップの作成元だったクラスターの名前と一致している必要があります。

1. 既存のすべての秘密をクラスターから削除します。
```bash
oc -n kube-system delete secret edge-computing edge-computing-agbotdb-postgresql-auth-secret edge-computing-exchangedb-postgresql-auth-secret edge-computing-css-db-ibm-mongodb-auth-secret;
```

2. これらの値をローカル・マシンにエクスポートします。

```bash
export BACKUP_DIR=/tmp/edge-computing-backup/<Insert desired backup datestamp YYYYMMDD_HHMMSS>
```

3. 以下を実行して、認証/秘密をリストアします。

```bash
oc apply -f $BACKUP_DIR
```

4. 『**チャートのインストール**』セクションの手順に従って、先に進む前に IBM Edge Computing Manager を再インストールします。

5. 以下を実行して、コンテナーにバックアップをコピーし、それらをリストアします。

```bash
oc -n kube-system cp $BACKUP_DIR/exchange-backup.tar edge-computing-exchangedb-keeper-0:/stolon-data/exchange-backup.tar && \
oc exec -n kube-system edge-computing-exchangedb-keeper-0 -- bash -c "export PGPASSWORD=$(oc get secret edge-computing -o jsonpath="{.data.exchange-db-pass}" | base64 --decode) && pg_restore -U admin -h edge-computing-exchangedb-proxy-svc -d postgres -c /stolon-data/exchange-backup.tar"
```

```bash
oc -n kube-system cp $BACKUP_DIR/agbot-backup.tar edge-computing-agbotdb-keeper-0:/stolon-data/agbot-backup.tar && \
oc exec -n kube-system edge-computing-agbotdb-keeper-0 -- bash -c "export PGPASSWORD=$(oc get secret edge-computing -o jsonpath="{.data.agbot-db-pass}" | base64 --decode) && pg_restore -U admin -h edge-computing-agbotdb-proxy-svc -d postgres -c /stolon-data/agbot-backup.tar"
```

```bash
oc -n kube-system cp $BACKUP_DIR/css-backup edge-computing-cssdb-server-0:/data/db/css-backup && \
oc exec -n kube-system edge-computing-cssdb-server-0 -- bash -c "mongorestore -u admin -p $(oc get secret edge-computing -o jsonpath="{.data.css-db-pass}" | base64 --decode) /data/db/css-backup";
```

6. 以下を実行して、kubernetes ポッドのデータベース接続をリフレッシュします。
```bash
for POD in $(oc get pods -n kube-system | grep -E '\-agbot\-|\-css\-|\-exchange\-' | awk '{print $1}'); do oc delete pod $POD -n kube-system; done
```

## 制限

* インストール制限: この製品は 1 回のみ、`kube-system` 名前空間にのみ、インストールできます。
* このリリースでは、製品の管理と製品の運用のための区別された許可特権はありません。

## 資料

* 追加のガイドラインおよび更新情報については、[インストール](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.1/devices/installing/install.html) Knowledge Center 資料を参照してください。

## 著作権

© Copyright IBM Corporation 2020. All Rights Reserved.
