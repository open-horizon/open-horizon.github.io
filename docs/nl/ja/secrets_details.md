---

copyright:
years: 2021
lastupdated: "2021-08-16"

---

{:shortdesc: .shortdesc}
{:new_window: target="_blank"}
{:codeblock: .codeblock}
{:pre: .pre}
{:screen: .screen}
{:tip: .tip}
{:download: .download}

# シークレットを使用したサービスの開発
{: #using secrets}

<img src="../images/edge/10_Secrets.svg" style="margin: 3%" alt="シークレットを使用したサービスの開発"> 

# シークレット・マネージャーの詳細
{: #secrets_details}

シークレット・マネージャーは、機密情報 (認証資格情報や暗号鍵など) 用のセキュア・ストレージを提供します。これらのシークレットは {{site.data.keyword.ieam}} により安全にデプロイされ、シークレットを受け取るように構成されたサービスのみがストレージにアクセスできるようになります。[Hello Secret World Example](https://github.com/open-horizon/examples/blob/master/edge/services/helloSecretWorld/CreateService.md) では、エッジ・サービスでシークレットを活用する方法の概要が示されています。

{{site.data.keyword.ieam}} では、シークレット・マネージャーとして [Hashicorp Vault](https://www.vaultproject.io/) の使用をサポートしています。hzn CLI を使用して作成されたシークレットは、[KV V2 Secrets Engine](https://www.vaultproject.io/docs/secrets/kv/kv-v2) を使用して Vault シークレットにマップされます。つまり、各 {{site.data.keyword.ieam}} シークレットの詳細は、鍵と値で構成されます。どちらもシークレットの詳細の一部として保管され、任意のストリング値に設定できます。この機能の一般的な使用法は、鍵に対してシークレットのタイプ、機密情報を値として指定する方法です。例えば、鍵を「basicauth」に、値を「user:password」に設定します。こうすることで、サービス開発者はシークレットのタイプを問い合わせ、サービス・コードが値を正しく処理するように設定できます。

シークレット・マネージャー内のシークレットの名前は、サービス実装によって認識されることはありません。シークレットの名前を使用して Vault からサービス実装に情報を伝達することはできません。

シークレットは、シークレット名にプレフィックスとして openhorizon とユーザー組織を加えた名前で、KV V2 Secrets Engine に保管されます。これにより、{{site.data.keyword.ieam}} ユーザーにより作成されたシークレットは、他の統合による Vault のその他の使用から分離され、マルチテナント分離が確実に維持されるようになります。

シークレット名は、{{site.data.keyword.ieam}} 組織管理者 (またはユーザー・プライベート・シークレット使用時のユーザー) によって管理されます。Vault のアクセス制御リスト (ACL) は、{{site.data.keyword.ieam}} ユーザーが管理できるシークレットを制御します。これは、ユーザー認証を {{site.data.keyword.ieam}} Exchange に委任する Vault の認証プラグインを介して実施されます。ユーザーの認証に成功すると、Vault 内の認証プラグインは、そのユーザーに固有の ACL ポリシー・セットを作成します。Exchange 内で管理特権を持つユーザーは以下が可能です。
- 組織全体のすべてのシークレットの追加、削除、読み取り、およびリスト
- そのユーザー専用のすべてのシークレットの追加、削除、読み取り、およびリスト
- 組織の他のユーザーのユーザー・プライベート・シークレットの削除とリスト、ただし、それらのシークレットの追加や読み取りはできません。

管理特権を持たないユーザーは以下が可能です。
- 組織全体のシークレットすべてのリスト、ただし、シークレットの追加、削除、読み取りはできません。
- そのユーザー専用のすべてのシークレットの追加、削除、読み取り、およびリスト

シークレットをエッジ・ノードにデプロイできるようにするため、{{site.data.keyword.ieam}} Agbot もシークレットにアクセスします。Agbot は、Vault への更新可能なログインを維持し、目的ごとに固有の ACL ポリシーが指定されます。Agbot は以下を行なうことができます。
- 組織全体のシークレットと、組織内のユーザー・プライベート・シークレットの読み取り、ただしそれらのシークレットの追加、削除、リストはできません。

Exchange root ユーザーと Exchange ハブ管理者は Vault 内でアクセス権がありません。これらの役割について詳しくは、[役割ベースのアクセス制御](../user_management/rbac.html)を参照してください。
