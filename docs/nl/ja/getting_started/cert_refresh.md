---

copyright:
  years: 2021
lastupdated: "2021-02-09"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 証明書の更新
{: #certrefresh}

{{site.data.keyword.ieam}} インストールの一環として、インストールされた {{site.data.keyword.common_services}} のバージョンによっては、自動更新につながる短い有効期間で証明書が作成されている可能性があります。

{{site.data.keyword.ieam}} がインストールされたクラスターにログインし、以下を実行して、{{site.data.keyword.common_services}} の現行バージョンを確認してください。
```
$ oc get csv -A | grep -E 'ibm-common-service-operator|NAME'
NAMESPACE                              NAME                                            DISPLAY                                VERSION   REPLACES                                        PHASE
ibm-common-services                    ibm-common-service-operator.v3.6.4              IBM Cloud Platform Common Services     3.6.4     ibm-common-service-operator.v3.6.3              Succeeded
ibm-edge                               ibm-common-service-operator.v3.6.4              IBM Cloud Platform Common Services     3.6.4     ibm-common-service-operator.v3.6.3              Succeeded
```

同じオペレーターの (少なくとも) 2 つのインスタンスが表示されるはずです。 1 つは `ibm-common-services` 名前空間内にあり、もう 1 つは {{site.data.keyword.ieam}} がインストールされた名前空間内にあります。 2 つのバージョンが一致していて、バージョンが `3.6.4` 以降であることを確認してください。 バージョンが一致していないか、古いバージョンの場合、{{site.data.keyword.open_shift}} コンソールを参照して、サブスクリプション更新を手動に設定したかどうかを確認するか、前のアップグレード試行が原因で生じた可能性のある問題を判別してください。

証明書が自動的に更新された場合、{{site.data.keyword.ieam}} が新しい証明書を適切に使用していることを確認するための手動アクションが必要です。
1. 新しい証明書を取得し、{{site.data.keyword.ieam}} リソースをリフレッシュします。
2. エッジ・ノード所有者に証明書を提供し、エッジ・ノードの指示を伝え、この新しい証明書を各エッジ・ノードに適用する必要があると通知します。

## タスク 1: 新しい証明書の取得と {{site.data.keyword.ieam}} リソースのリフレッシュ
{: #task1}
1. クラスター管理者として、{{site.data.keyword.ieam}} ハブがインストールされているクラスターにログインします。 既存の証明書の作成日と期限日付を確認します。
   ```
   echo "$(oc get secret management-ingress-ibmcloud-cluster-ca-cert -o jsonpath="{.data['ca\.crt']}" -n ibm-common-services | base64 --decode)" | openssl x509 -text -noout | grep -A 2 Validity
   ```
   {: codeblock}

   **注:** 作成日が通信問題が始まった時期と一致しない場合、問題の原因が証明書の更新である可能性は低いため、このプロセスの残りを続行する必要はありません。

2. 以下のようにして、新しい証明書をファイルにエクスポートします。
   ```
   oc get secret cs-ca-certificate-secret -o jsonpath="{.data['ca\.crt']}" -n ibm-common-services | base64 --decode > /tmp/cs-ca.crt
   ```
   {: codeblock}

3. 以下のように、{{site.data.keyword.ieam}} Exchange および SDO ポッドを更新します (これにより、{{site.data.keyword.ieam}} の短い通信障害が発生します)。
   ```
   oc delete pod -l app.kubernetes.io/component=exchange -n ibm-edge
   oc delete pod -l app.kubernetes.io/component=sdo -n ibm-edge
   ```
   {: codeblock}

4. 新しい証明書で CSS インストール **agent_files** を更新します。これにより、今後のエッジ・ノードのインストールで新しい証明書が信頼されるようになります。
   ```
   echo '{"objectID": "agent-install.crt","objectType": "agent_files","destinationOrgID": "IBM","version": "","public": true}' > /tmp/agent-cert-mms.json
   hzn mms -o IBM object publish -m /tmp/agent-cert-mms.json -f /tmp/cs-ca.crt
   ```
   {: codeblock}

   すべてのエッジ・ノード所有者に通知します。 エンド・ユーザーが新しい証明書を使用してノードを構成できるように、この証明書ファイルのコピーと、[タスク 2](cert_refresh.md#task2) 手順への直接リンクを含めます。

## タスク 2: エッジ・ノードへの新規証明書の適用
{: #task2}
### エッジ・デバイスの場合
1. ホストにログインし、新しい証明書ファイルを手動で置換するか、以下のコマンドを実行します (<DEVICE_HOST> はノードのホスト名または IP に、<CA_CERT_FILE> は渡された証明書ファイルの場所に置き換えてください)。
   ```
   ssh root@<DEVICE_HOST> "source /etc/default/horizon; echo -e '$(cat <CA_CERT_FILE>)' > \$HZN_MGMT_HUB_CERT_PATH"
   ```
   {: codeblock}

2. 古い証明書が置換されたことを確認します。
   ```
   ssh root@<DEVICE_HOST> "source /etc/default/horizon; cat \$HZN_MGMT_HUB_CERT_PATH"
   ```
   {: codeblock}

### エッジ・クラスターの場合
1. エージェント・ポッドが実行されている名前空間にログインし、有効期限が切れた既存の証明書を置き換えます (<CA_CERT_FILE> は、新規証明書を含んでいる渡されたファイルの場所に置き換えてください)。
   ```
   oc patch secret openhorizon-agent-secrets --type=merge --patch '{"data": {"agent-install.crt": "'$(cat <CA_CERT_FILE> | base64 | tr -d '\n')'"}}'
   ```
   {: codeblock}

2. 秘密が更新されたことを確認します。
   ```
   oc get secret openhorizon-agent-secrets -o jsonpath="{.data['agent-install\.crt']}" | base64 --decode
   ```
   {: codeblock}

3. 以下のようにして、{{site.data.keyword.ieam}} エージェント・ポッドを再始動します。
   ```
   oc delete pod $(oc get pods | grep 'agent-' | awk '{print $1}')
   ```
   {: codeblock}
