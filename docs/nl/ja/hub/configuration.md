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

# {{site.data.keyword.ieam}} の構成

## EamHub カスタム・リソースの構成
{: #cr}

{{site.data.keyword.ieam}} のメインの構成は、EamHub カスタム・リソース (特に、このカスタム・リソースの **spec** フィールド) を使用して行います。

この資料では、以下を前提としています。
* これらのコマンドを実行する名前空間が、{{site.data.keyword.ieam}} 管理ハブ・オペレーターがデプロイされている場所にある。
* EamHub カスタム・リソース名がデフォルトの **ibm-edge** である。 これと異なる場合は、コマンド内の **ibm-edge** を置き換えてください。
* バイナリー **jq** がインストールされている。これにより、出力が可読形式で表示されるようになります。


定義されているデフォルトの **spec** は最小限の設定であり、ライセンスの受け入れのみが含まれています。これは以下を使用して表示できます。
```
$ oc get eamhub ibm-edge -o yaml
...
spec:
  license:
    accept: true
...
```

### オペレーター制御ループ
{: #loop}

{{site.data.keyword.ieam}} Management Hub オペレーターは、リソースの現在の状態をリソースの予期される状態に同期するために、連続したべき等ループで実行されます。

この連続ループのため、オペレーター管理対象リソースを構成する際には以下の 2 つの事項を理解しておく必要があります。
* カスタム・リソースに対する変更はすべて、制御ループによって非同期的に読み取られます。 変更を行った後に、その変更がオペレーターによって実施されるまでに数分かかることがあります。
* オペレーターが制御しているリソースに行った手動の変更はすべて、オペレーターが特定の状態を強制することで上書きされる (元に戻される) 可能性があります。 

以下のように、オペレーター・ポッドのログを監視して、このループを確認します。
```
oc logs $(oc get pods | grep ibm-eamhub-operator | awk '{print $1}') --tail 20 -f
```
{: codeblock}

ループが完了すると、**PLAY RECAP** の要約が生成されます。 最新の要約を表示するには、以下を実行します。
```
oc logs $(oc get pods | grep ibm-eamhub-operator | awk '{print $1}') --tail 5000 | grep -A 1 '^PLAY RECAP' | tail -n 1
```
{: codeblock}

以下は、操作が行われずに完了したループを示しています (現在の状態では、**PLAY RECAP** では常に **changed=1** と示されます)。
```
$ oc logs $(oc get pods | grep ibm-eamhub-operator | awk '{print $1}') --tail 5000 | grep -A 1 '^PLAY RECAP' | tail -n 1
localhost                  : ok=51   changed=1    unreachable=0    failed=0    skipped=11   rescued=0    ignored=0
```
{: codeblock}

構成変更を行う際に、以下の 3 つのフィールドを確認します。
* **changed**: **1** より大きい場合、1 つ以上のリソースの状態を変更するタスクがオペレーターによって実行されたことを示しています (これは、要求でカスタム・リソースを変更して行われるか、手動で行われた変更をオペレーターが元に戻すことによって発生する可能性があります)。
* **rescued**: タスクは失敗しましたが、既知の起こりうる失敗であったため、タスクは次のループで再試行されます。
* **failed**: 初期インストールで、予期される失敗が発生しています。同じ失敗が繰り返し表示され、メッセージが明らかでない (または表示されない) 場合、これは問題を示している可能性があります。

### EamHub の一般的な構成オプション

複数の構成変更を行うことができますが、変更される可能性の高いものと低いものがあります。 このセクションでは、より一般的な設定について説明します。

| 構成値 | デフォルト | 説明 |
| :---: | :---: | :---: |
| グローバル値 | -- | -- |
| pause_control_loop | false | デバッグ用に一時的な手動の変更を有効にするために、上記の制御ループを一時停止します。 定常状態では使用してはなりません。 |
| ieam_maintenance_mode | false | 永続ストレージのないすべてのポッド・レプリカの数を 0 に設定します。バックアップ修復のために使用されます。 |
| ieam_local_databases | true | ローカル・データベースを有効または無効にします。 状態の切り替えはサポートされません。 [リモート・データベース構成](./configuration.md#remote)を参照してください。 |
| ieam_database_HA | true | ローカル・データベースの HA モードを有効または無効にします。 これは、すべてのデータベース・ポッドのレプリカ数を **3** (**true** の場合) および **1** (**false** の場合) に設定します。 |
| hide_sensitive_logs | true | 設定 **Kubernetes Secrets** を扱うオペレーター・ログを非表示にします。**false** に設定されている場合、タスクが失敗すると、オペレーターはエンコードされた認証値をログに記録します。 |
| storage_class_name | "" | ストレージ・クラスが設定されていない場合にデフォルトのストレージ・クラスを使用します。 |
| ieam_enable_tls | false | {{site.data.keyword.ieam}} コンポーネント間のトラフィックのための内部 TLS を有効または無効にします。**注意:** Exchange、CSS、または Vault のデフォルト構成をオーバーライドする場合、構成オーバーライド内で TLS 構成を手動で変更する必要があります。|
| ieam_local_secrets_manager | true | ローカルのシークレット・マネージャー・コンポーネント (ボールト) を有効または無効にします。|


### EamHub コンポーネントのスケーリング構成オプション

| コンポーネント・スケーリング値 | デフォルトのレプリカ数 | 説明 |
| :---: | :---: | :---: |
| exchange_replicas | 3 | Exchange のレプリカのデフォルトの数。デフォルトの Exchange 構成 (exchange_config) をオーバーライドする場合、式 `((exchangedb_max_connections - 8) / exchange_replicas)` を使用して、**maxPoolSize** を手動で調整する必要があります。|
| css_replicas | 3 | CSS のレプリカのデフォルト数。|
| ui_replicas | 3 | UI のレプリカのデフォルトの数。|
| agbot_replicas | 2 | agbot のレプリカのデフォルトの数。デフォルトの agbot 構成 (agbot_config) をオーバーライドする場合、式 `((agbotdb_max_connections - 8) / agbot_replicas)` を使用して、**MaxOpenConnections** を手動で調整する必要があります。|


### EamHub コンポーネントのリソース構成オプション

**注:** Ansible オペレーターでは、ネストされたディクショナリー全体を追加する必要があるため、ネストされた構成値を全体で追加する必要があります。[スケーリング構成](./configuration.md#scale)の例を参照してください。

<table>
<tr>
<td> コンポーネント・リソース値</td> <td> デフォルト </td> <td> 説明 </td>
</tr>
<tr>
<td> exchange_resources </td> 
<td>

```
  exchange_resources:
    requests:
      memory: 512Mi
      cpu: 10m
    limits:
      memory: 2Gi
      cpu: 2
```

</td>
<td>
Exchange のデフォルトの要求および制限。
</td>
</tr>
<tr>
<td> agbot_resources </td> 
<td>

```
  agbot_resources:
    requests:
      memory: 64Mi
      cpu: 10m
    limits:
      memory: 2Gi
      cpu: 2
```

</td>
<td>
agbot のデフォルトの要求および制限。
</td>
</tr>
<tr>
<td> css_resources </td> 
<td>

```
  css_resources:
    requests:
      memory: 64Mi
      cpu: 10m
    limits:
      memory: 2Gi
      cpu: 2
```

</td>
<td>
CSS のデフォルトの要求および制限。
</td>
</tr>
<tr>
<td> sdo_resources </td> 
<td>

```
  sdo_resources:
    requests:
      memory: 1024Mi
      cpu: 10m
    limits:
      memory: 2Gi
      cpu: 2
```

</td>
<td>
SDO のデフォルトの要求および制限。
</td>
</tr>
<tr>
<td> ui_resources </td> 
<td>

```
  ui_resources:
    requests:
      memory: 64Mi
      cpu: 10m
    limits:
      memory: 2Gi
      cpu: 2
```

</td>
<td>
UI のデフォルトの要求および制限。
</td>
</tr>
<tr>
<td> vault_resources </td> 
<td>

```
  vault_resources:
    requests:
      memory: 1024Mi
      cpu: 10m
    limits:
      memory: 2Gi
      cpu: 2
```

</td>
<td>
シークレット・マネージャーのデフォルトの要求および制限。
</td>
</tr>
<tr>
<td> mongo_resources </td> 
<td>

```
  mongo_resources:
    limits:
      cpu: 2
      memory: 2Gi
    requests:
      cpu: 100m
      memory: 256Mi
```

</td>
<td>
CSS Mongo データベースのデフォルトの要求および制限。
</td>
</tr>
<tr>
<td> postgres_exchangedb_sentinel </td> 
<td>

```
  postgres_exchangedb_sentinel:
    resources:
      requests:
        cpu: "100m"
        memory: "256Mi"
      limits:
        cpu: 1
        memory: 1Gi
```

</td>
<td>
Exchange postgres sentinel のデフォルトの要求および制限。
</td>
</tr>
<tr>
<td> postgres_exchangedb_proxy </td> 
<td>

```
  postgres_exchangedb_proxy:
    resources:
      requests:
        cpu: "100m"
        memory: "256Mi"
      limits:
        cpu: 1
        memory: 1Gi
```

</td>
<td>
Exchange postgres proxy のデフォルトの要求および制限。
</td>
</tr>
<tr>
<td> postgres_exchangedb_keeper </td> 
<td>

```
  postgres_exchangedb_keeper:
    resources:
      requests:
        cpu: "100m"
        memory: "256Mi"
      limits:
        cpu: 2
        memory: 2Gi
```

</td>
<td>
Exchange postgres keeper のデフォルトの要求および制限。
</td>
</tr>
<tr>
<td> postgres_agbotdb_sentinel </td> 
<td>

```
  postgres_agbotdb_sentinel:
    resources:
      requests:
        cpu: "100m"
        memory: "256Mi"
      limits:
        cpu: 1
        memory: 1Gi
```

</td>
<td>
agbot postgres sentinel のデフォルトの要求および制限。
</td>
</tr>
<tr>
<td> postgres_agbotdb_proxy </td> 
<td>

```
  postgres_agbotdb_proxy:
    resources:
      requests:
        cpu: "100m"
        memory: "256Mi"
      limits:
        cpu: 1
        memory: 1Gi
```

</td>
<td>
agbot postgres proxy のデフォルトの要求および制限。
</td>
</tr>
<tr>
<td> postgres_agbotdb_keeper </td> 
<td>

```
  postgres_agbotdb_keeper:
    resources:
      requests:
        cpu: "100m"
        memory: "256Mi"
      limits:
        cpu: 2
        memory: 2Gi
```

</td>
<td>
agbot postgres keeper のデフォルトの要求および制限。
</td>
</tr>
</table>

### EamHub ローカル・データベースのサイズ構成オプション

| コンポーネント構成値 | デフォルトの永続ボリューム・サイズ | 説明 |
| :---: | :---: | :---: |
| postgres_exchangedb_storage_size | 20Gi | postgres exchange データベースのサイズ。|
| postgres_agbotdb_storage_size | 20Gi | postgres agbot データベースのサイズ。|
| mongo_cssdb_storage_size | 20Gi | mongo CSS データベースのサイズ。|

## Exchange API 翻訳構成

特定の言語で応答を返すように {{site.data.keyword.ieam}} exchange API を構成できます。 これを行うには、サポートされている任意の **LANG** を使用して環境変数を定義します (デフォルトは **en**)。

```
oc set env deployment <CUSTOM_RESOURCE_NAME>-exchange HZN_EXCHANGE_LANG=<LANG>
```
{: codeblock}

**注:** サポートされている言語コードのリストは、[「サポートされる言語」](../getting_started/languages.md)ページの最初の表を参照してください。

## リモート・データベース構成
{: #remote}

**注**: リモート・データベースとローカル・データベースの切り替えはサポートされていません。

リモート・データベースを使用してインストールする場合は、インストール時に、**spec** フィールドで追加の値を指定して EamHub カスタム・リソースを作成します。
```
spec:
  ieam_local_databases: false
  license:
    accept: true
```
{: codeblock}

以下のテンプレートに入力して、認証の秘密を作成します。必ず各コメントを読み、正確に入力されていることを確認し、**edge-auth-overrides.yaml** に保存してください。
```
apiVersion: v1
kind: Secret
metadata:
  # NOTE: The name -must- be prepended by the name given to your Custom Resource, this defaults to 'ibm-edge'
  #name: <CR_NAME>-auth-overrides
  name: ibm-edge-auth-overrides
type: Opaque
stringData:
  # agbot postgresql connection settings uncomment and replace with your settings to use
  agbot-db-host: "<Single hostname of the remote database>"
  agbot-db-port: "<Single port the database runs on>"
  agbot-db-name: "<The name of the database to utilize on the postgresql instance>"
  agbot-db-user: "<Username used to connect>"
  agbot-db-pass: "<Password used to connect>"
  agbot-db-ssl: "<disable|require|verify-full>"
  # Ensure proper indentation (four spaces)
  agbot-db-cert: |-
    -----BEGIN CERTIFICATE-----
    ....
    -----END CERTIFICATE-----

  # exchange postgresql connection settings
  exchange-db-host: "<Single hostname of the remote database>"
  exchange-db-port: "<Single port the database runs on>"
  exchange-db-name: "<The name of the database to utilize on the postgresql instance>"
  exchange-db-user: "<Username used to connect>"
  exchange-db-pass: "<Password used to connect>"
  exchange-db-ssl: "<disable|require|verify-full>"
  # Ensure proper indentation (four spaces)
  exchange-db-cert: |-
    -----BEGIN CERTIFICATE-----
    ....
    -----END CERTIFICATE-----

  # css mongodb connection settings
  css-db-host: "<Comma separated list including ports: hostname.domain:port,hostname2.domain:port2 >"
  css-db-name: "<The name of the database to utilize on the mongodb instance>"
  css-db-user: "<Username used to connect>"
  css-db-pass: "<Password used to connect>"
  css-db-auth: "<The name of the database used to store user credentials>"
  css-db-ssl: "<true|false>"
  # Ensure proper indentation (four spaces)
  css-db-cert: |-
    -----BEGIN CERTIFICATE-----
    ....
    -----END CERTIFICATE-----
```
{: codeblock}

次のようにシークレットを作成します。
```
oc apply -f edge-auth-overrides.yaml
```
{: codeblock}

『[オペレーター制御ループ](./configuration.md#remote)』セクションで説明されているように、オペレーター・ログを監視します。


## スケーリング構成
{: #scale}

EamHub カスタム・リソース構成は、多数のエッジ・ノードをサポートするために {{site.data.keyword.ieam}} Management Hub のポッドへのリソースを増やすのに必要になることがある構成パラメーターを公開します。
お客様は、{{site.data.keyword.ieam}} ポッド、特に Exchange および同意ボット (agbot) のリソース消費量をモニターして、必要に応じてリソースを追加する必要があります。[{{site.data.keyword.ieam}} Grafana ダッシュボードへのアクセス](../admin/monitoring.md)を参照してください。
OpenShift プラットフォームは、これらの更新を認識し、{{site.data.keyword.ocp}} の下で実行されている {{site.data.keyword.ieam}} ポッドに自動的に適用します。

制限

IBM では、デフォルトのリソース割り振りを使用し、{{site.data.keyword.ieam}} ポッド間の内部 TLS を無効にした状態で、40,000 サービス・インスタンスを受け取る最大 40,000 の登録済みエッジ・ノードでテストしました。これらのインスタンスは、デプロイされたサービスの 25% (つまり 10,000) に影響するデプロイメント・ポリシー更新を使用してデプロイされています。

40,000 の登録済みエッジ・ノードをサポートするには、{{site.data.keyword.ieam}} ポッド間の内部 TLS が有効になっている場合、Exchange ポッドは追加 CPU リソースを必要とします。
EamHub カスタム・リソース構成で以下の変更を行います。

**spec** の下に以下のセクションを追加します。

```
spec:
  exchange_resources:
    requests:
      memory: 512Mi
      cpu: 10m
    limits:
      memory: 2Gi
      cpu: 5
```
{: codeblock}

90,000 より多いサービス・デプロイメントをサポートするには、EamHub カスタム・リソース構成で以下の変更を行います。

**spec** の下に以下のセクションを追加します。

```
spec:
  agbot_resources:
    requests:
      memory: 1Gi
      cpu: 10m
    limits:
      memory: 4Gi
      cpu: 2
```
{: codeblock}

