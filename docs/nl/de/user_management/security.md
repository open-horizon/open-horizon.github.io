---

copyright:
years: 2019
lastupdated: "2019-09-04"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Sicherheit 
{: #security}

{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}), basierend auf [Open Horizon](https://github.com/open-horizon), verwendet mehrere Sicherheitstechnologien, um sicherzustellen, dass es sicher vor Angriffen ist und die Privatsphäre geschützt wird. Weitere Informationen zur Sicherheit und zu den Rollen von {{site.data.keyword.ieam}} enthalten die folgenden Abschnitte:

* [Sicherheit und Datenschutz](../OH/docs/user_management/security_privacy.md)
* [Rollenbasierte Zugriffssteuerung (RBAC)](rbac.md)
* [Hinweise zur DSGVO-Umsetzung bei {{site.data.keyword.edge_notm}}](gdpr.md)
{: childlinks}

Im Abschnitt [Erstellung eines Edge-Service erstellen](../developing/service_containers.md) erfahren Sie genauer, wie Sie Signierschlüssel für Workloads erstellen können, falls Sie noch keine eigenen RSA-Schlüssel besitzen. Mit solchen Schlüsseln können Sie Services signieren, wenn Sie sie im Exchange publizieren, und dem {{site.data.keyword.ieam}}-Agenten so die Bestätigung ermöglichen, dass er eine gültige Workload gestartet hat.
