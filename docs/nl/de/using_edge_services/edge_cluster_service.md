---

copyright:
  years: 2020
lastupdated: "2020-05-9"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Edge-Cluster-Service
{: #Edge_cluster_service}

Generell gleicht die Entwicklung eines Service, der in einem Edge-Cluster ausgeführt werden soll, der Entwicklung eines Edge-Service, der auf einer Edge-Einheit ausgeführt wird. Bei der Bereitstellung des Edge-Services besteht jedoch ein Unterschied. Wenn Sie einen containerisierten Edge-Service in einem Edge-Cluster bereitstellen möchten, muss von einem Entwickler zunächst ein Kubernetes-Operator erstellt werden, der den containerisierten Edge-Service in einem Kubernetes-Cluster bereitstellt. Nachdem der Operator geschrieben und getestet worden ist, erstellt und publiziert der Entwickler den Operator als Service von {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}). Der Operatorservice kann wie jeder andere {{site.data.keyword.edge_notm}}-Service auf Edge-Clustern mit einer Richtlinie oder einem Muster bereitgestellt werden.

Der {{site.data.keyword.ieam}}-Exchange enthält einen Service mit dem Namen `hello-operator`, mit dem Sie einen Port auf dem Edge-Cluster zugänglich machen können, sodass auf ihn extern mit dem `curl`-Befehl zugegriffen werden kann. Informationen zum Implementieren dieses Beispielservice in Ihrem Edge-Cluster finden Sie unter [Horizon Operator Beispiel-Edge-Service](https://github.com/open-horizon/examples/tree/v2.27/edge/services/hello-operator#-using-the-operator-example-edge-service-with-deployment-policy).
