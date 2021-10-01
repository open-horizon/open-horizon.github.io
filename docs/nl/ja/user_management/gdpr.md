---

copyright:
years: 2020
lastupdated: "2020-10-7"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# GDPR の考慮事項

## 特記事項
{: #notice}
<!-- This is boilerplate text provided by the GDPR team. It cannot be changed. -->

この資料は、GDPR 対応に向けた準備に役立てるためのものです。 組織で GDPR に対応できるようにする際に、構成可能な {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) の機能に関する情報、および考慮する必要がある製品の使用の側面を示します。 この情報は、網羅的なリストではありません。 これは、お客様が多くの各種方法で機能を選択および構成でき、製品の使用方法も多岐にわたり、サード・パーティーのアプリケーションやシステムがインストールされることもあるためです。

<p class="ibm-h4 ibm-bold">お客様自身が欧州連合の一般データ保護規則を含む各種法令を遵守するために必要な措置を講ずるのはお客様の責任です。 お客様のビジネスに影響を与える可能性がある関連法規の確認と解釈、並びにかかる法規を遵守するためにお客様がとる必要のある措置に関して、弁護士の適切な助言を得ることはお客様のみにかかわる責任とさせていただきます。</p>

<p class="ibm-h4 ibm-bold">本書に記載の製品、サービス、およびその他の機能は、あらゆるお客様の状況に適しているわけではなく、利用が制限される可能性があります。 IBM は法律上、会計上、または監査上の助言を提供することはしません。また、IBM のサービスまたは製品が、お客様のいかなる法規制の遵守を裏付けることも表明または保証することもありません。</p>

## 目次

* [GDPR](#overview)
* [GDPR の製品構成](#productconfig)
* [データ・ライフサイクル](#datalifecycle)
* [データ処理](#dataprocessing)
* [個人データの使用を制限するための機能](#datasubjectrights)
* [付録](#appendix)

## GDPR
{: #overview}

<!-- This is boilerplate text provided by the GDPR team. It cannot be changed. -->
欧州連合 (EU) により一般データ保護規則 (GDPR) が採択され、2018 年 5 月 25 日より施行されています。

### GDPR が重要である理由

GDPR では、個人データを処理するための、より強力なデータ保護規制フレームワークを規定しています。 GDPR は、以下をもたらします。

* 個人の新しい権限および強化された権限
* 個人データの定義の拡大
* 個人データを扱う会社および組織に対する新しい義務
* 不遵守に対する高額の制裁金
* データ・ブリーチ通知の義務

IBM は、IBM の内部プロセスおよび商用オファリングを GDPR 遵守に向けて準備するためのグローバル対応プログラムを確立しています。

### 詳細情報

* [EU GDPR 情報のポータル](https://gdpr.eu/)
*  [ibm.com/GDPR website](https://www.ibm.com/data-responsibility/gdpr/)

## 製品の構成 – GDPR 対応に向けた考慮事項
{: #productconfig}

以下のセクションでは、{{site.data.keyword.ieam}} のさまざまな側面について説明し、GDPR 要件に対応するためにお客様に役立つ機能に関する情報を示します。

### データ・ライフサイクル
{: #datalifecycle}

{{site.data.keyword.ieam}} は、オンプレミスのコンテナー化されたアプリケーションを開発および管理するためのアプリケーションです。 これは、エッジでコンテナー・ワークロードを管理するための統合環境です。 コンテナー・オーケストレーター Kubernetes、プライベート・イメージ・レジストリー、管理コンソール、エッジ・ノード・エージェント、およびモニタリング・フレームワークが含まれます。

そのため、{{site.data.keyword.ieam}} では、アプリケーションの構成および管理に関連した技術データを主に扱いますが、その一部は GDPR の対象になる可能性があります。 {{site.data.keyword.ieam}} では、アプリケーションを管理するユーザーに関する情報も扱います。 お客様の責任で GDPR 要件を満たすことが認識されるように、このデータについては、本資料の至る所で記載されます。

このデータは、{{site.data.keyword.ieam}} のローカルまたはリモートのファイル・システム上の構成ファイルまたはデータベースで永続化されます。 {{site.data.keyword.ieam}} で実行されるように開発されたアプリケーションで、GDPR の対象となる他の形式の個人データを使用する可能性があります。 データの保護および管理に使用されるメカニズムは、{{site.data.keyword.ieam}} で実行されるアプリケーションでも使用可能です。 {{site.data.keyword.ieam}} で実行されるアプリケーションによって収集された個人データを管理および保護するために、追加のメカニズムが必要になることがあります。

{{site.data.keyword.ieam}} のデータ・フローを理解するには、Kubernetes、Docker、およびオペレーターの仕組みを把握する必要があります。 これらのオープン・ソースのコンポーネントは、{{site.data.keyword.ieam}} の基礎となっています。 {{site.data.keyword.ieam}} を使用して、アプリケーション・コンテナーのインスタンス (エッジ・サービス) をエッジ・ノードに配置します。 エッジ・サービスには、アプリケーションに関する詳細が含まれます。Docker イメージには、アプリケーションの実行に必要なすべてのソフトウェア・パッケージが含まれます。

{{site.data.keyword.ieam}} には、一連のオープンソースのエッジ・サービスの例が含まれています。 すべての {{site.data.keyword.ieam}} チャートのリストを表示するには、[open-horizon/examples](https://github.com/open-horizon/examples){:new_window} を参照してください。 オープン・ソース・ソフトウェアに対して適切な GDPR 管理を判別して実装するのは、お客様の責任です。

### {{site.data.keyword.ieam}} をフローするデータのタイプ

{{site.data.keyword.ieam}} は、以下のような、個人データと見なされる可能性がある複数のカテゴリーの技術データを扱います。

* 管理者やオペレーターのユーザー ID およびパスワード
* IP アドレス
* Kubernetes ノード名

この文書の以降のセクションでは、この技術データを収集、作成、保管、アクセス、保護、記録、削除する方法に関する情報を示します。

### <b>IBM とのオンラインによる連絡のために使用される個人データ</b>

{{site.data.keyword.ieam}} のお客様は、主に以下のようなさまざまな方法で、{{site.data.keyword.ieam}} についてオンライン・コメント、フィードバック、および要求を IBM に送信できます。

* 公共の {{site.data.keyword.ieam}} Slack コミュニティー
* {{site.data.keyword.ieam}} 製品資料のページ上のパブリック・コメント・エリア
* dW Answers の {{site.data.keyword.ieam}} スペース内のパブリック・コメント

通常は、送信された用件について個人的に返信できるように、お客様の名前と E メール・アドレスのみが使用されます。 この個人データの使用は、[IBM オンライン・プライバシー・ステートメント](https://www.ibm.com/privacy/us/en/){:new_window} に準拠しています。

### 認証

{{site.data.keyword.ieam}} 認証マネージャーは、{{site.data.keyword.gui}}からユーザー資格情報を受け入れ、その資格情報をバックエンドの OIDC プロバイダーに転送します。このプロバイダーは、エンタープライズ・ディレクトリーに対してユーザー資格情報を検証します。 次に、OIDC プロバイダーが、JSON Web Token (`JWT`) の内容が含まれた認証 Cookie (`auth-cookie`) を認証マネージャーに返します。 JWT トークンは、認証要求時のグループ・メンバーシップに加え、ユーザー ID および E メール・アドレスなどの情報を永続化します。 この認証 Cookie はその後 {{site.data.keyword.gui}} に戻されます。 Cookie はセッション中に更新されます。 これは、{{site.data.keyword.gui}} からサインアウト後、または Web ブラウザーをクローズしてから 12 時間有効です。

{{site.data.keyword.gui}} から作成された連続するすべての認証要求について、フロントエンド NodeJS サーバーは、要求内の使用可能な認証 Cookie をデコードして、認証マネージャーを呼び出すことで要求を検証します。

{{site.data.keyword.ieam}} CLI では、ユーザーは API 鍵を指定する必要があります。 API 鍵は、`cloudctl` コマンドを使用して作成されます。

**cloudctl**、**kubectl**、および **oc** CLI では、クラスターにアクセスするために資格情報も必要です。 これらの資格情報は、管理コンソールから取得でき、12 時間後に有効期限が切れます。

### 役割マッピング

{{site.data.keyword.ieam}} では、役割ベースのアクセス制御 (RBAC) がサポートされます。 役割マッピング・ステージでは、認証ステージで指定されたユーザー名がユーザーまたはグループの役割にマップされます。 役割は、認証済みユーザーがどのアクティビティーを実行できるのかを許可するために使用されます。 {{site.data.keyword.ieam}} の役割について詳しくは、『[役割ベースのアクセス制御](rbac.md)』を参照してください。

### ポッドのセキュリティー

ポッド・セキュリティー・ポリシーを使用して、ポッドが実行可能な内容や、ポッドがアクセス可能な対象について、管理ハブまたはエッジ・クラスターでの制御をセットアップします。 ポッドについて詳しくは、『[管理ハブのインストール](../hub/hub.md)』および『[エッジ・クラスター](../installing/edge_clusters.md)』を参照してください。

## データ処理
{: #dataprocessing}

{{site.data.keyword.ieam}} のユーザーは、構成および管理に関連した技術データをどのように処理および保護するのかをシステム構成によって制御できます。

* 役割ベースのアクセス制御 (RBAC) により、ユーザーがアクセスできるデータおよび機能を制御します。

* ポッド・セキュリティー・ポリシーを使用して、ポッドが実行可能な内容や、ポッドがアクセス可能な対象について、クラスター・レベルでの制御をセットアップします。

* 転送中データは、`TLS` を使用して保護されます。 `HTTPS` (`TLS` ベース) が、ユーザー・クライアントとバックエンド・サービスとの間のセキュアなデータ転送のために使用されます。 ユーザーは、インストール時に使用するルート証明書を指定できます。

* 保存データの保護は、`dm-crypt` を使用してデータを暗号化することでサポートされます。

* ロギング (ELK) およびモニター (Prometheus) のデータ保存期間が構成可能であり、提供されている API を使用したデータの削除がサポートされます。

{{site.data.keyword.ieam}} の技術データを管理および保護するために使用されるのと同じメカニズムを使用して、ユーザーが開発したアプリケーションやユーザー提供のアプリケーションの個人データを管理および保護できます。 お客様は、さらなる制御を実装するために独自の機能を開発することもできます。

証明書について詳しくは、[{{site.data.keyword.ieam}} のインストール](../hub/installation.md)を参照してください。

## 個人データの使用を制限するための機能
{: #datasubjectrights}

{{site.data.keyword.ieam}} では、ユーザーは、この資料で要約されている機能を使用して、個人データと見なされる、アプリケーション内の技術データの使用を制限できます。

GDPR の下で、ユーザーは、アクセス、変更、および処理制限の権利を持っています。 以下を制御するために、この資料の他のセクションを参照してください。
* アクセスする権利
  * {{site.data.keyword.ieam}} 管理者は、{{site.data.keyword.ieam}} 機能を使用して、個人が自分のデータにアクセスできるようにすることが可能です。
  * {{site.data.keyword.ieam}} 管理者は、{{site.data.keyword.ieam}} 機能を使用して、個人についてどのようなデータを {{site.data.keyword.ieam}} が収集して保持するのかに関する情報を個人に提供できます。
* 変更する権利
  * {{site.data.keyword.ieam}} 管理者は、{{site.data.keyword.ieam}} 機能を使用して、個人が自分のデータを変更または修正できるようにすることが可能です。
  * {{site.data.keyword.ieam}} 管理者は、{{site.data.keyword.ieam}} 機能を使用して、個人に代わって個人のデータを修正できます。
* 処理を制限する権利
  * {{site.data.keyword.ieam}} 管理者は、{{site.data.keyword.ieam}} 機能を使用して、個人のデータの処理を停止できます。

## 付録 - {{site.data.keyword.ieam}} によってログに記録されるデータ
{: #appendix}

アプリケーションとして、{{site.data.keyword.ieam}} は、以下のような、個人データと見なされる可能性がある複数のカテゴリーの技術データを扱います。

* 管理者やオペレーターのユーザー ID およびパスワード
* IP アドレス
* Kubernetes ノード名 

また、{{site.data.keyword.ieam}} は、{{site.data.keyword.ieam}} で実行されるアプリケーションを管理するユーザーに関する情報を扱い、本アプリケーションにとって不明な他のカテゴリーの個人データが導入される可能性があります。

### {{site.data.keyword.ieam}} のセキュリティー

* ログに記録されるデータ
  * ログイン・ユーザーのユーザー ID、ユーザー名、IP アドレス
* データがログに記録されるタイミング
  * ログイン要求時
* データがログに記録される場所
  * `/var/lib/icp/audit`??? の監査ログ内
  * `/var/log/audit`??? の監査ログ内
  * ??? の交換ログ
* データの削除方法
  * 監査ログでデータを検索してそのレコードを削除する

### {{site.data.keyword.ieam}} API

* ログに記録されるデータ
  * コンテナー・ログ内のクライアントのユーザー ID、ユーザー名、および IP アドレス
  * `etcd` サーバー内の Kubernetes クラスター状態データ
  * `etcd` サーバー内の OpenStack および VMware 資格情報
* データがログに記録されるタイミング
  * API 要求時
  * `credentials-set` コマンドからの資格情報の保管時
* データがログに記録される場所
  * コンテナー・ログ、Elasticsearch、および `etcd` サーバー内
* データの削除方法
  * コンテナー・ログ (`platform-api`, `platform-deploy`) をコンテナーから削除するか、ユーザー固有のログ項目を Elasticsearch から削除する
  * `etcdctl rm` コマンドを使用して、選択した `etcd` のキーと値のペアをクリアする
  * `credentials-unset` コマンドを呼び出して、資格情報を削除する


詳しくは、以下を参照してください。

  * [Kubernetes Logging](https://kubernetes.io/docs/concepts/cluster-administration/logging/){:new_window}
  * [etcdctl](https://github.com/coreos/etcd/blob/master/etcdctl/READMEv2.md){:new_window}

### {{site.data.keyword.ieam}} モニター

* ログに記録されるデータ
  * ポッド、リリース、イメージの IP アドレス、名前
  * お客様が開発したアプリケーションから取得されたデータに個人データが含まれている可能性があります
* データがログに記録されるタイミング
  * Prometheus が、構成されているターゲットからメトリックを取得したとき
* データがログに記録される場所
  * Prometheus サーバーまたは構成されているパーシスタント・ボリューム内
* データの削除方法
  * Prometheus API を使用して、データを検索して削除する

詳しくは、[Prometheus 資料](https://prometheus.io/docs/introduction/overview/){:new_window}を参照してください。


### {{site.data.keyword.ieam}} Kubernetes

* ログに記録されるデータ
  * クラスター・デプロイ・トポロジー (コントローラー、ワーカー、プロキシー、va のノード情報)
  * サービス構成 (k8s 構成マップ) および秘密 (k8s 秘密)
  * apiserver ログのユーザー ID
* データがログに記録されるタイミング
  * クラスターのデプロイ時
  * Helm カタログからのアプリケーションのデプロイ時
* データがログに記録される場所
  * `etcd` 内のクラスター・デプロイ・トポロジー
  * `etcd` 内のデプロイ済みアプリケーションの構成および秘密
* データの削除方法
  * {{site.data.keyword.ieam}} {{site.data.keyword.gui}}を使用する
  * k8s {{site.data.keyword.gui}} (`kubectl`) または `etcd` REST API を使用して、データを検索して削除する
  * Elasticsearch API を使用して、apiserver ログ・データを検索して削除する

Kubernetes クラスター構成の変更またはクラスター・データの削除を行う際には慎重に行ってください。

  詳しくは、[Kubernetes kubectl](https://kubernetes.io/docs/reference/kubectl/overview/){:new_window} を参照してください。

### {{site.data.keyword.ieam}} Helm API

* ログに記録されるデータ
  * ユーザー名および役割
* データがログに記録されるタイミング
  * チームに追加されたチャートまたはリポジトリーをユーザーが取得したとき
* データがログに記録される場所
  * helm-api デプロイメント・ログ、Elasticsearch
* データの削除方法
  * Elasticsearch API を使用して、helm-api ログ・データを検索して削除する

### {{site.data.keyword.ieam}} サービス・ブローカー

* ログに記録されるデータ
  * ユーザー ID (デバッグ・ログ・レベル 10 の場合のみ、デフォルトのログ・レベルでは記録されない)
* データがログに記録されるタイミング
  * サービス・ブローカーに API 要求が行われたとき
  * サービス・ブローカーがサービス・カタログにアクセスしたとき
* データがログに記録される場所
  * サービス・ブローカー・コンテナー・ログ、Elasticsearch
* データの削除方法
  * Elasticsearch API を使用する apiserver ログを検索して削除する
  * apiserver コンテナーでログを検索して削除する
      ```
      kubectl logs $(kubectl get pods -n kube-system | grep  service-catalogapiserver | awk '{print $1}') -n kube-system | grep admin
      ```
      {: codeblock}


  詳しくは、[Kubernetes kubectl](https://kubernetes.io/docs/reference/kubectl/overview/){:new_window} を参照してください。
