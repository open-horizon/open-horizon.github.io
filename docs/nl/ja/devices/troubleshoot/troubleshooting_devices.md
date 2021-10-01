---

copyright:
years: 2019
lastupdated: "2019-06-28"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# トラブルシューティングのヒント
{: #troubleshooting_devices}

{{site.data.keyword.edge_devices_notm}} で問題が発生した場合は、以下の質問を確認してください。 各質問のヒントとガイドは、一般的な問題の解決と根本原因の特定のための情報取得に役立ちます。
{:shortdesc}

  * [現在リリースされているバージョンの {{site.data.keyword.horizon}} パッケージはインストールされていますか?](#install_horizon)
  * [{{site.data.keyword.horizon}} エージェントは現在、アクティブに稼働中ですか?](#setup_horizon)
  * [エッジ・ノードは {{site.data.keyword.horizon_exchange}} と対話するように構成されていますか?](#node_configured)
  * [エッジ・ノードの実行に必要な Docker コンテナーは開始されていますか?](#node_running)
  * [予期されたサービス・コンテナー・バージョンは実行中ですか?](#run_user_containers)
  * [予期されたコンテナーは安定していますか?](#containers_stable)
  * [Docker コンテナーは正しくネットワーク化されていますか?](#container_networked)
  * [コンテナーのコンテキスト内で依存関係コンテナーにアクセス可能ですか?](#setup_correct)
  * [ユーザー定義コンテナーはエラー・メッセージをログに出力していますか?](#log_user_container_errors)
  * [組織の {{site.data.keyword.message_hub_notm}} Kafka ブローカーのインスタンスを使用できますか?](#kafka_subscription)
  * [コンテナーは {{site.data.keyword.horizon_exchange}} にパブリッシュされていますか?](#publish_containers)
  * [パブリッシュされたデプロイメント・パターンには、必要なすべてのサービスとバージョンが含まれていますか?](#services_included)
  * [{{site.data.keyword.open_shift_cp}} 環境に固有のトラブルシューティングのヒント](#troubleshooting_icp)
  * [ノード・エラーのトラブルシューティング](#troubleshooting_node_errors)

## 現在リリースされているバージョンの {{site.data.keyword.horizon}} パッケージはインストールされていますか?
{: #install_horizon}

エッジ・ノードにインストールされている {{site.data.keyword.horizon}} ソフトウェアは常に最新のリリース済みバージョンであるようにします。

{{site.data.keyword.linux_notm}} システムでは、通常、以下のコマンドを実行することによって、インストール済みの  {{site.data.keyword.horizon}} パッケージのバージョンを確認できます。  
```
dpkg -l | grep horizon
```
{: codeblock}

ご使用のシステムでパッケージ・マネージャーを使用する {{site.data.keyword.horizon}} パッケージを更新できます。 例えば、Ubuntu ベースの {{site.data.keyword.linux_notm}} システムでは、以下のコマンドを使用して {{site.data.keyword.horizon}} を現行バージョンに更新します。
```
sudo apt update
sudo apt install -y blue horizon
```

## {{site.data.keyword.horizon}} エージェントはアクティブに稼働中ですか?
{: #setup_horizon}

次の {{site.data.keyword.horizon}} CLI コマンドを使用して、エージェントが実行中であることを確認できます。
```
hzn node list | jq .
```
{: codeblock}

ホストのシステム管理ソフトウェアを使用して、{{site.data.keyword.horizon}} エージェントの状況を確認することもできます。 例えば、Ubuntu ベースの {{site.data.keyword.linux_notm}} システムの場合は、`systemctl` ユーティリティーを使用できます。
```
sudo systemctl status horizon
```
{: codeblock}

エージェントがアクティブである場合、以下のような行が表示されます。
```
Active: active (running) since Fri 2018-09-02 15:00:04 UTC; 2h 29min ago
```
{: codeblock}

## エッジ・ノードは {{site.data.keyword.horizon_exchange}} と対話するように構成されていますか? 
{: #node_configured}

{{site.data.keyword.horizon_exchange}} と通信できることを確認するには、次のコマンドを実行します。
```
hzn exchange version
```
{: codeblock}

{{site.data.keyword.horizon_exchange}} が受け入れられていることを確認するには、次のコマンドを実行します。
```
hzn exchange user list
```
{: codeblock}

エッジ・ノードが {{site.data.keyword.horizon}} に登録された後、ローカル {{site.data.keyword.horizon}} エージェント構成を表示することによって、そのノードが {{site.data.keyword.horizon_exchange}} と対話しているかどうかを確認できます。 次のコマンドを実行して、エージェント構成を表示します。
```
hzn node list | jq .configuration.exchange_api
```
{: codeblock}

## エッジ・ノードに必要な Docker コンテナーは実行中ですか?
{: #node_running}

エッジ・ノードが {{site.data.keyword.horizon}} に登録されている場合、{{site.data.keyword.horizon}} Agbot が、ゲートウェイ・タイプ (デプロイメント・パターン) で参照されるサービスを実行するためにエッジ・ノードとの合意を形成します。 合意が形成されない場合は、以下の確認を行い問題のトラブルシューティングを実行します。

エッジ・ノードが `configured` 状態にあり、正しい `id` および `organization` の値が設定されていることを確認します。 また、{{site.data.keyword.horizon}} が報告しているアーキテクチャーが、ご使用のサービスのメタデータで使用したアーキテクチャーと同じアーキテクチャーであることを確認します。 これらの設定をリストするために、以下のコマンドを実行します。
```
hzn node list | jq .
```
{: codeblock}

これらの値が予期どおりのものである場合は、次のコマンドを実行してエッジ・ノードの合意状況を確認できます。 
```
hzn agreement list -r | jq .
```
{: codeblock}

このコマンドで合意が表示されない場合、それらの合意は形成された可能性がありますが、問題が検出された可能性があります。 この問題が発生した場合、前のコマンドからの出力に表示される前に、その合意を取り消すことができます。 合意の取り消しが実施されると、取り消された合意はアーカイブ済み合意のリスト内に `terminated_description` という状況で表示されます。 アーカイブ済みリストを表示するには、次のコマンドを実行します。 
```
hzn agreement list -r | jq .
```
{: codeblock}

合意が形成される前に問題が発生する場合もあります。 この問題が発生した場合は、{{site.data.keyword.horizon}} エージェントのイベント・ログを確認して、可能性があるエラーを特定してください。 ログを表示するには、次のコマンドを実行します。 
```
hzn eventlog list
``` 
{: codeblock}

イベント・ログには、以下のものが含まれています。 

* サービス・メタデータのシグニチャー (特に `deployment` フィールド) を検証できません。 このエラーは、通常は署名公開鍵がエッジ・ノードにインポートされていないことを意味します。 この鍵は、`hzn key import -k <pubkey>` コマンドを使用してインポートできます。 `hzn key list` コマンドを使用すると、ローカル・エッジ・ノードにインポートされた鍵を表示できます。 次のコマンドを使用すると、{{site.data.keyword.horizon_exchange}} のサービス・メタデータがご使用の鍵で署名されたことを確認できます。
  ```
  hzn exchange service verify -k $PUBLIC_KEY_FILE <service-id>
  ```
  {: codeblock} 

`<service-id>` をサービスの ID に置き換えます。 この ID は `workload-cpu2wiotp_${CPU2WIOTP_VERSION}_${ARCH2}` のような形式になります。

* サービス `deployment` フィールドの Docker イメージのパスが正しくありません。 エッジ・ノードでそのイメージ・パスに対して `docker pull` を実行できることを確認します。
* エッジ・ノード上の {{site.data.keyword.horizon}} エージェントが、Docker イメージを保持する Docker レジストリーにはアクセスできません。 リモート Docker レジストリー内の Docker イメージが、全ユーザー読み取り可能ではない場合は、`docker login` コマンドを使用してエッジ・ノードに資格情報を追加する必要があります。 資格情報がエッジ・ノード上に記憶されるように、このステップは 1 回実行する必要があります。
* コンテナーが継続して再始動する場合は、コンテナー・ログで詳細を確認してください。 `docker ps` コマンドを実行したときに、コンテナーがわずか数秒しかリストされていない場合、または再始動中としてリストされた状態で残っている場合は、そのコンテナーは継続して再始動する可能性があります。 以下のコマンドを実行して、コンテナー・ログで詳細を確認できます。
  ```
  grep --text -E ' <service>\[[0-9]+\]' /var/log/syslog
  ```
  {: codeblock}

## 予期されたサービス・コンテナー・バージョンは実行中ですか?
{: #run_user_containers}

コンテナー・バージョンは、サービスをデプロイメント・パターンに追加した後、そしてそのパターンのエッジ・ノードを登録した後に形成される合意によって管理されます。 次のコマンドを実行して、ご使用のパターンの現在の合意がエッジ・ノードにあることを確認します。

```
hzn agreement list | jq .
```
{: codeblock}

パターンに対する正しい合意を確認した場合は、次のコマンドを使用して実行中のコンテナーを表示します。 ユーザー定義のコンテナーがリストされ、実行中であることを確認します。
```
docker ps
```
{: codeblock}

{{site.data.keyword.horizon}} エージェントでは、合意が受け入れられた後、対応するコンテナーがダウンロードされ、検査されて実行を開始するまでに数分間かかることがあります。 この合意は、ほとんどの場合、リモート・リポジトリーからプルする必要があるコンテナー自体のサイズによって異なります。

## 予期されたコンテナーは安定していますか?
{: #containers_stable}

コンテナーが安定していることを確認するために、次のコマンドを実行します。
```
docker ps
```
{: codeblock}

コマンド出力では、各コンテナーが実行している期間を確認できます。 時間が経過して、コンテナーが予期せず再始動していることが見られた場合、コンテナー・ログでエラーがないか確認します。

開発のベスト・プラクティスとして、以下のコマンドを実行して個別のサービス・ロギングを構成することを検討してください ({{site.data.keyword.linux_notm}} システムのみ):
```bash
cat <<'EOF' > /etc/rsyslog.d/10-horizon-docker.conf
$template DynamicWorkloadFile,"/var/log/workload/%syslogtag:R,ERE,1,DFLT:.*workload-([^\[]+)--end%.log"

:syslogtag, startswith, "workload-" -?DynamicWorkloadFile
& stop
:syslogtag, startswith, "docker/" -/var/log/docker_containers.log
& stop
:syslogtag, startswith, "docker" -/var/log/docker.log
& stop
EOF
service rsyslog restart
```
{: codeblock}

前のステップを完了すると、コンテナーのログが `/var/log/workload/` ディレクトリー内の個別のファイル内に記録されます。 `docker ps` コマンドを使用して、コンテナーの絶対パス名を検索します。 このディレクトリー内では末尾に `.log` が付いた、その名前のログ・ファイルが見つかります。

個別のサービス・ロギングが構成されていない場合、サービスは、他のすべてのログ・メッセージとともにシステム・ログに記録されます。 コンテナーのデータを確認するには、`/var/log/syslog/` ファイル内のシステム・ログ出力でコンテナー名を検索する必要があります。 例えば、次のようなコマンドを実行して、ログを検索できます。
```
grep --text -E 'YOURSERVICENAME\[[0-9]+\]' /var/log/syslog
```
{: codeblock}

## コンテナーは、Docker で正しくネットワーク化されていますか?
{: #container_networked}

コンテナーから必要なサービスにアクセスできるようにするために、コンテナーが Docker で適切にネットワーク化されていることを確認してください。 次のコマンドを実行して、エッジ・ノード上でアクティブになっている Docker 仮想ネットワークを確認できるようにします。
```
docker network list
```
{: codeblock}

ネットワークの詳細を表示するには、`docker inspect X` コマンドを使用します。ここで `X` はネットワークの名前です。 このコマンド出力では、仮想ネットワーク上で実行されるすべてのコンテナーをリストします。

各コンテナーで `docker inspect Y` コマンドを実行することもできます。ここで `Y` は詳細情報を確認するコンテナーの名前です。 例えば、`NetworkSettings` コンテナー情報を参照し、`Networks` コンテナーを検索します。 このコンテナー内で、関連するネットワーク ID ストリングおよびネットワーク上でのコンテナーの表示方法に関する情報を参照できます。 この表示情報には、コンテナーの `IPAddress`、およびこのネットワーク上にあるネットワーク別名のリストが含まれます。 

別名は、この仮想ネットワーク上のすべてのコンテナーで使用可能です。これらの名前は、通常は仮想ネットワーク上の他のコンテナーをディスカバーするために、コード・デプロイメント・パターン内のコンテナーによって使用されます。 例えば、サービスに `myservice` と名前を付けると、他のコンテナーは (コマンド `ping myservice` などで) その名前を直接使用してネットワーク上でそのサービスにアクセスすることができます。 コンテナーの別名は、 `hzn exchange service publish` コマンドに渡したサービス定義ファイルの `deployment` フィールドに指定されています。

Docker コマンド・ライン・インターフェースでサポートされるコマンドについて詳しくは、[Docker コマンド参照![新しいタブで開く](../../images/icons/launch-glyph.svg "新しいタブで開く")](https://docs.docker.com/engine/reference/commandline/docker/#child-commands)を参照してください。

## コンテナーのコンテキスト内で依存関係コンテナーにアクセス可能ですか?
{: #setup_correct}

`docker exec` コマンドを使用して、実行中のコンテナーのコンテキストを入力して、実行時の問題をトラブルシューティングすることができます。 `docker ps` コマンドを使用して実行中のコンテナーの ID を検索してから、次のようなコマンドを使用してコンテキストを入力します。 `CONTAINERID` をコンテナーの ID に置き換えます。
```
docker exec -it CONTAINERID /bin/sh
```
{: codeblock}

ご使用のコンテナーに bash が含まれている場合は、前のコマンドの最後に `/bin/sh` ではなく `/bin/bash` を指定することをお勧めします。

コンテナー・コンテキスト内では、`ping` や `curl` のようなコマンドを使用して、必要なコンテナーと対話し、接続を検証することができます。

Docker コマンド・ライン・インターフェースでサポートされるコマンドについて詳しくは、[Docker コマンド参照![新しいタブで開く](../../images/icons/launch-glyph.svg "新しいタブで開く")](https://docs.docker.com/engine/reference/commandline/docker/#child-commands)を参照してください。

## ユーザー定義コンテナーはエラー・メッセージをログに出力していますか?
{: #log_user_container_errors}

個別のサービス・ロギングを構成している場合、各コンテナーは `/var/log/workload/` ディレクトリー内の個別のファイルにログインします。 `docker ps` コマンドを使用して、コンテナーの絶対パス名を検索します。 そして、このディレクトリー内で、その名前で、末尾に `.log` が付いたファイルを探します。

個別のサービス・ロギングが構成されていない場合、サービスは、他のすべての詳細情報を含むシステム・ログに記録されます。 データを確認するには、`/var/log/syslog` ディレクトリー内のシステム・ログ出力でコンテナー・ログを検索します。 例えば、次のようなコマンドを実行して、ログを検索します。
```
grep --text -E 'YOURSERVICENAME\[[0-9]+\]' /var/log/syslog
```
{: codeblock}

## 組織の {{site.data.keyword.message_hub_notm}} Kafka ブローカーのインスタンスを使用できますか?
{: #kafka_subscription}

{{site.data.keyword.message_hub_notm}} から組織の Kafka インスタンスへのサブスクライブは、Kafka ユーザー資格情報が正しいことを確認する場合に役立ちます。 また、このサブスクリプションは、ご使用の Kafka サービス・インスタンスがクラウドで実行されていること、およびデータがパブリッシュされる場合にエッジ・ノードがデータを送信していることを確認する場合にも役立ちます。

Kafka ブローカーにサブスクライブするには、`kafkacat` プログラムをインストールします。 例えば、Ubuntu {{site.data.keyword.linux_notm}} システムでは、次のコマンドを使用します。

```bash
sudo apt install kafkacat
```
{: codeblock}

インストール後は以下の例のようなコマンドを使用してサブスクライブできます。このコマンドでは、通常、環境変数参照に挿入する資格情報を使用します。

```bash
kafkacat -C -q -o end -f "%t/%p/%o/%k: %s\n" -b $EVTSTREAMS_BROKER_URL -X api.version.request=true -X security.protocol=sasl_ssl -X sasl.mechanisms=PLAIN -X sasl.username=token -X sasl.password=$EVTSTREAMS_API_KEY -t $EVTSTREAMS_TOPIC
```
{: codeblock}

ここで `EVTSTREAMS_BROKER_URL` は Kafka ブローカーの URL、`EVTSTREAMS_TOPIC` は Kafka トピック、そして `EVTSTREAMS_API_KEY` は、{{site.data.keyword.message_hub_notm}} API で認証するための API 鍵です。

サブスクリプション・コマンドが正常に実行されると、このコマンドは無期限にブロックされます。 コマンドは、Kafka ブローカーへのパブリッシュを待機して、結果のメッセージをすべて取得して表示します。 数分たってもにエッジ・ノードからメッセージが表示されない場合は、サービス・ログにエラー・メッセージないかを調べてください。

例えば、`cpu2evtstreams` サービスのログを確認するには、次のコマンドを実行します。

* {{site.data.keyword.linux_notm}} および {{site.data.keyword.windows_notm}} の場合 

```bash
tail -n 500 -f /var/log/syslog | grep -E 'cpu2evtstreams\[[0-9]+\]:'
```
{: codeblock}

* macOS の場合

```bash
docker logs -f $(docker ps --filter 'name=-cpu2evtstreams' | tail -n +2 | awk '{print $1}')
```
{: codeblock}

## コンテナーは {{site.data.keyword.horizon_exchange}} にパブリッシュされていますか?
{: #publish_containers}

{{site.data.keyword.horizon_exchange}} は、エッジ・ノード用にパブリッシュされるコードに関するメタデータの中心的なウェアハウスです。 コードに署名しておらず、コードを {{site.data.keyword.horizon_exchange}} にパブリッシュしていない場合は、そのコードをエッジ・ノードにプルすること、コードを検証すること、およびコードを実行することはできません。

以下の引数を設定して `hzn` コマンドを実行し、パブリッシュされたコードのリストを表示して、サービス・コンテナーすべてが正常にパブリッシュされたことを確認します。

```
hzn exchange service list | jq .
hzn exchange service list $ORG_ID/$SERVICE | jq .
```
{: codeblock}

パラメーター `$ORG_ID` は組織 ID で、`$SERVICE` は、ユーザーが情報を取得するサービスの名前です。

## パブリッシュされたデプロイメント・パターンには、必要なすべてのサービスとバージョンが含まれていますか?
{: #services_included}

`hzn` コマンドがインストールされているマシンでは、このコマンドを使用して任意のデプロイメント・パターンに関する詳細情報を取得できます。 以下の引数を指定して hzn コマンドを実行し、デプロイメント・パターンのリストを {{site.data.keyword.horizon_exchange}} からプルします。 

```
hzn exchange pattern list | jq .
hzn exchange pattern list $ORG_ID/$PATTERN | jq .
```
{: codeblock}

パラメーター `$ORG_ID` は組織 ID で、`$PATTERN` は、ユーザーが情報を取得するデプロイメント・パターンの名前です。

## {{site.data.keyword.open_shift_cp}} 環境に固有のトラブルシューティングのヒント
{: #troubleshooting_icp}

{{site.data.keyword.edge_devices_notm}} に関連する {{site.data.keyword.open_shift_cp}} 環境の一般的な問題のトラブルシューティングを行う際は、以下の内容を確認してください。 これらのヒントは、一般的な問題の解決と根本原因の特定のための情報取得に役立ちます。
{:shortdesc}

### ユーザーの {{site.data.keyword.edge_devices_notm}} 資格情報は、{{site.data.keyword.open_shift_cp}} 環境で使用できるように正しく構成されていますか?
{: #setup_correct}

この環境で {{site.data.keyword.edge_devices_notm}} の任意のアクションを実行するには、{{site.data.keyword.open_shift_cp}} ユーザー・アカウントが必要です。 また、そのアカウントから作成された API 鍵も必要です。

この環境で {{site.data.keyword.edge_devices_notm}} 資格情報を確認するには、次のコマンドを実行します。

   ```
   hzn exchange user list
   ```
   {: codeblock}

Exchange から返された JSON 形式の項目に 1 人以上のユーザーが示されている場合、{{site.data.keyword.edge_devices_notm}} 資格情報は適切に構成されています。

エラー応答が返された場合は、資格情報のセットアップをトラブルシューティングするためのステップを行います。

エラー・メッセージが正しくない API 鍵を示している場合は、以下のコマンドを使用する新しい API 鍵を作成できます。

[必要な情報とファイルの収集](../developing/software_defined_radio_ex_full.md#prereq-horizon)を参照してください。

## ノード・エラーのトラブルシューティング
{: #troubleshooting_node_errors}

{{site.data.keyword.edge_devices_notm}} は、{{site.data.keyword.gui}} で表示可能なイベント・ログのサブセットを Exchange に公開します。 これらのエラーは、トラブルシューティングのガイダンスにリンクされています。
{:shortdesc}

  - [イメージのロードでのエラー](#eil)
  - [デプロイメント構成エラー](#eidc)
  - [コンテナー開始エラー](#esc)

### イメージのロードでのエラー
{: #eil}

このエラーは、サービス定義で参照されているサービス・イメージがイメージ・リポジトリーに存在しない場合に発生します。 このエラーを解決するには、以下のようにします。

1. **-I** フラグを付けずにサービスをリパブリッシュします。
    ```
    hzn exchange service publish -f <service-definition-file>
    ```
    {: codeblock}

2. サービス・イメージをイメージ・リポジトリーに直接プッシュします。 
    ```
    docker push <image name>
    ```
    {: codeblock} 
    
### デプロイメント構成エラー
{: #eidc}

このエラーは、サービス定義のデプロイメント構成で、ルート保護ファイルへのバインドが指定されている場合に発生します。 このエラーを解決するには、以下のようにします。

1. コンテナーをルート保護されていないファイルにバインドします。
2. ファイルのアクセス権を変更して、ユーザーがファイルを読み書きできるようにします。

### コンテナー開始エラー
{: #esc}

このエラーは、Docker がサービス・コンテナーを開始したときにエラーを検出した場合に発生します。 エラー・メッセージには、コンテナーの開始が失敗した理由を示す詳細が含まれていることがあります。 エラーの解決ステップは、エラーによって異なります。 以下のエラーが発生することがあります。

1. デバイスは、デプロイメント構成によって指定された公開ポートを既に使用しています。 エラーを解決するには、次のようにします。 

    - サービス・コンテナー・ポートに別のポートをマップします。 表示されたポート番号は、サービス・ポート番号と一致する必要はありません。
    - 同じポートを使用しているプログラムを停止します。

2. デプロイメント構成で指定された公開ポートのポート番号が有効ではありません。 ポート番号は、1 から 65535 の範囲の数値でなければなりません。
3. デプロイメント構成のボリューム名は、有効なファイル・パスではありません。 ボリューム・パスは、(相対パスではなく) 絶対パスで指定する必要があります。 

### 追加情報

詳しくは、以下を参照してください。
  * [トラブルシューティング](../troubleshoot/troubleshooting.md)
