---

copyright:
years: 2020
lastupdated: "2020-10-30"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}



# アンインストール
{: #uninstalling_hub}

**警告:** **EamHub** カスタム・リソースを削除すると、IBM Cloud Platform Common Services コンポーネントなど、{{site.data.keyword.ieam}} 管理ハブが依存しているリソースが即時に削除されます。 こうすることが目的であれば、続行してください。

前の状態へ容易に修復するためにこのアンインストールを実行している場合は、[バックアップとリカバリー](../admin/backup_recovery.md)のページを参照してください。

* **cloudctl** または **oc login** を使用して、{{site.data.keyword.ieam}} オペレーターがインストールされている名前空間のクラスターにクラスター管理者としてログインします。
* 以下を実行して、カスタム・リソース (デフォルトの **ibm-edge**) を削除します。
  ```
  oc delete eamhub ibm-edge
  ```
  {: codeblock}
* 次のステップに進む前に、すべての {{site.data.keyword.ieam}} 管理ハブ・ポッドが終了していて、ここで示されている 2 つのオペレーター・ポッドのみが実行されていることを確認します。
  ```
  $ oc get pods
  NAME                                           READY   STATUS    RESTARTS   AGE
  ibm-common-service-operator-794f868789-gdt2z   1/1     Running   0          20h
  ibm-eamhub-operator-7455c95496-nf48z           1/1     Running   0          20h
  ```
* OpenShift クラスター・コンソールを使用して、{{site.data.keyword.ieam}} 管理ハブ・オペレーターをアンインストールします。 {{site.data.keyword.ieam}} オペレーターがインストールされている名前空間を選択し、**「Operators」**>**「Installed Operators」**>**「IEAM Management Hub」**のオーバーフロー・メニュー・アイコン>**「Uninstall Operator」**に移動します。
* IBM Cloud Platform Common Services の『[アンインストール](https://www.ibm.com/docs/en/cpfs?topic=online-uninstalling-foundational-services)』ページの『**すべてのサービスのアンインストール**』の手順に従います。**common-service** 名前空間はすべて、{{site.data.keyword.ieam}} オペレーターがインストールされている名前空間に置き換えてください。
