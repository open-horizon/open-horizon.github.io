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

Generell gleicht die Entwicklung eines Service, der in einem Edge-Cluster ausgeführt werden soll, der Entwicklung eines Edge-Service, der auf einer Edge-Einheit ausgeführt wird. Bei der Bereitstellung des Edge-Services besteht jedoch ein Unterschied. Wenn Sie einen containerisierten Edge-Service in einem Edge-Cluster bereitstellen möchten, muss von einem Entwickler zunächst ein Kubernetes-Operator erstellt werden, der den containerisierten Edge-Service in einem Kubernetes-Cluster bereitstellt. Nachdem der Operator geschrieben und getestet wurde, erstellt und publiziert der Entwickler den Operator als IBM Edge Application Manager-Service (IEAM-Service). Diese Vorgehensweise ermöglicht es einem IEAM-Administrator, den Operator-Service wie einen beliebigen IEAM-Service mit einer Richtlinie oder mit Mustern bereitzustellen.

Wenn Sie den Service `ibm.operator` verwenden möchten, der bereits mit der Bereitstellungsrichtlinie für die Ausführung des containerisierten Service `helloworld` in Ihrem Cluster in IEAM-Exchange publiziert wurde, lesen Sie die Informationen im Abschnitt [Beispiel für Horizon-Operator als Edge-Service ![Wird in einer neuen Registerkarte geöffnet](../../images/icons/launch-glyph.svg "Wird in einer neuen Registerkarte geöffnet")](https://github.com/open-horizon/examples/tree/master/edge/services/operator#horizon-operator-example-edge-service).
