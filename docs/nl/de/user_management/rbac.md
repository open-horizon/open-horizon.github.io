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

{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) unterstützt verschiedene Rollen. Ihre Rolle bestimmt die Aktionen, die Sie ausführen können.
{:shortdesc}

## Organisationen
{: #orgs}

{{site.data.keyword.ieam}} unterstützt das allgemeine Konzept der Multi-Tenant-Funktionalität in Form von Organisationen, wobei jeder Tenant eine eigene Organisation besitzt. Organisationen dienen der Aufteilung von Ressourcen. Benutzer in einer Organisation können daher keine Ressourcen in einer anderen Organisation erstellen oder ändern. Darüber hinaus können Ressourcen in einer Organisation nur von Benutzern in dieser Organisation angezeigt werden, es sei denn, die Ressourcen sind als öffentlich (public) markiert. Als öffentlich markierte Ressourcen sind die einzigen Ressourcen, die auch in anderen Organisationen angezeigt werden können.

Die IBM Organisation stellt vordefinierte Services und Muster bereit. Die Ressourcen in dieser Organisation sind zwar öffentlich, aber sie ist nicht dafür vorgesehen, sämtlichen öffentlichen Inhalt im {{site.data.keyword.ieam}}-Management-Hub aufzunehmen.

Eine Organisation wird standardmäßig während der {{site.data.keyword.ieam}}-Installation mit einem von Ihnen gewählten Namen erstellt. Sie können nach Bedarf zusätzliche Organisationen erstellen. Weitere Informationen zum Hinzufügen von Organisationen zu Ihrem Management-Hub finden Sie unter [Multi-Tenant-Funktionalität](../admin/multi_tenancy.md).

## Identitäten
{: #ids}

{{site.data.keyword.ieam}} enthält die folgenden vier Typen von Identitäten:

* Identity and Access Management-Benutzer (IAM-Benutzer). IAM-Benutzer werden von allen {{site.data.keyword.ieam}}-Komponenten erkannt: Benutzerschnittstelle, Exchange, CLI **hzn**, CLI **cloudctl**, CLI **oc** und CLI **kubectl**.
  * IAM stellt ein LDAP-Plug-in bereit, sodass LDAP-Benutzer, die mit IAM verbunden sind, wie IAM-Benutzer agieren.
  * IAM-API-Schlüssel (verwendet mit dem Befehl **hzn**) agieren wie IAM-Benutzer.
* Reine Exchange-Benutzer: Der Exchange-Rootbenutzer ist ein Beispiel für einen lokalen Exchange-Benutzer. Normalerweise müssen Sie keine weiteren lokale und reinen Exchange-Benutzer erstellen. Es hat sich das Verfahren bewährt, Benutzer in IAM zu verwalten und diese Benutzerberechtigungsnachweise (oder die den Benutzern zugeordneten API-Schlüssel) zur Authentifizierung bei {{site.data.keyword.ieam}} zu verwenden.
* Exchange-Knoten (Edge-Einheiten oder Edge-Cluster)
* Exchange-Agbots

### Rollenbasierte Zugriffssteuerung (RBAC)
{: #rbac_roles}

{{site.data.keyword.ieam}} umfasst die folgenden Rollen:

| **Rolle**    | **Zugriff**    |  
|---------------|--------------------|
| IAM-Benutzer | Kann über IAM die folgenden Rollen für den Management-Hub erhalten: Clusteradministrator, Administrator, Bediener, Bearbeiter und Anzeigeberechtigter. Eine IAM-Rolle wird Benutzern oder Benutzergruppen zugeordnet, wenn Sie sie zu einem IAM-Team hinzufügen. Der Teamzugriff auf Ressourcen kann durch den Kubernetes-Namensbereich gesteuert werden. IAM-Benutzer kann mit der CLI **hzn exchange** auch eine der nachfolgend aufgeführten Exchange-Rollen erteilt werden. |
| Exchange-Rootbenutzer | Verfügt über uneingeschränkte Zugriffsrechte in Exchange. Dieser Benutzer ist in der Exchange-Konfigurationsdatei definiert. Kann bei Bedarf inaktiviert werden. |
| Exchange-Hubadministrator | Kann die Liste der Organisationen sowie die Benutzer in einer Organisation anzeigen und Organisationen erstellen oder löschen. |
| Exchange-Organisationsadministrator | Hat innerhalb der Organisation uneingeschränkte Exchange-Berechtigungen. |
| Exchange-Benutzer | Kann Exchange-Ressourcen (Knoten, Services, Muster, Richtlinien) in der Organisation erstellen. Kann Ressourcen, deren Eigner dieser Benutzer ist, aktualisieren oder löschen. Verfügt über einen Lesezugriff auf alle Services, Muster und Richtlinien in der Organisation sowie öffentliche Services und Muster in anderen Organisationen. Kann Knoten lesen, deren Eigner dieser Benutzer ist. |
| Exchange-Knoten | Verfügt über einen Lesezugriff auf den eigenen Knoten in Exchange und auf alle Services, Muster und Richtlinien in der Organisation sowie öffentliche Services und Muster in anderen Organisationen. Dies sind die einzigen Berechtigungsnachweise, die im Edge-Knoten gespeichert werden sollten, da sie die minimalen Berechtigungen für den Betrieb des Edge-Knotens enthalten.|
| Exchange-Agbots | Agbots in der Organisation IBM verfügen über einen Lesezugriff auf alle Knoten, Services, Muster und Richtlinien in allen Organisationen. |
{: caption="Tabelle 1. RBAC-Rollen" caption-side="top"}
