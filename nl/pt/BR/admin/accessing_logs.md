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

# Acessando os logs do hub de gerenciamento
{: #accessing_logs}

## Serviço de criação de log do {{site.data.keyword.ocp_tm}}
{: #ocp_logging}

Para configurar um serviço de criação de log do {{site.data.keyword.open_shift_cp}}, consulte a documentação para as versões compatíveis:

* [Criação de log do cluster do {{site.data.keyword.open_shift_cp}} 4.6](https://docs.openshift.com/container-platform/4.6/logging/cluster-logging.html)

** Notas: ** 

* Para instalar este serviço, deve-se ajustar o dimensionamento do cluster. Siga as instruções documentadas para instalar uma pilha replicada do Elasticsearch, Fluentd e Kibana (EFK). 

* O Elasticsearch requer memória e capacidade de armazenamento significativas.

## Criação de log básica

Cada pod do {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) envia logs para o STDOUT. Portanto, eles podem ser lidos com o comando `oc logs`. A capacidade de criação de log básica é limitada e a rotação de log é baseada em tempo e em quantidade de saída de log.

Determine o pod para o qual deseja obter os log:

```
oc get pods --namespace kube-system | grep ibm-edge
```
{: codeblock}

Este exemplo mostra a saída truncada.

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

Siga as últimas 10 linhas do log para o primeiro pod de robô de contrato na lista anterior.

```
oc logs ibm-edge-agbot-5f96655f47-6g97f --tail=10
```
{: codeblock}

Este exemplo mostra um exemplo de saída.

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
