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

* Einen der folgenden Typen von Edge-Clustern installieren:
  * [OCP-Edge-Cluster installieren](#install_ocp_edge_cluster)
  * [k3s-Edge-Cluster installieren und konfigurieren](#install_k3s_edge_cluster)
  * [microk8s-Edge-Cluster installieren und konfigurieren](#install_microk8s_edge_cluster) (für Entwicklungs- und Testumgebungen empfohlen, nicht für Produktionsumgebungen)
* [Erforderliche Informationen und Dateien für Edge-Cluster zusammenstellen](#gather_info)

## OCP-Edge-Cluster installieren
{: #install_ocp_edge_cluster}

1. Installieren Sie OCP wie in der [Dokumentation zu {{site.data.keyword.open_shift_cp}} ![Wird in einer neuen Registerkarte geöffnet](../../images/icons/launch-glyph.svg "Wird in einer neuen Registerkarte geöffnet")](https://docs.openshift.com/container-platform/4.4/welcome/index.html) beschrieben.

2. Installieren Sie die Kubenetes-CLI (**kubectl**) und Openshift-Client-CLI (**oc**) auf dem Admin-Host, über den Sie den Edge-Cluster verwalten (derselbe Host, von dem aus auch das Script zur Installation des Agenten ausgeführt wird). Weitere Informationen hierzu finden Sie unter ['cloudctl', 'kubectl' und 'oc' installieren](../installing/cloudctl_oc_cli.md).

## k3s-Edge-Cluster installieren und konfigurieren
{: #install_k3s_edge_cluster}

Im Folgenden finden Sie eine Übersicht über die Installation eines k3s- bzw. Rancher-Clusters, bei dem es sich um einen schlanken und kleinen Kubernetes-Cluster handelt, unter Ubuntu 18.04. (Detailliertere Anweisungen enthält die [k3s-Dokumentation ![Wird in einer neuen Registerkarte geöffnet](../../images/icons/launch-glyph.svg "Wird in einer neuen Registerkarte geöffnet")](https://rancher.com/docs/k3s/latest/en/).)

1. Melden Sie sich als **root** an oder wechseln Sie mit `sudo -i` zu einer **root**-Sitzung.

2. Installieren Sie k3s:

   ```bash
   curl -sfL https://get.k3s.io | sh -
   ```
   {: codeblock}

3. Erstellen Sie den Image-Registry-Service:

   1. Erstellen Sie eine Datei namens **k3s-registry-deployment.yml** mit dem folgenden Inhalt:

      ```yaml
      apiVersion: apps/v1
      kind: Deployment
      metadata:
        name: docker-registry
        labels:
          app: docker-registry
      spec:
        replicas: 1
        selector:
          matchLabels:
            app: docker-registry
        template:
          metadata:
            labels:
              app: docker-registry
          spec:
            containers:
            - name: docker-registry
              image: registry
              ports:
              - containerPort: 5000
              volumeMounts:
              - name: storage
                mountPath: /var/lib/registry
            volumes:
            - name: storage
              emptyDir: {} # FIXME: make this a persistent volume if using in production
      ---
      apiVersion: v1
      kind: Service
      metadata:
        name: docker-registry-service
      spec:
        selector:
          app: docker-registry
        type: NodePort
        ports:
          - protocol: TCP
            port: 5000
      ```
      {: codeblock}

   2. Erstellen Sie den Registry-Service:

      ```bash
      kubectl apply -f k3s-registry-deployment.yml
      ```
      {: codeblock}

   3. Überprüfen Sie, ob der Service erstellt wurde:

      ```bash
      kubectl get deployment
      kubectl get service
      ```
      {: codeblock}

   4. Definieren Sie den Registry-Endpunkt:

      ```bash
      export REGISTRY_ENDPOINT=$(kubectl get ep docker-registry-service | grep docker-registry-service | awk '{print $2}')
      cat << EOF >> /etc/rancher/k3s/registries.yaml
      mirrors:
        "$REGISTRY_ENDPOINT":
          endpoint:
            - "http://$REGISTRY_ENDPOINT"
      EOF
      ```
      {: codeblock}

   5. Starten Sie k3s erneut, um die Änderung in der Datei **/etc/rancher/k3s/registries.yaml** zu übernehmen:

      ```bash
      systemctl restart k3s
      ```
      {: codeblock}

4. Definieren Sie die Registry bei Docker als unsichere Registry:

   1. Erstellen Sie die Datei **/etc/docker/daemon.json** bzw. fügen Sie sie hinzu (ersetzen Sie dabei den Wert für `$REGISTRY_ENDPOINT`):

      ```json
      {
        "insecure-registries": [ "$REGISTRY_ENDPOINT" ]
      }
      ```
      {: codeblock}

   2. Starten Sie Docker erneut, um die Änderung zu übernehmen:

      ```bash
      systemctl restart docker
      ```
      {: codeblock}

## microk8s-Edge-Cluster installieren und konfigurieren
{: #install_microk8s_edge_cluster}

Im Folgenden finden Sie eine Übersicht über die Installation eines microk8s-Clusters, bei dem es sich um einen schlanken und kleinen Kubernetes-Cluster handelt, unter Ubuntu 18.04. (Detailliertere Anweisungen erhalten Sie in der [microk8s-Dokumentation ![Wird auf einer neuen Registerkarte geöffnet](../../images/icons/launch-glyph.svg "Wird auf einer neuen Registerkarte geöffnet")](https://microk8s.io/docs).)

Hinweis: Dieser Typ eines Edge-Clusters ist für Entwicklungs- oder Testzwecke bestimmt, da ein Kubernetes-Cluster mit nur einem Workerknoten keine Skalierbarkeit oder hohe Verfügbarkeit bereitstellt.

1. So installieren Sie microk8s:

   ```bash
   sudo snap install microk8s --classic --channel=stable
   ```
   {: codeblock}

2. Wenn Sie nicht als **Root** arbeiten, fügen Sie Ihren Benutzer zur Gruppe **microk8s** hinzu:

   ```bash
   sudo usermod -a -G microk8s $USER
   sudo chown -f -R $USER ~/.kube
   su - $USER   # create new session for group update to take place
   ```
   {: codeblock}

3. Aktivieren Sie DNS und die Speichermodule in microk8s:

   ```bash
   microk8s.enable dns
   microk8s.enable storage
   ```
   {: codeblock}

4. Überprüfen Sie den Status:

   ```bash
   microk8s.status --wait-ready
   ```
   {: codeblock}

5. Der Befehl 'kubectl' von microk8s trägt den Namen **microk8s.kubectl**, um Konflikte mit einem bereits installierten Befehl **kubectl** zu vermeiden. Wenn auf Ihrem System **kubectl** nicht bereits installiert ist, fügen Sie diesen Aliasnamen für **microk8s.kubectl** hinzu. 

   ```bash
   echo 'alias kubectl=microk8s.kubectl' >> ~/.bash_aliases
   source ~/.bash_aliases
   ```
   {: codeblock}

6. Aktivieren Sie die Container-Registry und konfigurieren Sie Docker so, dass die unsichere Registry toleriert wird:

   1. Aktivieren Sie die Container-Registry:

      ```bash
      microk8s.enable registry
      export REGISTRY_ENDPOINT=localhost:32000
      ```
      {: codeblock}

   2. Installieren Sie Docker, soweit Docker nicht bereits installiert ist:

      ```bash
      curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
      add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
      apt-get install docker-ce docker-ce-cli containerd.io
      ```
      {: codeblock}

   3. Definieren Sie die Registry bei Docker als unsichere Registry. Erstellen Sie die Datei **/etc/docker/daemon.json** bzw. fügen Sie sie hinzu (ersetzen Sie dabei den Wert für `$REGISTRY_ENDPOINT`):

      ```json
      {
        "insecure-registries": [ "$REGISTRY_ENDPOINT" ]
      }
      ```
      {: codeblock}

   4. Starten Sie Docker erneut, um die Änderung zu übernehmen:

      ```bash
      sudo systemctl restart docker
      ```
      {: codeblock}

## Weitere Schritte

* [Agent installieren](edge_cluster_agent.md)
