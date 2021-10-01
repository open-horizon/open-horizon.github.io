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

Führen Sie die folgenden Tasks aus, um einen Edge-Cluster zu installieren und ihn für den {{site.data.keyword.edge_notm}}-Agenten vorzubereiten:

Installieren Sie einen der folgenden Edge-Cluster und bereiten Sie ihn für den {{site.data.keyword.edge_notm}}-Agenten vor:
* [OCP-Edge-Cluster installieren](#install_ocp_edge_cluster)
* [k3s-Edge-Cluster installieren und konfigurieren](#install_k3s_edge_cluster)
* [microk8s-Edge-Cluster installieren und konfigurieren](#install_microk8s_edge_cluster) (für Entwicklungs- und Testumgebungen empfohlen, nicht für Produktionsumgebungen)

## OCP-Edge-Cluster installieren
{: #install_ocp_edge_cluster}

1. Installieren Sie OCP, indem Sie die Installationsanweisungen in der [{{site.data.keyword.open_shift_cp}}-Dokumentation](https://docs.openshift.com/container-platform/4.6/welcome/index.html) befolgen. ({{site.data.keyword.ieam}} unterstützt OCP nur auf x86_64-Plattformen.)

2. Installieren Sie die Kubernetes-CLI (**kubectl**) und die Openshift-Client-CLI (**oc**) sowie Docker auf dem Admin-Host, über den Sie den OCP-Edge-Cluster verwalten. Hierbei handelt es sich um denselben Host, auf dem auch das Script zur Installation des Agenten ausgeführt wird. Weitere Informationen finden Sie unter ['cloudctl', 'kubectl' und 'oc' installieren](../cli/cloudctl_oc_cli.md).

## k3s-Edge-Cluster installieren und konfigurieren
{: #install_k3s_edge_cluster}

Im Folgenden finden Sie eine Übersicht über die Installation eines k3s-Clusters (Rancher), bei dem es sich um einen schlanken und kleinen Kubernetes-Cluster handelt, unter Ubuntu 18.04. Weitere Informationen finden Sie in der [k3s-Dokumentation](https://rancher.com/docs/k3s/latest/en/).

**Hinweis**: Wenn 'kubectl' installiert ist, müssen Sie es deinstallieren, bevor Sie die folgenden Schritte ausführen.

1. Melden Sie sich als **root** an oder wechseln Sie mit `sudo -i` zu einer **root**-Sitzung.

2. Der vollständige Hostname Ihrer Maschine muss mindestens zwei Punkte enthalten. Überprüfen Sie den vollständigen Hostnamen:

   ```bash
   hostname
   ```
    {: codeblock}

   Wenn der vollständige Hostname Ihrer Maschine weniger als zwei Punkte enthält, müssen Sie den Hostnamen wie folgt ändern:

   ```bash
   hostnamectl set-hostname <neuer_hostname_mit_2_punkten>
   ```
   {: codeblock}

   Weitere Informationen finden Sie im Abschnitt [github-Problem](https://github.com/rancher/k3s/issues/53).

3. Installieren Sie k3s:

   ```bash
   curl -sfL https://get.k3s.io | sh -
   ```
   {: codeblock}

4. Erstellen Sie den Image-Registry-Service:
   1. Erstellen Sie eine Datei namens **k3s-persistent-claim.yml** mit dem folgenden Inhalt:
      ```yaml       apiVersion: v1       kind: PersistentVolumeClaim       metadata:         name: docker-registry-pvc       spec:         storageClassName: "local-path"         accessModes:
          - ReadWriteOnce         resources:           requests:             storage: 10Gi
      ```
      {: codeblock}

   2. Erstellen Sie die Anforderung eines persistenten Datenträgers (Persistent Volume Claim - PVC):

      ```bash
      kubectl apply -f k3s-persistent-claim.yml
      ```
      {: codeblock}

   3. Stellen Sie sicher, dass die Anforderung des persistenten Datenträgers erstellt wurde und den Status "Anstehend" (Pending) hat.

      ```bash
      kubectl get pvc
      ```
      {: codeblock}

   4. Erstellen Sie eine Datei namens **k3s-registry-deployment.yml** mit dem folgenden Inhalt:

      ```yaml
      apiVersion: apps/v1       kind: Deployment       metadata:         name: docker-registry         labels:           app: docker-registry       spec:         replicas: 1         selector:           matchLabels:             app: docker-registry         template:           metadata:             labels:               app: docker-registry           spec:             volumes:
            - name: registry-pvc-storage               persistentVolumeClaim:                 claimName: docker-registry-pvc             containers:
            - name: docker-registry               image: registry               ports:
              - containerPort: 5000               volumeMounts:
              - name: registry-pvc-storage                 mountPath: /var/lib/registry
      ---
      apiVersion: v1       kind: Service       metadata:         name: docker-registry-service       spec:         selector:           app: docker-registry         type: NodePort         ports:
          - protocol: TCP             port: 5000
      ```
      {: codeblock}

   5. Erstellen Sie die Registry-Bereitstellung und den Service:

      ```bash
      kubectl apply -f k3s-registry-deployment.yml
      ```
      {: codeblock}

   6. Überprüfen Sie, ob der Service erstellt wurde:

      ```bash
      kubectl get deployment       kubectl get service
      ```
      {: codeblock}

   7. Definieren Sie den Registry-Endpunkt:

      ```bash
      export REGISTRY_ENDPOINT=$(kubectl get service docker-registry-service | grep docker-registry-service | awk '{print $3;}'):5000       cat << EOF >> /etc/rancher/k3s/registries.yaml       mirrors:         "$REGISTRY_ENDPOINT":           endpoint:
            - "http://$REGISTRY_ENDPOINT"       EOF
      ```
      {: codeblock}

   8. Starten Sie k3s erneut, um die Änderung in der Datei **/etc/rancher/k3s/registries.yaml** zu übernehmen:

      ```bash
      systemctl restart k3s
      ```
      {: codeblock}

5. Definieren Sie die Registry bei Docker als unsichere Registry:

   1. Erstellen Sie die Datei **/etc/docker/daemon.json** oder fügen Sie zu dieser Datei hinzu und ersetzen Sie dabei den Wert für `<registry-endpoint>` durch den Wert der Umgebungsvariablen `$REGISTRY_ENDPOINT`, den Sie in einem vorherigen Schritt abgerufen haben.

      ```json
      {
        "insecure-registries": [ "<registry-endpoint>" ]       }
      ```
      {: codeblock}

   2. (Optional) Überprüfen Sie gegebenenfalls wie folgt, dass Docker auf der Maschine installiert ist:

      ```bash
      curl -fsSL get.docker.com | sh
      ```
      {: codeblock}     

   3. Starten Sie Docker erneut, um die Änderung zu übernehmen:

      ```bash
      systemctl restart docker
      ```
      {: codeblock}

## microk8s-Edge-Cluster installieren und konfigurieren
{: #install_microk8s_edge_cluster}

Im Folgenden finden Sie eine Übersicht über die Installation eines microk8s-Clusters, bei dem es sich um einen schlanken und kleinen Kubernetes-Cluster handelt, unter Ubuntu 18.04. (Weitere Anweisungen finden Sie in der [Mikrok8s-Dokumentation](https://microk8s.io/docs).)

**Hinweis:** Dieser Typ eines Edge-Clusters ist für Entwicklungs- oder Testzwecke bestimmt, da ein Kubernetes-Cluster mit nur einem Workerknoten keine Skalierbarkeit oder hohe Verfügbarkeit bereitstellt.

1. So installieren Sie microk8s:

   ```bash
   sudo snap install microk8s --classic --channel=stable
   ```
   {: codeblock}

2. Wenn Sie nicht als **Root** arbeiten, fügen Sie Ihren Benutzer zur Gruppe **microk8s** hinzu:

   ```bash
   sudo usermod -a -G microk8s $USER    sudo chown -f -R $USER ~/.kube    su - $USER   # create new session for group update to take place
   ```
   {: codeblock}

3. Aktivieren Sie DNS und die Speichermodule in microk8s:

   ```bash
   microk8s.enable dns    microk8s.enable storage
   ```
   {: codeblock}

   **Hinweis:** microk8s verwendet standardmäßig `8.8.8.8` und `8.8.4.4` als vorgelagerte Namensserver. Wenn diese Namensserver den Hostnamen des Management-Hubs nicht auflösen können, müssen Sie die von microk8s verwendeten Namensserver wie folgt ändern:
   
   1. Rufen Sie die Liste der vorgelagerten Namensserver in `/etc/resolv.conf` oder `/run/systemd/resolve/resolv.conf` ab.

   2. Bearbeiten Sie die ConfigMap `coredns` im Namensbereich `kube-system`. Legen Sie die vorgelagerten Namensserver im Abschnitt `forward` fest.
   
      ```bash
      microk8s.kubectl edit -n kube-system cm/coredns
      ```
      {: codeblock}
   
   3. Weitere Informationen zu Kubernetes DNS finden Sie in der [Kubernetes-Dokumentation](https://kubernetes.io/docs/tasks/administer-cluster/dns-custom-nameservers/).


4. Überprüfen Sie den Status:

   ```bash
   microk8s.status --wait-ready
   ```
   {: codeblock}

5. Der Befehl 'kubectl' von microk8s trägt den Namen **microk8s.kubectl**, um Konflikte mit einem bereits installierten Befehl **kubectl** zu vermeiden. Wenn auf Ihrem System **kubectl** nicht installiert ist, fügen Sie diesen Aliasnamen für **microk8s.kubectl** hinzu:

   ```bash
   echo 'alias kubectl=microk8s.kubectl' >> ~/.bash_aliases    source ~/.bash_aliases
   ```
   {: codeblock}

6. Aktivieren Sie die Container-Registry und konfigurieren Sie Docker so, dass die unsichere Registry toleriert wird:

   1. Aktivieren Sie die Container-Registry:

      ```bash
      microk8s.enable registry       export REGISTRY_ENDPOINT=localhost:32000
      ```
      {: codeblock}

   2. Installieren Sie Docker, soweit Docker nicht bereits installiert ist:

      ```bash
      curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -       add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"       apt-get install docker-ce docker-ce-cli containerd.io
      ```
      {: codeblock}

   3. Definieren Sie diese Registry bei Docker als unsichere Registry. Erstellen Sie die Datei **/etc/docker/daemon.json** oder fügen Sie zu dieser Datei hinzu und ersetzen Sie dabei den Wert für `<registry-endpoint>` durch den Wert der Umgebungsvariablen `$REGISTRY_ENDPOINT`, den Sie in einem vorherigen Schritt abgerufen haben.

      ```json
      {
        "insecure-registries": [ "<registry-endpoint>" ]       }
      ```
      {: codeblock}

   4. (Optional) Überprüfen Sie ggf. wie folgt, dass Docker auf der Maschine installiert ist:

      ```bash
      curl -fsSL get.docker.com | sh
      ```
      {: codeblock}   

   5. Starten Sie Docker erneut, um die Änderung zu übernehmen:

      ```bash
      sudo systemctl restart docker
      ```
      {: codeblock}

## Weitere Schritte

* [Agent installieren](edge_cluster_agent.md)
