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

* Schreiben eines Operators.
* Verwenden eines Operators, um einen Edge-Service in einem Cluster bereitzustellen (im vorliegenden Fall `ibm.helloworld`).
* Übergeben der Horizon-Umgebungsvariablen (und weiterer erforderlicher Variablen) an die bereitgestellten Service-Pods.

Weitere Informationen finden Sie unter [Eigenen Hello World-Cluster-Service erstellen ![Wird in einer neuen Registerkarte geöffnet](../../images/icons/launch-glyph.svg "Wird in einer neuen Registerkarte geöffnet")](https://github.com/open-horizon/examples/tree/master/edge/services/operator/CreateService.md).

Informationen zur Ausführung des publizierten Service `ibm.operator` finden Sie in dem Abschnitt zum [Beispiel für Operator-Edge-Service mit Bereitstellungsrichtlinie![Wird in einer neuen Registerkarte geöffnet](../../images/icons/launch-glyph.svg "Wird in einer neuen Registerkarte geöffnet")](https://github.com/open-horizon/examples/tree/master/edge/services/operator#horizon-operator-example-edge-service).
