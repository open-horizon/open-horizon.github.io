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

* Instale um desses tipos de clusters de borda:
  * [Instale um cluster de borda OCP](#install_ocp_edge_cluster)
  * [Instale e configure um cluster de borda k3s](#install_k3s_edge_cluster)
  * [Instale e configure um cluster de borda microk8s](#install_microk8s_edge_cluster) (para desenvolvimento e teste, não recomendado para produção) 
* [Reúna as informações e os arquivos necessários para os clusters de borda](#gather_info)

## Instale um cluster de borda OCP
{: #install_ocp_edge_cluster}

1. Instale o OCP seguindo as instruções de instalação na [Documentação do {{site.data.keyword.open_shift_cp}} ![Abre em uma nova guia](../../images/icons/launch-glyph.svg "Abre em uma nova guia")](https://docs.openshift.com/container-platform/4.4/welcome/index.html).

2. Instale a CLI do Kubenetes (**kubectl**) e a CLI do cliente Openshift (**oc**) no host admin a partir do qual o cluster OCP é administrado (o mesmo host a partir do qual o scritp de instalação do agente será instalado). Consulte [Instalando o cloudctl, o kubectl e o oc](../installing/cloudctl_oc_cli.md).

## Instale e configure um cluster de borda k3s
{: #install_k3s_edge_cluster}

Esta seção fornece um resumo de como instalar o k3s (rancher), um cluster Kubernetes leve e pequeno, no Unbutu 18.04. (Para
obter instruções mais detalhadas, consulte a [Documentação do k3s ![Abre em uma nova guia](../../images/icons/launch-glyph.svg "Abre em uma nova guia")](https://rancher.com/docs/k3s/latest/en/)).

1. Efetue login como **raiz** ou eleve para **raiz** com `sudo -i`

2. Instale o k3s:

   ```bash
   curl -sfL https://get.k3s.io | sh -
   ```
   {: codeblock}

3. Crie o serviço de registro de imagem:

   1. Crie um arquivo chamado **k3s-registry-deployment.yml** com este conteúdo:

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

   2. Crie o serviço de registro:

      ```bash
      kubectl apply -f k3s-registry-deployment.yml
      ```
      {: codeblock}

   3. Verifique se o serviço foi criado:

      ```bash
      kubectl get deployment
      kubectl get service
      ```
      {: codeblock}

   4. Defina o terminal de registro:

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

   5. Reinicie o k3s para que a mudança seja selecionada no **/etc/rancher/k3s/registries.yaml**:

      ```bash
      systemctl restart k3s
      ```
      {: codeblock}

4. Defina este registro para o Docker como um registro não protegido:

   1. Crie ou inclua no **/etc/docker/daemon.json** (substituindo o valor para `$REGISTRY_ENDPOINT`):

      ```json
      {
        "insecure-registries": [ "$REGISTRY_ENDPOINT" ]
      }
      ```
      {: codeblock}

   2. Reinicie o Docker para que a mudança seja selecionada:

      ```bash
      systemctl restart docker
      ```
      {: codeblock}

## Instale e configure um cluster de borda microk8sr
{: #install_microk8s_edge_cluster}

Esta seção fornece um resumo de como instalar o microk8s, um cluster Kubernetes leve e pequeno, no Unbutu 18.04. (Para obter instruções mais detalhadas, consulte a [Documentação do microk8s ![Abre em uma nova guia](../../images/icons/launch-glyph.svg "Abre em uma nova guia")](https://microk8s.io/docs)).

Nota: esse tipo de cluster de borda deve ser usado para desenvolvimento e teste, pois um único cluster Kubernetes do nó do trabalhador não fornece escalabilidade ou alta disponibilidade.

1. Instale o microk8s:

   ```bash
   sudo snap install microk8s --classic --channel=stable
   ```
   {: codeblock}

2. Se não estiver executando como **root**, inclua seu usuário no grupo **microk8s**:

   ```bash
   sudo usermod -a -G microk8s $USER
   sudo chown -f -R $USER ~/.kube
   su - $USER   # create new session for group update to take place
   ```
   {: codeblock}

3. Ative os módulos de dns e de armazenamento em microk8s:

   ```bash
   microk8s.enable dns
   microk8s.enable storage
   ```
   {: codeblock}

4. Verifique o status:

   ```bash
   microk8s.status --wait-ready
   ```
   {: codeblock}

5. O comando kubectl do microK8s é chamado de **microk8s.kubectl**, para evitar conflitos com um comando **kubectl** que já esteja instalado. Supondo que o **kubectl** ainda não esteja instalado, inclua esse alias em **microk8s.kubectl**.

   ```bash
   echo 'alias kubectl=microk8s.kubectl' >> ~/.bash_aliases
   source ~/.bash_aliases
   ```
   {: codeblock}

6. Ative o registro de contêiner e configure o Docker para tolerar o registro não seguro:

   1. Ative o registro de contêiner:

      ```bash
      microk8s.enable registry
      export REGISTRY_ENDPOINT=localhost:32000
      ```
      {: codeblock}

   2. Instale o Docker (se ainda não estiver instalado):

      ```bash
      curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
      add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
      apt-get install docker-ce docker-ce-cli containerd.io
      ```
      {: codeblock}

   3. Defina este registro para o Docker como um registro não protegido. Crie ou inclua no **/etc/docker/daemon.json** (substituindo o valor para `$REGISTRY_ENDPOINT`):

      ```json
      {
        "insecure-registries": [ "$REGISTRY_ENDPOINT" ]
      }
      ```
      {: codeblock}

   4. Reinicie o Docker para que a mudança seja selecionada:

      ```bash
      sudo systemctl restart docker
      ```
      {: codeblock}

## O que Vem Depois

* [Instalando o Agente](edge_cluster_agent.md)
