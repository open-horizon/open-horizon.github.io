---

copyright:
years: 2020
lastupdated: "2020-04-7"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 管理ハブのログへのアクセス
{: #accessing_logs}

## {{site.data.keyword.ocp_tm}} ロギング・サービス
{: #ocp_logging}

{{site.data.keyword.open_shift_cp}} クラスター・ロギング・サービスをセットアップするには、サポートされるバージョンの以下の資料を参照してください。

* [{{site.data.keyword.open_shift_cp}} 4.6 クラスター・ロギング](https://docs.openshift.com/container-platform/4.6/logging/cluster-logging.html)

**注:** 

* このサービスをインストールするには、クラスターのサイジングを調整する必要があります。 記載されている手順に従って、複製された EFK (Elasticsearch、Fluentd、および Kibana) スタックをインストールしてください。 

* Elasticsearch では、大量のメモリーおよびストレージ容量が必要です。

## 基本的なロギング

各 {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) ポッドはログを STDOUT に送信するため、ログは `oc logs` コマンドを使用して読み取ることができます。 基本的なロギングの容量には限度があり、ログのローテーションは時間およびログ出力量に基づきます。

以下のようにして、ログを取得する対象のポッドを判別します。

```
oc get pods --namespace kube-system | grep ibm-edge
```
{: codeblock}

このサンプル出力は、省略したものを示しています。

```
$ oc get pods --namespace kube-system | grep ibm-edge
ibm-edge-agbot-5f96655f47-6g97f                           1/1     Running     0          5h16m
ibm-edge-agbot-5f96655f47-jzdfv                           1/1     Running     0          5h16m
ibm-edge-agbotdb-create-cluster-4mk7m                     0/1     Completed   0          7d
ibm-edge-agbotdb-creds-gen-rfhd2                          0/1     Completed   0          7d
ibm-edge-agbotdb-keeper-0                                 1/1     Running     0          7d
...
```
{: codeblock}

次のようにして、前のリスト中の最初の agbot ポッドのログの末尾 10 行を表示します。

```
oc logs ibm-edge-agbot-5f96655f47-6g97f --tail=10
```
{: codeblock}

このサンプルでは、出力例を示します。

```
$ oc logs ibm-edge-agbot-5f96655f47-6g97f --tail=10
I0612 02:25:38.878379       8 agreementbot.go:660] AgreementBotWorker done queueing deferred commands
I0612 02:25:38.878475       8 handle_retry_agreements.go:15] AgreementBotWorker Handling retries: retry agreements: 
I0612 02:25:38.878613       8 handle_retry_agreements.go:25] AgreementBotWorker agreement retry is empty
I0612 02:25:38.878705       8 agreementbot.go:761] AgreementBotWorker work queues: Basic High: 0, Low: 0 
I0612 02:25:38.878791       8 agreementbot.go:602] AgreementBotWorker retrieving messages from the exchange
I0612 02:25:38.878932       8 rpc.go:860] Exchange RPC Invoking exchange GET at http://ibm-edge-exchange/v1/orgs/IBM/agbots/ieam-test-agbot/msgs with <nil>
I0612 02:25:38.892274       8 rpc.go:911] Exchange RPC Got 404. Response to GET at http://ibm-edge-exchange/v1/orgs/IBM/agbots/ieam-test-agbot/msgs is {"messages":[],"lastIndex":0}
I0612 02:25:38.892302       8 agreementbot.go:987] AgreementBotWorker retrieved 0 messages
I0612 02:25:38.892312       8 agreementbot.go:651] AgreementBotWorker done processing messages
I0612 02:25:38.892333       8 worker.go:348] CommandDispatcher: AgBot command processor non-blocking for commands
```
{: codeblock}
