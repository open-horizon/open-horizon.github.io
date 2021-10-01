---

copyright:
years: 2019
lastupdated: "2019-06-24"  

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 独自の Hello World エッジ・サービスの作成
{: #dev_start_ex}

以下のサンプルでは、単純な `Hello World` サービスが使用されており、{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) での開発についての詳細を確認するのに役立ちます。 このサンプルでは、3 つのハードウェア・アーキテクチャーをサポートし、{{site.data.keyword.horizon}} 開発ツールを使用する単一のエッジ・サービスを開発します。
{:shortdesc}

## 始める前に
{: #dev_start_ex_begin}

[エッジ・サービス作成の準備](service_containers.md)の前提条件ステップを実行してください。 その結果、以下の環境変数が設定され、以下のコマンドがインストールされ、以下のファイルが存在していなければなりません。
```
echo "HZN_ORG_ID=$HZN_ORG_ID, HZN_EXCHANGE_USER_AUTH=$HZN_EXCHANGE_USER_AUTH, DOCKER_HUB_ID=$DOCKER_HUB_ID"
which git jq make
ls ~/.hzn/keys/service.private.key ~/.hzn/keys/service.public.pem
cat /etc/default/horizon
```
{: codeblock}

## 手順
{: #dev_start_ex_procedure}

このサンプルは、[{{site.data.keyword.horizon_open}}](https://github.com/open-horizon/) オープン・ソース・プロジェクトの一部です。 [独自の Hello World サンプル・エッジ・サービスのビルドと公開](https://github.com/open-horizon/examples/blob/master/edge/services/helloworld/CreateService.md#build-publish-your-hw) のステップに従ってから、ここに戻ってください。

## 次の作業
{: #dev_start_ex_what_next}

* [デバイス用のエッジ・サービスの開発](../OH/docs/developing/developing.md)にある他のエッジ・サービスのサンプルを試してください。
