---

copyright:
years: 2020
lastupdated: "2020-03-18"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# エッジ・サービス用の CI-CD プロセス
{: #edge_native_practices}

進化していくエッジ・サービスのセットは、{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) の効果的な使用のために不可欠であり、堅固な継続的インテグレーションおよび継続的デプロイメント (Continuous Integration and Continuous Deployment (CI/CD)) プロセスは重要なコンポーネントです。 

このコンテンツを、独自の CI/CD プロセスの作成に利用可能なビルディング・ブロックをレイアウトするために使用できます。 このプロセスの詳細については、[`open-horizon/examples` リポジトリー ![新しいタブで開く](../../images/icons/launch-glyph.svg "新しいタブで開く")](https://github.com/open-horizon/examples) を参照してください。 

## 構成変数
{: #config_variables}

エッジ・サービスの開発者は、開発中のサービス・コンテナーのサイズを考慮する必要があります。 その情報に基づいて、サービスの機能を分割して別々のコンテナーに入れる必要が生じることがあります。 そのようなシチュエーションでは、テスト目的で使用される構成変数が、まだ開発されていないコンテナーからのデータをシミュレートするのに役立つことがあります。 [cpu2evtstreams サービス定義ファイル ![新しいタブで開く](../../images/icons/launch-glyph.svg "新しいタブで開く")](https://github.com/open-horizon/examples/blob/master/edge/evtstreams/cpu2evtstreams/horizon/service.definition.json) に **PUBLISH** や **MOCK** などの入力変数があるのを確認できます。 `service.sh` コードを調べると、これらおよびその他の構成変数がこのコードの動作を制御するために使用されていることが分かります。 **PUBLISH** は、このコードがメッセージを IBM Event Streams に送信しようとするかどうかを制御します。 **MOCK** は、service.sh が REST API およびその従属サービス (cpu および gps) に連絡しようとするかどうか、または、`service.sh` がフェイク・データを作成するかどうかを制御します。

サービスのデプロイメント時に、ノード定義内に指定するか、または `hzn register` コマンドで指定することによって、構成変数のデフォルト値をオーバーライドできます。

## クロス・コンパイル
{: #cross_compiling}

Docker を使用して、単一の amd64 マシンから、複数のアーキテクチャー向けの 1 つのコンテナー化されたサービスをビルドできます。 同様に、クロス・コンパイルをサポートするコンパイル型プログラミング言語 (Go など) を使用してエッジ・サービスを開発できます。 例えば、Mac (amd64 アーキテクチャーのデバイス) で ARM デバイス (Raspberry Pi) 用にコードを作成する場合、GOARCH といったパラメーターをターゲット arm に定する Docker コンテナーをビルドすることが必要になる可能性があります。 このセットアップは、デプロイメントのエラーを防止できます。 [open-horizon gps サービス ![新しいタブで開く](../../images/icons/launch-glyph.svg "新しいタブで開く")](https://github.com/open-horizon/examples/tree/master/edge/services/gps) を参照してください。

## テスト
{: #testing}

頻繁な自動化されたテストは、開発プロセスの重要な部分です。 テストを促進するために、`hzn dev service start` コマンドを使用して、シミュレートされた Horizon エージェント環境でサービスを実行できます。 この手法は、完全な Horizon エージェントのインストールおよび登録には問題がある可能性がある DevOps 環境でも有用です。 このメソッドは、**make test** ターゲットの `open-horizon examples` リポジトリー内のサービス・テストを自動化します。 [make test target ![新しいタブで開く](../../images/icons/launch-glyph.svg "新しいタブで開く")](https://github.com/open-horizon/examples/blob/305c4f375aafb09733f244ec9a899ce136b6d311/edge/services/helloworld/Makefile#L30) を参照してください。


**make test** を実行してサービスをビルドして実行します。これは **hzn dev service start** を使用します。 この実行後、[serviceTest.sh ![新しいタブで開く](../../images/icons/launch-glyph.svg "新しいタブで開く")](https://github.com/open-horizon/examples/blob/master/tools/serviceTest.sh) は、サービス・ログをモニターして、サービスが正しく実行していることを示すデータを見つけます。

## テスト・デプロイメント
{: #testing_deployment}

新しいサービス・バージョンを開発している場合、完全な実世界のテストにアクセスできることが理想的です。 これを行うために、サービスをエッジ・ノードにデプロイすることができますが、これはテストであるため、最初はエッジ・ノードのすべてにサービスをデプロイする必要はありません。

これを行うには、新しいサービス・バージョンのみを参照するデプロイメント・ポリシーまたはパターンを作成します。 次に、このポリシーまたはパターンにテスト・ノードを登録します。 ポリシーを使用する場合の 1 つのオプションが、エッジ・ノードにプロパティーを設定することです。 例えば、("name": "mode", "value": "testing") であり、その制約をデプロイメント・ポリシーに追加します ("mode == testing")。 これにより、テスト用に確保したノードのみが新バージョンのサービスを受け取ることが確実になります。

注: デプロイメント・ポリシーまたはパターンを管理コンソールから作成することもできます。 [管理コンソールの使用](../getting_started/accessing_ui.md)を参照してください。

## 実動デプロイメント
{: #production_deployment}

新バージョンのサービスをテスト環境から実稼働環境に移した後、テスト中には発生しなかった問題が起こることがあり得ます。 デプロイメント・ポリシーまたはパターンのロールバック設定がそれらの問題に対処するのに役立ちます。 パターンまたはデプロイメント・ポリシーの `serviceVersions` セクションに、サービスの古いバージョンを複数指定できます。 新バージョンでエラーがあった場合にエッジ・ノードがロールバックする際の優先順位を各バージョンに付与します。 各ロールバック・バージョンに優先順位を割り当てることに加えて、指定されたサービスの優先順位の低いバージョンにフォールバックするまでの再試行の回数と期間などといったことを指定できます。具体的な構文については、[このデプロイメント・ポリシー例 ![新しいタブで開く](../../images/icons/launch-glyph.svg "新しいタブで開く")](https://github.com/open-horizon/anax/blob/master/cli/samples/business_policy.json) を参照してください。

## エッジ・ノードの表示
{: #viewing_edge_nodes}

新バージョンのサービスをノードにデプロイした後、エッジ・ノードの正常性を簡単にモニターできることが重要です。 このタスクのために {{site.data.keyword.ieam}} {{site.data.keyword.gui}}を使用します。 例えば、[テスト・デプロイメント](#testing_deployment)または[実動デプロイメント](#production_deployment)のプロセス中に、デプロイメント・ポリシーを使用するノードや、エラーのあるノードを迅速に検索できます。

## サービスのマイグレーション
{: #migrating_services}

ある時点で、サービス、パターン、またはポリシーを、{{site.data.keyword.ieam}} のあるインスタンスから別のインスタンスに移動することが必要になる場合があります。 同様に、ある Exchange 組織から別の組織にサービスを移動することが必要になることもあります。 こういうことは、{{site.data.keyword.ieam}} の新しいインスタンスを異なるホスト環境にインストールした場合に起こる可能性があります。 あるいは、1 つは開発専用、もう 1 つは実動用として、2 つの {{site.data.keyword.ieam}} インスタンスがある場合にも、サービスの移動が必要になることがあります。 この処理を容易にするために、open-horizon examples リポジトリー内の [`loadResources` スクリプト ![新しいタブを開く](../../images/icons/launch-glyph.svg "新しいタブを開く")](https://github.com/open-horizon/examples/blob/master/tools/loadResources) を使用できます。 

## Travis を使用して自動化されるプル要求テスト
{: #testing_with_travis}

[Travis CI ![新しいタブで開く](../../images/icons/launch-glyph.svg "新しいタブで開く")](https://travis-ci.com) を使用して、プル要求 (PR) が GitHub リポジトリーに対してオープンされるたびにテストが行われるように自動化できます。 

Travis および open-horizon examples GitHub リポジトリー内の技法を活用する方法については、このコンテンツを引き続きお読みください。

examples リポジトリー内では、サンプルのビルド、テスト、および公開のために Travis CI が使用されています。 [`.travis.yml` ファイル ![新しいタブで開く](../../images/icons/launch-glyph.svg "新しいタブで開く")](https://github.com/open-horizon/examples/blob/master/.travis.yml) で、1 つの仮想環境が、複数のアーキテクチャーでのビルドのために、hzn、Docker、および [qemu ![新しいタブで開く](../../images/icons/launch-glyph.svg "新しいタブで開く")](https://github.com/multiarch/qemu-user-static) がある Linux amd64 マシンとして稼働するようにセットアップされています。

このシナリオでは、cpu2evtstreams がデータを IBM Event Streams に送信するようにするために kafkacat もインストールされます。 コマンド・ラインの使用と同様に、Travis は、サンプル・エッジ・サービスと共に使用するために `EVTSTREAMS_TOPIC` や `HZN_DEVICE_ID` などの環境変数を使用できます。 HZN_EXCHANGE_URL は、変更されたサービスを公開するためのステージング Exchange をポイントするように設定されます。

次に [travis-find ![新しいタブで開く](../../images/icons/launch-glyph.svg "新しいタブで開く")](https://github.com/open-horizon/examples/blob/master/tools/travis-find) スクリプトを使用して、オープンされたプル要求によって変更されたサービスが識別されます。

変更されたサンプルがある場合、そのサービスの **makefile** 内の `test-all-arches` ターゲットが実行されます。 サポートされるアーキテクチャーの qemu コンテナーが実行中である状態で、クロス・アーキテクチャー・ビルドが、ビルドおよびテストの直前に `ARCH` 環境変数を設定することによって、この **makefile** ターゲットで実行されます。 

`hzn dev service start` コマンドはエッジ・サービスを実行し、[serviceTest.sh ![新しいタブで開く](../../images/icons/launch-glyph.svg "新しいタブで開く")](https://github.com/open-horizon/examples/blob/master/tools/serviceTest.sh) ファイルは、サービス・ログをモニターして、サービスが正しく作動しているかどうかを判別します。

[helloworld Makefile ![新しいタブで開く](../../images/icons/launch-glyph.svg "新しいタブで開く")](https://github.com/open-horizon/examples/blob/afd4a5822aede44616eb5da7cd9dafd4d78f12ec/edge/services/helloworld/Makefile#L24) を参照して、専用 `test-all-arches` Makefile ターゲットを確認してください。

以下のシナリオは、さらにエンドツーエンドのテストを示します。 変更されたサンプルの 1 つに `cpu2evtstreams` が含まれている場合、IBM Event Streams の 1 つのインスタンスがバックグラウンドで変更され、HZN_DEVICE_ID があるか検査されることができます。 それがテストに合格してすべての合格サービスのリストに追加されることができるのは、それが cpu2evtstreams トピックから読み取ったデータ中に **travis-test** ノード ID を見つけた場合のみです。 これには、秘密環境変数として設定された IBM Event Streams API キーおよびブローカー URL が必要です。

PR がマージされた後、このプロセスが繰り返され、合格サービスのリストを使用して、どのサービスを Exchange に公開できるのかが識別されます。 この例で使用されている Travis 秘密環境変数には、サービスのプッシュ、署名、および Exchange への公開に必要なすべてのものが含まれています。 これには、Docker 資格情報である HZN_EXCHANGE_USER_AUTH と、`hzn key create` コマンドで取得できる暗号署名鍵ペアが含まれます。 セキュアな環境変数として署名鍵を保存するために、署名鍵は base64 エンコードである必要があります。

機能テストに合格したサービスのリストを使用して、専用の公開 `Makefile` ターゲットでの公開が必要なサービスが識別されます。 [helloworld サンプル ![新しいタブで開く](../../images/icons/launch-glyph.svg "新しいタブで開く")](https://github.com/open-horizon/examples/blob/afd4a5822aede44616eb5da7cd9dafd4d78f12ec/edge/services/helloworld/Makefile#L45) を参照してください。

サービスのビルドとテストが完了したため、このターゲットは、すべてのアーキテクチャーの、サービス、サービス・ポリシー、パターン、およびデプロイメント・ポリシーを Exchange に公開します。

注: これらのタスクの多くは管理コンソールから実行することもできます。 [管理コンソールの使用](../getting_started/accessing_ui.md)を参照してください。

