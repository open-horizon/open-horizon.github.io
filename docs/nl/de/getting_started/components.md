---

copyright:
years: 2019, 2020
lastupdated: "2020-02-10"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Komponenten

{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) enthält eine Reihe von Komponenten, die im Lieferumfang des Produkts enthalten sind.
{:shortdesc}

Die folgende Tabelle enthält eine Beschreibung der Komponenten von {{site.data.keyword.ieam}}:

|Komponente|Version|Beschreibung|
|---------|-------|----|
|[IBM Cloud Platform Common Services](https://www.ibm.com/docs/en/cpfs)|3.6.x|Hierbei handelt es sich um eine Gruppe von Basiskomponenten, die automatisch im Rahmen der {{site.data.keyword.ieam}}-Operatorinstallation installiert werden.|
|Agbot|{{site.data.keyword.anax_ver}}|Agbot-Instanzen (Agbot - Agreement-Bot - Vereinbarungsbot) werden zentral erstellt und werden verwendet, um Workloads und Modelle für maschinelles Lernen auf {{site.data.keyword.ieam}} bereitzustellen.|
|MMS |1.5.3-338|Das MMS (Modell Management System) vereinfacht die Speicherung, Übermittlung und Sicherheit von Modellen, Daten und anderen Metadatenpaketen, die von den Edge-Services benötigt werden. Auf diese Weise können Edge-Knoten Modelle und Metadaten einfach an die Cloud senden und aus ihr empfangen.|
|Exchange-API|2.87.0-531|Exchange stellt die REST-API bereit, die alle Definitionen (Muster, Richtlinien, Services usw.) enthält, die von allen anderen Komponenten in {{site.data.keyword.ieam}} verwendet werden.|
|Managementkonsole|1.5.0-578|Die Webbenutzerschnittstelle, die von {{site.data.keyword.ieam}}-Administratoren verwendet wird, um die anderen Komponenten von {{site.data.keyword.ieam}} anzuzeigen und zu verwalten.|
|Secure Device Onboard|1.11.11-441|Die Komponente Secure Device Onboard (SDO) ermöglicht die Nutzung der Intel-Technologie zur einfachen und sicheren Konfiguration von Edge-Einheiten und deren Zuordnung zu einem Edge-Management-Hub.|
|Clusteragent|{{site.data.keyword.anax_ver}}|Ein Container-Image, das als Agent in Edge-Clustern installiert wird, um das Workload-Management für Knoten durch {{site.data.keyword.ieam}} zu ermöglichen.|
|Einheitenagent|{{site.data.keyword.anax_ver}}|Diese Komponente wird auf Edge-Einheiten installiert, um das Workload-Management für Knoten durch {{site.data.keyword.ieam}} zu ermöglichen.|
|Secrets Manager|1.0.0-168|Der Secrets Manager ist das Repository für geheime Schlüssel, die in Edge-Einheiten implementiert sind, und ermöglicht es Services, Berechtigungsnachweise sicher zu empfangen, die für die Authentifizierung bei ihren Upstream-Abhängigkeiten verwendet werden.|
