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

# 관리 허브 로그에 액세스
{: #accessing_logs}

## {{site.data.keyword.ocp_tm}} 로깅 서비스
{: #ocp_logging}

{{site.data.keyword.open_shift_cp}} 클러스터 로깅 서비스를 설정하려면 문서에서 지원되는 버전을 참조하십시오.

* [{{site.data.keyword.open_shift_cp}} 4.6 클러스터 로깅](https://docs.openshift.com/container-platform/4.6/logging/cluster-logging.html)

**참고:** 

* 이 서비스를 설치하려면 클러스터 크기를 조정해야 합니다. 문서화된 지침에 따라 복제된 Elasticsearch, Fluentd 및 Kibana(EFK) 스택을 설치하십시오. 

* Elasticsearch에는 상당한 메모리 및 스토리지 용량이 필요합니다.

## 기본 로깅

각 {{site.data.keyword.edge_notm}}({{site.data.keyword.ieam}}) 팟(pod)에서 로그를 STDOUT에 전송하므로 `oc logs` 명령을 사용하여 읽을 수 있습니다. 기본 로깅 용량은 제한되며, 로그 순환은 시간 및 로그 순환 수량을 기반으로 합니다.

로그를 얻을 팟(pod)을 판별하십시오.

```
oc get pods --namespace kube-system | grep ibm-edge
```
{: codeblock}

다음 샘플은 잘린 출력을 표시합니다.

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

이전 목록에 있는 첫 번째 agbot 팟의 로그 중 마지막 10행을 첨부하십시오.

```
oc logs ibm-edge-agbot-5f96655f47-6g97f --tail=10
```
{: codeblock}

다음 샘플은 출력 예제를 표시합니다.

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
