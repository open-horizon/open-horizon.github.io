---

copyright:
years: 2020
lastupdated: "2020-4-24"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Edge-Cluster vorbereiten
{: #preparing_edge_cluster}

## Vorbereitende Schritte

Lesen Sie vor der Arbeit mit Edge-Clustern die Informationen in den folgenden Abschnitten:

* [Voraussetzungen](#preparing_clusters)
* [Erforderliche Informationen und Dateien für Edge-Cluster zusammenstellen](#gather_info)

## Voraussetzungen
{: #preparing_clusters}

Führen Sie vor der Installation eines Agenten in einem Edge-Cluster Folgendes aus:

1. Installieren Sie 'kubectl' in der Umgebung, in der das Agenteninstallationsscript ausgeführt wird.
2. Installieren Sie die {{site.data.keyword.open_shift}}-Client-CLI (oc) in der Umgebung, in der das Agenteninstallationsscript ausgeführt wird.
3. Fordern Sie den Zugriff eines Clusteradministrators an; dieser Zugriff ist für die Erstellung der relevanten Clusterressourcen erforderlich.
4. Stellen Sie eine Edge-Cluster-Registry als Host für das Docker-Image des Agenten zur Verfügung.
5. Installieren Sie die Befehle **cloudctl** und **kubectl** und extrahieren Sie **ibm-edge-computing-4.1-x86_64.tar.gz**. Weitere Informationen enthält der Abschnitt  [Installationsprozess](../installing/install.md#process).

## Erforderliche Informationen und Dateien für Edge-Cluster zusammenstellen
{: #gather_info}

Um Ihre Edge-Cluster zu installieren und bei {{site.data.keyword.edge_notm}} zu registrieren, benötigen Sie verschiedene Dateien. In diesem Abschnitt erfahren Sie, wie Sie diese Dateien in einer TAR-Datei zusammenstellen, die Sie anschließend auf jedem einzelnen Edge-Cluster verwenden können.

1. Legen Sie die Umgebungsvariablen für **CLUSTER_URL** fest:

    ```
    export CLUSTER_URL=<cluster-url>
    export USER=<your-icp-admin-user>
    export PW=<your-icp-admin-password>
    ```
    {: codeblock}

    Alternativ können Sie nach dem Verbinden Ihres Clusters mit **oc login** Folgendes ausführen:

    ```
    export CLUSTER_URL=https://$(oc get routes icp-console -o jsonpath='{.spec.host}')
    ```
    {: codeblock}
    
2. Stellen Sie die Verbindung zu Ihrem Cluster unter Verwendung der Zugriffsrechte für den Clusteradministrator her. Wählen Sie anschließend den Namensbereich **kube-system** und setzen Sie das Kennwort ein, das Sie in der Datei 'config.yaml' während des [Installationsprozesses](../installing/install.md#process) für den {{site.data.keyword.mgmt_hub}} definiert haben:

    ```
    cloudctl login -a $CLUSTER_URL -u admin -p <icp-admin-kennwort> -n kube-system --skip-ssl-validation
    ```
    {: codeblock}    

3. Legen Sie den Benutzernamen, das Kennwort und den vollständigen Imagenamen für die Edge-Cluster-Registry in den Umgebungsvariablen fest. Der Wert von IMAGE_ON_EDGE_CLUSTER_REGISTRY wird im folgenden Format angegeben:

    ```
    <registry-name>/<repository-name>/<image-name>.
    ```
    {: codeblock} 

    Wenn Sie den Docker Hub als Registry verwenden, geben Sie den Wert im folgenden Format an:
    
    ```
    <docker-repository-name>/<image-name>
    ```
    {: codeblock}
    
    Beispiel:
    
    ```
    export EDGE_CLUSTER_REGISTRY_USER=<your-edge-cluster-registry-username>
    export EDGE_CLUSTER_REGISTRY_PW=<your-edge-cluster-registry-password>
    export IMAGE_ON_EDGE_CLUSTER_REGISTRY=<full-image-name-on-your-edge-cluster registry>
    ```
    {: codeblock}
    
4. Laden Sie die aktuelle Version von **edgeDeviceFiles.sh** herunter:

   ```
   curl -O https://raw.githubusercontent.com/open-horizon/examples/master/tools/edgeDeviceFiles.sh chmod +x edgeDeviceFiles.sh
   ```
   {: codeblock}

5. Führen Sie das Script **edgeDeviceFiles.sh** aus, um die erforderlichen Dateien zusammenzustellen:

   ```
   ./edgeDeviceFiles.sh x86_64-Cluster -t -r -o <hzn-org-id> -n <node-id> <other flags>
   ```
   {: codeblock}
    
   Hiermit wird eine Datei namens 'agentInstallFiles-x86_64-Cluster..tar.gz' erstellt. 
    
**Befehlsargumente**
   
Hinweis: Geben Sie 'x86_64-Cluster' an, um den Agenten in einem Edge-Cluster zu installieren.
   
|Befehlsargumente|Ergebnis|
|-----------------|------|
|t                |Erstellt eine Datei namens **agentInstallFiles-&lt;edge-einheitentyp&gt;.tar.gz**, die alle zusammengestellten Dateien enthält. Ist dieses Flag nicht gesetzt, werden die zusammengestellten Dateien im aktuellen Verzeichnis angeordnet.|
|f                |Gibt ein Verzeichnis an, in das die zusammengestellten Dateien verschoben werden sollen. Ist das Verzeichnis noch nicht vorhanden, wird es erstellt. Standardwert ist das aktuelle Verzeichnis.|
|r                |**EDGE_CLUSTER_REGISTRY_USER**, **EDGE_CLUSTER_REGISTRY_PW** und **IMAGE_ON_EDGE_CLUSTER_REGISTRY** müssen bei Verwendung dieses Flags in der Umgebungsvariablen festgelegt werden (Schritt 1). In Version 4.1 ist dieses Flag erforderlich.|
|o                |Geben Sie **HZN_ORG_ID** an. Dieser Wert wird für die Registrierung des Edge-Clusters verwendet.|
|n                |Geben Sie **NODE_ID** an; der Wert sollte der Name Ihres Edge-Clusters sein. Dieser Wert wird für die Registrierung des Edge-Clusters verwendet.|
|s                |Gibt die Clusterspeicherklasse an, die von der Anforderung eines persistenten Datenträgers verwendet werden soll. Die Standardspeicherklasse ist 'gp2'.|
|i                |Gibt die Version des Agentenimage an, das im Edge-Cluster bereitgestellt werden soll.|


Wenn Sie die Installation des Agenten im Edge-Cluster vollständig vorbereitet haben, fahren Sie mit dem Abschnitt [Agenten installieren und Edge-Cluster registrieren](importing_clusters.md) fort.

<!--DELETE DOWN TO    
   The following flags are only supported for x86_64-Cluster:

    * **-r**: specify edge cluster registry if edge cluster is not using Openshift image registry. "EDGE_CLUSTER_REGISTRY_USER", "EDGE_CLUSTER_REGISTRY_PW" and "EDGE_CLUSTER_REGISTRY_REPONAME" need to be set in environment variable (step 1) if using this flag.
    * **-s**: specify cluster storage class to be used by persistent volume claim. Default storage class is "gp2".
    * **-i**: agent image version to be deployed on edge cluster
    * **-o**: specify HZN_ORG_ID. This value is used for edge cluster registration.
    * **-n**: specify NODE_ID. NODE_ID should be the value of your edge cluster name. This value is used for edge cluster registration. 

4. The command in the previous step creates a file that is called **agentInstallFiles-&lt;edge-device-type&gt;.tar.gz**. If you have other types of edge devices (different architectures), repeat the previous step for each type.

5. Take note of the API key that was created and displayed by the **edgeDeviceFiles.sh** command.

6. Now that you are logged in via **cloudctl**, if you need to create additional API keys for users to use with the {{site.data.keyword.horizon}} **hzn** command:

   ```
   cloudctl iam api-key-create "<choose-an-api-key-name>" -d "<choose-an-api-key-description>"
   ```
   {: codeblock}

   In the output of the command look for the key value in the line that starts with **API Key** and save the key value for future use.

7. When you are ready to set up edge devices, follow [Getting started using {{site.data.keyword.edge_devices_notm}}](../getting_started/getting_started.md).

Lily - is the pointer in step 7 above still correct?-->

## Weitere Schritte

* [Agenten installieren und Edge-Cluster registrieren](importing_clusters.md)

## Zugehörige Informationen

* [Edge-Cluster](edge_clusters.md)
* [Erste Schritte bei der Verwendung von {{site.data.keyword.edge_notm}}](../getting_started/getting_started.md)
* [Installationsprozess](../installing/install.md#process)
