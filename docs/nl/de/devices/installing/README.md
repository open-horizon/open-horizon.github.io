# IBM Edge Computing Manager

## Einführung

IBM Edge Computing Manager for Devices stellt eine durchgängige **Anwendungsmanagementplattform** für Anwendungen bereit, die auf Edge-Einheiten bereitgestellt wurden, die typisch für IoT-Bereitstellungen sind. Diese Plattform ermöglicht eine vollständige Automatisierung und befreit die Anwendungsentwickler von der Aufgabe, die Revisionen von Edge-Workloads auf Tausenden von im Feld implementierten Edge-Einheiten sicher bereitzustellen. Stattdessen kann sich der Anwendungsentwickler auf die Aufgabe konzentrieren, den Anwendungscode in jeder Programmiersprache als unabhängig bereitstellbaren Docker-Container zu schreiben. Diese Plattform übernimmt die Last, die komplette Geschäftslösung als mehrschichtige Orchestrierung von Docker-Containern auf allen Einheiten sicher und nahtlos bereitzustellen.

## Voraussetzungen

* Red Hat OpenShift Container Platform 4.2
* IBM Multicloud Management Core 1.2
* Wenn Sie Ihre eigenen Datenbanken hosten, stellen Sie zwei Instanzen von PostgreSQL und eine Instanz von MongoDB bereit, um Daten für die Komponenten von IBM Edge Computing Manager for Devices zu speichern. Details hierzu finden Sie im Abschnitt **Speicher**.
* Ein Ubuntu Linux- oder macOS-Host, von dem aus die Installation gestartet werden soll. Auf ihm muss die folgende Software installiert sein:
  * [Kubernetes-CLI (kubectl)](https://kubernetes.io/docs/tasks/tools/install-kubectl/) Version 1.14.0 oder höher
  * [IBM Cloud Pak-CLI (cloudctl)](https://www.ibm.com/support/knowledgecenter/SSFC4F_1.2.0/cloudctl/icp_cli.html)
  * [OpenShift-CLI (oc)](https://docs.openshift.com/container-platform/4.2/cli_reference/openshift_cli/getting-started-cli.html)
  * [Helm-CLI](https://helm.sh/docs/using_helm/#installing-the-helm-client) Version 2.9.1 oder höher
  * Andere Softwarepakete:
    * jq
    * git
    * Docker (Version 18.06.01 oder höher)
    * make

## Red Hat OpenShift SecurityContextConstraints - Voraussetzungen

Der Standardname für `SecurityContextConstraints`: [`restricted`](https://ibm.biz/cpkspec-scc) wurde für dieses Diagramm geprüft. Dieses Release ist beschränkt auf die Bereitstellung in den Namensbereich `kube-system` und verwendet das Standard-Servicekonto '`default`' zusätzlich zur Erstellung eigener Servicekonten für die optionalen Unterdiagramme der lokalen Datenbank.

## Diagrammdetails

Dieses Helm-Diagramm installiert und konfiguriert den zertifizierten Container für IBM Edge Computing Manager for Devices in einer OpenShift-Umgebung. Folgende Komponenten werden installiert:

* IBM Edge Computing Manager for Devices - Exchange
* IBM Edge Computing Manager for Devices - AgBots
* IBM Edge Computing Manager for Devices - Cloud Sync Service (Teil des Model Management-Systems)
* IBM Edge Computing Manager for Devices - Benutzerschnittstelle (Managementkonsole)

## Erforderliche Ressourcen

Informationen zu den erforderlichen Ressourcen finden Sie unter [Installation - Dimensionierung](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.0/devices/installing/install.html#size).

## Speicher- und Datenbankanforderungen

Drei Datenbankinstanzen sind erforderlich, um die Daten der Komponenten von IBM Edge Computing Manager for Devices zu speichern.

Standardmäßig installiert das Diagramm drei persistente Datenbanken mit den unten angegebenen Dimensionierungen von Datenträgern unter Verwendung einer definierten Standard- (oder benutzerkonfigurierten) dynamischen Kubernetes-Speicherklasse.

**Hinweis:** Diese Standarddatenbanken sind nicht für die produktive Nutzung vorgesehen. Um Ihre eigenen verwalteten Datenbanken zu nutzen, lesen Sie die nachstehenden Anforderungen und befolgen Sie die Schritte im Abschnitt **Ferne Datenbanken konfigurieren**.

* PostgreSQL: Speichert die Daten von Exchange und AgBot
  * Es werden zwei separate Instanzen von jeweils 10 GB Speicher benötigt.
  * Die Instanz sollte mindestens 100 Verbindungen unterstützen.
  * Für den Produktionseinsatz sollten diese Instanzen hoch verfügbar sein. 
* MongoDB: Speichert die Daten von Cloud Sync Service.
  * Es wird eine Instanz von mindestens 50 GB Speicher benötigt. **Hinweis:** Die erforderliche Größe ist stark abhängig von der Dimensionierung und Anzahl der Edge-Service-Modelle und Dateien, die Sie speichern und verwenden.
  * Für den Produktionseinsatz sollte diese Instanz hoch verfügbar sein.

**Hinweis:** Wenn Sie Ihre eigenen verwalteten Datenbanken nutzen, sind Sie für die Sicherungs- und Wiederherstellungsverfahren verantwortlich.
Die Standarddatenbankprozeduren sind im Abschnitt **Sicherung und Wiederherstellung** beschrieben.

## Ressourcen überwachen

Wenn IBM Edge Computing Manager for Devices installiert ist, wird die Überwachung des Produkts und der Pods, auf denen es ausgeführt wird, automatisch eingerichtet. Die Überwachungsdaten können im Grafana-Dashboard der Managementkonsole an den folgenden Positionen angezeigt werden:

* `https://<MANAGEMENT_URL:PORT>/grafana/d/kube-system-edge-computing-overview/edge-computing-overview`
* `https://<MANAGEMENT_URL:PORT>/grafana/d/kube-system-edge-computing-pod-overview/edge-computing-pod-overview`

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
  name: edge-computing-remote-dbs
  labels:
    release: edge-computing
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

Um einen der Standardparameter der Helm-Konfiguration zu ändern, können Sie die Parameter und ihre Beschreibungen mit dem nachstehenden Befehl `grep` überprüfen und dann die entsprechenden Werte in `values.yaml` anzeigen und gegebenenfalls bearbeiten:

```bash
grep -v -E '(^ *#|__metadata)' ibm_cloud_pak/values-metadata.yaml
vi values.yaml   # or use your preferred editor
```

## Diagramm installieren

**Hinweise:**

* Hierbei handelt es sich um eine ausschließliche CLI-Installation; die Installation über die GUI wird nicht unterstützt.

* Sie sollten die Schritte im Abschnitt [IBM Edge Computing Manager for Devices-Infrastruktur installieren - Installationsprozess](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.0/devices/installing/install.html#process) bereits durchgeführt haben.
* Pro Cluster kann nur eine Instanz von IBM Edge Computing Manager for Devices installiert sein und sie darf nur für den Namensbereich `kube-system` installiert sein.
* Ein Upgrade von IBM Edge Computing Manager for Devices 3.2 wird nicht unterstützt.

Führen Sie das bereitgestellte Installationsscript aus, um IBM Edge Computing Manager for Devices zu installieren. Die Hauptschritte, die vom Script ausgeführt werden, sind: Installation des Helm-Diagramms und Konfiguration der Umgebung nach der Installation (Erstellen der Agbot-, Organisations- und Muster-/Richtlinienservices).

```bash
ibm_cloud_pak/pak_extensions/full-install/install-edge-computing.sh
```

**Hinweis:** Abhängig von Ihren Netzgeschwindigkeiten dauert es einige Minuten, bis die Images heruntergeladen sind, während die Pods in den Status RUNNING übergehen und alle Services aktiviert werden.

### Diagramm überprüfen

* Das obige Skript überprüft, ob die Pods laufen und ob Agbot und Exchange antworten. Suchen Sie nach der Nachricht "RUNNING" und "PASSED" am Ende der Installation.
* Bei "FAILED" werden Sie in der Ausgabe gebeten, in bestimmten Protokollen nach weiteren Informationen zu sehen.
* Bei "PASSED" zeigt die Ausgabe Details zu den Tests an, die ausgeführt wurden, sowie zwei weitere Elemente zur Überprüfung.
  * Navigieren Sie zur Benutzerschnittstellenkonsole von IBM Edge Computing Manager in der URL, die am Ende des Protokolls angegeben ist.
    * `https://<MANAGEMENT_URL:PORT>/edge`

## Nach der Installation

Befolgen Sie die Schritte in [Konfiguration nach der Installation](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.0/devices/installing/install.html#postconfig).

## Diagramm deinstallieren

**Hinweis:** Wenn Sie eine Deinstallation mit konfigurierten lokalen Datenbanken durchführen, **werden alle Daten gelöscht**. Wenn Sie diese Daten auch nach der Deinstallation beibehalten möchten, lesen Sie den Abschnitt **Sicherungsprozedur** unten.

Kehren Sie zur Position der README.md-Datei zurück und führen Sie das bereitgestellte Deinstallationsscript aus, um die Deinstallationstasks zu automatisieren. Die Hauptschritte des Scripts sind: Deinstallation der Helm-Diagramme und Entfernung von geheimen Schlüsseln. Melden Sie sich zunächst als Clusteradministrator beim Cluster an und verwenden Sie dazu `cloudctl`. Anschließend gehen Sie wie folgt vor:

```bash
ibm_cloud_pak/pak_extensions/uninstall/uninstall-edge-computing.sh <clustername>
```

**Hinweis:** Wenn Sie ferne Datenbanken angegeben haben, wird der geheime Schlüssel für die Authentifizierung gelöscht; es werden jedoch keine Tasks ausgeführt, um Daten aus diesen fernen Datenbanken aus dem Betrieb zu nehmen oder zu löschen. Wenn Sie diese Daten löschen möchten, tun Sie es jetzt.

## Rollenbasierter Zugriff

* Für die Installation und Verwaltung dieses Produkts ist die Clusteradministrator-Berechtigung im Namensbereich `kube-system` erforderlich.
* Exchange-Authentifizierung und -Rollen:
  * Die Authentifizierung aller Exchange-Administratoren und -Benutzer wird von IAM über API-Schlüssel bereitgestellt, die mit dem Befehl `cloudctl` generiert werden.
  * Exchange-Administratoren muss die `admin`-Berechtigung innerhalb von Exchange erteilt werden. Mit dieser Berechtigung können sie alle Benutzer, Knoten, Services, Muster und Richtlinien innerhalb ihrer Exchange-Organisation verwalten.
  * Exchange-Benutzer ohne Administratorberechtigung können nur solche Benutzer, Knoten, Services, Muster und Richtlinien verwalten, die sie erstellt haben.

## Sicherheit

* Für alle Daten, die als Ingress in den OpenShift-Cluster eingehen oder ihn verlassen, wird TLS verwendet. In diesem Release wird TLS **nicht innerhalb** des OpenShift-Clusters für die Knoten-zu-Knoten-Kommunikation verwendet. Bei Bedarf können Sie das Red Hat OpenShift-Servicenetz für die Kommunikation zwischen Mikroservices konfigurieren. Siehe hierzu [Informationen zum Red Hat OpenShift-Servicenetz](https://docs.openshift.com/container-platform/4.2/service_mesh/service_mesh_arch/understanding-ossm.html#understanding-ossm).
* Von diesem Diagramm wird keine Verschlüsselung ruhender Daten bereitgestellt. Die Konfiguration einer Speicherverschlüsselung ist dem Administrator überlassen.

## Sicherung und Wiederherstellung

### Sicherungsprozedur

Führen Sie diese Befehle aus, nachdem Sie eine Verbindung zu Ihrem Cluster an einer Position hergestellt haben, die über ausreichend Speicherplatz für die Speicherung dieser Sicherungen verfügt.


1. Erstellen Sie ein Verzeichnis, das zum Speichern der folgenden Sicherungen verwendet wird, und nehmen Sie nach Bedarf Anpassungen vor.

```bash
export BACKUP_DIR=/tmp/edge-computing-backup/$(date +%Y%m%d_%H%M%S)
mkdir -p $BACKUP_DIR
```

2. Führen Sie den folgenden Befehl aus, um Authentifizierungen und geheime Schlüssel zu sichern:

```bash
oc -n kube-system get secret edge-computing -o yaml > $BACKUP_DIR/edge-computing-secret.yaml && \
oc -n kube-system get secret edge-computing-agbotdb-postgresql-auth-secret -o yaml > $BACKUP_DIR/edge-computing-agbotdb-postgresql-auth-secret-backup.yaml && \
oc -n kube-system get secret edge-computing-exchangedb-postgresql-auth-secret -o yaml > $BACKUP_DIR/edge-computing-exchangedb-postgresql-auth-secret-backup.yaml && \
oc -n kube-system get secret edge-computing-css-db-ibm-mongodb-auth-secret -o yaml > $BACKUP_DIR/edge-computing-css-db-ibm-mongodb-auth-secret-backup.yaml
```

3. Führen Sie den folgenden Befehl aus, um Datenbankinhalte zu sichern:

```bash
oc -n kube-system exec edge-computing-exchangedb-keeper-0 -- bash -c "export PGPASSWORD=$(oc -n kube-system get secret edge-computing -o jsonpath="{.data.exchange-db-pass}" | base64 --decode) && pg_dump -U admin -h edge-computing-exchangedb-proxy-svc -F t postgres > /stolon-data/exchange-backup.tar" && \
oc -n kube-system cp edge-computing-exchangedb-keeper-0:/stolon-data/exchange-backup.tar $BACKUP_DIR/exchange-backup.tar
```

```bash
oc -n kube-system exec edge-computing-agbotdb-keeper-0 -- bash -c "export PGPASSWORD=$(oc -n kube-system get secret edge-computing -o jsonpath="{.data.agbot-db-pass}" | base64 --decode) && pg_dump -U admin -h edge-computing-agbotdb-proxy-svc -F t postgres > /stolon-data/agbot-backup.tar" && \
oc -n kube-system cp edge-computing-agbotdb-keeper-0:/stolon-data/agbot-backup.tar $BACKUP_DIR/agbot-backup.tar
```

```bash
oc -n kube-system exec edge-computing-cssdb-server-0 -- bash -c "mkdir -p /data/db/backup; mongodump -u admin -p $(oc -n kube-system get secret edge-computing -o jsonpath="{.data.css-db-pass}" | base64 --decode) --out /data/db/css-backup" && \
oc -n kube-system cp edge-computing-cssdb-server-0:/data/db/css-backup $BACKUP_DIR/css-backup
```

4. Nachdem die Sicherungen geprüft wurden, entfernen Sie sie aus den statusunabhängigen Containern.

```bash
oc -n kube-system exec edge-computing-exchangedb-keeper-0 -- bash -c "rm -f /stolon-data/exchange-backup.tar"
```

```bash
oc -n kube-system exec edge-computing-agbotdb-keeper-0 -- bash -c "rm -f /stolon-data/agbot-backup.tar"
```

```bash
oc -n kube-system exec edge-computing-cssdb-server-0 -- bash -c "rm -rf /data/db/css-backup"
```

### Wiederherstellungsprozedur

**Hinweis:** Wenn die Wiederherstellung in einem neuen Cluster erfolgt, muss dieser 'cluster name' mit dem Namen des Clusters übereinstimmen, aus dem die Sicherungen entnommen wurden.

1. Löschen Sie alle bestehenden geheimen Schlüssel aus Ihrem Cluster.
```bash
oc -n kube-system delete secret edge-computing edge-computing-agbotdb-postgresql-auth-secret edge-computing-exchangedb-postgresql-auth-secret edge-computing-css-db-ibm-mongodb-auth-secret;
```

2. Exportieren Sie diese Werte auf Ihre lokale Maschine.

```bash
export BACKUP_DIR=/tmp/edge-computing-backup/<Insert desired backup datestamp YYYYMMDD_HHMMSS>
```

3. Führen Sie den folgenden Befehl aus, um Authentifizierungen und geheime Schlüssel wiederherzustellen:

```bash
oc apply -f $BACKUP_DIR
```

4. Installieren Sie IBM Edge Computing Manager erneut, bevor Sie weitere Schritte ausführen. Folgen Sie den Anweisungen im Abschnitt **Diagramm installieren**.

5. Führen Sie die folgenden Schritte aus, um Sicherungen in die Container zu kopieren und wiederherzustellen.

```bash
oc -n kube-system cp $BACKUP_DIR/exchange-backup.tar edge-computing-exchangedb-keeper-0:/stolon-data/exchange-backup.tar && \
oc exec -n kube-system edge-computing-exchangedb-keeper-0 -- bash -c "export PGPASSWORD=$(oc get secret edge-computing -o jsonpath="{.data.exchange-db-pass}" | base64 --decode) && pg_restore -U admin -h edge-computing-exchangedb-proxy-svc -d postgres -c /stolon-data/exchange-backup.tar"
```

```bash
oc -n kube-system cp $BACKUP_DIR/agbot-backup.tar edge-computing-agbotdb-keeper-0:/stolon-data/agbot-backup.tar && \
oc exec -n kube-system edge-computing-agbotdb-keeper-0 -- bash -c "export PGPASSWORD=$(oc get secret edge-computing -o jsonpath="{.data.agbot-db-pass}" | base64 --decode) && pg_restore -U admin -h edge-computing-agbotdb-proxy-svc -d postgres -c /stolon-data/agbot-backup.tar"
```

```bash
oc -n kube-system cp $BACKUP_DIR/css-backup edge-computing-cssdb-server-0:/data/db/css-backup && \
oc exec -n kube-system edge-computing-cssdb-server-0 -- bash -c "mongorestore -u admin -p $(oc get secret edge-computing -o jsonpath="{.data.css-db-pass}" | base64 --decode) /data/db/css-backup";
```

6. Führen Sie die folgenden Schritte aus, um die Datenbankverbindungen des Kubernetes-Pods zu aktualisieren.
```bash
for POD in $(oc get pods -n kube-system | grep -E '\-agbot\-|\-css\-|\-exchange\-' | awk '{print $1}'); do oc delete pod $POD -n kube-system; done
```

## Einschränkungen

* Einschränkungen der Installation: Dieses Produkt kann nur einmal und nur in den Namensbereich `kube-system` installiert werden.
* In diesem Release gibt es keine spezifischen Autorisierungsberechtigungen für die Verwaltung und das Betreiben des Produkts.

## Dokumentation

* Im Dokument [Installation](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.1/devices/installing/install.html) des Knowledge Center finden Sie weitere Anleitungen und Aktualisierungen.

## Copyright

© Copyright IBM Corporation 2020. Alle Rechte vorbehalten.
