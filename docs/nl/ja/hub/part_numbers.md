---

copyright:
years: 2020
lastupdated: "2020-02-10"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# パスポート・アドバンテージ
{: #part_numbers}

{{site.data.keyword.ieam}} パッケージをダウンロードするには、以下の手順を実行します。

1. {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) 部品番号を見つけます。
2. [パスポート・アドバンテージ](https://www.ibm.com/software/passportadvantage/) で IBM パスポート・アドバンテージ・オンライン・タブにアクセスし、IBMid を使用してログインします。
2. 次の [{{site.data.keyword.ieam}} パッケージおよび部品番号](#part_numbers_table)にリストされている部品番号を使用してファイルを検索します。
3. ファイルをご使用のコンピューター上のディレクトリーにダウンロードします。

## {{site.data.keyword.ieam}} パッケージおよび部品番号
{: #part_numbers_table}

|部品説明|パスポート・アドバンテージ部品番号|
|----------------|------------------------------|
|{{site.data.keyword.edge_notm}} Resource Value Unit License + SW Subscription & Support 12 Months|D2840LL|
|{{site.data.keyword.edge_notm}} Resource Value Unit ANNUAL SW S&S RNWL 12 months|E0R0HLL|
|{{site.data.keyword.edge_notm}} Resource Value Unit ANNUAL SW S&S REINSTATE 12 months|D2841LL|
|{{site.data.keyword.edge_notm}} Resource Value Unit MONTHLY LICENSE|D283ZLL|
|{{site.data.keyword.edge_notm}} Resource Value Unit Committed Term License|D28I1LL|
{: caption="表 1. {{site.data.keyword.ieam}} パッケージおよび部品番号" caption-side="top"}

## ライセンス交付
{: #licensing}

ライセンス要件は、登録されているノードの合計に基づいて計算されます。 管理ハブに認証するように構成されている **hzn** CLI がインストールされている任意のシステムで、以下のように、登録されているノードの合計を確認します。

  ```
  hzn exchange status | jq .numberOfNodes
  ```
  {: codeblock}

出力は整数です。以下の出力例を参照してください。

  ```
  $ hzn exchange status | jq .numberOfNodes
  2641
  ```

[{{site.data.keyword.ieam}} License document](https://ibm.biz/ieam-43-license) の以下の変換表を使用し、ご使用の環境について前のコマンドで返されたノード数に基づいて、必要なライセンスを計算します。

  ```
  From 1 to 10 Resources, 1.00 UVU per Resource
  From 11 to 50 Resources, 10.0 UVUs plus 0.87 UVUs per Resource above 10
  From 51 to 100 Resources, 44.8 UVUs plus 0.60 UVUs per Resource above 50
  From 101 to 500 Resources, 74.8 UVUs plus 0.25 UVUs per Resource above 100
  From 501 to 1,000 Resources, 174.8.0 UVUs plus 0.20 UVUs per Resource above 500
  From 1,001 to 10,000 Resources, 274.8 UVUs plus 0.07 UVUs per Resource above 1,000
  From 10,001 to 25,000 Resources, 904.8 UVUs plus 0.04 UVUs per Resource above 10,000
  From 25,001 to 50,000 Resources, 1,504.8 UVUs plus 0.03 UVUs per Resource above 25,000
  From 50,001 to 100,000 Resources, 2,254.8 UVUs plus 0.02 UVUs per Resource above 50,000
  For more than 100,000 Resources, 3,254.8 UVUs plus 0.01 UVUs per Resource above 100,000
  ```

以下の例では、**2641** ノードの場合に必要なライセンスの計算について説明します。この場合、**390 以上**のライセンスを購入する必要があります。

  ```
  274.8 + ( .07 * ( 2641 - 1000 ) )
  274.8 + ( .07 * 1641 )
  274.8 + 114.87
  389.67
  ```

## ライセンス・レポート

{{site.data.keyword.edge_notm}} 使用状況は自動的に計算され、クラスターにローカルにインストールされた共通ライセンス・サービスに定期的にアップロードされます。現在の使用状況の表示方法や使用量レポートの生成などを含めて、ライセンス・サービスの詳細について詳しくは、[ライセンス・サービス資料](https://www.ibm.com/docs/en/cpfs?topic=operator-overview)を参照してください。
