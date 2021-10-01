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

# データのバックアップとリカバリー
{: #data_backup}

## {{site.data.keyword.open_shift_cp}} のバックアップとリカバリー

クラスター全体のデータのバックアップとリカバリーについて詳しくは、以下を参照してください。

* [{{site.data.keyword.open_shift_cp}} 4.6 etcd のバックアップ](https://docs.openshift.com/container-platform/4.6/backup_and_restore/backing-up-etcd.html)

## {{site.data.keyword.edge_notm}} のバックアップとリカバリー

{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) のバックアップ手順は、使用しているデータベースのタイプによって多少異なります。 これらのデータベースは、ローカルまたはリモートと呼ばれます。

|データベース・タイプ|説明|
|-------------|-----------|
|ローカル|これらのデータベースは、デフォルトでは、{{site.data.keyword.open_shift}} リソースとして {{site.data.keyword.open_shift}} クラスターにインストールされます。|
|リモート|これらのデータベースは、クラスターの外部にプロビジョンされます。 例えば、これらのデータベースは、オンプレミスでも、クラウド・プロバイダーの SaaS オファリングでも構いません。|

どのデータベースを使用するかを制御する構成設定は、インストール時にカスタム・リソースに **spec.ieam\_local\_databases** として設定され、デフォルトでは true です。

インストール済み {{site.data.keyword.ieam}} インスタンスのアクティブ値を判別するには、以下を実行します。

```
oc get eamhub ibm-edge -o jsonpath="{.spec.ieam_local_databases}"
```
{: codeblock}

インストール時のリモート・データベースの構成について詳しくは、[「構成」](../hub/configuration.md)ページを参照してください。

**注**: ローカル・データベースとリモート・データベースの切り替えはサポートされていません。

{{site.data.keyword.edge_notm}} 製品は、データを自動的にバックアップしません。 リカバリー可能性を確保するために、ユーザーには、選択した頻度でコンテンツをバックアップし、それらのバックアップを別個のセキュアな場所に保管する責任があります。 秘密のバックアップにはデータベース接続および{{site.data.keyword.mgmt_hub}} ・アプリケーション認証のためのエンコードされた認証コンテンツが含まれているため、セキュアな場所に保管します。

独自のリモート・データベースを使用している場合は、それらのデータベースがバックアップされるようにしてください。 本書では、それらのリモート・データベースのデータのバックアップ方法は説明しません。

{{site.data.keyword.ieam}} のバックアップ手順では `yq` v3 も必要です。

### バックアップ手順

1. **cloudctl login** または **oc login** のいずれかを使用してクラスターに管理者として接続していることを確認します。 以下のスクリプト (パスポート・アドバンテージからの{{site.data.keyword.mgmt_hub}} のインストールのために使用した解凍済みメディアに入っています) を使用して、データおよび秘密をバックアップします。 使用法を表示するには、以下のように **-h** を指定してスクリプトを実行します。

   ```
   ibm-eam-{{site.data.keyword.semver}}-bundle/tools/ieam-backup.sh -h
   ```
   {: codeblock}
   
   **注**: バックアップ・スクリプトにより、インストール時に使用されたデータベースのタイプが自動的に検出されます。

   * 次の例をオプションを指定せずに実行すると、スクリプトが実行されたフォルダーが生成されます。 このフォルダーは、命名パターン **ibm-edge-backup/$DATE/** に従います。

     ```
     ibm-eam-{{site.data.keyword.semver}}-bundle/tools/ieam-backup.sh
     ```
     {: codeblock}
     
     **ローカル・データベース**のインストールが検出された場合、バックアップには、**customresource** ディレクトリー、**databaseresources** ディレクトリー、および 2 つの yaml ファイルが含まれます。

     ```
     $ ls -l ibm-edge-backup/20201026_215107/
  	  drwxr-xr-x  3 staff  staff     96 Oct 26 21:51 customresource
	  drwxr-xr-x  5 staff  staff    160 Oct 26 21:51 databaseresources
	  -rw-r--r--  1 staff  staff  13308 Oct 26 21:51 ibm-edge-auth-secret.yaml
	  -rw-r--r--  1 staff  staff   3689 Oct 26 21:51 ibm-edge-config.yaml
     ```
     {: codeblock}
     
	  **リモート・データベース**のインストールが検出された場合、上記のディレクトリーと同じディレクトリーが表示されますが、yaml ファイルは 2 つではなく 3 つです。
	  
	  ```
     $ ls -l ibm-edge-backup/20201026_215518/
	  drwxr-xr-x  3 staff  staff     96 Oct 26 21:55 customresource
	  drwxr-xr-x  3 staff  staff     96 Oct 26 21:55 databaseresources
	  -rw-r--r--  1 staff  staff  10477 Oct 26 21:55 ibm-edge-auth-overrides.yaml
	  -rw-r--r--  1 staff  staff  11433 Oct 26 21:55 ibm-edge-auth-secret.yaml
	  -rw-r--r--  1 staff  staff   2499 Oct 26 21:55 ibm-edge-config.yaml
     ```
     {: codeblock}

### リストア手順

**注**: ローカル・データベースが使用されている場合、または新規または空のリモート・データベースにリストアされる場合、{{site.data.keyword.ieam}} の自律設計では、{{site.data.keyword.mgmt_hub}} にバックアップをリストアするときに既知の課題が発生します。

バックアップをリストアするには、同じ{{site.data.keyword.mgmt_hub}} をインストールする必要があります。 この新しいハブが、初期インストール時に **ieam\_maintenance\_mode** にならずにインストールされている場合は、以前に登録されたすべてのエッジ・ノードが登録抹消してしまう可能性があります。 そのため、再登録する必要があります。

この状態は、データベースが空になったため、エッジ・ノードがもう Exchange に存在しなくなったことを認識したときに発生します。 **ieam\_maintenance\_mode** を有効にして{{site.data.keyword.mgmt_hub}} のためだけにデータベース・リソースを起動することで、これを回避します。 これにより、残りの{{site.data.keyword.mgmt_hub}} ・リソース (これらのデータベースを使用) が開始される前にリストアを完了できます。

**注**: 

* **カスタム・リソース**・ファイルがバックアップされたときに、クラスターに再適用するとすぐに **ieam\_maintenance\_mode** になるように自動的に変更されました。

* リストア・スクリプトは、**\<path/to/backup\>/customresource/eamhub-cr.yaml** ファイルを調べることによって、以前に使用されたデータベースのタイプを自動的に判別します。

1. クラスター管理者は、**cloudctl login** または **oc login** を使用してクラスターに接続されていること、および有効なバックアップが作成されていることを確認してください。 バックアップが作成されたクラスターで、以下のコマンドを実行して **eamhub** カスタム・リソースを削除します (これは、カスタム・リソースに、**ibm-edge** のデフォルト名が使用されていたと想定しています)。
	```
	oc delete eamhub ibm-edge
	```
	{: codeblock}

2. **ieam\_maintenance\_mode** が正しく設定されていることを確認します。
	```
	yq r ibm-edge-backup/20201026_215738/customresource/eamhub-cr.yaml 'items[0].spec.ieam_maintenance_mode'
	```
	{: codeblock}
	

3. オプション **-f** がバックアップの場所を指すように定義された `ieam-restore-k8s-resources.sh` スクリプトを実行します。
	```
	ibm-eam-{{site.data.keyword.semver}}-bundle/tools/ieam-restore-k8s-resources.sh -f ibm-edge-backup/20201026_215738/
	```
	{: codeblock}

   すべてのデータベースおよび SDO ポッドが実行中になるまで待ってから先に進んでください。
	
4. **ibm-edge** カスタム・リソースを編集して、オペレーターを一時停止します。
	```
	oc patch eamhub ibm-edge --type merge --patch '{"spec":{"pause_control_loop": true}}'
	```
	{: codeblock}

5. **ibm-edge-sdo** ステートフル・セットを編集して、レプリカの数を **1** にスケールアップします。
	```
	oc patch statefulset ibm-edge-sdo --type merge --patch '{"spec":{"replicas": 1}}'
	```
	{: codeblock}

6. **ibm-edge-sdo-0** ポッドが実行状態になるまで待ちます。
	```
   	watch oc get pods -n ibm-edge | grep ibm-edge-sdo-0
   	```
	{: codeblock}

7. オプション **-f** がバックアップの場所を指すように定義された「ieam-restore-data.sh」スクリプトを実行します。
	```
	ibm-eam-{{site.data.keyword.semver}}-bundle/tools/ieam-restore-data.sh -f ibm-edge-backup/20201026_215738/
	```
	{: codeblock}
	
8. スクリプトが完了し、データがリストアされたら、オペレーターの一時停止を取り除き、制御ループを再開します。
	```
	oc patch eamhub ibm-edge --type merge --patch '{"spec":{"pause_control_loop": false}}'
	```
	{: codeblock}

