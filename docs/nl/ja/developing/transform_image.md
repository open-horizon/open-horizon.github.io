---

copyright:
years: 2020
lastupdated: "2020-04-09"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# エッジ・サービスへのイメージの変換
{: #transform_image}

このサンプルは、既存の Docker イメージをエッジ・サービスとして公開し、関連するデプロイメント・パターンを作成し、そのデプロイメント・パターンを実行するエッジ・ノードを登録するステップを示します。
{:shortdesc}

## 始める前に
{: #quickstart_ex_begin}

[エッジ・サービス作成の準備](service_containers.md)の前提条件ステップを実行してください。 その結果、以下の環境変数が設定され、以下のコマンドがインストールされ、以下のファイルが存在していなければなりません。

```bash
echo "HZN_ORG_ID=$HZN_ORG_ID, HZN_EXCHANGE_USER_AUTH=$HZN_EXCHANGE_USER_AUTH, DOCKER_HUB_ID=$DOCKER_HUB_ID"
which git jq
ls ~/.hzn/keys/service.private.key ~/.hzn/keys/service.public.pem
cat /etc/default/horizon
```
{: codeblock}

## 手順
{: #quickstart_ex_procedure}

**注**: コマンド構文について詳しくは、[本書の規則](../getting_started/document_conventions.md)を参照してください。

1. プロジェクト・ディレクトリーを作成します。

  1. 開発ホストで、既存の Docker プロジェクト・ディレクトリーに移動します。 **既存の Docker プロジェクトがなく、このサンプルを使用したい場合は**、以下のコマンドを使用して、この手順の残りの部分で使用できる単純な Dockerfile を作成します。

    ```bash
    cat << EndOfContent > Dockerfile
    FROM alpine:latest
    CMD while :; do echo "Hello, world."; sleep 3; done
    EndOfContent
    ```
    {: codeblock}

  2. プロジェクトのエッジ・サービス・メタデータを作成します。

    ```bash
    hzn dev service new -s myservice -V 1.0.0 -i $DOCKER_HUB_ID/myservice --noImageGen
    ```
    {: codeblock}

    このコマンドによって、サービスを記述するための **horizon/service.definition.json** と、デプロイメント・パターンを記述するための **horizon/pattern.json** が作成されます。 これらのファイルを開いて、内容を参照することができます。

2. サービスをビルドし、テストします。

  1. Docker イメージをビルドします。 イメージ名は、**horizon/service.definition.json** で参照されるものと一致しなければなりません。

    ```bash
    eval $(hzn util configconv -f horizon/hzn.json)
    export ARCH=$(hzn architecture)
    sudo docker build -t "${DOCKER_IMAGE_BASE}_$ARCH:$SERVICE_VERSION" .
    unset DOCKER_IMAGE_BASE SERVICE_NAME SERVICE_VERSION
    ```
    {: codeblock}

  2. このサービス・コンテナー・イメージを {{site.data.keyword.horizon}} でシミュレートされたエージェント環境で実行します。

    ```bash
    hzn dev service start -S
    ```
    {: codeblock}

  3. サービス・コンテナーが実行中であることを確認します。

    ```bash
    sudo docker ps
    ```
    {: codeblock}

  4. 開始時にコンテナーに渡された環境変数を表示します。 (これらは、完全なエージェントがサービス・コンテナーに渡す環境変数と同じです。)

    ```bash
    sudo docker inspect $(sudo docker ps -q --filter name=myservice) | jq '.[0].Config.Env'
    ```
    {: codeblock}

  5. サービス・コンテナー・ログを表示します。

    **{{site.data.keyword.linux_notm}}** の場合:

    ```bash
    sudo tail -f /var/log/syslog | grep myservice[[]
    ```
    {: codeblock}

    **{{site.data.keyword.macOS_notm}}** の場合:

    ```bash
    sudo docker logs -f $(sudo docker ps -q --filter name=myservice)
    ```
    {: codeblock}

  6. サービスを停止します。

    ```bash
    hzn dev service stop
    ```
    {: codeblock}

3. サービスを {{site.data.keyword.edge_notm}} に公開します。 これで、シミュレートされたエージェント環境においてサービス・コードが予期したとおりに実行されることを検証したので、サービスを {{site.data.keyword.horizon_exchange}} に公開して、エッジ・ノードへのデプロイメントに使用できるようにします。

  以下の **publish** コマンドは、**horizon/service.definition.json** ファイルと鍵ペアを使用してサービスに署名し、それを {{site.data.keyword.horizon_exchange}} に公開します。 このコマンドはさらに、イメージを Docker Hub にプッシュします。

  ```bash
  hzn exchange service publish -f horizon/service.definition.json
  hzn exchange service list
  ```
  {: codeblock}

4. サービスのデプロイメント・パターンを公開します。 このデプロイメント・パターンをエッジ・ノードで使用して、サービスが {{site.data.keyword.edge_notm}} によってエッジ・ノードにデプロイされるようにすることができます。

  ```bash
  hzn exchange pattern publish -f horizon/pattern.json
    hzn exchange pattern list
  ```
  {: codeblock}

5. デプロイメント・パターンを実行するためのエッジ・ノードを登録します。

  1. 以前に **IBM** 組織のパブリック・デプロイメント・パターンにエッジ・ノードを登録したときと同じ方法で、独自の組織の下で公開したデプロイメント・パターンにエッジ・ノードを登録します。

    ```bash
    hzn register -p pattern-myservice-$(hzn architecture) -s myservice --serviceorg $HZN_ORG_ID
    ```
    {: codeblock}

  2. 結果として開始された Docker コンテナー・エッジ・サービスをリストします。

    ```bash
    sudo docker ps
    ```
    {: codeblock}

  3. myservice エッジ・サービス出力を表示します。

    ```bash
    sudo hzn service log -f myservice
    ```
    {: codeblock}

6. {{site.data.keyword.edge_notm}} コンソールに作成したノード、サービス、およびパターンを表示します。 以下のようにして、コンソールの URL を表示できます。

  ```bash
  echo "$(awk -F '=|edge-exchange' '/^HZN_EXCHANGE_URL/ {print $2}' /etc/default/horizon)edge"
  ```
  {: codeblock}

7. エッジ・ノードを登録抹消し、**myservice** サービスを停止します。

  ```bash
  hzn unregister -f
  ```
  {: codeblock}

## 次の作業
{: #quickstart_ex_what_next}

* [エッジ・サービスのデプロイ](../using_edge_services/detailed_policy.md)にある他のエッジ・サービスのサンプルを試してみます。
