# IBM&reg; Edge Application Manager

## Einführung

IBM Edge Application Manager stellt eine durchgängige **Anwendungsmanagementplattform** für Anwendungen auf Edge-Einheiten bereit, die für IoT-Bereitstellungen typisch sind. Die Plattform ermöglicht eine vollständige Automatisierung und erspart Anwendungsentwicklern den Aufwand für die sichere Bereitstellung der Revisionen von Edge-Workloads auf Tausenden von in der Praxis eingesetzten Edge-Einheiten. Stattdessen kann sich der Anwendungsentwickler auf die Aufgabe konzentrieren, den Anwendungscode in jeder Programmiersprache als unabhängig bereitstellbaren Docker-Container zu schreiben. Diese Plattform übernimmt die Last, die komplette Geschäftslösung als mehrschichtige Orchestrierung von Docker-Containern auf allen Einheiten sicher und nahtlos bereitzustellen.

https://www.ibm.com/cloud/edge-application-manager

## Voraussetzungen

Informieren Sie sich bei Bedarf über die [Voraussetzungen](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.1/hub/offline_installation.html#prereq).

## Red Hat OpenShift SecurityContextConstraints - Voraussetzungen

Der Standardname für `SecurityContextConstraints`: [`restricted`](https://ibm.biz/cpkspec-scc) wurde für dieses Chart geprüft. Das vorliegende Release ist auf die Bereitstellung unter dem Namensbereich `kube-system` beschränkt und erstellt Servicekonten für das Haupt-Chart sowie zusätzliche Servicekonten für die standardmäßigen untergeordneten Charts der lokalen Datenbank.

## Chart-Details

Das Helm Chart installiert und konfiguriert die zertifizierten IBM Edge Application Manager-Container in einer OpenShift-Umgebung. Folgende Komponenten werden installiert:

* IBM Edge Application Manager - Exchange
* IBM Edge Application Manager - AgBots
* IBM Edge Application Manager - Cloud Sync Service (Teil von Model Management System)
* IBM Edge Application Manager - Benutzerschnittstelle (Managementkonsole)

## Erforderliche Ressourcen

Informieren Sie sich bei Bedarf über die erforderliche [Dimensionierung](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.1/hub/cluster_sizing.html).

## Speicher- und Datenbankanforderungen

Zum Speichern der Daten der IBM Edge Application Manager-Komponenten werden drei Datenbankinstanzen benötigt.

Standardmäßig installiert das Chart drei persistente Datenbanken mit der unten angegebenen Datenträgergröße unter Verwendung einer definierten standardmäßigen (oder benutzerkonfigurierten) Kubernetes-Speicherklasse für dynamische Speicherverwaltung. Achten Sie auf ausreichende Erweiterungsmöglichkeiten, wenn Sie eine Speicherklasse verwenden, die keine Datenträgererweiterung zulässt.

**Hinweis:** Diese Standarddatenbanken sind nicht für die produktive Nutzung vorgesehen. Um Ihre eigenen verwalteten Datenbanken zu nutzen, lesen Sie die nachstehenden Anforderungen und befolgen Sie die Schritte im Abschnitt **Ferne Datenbanken konfigurieren**.

* PostgreSQL: Speichert die Daten von Exchange und AgBot
  * Es werden zwei separate Instanzen mit jeweils 20 GB Speicher benötigt.
  * Die Instanz sollte mindestens 100 Verbindungen unterstützen.
  * Für den Produktionseinsatz sollten diese Instanzen hoch verfügbar sein.
* MongoDB: Speichert die Daten von Cloud Sync Service.
  * Es wird eine Instanz mit mindestens 50 GB Speicher benötigt. **Hinweis:** Die erforderliche Größe ist stark abhängig von der Dimensionierung und Anzahl der Edge-Service-Modelle und Dateien, die Sie speichern und verwenden.
  * Für den Produktionseinsatz sollte diese Instanz hoch verfügbar sein.

**Hinweis:** Die Verantwortung für den Sicherungsrhythmus und die Sicherungsverfahren für diese Standarddatenbanken sowie für Ihre eigenen verwalteten Datenbanken liegt bei Ihnen.
Die Standarddatenbankprozeduren werden im Abschnitt **Sicherung und Wiederherstellung** beschrieben.

## Ressourcen überwachen

Nach der Installation von IBM Edge Application Manager wird automatisch eine Basisüberwachung der in Kubernetes ausgeführten Produktressourcen gestartet. Die Überwachungsdaten können im Grafana-Dashboard der Managementkonsole an folgender Position angezeigt werden:

* `https://<MANAGEMENT_URL:PORT>/grafana/d/kube-system-ibm-edge-overview/ibm-edge-overview`

## Konfiguration

#### Ferne Datenbanken konfigurieren

1. Für die Nutzung Ihrer eigenen verwalteten Datenbanken suchen Sie in `values.yaml` den folgenden Helm-Konfigurationsparameter und ändern Sie seinen Wert in `false`:

```yaml
localDBs:
  enabled: true
```

2. Erstellen Sie eine Datei (z. B. mit dem Namen `dbinfo.yaml`), die mit diesem Vorlageninhalt beginnt:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: ibm-edge-remote-dbs
  labels:
    release: ibm-edge
type: Opaque
stringData:
  # agbot postgresql connection settings
  agbot-db-host: "Single hostname of the remote database"
  agbot-db-port: "Single port the database runs on"
  agbot-db-name: "The name of the database to utilize on the postgresql instance"
  agbot-db-user: "Username used to connect"
  agbot-db-pass: "Password used to connect"
  agbot-db-ssl: "SSL Options: <disable|require|verify-full>"

  # exchange postgresql connection settings
  exchange-db-host: "Single hostname of the remote database"
  exchange-db-port: "Single port the database runs on"
  exchange-db-name: "The name of the database to utilize on the postgresql instance"
  exchange-db-user: "Username used to connect"
  exchange-db-pass: "Password used to connect"
  exchange-db-ssl: "SSL Options: <disable|require|verify-full>"

  # css mongodb connection settings
  css-db-host: "Comma separate <hostname>:<port>,<hostname2>:<port2>"
  css-db-name: "The name of the database to utilize on the mongodb instance"
  css-db-user: "Username used to connect"
  css-db-pass: "Password used to connect"
  css-db-auth: "The name of the database used to store user credentials"
  css-db-ssl: "SSL Options: <true|false>"

  trusted-certs: |-
    -----BEGIN CERTIFICATE-----
    ....
    -----END CERTIFICATE-----
    -----BEGIN CERTIFICATE-----
    ....
    -----END CERTIFICATE-----
```

3. Bearbeiten Sie die Datei `dbinfo.yaml` und geben Sie die Zugriffsinformationen für die von Ihnen bereitgestellten Datenbanken an. Füllen Sie alle Informationen zwischen den doppelten Anführungszeichen aus (wobei die Werte in Anführungszeichen bleiben). Beim Hinzufügen der vertrauenswürdigen Zertifikate stellen Sie sicher, dass jede Zeile um 4 Leerzeichen eingerückt ist, damit die yaml-Datei ordnungsgemäß gelesen werden kann. Wenn zwei oder mehr Datenbanken dasselbe Zertifikat verwenden, muss das Zertifikat **nicht** in `dbinfo.yaml` wiederholt werden. Speichern Sie die Datei und führen Sie anschließend Folgendes aus:

```bash
oc --namespace kube-system apply -f dbinfo.yaml
```


#### Erweiterte Konfiguration

Informieren Sie sich vor Änderungen an den Helm-Standardkonfigurationsparametern zunächst mithilfe des folgenden `grep`-Befehls über die Parameter und die zugehörigen Beschreibungen und zeigen Sie dann die entsprechenden Werte in der Datei `values.yaml` an. Bearbeiten Sie anschließend bei Bedarf zu ändernde Werte.

```bash
grep -v -E '(^ *#|__metadata)' ibm_cloud_pak/values-metadata.yaml
vi values.yaml   # Sie können stattdessen auch einen beliebigen Editor verwenden.
```

## Chart installieren

**Hinweise:**

* Hierbei handelt es sich um eine ausschließliche CLI-Installation; die Installation über die GUI wird nicht unterstützt.

* Stellen Sie sicher, dass die im Abschnitt zum [Installationsprozess für die IBM Edge Application Manager-Infrastruktur](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.1/hub/offline_installation.html#process) angegebenen Schritte ausgeführt wurden.
* Pro Cluster kann nur eine einzige Instanz von IBM Edge Application Manager installiert sein und die Installation dieser Instanz darf nur für den Namensbereich `kube-system` erfolgt sein.
* Ein Upgrade von IBM Edge Application Manager 4.0 wird nicht unterstützt.

Führen Sie das bereitgestellte Installationsscript für die Installation von IBM Edge Application Manager aus. Die Hauptschritte, die vom Script ausgeführt werden, sind: Installation des Helm Charts und Konfiguration der Umgebung nach der Installation (Erstellen der Agbot-, Organisations- und Muster-/Richtlinienservices).

```bash
ibm_cloud_pak/pak_extensions/support/ieam-install.sh
```

**Hinweis:** Je nach Netzgeschwindigkeit beansprucht das Herunterladen der Images und Bereitstellen der gesamten Chartressourcen einige Minuten.

### Chart überprüfen

* Das obige Skript überprüft, ob die Pods laufen und ob Agbot und Exchange antworten. Suchen Sie nach der Nachricht "RUNNING" und "PASSED" am Ende der Installation.
* Bei "FAILED" werden Sie in der Ausgabe gebeten, in bestimmten Protokollen nach weiteren Informationen zu sehen.
* Bei "PASSED" zeigt die Ausgabe Details zu den ausgeführten Tests sowie die URL für die Verwaltungsbenutzerschnittstelle an.
  * Navigieren Sie zu der Benutzerschnittstellenkonsole von IBM Edge Application Manager unter der URL, die am Ende des Protokolls angegeben ist.
    * `https://<MANAGEMENT_URL:PORT>/edge`

## Nach der Installation

Befolgen Sie die Schritte in [Konfiguration nach der Installation](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.1/hub/post_install.html).

## Chart deinstallieren

Führen Sie die Schritte zum [Deinstallieren des Management-Hubs](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.1/hub/uninstall.html) aus.

## Rollenbasierter Zugriff

* Für die Installation und Verwaltung dieses Produkts ist die Clusteradministrator-Berechtigung im Namensbereich `kube-system` erforderlich.
* Servicekonten, Rollen und Rollenbindungen werden für das Chart und die untergeordneten Charts auf der Basis des Releasenamens erstellt.
* Exchange-Authentifizierung und -Rollen:
  * Die Authentifizierung aller Exchange-Administratoren und -Benutzer wird von IAM über API-Schlüssel bereitgestellt, die mit dem Befehl `cloudctl` generiert werden.
  * Exchange-Administratoren muss die `admin`-Berechtigung innerhalb von Exchange erteilt werden. Mit dieser Berechtigung können sie alle Benutzer, Knoten, Services, Muster und Richtlinien innerhalb ihrer Exchange-Organisation verwalten.
  * Exchange-Benutzer ohne Administratorberechtigung können nur solche Benutzer, Knoten, Services, Muster und Richtlinien verwalten, die sie erstellt haben.

## Sicherheit

* Für alle Daten, die als Ingress in den OpenShift-Cluster eingehen oder ihn verlassen, wird TLS verwendet. In diesem Release wird TLS **nicht innerhalb** des OpenShift-Clusters für die Knoten-zu-Knoten-Kommunikation verwendet. Konfigurieren Sie das Red Hat OpenShift-Servicenetz bei Bedarf für eine Kommunikation zwischen Mikroservices. Siehe hierzu [Informationen zum Red Hat OpenShift-Servicenetz](https://docs.openshift.com/container-platform/4.4/service_mesh/service_mesh_arch/understanding-ossm.html#understanding-ossm).
* Dieses Chart stellt keine Verschlüsselung ruhender Daten bereit.  Die Konfiguration einer Verschlüsselung für gespeicherte ruhende Daten ist dem Administrator überlassen.

## Sicherung und Wiederherstellung

Führen Sie die Schritte zur [Sicherung und Wiederherstellung](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.1/admin/backup_recovery.html) aus.

## Einschränkungen

* Einschränkungen der Installation: Dieses Produkt kann nur einmal und nur in den Namensbereich `kube-system` installiert werden.

## Dokumentation

* Ziehen Sie die Dokumentation im Knowledge Center für [Installation](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.1/hub/hub.html) zurate, wenn Sie zusätzliche Informationen benötigen.

## Copyright

© Copyright IBM Corporation 2020. All Rights Reserved.
