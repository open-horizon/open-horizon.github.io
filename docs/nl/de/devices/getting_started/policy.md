---

copyright:
  years: 2019, 2020
lastupdated: "2020-2-06"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Hello World
{: #policy}

{{site.data.keyword.edge_devices_notm}} verwendet Richtlinien, um Service- und Modellbereitstellungen zu erstellen und zu verwalten. Diese Richtlinien geben Administratoren die Flexibilität und Skalierbarkeit, die für die Arbeit mit sehr vielen Edge-Knoten erforderlich sind. Richtlinien in {{site.data.keyword.edge_devices_notm}} stellen eine Alternative zu Bereitstellungsmustern dar. Sie ermöglicht eine bessere Trennung der Belange (Separation of Concerns) sodass die Eigner von Edge-Knoten, die Entwickler von Service-Code und die Geschäftseigentümer unabhängig voneinander Richtlinien formulieren können. 

Dies ist ein minimales "Hello World"-Beispiel, das als Einführung in die Bereitstellungsrichtlinien von {{site.data.keyword.edge_devices_notm}} dienen soll.

Typen der Horizon-Richtlinien: 

* Knotenrichtlinie (wird bei der Registrierung vom Knoteneigner bereitgestellt)
* Servicerichtlinie (kann auf einen publizierten Service im Exchange angewendet werden)
* Bereitstellungsrichtlinie (wird bisweilen auch als Geschäftsrichtlinie bezeichnet und entspricht in etwa einem Bereitstellungsmuster)

Richtlinien bieten eine bessere Kontrolle über die Definition von Vereinbarungen zwischen Horizon-Agenten auf Edge-Knoten und den Horizon-Agbots.

## Richtlinie zum Ausführen des 'Hello World'-Beispiels verwenden
{: #helloworld_policy}

Weitere Informationen finden Sie unter [Using the Hello World Example Edge Service with Deployment Policy ![Wird in einer neuen Registerkarte geöffnet](../../images/icons/launch-glyph.svg "Wird in einer neuen Registerkarte geöffnet")](https://github.com/open-horizon/examples/blob/master/edge/services/helloworld/PolicyRegister.md#using-the-hello-world-example-edge-service-with-deployment-policy). 

## Zugehörige Informationen

* [Edge-Services bereitstellen](../using_edge_devices/detailed_policy.md)
* [Anwendungsfälle für Bereitstellungsrichtlinien](../using_edge_devices/policy_user_cases.md)
