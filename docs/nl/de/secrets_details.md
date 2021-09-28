---

copyright:
years: 2021
lastupdated: "2021-08-16"

---

{:shortdesc: .shortdesc}
{:new_window: target="_blank"}
{:codeblock: .codeblock}
{:pre: .pre}
{:screen: .screen}
{:tip: .tip}
{:download: .download}

# Service unter Verwendung von geheimen Schlüsseln entwickeln
{: #using secrets}

<img src="../images/edge/10_Secrets.svg" style="margin: 3%" alt="Developing a service using secrets"> 

# Details des Secrets Managers
{: #secrets_details}

Der Secrets Manager sorgt für sicheren Speicher für sensible Informationen wie Authentifizierungsnachweise oder Verschlüsselungsschlüssel. Diese Geheimnisse werden sicher von {{site.data.keyword.ieam}} bereitgestellt, sodass nur die Services, die für den Empfang eines geheimen Schlüssels konfiguriert sind, Zugriff darauf haben. Das Beispiel [Hello Secret World](https://github.com/open-horizon/examples/blob/master/edge/services/helloSecretWorld/CreateService.md) gibt einen Überblick über die Verwendung von Geheimnissen in einem Edge-Service.

{{site.data.keyword.ieam}} unterstützt die Verwendung von [Hashicorp Vault](https://www.vaultproject.io/) als 'Secrets Manager'. Geheimnisse, die mit der hzn-CLI erstellt werden, werden mithilfe der [KV V2 Secrets Engine](https://www.vaultproject.io/docs/secrets/kv/kv-v2)den Vault-Geheimnissen zugeordnet. Das bedeutet, dass die Details jedes {{site.data.keyword.ieam}} Geheimnisses aus einem Schlüssel und einem Wert zusammengesetzt sind. Beide werden als Teil der Details des geheimen Schlüssels gespeichert, und beide können auf einen beliebigen Zeichenfolgewert gesetzt werden. Eine allgemeine Verwendung dieser Funktion besteht darin, den Typ des geheimen Schlüssels für den Schlüssel und die sensiblen Informationen als Wert anzugeben. Setzen Sie zum Beispiel den Schlüssel auf "basicauth" und setzen Sie den Wert auf "user:password". Dabei kann der Service-Entwickler den Typ des geheimen Schlüssels abfragen, so dass der Service-Code den Wert korrekt verarbeiten kann.

Die Namen von Geheimnissen im Secrets Manager sind niemals durch eine Serviceimplementierung bekannt. Es ist nicht möglich, Informationen aus dem Vault in eine Serviceimplementierung zu übertragen, indem der Name eines geheimen Schlüssels verwendet wird.

Geheimnisse werden in der KV V2 Secrets Engine gespeichert, indem der geheime Name mit "openhorizon" und der Organisation des Benutzers vorfixiert wird. Dadurch wird sichergestellt, dass die von {{site.data.keyword.ieam}} Benutzern erstellten Geheimnisse von anderen Anwendungen des Vault durch andere Integrationen isoliert werden, und zudem, dass eine Multi-Tenant-Isolation beibehalten wird.

Geheime Namen werden von {{site.data.keyword.ieam}} org Admins (oder Benutzern bei Verwendung von privaten Benutzergeheimnissen) verwaltet. Die Vault-Zugriffskontrolllisten (ACLs) steuern, welche Geheimnisse ein {{site.data.keyword.ieam}} Benutzer verwalten kann. Dies erfolgt über ein Vault-Authentifizierungs-Plug-in, das die Benutzerauthentifizierung an {{site.data.keyword.ieam}} Exchange delegiert. Beim erfolgreichen Authentifizieren eines Benutzers erstellt das Authentifizierungs-Plug-in im Vault eine Gruppe von ACL-Richtlinien, die für diesen Benutzer spezifisch sind. Ein Benutzer mit Administratorrechten in Exchange kann:
- Alle Geschäftsgeheimnisse hinzufügen, entfernen und auflisten.
- Hinzufügen, Entfernen, Lesen und Auflisten aller geheimen Daten, die für diesen Benutzer privat sind.
- Entfernen Sie die privaten Geheimnisse anderer Benutzer in der Organisation, und listen Sie sie auf. Sie können diese Geheimnisse jedoch nicht hinzufügen oder lesen.

Ein Benutzer ohne Administratorrechte kann:
- Alle Geschäftsgeheimnisse der Organisation auflisten, sie jedoch nicht hinzufügen, entfernen oder lesen.
- Hinzufügen, Entfernen, Lesen und Auflisten aller geheimen Daten, die für diesen Benutzer privat sind.

Der {{site.data.keyword.ieam}} Agbot hat auch Zugriff auf Geheimnisse, um sie in Edge-Knoten implementieren zu können. Der agbot pflegt eine nachwachsende Anmeldung zum Vault und gibt ACL-Richtlinien speziell für seine Zwecke an. Ein agbot kann:
- Organisationsweite Geheimnisse lesen und alle privaten geheimen Benutzer in einer beliebigen Organisation, aber er kann keine Geheimnisse hinzufügen, entfernen oder auflisten.

Die Exchange-Rootbenutzer und die Exchange-Hub-Administratoren verfügen über keine Berechtigungen im Vault. Weitere Informationen zu diesen Rollen finden Sie unter [Role-Based Access Control](../user_management/rbac.html).
