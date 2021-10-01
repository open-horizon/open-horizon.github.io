---

copyright:
years: 2019
lastupdated: "2019-09-27"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Rollenbasierte Zugriffssteuerung (RBAC)
{: #rbac}

{{site.data.keyword.edge_notm}} {{site.data.keyword.ieam}} unterstützt verschiedene Rollen. Ihre Rolle bestimmt die Aktionen, die Sie ausführen können.
{:shortdesc}

## Organisationen
{: #orgs}

Organisationen in {{site.data.keyword.ieam}} werden verwendet, um eine Trennung des Zugriffs auf Ressourcen zu erreichen. Ressourcen für eine Organisation können nur von der jeweiligen Organisation angezeigt werden, es sei denn, die Ressourcen sind explizit als öffentliche Ressourcen markiert. Als öffentlich markierte Ressourcen sind die einzigen Ressourcen, die auch in anderen Organisationen angezeigt werden können. 

Die Organisation IBM wird verwendet, um Ihnen vordefinierte Services und Muster bereitzustellen.

Innerhalb von {{site.data.keyword.ieam}} ist der Name Ihrer Organisation der Name Ihres Clusters. 

## Identitäten
{: #ids}

{{site.data.keyword.ieam}} enthält die folgenden drei Typen von Identitäten: 

* Es gibt zwei Typen von Benutzern. Benutzer können auf die {{site.data.keyword.ieam}}-Konsole und Exchange zugreifen.
  * Identity and Access Management-Benutzer (IAM-Benutzer). IAM-Benutzer werden von {{site.data.keyword.ieam}}-Exchange erkannt.
    * IAM stellt ein LDAP-Plug-in bereit, sodass LDAP-Benutzer, die mit IAM verbunden sind, wie IAM-Benutzer agieren.
    * IAM-API-Schlüssel (verwendet mit dem Befehl **hzn**) agieren wie IAM-Benutzer.
  * Lokale Exchange-Benutzer: Der Exchange-Root-Benutzer ist ein Beispiel für einen lokalen Exchange-Benutzer. Normalerweise müssen Sie keine weiteren lokale Exchange-Benutzer erstellen.
* Knoten (Edge-Einheiten oder Edge-Cluster)
* AgBots

### Rollenbasierte Zugriffssteuerung (RBAC)
{: #rbac_roles}

{{site.data.keyword.ieam}} umfasst die folgenden Rollen:

| **Rolle**    | **Zugriff**    |  
|---------------|--------------------|
| Exchange-Rootbenutzer | Verfügt über uneingeschränkte Zugriffsrechte in Exchange. Dieser Benutzer ist in der Exchange-Konfigurationsdatei definiert. Kann bei Bedarf inaktiviert werden. |
| Benutzer oder API-Schlüssel mit Administratorberechtigung | Verfügt über uneingeschränkte Zugriffsrechte in der Organisation. |
| Benutzer oder API-Schlüssel ohne Administratorberechtigung | Kann Exchange-Ressourcen (Knoten, Services, Muster, Richtlinien) in der Organisation erstellen. Kann Ressourcen, deren Eigner dieser Benutzer ist, aktualisieren oder löschen. Verfügt über einen Lesezugriff auf alle Services, Muster und Richtlinien in der Organisation sowie öffentliche Services und Muster in anderen Organisationen. |
| Knoten | Verfügt über einen Lesezugriff auf den eigenen Knoten in Exchange und auf alle Services, Muster und Richtlinien in der Organisation sowie öffentliche Services und Muster in anderen Organisationen. |
|Agbots| Agbots in der Organisation IBM verfügen über einen Lesezugriff auf alle Knoten, Services, Muster und Richtlinien in allen Organisationen. |
{: caption="Tabelle 1. RBAC-Rollen" caption-side="top"}
