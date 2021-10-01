---

copyright:
years: 2019
lastupdated: "2019-09-27"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 役割ベースのアクセス制御
{: #rbac}

{{site.data.keyword.edge_notm}} {{site.data.keyword.ieam}} は複数の役割をサポートします。 役割は、実行できるアクションを決定します。
{:shortdesc}

## 組織
{: #orgs}

{{site.data.keyword.ieam}} 内で、組織はリソースへのアクセスを分離するために使用されます。 組織用のリソースは、それらのリソースがパブリックとして明示的にマークされていない限り、その組織でのみ表示できます。パブリックとしてマークされたリソースは、全組織で表示できる唯一のリソースです。

IBM 組織は、事前定義されたサービスおよびパターンを提供するために使用されます。

{{site.data.keyword.ieam}} 内では、組織名はクラスターの名前です。

## ID
{: #ids}

{{site.data.keyword.ieam}} では、以下の 3 つのタイプの ID があります。

* ユーザーには 2 つのタイプがあります。ユーザーは、{{site.data.keyword.ieam}} コンソールおよび Exchange にアクセスできます。
  * ID とアクセス管理 (IAM) ユーザー。IAM ユーザーは、{{site.data.keyword.ieam}} Exchange によって認識されます。
    * IAM は LDAP プラグインを提供しているため、IAM に接続された LDAP ユーザーは IAM ユーザーのように動作します。
    * IAM API 鍵 (**hzn** コマンドで使用される) は IAM ユーザーのように動作します。
  * ローカル Exchange ユーザー: Exchange root ユーザーは、この一例です。通常、他のローカル Exchange ユーザーを作成する必要はありません。
* ノード (エッジ・デバイスまたはエッジ・クラスター)
* agbot

### 役割ベースのアクセス制御 (RBAC)
{: #rbac_roles}

{{site.data.keyword.ieam}} には、以下の役割があります。

| **役割**    | **アクセス権限**    |  
|---------------|--------------------|
| Exchange root ユーザー | Exchange 内での無制限の特権を持ちます。このユーザーは、Exchange 構成ファイルに定義されます。必要に応じて無効にすることができます。|
| 管理ユーザーまたは API 鍵 | 組織内での無制限の特権を持ちます。|
| 非管理ユーザーまたは API 鍵 | 組織内に Exchange リソース (ノード、サービス、パターン、ポリシー) を作成できます。このユーザーが所有するリソースを更新または削除できます。組織内のすべてのサービス、パターン、およびポリシーと、他の組織内のパブリックなサービスおよびパターンを読み取ることができます。|
| ノード (Nodes) |Exchange 内の独自のノードを読み取ることができ、組織内のすべてのサービス、パターン、およびポリシーと、他の組織内のパブリックなサービスおよびパターンを読み取ることができます。|
| agbot | IBM 組織内の agbot は、すべての組織内のすべてのノード、サービス、パターン、およびポリシーを読み取ることができます。|
{: caption="表 1. RBAC の役割" caption-side="top"}
