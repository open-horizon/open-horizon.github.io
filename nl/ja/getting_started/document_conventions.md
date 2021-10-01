---

copyright:
years: 2020
lastupdated: "2020-04-01"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 本書の規則
{: #document_conventions}

本書では、特定の意味を示すために以下の規則を使用します。  

## コマンド規則

< > に示された変数の内容を、必要な値に置き換えてください。 < > の文字は、コマンドに含めないでください。

### 例

  ```
  hzn key create "<companyname>" "<youremailaddress>"
  ```
  {: codeblock}
   
## リテラル・ストリング

管理ハブまたはコードのコンテンツは、リテラル・ストリングです。 このコンテンツは、**太字**テキストで示されます。
   
 ### 例
   
 `service.sh` コードを調べると、これらおよびその他の構成変数がこのコードの動作を制御するために使用されていることが分かります。 **PUBLISH** は、このコードがメッセージを IBM Event Streams に送信しようとするかどうかを制御します。 **MOCK** は、service.sh が REST API およびその従属サービス (cpu および gps) に連絡しようとするかどうか、または、`service.sh` がフェイク・データを作成するかどうかを制御します。
  
