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

# Preparando um cluster de borda
{: #preparing_edge_cluster}

Execute as tarefas a seguir para instalar um cluster de borda e prepará-lo para o gente {{site.data.keyword.edge_notm}}:

Instale um desses clusters de borda e prepare-o para o agente {{site.data.keyword.edge_notm}}:
* [Instale um cluster de borda OCP](#install_ocp_edge_cluster)
* [Instale e configure um cluster de borda k3s](#install_k3s_edge_cluster)
* [Instale e configure um cluster de borda microk8s](#install_microk8s_edge_cluster) (para desenvolvimento e teste, não recomendado para produção)

## Instale um cluster de borda OCP
{: #install_ocp_edge_cluster}

1. Instale o OCP seguindo as instruções de instalação na [Documentação do {{site.data.keyword.open_shift_cp}}](https://docs.openshift.com/container-platform/4.6/welcome/index.html). ({{site.data.keyword.ieam}} suporta apenas OCP em plataformas x86_64.)

2. Instale a CLI do Kubernetes (**kubectl**), a CLI do cliente do Openshift (**oc**) e o Docker no host admin no qual você administra o cluster de borda do OCP. Este host é o mesmo no qual você executa o script de instalação do agente. Para obter mais informações, consulte [Instalando o cloudctl, o kubectl e o oc](../cli/cloudctl_oc_cli.md).

## Instale e configure um cluster de borda k3s
{: #install_k3s_edge_cluster}

Este conteúdo fornece um resumo de como instalar o k3s (rancher), um cluster Kubernetes leve e pequeno, no Ubuntu 18.04. Para obter mais informações, consulte a [Documentação k3s](https://rancher.com/docs/k3s/latest/en/).

**Nota**: se instalado, desinstale o kubectl antes de concluir as etapas a seguir.

1. Efetue login como **raiz** ou eleve para **raiz** com `sudo -i`

2. O nome do host integral de sua máquina deve conter pelo menos dois pontos. Verifique o nome do host completo:

   ```bash
   Nome do host
   ```
    {: codeblock}

   Se o nome completo do host de sua máquina contiver menos de dois pontos, mude-o:

   ```bash
   hostnamectl set-hostname <your-new-hostname-with-2-dots>
   ```
   {: codeblock}

   Para obter mais informações, consulte [Problema de github](https://github.com/rancher/k3s/issues/53).

3. Instale o k3s:

   ```bash
   curl -sfL https://get.k3s.io | sh -
   ```
   {: codeblock}

4. Crie o serviço de registro de imagem:
   1. Crie um arquivo chamado **k3s-persistent-claim.yml** com este conteúdo:
      ```yaml       apiVersion: v1       kind: PersistentVolumeClaim       metadata:         name: docker-registry-pvc       spec:         storageClassName: "local-path"         accessModes:
          - ReadWriteOnce         resources:           requests:             storage: 10Gi
      ```
      {: codeblock}

   2. Crie a solicitação de volume persistente:

      ```bash
      kubectl apply -f k3s-persistent-claim.yml
      ```
      {: codeblock}

   3. Verifique se a solicitação de volume persistente foi criada e está no status "Pendente"

      ```bash
      Kubectl get pvc
      ```
      {: codeblock}

   4. Crie um arquivo chamado **k3s-registry-deployment.yml** com este conteúdo:

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

   5. Crie a implementação e o serviço do registro:

      ```bash
      kubectl apply -f k3s-registry-deployment.yml
      ```
      {: codeblock}

   6. Verifique se o serviço foi criado:

      ```bash
      kubectl get deployment       kubectl get service
      ```
      {: codeblock}

   7. Defina o terminal de registro:

      ```bash
      export REGISTRY_ENDPOINT=$(kubectl get service docker-registry-service | grep docker-registry-service | awk '{print $3;}'):5000       cat << EOF >> /etc/rancher/k3s/registries.yaml       mirrors:         "$REGISTRY_ENDPOINT":           endpoint:
            - "http://$REGISTRY_ENDPOINT"       EOF
      ```
      {: codeblock}

   8. Reinicie o k3s para que a mudança seja selecionada no **/etc/rancher/k3s/registries.yaml**:

      ```bash
      systemctl restart k3s
      ```
      {: codeblock}

5. Defina este registro para o Docker como um registro não protegido:

   1. Crie ou inclua ao **/etc/docker/daemon.json** (substituindo `<registry-endpoint>` pelo valor da variável de ambiente `$REGISTRY_ENDPOINT` obtida em uma etapa anterior).

      ```json
      {
        "insecure-registries": [ "<registry-endpoint>" ]       }
      ```
      {: codeblock}

   2. (opcional) Se necessário, verifique se o Docker está em sua máquina:

      ```bash
      curl -fsSL get.docker.com | sh
      ```
      {: codeblock}     

   3. Reinicie o Docker para que a mudança seja selecionada:

      ```bash
      systemctl restart docker
      ```
      {: codeblock}

## Instale e configure um cluster de borda microk8sr
{: #install_microk8s_edge_cluster}

Este conteúdo fornece um resumo de como instalar o microk8s, um cluster Kubernetes leve e pequeno, no Ubuntu 18.04. (Para obter instruções mais detalhadas, consulte a [Documentação microk8s](https://microk8s.io/docs).)

**Nota**: este tipo de cluster de borda destina-se ao desenvolvimento e teste porque um único cluster Kubernetes do nó do trabalhador não fornece escalabilidade ou alta disponibilidade.

1. Instale o microk8s:

   ```bash
   sudo snap install microk8s --classic --channel=stable
   ```
   {: codeblock}

2. Se não estiver executando como **root**, inclua seu usuário no grupo **microk8s**:

   ```bash
   sudo usermod -a -G microk8s $USER    sudo chown -f -R $USER ~/.kube    su - $USER   # create new session for group update to take place
   ```
   {: codeblock}

3. Ative os módulos de dns e de armazenamento em microk8s:

   ```bash
   microk8s.enable dns    microk8s.enable storage
   ```
   {: codeblock}

   **Nota**: por padrão, o Microk8s usa `8.8.8.8` e `8.8.4.4` como servidores de nomes de envio de dados. Se esses servidores de nomes não puderem resolver o nome do host do hub de gerenciamento, deve-se mudar os servidores de nomes que o microk8s está usando:
   
   1. Recupere a lista de servidores de nomes de envio de dados em `/etc/resolv.conf` ou `/run/systemd/resolve/resolv.conf`.

   2. Edite o configmap `coredns` no namespace `kube-system`. Configure os servidores de nome de envio de dados na seção `forward`.
   
      ```bash
      microk8s.kubectl edit -n kube-system cm/coredns
      ```
      {: codeblock}
   
   3. Para obter mais informações sobre o DNS Kubernetes, consulte a [documentação do Kubernetes](https://kubernetes.io/docs/tasks/administer-cluster/dns-custom-nameservers/).


4. Verifique o status:

   ```bash
   microk8s.status --wait-ready
   ```
   {: codeblock}

5. O comando kubectl do microK8s é chamado de **microk8s.kubectl**, para evitar conflitos com um comando **kubectl** que já esteja instalado. Supondo que **kubectl** não esteja instalado, inclua este alias para **microk8s.kubectl**:

   ```bash
   echo 'alias kubectl=microk8s.kubectl' >> ~/.bash_aliases    source ~/.bash_aliases
   ```
   {: codeblock}

6. Ative o registro de contêiner e configure o Docker para tolerar o registro não seguro:

   1. Ative o registro de contêiner:

      ```bash
      microk8s.enable registry       export REGISTRY_ENDPOINT=localhost:32000
      ```
      {: codeblock}

   2. Instale o Docker (se ainda não estiver instalado):

      ```bash
      curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -       add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"       apt-get install docker-ce docker-ce-cli containerd.io
      ```
      {: codeblock}

   3. Defina este registro como inseguro para o Docker. Crie ou inclua ao **/etc/docker/daemon.json** (substituindo `<registry-endpoint>` pelo valor da variável de ambiente `$REGISTRY_ENDPOINT` obtida em uma etapa anterior).

      ```json
      {
        "insecure-registries": [ "<registry-endpoint>" ]       }
      ```
      {: codeblock}

   4. (opcional) Verifique se o Docker está em sua máquina:

      ```bash
      curl -fsSL get.docker.com | sh
      ```
      {: codeblock}   

   5. Reinicie o Docker para que a mudança seja selecionada:

      ```bash
      sudo systemctl restart docker
      ```
      {: codeblock}

## O que vem depois

* [Instalando o Agente](edge_cluster_agent.md)
