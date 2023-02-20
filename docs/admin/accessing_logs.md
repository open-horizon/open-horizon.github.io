---

copyright:
years: 2020 - 2023
lastupdated: "2023-02-18"
title: Accessing logs
description: Accessing management hub logs

parent: Administering functions
grand_parent: Administering
nav_order: 5
---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Accessing management hub logs
{: #accessing_logs}

## {{site.data.keyword.ocp_tm}} logging service
{: #ocp_logging}

To set up {{site.data.keyword.open_shift_cp}} a cluster logging service, see the documentation for the supported versions:

* [{{site.data.keyword.open_shift_cp}} 4.6 Cluster Logging ](https://docs.openshift.com/container-platform/4.6/logging/cluster-logging.html){:target="_blank"}{: .externalLink}

**Notes:**

* To install this service, you must adjust your cluster sizing. Follow the documented instructions to install a replicated Elasticsearch, Fluentd, and Kibana (EFK) stack.

* Elasticsearch requires significant memory and storage capacity.

## Basic logging

Each {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) pod sends logs to STDOUT, so they can be read with the `oc logs` command. Basic logging capacity is limited, and log-rotation is based on time and log output quantity.

Determine the pod that you want to obtain the logs for:

```bash
oc get pods --namespace kube-system | grep ibm-edge
```
{: codeblock}

This sample shows truncated output.

```text
$ oc get pods --namespace kube-system | grep ibm-edge
ibm-edge-agbot-5f96655f47-6g97f                           1/1     Running     0          5h16m
ibm-edge-agbot-5f96655f47-jzdfv                           1/1     Running     0          5h16m
ibm-edge-agbotdb-create-cluster-4mk7m                     0/1     Completed   0          7d
ibm-edge-agbotdb-creds-gen-rfhd2                          0/1     Completed   0          7d
ibm-edge-agbotdb-keeper-0                                 1/1     Running     0          7d
...
```
{: codeblock}

Tail the last 10 lines of the log for the first agbot pod in the previous list.

```bash
oc logs ibm-edge-agbot-5f96655f47-6g97f --tail=10
```
{: codeblock}

This sample shows an example of output.

```text
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
