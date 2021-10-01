---

copyright:
years: 2020
lastupdated: "2020-04-27"

---

{:shortdesc: .shortdesc}
{:new_window: target="_blank"}
{:codeblock: .codeblock}
{:pre: .pre}
{:screen: .screen}
{:tip: .tip}
{:download: .download}

# Kubernetes オペレーターの開発
{: #kubernetes_operator}

一般に、エッジ・クラスター内で実行されるサービスの開発は、エッジ・デバイス上で実行されるエッジ・サービスの開発に似ています。 エッジ・サービスは[エッジ・ネイティブ開発のベスト・プラクティス](best_practices.md)開発を使用して開発され、コンテナーにパッケージされます。 相違点は、エッジ・サービスのデプロイ方法にあります。

コンテナー化されたエッジ・サービスをエッジ・クラスターにデプロイするために、開発者はまず、コンテナー化されたエッジ・サービスを Kubernetes クラスターにデプロイする Kubernetes オペレーターを作成する必要があります。 オペレーターが記述されてテストされた後、開発者はそのオペレーターを {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) サービスとして作成して公開します。 このプロセスによって、{{site.data.keyword.ieam}} 管理者は、あらゆる {{site.data.keyword.ieam}} サービスに行われるのと同様に、ポリシーやパターンとともに、このオペレーター・サービスをデプロイできるようになります。 エッジ・サービスに対する {{site.data.keyword.ieam}} サービス定義を作成する必要はありません。 {{site.data.keyword.ieam}} 管理者がオペレーター・サービスをデプロイすると、オペレーターがエッジ・サービスをデプロイします。

Kubernetes オペレーターを記述する際には、いくつかのオプションがあります。 まず、[Kubernetes Concepts - Operator pattern ![新しいタブで開く](../../images/icons/launch-glyph.svg "新しいタブで開く")](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/) をお読みください。 このサイトは、オペレーターの詳細を知るのに役立つ資源です。 オペレーターの概念を十分に理解したら、[Operator Framework ![新しいタブで開く](../../images/icons/launch-glyph.svg "新しいタブで開く")](https://github.com/operator-framework/getting-started) を使用して、オペレーターの記述を行います。 この記事では、オペレーターとは何かの詳細を示し、オペレーターの Software Development Kit (SDK) を使用して、単純なオペレーターの作成を順を追って説明しています。

## {{site.data.keyword.ieam}} のオペレーターを開発する際の考慮事項

{{site.data.keyword.ieam}} は、オペレーターが生成するすべての状況を {{site.data.keyword.ieam}} 管理ハブに報告するため、オペレータの状況を十分に活用するのがベスト・プラクティスです。 オペレーターを記述すると、オペレーター・フレームワークは、当該オペレーターに対する Kubernetes カスタム・リソース定義 (CRD) を生成します。 各オペレーター CRD には 1 つの状況オブジェクトがあり、そのオペレーターとそのオペレーターがデプロイするエッジ・サービスの状態に関する重要な状況情報が取り込まれる必要があります。 これは、Kubernetes によって自動的に行われません。オペレーターの開発者が、オペレータの実装に記述する必要があります。 エッジ・クラスター内の {{site.data.keyword.ieam}} エージェントは、定期的にオペレーターの状況を収集して管理ハブに報告します。

必要であれば、オペレーターは、サービス固有の {{site.data.keyword.ieam}} 環境変数を、それが開始する任意のサービスに接続することができます。 オペレーターが開始されると、{{site.data.keyword.ieam}} エージェントは、サービス固有の環境変数を含む、`hzn-env-vars` という名前の kubernetes configmap を作成します。 オペレーターは、オプションで、作成する任意のデプロイメントにその config map を接続することもできます。これにより、開始するサービスが、同じサービス固有環境変数を認識できるようになります。 これらは、エッジ・デバイスで実行されるサービスに注入されるものと同じ環境変数です。 唯一の例外が、ESS* 環境変数です。これは、モデル管理システム (MMS) がエッジ・クラスター・サービスにまだサポートされていないためです。

必要であれば、{{site.data.keyword.ieam}} がデプロイしたオペレーターを、デフォルト以外の名前空間にデプロイすることが可能です。 これは、オペレーター開発者が、その名前空間を指すようにオペレーター yaml ファイルを変更することで行います。 これには、2 つの方法があります。

 * オペレーターのデプロイメント定義 (通常、**./deploy/operator.yaml** という名前) を変更して、名前空間を指定する。

または

* オペレーターの yaml 定義ファイルとともに名前空間定義の yaml ファイルを、例えばオペレーター・プロジェクトの **./deploy** ディレクトリーなどに含める。

注: デフォルト以外の名前空間にオペレーターがデプロイされた場合、{{site.data.keyword.ieam}} は、その名前空間が存在しなければ作成し、そのオペレーターが {{site.data.keyword.ieam}} によってアンデプロイされるときに削除します。

## {{site.data.keyword.ieam}} のオペレーターの記述

オペレーターを記述してテストしたら、以下のように、{{site.data.keyword.ieam}} によるデプロイメントのためにパッケージ化する必要があります。

1. 必ず、クラスター内のデプロイメントとして実行されるようにオペレーターをパッケージ化します。 つまり、オペレーターはコンテナーにビルドされ、{{site.data.keyword.ieam}} がデプロイ時にそのコンテナーを取得する元のコンテナー・レジストリーにプッシュされます。 これは通常、コマンド **operator-sdk build** の後に **docker push** を使用してオペレーターをビルドすることで行います。 これは [Operator Framework ![新しいタブで開く](../../images/icons/launch-glyph.svg "新しいタブで開く")](https://github.com/operator-framework/getting-started#1-run-as-a-deployment-inside-the-cluster) に説明されています。

2. 必ず、オペレーターによってデプロイされるサービス・コンテナーは、オペレーターがそれらをデプロイする元のレジストリーにもプッシュされるようにします。

3. 以下のようにして、オペレーター・プロジェクトからのオペレーターの yaml 定義ファイルを含むアーカイブを作成します。

   ```bash
   cd <operator-project>/<operator-name>/deploy
    tar -zcvf <archive-name>.tar.gz
   ```
   {: codeblock}

4. {{site.data.keyword.ieam}} サービス作成ツールを使用して、オペレーター・サービスのサービス定義を作成します。例えば、以下のステップに従って行います。

   1. 新規プロジェクトを作成します。

      ```bash
      hzn dev service new -V <a version> -s <a service name> -c cluster
      ```
      {: codeblock}

   2. ステップ 3 で作成したオペレーターの yaml アーカイブを指すように、**horizon/service.definition.json** ファイルを編集します。

   3. サービス署名鍵を作成します。あるいは、既存のサービス署名鍵を使用します。

   4. サービスの公開

      ```
      hzn exchange service publish -k <signing key> -f ./horizon/service.definition.json
      ```
      {: codeblock}

5. オペレーター・サービスをエッジ・クラスターにデプロイするためのデプロイメント・ポリシーまたはパターンを作成します。
