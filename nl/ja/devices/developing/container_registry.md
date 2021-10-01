---

copyright:
years: 2019, 2020
lastupdated: "2020-01-22"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# プライベート・コンテナー・レジストリーの使用
{: #container_registry}

エッジ・サービス・イメージに、パブリック・レジストリーに含めるのに適していないアセットが含まれている場合、アクセスが厳密に制御されるプライベート Docker コンテナー・レジストリー (例えば {{site.data.keyword.open_shift}} イメージ・レジストリーまたは {{site.data.keyword.ibm_cloud}} Container Registry) を使用できます。
{:shortdesc}

作業を始める前に、[デバイス用のエッジ・サービスの開発](developing.md)で説明されている手順に従って、少なくとも 1 つのサンプル・エッジ・サービスを作成およびデプロイし、基本的なプロセスに習熟するようにしてください。

このページでは、エッジ・サービス・イメージを保管できる 2 つのレジストリーについて説明します。
* [{{site.data.keyword.open_shift}} イメージ・レジストリーの使用](#ocp_image_registry)
* [{{site.data.keyword.cloud_notm}} Container Registry の使用](#ibm_cloud_container_registry)

{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) でのプライベート・イメージ・レジストリーの使用方法の例としてこれらを使用することもできます。

## {{site.data.keyword.open_shift}} イメージ・レジストリーの使用
{: #ocp_image_registry}

### 始める前に

* [cloudctl コマンド ![新しいタブで開く](../../images/icons/launch-glyph.svg "新しいタブで開く")](https://www.ibm.com/support/knowledgecenter/SSFC4F_1.3.0/cloudctl/install_cli.html) をインストールしていない場合は、インストールします。
* [{{site.data.keyword.open_shift}} oc コマンド ![新しいタブで開く](../../images/icons/launch-glyph.svg "新しいタブで開く")](https://docs.openshift.com/container-platform/4.4/cli_reference/openshift_cli/getting-started-cli.html) をインストールしていない場合は、インストールします。
* {{site.data.keyword.macOS_notm}} では、[homebrew ![新しいタブで開く](../../images/icons/launch-glyph.svg "新しいタブで開く")](https://docs.brew.sh/Installation) を使用して、{{site.data.keyword.open_shift}} **oc** コマンドをインストールできます。

    ```bash
    brew install openshift-cli
    ```
    {: codeblock}

### 手順

注: コマンド構文について詳しくは、[本書の規則](../../getting_started/document_conventions.md)を参照してください。

1. {{site.data.keyword.open_shift}} クラスターにクラスター管理者権限で接続されていることを確認します。

   ```bash
   cloudctl login -a <cluster-url> -u <user> -p <password> -n kube-system --skip-ssl-validation
   ```
   {: codeblock}

2. {{site.data.keyword.open_shift}} イメージ・レジストリーのデフォルト・ルートが、クラスターの外部からアクセス可能であるように作成されているかどうかを判別します。

   ```bash
   oc get route default-route -n openshift-image-registry --template='{{ .spec.host }}'
   ```
   {: codeblock}

   **default-route** が見つからないことがコマンド応答で示される場合、作成します (詳しくは、[Exposing the registry  ![新しいタブで開く](../../images/icons/launch-glyph.svg "新しいタブで開く")](https://docs.openshift.com/container-platform/4.4/registry/securing-exposing-registry.html) を参照してください)。

   ```bash
   oc patch configs.imageregistry.operator.openshift.io/cluster --patch '{"spec":{"defaultRoute":true}}' --type=merge
   ```
   {: codeblock}

3. 使用する必要があるリポジトリー・ルート名を取得します。

   ```bash
   export OCP_DOCKER_HOST=`oc get route default-route -n openshift-image-registry --template='{{ .spec.host }}'`
   ```
   {: codeblock}

4. イメージを格納するための新規プロジェクトを作成します。

   ```bash
   export OCP_PROJECT=<your-new-project>
   oc new-project $OCP_PROJECT
   ```
   {: codeblock}

5. 選択した名前を使用してサービス・アカウントを作成します。

   ```bash
   export OCP_USER=<service-account-name>
   oc create serviceaccount $OCP_USER
   ```
   {: codeblock}

6. 現行プロジェクトのサービス・アカウントに役割を追加します。

   ```bash
   oc policy add-role-to-user edit system:serviceaccount:$OCP_PROJECT:$OCP_USER
   ```
   {: codeblock}

7. サービス・アカウントに割り当てられたトークンを取得します。

   ```bash
   export OCP_TOKEN=`oc serviceaccounts get-token $OCP_USER`
   ```
   {: codeblock}

8. {{site.data.keyword.open_shift}} 証明書を取得し、docker がそれを信頼するようにします。

   ```bash
   echo | openssl s_client -connect $OCP_DOCKER_HOST:443 -showcerts | sed -n "/-----BEGIN CERTIFICATE-----/,/-----END CERTIFICATE-----/p" > ca.crt
   ```
   {: codeblock}

   {{site.data.keyword.linux_notm}} の場合:

   ```bash
   mkdir -p /etc/docker/certs.d/$OCP_DOCKER_HOST
   cp ca.crt /etc/docker/certs.d/$OCP_DOCKER_HOST
   systemctl restart docker.service
   ```
   {: codeblock}

   {{site.data.keyword.macOS_notm}} の場合:

   ```bash
   mkdir -p ~/.docker/certs.d/$OCP_DOCKER_HOST
   cp ca.crt ~/.docker/certs.d/$OCP_DOCKER_HOST
   ```
   {: codeblock}

   {{site.data.keyword.macOS_notm}} の場合、デスクトップ・メニュー・バーの右側にある鯨のアイコンをクリックし、**「Restart」**を選択して、Docker を再始動します。

9. {{site.data.keyword.ocp}} Docker ホストにログインします。

   ```bash
   echo "$OCP_TOKEN" | docker login -u $OCP_USER --password-stdin $OCP_DOCKER_HOST
   ```
   {: codeblock}

10. 以下のパス形式でイメージをビルドします。以下に例を示します。

   ```bash
   export BASE_IMAGE_NAME=myservice
   docker build -t $OCP_DOCKER_HOST/$OCP_PROJECT/${BASE_IMAGE_NAME}_amd64:1.2.3 -f ./Dockerfile.amd64 .
   ```
   {: codeblock}

11. エッジ・サービスを公開するための準備として、**service.definition.json** ファイルを変更して、**deployment** セクションでイメージ・レジストリー・パスが参照されるようにします。 以下を使用して、そのようなサービスおよびパターンの定義ファイルを作成できます。

   ```bash
   hzn dev service new -s $BASE_IMAGE_NAME -i $OCP_DOCKER_HOST/$OCP_PROJECT/$BASE_IMAGE_NAME
   ```
   {: codeblock}

   **&lt;base-image-name&gt;** は、アーキテクチャーまたはバージョンがない基本イメージ名にする必要があります。 次に、必要に応じて、作成されたファイル **horizon/hzn.json** 内の変数を編集できます。

   あるいは、独自のサービス定義ファイルを作成済みの場合、**deployment.services.&lt;service-name&gt;.image** フィールドでイメージ・レジストリー・パスが参照されていることを確認します。

12. サービス・イメージを公開する準備ができたら、イメージをプライベート・コンテナー・レジストリーにプッシュし、イメージを {{site.data.keyword.horizon}} Exchange に公開します。

   ```bash
   hzn exchange service publish -r "$OCP_DOCKER_HOST:$OCP_USER:$OCP_TOKEN" -f horizon/service.definition.json
   ```
   {: codeblock}

   **-r "$OCP_DOCKER_HOST:$OCP_USER:$OCP_TOKEN"** 引数は、{{site.data.keyword.horizon_open}} エッジ・ノードに資格情報を提供して、サービス・イメージをプルできるようにします。

   このコマンドは、以下のタスクを実行します。

   * Docker イメージを {{site.data.keyword.cloud_notm}} Container Registry にプッシュし、プロセス中のイメージのダイジェストを取得します。
   * 秘密鍵を使用してダイジェストおよびデプロイメント情報に署名します。
   * サービス・メタデータ (署名を含む) を {{site.data.keyword.horizon}} Exchange に入れます。
   * 公開鍵を {{site.data.keyword.horizon}} Exchange のサービス定義の下に入れて、必要なときに {{site.data.keyword.horizon}} エッジ・ノードが定義を自動的に取得して署名を検証できるようにします。
   * OpenShift ユーザーおよびトークンを {{site.data.keyword.horizon}} Exchange のサービス定義の下に入れて、必要なときに {{site.data.keyword.horizon}} エッジ・ノードが定義を自動的に取得できるようにします。
   
### {{site.data.keyword.horizon}} エッジ・ノード上のサービスの使用
{: #using_service}

エッジ・ノードが {{site.data.keyword.ocp}} イメージ・レジストリーから必要なサービス・イメージをプルするのを許可するため、{{site.data.keyword.open_shift}} 証明書を信頼するように各エッジ・ノード上の Docker を構成する必要があります。 **ca.crt** ファイルを各エッジ・ノードにコピーしてから、次のようにします。

{{site.data.keyword.linux_notm}} の場合:

```bash
mkdir -p /etc/docker/certs.d/$OCP_DOCKER_HOST
   cp ca.crt /etc/docker/certs.d/$OCP_DOCKER_HOST
   systemctl restart docker.service
```
{: codeblock}

{{site.data.keyword.macOS_notm}} の場合:

```bash
mkdir -p ~/.docker/certs.d/$OCP_DOCKER_HOST
   cp ca.crt ~/.docker/certs.d/$OCP_DOCKER_HOST
```
{: codeblock}

{{site.data.keyword.macOS_notm}} の場合、デスクトップ・メニュー・バーの右側にある鯨のアイコンをクリックし、**「Restart」**を選択して、Docker を再始動します。

これで、{{site.data.keyword.horizon}} には、このエッジ・サービス・イメージを {{site.data.keyword.open_shift}} イメージ・レジストリーから取得し、作成したデプロイメント・パターンまたはポリシーでの指定に従ってそれをエッジ・ノードにデプロイするために必要なものがすべて揃いました。

## {{site.data.keyword.cloud_notm}} Container Registry の使用
{: #ibm_cloud_container_registry}

### 始める前に

* [{{site.data.keyword.cloud_notm}} CLI ツール (ibmcloud) ![新しいタブで開く](../../images/icons/launch-glyph.svg "新しいタブで開く")](https://cloud.ibm.com/docs/cli?topic=cloud-cli-install-ibmcloud-cli) をインストールします。
* {{site.data.keyword.cloud_notm}} アカウント内で**クラスター管理者**または**チーム管理者**のアクセス権限レベルを持っていることを確認します。

### 手順

1. {{site.data.keyword.cloud_notm}} にログインし、組織をターゲットにします。

   ```bash
   ibmcloud login -a cloud.ibm.com -u <cloud-username> -p <cloud-password
   ibmcloud target -o <organization-id> -s <space-id>
   ```
   {: codeblock}

   組織 ID およびスペース ID が分からない場合は、[{{site.data.keyword.cloud_notm}} コンソール ![新しいタブで開く](../../images/icons/launch-glyph.svg "新しいタブで開く")](https://cloud.ibm.com/) にログインして、それらを見つけるか、作成することができます。

2. クラウド API 鍵を作成します。

   ```bash
   ibmcloud iam api-key-create <key-name> -d "<key-description>"
   ```
   {: codeblock}

   API 鍵の値 (**API Key** で始まる行に表示される) を安全な場所に保存し、以下の環境変数に設定します。

   ```bash
   export CLOUD_API_KEY=<your-cloud-api-key>
   ```
   {: codeblock}

   注: この API 鍵は、`hzn` コマンドで使用するために作成した {{site.data.keyword.open_shift}} API 鍵とは異なります。

3. container-registry プラグインを取得し、プライベート・レジストリー名前空間を作成します。 (このレジストリー名前空間は、Docker イメージの識別に使用されるパスの一部になります。)

   ```bash
   ibmcloud plugin install container-registry
   export REGISTRY_NAMESPACE=<your-registry-namespace>
   ibmcloud cr namespace-add $REGISTRY_NAMESPACE
   ```
   {: codeblock}

4. Docker レジストリー名前空間にログインします。

   ```bash
   ibmcloud cr login
   ```
   {: codeblock}

   **ibmcloud cr** の使用について詳しくは、[ibmcloud cr CLI Web 資料 ![新しいタブで開く](../../images/icons/launch-glyph.svg "新しいタブで開く")](https://cloud.ibm.com/docs/services/Registry/) を参照してください。 以下のコマンドを実行してヘルプ情報を表示することもできます。

   ```bash
   ibmcloud cr --help
   ```
   {: codeblock}

   {{site.data.keyword.cloud_registry}} 内のプライベート名前空間にログインした後、レジストリーにログインするために `docker login` を使用する必要はありません。 **docker push** コマンドおよび **docker pull** コマンド内で以下のようなコンテナー・レジストリー・パスを使用できます。

   ```bash
   us.icr.io/$REGISTRY_NAMESPACE/<base-image-name>_<arch>:<version>
   ```
   {: codeblock}

5. 以下のパス形式でイメージをビルドします。以下に例を示します。

   ```bash
   export BASE_IMAGE_NAME=myservice
   docker build -t us.icr.io/$REGISTRY_NAMESPACE/${BASE_IMAGE_NAME}_amd64:1.2.3 -f ./Dockerfile.amd64 .
   ```
   {: codeblock}

6. エッジ・サービスを公開するための準備として、**service.definition.json** ファイルを変更して、**deployment** セクションでイメージ・レジストリー・パスが参照されるようにします。 以下を使用して、そのようなサービスおよびパターンの定義ファイルを作成できます。

   ```bash
   hzn dev service new -s $BASE_IMAGE_NAME -i us.icr.io/$REGISTRY_NAMESPACE/$BASE_IMAGE_NAME
   ```
   {: codeblock}

   **&lt;base-image-name&gt;** は、アーキテクチャーまたはバージョンがない基本イメージ名にする必要があります。 次に、必要に応じて、作成されたファイル **horizon/hzn.json** 内の変数を編集できます。

   あるいは、独自のサービス定義ファイルを作成済みの場合、**deployment.services.&lt;service-name&gt;.image** フィールドでイメージ・レジストリー・パスが参照されていることを確認します。

7. サービス・イメージを公開する準備ができたら、イメージをプライベート・コンテナー・レジストリーにプッシュし、イメージを {{site.data.keyword.horizon}} Exchange に公開します。

   ```bash
   hzn exchange service publish -r "us.icr.io:iamapikey:$CLOUD_API_KEY" -f horizon/service.definition.json
   ```
   {: codeblock}

   **-r "us.icr.io:iamapikey:$CLOUD_API_KEY"** 引数は、{{site.data.keyword.horizon_open}} エッジ・ノードに資格情報を提供して、サービス・イメージをプルできるようにします。

   このコマンドは、以下のタスクを実行します。

   * Docker イメージを {{site.data.keyword.cloud_notm}} Container Registry にプッシュし、プロセス中のイメージのダイジェストを取得します。
   * 秘密鍵を使用してダイジェストおよびデプロイメント情報に署名します。
   * サービス・メタデータ (署名を含む) を {{site.data.keyword.horizon}} Exchange に入れます。
   * 公開鍵を {{site.data.keyword.horizon}} Exchange のサービス定義の下に入れて、必要なときに {{site.data.keyword.horizon}} エッジ・ノードが定義を自動的に取得して署名を検証できるようにします。
   * {{site.data.keyword.cloud_notm}} API 鍵を {{site.data.keyword.horizon}} Exchange のサービス定義の下に入れて、必要なときに {{site.data.keyword.horizon}} エッジ・ノードが定義を自動的に取得できるようにします。

8. サービス・イメージが {{site.data.keyword.cloud_notm}} Container Registry にプッシュされたことを確認します。

   ```bash
   ibmcloud cr images
   ```
   {: codeblock}

9. サービスをいくつかのエッジ・ノードにデプロイするデプロイメント・パターンまたはポリシーを公開します。 以下に例を示します。

   ```bash
   hzn exchange pattern publish -f horizon/pattern.json
   ```
   {: codeblock}

これで、{{site.data.keyword.horizon}} には、このエッジ・サービス・イメージを {{site.data.keyword.cloud_notm}} Container Registry から取得し、作成したデプロイメント・パターンまたはポリシーでの指定に従ってそれをエッジ・ノードにデプロイするために必要なものがすべて揃いました。
