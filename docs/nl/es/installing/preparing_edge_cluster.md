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

Realice las siguientes tareas para instalar un clúster periférico y prepararlo para el agente de {{site.data.keyword.edge_notm}}:

Instale uno de estos clústeres periféricos y prepárelo para el agente de {{site.data.keyword.edge_notm}}:
* [Instalar un clúster periférico de OCP](#install_ocp_edge_cluster)
* [Instalar y configurar un clúster periférico k3s](#install_k3s_edge_cluster)
* [Instalar y configurar un clúster periférico microk8s](#install_microk8s_edge_cluster) (para desarrollo y prueba, no recomendado para producción)

## Instalar un clúster periférico de OCP
{: #install_ocp_edge_cluster}

1. Instale OCP siguiendo las instrucciones de instalación de la [Documentación de {{site.data.keyword.open_shift_cp}}](https://docs.openshift.com/container-platform/4.6/welcome/index.html). ({{site.data.keyword.ieam}} sólo soporta OCP en plataformas x86_64.)

2. Instale la CLI de Kubernetes (**kubectl**), la CLI del cliente de Openshift (**oc**) y Docker en el host del administrador en el que se administra el clúster periférico de OCP. Es el mismo host en el que se ejecuta el script de instalación del agente. Para obtener más información, consulte [Instalación de cloudctl, kubectl y oc](../cli/cloudctl_oc_cli.md).

## Instalar y configurar un clúster periférico k3s
{: #install_k3s_edge_cluster}

En este contenido se proporciona un resumen de cómo instalar k3s (rancher), un clúster de Kubernetes ligero y pequeño, en Ubuntu 18.04. Para obtener más información, consulte la [documentación de k3s](https://rancher.com/docs/k3s/latest/en/).

**Nota**: Si está instalado, desinstale kubectl antes de completar los pasos siguientes.

1. Inicie la sesión como **root** o elévese a **root** con `sudo -i`

2. El nombre de host completo de la máquina debe contener al menos dos puntos. Compruebe el nombre de host completo:

   ```bash
   hostname
   ```
    {: codeblock}

   Si el nombre de host completo de la máquina contiene menos de dos puntos, cambie el nombre de host:

   ```bash
   hostnamectl set-hostname <nuevo-nombre-host-con-2-puntos>
   ```
   {: codeblock}

   Para obtener más información, consulte [Problema de github](https://github.com/rancher/k3s/issues/53).

3. Instale k3s:

   ```bash
   curl -sfL https://get.k3s.io | sh -
   ```
   {: codeblock}

4. Cree el servicio de registro de imágenes:
   1. Cree un archivo denominado **k3s-persistent-claim.yml** con este contenido:
      ```yaml       apiVersion: v1       kind: PersistentVolumeClaim       metadata:         name: docker-registry-pvc       spec:         storageClassName: "local-path"         accessModes:
          - ReadWriteOnce         resources:           requests:             storage: 10Gi
      ```
      {: codeblock}

   2. Cree la reclamación de volumen persistente:

      ```bash
      kubectl apply -f k3s-persistent-claim.yml
      ```
      {: codeblock}

   3. Verifique que la reclamación de volumen persistente se ha creado y está en estado "Pendiente"

      ```bash
      kubectl get pvc
      ```
      {: codeblock}

   4. Cree un archivo denominado **k3s-registry-deployment.yml** con este contenido:

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

   5. Cree el despliegue de registro y servicio:

      ```bash
      kubectl apply -f k3s-registry-deployment.yml
      ```
      {: codeblock}

   6. Verifique que se ha creado el servicio:

      ```bash
      kubectl get deployment       kubectl get service
      ```
      {: codeblock}

   7. Defina el punto final de registro:

      ```bash
      export REGISTRY_ENDPOINT=$(kubectl get service docker-registry-service | grep docker-registry-service | awk '{print $3;}'):5000       cat << EOF >> /etc/rancher/k3s/registries.yaml       mirrors:         "$REGISTRY_ENDPOINT":           endpoint:
            - "http://$REGISTRY_ENDPOINT"       EOF
      ```
      {: codeblock}

   8. Reinicie k3s para seleccionar el cambio en **/etc/rancher/k3s/registries.yaml**:

      ```bash
      systemctl restart k3s
      ```
      {: codeblock}

5. Defina este registro en docker como un registro no seguro:

   1. Créelo o añádalo a **/etc/docker/daemon.json** (sustituyendo `<registry-endpoint>` por el valor de la variable de entorno `$REGISTRY_ENDPOINT` que ha obtenido en un paso anterior).

      ```json
      {
        "insecure-registries": [ "<registry-endpoint>" ]       }
      ```
      {: codeblock}

   2. (opcional) Si es necesario, verifique que docker está en la máquina:

      ```bash
      curl -fsSL get.docker.com | sh
      ```
      {: codeblock}     

   3. Reinicie docker para seleccionar el cambio:

      ```bash
      systemctl restart docker
      ```
      {: codeblock}

## Instalar y configurar un clúster periférico microk8s
{: #install_microk8s_edge_cluster}

En este contenido se proporciona un resumen de cómo instalar microk8s, un clúster de Kubernetes ligero y pequeño, en Ubuntu 18.04. (Para obtener instrucciones más detalladas, consulte la [documentación de microk8s](https://microk8s.io/docs).)

**Nota:** Este tipo de clúster periférico está pensado para desarrollo y prueba, ya que un único clúster de Kubernetes de nodo de trabajador no proporciona escalabilidad ni alta disponibilidad.

1. Instale microk8s:

   ```bash
   sudo snap install microk8s --classic --channel=stable
   ```
   {: codeblock}

2. Si no está ejecutando como **root**, añada el usuario al grupo **microk8s**:

   ```bash
   sudo usermod -a -G microk8s $USER    sudo chown -f -R $USER ~/.kube    su - $USER   # crear sesión nueva para que se produzca la actualización de grupo
   ```
   {: codeblock}

3. Habilite dns y módulos de almacenamiento en microk8s:

   ```bash
   microk8s.enable dns    microk8s.enable storage
   ```
   {: codeblock}

   **Nota**: Microk8s utiliza `8.8.8.8` y `8.8.4.4` como nombres de servidores ascendentes de forma predeterminada. Si estos nombres de servidores no pueden resolver el nombre de host del centro de gestión, debe cambiar los servidores de nombres que microk8s está utilizando:
   
   1. Recupere la lista de nombres de servidores ascendentes en `/etc/resolv.conf` o `/run/systemd/resolve/resolv.conf`.

   2. Edite el mapa de configuración `coredns` en el espacio de nombres `kube-system`. Establezca los servidores de nombres ascendentes en la sección de `reenvío`.
   
      ```bash
      microk8s.kubectl edit -n kube-system cm/coredns
      ```
      {: codeblock}
   
   3. Para obtener más información sobre el DNS de Kubernetes, consulte la [documentación de Kubernetes](https://kubernetes.io/docs/tasks/administer-cluster/dns-custom-nameservers/).


4. Compruebe el estado:

   ```bash
   microk8s.status --wait-ready
   ```
   {: codeblock}

5. El mandato kubectl de microK8s se denomina **microk8s.kubectl** para evitar conflictos con un mandato **kubectl** ya instalado. Suponiendo que **kubectl** no esté instalado, añada este alias para **microk8s.kubectl**:

   ```bash
   echo 'alias kubectl=microk8s.kubectl' >> ~/.bash_aliases    source ~/.bash_aliases
   ```
   {: codeblock}

6. Habilite el registro de contenedor y configure docker para tolerar el registro inseguro:

   1. Habilite el registro de contenedor:

      ```bash
      microk8s.enable registry       export REGISTRY_ENDPOINT=localhost:32000
      ```
      {: codeblock}

   2. Instale docker (si todavía no está instalado):

      ```bash
      curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -       add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"       apt-get install docker-ce docker-ce-cli containerd.io
      ```
      {: codeblock}

   3. Defina este registro como inseguro para docker. Créelo
o añádalo a **/etc/docker/daemon.json** (sustituyendo
`<registry-endpoint>` por el valor de la variable de entorno
`$REGISTRY_ENDPOINT` que ha obtenido en un paso anterior).

      ```json
      {
        "insecure-registries": [ "<registry-endpoint>" ]
      }
      ```
      {: codeblock}

   4. (opcional) Verifique que docker está en la máquina:

      ```bash
      curl -fsSL get.docker.com | sh
      ```
      {: codeblock}   

   5. Reinicie docker para seleccionar el cambio:

      ```bash
      sudo systemctl restart docker
      ```
      {: codeblock}

## Qué hacer a continuación

* [Instalación del agente](edge_cluster_agent.md)
