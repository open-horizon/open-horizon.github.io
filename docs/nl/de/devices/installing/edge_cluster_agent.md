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

# Agent installieren
{: #importing_clusters}

Beginnen Sie mit der Installation des {{site.data.keyword.edge_notm}}-Agenten auf einem der folgenden Typen von Kubernetes-Edge-Clustern:

* [Agenten in {{site.data.keyword.ocp}}-Kubernetes-Edge-Cluster installieren](#install_kube)
* [Agenten in k3s- und microk8s-Edge-Clustern installieren](#install_lite)

Stellen Sie anschließend einen Edge-Service in Ihrem Edge-Cluster bereit:

* [Services im Edge-Cluster bereitstellen](#deploying_services)

Gehen Sie wie folgt vor, wenn der Agenten entfernt werden soll:

* [Agenten in Edge-Cluster entfernen](#remove_agent)

## Agenten in {{site.data.keyword.ocp}}-Kubernetes-Edge-Cluster installieren
{: #install_kube}

Im Folgenden wird die Installation des {{site.data.keyword.ieam}}-Agenten im {{site.data.keyword.ocp}}-Edge-Cluster beschrieben. Führen Sie die folgenden Schritte auf einem Host aus, der über Administratorzugriff auf Ihren Edge-Cluster verfügt:

1. Melden Sie sich bei Ihrem Edge-Cluster als **admin** an:

   ```bash
	oc login https://<API-ENDPUNKT-HOST>:<PORT> -u <ADMIN-BENUTZER> -p <ADMIN-KENNWORT> --insecure-skip-tls-verify=true
   ```
   {: codeblock}

2. Legen Sie für die Variable für den Namensbereich des Agenten den Standardwert (oder den Namensbereich, in dem der Agent explizit installiert werden soll) fest:

   ```bash
      export AGENT_NAMESPACE=openhorizon-agent
      ```
   {: codeblock}

3. Legen Sie als Speicherklasse für den Agenten eine integrierte Speicherklasse oder eine von Ihnen erstellte Speicherklasse fest. Beispiel:

   ```bash
   export EDGE_CLUSTER_STORAGE_CLASS=rook-ceph-cephfs-internal
   ```
   {: codeblock}

4. Führen Sie zum Einrichten der Image-Registry in Ihrem Edge-Cluster Schritt 2 bis 8 im Abschnitt [OpenShift-Image-Registry](../developing/container_registry.md##ocp_image_registry) mit folgender Änderung aus: Legen Sie in Schritt 4 für **OCP_PROJECT** den Wert **$AGENT_NAMESPACE** fest. 

5. Über das Script **agent-install.sh** wird der {{site.data.keyword.ieam}}-Agent in der Container-Registry des Edge-Clusters gespeichert. Legen Sie den Registry-Benutzer, das Kennwort und den vollständigen Imagepfad (ohne Tag) fest, der verwendet werden soll:

   ```bash
   export EDGE_CLUSTER_REGISTRY_USERNAME=$OCP_USER
   export EDGE_CLUSTER_REGISTRY_TOKEN="$OCP_TOKEN"
   export IMAGE_ON_EDGE_CLUSTER_REGISTRY=$OCP_DOCKER_HOST/$OCP_PROJECT/amd64_anax_k8s
   ```
   {: codeblock}

   **Hinweis:** Das {{site.data.keyword.ieam}}-Agentenimage wird in der lokalen Edge-Cluster-Registry gespeichert, da Kubernetes im Edge-Cluster fortlaufend Zugriff auf das Image benötigt, falls ein Neustart oder Versetzen in einen anderen Pod erforderlich ist.

6. Exportieren Sie Ihre Benutzerberechtigungsnachweise für Horizon Exchange:

   ```bash
  export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-schlüssel>
  ```
   {: codeblock}

7. Rufen Sie die Datei **agentInstallFiles-x86_64-Cluster.tar.gz** ab und besorgen Sie sich bei Ihrem Administrator einen API-Schlüssel. API-Schlüssel sollten bereits mit den im Abschnitt [Erforderliche Informationen und Dateien für Edge-Cluster zusammenstellen](preparing_edge_cluster.md) beschriebenen Schritten erstellt worden sein.

8. Extrahieren Sie das Script **agent-install.sh** aus der TAR-Datei:

   ```bash
   tar -zxvf agentInstallFiles-x86_64-Cluster.tar.gz agent-install.sh
   ```
   {: codeblock}

9. Führen Sie das Script **agent-install.sh** aus, um den Horizon-Agenten zu installieren und zu konfigurieren und den Edge-Cluster für Richtlinien zu registrieren:

   ```bash
   ./agent-install.sh -D cluster -z agentInstallFiles-x86_64-Cluster.tar.gz -d <knoten-id>
   ```
   {: codeblock}

   **Hinweise:**
   * Führen Sie das folgende Script aus, um alle verfügbaren Flags anzuzeigen: **./agent-install.sh -h**
   * Wenn ein Fehler auftritt, der dazu führt, dass **agent-install.sh** nicht ausgeführt werden kann, führen Sie zunächst **agent-uninstall.sh** aus (siehe [Agenten in Edge-Cluster entfernen](#remove_agent)) und wiederholen Sie dann die in diesem Abschnitt angegebenen Schritte.

10. Wechseln Sie zum Namensbereich bzw. Projekt des Agenten und vergewissern Sie sich, dass der Agentenpod ausgeführt wird:

   ```bash
   oc project $AGENT_NAMESPACE
   oc get pods
   ```
   {: codeblock}

11. Nach der Installation des Agenten in Ihrem Edge-Cluster können Sie nun die folgenden Befehle ausführen, wenn Sie sich mit den zum Agenten gehörigen Kubernetes-Ressourcen vertraut machen möchten:

   ```bash
   oc get namespace $AGENT_NAMESPACE
   oc project $AGENT_NAMESPACE   # Dies muss der aktuelle Namensbereich bzw. das aktuelle Projekt sein.
   oc get deployment -o wide
   oc get deployment agent -o yaml   # Details der Bereitstellung abrufen
   oc get configmap openhorizon-agent-config -o yaml
   oc get secret openhorizon-agent-secrets -o yaml
   oc get pvc openhorizon-agent-pvc -o yaml   # persistenter Datenträger
   ```
   {: codeblock}

12. Wenn ein Edge-Cluster für Richtlinien registriert ist, jedoch nicht über eine benutzerdefinierte Knotenrichtlinie verfügt, kann in vielen Fällen über keine der Bereitstellungsrichtlinien eine Bereitstellung von Edge-Services im Cluster durchgeführt werden. Dies ist bei den Horizon-Beispielen der Fall. Fahren Sie mit dem Abschnitt [Services im Edge-Cluster bereitstellen](#deploying_services) fort, um die Knotenrichtlinie so festzulegen, dass ein Edge-Service im Edge-Cluster bereitgestellt wird.

## Agenten in k3s- und microk8s-Edge-Clustern installieren
{: #install_lite}

Im Folgenden wird die Installation des {{site.data.keyword.ieam}}-Agenten in schlanken k3s- oder microk8s-Kubernetes-Clustern beschrieben:

1. Melden Sie sich bei Ihrem Edge-Cluster als **root** an.

2. Rufen Sie die Datei **agentInstallFiles-x86_64-Cluster.tar.gz** ab und besorgen Sie sich bei Ihrem Administrator einen API-Schlüssel. Diese sollten bereits mit den Schritten im Abschnitt [Erforderliche Informationen und Dateien für Edge-Cluster zusammenstellen](preparing_edge_cluster.md) erstellt worden sein.

3. Extrahieren Sie das Script **agent-install.sh** aus der TAR-Datei:

   ```bash
   tar -zxvf agentInstallFiles-x86_64-Cluster.tar.gz agent-install.sh
   ```
   {: codeblock}

4. Exportieren Sie Ihre Benutzerberechtigungsnachweise für Horizon Exchange:

   ```bash
  export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-schlüssel>
  ```
   {: codeblock}

5. Über das Script **agent-install.sh** wird der {{site.data.keyword.ieam}}-Agent in der Image-Registry des Edge-Clusters gespeichert. Legen Sie den vollständigen Imagepfad (ohne Tag) fest, der verwendet werden soll. Beispiel:

   ```bash
   export IMAGE_ON_EDGE_CLUSTER_REGISTRY=$REGISTRY_ENDPOINT/openhorizon-agent/amd64_anax_k8s
   ```
   {: codeblock}

   **Hinweis:** Das {{site.data.keyword.ieam}}-Agentenimage wird in der lokalen Edge-Cluster-Registry gespeichert, da Kubernetes im Edge-Cluster fortlaufend Zugriff auf das Image benötigt, falls ein Neustart oder Versetzen in einen anderen Pod erforderlich ist.

6. Weisen Sie **agent-install.sh** an, die Standardspeicherklasse zu verwenden:

   * Auf k3s:

      ```bash
      export EDGE_CLUSTER_STORAGE_CLASS=local-path
      ```
      {: codeblock}

   * Auf microk8s:

      ```bash
      export EDGE_CLUSTER_STORAGE_CLASS=microk8s-hostpath
      ```
      {: codeblock}

7. Führen Sie den Befehl **agent-install.sh** aus, um den Horizon-Agenten zu installieren und zu konfigurieren und den Edge-Cluster für Richtlinien zu registrieren:

   ```bash
   ./agent-install.sh -D cluster -z agentInstallFiles-x86_64-Cluster.tar.gz -d <knoten-id>
   ```
   {: codeblock}

   **Hinweise:**
   * Führen Sie das folgende Script aus, um alle verfügbaren Flags anzuzeigen: **./agent-install.sh -h**
   * Wenn ein Fehler auftritt, der dazu führt, dass **agent-install.sh** nicht ausgeführt werden kann, führen Sie zunächst das Script **agent-uninstall.sh** aus (siehe [Agenten in Edge-Cluster entfernen](#remove_agent)), bevor Sie **agent-install.sh** erneut ausführen.

8. Überprüfen Sie, ob der Pod des Agenten ausgeführt wird:

   ```bash
   kubectl get namespaces
   kubectl -n openhorizon-agent get pods
   ```
   {: codeblock}

9. Wenn ein Edge-Cluster für Richtlinien registriert ist, jedoch nicht über eine benutzerdefinierte Knotenrichtlinie verfügt, werden in vielen Fällen über keine der Bereitstellungsrichtlinien Edge-Services im Cluster bereitgestellt. Dies ist bei den Horizon-Beispielen der Fall. Fahren Sie mit dem Abschnitt [Services im Edge-Cluster bereitstellen](#deploying_services) fort, um die Knotenrichtlinie so festzulegen, dass ein Edge-Service in diesem Edge-Cluster bereitgestellt wird.

## Services im Edge-Cluster bereitstellen
{: #deploying_services}

Das Festlegen einer Knotenrichtlinie für diesen Edge-Cluster kann dazu führen, dass Edge-Services über Bereitstellungsrichtlinien im Cluster bereitgestellt werden. Im Folgenden finden Sie ein entsprechendes Beispiel.

1. Legen Sie verschiedene Aliasnamen fest, um die Ausführung des Befehls `hzn` benutzerfreundlicher zu gestalten. (Der Befehl `hzn` wird im Agentencontainer ausgeführt, durch die Aliasnamen wird jedoch eine Ausführung von `hzn` vom Host aus ermöglicht.)

   ```bash
   cat << 'END_ALIASES' >> ~/.bash_aliases
   alias getagentpod='kubectl -n openhorizon-agent get pods --selector=app=agent -o jsonpath={.items[*].metadata.name}'
   alias hzn='kubectl -n openhorizon-agent exec -i $(getagentpod) -- hzn'
   END_ALIASES
   source ~/.bash_aliases
   ```
   {: codeblock}

2. Vergewissern Sie sich, dass Ihr Edge-Knoten konfiguriert (beim {{site.data.keyword.ieam}}-Management-Hub registriert) ist:

   ```bash
   hzn node list
   ```
   {: codeblock}

3. Legen Sie zum Testen des Edge-Clusteragenten die Knotenrichtlinie mit einer Eigenschaft fest, die dazu führt, dass der Beispieloperator und -Service 'helloworld' auf dem Edge-Knoten bereitgestellt wird:

   ```bash
   cat << 'EOF' > operator-example-node.policy.json
   {
     "properties": [
       { "name": "openhorizon.example", "value": "operator" }
     ]
   }
   EOF

   cat operator-example-node.policy.json | hzn policy update -f-
   hzn policy list
   ```
   {: codeblock}

   **Hinweis:**
   * Da der tatsächliche Befehl **hzn** im Agentencontainer ausgeführt wird, müssen Sie für alle `hzn`-Unterbefehle, die eine Eingabedatei benötigen, die betreffende Datei über eine Pipe in den Befehl übertragen, damit ihr Inhalt in den Container übertragen wird.

4. Überprüfen Sie nach einer Minute, ob eine Vereinbarung und die aktiven Container für den Edge-Operator und den Service vorhanden sind:

   ```bash
   hzn agreement list
   kubectl -n openhorizon-agent get pods
   ```
   {: codeblock}

5. Verwenden Sie die Pod-IDs aus dem vorherigen Befehl, um das Protokoll des Edge-Operators und des Service anzuzeigen:

   ```bash
   kubectl -n openhorizon-agent logs -f <operator-pod-id>
   # control-c to get out
   kubectl -n openhorizon-agent logs -f <service-pod-id>
   # control-c to get out
   ```
   {: codeblock}

6. Sie können auch die Umgebungsvariablen anzeigen, die der Agent an den Edge-Service übergibt:

   ```bash
   kubectl -n openhorizon-agent exec -i <service-pod-id> -- env | grep HZN_
   ```
   {: codeblock}

### Im Edge-Cluster bereitgestellte Services ändern
{: #changing_services}

* Ändern Sie die Auswahl der Services, die in Ihrem Edge-Cluster bereitgestellt werden, indem Sie die Knotenrichtlinie ändern:

  ```bash
  cat <neue_knotenrichtlinie>.json | hzn policy update -f-
  hzn policy list
  ```
  {: codeblock}

   Nach wenigen Minuten werden die neuen Services im Edge-Cluster bereitgestellt.

* Hinweis: Bei microk8s kann in einigen Typen von VMs bei Service-Pods, die gestoppt (ersetzt) werden, eine Blockierung beim Beendigungsstatus (**Terminating**) auftreten. Falls dies der Fall ist, können Sie die VMs mit den folgenden Befehlen bereinigen:

  ```bash
  kubectl delete pod <pod-id> -n openhorizon-agent --force --grace-period=0
  pkill -fe <serviceprozess>
  ```
  {: codeblock}

* Wenn Sie anstelle einer Richtlinie ein Muster für die Ausführung von Services in Ihrem Edge-Cluster verwenden möchten, gehen Sie wie folgt vor:

  ```bash
  hzn unregister -f
  hzn register -n $HZN_EXCHANGE_NODE_AUTH -p <mustername>
  ```
  {: codeblock}

## Agenten in Edge-Cluster entfernen
{: #remove_agent}

Führen Sie die folgenden Schritte aus, um die Registrierung eines Edge-Clusters aufzuheben und den {{site.data.keyword.ieam}}-Agenten in dem betreffenden Cluster zu entfernen:

1. Extrahieren Sie das Script **agent-uninstall.sh** aus der TAR-Datei:

   ```bash
   tar -zxvf agentInstallFiles-x86_64-Cluster.tar.gz agent-uninstall.sh
   ```
   {: codeblock}

2. Exportieren Sie Ihre Benutzerberechtigungsnachweise für Horizon Exchange:

   ```bash
  export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-schlüssel>
  ```
   {: codeblock}

3. Entfernen Sie den Agenten:

   ```bash
   ./agent-uninstall.sh -u $HZN_EXCHANGE_USER_AUTH -d
   ```
   {: codeblock}

Hinweis: Das Löschen des Namensbereichs führt gelegentlich zu einer Blockierung im Beendigungsstatus (Terminating). In einer solchen Situation können Sie unter [Namensbereich verbleibt im Status 'Terminating'![Wird in einer neuen Registerkarte geöffnet](../../images/icons/launch-glyph.svg "Wird in einer neuen Registerkarte geöffnet")](https://www.ibm.com/support/knowledgecenter/SSBS6K_3.1.1/troubleshoot/ns_terminating.html) nachlesen, wie Sie den Namensbereich manuell löschen können.
