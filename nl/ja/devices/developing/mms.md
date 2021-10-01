---

copyright:
  years: 2019
lastupdated: "2019-06-24"

---

{:shortdesc: .shortdesc}
{:new_window: target="_blank"}
{:codeblock: .codeblock}
{:pre: .pre}
{:screen: .screen}
{:tip: .tip}
{:download: .download}

# モデル管理システム・サービス (MMS) を使用するエッジ・サービス
{: #mms}

このサンプルは、モデル管理システム (MMS) を使用する {{site.data.keyword.edge_service}} を開発する方法を理解するのに役立ちます。 このシステムを使用して、エッジ・ノードで実行されるエッジ・サービスによって使用される機械学習モデルをデプロイしたり、更新したりすることができます。
{:shortdesc}

## 始める前に
{: #mms_begin}

[エッジ・サービス作成の準備](service_containers.md)の前提条件ステップを実行してください。 その結果、以下の環境変数が設定され、以下のコマンドがインストールされ、以下のファイルが存在していなければなりません。

```bash
echo "HZN_ORG_ID=$HZN_ORG_ID, HZN_EXCHANGE_USER_AUTH=$HZN_EXCHANGE_USER_AUTH, DOCKER_HUB_ID=$DOCKER_HUB_ID"
which git jq make
ls ~/.hzn/keys/service.private.key ~/.hzn/keys/service.public.pem
cat /etc/default/horizon
```

## 手順
{: #mms_procedure}

このサンプルは、[{{site.data.keyword.horizon_open}} ![新しいタブで開く](../../images/icons/launch-glyph.svg "新しいタブで開く")](https://github.com/open-horizon/) オープン・ソース・プロジェクトの一部です。 [Creating Your Own Hello MMS Edge Service ![新しいタブで開く](../../images/icons/launch-glyph.svg "新しいタブで開く")](https://github.com/open-horizon/examples/blob/master/edge/services/helloMMS/CreateService.md) の手順に従った後、ここに戻ってください。

## 次の作業
{: #mms_what_next}

* [{{site.data.keyword.edge_devices_notm}} を使用したエッジ・サービスの開発](developing.md)にある他のエッジ・サービスのサンプルを試してください。

## 参考文献

* [モデル管理システム](model_management_system.md)
