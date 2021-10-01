---

copyright:
years: 2020
lastupdated: "2020-10-7"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Hinweise zur Datenschutz-Grundverordnung (DSGVO)

## Hinweis
{: #notice}
<!-- This is boilerplate text provided by the GDPR team. It cannot be changed. -->

Dieses Dokument soll Sie bei Ihren Vorbereitungen für die Umsetzung der DSGVO unterstützen. Hier finden Sie Informationen zu den Funktionen von {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}), die Sie konfigurieren können, sowie Aspekte zur Produktverwendung, die Sie berücksichtigen sollten, wenn Sie Ihre Organisation auf die DSGVO-Umsetzung vorbereiten. Die Informationen erheben keinen Anspruch auf Vollständigkeit. Kunden stehen zahlreiche Möglichkeiten zum Auswählen und Konfigurieren der Funktionen und Verwendungsweisen des Produkts an sich sowie in Kombination mit Anwendungen und Systemen anderer Anbieter zur Verfügung.

<p class="ibm-h4 ibm-bold">Jeder Kunde ist für die Einhaltung der geltenden Gesetze und Verordnungen, einschließlich der Datenschutz-Grundverordnung der Europäischen Union selbst verantwortlich. Es obliegt allein den Kunden, sich von kompetenter juristischer Stelle zu Inhalt und Auslegung aller relevanten Gesetze und Vorschriften beraten zu lassen, die ihre Geschäftstätigkeit und die von ihnen eventuell einzuleitenden Maßnahmen zur Einhaltung dieser Gesetze und Vorschriften betreffen.</p>

<p class="ibm-h4 ibm-bold">Die hierin beschriebenen Produkte, Services und sonstigen Funktionen eignen sich nicht für alle Kundensituationen und sind möglicherweise nur eingeschränkt verfügbar. IBM erteilt keine Rechts- oder Steuerberatung und gibt keine Garantie bezüglich der Konformität von IBM Produkten oder Services mit den geltenden Gesetzen und Vorschriften.</p>

## Inhaltsverzeichnis

* [Datenschutz-Grundverordnung (DSGVO)](#overview)
* [Produktkonfiguration für DSGVO](#productconfig)
* [Datenlebenszyklus](#datalifecycle)
* [Datenverarbeitung](#dataprocessing)
* [Möglichkeiten zur Beschränkung der Verwendung personenbezogener Daten](#datasubjectrights)
* [Anhang](#appendix)

## Datenschutz-Grundverordnung (DSGVO)
{: #overview}

<!-- This is boilerplate text provided by the GDPR team. It cannot be changed. -->
Die Datenschutz-Grundverordnung (DSGVO) wurde von der Europäischen Union (EU) eingeführt und gilt seit dem 25 Mai 2018.

### Warum ist die DSGVO so wichtig?

Die DSGVO legt einen strengeren datenschutzrechtlichen Rahmen für die Verarbeitung personenbezogener Daten von Einzelpersonen fest. Das bietet die DSGVO:

* Neue und erweiterte Rechte für Einzelpersonen
* Erweiterte Definition der personenbezogenen Daten
* Neue Verpflichtungen für Unternehmen und Organisationen bei der Handhabung personenbezogener Daten
* Androhung hoher Bußgelder für die Nichteinhaltung
* Verpflichtende Benachrichtigung bei Datenschutzverletzungen

IBM hat ein globales Umsetzungsprogramm eingerichtet, dessen Aufgabe es ist, IBM interne Prozesse und kommerzielle Angebote für die Konformität mit der DSGVO vorzubereiten.

### Weitere Informationen

* [EU-DSGVO-Informationsportal](https://gdpr.eu/)
*  [ibm.com/GDPR-Website](https://www.ibm.com/data-responsibility/gdpr/)

## Produktkonfiguration - Hinweise zur Umsetzung der DSGVO
{: #productconfig}

In den folgenden Abschnitten sind Aspekte von {{site.data.keyword.ieam}} beschrieben und Informationen zu Leistungsmerkmalen verfügbar, die Kunden dabei unterstützen, die Voraussetzungen für die DSGVO-Umsetzung zu schaffen.

### Datenlebenszyklus
{: #datalifecycle}

{{site.data.keyword.ieam}} ist eine Anwendung für die Entwicklung und Verwaltung von lokalen containerisierten Anwendungen. Das Produkt stellt eine integrierte Umgebung für die Verwaltung von Container-Workloads in der Peripherie dar. Es umfasst den Containerorchestrator 'Kubernetes', eine private Image-Registry, eine Managementkonsole, einen Edge-Knotenagenten sowie Überwachungsframeworks.

{{site.data.keyword.ieam}} arbeitet in erster Linie mit technischen Daten zusammen, die sich auf die Konfiguration und Verwaltung der Anwendung beziehen, von denen einige möglicherweise der DSGVO unterliegen. {{site.data.keyword.ieam}} arbeitet auch mit Informationen zu Benutzern, die die Anwendung verwalten. Diese Daten sind im vorliegenden Dokument beschrieben, damit Kunden, die für die Erfüllung der Voraussetzungen für die DSGVO-Umsetzung verantwortlich sind, sich dieser Daten bewusst sind.

Diese Daten sind bei {{site.data.keyword.ieam}} in lokalen oder fernen Dateisystemen als Konfigurationsdateien oder in Datenbanken permanent gespeichert. Anwendungen, die für die Ausführung unter {{site.data.keyword.ieam}} entwickelt werden, können andere Formen von personenbezogenen Daten verwenden, die der DSGVO unterliegen. Die Mechanismen, die zum Schutz und zur Verwaltung der Daten verwendet werden, sind auch für Anwendungen verfügbar, die unter {{site.data.keyword.ieam}} ausgeführt werden. Zum Schutz und zur Verwaltung von personenbezogenen Daten, die von Anwendungen erfasst werden, deren Ausführung unter {{site.data.keyword.ieam}} erfolgt, werden möglicherweise weitere Mechanismen benötigt.

Um die Datenflüsse in {{site.data.keyword.ieam}} nachvollziehen zu können, müssen Sie verstehen, wie Kubernetes, Docker und Operatoren arbeiten. Diese Open-Source-Komponenten sind von grundlegender Bedeutung für {{site.data.keyword.ieam}}. Mithilfe von {{site.data.keyword.ieam}} stellen Sie Instanzen von Anwendungscontainern (Edge-Services) auf Edge-Knoten zur Verfügung. Die Edge-Services enthalten die Details über die Anwendung; die Docker-Images enthalten alle Softwarepakete, die zur Ausführung der Anwendungen benötigt werden.

{{site.data.keyword.ieam}} beinhaltet eine Reihe von Beispielen für Open-Source-Edge-Services. Eine Liste aller {{site.data.keyword.ieam}}-Diagramme finden Sie unter [open-horizon/examples](https://github.com/open-horizon/examples){:new_window}. Die Ermittlung und Implementierung geeigneter DSGVO-Kontrollmechanismen für Open-Source-Software liegt in der Verantwortlichkeit des Kunden.

### Typen von Datenflüssen in {{site.data.keyword.ieam}}

{{site.data.keyword.ieam}} arbeitet mit verschiedenen Kategorien von technischen Daten, die als personenbezogene Daten eingestuft werden können. Hierzu gehören unter anderem:

* ID und Kennwort für Benutzer mit Administrator- oder Bedienerberechtigung
* IP-Adressen
* Kubernetes-Knotennamen

In späteren Abschnitten dieses Dokuments ist beschrieben, wie auf diese technischen Daten zugegriffen wird und wie die Daten erfasst und erstellt, gespeichert, geschützt, protokolliert und gelöscht werden.

### Für Onlinekontakt zu IBM genutzte personenbezogene Daten

{{site.data.keyword.ieam}}-Kunden können auf verschiedenen Wegen an IBM Onlinekommentare, -rückmeldungen und -anforderungen zu   {{site.data.keyword.ieam}}-Themen übergeben; hauptsächlich wird hierzu Folgendes genutzt:

* Öffentliche Slack-Community für {{site.data.keyword.ieam}}
* Bereiche für öffentliche Kommentare auf den Seiten der Produktdokumentation zu {{site.data.keyword.ieam}}
* Öffentliche Kommentare im Bereich von dW Answers für {{site.data.keyword.ieam}}

In der Regel werden für persönliche Antworten auf das Thema des Kontakts lediglich der Kundenname und die E-Mail-Adresse verwendet. Diese Verwendung personenbezogener Daten entspricht der [IBM Online-Datenschutzbestimmung](https://www.ibm.com/privacy/us/en/){:new_window}.

### Authentifizierung

Der {{site.data.keyword.ieam}}-Authentifizierungsmanager akzeptiert Benutzerberechtigungsnachweise aus der {{site.data.keyword.gui}} und leitet die Berechtigungsnachweise an den OIDC-Back-End-Provider weiter, der die Benutzerberechtigungsnachweise anhand des Unternehmensverzeichnisses überprüft. Der OIDC-Provider gibt anschließend ein Authentifizierungscookie (`auth-cookie`) mit dem Inhalt eines JSON-Web-Tokens (`JWT`) an den Authentifizierungsmanager zurück. Im JWT-Token sind neben der Benutzer-ID und E-Mail-Adresse zusätzlich Angaben über die Gruppenzugehörigkeit zum Zeitpunkt der Authentifizierungsanforderung gespeichert. Dieses Authentifizierungscookie wird danach zurück an die {{site.data.keyword.gui}} gesendet. Während der Sitzung wird das Cookie aktualisiert. Nach der Abmeldung bei der  {{site.data.keyword.gui}} oder dem Schließen des Web-Browsers ist es 12 Stunden lang gültig.

Bei allen nachfolgenden Authentifizierungsanforderungen, die von der {{site.data.keyword.gui}} ausgegeben werden, entschlüsselt der NodeJS-Front-End-Server das verfügbare Authentifizierungscookie in der Anforderung und validiert die Anforderung durch einen Aufruf des Authentifizierungsmanagers.

Bei der {{site.data.keyword.ieam}}-CLI muss der Benutzer einen API-Schlüssel angeben. API-Schlüssel werden mit dem Befehl `cloudctl` erstellt.

Die CLIs **cloudctl**, **kubectl** und **oc** machen für den Zugriff auf den Cluster ebenfalls Berechtigungsnachweise erforderlich. Diese Berechtigungsnachweise werden aus der Managementkonsole abgerufen und laufen nach 12 Stunden ab.

### Rollenzuordnung

{{site.data.keyword.ieam}} unterstützt die rollenbasierte Zugriffssteuerung (Role-based access control, RBAC). In der Rollenzuordnungsphase wird dem Benutzernamen, der in der Authentifizierungsphase bereitgestellt wird, eine Benutzer- oder Gruppenrolle zugeordnet. Die Rollen autorisieren die Aktivitäten, die durch den authentifizierten Benutzer ausgeführt werden können. Im Abschnitt [Rollenbasierte Zugriffssteuerung](rbac.md) finden Sie Details über {{site.data.keyword.ieam}}-Rollen.

### Pod-Sicherheit

Mit Pod-Sicherheitsrichtlinien wird die Steuerung auf Management-Hub- oder Edge-Clusterebene der für einen Pod verfügbaren Funktionen und Zugriffsrechte eingerichtet. Weitere Informationen zu Pods enthalten die Abschnitte [Management-Hub installieren](../hub/hub.md) und [Edge-Cluster](../installing/edge_clusters.md).

## Datenverarbeitung
{: #dataprocessing}

Benutzer von {{site.data.keyword.ieam}} können steuuern, wie technische Daten, die sich auf die Konfiguration und die Verwaltung beziehen, bei der Systemkonfiguration verarbeitet und geschützt werden.

* Die rollenbasierte Zugriffssteuerung steuert, auf welche Daten und Funktionen Benutzer zugreifen können.

* Mit Pod-Sicherheitsrichtlinien wird die Steuerung auf Clusterebene der für einen Pod verfügbaren Funktionen und Zugriffsrechte eingerichtet.

* Daten werden bei der Übertragung mit `TLS` geschützt. `HTTPS` (mit zugrundeliegendem `TLS`) wird für die sichere Datenübertragung zwischen Client- und Back-End-Services verwendet. Benutzer können während der Installation das zu verwendende Stammzertifikat angeben.

* Der Schutz für ruhende Daten wird durch die Verwendung von `dm-crypt` zur Datenverschlüsselung unterstützt.

* Die Dauer der Datenaufbewahrung für die Protokollierung (ELK) und Überwachung (Prometheus) ist konfigurierbar; die Datenlöschung wird durch bereitgestellte APIs unterstützt.

Dieselben Mechanismen, die für die Verwaltung und den Schutz der technischen Daten von {{site.data.keyword.ieam}} eingesetzt werden, können auch zur Verwaltung und zum Schutz von personenbezogenen Daten für die vom Benutzer entwickelten oder bereitgestellten Anwendungen genutzt werden. Kunden können eigene Funktionalität entwickeln, um weitergehende Kontrollmechanismen zu implementieren.

Weitere Informationen zu Zertifikaten erhalten Sie unter [{{site.data.keyword.ieam}} installieren](../hub/installation.md).

## Möglichkeiten zur Beschränkung der Verwendung personenbezogener Daten
{: #datasubjectrights}

Mit den in diesem Dokument zusammengefassten Funktionen versetzt {{site.data.keyword.ieam}} einen Benutzer in die Lage, die Nutzung von technischen Daten innerhalb der Anwendung einzuschränken, die als personenbezogene Daten eingestuft werden.

Gemäß der DSGVO besitzen Benutzer Berechtigungen, um auf die Verarbeitung zuzugreifen, sie zu ändern und sie einzuschränken. In anderen Abschnitten dieses Dokuments finden Sie weitere Informationen zu den folgenden Kontrollinstrumenten:
* Recht auf Zugriff
  * {{site.data.keyword.ieam}}-Administratoren können mit {{site.data.keyword.ieam}}-Funktionen Einzelpersonen den Zugriff auf ihre Daten ermöglichen.
  * {{site.data.keyword.ieam}}-Administratoren können mit {{site.data.keyword.ieam}}-Funktionen Einzelpersonen darüber informieren, welche Daten {{site.data.keyword.ieam}} über sie erfasst und aufbewahrt.
* Recht auf Änderung
  * {{site.data.keyword.ieam}}-Administratoren können mit {{site.data.keyword.ieam}}-Funktionen einer Einzelperson erlauben, ihre Daten zu ändern oder zu korrigieren.
  * {{site.data.keyword.ieam}}-Administratoren können mit {{site.data.keyword.ieam}}-Funktionen die Daten einer Einzelperson für sie korrigieren.
* Recht auf Beschränkung der Verarbeitung
  * {{site.data.keyword.ieam}}-Administratoren können mit {{site.data.keyword.ieam}}-Funktionen die Verarbeitung von Daten einer Einzelperson stoppen.

## Anhang- Von {{site.data.keyword.ieam}} protokollierte Daten
{: #appendix}

Als Anwendung arbeitet {{site.data.keyword.ieam}} mit verschiedenen Kategorien von technischen Daten, die als personenbezogene Daten eingestuft werden können:

* ID und Kennwort für Benutzer mit Administrator- oder Bedienerberechtigung
* IP-Adressen
* Kubernetes-Knotennamen 

{{site.data.keyword.ieam}} arbeitet auch mit Informationen zu Benutzern, die die unter {{site.data.keyword.ieam}} ausgeführten Anwendungen verwalten, und nimmt möglicherweise weitere Kategorien von personenbezogenen Daten auf, die der Anwendung unbekannt sind.

### Sicherheit bei {{site.data.keyword.ieam}}

* Umfang der protokollierten Daten
  * Benutzer-ID, Benutzername und IP-Adresse von angemeldeten Benutzern
* Zeitpunkt der Datenprotokollierung
  * Bei Anmeldeanforderungen
* Position der Datenprotokollierung
  * Auditprotokolle unter `/var/lib/icp/audit`
  * Auditprotokolle unter `/var/log/audit`
  * Exchange-Protokolle
* Datenlöschung
  * Suchen Sie nach den Daten und löschen Sie den Datensatz aus dem Auditprotokoll.

### {{site.data.keyword.ieam}}-API

* Umfang der protokollierten Daten
  * Benutzer-ID, Benutzername und IP-Adresse des Clients in Containerprotokollen
  * Daten zum Status des Kubernetes-Clusters in Server `etcd`
  * OpenStack- und VMware-Berechtigungsnachweise im Server `etcd`
* Zeitpunkt der Datenprotokollierung
  * Bei API-Anforderungen
  * Mit dem Befehl `credentials-set` gespeicherte Berechtigungsnachweise
* Position der Datenprotokollierung
  * Containerprotokolle, Elasticsearch und Server `etcd`
* Datenlöschung
  * Löschen Sie Containerprotokolle (`platform-api`, `platform-deploy`) aus Containern oder löschen Sie die benutzerspezifischen Protokolleinträge aus Elasticsearch.
  * Löschen Sie die ausgewählten Schlüssel/Wert-Paare für `etcd` mit dem Befehl `etcdctl rm`.
  * Entfernen Sie Berechtigungsnachweise durch einen Aufruf des Befehls `credentials-unset`.


Weitere Informationen finden Sie in den folgenden Abschnitten:

  * [Kubernetes-Protokollierung](https://kubernetes.io/docs/concepts/cluster-administration/logging/){:new_window}
  * [etcdctl](https://github.com/coreos/etcd/blob/master/etcdctl/READMEv2.md){:new_window}

### {{site.data.keyword.ieam}}-Überwachung

* Umfang der protokollierten Daten
  * IP-Adresse, Namen von Pods, Release, Image
  * Aus vom Kunden entwickelten Anwendungen mit Scraping erfasste Daten können personenbezogene Daten beinhalten
* Zeitpunkt der Datenprotokollierung
  * Erfassung von Metriken aus konfigurierten Zielen mit Scraping durch Prometheus
* Position der Datenprotokollierung
  * Prometheus-Server oder konfigurierte persistente Datenträger
* Datenlöschung
  * Suchen und löschen Sie die Daten mit der Prometheus-API.

Weitere Informationen finden Sie in der [Prometheus-Dokumentation](https://prometheus.io/docs/introduction/overview/){:new_window}.


### Kubernetes bei {{site.data.keyword.ieam}}

* Umfang der protokollierten Daten
  * Im Cluster bereitgestellte Topologie (Knoteninformationen für Controller, Worker, Proxy usw.)
  * Servicekonfiguration (k8s-Konfigurationsübersicht) und geheime Schlüssel (geheime k8s-Schlüssel)
  * Benutzer-ID im Protokoll 'apiserver'
* Zeitpunkt der Datenprotokollierung
  * Bereitstellung eines Clusters
  * Bereitstellung einer Anwendung aus dem Helm-Katalog
* Position der Datenprotokollierung
  * Im Cluster bereitgestellte Topologie: `etcd`
  * Konfiguration und geheimer Schlüssel für bereitgestellte Anwendungen: `etcd`
* Datenlöschung
  * Verwenden Sie die {{site.data.keyword.ieam}}-{{site.data.keyword.gui}}.
  * Suchen und löschen Sie Daten mit der k8s-{{site.data.keyword.gui}} (`kubectl`) oder der REST-API von `etcd`
  * Suchen und löschen Sie Daten im Protokoll 'apiserver' mit der Elasticsearch-API.

Lassen Sie beim Ändern der Konfiguration von Kubernetes-Clustern oder beim Löschen von Clusterdaten Vorsicht walten.

  Weitere Informationen finden Sie unter [Kubernetes kubectl](https://kubernetes.io/docs/reference/kubectl/overview/){:new_window}.

### Helm-API von {{site.data.keyword.ieam}}

* Umfang der protokollierten Daten
  * Benutzername und Rolle
* Zeitpunkt der Datenprotokollierung
  * Abruf von Diagrammen oder Repositorys, die zu einem Team hinzugefügt werden, durch einen Benutzer
* Position der Datenprotokollierung
  * Bereitstellungsprotokolle 'helm-api', Elasticsearch
* Datenlöschung
  * Suchen und löschen Sie Daten im Protokoll 'helm-api' mit der Elasticsearch-API.

### Service-Broker von {{site.data.keyword.ieam}}

* Umfang der protokollierten Daten
  * Benutzer-ID (nur bei Debugprotokollebene 10, nicht bei der Standardprotokollebene)
* Zeitpunkt der Datenprotokollierung
  * Ausgabe von API-Anforderungen an den Service-Broker
  * Zugriff des Service-Brokers auf den Servicekatalog
* Position der Datenprotokollierung
  * Containerprotokoll für Service-Broker, Elasticsearch
* Datenlöschung
  * Suchen und löschen Sie das Protokoll 'apiserver', das die Elasticsearch-API verwendet.
  * Suchen und löschen Sie das Protokoll aus dem Container 'apiserver':
      ```
      kubectl logs $(kubectl get pods -n kube-system | grep  service-catalogapiserver | awk '{print $1}') -n kube-system | grep admin
      ```
      {: codeblock}


  Weitere Informationen finden Sie unter [Kubernetes kubectl](https://kubernetes.io/docs/reference/kubectl/overview/){:new_window}.
