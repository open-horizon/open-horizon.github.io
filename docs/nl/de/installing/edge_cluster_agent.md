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

**Hinweis**: Zur Installation des {{site.data.keyword.ieam}}-Agenten ist Clusteradministratorzugriff für den Edge-Cluster erforderlich.

Beginnen Sie mit der Installation des {{site.data.keyword.edge_notm}}-Agenten auf einem der folgenden Typen von Kubernetes-Edge-Clustern:

* [Agenten in {{site.data.keyword.ocp}}-Kubernetes-Edge-Cluster installieren](#install_kube)
* [Agenten in k3s- und microk8s-Edge-Clustern installieren](#install_lite)

Stellen Sie anschließend einen Edge-Service in Ihrem Edge-Cluster bereit:

* [Services im Edge-Cluster bereitstellen](#deploying_services)

Gehen Sie wie folgt vor, wenn der Agenten entfernt werden soll:

* [Agenten in Edge-Cluster entfernen](../using_edge_services/removing_agent_from_cluster.md)

## Agenten in {{site.data.keyword.ocp}}-Kubernetes-Edge-Cluster installieren
{: #install_kube}

Im Folgenden wird die Installation des {{site.data.keyword.ieam}}-Agenten im {{site.data.keyword.ocp}}-Edge-Cluster beschrieben. Führen Sie die folgenden Schritte auf einem Host aus, der über Administratorzugriff auf Ihren Edge-Cluster verfügt:

1. Melden Sie sich bei Ihrem Edge-Cluster als **admin** an:

   ```bash
   oc login https://<api-endpunkt-host>:<port> -u <admin-benutzer> -p <admin-kennwort> --insecure-skip-tls-verify=true
   ```
   {: codeblock}

2. Wenn Sie die Schritte im Abschnitt [API-Schlüssel erstellen](../hub/prepare_for_edge_nodes.md) noch nicht abgeschlossen haben, tun Sie dies jetzt. Durch diesen Vorgang werden ein API-Schlüssel erstellt, bestimmte Dateien gesucht und Umgebungsvariablenwerte erfasst, die für die Einrichtung von Edge-Knoten erforderlich sind. Legen Sie die folgenden Umgebungsvariablen auf diesem Edge-Cluster fest:

  ```bash
  export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-schlüssel>   export HZN_ORG_ID=<ihre_exchange-organisation>   export HZN_FSS_CSSURL=https://<ieam-management-hub-ingress>/edge-css/
  ```
  {: codeblock}

3. Legen Sie für die Variable für den Namensbereich des Agenten den Standardwert (oder den Namensbereich, in dem der Agent explizit installiert werden soll) fest:

   ```bash
   export AGENT_NAMESPACE=openhorizon-agent
   ```
   {: codeblock}

4. Legen Sie als Speicherklasse für den Agenten eine integrierte Speicherklasse oder eine von Ihnen erstellte Speicherklasse fest. Sie können die verfügbaren Speicherklassen mit dem ersten der beiden folgenden Befehle anzeigen. Setzen Sie dann den Namen der zu verwendenden Speicherklasse im zweiten Befehl ein. Eine Speicherklasse muss mit der Bezeichnung `(default)` versehen sein:

   ```bash
   oc get storageclass    export EDGE_CLUSTER_STORAGE_CLASS=<rook-ceph-cephfs-internal>
   ```
   {: codeblock}

5. Stellen Sie fest, ob eine Standardroute für die {{site.data.keyword.open_shift}}-Image-Registry erstellt wurde, die von außerhalb des Clusters zugänglich ist:

   ```bash
   oc get route default-route -n openshift-image-registry --template='{{ .spec.host }}'
   ```
   {: codeblock}

   Wenn die Befehlsantwort angibt, dass die **Standardroute** nicht gefunden wird, müssen Sie sie zugänglich machen (weitere Informationen hierzu finden Sie im Abschnitt [Registry löschen](https://docs.openshift.com/container-platform/4.6/registry/securing-exposing-registry.html)):

   ```bash
   oc patch configs.imageregistry.operator.openshift.io/cluster --patch '{"spec":{"defaultRoute":true}}' --type=merge
   ```
   {: codeblock}

6. Rufen Sie den Namen der Repository-Route ab, die Sie verwenden müssen:

   ```bash
   export OCP_IMAGE_REGISTRY=`oc get route default-route -n openshift-image-registry --template='{{ .spec.host }}'`
   ```
   {: codeblock}

7. Erstellen Sie ein neues Projekt, in dem Ihre Images gespeichert werden sollen:

   ```bash
   export OCP_PROJECT=$AGENT_NAMESPACE    oc new-project $OCP_PROJECT
   ```
   {: codeblock}

8. Erstellen Sie Servicekonto mit einem Namen Ihrer Wahl:

   ```bash
   export OCP_USER=<servicekontoname>    oc create serviceaccount $OCP_USER
   ```
   {: codeblock}

9. Fügen Sie zu Ihrem Servicekonto eine Rolle für das aktuelle Projekt hinzu:

   ```bash
   oc policy add-role-to-user edit system:serviceaccount:$OCP_PROJECT:$OCP_USER
   ```
   {: codeblock}

10. Legen Sie Ihr Servicekontotoken in der folgenden Umgebungsvariablen fest:

   ```bash
   export OCP_TOKEN=`oc serviceaccounts get-token $OCP_USER`
   ```
   {: codeblock}

11. Rufen Sie das {{site.data.keyword.open_shift}}-Zertifikat ab und lassen Sie die Anerkennung durch Docker zu:

   ```bash
   echo | openssl s_client -connect $OCP_IMAGE_REGISTRY:443 -showcerts | sed -n "/-----BEGIN CERTIFICATE-----/,/-----END CERTIFICATE-----/p" > ca.crt
   ```
   {: codeblock}

   Unter {{site.data.keyword.linux_notm}}:

   ```bash
   mkdir -p /etc/docker/certs.d/$OCP_IMAGE_REGISTRY    cp ca.crt /etc/docker/certs.d/$OCP_IMAGE_REGISTRY    systemctl restart docker.service
   ```
   {: codeblock}

   Unter {{site.data.keyword.macOS_notm}}:

   ```bash
   mkdir -p ~/.docker/certs.d/$OCP_IMAGE_REGISTRY    cp ca.crt ~/.docker/certs.d/$OCP_IMAGE_REGISTRY
   ```
   {: codeblock}

   Verwenden Sie in {{site.data.keyword.macOS_notm}} das Docker-Desktop-Symbol auf der rechten Seite der Desktop-Menüleiste, um Docker erneut zu starten, indem Sie im Dropdown-Menü auf **Neustart** klicken.

12. Melden Sie sich beim {{site.data.keyword.ocp}} Docker-Host an:

   ```bash
   echo "$OCP_TOKEN" | docker login -u $OCP_USER --password-stdin $OCP_IMAGE_REGISTRY
   ```
   {: codeblock}

13. Konfigurieren Sie weitere Truststores für den Zugriff auf die Image-Registry:   

    ```bash
    oc create configmap registry-config --from-file=$OCP_IMAGE_REGISTRY=ca.crt -n openshift-config
    ```
    {: codeblock}

14. Bearbeiten Sie die neue `registry-config`-Komponente:

    ```bash
    oc edit image.config.openshift.io cluster
    ```
    {: codeblock}

15. Aktualisieren Sie den Abschnitt `spec:`:

    ```bash
    spec:       additionalTrustedCA:        name: registry-config
    ```
    {: codeblock}

16. Über das Script **agent-install.sh** wird der {{site.data.keyword.ieam}}-Agent in der Container-Registry des Edge-Clusters gespeichert. Legen Sie den Registry-Benutzer, das Kennwort und den vollständigen Imagepfad (ohne Tag) wie folgt fest:

   ```bash
   export EDGE_CLUSTER_REGISTRY_USERNAME=$OCP_USER    export EDGE_CLUSTER_REGISTRY_TOKEN="$OCP_TOKEN"    export IMAGE_ON_EDGE_CLUSTER_REGISTRY=$OCP_IMAGE_REGISTRY/$OCP_PROJECT/amd64_anax_k8s
   ```
   {: codeblock}

   **Hinweis:** Das {{site.data.keyword.ieam}}-Agentenimage wird in der lokalen Edge-Cluster-Registry gespeichert, da Kubernetes im Edge-Cluster fortlaufend Zugriff auf das Image benötigt, falls ein Neustart oder Versetzen in einen anderen Pod erforderlich ist.

17. Laden Sie das Script **agent-install.sh** aus dem Cloud Sync-Service (CSS) herunter und machen Sie es ausführbar:

   ```bash
   curl -u "$HZN_ORG_ID/$HZN_EXCHANGE_USER_AUTH" -k -o agent-install.sh $HZN_FSS_CSSURL/api/v1/objects/IBM/agent_files/agent-install.sh/data    chmod +x agent-install.sh
   ```
   {: codeblock}

18. Führen Sie **agent-install.sh** aus, um die erforderlichen Dateien aus CSS abzurufen, den {{site.data.keyword.horizon}}-Agenten zu installieren und zu konfigurieren und den Edge-Cluster mit der Richtlinie zu registrieren:

   ```bash
   ./agent-install.sh -D cluster -i 'css:'
   ```
   {: codeblock}

   **Hinweise:**
   * Führen Sie das folgende Script aus, um alle verfügbaren Flags anzuzeigen: **./agent-install.sh -h**
   * Wenn das Script **agent-install.sh** fehlschlägt, müssen Sie den Fehler beheben und **agent-install.sh** erneut ausführen. Falls das Problem hierdurch nicht gelöst wird, führen Sie das Script **agent-uninstall.sh** (siehe [Agenten aus Edge-Cluster entfernen](../using_edge_services/removing_agent_from_cluster.md)) aus, bevor Sie erneut das Script  **agent-install.sh** ausführen.

19. Wechseln Sie in den Namensbereich des Agenten (auch als Projekt bezeichnet) und vergewissern Sie sich wie folgt, dass der Agentenpod ausgeführt wird:

   ```bash
   oc project $AGENT_NAMESPACE    oc get pods
   ```
   {: codeblock}

20. Nach der Installation des Agenten in Ihrem Edge-Cluster können Sie nun die folgenden Befehle ausführen, wenn Sie sich mit den zum Agenten gehörigen Kubernetes-Ressourcen vertraut machen möchten:

   ```bash
   oc get namespace $AGENT_NAMESPACE    oc project $AGENT_NAMESPACE   # Dies muss der aktuelle Namensbereich bzw. das aktuelle Projekt sein.    oc get deployment -o wide    oc get deployment agent -o yaml   # Details der Bereitstellung abrufen    oc get configmap openhorizon-agent-config -o yaml    oc get secret openhorizon-agent-secrets -o yaml    oc get pvc openhorizon-agent-pvc -o yaml   # persistenter Datenträger
   ```
   {: codeblock}

21. Wenn ein Edge-Cluster für Richtlinien registriert ist, jedoch nicht über eine benutzerdefinierte Knotenrichtlinie verfügt, kann in vielen Fällen über keine der Bereitstellungsrichtlinien eine Bereitstellung von Edge-Services im Cluster durchgeführt werden. Dies ist bei den Horizon-Beispielen der Fall. Fahren Sie mit dem Abschnitt [Services im Edge-Cluster bereitstellen](#deploying_services) fort, um die Knotenrichtlinie so festzulegen, dass ein Edge-Service in diesem Edge-Cluster bereitgestellt wird.

## Agenten in k3s- und microk8s-Edge-Clustern installieren
{: #install_lite}

In diesem Inhalt wird beschrieben, wie der {{site.data.keyword.ieam}}-Agent auf [k3s](https://k3s.io/)- oder [microk8s](https://microk8s.io/)- und leichten und kleinen Kubernetes-Clustern installiert werden kann:

1. Melden Sie sich bei Ihrem Edge-Cluster als **root** an.

2. Wenn Sie die Schritte im Abschnitt [API-Schlüssel erstellen](../hub/prepare_for_edge_nodes.md) noch nicht abgeschlossen haben, tun Sie dies jetzt. Durch diesen Vorgang werden ein API-Schlüssel erstellt, bestimmte Dateien gesucht und Umgebungsvariablenwerte erfasst, die für die Einrichtung von Edge-Knoten erforderlich sind. Legen Sie die folgenden Umgebungsvariablen auf diesem Edge-Cluster fest:

  ```bash
  export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-schlüssel>   export HZN_ORG_ID=<ihre_exchange-organisation>   export HZN_FSS_CSSURL=https://<ieam-management-hub-ingress>/edge-css/
  ```
  {: codeblock}

3. Kopieren Sie das Script **agent-install.sh** in Ihren neuen Edge-Cluster.

4. Über das Script **agent-install.sh** wird der {{site.data.keyword.ieam}}-Agent in der Image-Registry des Edge-Clusters gespeichert. Legen Sie den vollständigen Imagepfad (ohne Tag) fest, der verwendet werden soll. Beispiel:

   * Auf k3s:

      ```bash
      REGISTRY_ENDPOINT=$(kubectl get service docker-registry-service | grep docker-registry-service | awk '{print $3;}'):5000       export IMAGE_ON_EDGE_CLUSTER_REGISTRY=$REGISTRY_ENDPOINT/openhorizon-agent/amd64_anax_k8s
      ```
      {: codeblock}

   * Auf microk8s:

      ```bash
      export IMAGE_ON_EDGE_CLUSTER_REGISTRY=localhost:32000/openhorizon-agent/amd64_anax_k8s
      ```
      {: codeblock}

   **Hinweis:** Das {{site.data.keyword.ieam}}-Agentenimage wird in der lokalen Edge-Cluster-Registry gespeichert, da Kubernetes im Edge-Cluster fortlaufend Zugriff auf das Image benötigt, falls ein Neustart oder Versetzen in einen anderen Pod erforderlich ist.

5. Weisen Sie **agent-install.sh** an, die Standardspeicherklasse zu verwenden:

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

6. Führen Sie das Script **agent-install.sh** aus, um die erforderlichen Dateien aus CSS (Cloud Sync Service) abzurufen, den {{site.data.keyword.horizon}}-Agenten zu installieren und zu konfigurieren und ihren Edge-Cluster mit der Richtlinie zu registrieren:

   ```bash
   ./agent-install.sh -D cluster -i 'css:'
   ```
   {: codeblock}

   **Hinweise:**
   * Führen Sie das folgende Script aus, um alle verfügbaren Flags anzuzeigen: **./agent-install.sh -h**
   * Wenn ein Fehler auftritt, der dazu führt, dass **agent-install.sh** nicht ausgeführt werden kann, beheben Sie den angezeigten Fehler und führen Sie das Script **agent-install.sh** erneut aus. Falls das Problem hierdurch nicht gelöst wird, führen Sie das Script **agent-uninstall.sh** (siehe [Agenten aus Edge-Cluster entfernen](../using_edge_services/removing_agent_from_cluster.md)) aus, bevor Sie erneut das Script  **agent-install.sh** ausführen.

7. Überprüfen Sie wie folgt, ob der Pod des Agenten ausgeführt wird:

   ```bash
   kubectl get namespaces    kubectl -n openhorizon-agent get pods
   ```
   {: codeblock}

8. Wenn ein Edge-Cluster für Richtlinien registriert ist, jedoch nicht über eine benutzerdefinierte Knotenrichtlinie verfügt, kann in der Regel über keine der Bereitstellungsrichtlinien eine Bereitstellung von Edge-Services im Cluster durchgeführt werden. Dies ist ein erwartetes Verhalten. Fahren Sie mit dem Abschnitt [Services im Edge-Cluster bereitstellen](#deploying_services) fort, um die Knotenrichtlinie so festzulegen, dass ein Edge-Service in diesem Edge-Cluster bereitgestellt wird.

## Services im Edge-Cluster bereitstellen
{: #deploying_services}

Das Festlegen einer Knotenrichtlinie für diesen Edge-Cluster kann dazu führen, dass Edge-Services über Bereitstellungsrichtlinien im Cluster bereitgestellt werden. Im Folgenden finden Sie ein entsprechendes Beispiel.

1. Legen Sie verschiedene Aliasnamen fest, um die Ausführung des Befehls `hzn` benutzerfreundlicher zu gestalten. (Der Befehl `hzn` wird im Agentencontainer ausgeführt, durch die Aliasnamen wird jedoch eine Ausführung von `hzn` vom Host aus ermöglicht.)

   ```bash
   cat << 'END_ALIASES' >> ~/.bash_aliases    alias getagentpod='kubectl -n openhorizon-agent get pods --selector=app=agent -o jsonpath={.items[*].metadata.name}'    alias hzn='kubectl -n openhorizon-agent exec -i $(getagentpod) -- hzn'    END_ALIASES    source ~/.bash_aliases
   ```
   {: codeblock}

2. Vergewissern Sie sich, dass Ihr Edge-Knoten konfiguriert (beim {{site.data.keyword.ieam}}-Management-Hub registriert) ist:

   ```bash
   hzn node list
   ```
   {: codeblock}

3. Legen Sie zum Testen des Edge-Clusteragenten die Knotenrichtlinie mit einer Eigenschaft fest, die den Beispieloperator und -Service 'helloworld' auf dem Edge-Knoten bereitstellt:

   ```bash
   cat << 'EOF' > operator-example-node.policy.json    {
     "properties": [
       { "name": "openhorizon.example", "value": "operator" }      ]
   }    EOF

   cat operator-example-node.policy.json | hzn policy update -f-    hzn policy list
   ```
   {: codeblock}

   **Hinweis:**
   * Da der tatsächliche Befehl **hzn** im Agentencontainer ausgeführt wird, müssen Sie für alle `hzn`-Befehle, die eine Eingabedatei benötigen, die betreffende Datei über eine Pipe in den Befehl übertragen, damit ihr Inhalt in den Container übertragen wird.

4. Überprüfen Sie nach einer Minute, ob eine Vereinbarung und die aktiven Container für den Edge-Operator und den Service vorhanden sind:

   ```bash
   hzn agreement list    kubectl -n openhorizon-agent get pods
   ```
   {: codeblock}

5. Verwenden Sie die Pod-IDs aus dem vorherigen Befehl, um das Protokoll des Edge-Operators und des Service anzuzeigen:

   ```bash
   kubectl -n openhorizon-agent logs -f <operator-pod-id>    # control-c to get out    kubectl -n openhorizon-agent logs -f <service-pod-id>    # control-c to get out
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
  cat <neue_knotenrichtlinie>.json | hzn policy update -f-   hzn policy list
  ```
  {: codeblock}

   Nach wenigen Minuten werden die neuen Services im Edge-Cluster bereitgestellt.

* **Hinweis**: Auf bestimmten VMs mit microk8s blockieren die Service-Pods, die gestoppt (ersetzt) werden, möglicherweise im Status **Terminating**. Führen Sie in diesem Fall Folgendes aus:

  ```bash
  kubectl delete pod <pod-id> -n openhorizon-agent --force --grace-period=0   pkill -fe <serviceprozess>
  ```
  {: codeblock}

* Wenn Sie anstelle einer Richtlinie ein Muster für die Ausführung von Services in Ihrem Edge-Cluster verwenden möchten, gehen Sie wie folgt vor:

  ```bash
  hzn unregister -f   hzn register -n $HZN_EXCHANGE_NODE_AUTH -p <mustername>
  ```
  {: codeblock}
