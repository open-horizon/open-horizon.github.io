---

copyright:
  years: 2020
lastupdated: "2020-04-9"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Agenten installieren und Edge-Cluster registrieren
{: #importing_clusters}

Sie können Agenten in den folgenden Edge-Clustern installieren:

* Kubernetes-Cluster
* Schlanke Kubernetes-Cluster (wird für Tests empfohlen)

## Agenten in Kubernetes-Edge-Clustern installieren
{: #install_kube}

Es besteht die Möglichkeit, den Agenten durch die Ausführung des Scripts `agent-install.sh` automatisch zu installieren. 

Führen Sie die folgenden Schritte in der Umgebung aus, in der das Agenteninstallationsscript ausgeführt wird:

1. Rufen Sie die Datei `agentInstallFiles-x86_64-Cluster.tar.gz` ab und besorgen Sie sich bei Ihrem Administrator einen API-Schlüssel. Diese sollten bereits mit den Schritten im Abschnitt [Erforderliche Informationen und Dateien für Edge-Cluster zusammenstellen](preparing_edge_cluster.md) erstellt worden sein.

2. Legen Sie den Dateinamen für nachfolgende Schritte in einer Umgebungsvariablen fest:

   ```
   export AGENT_TAR_FILE=agentInstallFiles-x86_64-Cluster.tar.gz
   ```
   {: codeblock}

3. Extrahieren Sie die Dateien aus der TAR-Datei:

   ```
   tar -zxvf agentInstallFiles-x86_64-Cluster.tar.gz
   ```
   {: codeblock}

4. Exportieren Sie Ihre Berechtigungsnachweise für Horizon Exchange mit einem der folgenden Formate:

   ```
  export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-schlüssel>
  ```
   {: codeblock}

   Alternativ:

   ```
   export HZN_EXCHANGE_USER_AUTH=<benutzername>/<benutzername>:<kennwort>
   ```
   {: codeblock}

5. Führen Sie den Befehl `agent-install.sh` aus, um den Horizon-Agenten zu installieren und zu konfigurieren und um den Edge-Cluster für die Ausführung des Beispiel-Edge-Service 'helloworld' zu registrieren:

   ```
   ./agent-install.sh -u $HZN_EXCHANGE_USER_AUTH -k agent-install.cfg  -D cluster -p
   ```
   {: codeblock}

   Hinweis: Während der Installation des Agenten wird möglicherweise die folgende Eingabeaufforderung angezeigt: **Do you want to overwrite horizon?[y/N]: ** Wählen Sie **y** aus und drücken Sie die **Eingabetaste**. Das Script `agent-install.sh` legt die Konfiguration korrekt fest.

6. (Optional) Führen Sie Folgendes aus, um Beschreibungen der verfügbaren Flags für das Script `agent-install.sh` anzuzeigen: 

   ```
  ./agent-install.sh -h
  ```
   {: codeblock}

7. Rufen Sie eine Liste der in Kubernetes ausgeführten Agentenressourcen ab. Nachdem der Agent jetzt in Ihrem Edge-Cluster installiert ist und Ihr Edge-Cluster registriert wurde, können Sie die folgenden Edge-Clusterressourcen auflisten:

   * Namensbereich:

   ```
   kubectl get namespace openhorizon-agent
   ```
   {: codeblock}

   * Bereitstellung:

   ```
   kubectl get deployment -n openhorizon-agent
   ```
   {: codeblock}

   So listen Sie Details der Agentenbereitstellung auf:

   ```
   kubectl get deployment -n openhorizon-agent -o yaml
   ```
   {: codeblock}

   * Konfigurationszuordnung (Configmap):

   ```
   kubectl get configmap openhorizon-agent-config -n openhorizon-agent -o yaml
   ```
   {: codeblock}

   * Geheimer Schlüssel:
   
   ```
   kubectl get secret openhorizon-agent-secrets -n openhorizon-agent -o yaml
   ```
   {: codeblock}

   * Anforderung eines persistenten Datenträgers:
   
   ```
   kubectl get pvc openhorizon-agent-pvc -n openhorizon-agent -o yaml
   ```
   {: codeblock}

   * Pod:

   ```
   kubectl get pod -n openhorizon-agent
   ```
   {: codeblock}

8. Zeigen Sie die Protokolle an, rufen Sie die Pod-ID ab und führen Sie dann Folgendes aus: 

   ```
   kubectl logs <pod-id> -n openhorizon-agent
   ```
   {: codeblock}

9. Führen Sie den Befehl `hzn` im Agentencontainer aus:

   ```
   kubectl exec -it <pod-id> -n openhorizon-agent /bin/bash
   hzn --help
   ```
   {: codeblock}

10. Untersuchen Sie die Flags und den Unterbefehl für den Befehl `hzn`:

   ```
  hzn --help
  ```
   {: codeblock}

## Agenten in schlanken Kubernetes-Edge-Clustern installieren

Nachfolgend ist die Installation eines Agenten in microk8s beschrieben, einem schlanken Kubernetes-Cluster, den Sie lokal installieren und konfigurieren können. Unter anderem erhalten Sie Informationen zu den folgenden Aktionen:

* microk8s installieren und konfigurieren
* Agenten in microk8s installieren

### microk8s installieren und konfigurieren

1. So installieren Sie microk8s:

   ```
   sudo snap install microk8s --classic --channel=1.14/stable
   ```
   {: codeblock}

2. Legen Sie einen Aliasnamen für 'microk8s.kubectl' fest:

   Hinweis: Stellen Sie sicher, dass der Befehl `kubectl` nicht verfügbar ist, wenn Sie einen Test in microk8s durchführen wollen. 

  * microK8s verwendet einen Befehl 'kubectl' mit Namensbereich, um Konflikte mit bestehenden Installationen von kubectl zu verhindern. Falls keine Installation vorhanden ist, ist es einfacher, einen Aliasnamen hinzuzufügen (`append to ~/.bash_aliases`): 
   
   ```
   alias kubectl='microk8s.kubectl' 
   ```
   {: codeblock}
  
   * Anschließend gehen Sie wie folgt vor:

   ```
   source ~/.bash_aliases
   ```
   {: codeblock}

3. Aktivieren Sie DNS und das Speichermodul in microk8s:

   ```
   microk8s.enable dns storage
   ```
   {: codeblock}

4. Erstellen Sie die Speicherklasse in microk8s. Das Agenteninstallationsscript verwendet `gp2` als Standardspeicherklasse für Anforderungen eines persistenten Datenträgers. Diese Speicherklasse muss vor der Installation des Agenten in der microk8s-Umgebung erstellt worden sein. Falls der Edge-Clusteragent eine andere Speicherklasse verwendet, muss diese ebenfalls vorher erstellt worden sein. 

   Das folgende Beispiel zeigt die Erstellung von `gp2` als Speicherklasse:  

   1. Erstellen Sie eine Datei 'storageClass.yml': 

      ```
      apiVersion: storage.k8s.io/v1
      kind: StorageClass
      metadata:
       name: gp2
      provisioner: microk8s.io/hostpath
      reclaimPolicy: Delete
      volumeBindingMode: Immediate
      ```
      {: codeblock}

   2. Erstellen Sie mit dem Befehl `kubectl` das Objekt 'storageClass' in microk8s:

      ```
      kubectl apply -f storageClass.yml
      ```
      {: codeblock}

### Agenten in microk8s installieren

Führen Sie die folgenden Schritte aus, um einen Agenten in microk8s zu installieren.

1. Führen Sie die [Schritte 1 - 3](#install_kube) aus.

2. Führen Sie den Befehl `agent-install.sh` aus, um den Horizon-Agenten zu installieren und zu konfigurieren und um den Edge-Cluster für die Ausführung des Beispiel-Edge-Service 'helloworld' zu registrieren:

   ```
   source agent-install.sh -u $HZN_EXCHANGE_USER_AUTH -k agent-install.cfg  -D cluster -p "IBM/pattern-ibm.helloworld"
   ```
   {: codeblock}

   Hinweis: Während der Installation des Agenten wird möglicherweise die folgende Eingabeaufforderung angezeigt: **Do you want to overwrite horizon?[y/N]: ** Wählen Sie **y** aus und drücken Sie die  **Eingabetaste**. Das Script `agent-install.sh` legt die Konfiguration korrekt fest.

## Agenten aus dem schlanken Kubernetes-Cluster entfernen 

Hinweis: Da das Agentendeinstallationsscript im aktuellen Release noch nicht vollständig ist, wird zum Entfernen des Agenten der Namensbereich 'openhorizon-agent' gelöscht.

1. Löschen Sie den Namensbereich:

   ```
   kubectl delete namespace openhorizon-agent
   ```
   {: codeblock}

      Hinweis: Das Löschen des Namensbereichs wird gelegentlich im Status 'Terminating' (= wird beendet) blockiert. In einer solchen Situation können Sie unter [Namensbereich verbleibt im Status 'Terminating'![Wird auf einer neuen Registerkarte geöffnet](../../images/icons/launch-glyph.svg "Wird auf einer neuen Registerkarte geöffnet")](https://www.ibm.com/support/knowledgecenter/SSBS6K_3.1.1/troubleshoot/ns_terminating.html) nachlesen, wie Sie den Namensbereich manuell löschen.

2. Löschen Sie die Clusterrollenbindung: 

   ```
   kubectl delete clusterrolebinding openhorizon-agent-cluster-rule
   ```
   {: codeblock}

<!--If this installation was done as part of a prerequisite for {{site.data.keyword.edge_devices_notm}}, [return to continue that installation](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.0/devices/installing/install.html).-->
