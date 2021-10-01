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

# 访问管理中心日志
{: #accessing_logs}

## {{site.data.keyword.ocp_tm}} 日志记录服务
{: #ocp_logging}

要设置 {{site.data.keyword.open_shift_cp}} 集群日志记录服务，请查看受支持的版本的文档：

* [{{site.data.keyword.open_shift_cp}} 4.6 集群日志记录 ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://docs.openshift.com/container-platform/4.6/logging/cluster-logging.html)

**注：** 

* 要安装此服务，必须调整集群大小。 遵循记录的指示信息以安装复制的 Elasticsearch、Fluentd 和 Kibana (EFK) 堆栈。 

* Elasticsearch 需要大量内存和存储容量。

## 基本日志记录

每个 {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) pod 将日志发送到 STDOUT，因此可以使用 `oc logs` 命令来读取日志。 基本日志记录的容量有限，且日志循环基于时间和日志输出数量。

确定想要获取其日志的 pod：

```
oc get pods --namespace kube-system | grep ibm-edge
```
{: codeblock}

此样本显示截断的输出。

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

跟踪先前列表中第一个 agbot pod 的日志的最后 10 行：

```
oc logs ibm-edge-agbot-5f96655f47-6g97f --tail=10
```
{: codeblock}

此样本显示输出示例。

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
