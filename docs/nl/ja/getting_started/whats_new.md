---

copyright:
  years: 2019, 2020
lastupdated: "2020-06-10"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 新機能
{: #whatsnew}

{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) {{site.data.keyword.semver}} では、以下が導入されています。

|解決策|説明|
|----------|------|
|シークレット・マネージャー|[シークレット・マネージャー](../OH/docs/getting_started/overview_sm.md)は、機密情報 (認証資格情報や暗号鍵など) 用のセキュア・ストレージを提供します。|
|内部 TLS| オプションで、{{site.data.keyword.ieam}} 管理ハブ内のすべての内部 API 呼び出しに対して TLS を有効にします。|
|拡張エージェント・サポート | Power シングル・サーバーで使用可能 
| Red Hat サポート| Red Hat OpenShift Container Platform 4.6 での管理サポート
|マルチテナント SDO|[Intel© セキュア・デバイス・オンボード](../installing/sdo.md)を使用して、マルチテナント {{site.data.keyword.ieam}} インストール済み環境内のすべての組織にエッジ・デバイスを構成する機能。 |
| OCP サポート| クラスター・エージェントは OCP バージョン 4.6.16 をサポート|
| Ubuntu および RHEL サポート | Ubuntu 20.04.2 および RHEL 8.3 オペレーティング・システムでのエージェント・サポート|
| ネットワーク通信| 依存関係サービス・コンテナーは、ネットワーク別名を介して親サービス・コンテナーと通信できます。 別名は、サービス定義のデプロイメント構成で、そのコンテナーに定義されている親サービスの container-name (コンテナー名) です (https://github.com/open-horizon/anax/blob/master/docs/deployment_string.html#deployment-string-fields)。|

https://www.ibm.com/cloud/edge-application-manager/get-started で {{site.data.keyword.ieam}} の無料トライアルを確認して開始してください。
