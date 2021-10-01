---

copyright:
  years: 2020
lastupdated: "2020-04-9"

---

{:shortdesc: .shortdesc}
{:new_window: target="_blank"}
{:codeblock: .codeblock}
{:pre: .pre}
{:screen: .screen}
{:tip: .tip}
{:download: .download}

# Eigenen Hello World-Service für Cluster erstellen
{: #creating_hello_world}

Wenn Sie einen containerisierten Edge-Service in einem Edge-Cluster bereitstellen möchten, müssen Sie zunächst einen Kubernetes-Operator erstellen, der den containerisierten Edge-Service in einem Kubernetes-Cluster bereitstellt.

Verwenden Sie dieses Beispiel, um sich mit der Vorgehensweise bei der Ausführung folgender Aktionen vertraut zu machen:

* Einen Ansible-Operator mithilfe von `operator-sdk` erstellen
* Den Operator verwenden, um einen Service auf einem Edge-Cluster bereitzustellen
* Einen Port auf dem Edge-Cluster zugänglich machen, auf den extern mit dem `curl`-Befehl zugegriffen werden kann

Siehe [Eigenen Operator Edge-Service erstellen)](https://github.com/open-horizon/examples/blob/v2.27/edge/services/hello-operator/CreateService.md#creating-your-own-operator-edge-service).

Informationen zum Ausführen des veröffentlichten Service `hello-operator` finden Sie unter [Beispiel-Operator Edge-Service mit Implementierungsrichtlinie verwenden](https://github.com/open-horizon/examples/tree/v2.27/edge/services/hello-operator#-using-the-operator-example-edge-service-with-deployment-policy).
