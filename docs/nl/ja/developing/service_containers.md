---

copyright:
years: 2019,2020
lastupdated: "2020-01-28"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# エッジ・サービス作成の準備
{: #service_containers}

{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) を使用して、エッジ・デバイス用に {{site.data.keyword.docker}} コンテナー内でサービスを開発します。 エッジ・サービスを作成するために、任意の適切な {{site.data.keyword.linux_notm}} ベース、プログラミング言語、ライブラリー、またはユーティリティーを使用できます。
{:shortdesc}

サービスのプッシュ、署名、および公開を行うと、その後、{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) では、エッジ・デバイス上の完全自律型エージェントによって、サービスのダウンロード、検証、構成、インストール、およびモニターが行われます。 

多くの場合、エッジ・サービスはクラウドの取り込みサービスを使用して、エッジ分析結果を保管し、さらなる処理を行います。 このプロセスには、エッジおよびクラウド・コードの開発ワークフローが含まれます。

{{site.data.keyword.ieam}} は、オープン・ソースの [{{site.data.keyword.horizon_open}}](https://github.com/open-horizon/) プロジェクトに基づいており、`hzn` {{site.data.keyword.horizon}} {{site.data.keyword.linux_notm}} コマンドを使用して一部のプロセスを実行します。

## 始める前に
{: #service_containers_begin}

1. {{site.data.keyword.horizon}} エージェントをホストにインストールし、ホストを {{site.data.keyword.horizon_exchange}} に登録することで、開発ホストを {{site.data.keyword.ieam}} で使用できるように構成します。 [Hello World サンプルを使用したエッジ・デバイスでの {{site.data.keyword.horizon}} エージェントのインストールと登録](../installing/registration.md)を参照してください。

2. [Docker Hub](https://hub.docker.com/) ID を作成します。 このセクションの手順には、サービス・コンテナー・イメージの Docker Hub への公開が含まれているため、この ID が必要です。

## 手順
{: #service_containers_procedure}

**注**: コマンド構文について詳しくは、[本書の規則](../getting_started/document_conventions.md)を参照してください。

1. [Hello World サンプルを使用したエッジ・デバイスでの {{site.data.keyword.horizon}} エージェントのインストールと登録](../installing/registration.md)のステップを実行した際に、Exchange の資格情報を設定しています。 以下のコマンドでエラーが表示されないことを検証し、資格情報が依然として正しく設定されていることを確認します。

  ```
  hzn exchange user list
  ```
  {: codeblock}

2. 開発ホストとして {{site.data.keyword.macOS_notm}} を使用している場合は、Docker hub 登録資格情報を `~/.docker/plaintext-passwords.json` に入れます。

  ```
  export DOCKER_HUB_ID="<yourdockerhubid>"
  export DOCKER_HUB_PW="<yourdockerhubpassword>"
  echo "{ \"auths\": { \"https://index.docker.io/v1/\": { \"auth\": \"$(printf "${DOCKER_HUB_ID:?}:${DOCKER_HUB_PW:?}" | base64)\" } } }" > ~/.docker/plaintext-passwords.json

  ```
  {: codeblock}

3. 前に作成した Docker Hub ID を使用して Docker Hub にログインします。

  ```
  export DOCKER_HUB_ID="<yourdockerhubid>"
  export DOCKER_HUB_PW="<yourdockerhubpassword>"
  echo "$DOCKER_HUB_PW" | docker login -u $DOCKER_HUB_ID --password-stdin
  ```
  {: codeblock}

  出力例:
  ```
  WARNING! Your password will be stored unencrypted in ~userName/.docker/config.json.
  Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store

  Login Succeeded
  ```

4. 暗号署名鍵ペアを作成します。 これにより、Exchange にサービスを公開するときに、サービスに署名できるようになります。 

   **注**: このステップを実行する必要があるのは 1 回のみです。

  ```
  hzn key create "<companyname>" "<youremailaddress>"
  ```
  {: codeblock}
  
  ここで、`companyname` は x509 組織として使用され、`youremailaddress` は x509 CN として使用されます。

5. いくつかの開発ツールをインストールします。

  **{{site.data.keyword.linux_notm}}** 上 (Ubuntu/Debian ディストリビューション用):

  ```
  sudo apt install -y git jq make
  ```
  {: codeblock}

  **{{site.data.keyword.macOS_notm}}** の場合:

  ```
  brew install git jq make
  ```
  {: codeblock}
  
  **注**: 必要な場合、brew のインストールについて詳しくは、[homebrew](https://brew.sh/) を参照してください。

## 次の作業
{: #service_containers_what_next}

* 資格情報および署名鍵を使用して、[開発サンプル](../OH/docs/developing/developing.md)を実行します。 これらのサンプルには、単純なエッジ・サービスを作成して、{{site.data.keyword.edge_notm}} での開発の基本を学ぶ方法が示されています。
* {{site.data.keyword.edge_notm}} でエッジ・ノードにデプロイする Docker イメージが既にある場合は、『[エッジ・サービスへのイメージの変換](transform_image.md)』を参照してください。
