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

# Auf Management-Hub-Protokolle zugreifen
{: #accessing_logs}

## {{site.data.keyword.ocp_tm}}-Protokollierungsservice
{: #ocp_logging}

Informationen zum Einrichten eines Clusterprotokollierungsservice für {{site.data.keyword.open_shift_cp}} finden Sie in der Dokumentation zu den folgenden unterstützten Versionen:

* [{{site.data.keyword.open_shift_cp}} 4.6 Clusterprotokollierung](https://docs.openshift.com/container-platform/4.6/logging/cluster-logging.html)

**Hinweise:** 

* Die Installation dieses Service erfordert eine Anpassung der Clusterdimensionierung. Mit den dokumentierten Anweisungen können Sie einen replizierten EFK-Stack (EFK = Elasticsearch, Fluentd und Kibana) installieren. 

* Elasticsearch benötigt eine erhebliche Hauptspeicher- und Speicherkapazität.

## Basisprotokollierung

Von jedem {{site.data.keyword.ieam}}-Pod (IEAM - {{site.data.keyword.edge_notm}}) werden Protokolle an die Standardausgabe gesendet. Mit dem Befehl `oc logs` ist somit ein Lesezugriff auf diese Protokolle möglich. Die Kapazität für die Basisprotokollierung ist begrenzt und die Protokollrotation basiert auf Frequenz und Umfang der Protokollausgabe.

Ermitteln Sie den Pod, für den die Protokolle abgerufen werden sollen:

```
oc get pods --namespace kube-system | grep ibm-edge
```
{: codeblock}

Die Ausgabe im Beispiel ist verkürzt.

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

Zeigen Sie die letzten 10 Zeilen des Protokolls für den ersten Agbot-Pod in der obigen Liste an.

```
oc logs ibm-edge-agbot-5f96655f47-6g97f --tail=10
```
{: codeblock}

Nachfolgend ist eine Beispielausgabe dargestellt.

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
