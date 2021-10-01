---

copyright:
years: 2020
lastupdated: "2020-10-28"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Datensicherung und -wiederherstellung
{: #data_backup}

## Sicherung und Wiederherstellung von {{site.data.keyword.open_shift_cp}}

Weitere Informationen zur clusterweiten Datensicherung und -wiederherstellung finden Sie in folgenden Abschnitten:

* [{{site.data.keyword.open_shift_cp}} 4.6-Sicherung etcd](https://docs.openshift.com/container-platform/4.6/backup_and_restore/backing-up-etcd.html).

## Sicherung und Wiederherstellung von {{site.data.keyword.edge_notm}}

Die Sicherungsprozeduren für {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) variieren abhängig vom Typ der verwendeten Datenbanken geringfügig. Diese Datenbanken werden als lokale oder ferne Datenbanken bezeichnet.

|Datenbanktyp|Beschreibung|
|-------------|-----------|
|Lokal|Diese Datenbanken werden (standardmäßig) als {{site.data.keyword.open_shift}}-Ressourcen in Ihrem {{site.data.keyword.open_shift}}-Cluster installiert.|
|Fern|Diese Datenbanken werden außerhalb des Clusters bereitgestellt. Solche Datenbanken können beispielsweise vor Ort oder als SaaS-Angebot eines Cloud-Providers zur Verfügung stehen.|

Die Konfigurationseinstellung, die steuert, welche Datenbanken verwendet werden, wird bei der Installation in Ihrer angepassten Ressource mit **spec.ieam\_local\_databases** festgelegt; die Standardeinstellung lautet 'true'.

Um den aktiven Wert für eine installierte {{site.data.keyword.ieam}}-Instanz zu ermitteln, führen Sie Folgendes aus:

```
oc get eamhub ibm-edge -o jsonpath="{.spec.ieam_local_databases}"
```
{: codeblock}

Weitere Informationen zum Konfigurieren von fernen Datenbanken bei der Installation finden Sie auf der Seite [Konfiguration](../hub/configuration.md).

**Hinweis:** Ein Wechsel zwischen lokalen und fernen Datenbanken wird nicht unterstützt.

Ihre Daten werden von {{site.data.keyword.edge_notm}} nicht automatisch gesichert. Die Verantwortung für das Sichern von Inhalten in der gewünschten Häufigkeit und das Speichern dieser Sicherungen an einer separaten sicheren Position zur Gewährleistung der Wiederherstellbarkeit liegt bei Ihnen. Da Sicherungen geheimer Schlüssel codierten Authentifizierungsinhalt für  Datenbankverbindungen und die Anwendungsauthentifizierung des {{site.data.keyword.mgmt_hub}}s enthalten, müssen sie  an einer sicheren Position gespeichert werden.

Wenn Sie Ihre eigenen fernen Datenbanken verwenden, stellen Sie sicher, dass diese Datenbanken gesichert werden. In der vorliegenden Dokumentation ist nicht beschrieben, wie Sie die Daten dieser fernen Datenbanken sichern können.

Für die {{site.data.keyword.ieam}} Sicherungsprozedur ist auch `yq` v3 erforderlich.

### Sicherungsprozedur

1. Stellen Sie sicher, dass Sie mit dem Cluster über **cloudctl login** oder **oc login** als Clusteradministrator verbunden sind. Sichern Sie Ihre Daten und geheimen Schlüssel mithilfe des folgenden Scripts, das sich in den entpackten, von Passport Advantage heruntergeladenen Installationsmedien für die Installation des {{site.data.keyword.mgmt_hub}}s befindet. Führen Sie das Script mit dem Parameter **-h** aus, um die Syntax anzuzeigen:

   ```
   ibm-eam-{{site.data.keyword.semver}}-bundle/tools/ieam-backup.sh -h
   ```
   {: codeblock}
   
   **Hinweis:** Das Sicherungsscript erkennt automatisch den Typ der bei der Installation verwendeten Datenbanken.

   * Wenn Sie das folgende Beispiel ohne Optionen ausführen, generiert das Script einen Ordner an der Position, an der es ausgeführt wurde. Der Ordner folgt dem Namensmuster **ibm-edge-backup/$DATE/**:

     ```
     ibm-eam-{{site.data.keyword.semver}}-bundle/tools/ieam-backup.sh
     ```
     {: codeblock}
     
     Falls die Installation einer **lokalen Datenbank** festgestellt worden ist, enthält Ihre Sicherung ein Verzeichnis namens **customresource**, ein Verzeichnis namens **databaseresources** und zwei YAML-Dateien:

     ```
     $ ls -l ibm-edge-backup/20201026_215107/   	  drwxr-xr-x  3 staff  staff     96 Oct 26 21:51 customresource 	  drwxr-xr-x  5 staff  staff    160 Oct 26 21:51 databaseresources 	  -rw-r--r--  1 staff  staff  13308 Oct 26 21:51 ibm-edge-auth-secret.yaml 	  -rw-r--r--  1 staff  staff   3689 Oct 26 21:51 ibm-edge-config.yaml
     ```
     {: codeblock}
     
	  Falls die Installation einer **fernen Datenbank** festgestellt wurde, beinhaltet die Sicherung dieselben Verzeichnisse wie bei einer lokalen Datenbank, jedoch nicht zwei, sondern drei YAML-Dateien.
	  
	  ```
     $ ls -l ibm-edge-backup/20201026_215518/ 	  drwxr-xr-x  3 staff  staff     96 Oct 26 21:55 customresource 	  drwxr-xr-x  3 staff  staff     96 Oct 26 21:55 databaseresources 	  -rw-r--r--  1 staff  staff  10477 Oct 26 21:55 ibm-edge-auth-overrides.yaml 	  -rw-r--r--  1 staff  staff  11433 Oct 26 21:55 ibm-edge-auth-secret.yaml 	  -rw-r--r--  1 staff  staff   2499 Oct 26 21:55 ibm-edge-config.yaml
     ```
     {: codeblock}

### Wiederherstellungsprozedur

**Hinweis:** Wenn lokale Datenbanken verwendet oder in neuen oder leeren fernen Datenbanken wiederhergestellt werden, führt das autonome Design von {{site.data.keyword.ieam}} zu einem bekannten Problem, wenn Sicherungen auf dem {{site.data.keyword.mgmt_hub}} wiederhergestellt werden.

Damit Sicherungen wiederhergestellt werden können, muss ein identischer {{site.data.keyword.mgmt_hub}} installiert sein. Wenn dieser neue Hub während der Erstinstallation ohne Eingabe von **ieam \_maintenance\_mode** installiert wird, ist es wahrscheinlich, dass alle Randknoten, die zuvor registriert wurden, sich selbst aufheben. und erneut registriert werden müssen.

Diese Situation tritt auf, wenn ein Edge-Knoten angesichts der vermeintlich leeren Datenbank davon ausgeht, dass er nicht mehr im Exchange vorhanden ist. Aktivieren Sie zur Vermeidung dieses Problems die Option **ieam\_maintenance\_mode**, damit die Datenbankressourcen ausschließlich für den  {{site.data.keyword.mgmt_hub}} gestartet werden. Dadurch kann die Wiederherstellung vollständig abgeschlossen werden, bevor die übrigen  {{site.data.keyword.mgmt_hub}}-Ressourcen (die diese Datenbanken verwenden) gestartet werden.

**Hinweise:** 

* Beim Sichern der Datei für Ihre **angepasste Ressource** wurde sie automatisch so geändert, dass bei ihrer erneuten Anwendung auf den Cluster sofort **ieam\_maintenance\_mode** aktiviert wird.

* Die Wiederherstellungsscripts ermitteln automatisch, welcher Datenbanktyp zuvor verwendet wurde; hierzu wird die Datei **\<path/to/backup\>/customresource/eamhub-cr.yaml** untersucht.

1. Stellen Sie als Clusteradministrator sicher, dass Sie über **cloudctl login** oder **oc login** mit dem Cluster verbunden sind und dass eine gültige Sicherung erstellt wurde. Führen Sie auf dem Cluster, auf dem die Sicherung ausgeführt wurde, den folgenden Befehl aus, um die angepasste Ressource **eamhub** zu löschen (dabei wird davon ausgegangen, dass der Standardname **ibm-edge** für die angepasste Ressource verwendet wurde):
	```
	oc delete eamhub ibm-edge
	```
	{: codeblock}

2. Vergewissern Sie sich, dass die Einstellung **ieam\_maintenance\_mode** ordnungsgemäß festgelegt ist:
	```
	yq r ibm-edge-backup/20201026_215738/customresource/eamhub-cr.yaml 'items[0] .spec.ieam_maintenance_mode'
	```
	{: codeblock}
	

3. Führen Sie das Script `ieam-restore-k8s-resources.sh` mit der Option **-f** aus, die so definiert ist, dass sie auf Ihre Sicherung verweist:
	```
	ibm-eam-{{site.data.keyword.semver}}-bundle/tools/ieam-restore-k8s-resources.sh -f ibm-edge-backup/20201026_215738/
	```
	{: codeblock}

   Warten Sie, bis die gesamte Datenbank und die SDO-Pods ausgeführt werden, bevor Sie fortfahren.
	
4. Bearbeiten Sie die angepasste Ressource **ibm-edge**, um den Operator zu pausieren:
	```
	oc patch eamhub ibm-edge --type merge --patch '{"spec":{"pause_control_loop": true}}'
	```
	{: codeblock}

5. Bearbeiten Sie die statusabhängige Gruppe **ibm-edge-sdo**, um ein Scale-up für die Anzahl der Replikate auf **1** durchzuführen:
	```
	oc patch statefulset ibm-edge-sdo --type merge --patch '{"spec":{"replicas": 1}}'
	```
	{: codeblock}

6. Warten Sie, bis der Pod **ibm-edge-sdo-0** in einem aktiven Status ist:
	```
   	watch oc get pods -n ibm-edge | grep ibm-edge-sdo-0
   	```
	{: codeblock}

7. Führen Sie das Script `ieam-restore-data.sh` mit der Option **-f** aus, die so definiert ist, dass sie auf die Sicherung verweist:
	```
	ibm-eam-{{site.data.keyword.semver}}-bundle/tools/ieam-restore-data.sh -f ibm-edge-backup/20201026_215738/
	```
	{: codeblock}
	
8. Nachdem die Ausführung des Scripts abgeschlossen wurde und die Daten wiederhergestellt wurden, müssen Sie die Pausierung des Operators zurücknehmen, um die Steuerschleife fortzusetzen:
	```
	oc patch eamhub ibm-edge --type merge --patch '{"spec":{"pause_control_loop": false}}'
	```
	{: codeblock}

