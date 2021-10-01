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

# Installation von {{site.data.keyword.ieam}}
{: #hub_install_overview}

Bevor Sie die Knotentasks von {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) ausführen können, müssen Sie zunächst einen Management-Hub installieren und konfigurieren.

## Installationszusammenfassung
{: #sum}

* In diesem Inhalt werden die Schritte zur Bereitstellung der folgenden Komponenten beschrieben.
  * [IBM Cloud Platform Common Services 3.6.x](https://www.ibm.com/docs/en/cpfs).
  * Operator für den Management-Hub von {{site.data.keyword.edge_notm}}
  * Exchange-API für {{site.data.keyword.edge_notm}}
  * Agbot für {{site.data.keyword.edge_notm}}
  * Cloud Sync Service (CSS) für {{site.data.keyword.edge_notm}}
  * Benutzerschnittstelle von {{site.data.keyword.edge_notm}}
  * {{site.data.keyword.edge_notm}} Secure Device Onboarding (SDO)
  * {{site.data.keyword.edge_notm}} Secrets Manager (Vault).

**Hinweis**: Weitere Informationen finden Sie in der [Upgradedokumentation](upgrade.md) , wenn Sie versuchen, ein Upgrade von einer früheren Version durchzuführen.

## Voraussetzungen
{: #prereq}

### {{site.data.keyword.ocp_tm}}
Stellen Sie sicher, dass Sie über eine [entsprechend dimensionierte](cluster_sizing.md) und unterstützte {{site.data.keyword.open_shift_cp}} 4.6-Installation verfügen, einschließlich einer geeigneten Speicherklasse, die in Ihrem Cluster installiert ist und funktioniert.

Weitere Informationen zur Bereitstellung eines verwalteten IBM Cloud-Clusters {{site.data.keyword.open_shift_cp}} 4.6 finden Sie in den folgenden Abschnitten:

* [{{site.data.keyword.ocp_tm}} auf {{site.data.keyword.cloud}}](https://www.ibm.com/cloud/openshift)

Weitere Informationen zum Erstellen eines eigenen verwalteten {{site.data.keyword.open_shift_cp}} Clusters finden Sie in der {{site.data.keyword.open_shift}} Dokumentation:

* [{{site.data.keyword.open_shift_cp}} 4.6-Dokumentation](https://docs.openshift.com/container-platform/4.6/welcome/index.html)

**Hinweis**: Standardmäßig werden ein lokaler Entwicklungs-Secrets Manager und Entwicklungsdatenbanken als Teil der Implementierung des Operators bereitgestellt. Weitere Informationen zum Herstellen einer Verbindung zu Ihren eigenen bereitgestellten Datenbanken und zu anderen Konfigurationsoptionen finden Sie unter [Konfiguration](configuration.md).

Sie sind für die Sicherung und Wiederherstellung aller persistenten Daten verantwortlich, siehe [Sicherung und Wiederherstellung](../admin/backup_recovery.md).

## Installationsprozess im Browser
{: #process}

1. Melden Sie sich über die Webbenutzerschnittstelle von {{site.data.keyword.open_shift_cp}} mit Clusteradministratorberechtigungen an. Navigieren Sie zur Seite **Speicher** und vergewissern Sie sich, dass Sie eine unterstützte Standardspeicherklasse (**Default**) definiert haben:

   <img src="../images/edge/hub_install_storage_class.png" style="margin: 3%" alt="Standardspeicherklasse" width="75%" height="75%" align="center">

   **Hinweis:** Weitere Informationen zur Verwendung einer nicht dem Standard entsprechenden Speicherklasse finden Sie auf der Seite [Konfiguration](configuration.md).

2. Erstellen Sie die Quelle für den IBM Operatorkatalog (IBM Operator Catalog Source); sie stellt die Möglichkeit zur Verfügung, das Bundle für den **IEAM-Management-Hub** zu installieren. Kopieren Sie den folgenden Text und fügen Sie ihn wie in der folgenden Abbildung gezeigt nach Auswahl des Pluszeichens für den Import ein. Klicken Sie nach dem Einfügen des Textes auf **Erstellen**:

   ```
   apiVersion: operators.coreos.com/v1alpha1    kind: CatalogSource    metadata:      name: ibm-operator-catalog      namespace: openshift-marketplace    spec:      displayName: IBM Operator Catalog      publisher: IBM      sourceType: grpc      image: icr.io/cpopen/ibm-operator-catalog:latest      updateStrategy:        registryPoll:          interval: 45m
   ```
   {: codeblock}

   <img src="../images/edge/hub_install_ibm_catalog.png" style="margin: 3%" alt="Quelle für IBM Katalog erstellen" align="center">

3. Erstellen Sie die Quelle für den Operatorkatalog von IBM Common Services. Dies stellt die Suite der Common Service-Operatoren bereit, die vom **IEAM-Management-Hub** zusätzlich installiert werden. Kopieren Sie den folgenden Text und fügen Sie ihn wie in der folgenden Abbildung gezeigt nach Auswahl des Pluszeichens für den Import ein. Klicken Sie nach dem Einfügen des Textes auf **Erstellen**:
   ```
   apiVersion: operators.coreos.com/v1alpha1    kind: CatalogSource    metadata:      name: opencloud-operators      namespace: openshift-marketplace    spec:      displayName: IBMCS Operators      publisher: IBM      sourceType: grpc      image: quay.io/opencloudio/ibm-common-service-catalog:3.6      updateStrategy:        registryPoll:          interval: 45m
   ```
   {: codeblock}

   <img src="../images/edge/hub_install_cs_catalog.png" style="margin: 3%" alt="Quelle für IBM CS-Katalog erstellen">

4. Navigieren Sie zur Seite für **Projekte** und erstellen Sie ein Projekt, in dem Sie den Operator installieren wollen:

   <img src="../images/edge/hub_install_create_project.png" style="margin: 3%" alt="Projekt erstellen">

5. Definieren Sie für die Image-Pull-Operation einen geheimen Schlüssel namens **ibm-entitlement-key** zur Authentifizierung bei der IBM Entitled Registry:

   **Hinweise:**
   * Rufen Sie Ihren Berechtigungsschlüssel bei [My IBM Key](https://myibm.ibm.com/products-services/containerlibrary) ab und füllen Sie die Felder wie nachfolgend gezeigt aus.
   * Achten Sie darauf, diese Ressource in demjenigen Projekt zu erstellen, das Sie im vorherigen Schritt erstellt haben.

   <img src="../images/edge/hub_install_pull_secret.png" style="margin: 3%" alt="Geheimen Schlüssel für Image-Pull-Operation erstellen">

6. Navigieren Sie zu der Seite **OperatorHub** und suchen Sie nach **IEAM Management Hub**.

7. Klicken Sie auf die Karte **IEAM Management Hub** und anschließend auf **Installieren**.

8. Installieren Sie den Operator, und stellen Sie sicher, dass das Projekt mit dem in Schritt 4 erstellten Projekt übereinstimmt.

   **Hinweis**: Dies ist das einzige Projekt, das der Operator **IEAM Management Hub** nach der Installation überwacht.

   <img src="../images/edge/hub_install_operator.png" style="margin: 3%" alt="IEAM-Operator installieren">

9. Ändern Sie den Wert für **Projekt** wieder in das in Schritt 4 erstellte Projekt, klicken Sie in der Spalte **Bereitgestellte APIs** (siehe Schritt 7) auf **EamHub** und klicken Sie dann auf **EamHub erstellen**:

   <img src="../images/edge/hub_install_create_eamhub.png" style="margin: 3%" alt="Angepasste Ressource 'EamHub'" width="75%" height="75%">

10. Erstellen Sie die angepasste **EamHub** -Ressource, die Ihr Management-Hub definiert und konfiguriert. Weitere Informationen zu Anpassungsoptionen finden Sie unter [Konfiguration](configuration.md). Stellen Sie sicher, dass das Projekt dem entspricht, was Sie in Schritt 4 erstellt haben.

   * Klicken Sie auf das Umschaltelement für **Lizenz akzeptieren** und dann auf **Erstellen**, um die Lizenz zu akzeptieren.

   <img src="../images/edge/hub_install_create_cr_45.png" style="margin: 3%" alt="Angepasste Ressource 'EamHub' bei 4.5 erstellen" width="75%" height="75%">

Der Operator stellt die definierten Workloads aus dem Projekt bereit, das in Schritt 4 angegeben wurde. Außerdem werden die erforderlichen {{site.data.keyword.common_services}}-Workloads aus dem Projekt **ibm-common-services** bereitgestellt.

## Weitere Schritte

Setzen Sie die Einrichtung Ihres neuen Management-Hubs mit den Schritten im Abschnitt [Installationsabschluss](post_install.md) fort.
