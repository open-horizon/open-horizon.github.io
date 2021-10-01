---

copyright:
years: 2020
lastupdated: "2020-10-28"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# マルチテナンシー
{: #multit}

## {{site.data.keyword.edge_notm}} のテナント
{: #tenants}

{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) では、組織を介したマルチテナンシーという一般的な IT の概念がサポートされます。マルチテナンシーでは、各テナントに独自の組織が含まれます。 組織によってリソースが分離されます。したがって、各組織内のユーザーは別の組織のリソースを作成および変更できません。 さらに、リソースが公開としてマークされていない限り、組織内のリソースを表示できるのは、その組織内のユーザーのみです。

### 一般的なユース・ケース

{{site.data.keyword.ieam}} でマルチテナンシーを利用するために、以下の 2 つの大まかなユース・ケースを使用します。

* 企業に複数の事業単位があり、各事業単位が同じ {{site.data.keyword.ieam}} 管理ハブ内の別個の組織である。 各事業単位が、他の事業単位からデフォルトではアクセスできない独自の一連の {{site.data.keyword.ieam}} リソースを備えた別個の組織でなければならない法的、ビジネス上、技術的な理由を検討してください。 別個の組織を使用する場合でも、企業では、組織管理者の共通グループを使用してすべての組織を管理することができます。
* 企業で、顧客用のサービスとして {{site.data.keyword.ieam}} をホストし、各顧客が管理ハブ内に 1 つ以上の組織を持つ。 この場合、組織管理者は、各顧客に固有です。

選択したユース・ケースにより、{{site.data.keyword.ieam}} および Identity and Access Manager ([IAM](https://www.ibm.com/support/knowledgecenter/SSHKN6/iam/landing_iam.html)) を構成する方法が決まります。

### {{site.data.keyword.ieam}} ユーザーのタイプ
{: #user-types}

{{site.data.keyword.ieam}} では、以下のユーザー役割がサポートされます。

| **役割** | **アクセス権限** |
|--------------|-----------------|
| **ハブ管理者** | 必要に応じて組織を作成、変更、削除したり、各組織内に組織管理者を作成したりして、{{site.data.keyword.ieam}} 組織のリストを管理します。 |
| **組織管理者** | 1 つ以上の {{site.data.keyword.ieam}} 組織のリソースを管理します。 組織管理者は、リソースの所有者でない場合でも、組織内の任意のリソース (ユーザー、ノード、サービス、ポリシー、またはパターン) を作成、表示、変更できます。 |
| **通常ユーザー** | 組織内でノード、サービス、ポリシー、およびパターンを作成したり、自分が作成したリソースを変更または削除したりします。 他のユーザーが作成した、組織内のすべてのサービス、ポリシー、およびパターンを表示できます。 |
{: caption="表 1. {{site.data.keyword.ieam}} ユーザーの役割" caption-side="top"}

すべての {{site.data.keyword.ieam}} の役割の説明については、『[役割ベースのアクセス制御](../user_management/rbac.md)』を参照してください。

## IAM と {{site.data.keyword.ieam}} の関係
{: #iam-to-ieam}

IAM (Identity and Access Manager) サービスは、{{site.data.keyword.ieam}} を含むすべての Cloud Pak ベースの製品のユーザーを管理します。 IAM は LDAP を使用してユーザーを保管します。 各 IAM ユーザーは、1 つ以上の IAM チームのメンバーになることができます。 各 IAM チームが 1 つの IAM アカウントに関連付けられているため、IAM ユーザーは、間接的に 1 つ以上の IAM アカウントのメンバーになることができます。 詳しくは、[IAM のマルチテナンシー](https://www.ibm.com/support/knowledgecenter/SSHKN6/iam/3.x.x/multitenancy/multitenancy.html)を参照してください。

{{site.data.keyword.ieam}} Exchange は、他の {{site.data.keyword.ieam}} コンポーネントの認証および許可サービスを提供します。 Exchange はユーザーの認証を IAM に委任します。つまり、IAM ユーザー資格情報が Exchange に渡され、IAM を利用してその資格情報が有効かどうかが判別されます。 各ユーザー役割 (ハブ管理者、組織管理者、または通常ユーザー) が Exchange で定義され、それにより、ユーザーが {{site.data.keyword.ieam}} で実行できるアクションが決まります。

{{site.data.keyword.ieam}} Exchange 内の各組織は、IAM アカウントに関連付けられます。 したがって、IAM アカウント内の IAM ユーザーは自動的に、対応する {{site.data.keyword.ieam}} 組織のメンバーになります。 このルールに 1 つ例外があり、{{site.data.keyword.ieam}} ハブ管理者役割は、特定の組織に属していないと見なされるため、ハブ管理者 IAM ユーザーがどの IAMアカウントに属しているのかは重要ではありません。

IAM と {{site.data.keyword.ieam}} 間の対応を要約すると、以下のようになります。

| **IAM** | **関係** | **{{site.data.keyword.ieam}}** |
|--------------|----------|-----------------|
| IAM アカウント | → | {{site.data.keyword.ieam}} 組織 |
| IAM ユーザー | → | {{site.data.keyword.ieam}} ユーザー |
| IAM には役割に対応するものはありません | なし | {{site.data.keyword.ieam}} 役割 |
{: caption="表 2. IAM と {{site.data.keyword.ieam}} の対応関係" caption-side="top"}

{{site.data.keyword.ieam}} コンソールへのログインに使用する資格情報は、IAM ユーザーおよびパスワードです。 {{site.data.keyword.ieam}} CLI (`hzn`) で使用する資格情報は、IAM API 鍵です。

## 初期組織
{: #initial-org}

デフォルトでは、組織は、{{site.data.keyword.ieam}} のインストール時に、指定した名前で作成されます。 {{site.data.keyword.ieam}} のマルチテナント機能が不要な場合、{{site.data.keyword.ieam}} を使用するにはこの初期組織で十分であり、このページの残りの部分をスキップしてかまいません。

## ハブ管理者ユーザーの作成
{: #create-hub-admin}

{{site.data.keyword.ieam}} のマルチテナンシーを使用する最初のステップとして、組織を作成および管理できる 1 人以上のハブ管理者を作成します。 これを行う前に、ハブ管理者役割が割り当てられたユーザーおよび IAM アカウントを作成または選択する必要があります。

1. `cloudctl` を使用して、{{site.data.keyword.ieam}} 管理ハブにクラスター管理者としてログインします。 (`cloudctl` がまだインストールされていない場合は、『[cloudctl、kubectl、および oc のインストール](../cli/cloudctl_oc_cli.md)』の説明を参照してください)。

   ```bash
   cloudctl login -a <cluster-url> -u admin -p <password> --skip-ssl-validation
   ```
   {: codeblock}

2. LDAP インスタンスが IAM にまだ接続されていない場合は、『[LDAP ディレクトリーへの接続](https://www.ibm.com/support/knowledgecenter/SSHKN6/iam/3.x.x/configure_ldap.html)』に従って、ここで接続します。

3. ハブ管理者ユーザーは、IAM アカウントに属している必要があります。 (どのアカウントであっても構いません)。 ハブ管理者ユーザーを所属させる IAM アカウントがまだない場合は、以下のように作成します。

   ```bash
   IAM_ACCOUNT_NAME='hub admin account'   # or choose another name
   cloudctl iam account-create "$IAM_ACCOUNT_NAME" -d 'account for the hub admin users'
   IAM_ACCOUNT_ID=$(cloudctl iam account "$IAM_ACCOUNT_NAME" | grep -E '^ID' | awk '{print $2}')
   IAM_TEAM_ID=$(cloudctl iam teams -s | grep -m 1 "$IAM_ACCOUNT_NAME" | awk '{print $1}')
   ```
   {: codeblock}

4. {{site.data.keyword.ieam}} ハブ管理者役割専用の LDAP ユーザーを作成または選択します。 {{site.data.keyword.ieam}} ハブ管理者と {{site.data.keyword.ieam}}組織管理者 (または通常の {{site.data.keyword.ieam}} ユーザー) として同じユーザーを使用しないでください。

5. 以下のように、ユーザーを IAM にインポートします。

   ```bash
   HUB_ADMIN_USER=<the IAM/LDAP user name of the hub admin user>
   cloudctl iam user-import -u $HUB_ADMIN_USER
   cloudctl iam user-onboard $IAM_ACCOUNT_ID -r PRIMARY_OWNER -u $HUB_ADMIN_USER
   IAM_RESOURCE_ID=$(cloudctl iam resources | grep ':n/ibm-edge:')
   cloudctl iam resource-add $IAM_TEAM_ID -r $IAM_RESOURCE_ID
   ```
   {: codeblock}

6. 以下のように、ハブ管理者役割を IAM ユーザーに割り当てます。

   ```bash
   EXCHANGE_ROOT_PW=<password for the exchange root user>
   export HZN_ORG_ID=root
   export HZN_EXCHANGE_USER_AUTH=root/root:$EXCHANGE_ROOT_PW
   export HZN_EXCHANGE_URL=<the URL of your exchange>
   hzn exchange user create -H $HUB_ADMIN_USER ""
   ```
   {: codeblock}

7. ユーザーがハブ管理者ユーザー役割を備えていることを確認します。 以下のコマンドの出力で、`"hubAdmin": true` と表示される必要があります。

   ```bash
   hzn exchange user list $HUB_ADMIN_USER
   ```
   {: codeblock}

### {{site.data.keyword.ieam}} CLI でのハブ管理者ユーザーの使用
{: #verify-hub-admin}

以下のように、ハブ管理者ユーザー用の API 鍵を作成し、それがハブ管理者機能を備えていることを確認します。

1. 以下のように `cloudctl` を使用して、{{site.data.keyword.ieam}} 管理ハブにハブ管理者としてログインします。

   ```bash
   cloudctl login -a <cluster-url> -u $HUB_ADMIN_USER -p <hub-admin-password> -c $IAM_ACCOUNT_ID --skip-ssl-validation
   ```
   {: codeblock}

2. 以下のように、ハブ管理者ユーザー用の API 鍵を作成します。

   ```bash
   cloudctl iam api-key-create "${HUB_ADMIN_USER}-api-key" -d "API key for $HUB_ADMIN_USER"
   ```
   {: codeblock}

   **API Key** で始まるコマンド出力行で API 鍵を確認します。 後からシステムで鍵の値を照会することはできないため、後の使用に備えて鍵の値を安全な場所に保存します。 また、後続のコマンド用に以下の変数に設定します。

   ```bash
   HUB_ADMIN_API_KEY=<IAM API key you just created>
   ```
   {: codeblock}

3. 管理ハブですべての組織を表示します。 インストール時に作成された初期組織、**root**、および **IBM** の各組織が表示されます。

   ```bash
   export HZN_ORG_ID=root
   export HZN_EXCHANGE_USER_AUTH=root/iamapikey:$HUB_ADMIN_API_KEY
   hzn exchange org list -o root
   ```
   {: codeblock}

4. ハブ管理者 IAM ユーザーおよびパスワードを使用して、[{{site.data.keyword.ieam}} 管理コンソール](../console/accessing_ui.md)にログインします。 ログイン資格情報がハブ管理者役割を備えているため、組織管理コンソールが表示されます。 このコンソールを使用して、組織を表示、管理、および追加します。 あるいは、以下のセクションの CLI を使用して組織を追加することもできます。

## CLI を使用した組織の作成
{: #create-org}

{{site.data.keyword.ieam}} 組織管理コンソールを使用する代わりに、CLI を使用して組織を作成できます。 組織を作成する前提条件として、組織に関連付けられる IAM アカウントを作成または選択する必要があります。 別の前提条件として、組織管理者役割を割り当てる IAM ユーザーを作成または選択する必要もあります。

**注:**: 組織名に、下線 (_)、コンマ (,)、空白スペース ( )、単一引用符 (')、および疑問符 (?) を含めることはできません。

以下のステップを実行します。

1. 前のセクションのステップを実行して、ハブ管理者ユーザーを作成します (まだ作成していない場合)。 ハブ管理者 API 鍵を以下の変数に設定してください。

   ```bash
   HUB_ADMIN_API_KEY=<IAM API key of the hub admin user>
   ```
   {: codeblock}

2. `cloudctl` を使用して、{{site.data.keyword.ieam}} 管理ハブにクラスター管理者としてログインし、新しい {{site.data.keyword.ieam}} 組織を関連付ける IAM アカウントを作成します。 (`cloudctl` がまだインストールされていない場合は、『[cloudctl、kubectl、および oc のインストール](../cli/cloudctl_oc_cli.md)』を参照してください)。

   ```bash
   cloudctl login -a <cluster-url> -u admin -p <password> --skip-ssl-validation
   NEW_ORG_ID=<new organization name>
   IAM_ACCOUNT_NAME="$NEW_ORG_ID"
   cloudctl iam account-create "$IAM_ACCOUNT_NAME" -d "$IAM_ACCOUNT_NAME account"
   IAM_ACCOUNT_ID=$(cloudctl iam account "$IAM_ACCOUNT_NAME" | grep -E '^ID' | awk '{print $2}')
   IAM_TEAM_ID=$(cloudctl iam teams -s | grep -m 1 "$IAM_ACCOUNT_NAME" | awk '{print $1}')
   ```
   {: codeblock}

3. 組織管理者役割を割り当てる LDAP ユーザーを作成または選択し、IAM にインポートします。 ハブ管理者ユーザーを組織管理者ユーザーとして使用することはできませんが、同じ組織管理者ユーザーを複数の IAM アカウントで使用できます。 それによって、複数の {{site.data.keyword.ieam}} 組織を管理できます。

   ```bash
   ORG_ADMIN_USER=<the IAM/LDAP user name of the organization admin user>
   cloudctl iam user-import -u $ORG_ADMIN_USER
   cloudctl iam user-onboard $IAM_ACCOUNT_ID -r PRIMARY_OWNER -u $ORG_ADMIN_USER
   IAM_RESOURCE_ID=$(cloudctl iam resources | grep ':n/ibm-edge:')
   cloudctl iam resource-add $IAM_TEAM_ID -r $IAM_RESOURCE_ID
   ```
   {: codeblock}

4. 以下の環境変数を設定し、{{site.data.keyword.ieam}} 組織を作成し、その組織が存在していることを確認します。
   ```bash
   export HZN_ORG_ID=root
   export HZN_EXCHANGE_USER_AUTH=root/iamapikey:$HUB_ADMIN_API_KEY
   export HZN_EXCHANGE_URL=<URL of your exchange>
   hzn exchange org create -a IBM/agbot -t "cloud_id=$IAM_ACCOUNT_ID" --description "$NEW_ORG_ID organization" $NEW_ORG_ID
   hzn exchange agbot addpattern IBM/agbot IBM '*' $NEW_ORG_ID
   hzn exchange org list $NEW_ORG_ID
   ```
   {: codeblock}

5. 以下のように、前に選択した IAM ユーザーに組織管理者ユーザー役割を割り当て、そのユーザーが {{site.data.keyword.ieam}} Exchange で作成されていて、組織管理者役割を備えていることを確認します。

   ```bash
   hzn exchange user create -o $NEW_ORG_ID -A $ORG_ADMIN_USER "" "<email-address>"
   hzn exchange user list -o $NEW_ORG_ID $ORG_ADMIN_USER
   ```
   {: codeblock}

   ユーザーのリストで、`"admin": true` と表示される必要があります。

<div class="note"><span class="notetitle">注:</span> 複数の組織を作成し、同じ組織管理者によってすべての組織を管理する場合は、このセクションで毎回 `ORG_ADMIN_USER` に同じ値を使用してください。</div>

これで、組織管理者が [{{site.data.keyword.ieam}} 管理コンソール](../console/accessing_ui.md)を使用して当該組織内の {{site.data.keyword.ieam}} リソースを管理できるようになりました。

### 組織管理者による CLI 使用の有効化

組織管理者は、`hzn exchange` コマンドを使用して {{site.data.keyword.ieam}} リソースを CLI で管理するには、以下のようにする必要があります。

1. 以下のように、`cloudctl` を使用して {{site.data.keyword.ieam}} 管理ハブにログインし、API 鍵を作成します。

   ```bash
   cloudctl login -a <cluster-url> -u $ORG_ADMIN_USER -p <hub-admin-password> -c $IAM_ACCOUNT_ID --skip-ssl-validation
   cloudctl iam api-key-create "${ORG_ADMIN_USER}-api-key" -d "API key for $ORG_ADMIN_USER"
   ```
   {: codeblock}

   **API Key** で始まるコマンド出力行で API 鍵を確認します。 後からシステムで鍵の値を照会することはできないため、後の使用に備えて鍵の値を安全な場所に保存します。 また、後続のコマンド用に以下の変数に設定します。

   ```bash
   ORG_ADMIN_API_KEY=<IAM API key you just created>
   ```
   {: codeblock}

   **ヒント:** 将来追加の IAM アカウントにこのユーザーを追加した場合、アカウントごとに API 鍵を作成する必要はありません。 このユーザーがメンバーとして属しているすべての IAM アカウントで (したがって、このユーザーがメンバーになっているすべての {{site.data.keyword.ieam}} 組織で) 同じ API 鍵が機能します。

2. 以下のように、API 鍵が `hzn exchange` コマンドで機能することを確認します。

   ```bash
   export HZN_ORG_ID=<organization id>
   export HZN_EXCHANGE_USER_AUTH=root/iamapikey:$ORG_ADMIN_API_KEY
   hzn exchange user list
   ```
   {: codeblock}


新しい組織を使用する準備ができました。 当該組織に最大数のエッジ・ノードを設定する場合、あるいはデフォルト・エッジ・ノード・ハートビート設定をカスタマイズする場合は、『[組織の構成](#org-config)』を参照してください。

## 組織内の非管理者ユーザー
{: #org-users}

IAM ユーザーを (`MEMBER` として) 対応する IAM アカウントにインポートおよびオンボードすることで、新規ユーザーを組織に追加できます。 明示的にユーザーを {{site.data.keyword.ieam}} Exchange に追加する必要はありません。これは、必要に応じて自動的に行われるためです。

これにより、ユーザーは [{{site.data.keyword.ieam}} 管理コンソール](../console/accessing_ui.md)を使用できます。 ユーザーは、`hzn exchange` CLI を使用するには、以下のようにする必要があります。

1. 以下のように、`cloudctl` を使用して {{site.data.keyword.ieam}} 管理ハブにログインし、API 鍵を作成します。

   ```bash
   IAM_USER=<iam user>
   cloudctl login -a <cluster-url> -u $IAM_USER -p <hub-admin-password> -c $IAM_ACCOUNT_ID --skip-ssl-validation
   cloudctl iam api-key-create "${IAM_USER}-api-key" -d "API key for $IAM_USER"
   ```
   {: codeblock}

   **API Key** で始まるコマンド出力行で API 鍵を確認します。 後からシステムで鍵の値を照会することはできないため、後の使用に備えて鍵の値を安全な場所に保存します。 また、後続のコマンド用に以下の変数に設定します。

   ```bash
   IAM_USER_API_KEY=<IAM API key you just created>
   ```
   {: codeblock}

3. 以下の環境変数を設定し、ユーザーを確認します。

```bash
export HZN_ORG_ID=<organization-id>
export HZN_EXCHANGE_USER_AUTH=iamapikey:$IAM_USER_API_KEY
hzn exchange user list
```
{: codeblock}

## IBM 組織
{: #ibm-org}

IBM 組織は、任意の組織の任意のユーザーが使用できるテクノロジーの例を示すことを目的とした事前定義のサービスおよびパターンを提供する固有の組織です。 IBM 組織は、{{site.data.keyword.ieam}} 管理ハブのインストール時に自動的に作成されます。

**注**: IBM 組織内のリソースは公開されていますが、IBM 組織は、{{site.data.keyword.ieam}} 管理ハブ内のすべての公開コンテンツを保持するためのものではありません。

## 組織の構成
{: #org-config}

すべての {{site.data.keyword.ieam}} 組織には以下の設定があります。 多くの場合、これらの設定のデフォルト値で十分です。 設定のいずれかをカスタマイズする場合は、コマンド `hzn exchange org update -h` を実行して、使用できるコマンド・フラグを確認してください。

| **設定** | **説明** |
|--------------|-----------------|
| `description` | 組織の説明。 |
| `label` | 組織の名前。 この値は、{{site.data.keyword.ieam}} 管理コンソールで組織名を表示するために使用されます。 |
| `heartbeatIntervals` | 組織内のエッジ・ノード・エージェントが管理ハブに命令についてポーリングする頻度。 詳しくは、以下のセクションを参照してください。 |
| `limits` | この組織の制限。 現在、制限は `maxNodes` のみであり、これは当該組織で許可される最大エッジ・ノード数です。 単一の {{site.data.keyword.ieam}} 管理ハブでサポートできるエッジ・ノードの総数に実際の制限があります。 この設定により、ハブ管理者ユーザーは、各組織に含めることができるノードの数を制限し、1 つの組織がすべての容量を使用しないようにすることができます。 値 `0` は制限なしを意味します。 |
{: caption="表 3. 組織設定" caption-side="top"}

### エージェントのハートビート・ポーリング間隔
{: #agent-hb}

各エッジ・ノードにインストールされている {{site.data.keyword.ieam}} エージェントは、自身がまだ実行中で接続されていることを管理ハブに知らせ、命令を受信するために、定期的に管理ハブにハートビートを送信します。 これらの設定を変更する必要があるのは、極めて高いスケーリングの環境の場合のみです。

ハートビート間隔は、エージェントが管理ハブに次のハートビートを送信まで待機する時間です。 この間隔は、応答性を最適化し、管理ハブでの負荷を削減するために、時間の経過とともに自動的に調整されます。 間隔の調整は、以下の 3 つの設定によって制御されます。

| **設定** | **説明**|
|-------------|----------------|
| `minInterval` | エージェントが次のハートビートを管理ハブに送信するまで待機する必要がある最短時間 (秒)。 エージェントは、登録されると、この間隔でのポーリングを開始します。 間隔がこの値より短くなることはありません。 値 `0` はデフォルト値の使用を意味します。 |
| `maxInterval` | エージェントが次のハートビートを管理ハブに送信するまで待機する必要がある最長時間 (秒)。 値 `0` はデフォルト値の使用を意味します。 |
| `intervalAdjustment` | エージェントが間隔を伸ばせると検出した場合に現在のハートビート間隔に追加する秒数。 ハートビートを管理ハブに正常に送信したが、しばらく命令を受信しなかった場合、ハートビート間隔は、最大ハートビート間隔に達するまで、徐々に長くなります。 同様に、命令を受信した場合、後続の命令が迅速に処理されるように、ハートビート間隔は短くなります。 値 `0` はデフォルト値の使用を意味します。 |
{: caption="表 4. ハートビート間隔設定" caption-side="top"}

組織内のハートビート・ポーリング間隔設定は、ハートビート間隔が明示的に構成されていないノードに適用されます。 ノードでハートビート間隔設定が明示的に設定されているかどうかを確認するには、`hzn exchange node list <node id>` を使用します。

高スケーリング環境における設定の構成について詳しくは、『[スケーリング構成](../hub/configuration.md#scale)』を参照してください。
