---

copyright:
years: 2021
lastupdated: "2021-08-16"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# シークレットを使用する Hello World
{: #secrets}

この例は、シークレットを使用する{{site.data.keyword.edge_service}}の作成方法を示します。シークレットによって、ログイン資格情報や他の機密情報が確実に保護されます。
{:shortdesc}

## 始める前に
{: #secrets_begin}

[エッジ・サービス作成の準備](service_containers.md)の前提条件ステップを実行してください。 その結果、以下の環境変数が設定され、以下のコマンドがインストールされ、以下のファイルが存在していなければなりません。

```bash
echo "HZN_ORG_ID=$HZN_ORG_ID, HZN_EXCHANGE_USER_AUTH=$HZN_EXCHANGE_USER_AUTH, DOCKER_HUB_ID=$DOCKER_HUB_ID"
which git jq make
ls ~/.hzn/keys/service.private.key ~/.hzn/keys/service.public.pem
cat /etc/default/horizon
```

## 手順
{: #secrets_procedure}

このサンプルは、[{{site.data.keyword.horizon_open}}](https://github.com/open-horizon/) オープン・ソース・プロジェクトの一部です。 [Creating Your Own Hello Secret Service](https://github.com/open-horizon/examples/blob/master/edge/services/helloSecretWorld/CreateService.md) の手順に従った後、ここに戻ってください。

## 次の作業
{: #secrets_what_next}

* [デバイス用のエッジ・サービスの開発](developing.md)にある他のエッジ・サービスのサンプルを試してください。

## 参考文献

* [シークレットの使用](../developing/secrets_details.md)
