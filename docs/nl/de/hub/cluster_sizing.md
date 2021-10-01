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


# Dimensionierung und Systemvoraussetzungen
{: #size}

## Hinweise zur Dimensionierung

Die passende Dimensionierung Ihres Clusters beinhaltet verschiedene Aspekte. Einige dieser Aspekte werden im Folgenden erläutert, um Ihnen die Entscheidung für die geeignete Dimensionierung Ihres Clusters nach Möglichkeit zu erleichtern.

Im Vordergrund steht die Frage nach den Services, die in Ihrem Cluster ausgeführt werden sollen. Folgenden finden Sie lediglich Dimensionierungsrichtlinien für die folgenden Services:

* {{site.data.keyword.common_services}}
* {{site.data.keyword.edge_notm}}-Management-Hub ({{site.data.keyword.ieam}}-Management-Hub)

Optional können Sie die [{{site.data.keyword.open_shift_cp}}-Clusterprotokollierung](../admin/accessing_logs.md#ocp_logging) installieren.

## Hinweise zur {{site.data.keyword.ieam}}-Datenbank

Für Datenbanken stehen zwei unterstützte Konfigurationen zur Auswahl, die sich auf die Dimensionierung des {{site.data.keyword.ieam}}-Management-Hubs auswirken:

* **Lokale** Datenbanken werden (standardmäßig) als {{site.data.keyword.open_shift}}-Ressourcen im {{site.data.keyword.open_shift}}-Cluster installiert.
* **Ferne** Datenbanken sind die Ihnen bereitgestellten Datenbanken. Bei diesen Datenbanken kann es sich z. B. um On-Premises-Datenbanken oder SaaS-Angebote eines Cloud-Providers handeln.

### {{site.data.keyword.ieam}} Anforderungen für den lokalen Speicher

Zusätzlich zur stets installierten Komponente "Secure Device Onboarding" (SDO) erfordern die **lokalen** Datenbanken und der Secrets Manager einen persistenten Speicher. Dieser Speicher verwendet dynamische Speicherklassen, die für Ihren {{site.data.keyword.open_shift}} -Cluster konfiguriert sind.

Weitere Informationen finden Sie unter [unterstützte dynamische {{site.data.keyword.open_shift}}-Speicheroptionen und Konfigurationsanweisungen](https://docs.openshift.com/container-platform/4.6/storage/understanding-persistent-storage.html).

Sie sind verantwortlich für die Aktivierung der Verschlüsselung, die sich zum Zeitpunkt der Clustererstellung im Ruhezustand befindet. Sie kann häufig als Teil der Clustererstellung auf Cloud-Plattformen installiert werden. Weitere Informationen finden Sie in der [folgenden Dokumentation](https://docs.openshift.com/container-platform/4.6/installing/installing-fips.html).

Bei der Entscheidung für einen Speicherklassentyp ist die Frage, ob die Speicherklasse eine Datenträgererweiterung (Feld **allowVolumeExpansion**) unterstützt, von zentraler Bedeutung. Wird die Datenträgererweiterung unterstützt, wird für den folgenden Befehl **true** zurückgegeben:

```
oc get storageclass <gewünschte_speicherklasse> -o json | jq .allowVolumeExpansion
```
{: codeblock}

Wenn die Speicherklasse eine Datenträgererweiterung zulässt, kann die Dimensionierung nach der Installation angepasst werden (vorausgesetzt, der zugrunde liegende Speicherplatz reicht für die Zuordnung aus). Wenn die Speicherklasse keine Datenträgererweiterung zulässt, müssen Sie den für Ihren Anwendungsfall erforderlichen Speicher vorab zuordnen. 

Wenn nach der Erstinstallation mit einer Speicherklasse, die keine Datenträgererweiterung zulässt, weiterer Speicher benötigt wird, müssen Sie eine Neuinstallation durchführen. Führen Sie dazu die auf der Seite [Sicherung und Wiederherstellung](../admin/backup_recovery.md) beschriebenen Schritte aus.

Die Speicherzuordnungen können vor der Installation des {{site.data.keyword.ieam}}-Management-Hubs geändert werden, indem Sie Werte für den **Speicher** wie auf der Seite [Konfiguration](configuration.md) beschrieben ändern. Für die Zuordnungen gelten die folgenden Standardwerte:

* PostgreSQL Exchange (Speichert Daten für Exchange und weist einen je nach Nutzung schwankenden Speicherbedarf auf. Die Standardspeichereinstellung ist jedoch für eine Unterstützung der beworbenen maximalen Anzahl von Edge-Knoten ausgelegt.)
  * 20 GB
* PostgreSQL AgBot (Speichert Daten für den Agbot. Die Standardspeichereinstellung ist für eine Unterstützung der beworbenen maximalen Anzahl von Edge-Knoten ausgelegt.)
  * 20 GB
* MongoDB Cloud Sync Service (Speichert Inhalte für den Model Management-Service (MMS)). Abhängig von der Anzahl und Größe Ihrer Modelle können Sie diese Standardzuordnung ändern.
  * 50 GB
* Persistenter Datenträger mit Hashicorp-Vault (speichert die von den Edge-Einheitenservices verwendeten geheimen Schlüssel)
  * 10 GB (Diese Datenträgergröße ist nicht konfigurierbar)
* Persistenter Datenträger für Secure Device Onboarding (speichert Voucher für das Einheiteneigentum, Einheitenkonfigurationsoptionen und den Bereitstellungsstatus jeder Einheit)
  * 1 GB (diese Datenträgergröße ist nicht konfigurierbar)

* **Hinweise:**
  * {{site.data.keyword.ieam}}-Datenträger werden mit dem Zugriffsmodus **ReadWriteOnce** erstellt.
  * IBM Cloud Platform Common Services verfügt über zusätzliche Speicheranforderungen für ihre Services. Die folgenden Datenträger werden im Namensbereich **ibm-common-services** bei der Installation mit {{site.data.keyword.ieam}}-Standardwerten erstellt:
    ```
    NAME                                                                                     STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE     alertmanager-ibm-monitoring-alertmanager-db-alertmanager-ibm-monitoring-alertmanager-0   Bound    pvc-3979805f-8e3b-44d6-a039-cd438a3dbb25   10Gi       RWO            csi-cephfs     20h     mongodbdir-icp-mongodb-0                                                                 Bound    pvc-e21604a7-14e4-4049-824e-a5a9feb472c8   20Gi       RWO            csi-cephfs     20h     mongodbdir-icp-mongodb-1                                                                 Bound    pvc-eaecfa29-5c6a-45c2-9d26-58a393103791   20Gi       RWO            csi-cephfs     20h     mongodbdir-icp-mongodb-2                                                                 Bound    pvc-42282c2b-bde8-4adf-86ad-006d2f07df91   20Gi       RWO            csi-cephfs     19h     prometheus-ibm-monitoring-prometheus-db-prometheus-ibm-monitoring-prometheus-0           Bound    pvc-90237949-6f13-481b-8afa-7d86883b8a4f   10Gi       RWO            csi-cephfs     20h
    ```

    Weitere Informationen zum Speicherbedarf und zu den Konfigurationsoptionen von IBM Cloud Platform Common Services erhalten Sie [hier](https://www.ibm.com/support/knowledgecenter/SSHKN6/installer/3.x.x/custom_resource.html).

### Hinweise zu fernen {{site.data.keyword.ieam}}-Datenbanken

Die Nutzung eigener **ferner** Datenbanken reduziert den Bedarf an Speicherklassen- und Rechenressourcen für diese Installation, sofern die fernen Datenbanken nicht in demselben Cluster bereitgestellt werden.

Für **ferne** Datenbanken sollten mindestens die folgenden Ressourcen und Einstellungen bereitgestellt werden:

* 2 vCPUs
* 2 GB RAM
* Die im vorherigen Abschnitt genannten Standardspeichergrößen
* Für die PostgreSQL-Datenbanken 100 als Wert für **max_connections** (dies ist normalerweise der Standardwert)

## Dimensionierung von Workerknoten

Die Services, die [Kubernetes-Rechenressourcen](https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container) nutzen, werden über die verfügbaren Workerknoten aufgeteilt.

### Mindestvoraussetzungen für die Standardkonfiguration {{site.data.keyword.ieam}}
| Anzahl der Workerknoten | vCPUs pro Workerknoten | Hauptspeicher pro Workerknoten (GB) | Lokaler Plattenspeicher pro Workerknoten (GB) |
| :---: | :---: | :---: | :---: |
| 3	| 8	| 32	| 100 	|

**Hinweis:** Einige Kundenumgebungen erfordern möglicherweise zusätzliche vCPUs pro Workerknoten oder zusätzliche Workerknoten, so dass mehr CPU-Kapazität für die Exchange-Komponente zugeordnet werden kann.


&nbsp;
&nbsp;

Wenn Sie die entsprechende Dimensionierung für Ihren Cluster festgelegt haben, können Sie mit der [Installation](online_installation.md) beginnen.
