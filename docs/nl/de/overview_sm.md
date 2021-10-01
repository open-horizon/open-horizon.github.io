---

copyright:
years: 2021
lastupdated: "2021-07-20"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Übersicht über Secrets Manager
{: #overviewofsm}

Für Services, die an der Edge implementiert werden, ist häufig der Zugriff auf Cloud-Services erforderlich. Dies bedeutet, dass der Service Berechtigungsnachweise für die Authentifizierung beim Cloud-Service benötigt. Der Secrets Manager stellt einen sicheren Mechanismus bereit, mit dem Berechtigungsnachweise gespeichert, implementiert und verwaltet werden können, ohne die Details innerhalb von {{site.data.keyword.ieam}} Metadaten (z. B. Servicedefinitionen und -richtlinien) oder anderen Benutzern im System auszusetzen, die keinen Zugriff auf das geheime System haben sollten. Der Secrets Manager ist eine Plug-in-Komponente von {{site.data.keyword.ieam}}. Derzeit ist HashiCorp Vault der einzige unterstützte Secrets Manager.

Ein geheimer Schlüssel ist eine Benutzer-ID/ein Kennwort, ein Zertifikat, ein RSA-Schlüssel oder ein anderer Berechtigungsnachweis, der Zugriff auf eine geschützte Ressource gewährt, die eine Edge-Anwendung benötigt, um die Funktion auszuführen. Geheime Schlüssel werden im Secrets Manager gespeichert. Ein geheimer Schlüssel hat einen Namen, der benutzt wird, um das Geheimnis zu identifizieren, das aber keine Informationen über die Details des Geheimnisses selbst liefert. Geheime Schlüssel werden von der {{site.data.keyword.ieam}} CLI oder von einem Administrator unter Verwendung der Benutzerschnittstelle oder CLI des Secrets Manager verwaltet.

Ein Serviceentwickler deklariert das Bedürfnis nach einem geheimen Schlüssel in einer {{site.data.keyword.ieam}} Servicedefinition. Der Service-Implementierer ordnet (oder bindet) ein Geheimnis aus dem Secrets Manager an die Implementierung des Service an, indem er den Service einem geheimen Schlüssel des Secrets Manager zuordnet. Beispiel: Angenommen, ein Entwickler muss über die Basisauthentifizierung auf den Cloud-Service XYZ zugreifen. Der Entwickler aktualisiert die {{site.data.keyword.ieam}} Servicedefinition so, dass sie ein Geheimnis mit dem Namen 'myCloudServiceCred' enthält. Der Service-Implementierer sieht, dass der Service ein Geheimnis erfordert, um es zu implementieren, und ist sich eines Geheimnisses im Secrets Manager namens cloudServiceXYZSecret bewusst, das grundlegende Authentifizierungsnachweise enthält. Der Service-Implementierer aktualisiert die Implementierungsrichtlinie (oder das Muster), um anzugeben, dass der geheime Name des Service mit dem Namen 'myCloudServiceCreds' die Berechtigungsnachweise aus dem geheimen Schlüssel 'Secrets Manager' mit dem Namen cloudServiceXYZSecret enthalten soll. Wenn der Service-Implementierer die Implementierungsrichtlinie (oder das Muster) veröffentlicht, wird {{site.data.keyword.ieam}} die Details von cloudServiceXYZSecret sicher auf allen Edge-Knoten implementieren, die mit der Implementierungsrichtlinie (oder dem Muster) kompatibel sind.
