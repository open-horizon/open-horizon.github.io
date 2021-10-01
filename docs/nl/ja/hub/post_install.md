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

# インストール後の構成

## 前提条件

* [IBM Cloud Pak CLI (**cloudctl**) および OpenShift クライアント CLI (**oc**)](../cli/cloudctl_oc_cli.md)
* [**jq**](https://stedolan.github.io/jq/download/)
* [**git**](https://git-scm.com/downloads)
* [**docker**](https://docs.docker.com/get-docker/) バージョン 1.13 以上
* **make**

## インストールの検査

1. 『[{{site.data.keyword.ieam}} のインストール](online_installation.md)』のステップを実行します。
2. 以下のようにして、{{site.data.keyword.ieam}} 名前空間内のすべてのポッドが **Running** または **Completed** であることを確認します。

   ```
   oc get pods
   ```
   {: codeblock}

   これは、ローカル・データベースおよびローカルのシークレット・マネージャーがインストールされている場合に表示される内容の例です。一部の初期化のための再始動は予期されたものですが、通常、複数回の再始動は問題を示しています。
   ```
   $ oc get pods
   NAME                                           READY   STATUS      RESTARTS   AGE
   create-agbotdb-cluster-j4fnb                   0/1     Completed   0          88m
   create-exchangedb-cluster-hzlxm                0/1     Completed   0          88m
   ibm-common-service-operator-68b46458dc-nv2mn   1/1     Running     0          103m
   ibm-eamhub-controller-manager-7bf99c5fc8-7xdts 1/1     Running     0          103m
   ibm-edge-agbot-5546dfd7f4-4prgr                1/1     Running     0          81m
   ibm-edge-agbot-5546dfd7f4-sck6h                1/1     Running     0          81m
   ibm-edge-agbotdb-keeper-0                      1/1     Running     0          88m
   ibm-edge-agbotdb-keeper-1                      1/1     Running     0          87m
   ibm-edge-agbotdb-keeper-2                      1/1     Running     0          86m
   ibm-edge-agbotdb-proxy-7447f6658f-7wvdh        1/1     Running     0          88m
   ibm-edge-agbotdb-proxy-7447f6658f-8r56d        1/1     Running     0          88m
   ibm-edge-agbotdb-proxy-7447f6658f-g4hls        1/1     Running     0          88m
   ibm-edge-agbotdb-sentinel-5766f666f4-5qm9x     1/1     Running     0          88m
   ibm-edge-agbotdb-sentinel-5766f666f4-5whgr     1/1     Running     0          88m
   ibm-edge-agbotdb-sentinel-5766f666f4-9xjpr     1/1     Running     0          88m
   ibm-edge-css-5c59c9d6b6-kqfnn                  1/1     Running     0          81m
   ibm-edge-css-5c59c9d6b6-sp84w                  1/1     Running     0          81m
   ibm-edge-css-5c59c9d6b6-wf84s                  1/1     Running     0          81m
   ibm-edge-cssdb-server-0                        1/1     Running     0          88m
   ibm-edge-exchange-b6647db8d-k97r8              1/1     Running     0          81m
   ibm-edge-exchange-b6647db8d-kkcvs              1/1     Running     0          81m
   ibm-edge-exchange-b6647db8d-q5ttc              1/1     Running     0          81m
   ibm-edge-exchangedb-keeper-0                   1/1     Running     1          88m
   ibm-edge-exchangedb-keeper-1                   1/1     Running     0          85m
   ibm-edge-exchangedb-keeper-2                   1/1     Running     0          84m
   ibm-edge-exchangedb-proxy-6bbd5b485-cx2v8      1/1     Running     0          88m
   ibm-edge-exchangedb-proxy-6bbd5b485-hs27d      1/1     Running     0          88m
   ibm-edge-exchangedb-proxy-6bbd5b485-htldr      1/1     Running     0          88m
   ibm-edge-exchangedb-sentinel-6d685bf96-hz59z   1/1     Running     1          88m
   ibm-edge-exchangedb-sentinel-6d685bf96-m4bdh   1/1     Running     0          88m
   ibm-edge-exchangedb-sentinel-6d685bf96-mxv2b   1/1     Running     1          88m
   ibm-edge-sdo-0                                 1/1     Running     0          81m
   ibm-edge-ui-545d694f6c-4rnrf                   1/1     Running     0          81m
   ibm-edge-ui-545d694f6c-97ptz                   1/1     Running     0          81m
   ibm-edge-ui-545d694f6c-f7bf6                   1/1     Running     0          81m
   ibm-edge-vault-0                               1/1     Running     0          81m
   ibm-edge-vault-bootstrap-k8km9                 0/1     Completed   0          80m
   ```
   {: codeblock}

   **注**:
   * リソースまたはスケジューリングの問題が原因で **Pending** 状態になっているポッドについて詳しくは、[クラスターのサイジング](cluster_sizing.md)に関するページを参照してください。 これには、コンポーネントのスケジューリングのコストを削減する方法に関する情報が含まれています。
   * 他のエラーについて詳しくは、[トラブルシューティング](../admin/troubleshooting.md)を参照してください。
3. 以下のようにして、**ibm-common-services** 名前空間内のすべてのポッドが **Running** または **Completed** であることを確認します。

   ```
   oc get pods -n ibm-common-services
   ```
   {: codeblock}

4. [Entitled Registry](https://myibm.ibm.com/products-services/containerlibrary) を介してライセンス・キーを使用して、ログインし、エージェント・バンドルをプルし、解凍します。
    ```
    docker login cp.icr.io --username cp && \
    docker rm -f ibm-eam-{{site.data.keyword.semver}}-bundle; \
    docker create --name ibm-eam-{{site.data.keyword.semver}}-bundle cp.icr.io/cp/ieam/ibm-eam-bundle:{{site.data.keyword.anax_ver}} bash && \
    docker cp ibm-eam-{{site.data.keyword.semver}}-bundle:/ibm-eam-{{site.data.keyword.semver}}-bundle.tar.gz ibm-eam-{{site.data.keyword.semver}}-bundle.tar.gz && \
    tar -zxvf ibm-eam-{{site.data.keyword.semver}}-bundle.tar.gz && \
    cd ibm-eam-{{site.data.keyword.semver}}-bundle/tools
    ```
    {: codeblock}
5. 以下のようにして、インストールの状態を検証します。
    ```
    ./service_healthcheck.sh
    ```
    {: codeblock}

    出力は以下の例のようになります。
    ```
    $ ./service_healthcheck.sh
    ==Running service verification tests for IBM Edge Application Manager==
    SUCCESS: IBM Edge Application Manager Exchange API is operational
    SUCCESS: IBM Edge Application Manager Cloud Sync Service is operational
    SUCCESS: IBM Edge Application Manager Agbot database heartbeat is current
    SUCCESS: IBM Edge Application Manager SDO API is operational
    SUCCESS: IBM Edge Application Manager UI is properly requiring valid authentication
    ==All expected services are up and running==
    ```

   * **service_healthcheck.sh** コマンドの失敗が生じた場合、下記のコマンドの実行中に問題が発生した場合、あるいは実行時に問題が発生した場合は、[トラブルシューティング](../admin/troubleshooting.md)を参照してください。

## インストール後の構成
{: #postconfig}

以下のプロセスは、**hzn** CLI のインストールをサポートするホスト上で実行する必要があります。現在これをインストールできるのは、Debian/apt ベースの Linux、amd64 Red Hat/rpm Linux、または macOS ホストです。 これらのステップでは、『インストールの検査』セクションで PPA からダウンロードしたのと同じメディアを使用しています。

1. サポートされるプラットフォームの手順を使用して、**hzn** CLI をインストールします。
  * **agent** ディレクトリーに移動し、エージェント・ファイルを解凍します。
    ```
    cd ibm-eam-{{site.data.keyword.semver}}-bundle/agent && \
    tar -zxvf edge-packages-{{site.data.keyword.semver}}.tar.gz
    ```
    {: codeblock}

    * Debian {{site.data.keyword.linux_notm}} の例:
      ```
      sudo apt-get install ./edge-packages-{{site.data.keyword.semver}}/linux/deb/amd64/horizon-cli*.deb
      ```
      {: codeblock}

    * Red Hat {{site.data.keyword.linux_notm}} の例:
      ```
      sudo dnf install -yq ./edge-packages-{{site.data.keyword.semver}}/linux/rpm/x86_64/horizon-cli-*.x86_64.rpm
      ```
      {: codeblock}

    * macOS の例:
      ```
      sudo security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain edge-packages-{{site.data.keyword.semver}}/macos/pkg/x86_64/horizon-cli.crt && \
      sudo installer -pkg edge-packages-{{site.data.keyword.semver}}/macos/pkg/x86_64/horizon-cli-*.pkg -target /
      ```
      {: codeblock}

2. インストール後のスクリプトを実行します。 このスクリプトは、最初の組織を作成するために必要なすべての初期化を実行します。 (組織は、{{site.data.keyword.ieam}} でリソースおよびユーザーを分離してマルチテナンシーを実現する手段です。 初期段階では、この最初の組織で十分です。 後から追加の組織を構成できます。 詳しくは、[マルチテナンシー](../admin/multi_tenancy.md)を参照してください。

   **注:** **IBM** および **root** は、内部で使用するための組織であり、初期組織として選択することはできません。組織名に、下線 (_)、コンマ (,)、空白スペース ( )、単一引用符 (')、および疑問符 (?) を含めることはできません。

   ```
   ./post_install.sh <choose-your-org-name>
   ```
   {: codeblock}

3. 以下を実行して、ご使用のインストール済み環境の {{site.data.keyword.ieam}} 管理コンソールのリンクを出力します。
   ```
   echo https://$(oc get cm management-ingress-ibmcloud-cluster-info -o jsonpath='{.data.cluster_ca_domain}')/edge
   ```
   {: codeblock}

## 認証 

{{site.data.keyword.ieam}} 管理コンソールにアクセスするときには、ユーザー認証が必要です。 管理者の初期アカウントがこのインストールによって作成されており、以下のコマンドで出力できます。
```
echo "$(oc -n ibm-common-services get secret platform-auth-idp-credentials -o jsonpath='{.data.admin_username}' | base64 --decode) // $(oc -n ibm-common-services get secret platform-auth-idp-credentials -o jsonpath='{.data.admin_password}' | base64 --decode)"
```
{: codeblock}

この管理者アカウントを初期認証に使用でき、以下のコマンドで出力される管理コンソールのリンクにアクセスすることによって、追加で [LDAP の構成](https://www.ibm.com/support/knowledgecenter/SSHKN6/iam/3.x.x/configure_ldap.html)を行うことができます。
```
echo https://$(oc get cm management-ingress-ibmcloud-cluster-info -o jsonpath='{.data.cluster_ca_domain}')
```
{: codeblock}

LDAP 接続が確立されたら、チームを作成し、{{site.data.keyword.edge_notm}} オペレーターがデプロイされている名前空間へのアクセス権限をそのチームに付与し、ユーザーをそのチームに追加します。 これにより、個々のユーザーに API 鍵を作成するための許可が付与されます。

API 鍵は {{site.data.keyword.edge_notm}} CLI での認証に使用され、API 鍵に関連付けられた許可は、それらを生成したユーザーと同一です。

LDAP 接続をまだ作成していない場合でも、管理者の初期資格情報を使用して API 鍵を作成できます。ただし、その API 鍵は **クラスター管理者**特権を持つことに注意してください。

## 次に行うこと

『[エッジ・ノード・ファイルの収集](gather_files.md)』ページのプロセスに従って、エッジ・ノード用のインストール・メディアを準備します。
