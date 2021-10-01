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

# Preparación de un clúster periférico
{: #preparing_edge_cluster}

Realice las siguientes tareas para instalar un clúster periférico y prepararlo para el agente de
{{site.data.keyword.edge_notm}}:

* Instale uno de estos tipos de clústeres periféricos:
  * [Instalar un clúster periférico de OCP](#install_ocp_edge_cluster)
  * [Instalar y configurar un clúster periférico k3s](#install_k3s_edge_cluster)
  * [Instalar y configurar un clúster periférico microk8s](#install_microk8s_edge_cluster) (para desarrollo y prueba, no recomendado para producción)
* [Recopile la información y los archivos necesarios para los clústeres periféricos](#gather_info)

## Instalar un clúster periférico de OCP
{: #install_ocp_edge_cluster}

1. Instale OCP siguiendo las instrucciones de instalación en la documentación de
[{{site.data.keyword.open_shift_cp}}{{site.data.keyword.open_shift_cp}}
![Se abre en otro separador](../../images/icons/launch-glyph.svg "Se abre en otro separador")](https://docs.openshift.com/container-platform/4.4/welcome/index.html).

2. Instale la CLI de Kubenetes (**kubectl**) y la CLI del cliente de Openshift
(**oc**) en el host de administración desde el que administra el clúster de OCP
(el mismo host desde el que ejecutará el script de instalación de agente). Consulte
[Instalación de cloudctl, kubectl y oc](../installing/cloudctl_oc_cli.md).

## Instalar y configurar un clúster periférico k3s
{: #install_k3s_edge_cluster}

Esta sección proporciona un resumen de cómo instalar k3s (rancher), un clúster de Kubernetes ligero y pequeño,
en Ubuntu 18.04. (Para obtener instrucciones más detalladas, consulte la
[documentación de k3s ![Se abre en otro separador](../../images/icons/launch-glyph.svg "Se abre en otro separador")](https://rancher.com/docs/k3s/latest/en/).)

1. Inicie la sesión como **root** o elévese a **root**
con `sudo -i`

2. Instale k3s:

   ```bash
   curl -sfL https://get.k3s.io | sh -
   ```
   {: codeblock}

3. Cree el servicio de registro de imágenes:

   1. Cree un archivo denominado **k3s-registry-deployment.yml** con este contenido:

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
              emptyDir: {} # FIXME: convertirlo en volumen persistente si se utiliza en producción
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

   2. Cree el servicio de registro:

      ```bash
      kubectl apply -f k3s-registry-deployment.yml
      ```
      {: codeblock}

   3. Verifique que se ha creado el servicio:

      ```bash
      kubectl get deployment
      kubectl get service
      ```
      {: codeblock}

   4. Defina el punto final de registro:

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

   5. Reinicie k3s para seleccionar el cambio en **/etc/rancher/k3s/registries.yaml**:

      ```bash
      systemctl restart k3s
      ```
      {: codeblock}

4. Defina este registro en docker como un registro no seguro:

   1. Créelo o añádalo a **/etc/docker/daemon.json** (sustituyendo el valor
por `$REGISTRY_ENDPOINT`):

      ```json
      {
        "insecure-registries": [ "$REGISTRY_ENDPOINT" ]
      }
      ```
      {: codeblock}

   2. Reinicie docker para seleccionar el cambio:

      ```bash
      systemctl restart docker
      ```
      {: codeblock}

## Instalar y configurar un clúster periférico microk8s
{: #install_microk8s_edge_cluster}

Esta sección proporciona un resumen de cómo instalar microk8s, un clúster de Kubernetes ligero y pequeño,
en Ubuntu 18.04. (Para obtener instrucciones más detalladas, consulte la [documentación
de microk8s ![Se abre en otro separador](../../images/icons/launch-glyph.svg "Se abre en otro separador")](https://microk8s.io/docs).)

Nota: Este tipo de clúster periférico está pensado para desarrollo y prueba, ya que un único clúster kubernetes
de nodo de trabajador no proporciona escalabilidad o alta disponibilidad.

1. Instale microk8s:

   ```bash
   sudo snap install microk8s --classic --channel=stable
   ```
   {: codeblock}

2. Si no está ejecutando como **root**, añada el usuario al grupo
**microk8s**:

   ```bash
   sudo usermod -a -G microk8s $USER
   sudo chown -f -R $USER ~/.kube
   su - $USER   # crear sesión nueva para que se produzca la actualización de grupo
   ```
   {: codeblock}

3. Habilite dns y módulos de almacenamiento en microk8s:

   ```bash
   microk8s.enable dns
   microk8s.enable storage
   ```
   {: codeblock}

4. Compruebe el estado:

   ```bash
   microk8s.status --wait-ready
   ```
   {: codeblock}

5. El mandato kubectl de microK8s se denomina **microk8s.kubectl**
para evitar conflictos con un mandato **kubectl** ya instalado. Suponiendo que todavía no tiene instalado
**kubectl**, añada este alias para **microk8s.kubectl**.

   ```bash
   echo 'alias kubectl=microk8s.kubectl' >> ~/.bash_aliases
   source ~/.bash_aliases
   ```
   {: codeblock}

6. Habilite el registro de contenedor y configure docker para tolerar el registro inseguro:

   1. Habilite el registro de contenedor:

      ```bash
      microk8s.enable registry
      export REGISTRY_ENDPOINT=localhost:32000
      ```
      {: codeblock}

   2. Instale docker (si todavía no está instalado):

      ```bash
      curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
      add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
      apt-get install docker-ce docker-ce-cli containerd.io
      ```
      {: codeblock}

   3. Defina este registro en docker como un registro no seguro. Créelo o añádalo
a **/etc/docker/daemon.json** (sustituyendo el valor
por `$REGISTRY_ENDPOINT`):

      ```json
      {
        "insecure-registries": [ "$REGISTRY_ENDPOINT" ]
      }
      ```
      {: codeblock}

   4. Reinicie docker para seleccionar el cambio:

      ```bash
      sudo systemctl restart docker
      ```
      {: codeblock}

## Qué hacer a continuación

* [Instalación del agente](edge_cluster_agent.md)
