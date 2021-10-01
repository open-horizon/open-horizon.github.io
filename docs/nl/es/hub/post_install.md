---

copyright:
years: 2020
lastupdated: "2020-10-28"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Configuración posterior a la instalación

## Requisitos previos

* [CLI de IBM Cloud Pak (**cloudctl**) y CLI de cliente de OpenShift (**oc**)](../cli/cloudctl_oc_cli.md)
* [**jq**](https://stedolan.github.io/jq/download/)
* [**git**](https://git-scm.com/downloads)
* [**docker**](https://docs.docker.com/get-docker/) versión 1.13 o posterior
* **make**

## Verificación de la instalación

1. Siga los pasos del tema sobre [Instalar {{site.data.keyword.ieam}}](online_installation.md)
2. Asegúrese de que todos los pods del espacio de nombres de {{site.data.keyword.ieam}} están en el estado **Running** (en ejecución) o **Completed** (completados):

   ```
   oc get pods
   ```
   {: codeblock}

   Este es un ejemplo de lo que se debe ver con las bases de datos locales y el gestor de secretos local instalado. Se esperan algunos reinicios de inicialización, normalmente varios reinicios indican un problema.
   ```
   $ oc get pods    NAME                                           READY   STATUS      RESTARTS   AGE    create-agbotdb-cluster-j4fnb                   0/1     Completed   0          88m    create-exchangedb-cluster-hzlxm                0/1     Completed   0          88m    ibm-common-service-operator-68b46458dc-nv2mn   1/1     Running     0          103m    ibm-eamhub-controller-manager-7bf99c5fc8-7xdts 1/1     Running     0          103m    ibm-edge-agbot-5546dfd7f4-4prgr                1/1     Running     0          81m    ibm-edge-agbot-5546dfd7f4-sck6h                1/1     Running     0          81m    ibm-edge-agbotdb-keeper-0                      1/1     Running     0          88m    ibm-edge-agbotdb-keeper-1                      1/1     Running     0          87m    ibm-edge-agbotdb-keeper-2                      1/1     Running     0          86m    ibm-edge-agbotdb-proxy-7447f6658f-7wvdh        1/1     Running     0          88m    ibm-edge-agbotdb-proxy-7447f6658f-8r56d        1/1     Running     0          88m    ibm-edge-agbotdb-proxy-7447f6658f-g4hls        1/1     Running     0          88m    ibm-edge-agbotdb-sentinel-5766f666f4-5qm9x     1/1     Running     0          88m    ibm-edge-agbotdb-sentinel-5766f666f4-5whgr     1/1     Running     0          88m    ibm-edge-agbotdb-sentinel-5766f666f4-9xjpr     1/1     Running     0          88m    ibm-edge-css-5c59c9d6b6-kqfnn                  1/1     Running     0          81m    ibm-edge-css-5c59c9d6b6-sp84w                  1/1     Running     0          81m
   ibm-edge-css-5c59c9d6b6-wf84s                  1/1     Running     0          81m    ibm-edge-cssdb-server-0                        1/1     Running     0          88m    ibm-edge-exchange-b6647db8d-k97r8              1/1     Running     0          81m    ibm-edge-exchange-b6647db8d-kkcvs              1/1     Running     0          81m    ibm-edge-exchange-b6647db8d-q5ttc              1/1     Running     0          81m    ibm-edge-exchangedb-keeper-0                   1/1     Running     1          88m    ibm-edge-exchangedb-keeper-1                   1/1     Running     0          85m    ibm-edge-exchangedb-keeper-2                   1/1     Running     0          84m    ibm-edge-exchangedb-proxy-6bbd5b485-cx2v8      1/1     Running     0          88m    ibm-edge-exchangedb-proxy-6bbd5b485-hs27d      1/1     Running     0          88m    ibm-edge-exchangedb-proxy-6bbd5b485-htldr      1/1     Running     0          88m    ibm-edge-exchangedb-sentinel-6d685bf96-hz59z   1/1     Running     1          88m    ibm-edge-exchangedb-sentinel-6d685bf96-m4bdh   1/1     Running     0          88m    ibm-edge-exchangedb-sentinel-6d685bf96-mxv2b   1/1     Running     1          88m    ibm-edge-sdo-0                                 1/1     Running     0          81m    ibm-edge-ui-545d694f6c-4rnrf                   1/1     Running     0          81m    ibm-edge-ui-545d694f6c-97ptz                   1/1     Running     0          81m    ibm-edge-ui-545d694f6c-f7bf6                   1/1     Running     0          81m
   ibm-edge-vault-0                               1/1     Running     0          81m    ibm-edge-vault-bootstrap-k8km9                 0/1     Completed   0          80m
   ```
   {: codeblock}

   **Notas**:
   * Para obtener más información sobre los pods que están en el estado **Pending** (pendiente) debido a problemas de recursos o de planificación, consulte la página de [dimensionamiento del clúster](cluster_sizing.md). Incluye información sobre cómo reducir los costes de planificación de componentes.
   * Para obtener información sobre cualquier otro error, consulte [resolución de problemas](../admin/troubleshooting.md).
3. Asegúrese de que todos los pods del espacio de nombres **ibm-common-services** están en estado **Running** o **Completed**:

   ```
   oc get pods -n ibm-common-services
   ```
   {: codeblock}

4. Inicie sesión, saque y extraiga el paquete de agentes con la clave de titularidad a través del [Registro autorizado](https://myibm.ibm.com/products-services/containerlibrary):
    ```
    docker login cp.icr.io --username cp &amp;TWBAMP;&amp;TWBAMP; \     docker rm -f ibm-eam-{{site.data.keyword.semver}}-bundle; \     docker create --name ibm-eam-{{site.data.keyword.semver}}-bundle cp.icr.io/cp/ieam/ibm-eam-bundle:{{site.data.keyword.anax_ver}} bash &amp;TWBAMP;&amp;TWBAMP; \     docker cp ibm-eam-{{site.data.keyword.semver}}-bundle:/ibm-eam-{{site.data.keyword.semver}}-bundle.tar.gz ibm-eam-{{site.data.keyword.semver}}-bundle.tar.gz &amp;TWBAMP;&amp;TWBAMP; \     tar -zxvf ibm-eam-{{site.data.keyword.semver}}-bundle.tar.gz &amp;TWBAMP;&amp;TWBAMP; \     cd ibm-eam-{{site.data.keyword.semver}}-bundle/tools
    ```
    {: codeblock}
5. Valide el estado de instalación:
    ```
    ./service_healthcheck.sh
    ```
    {: codeblock}

    Consulte la salida de ejemplo siguiente:
    ```
    $ ./service_healthcheck.sh     ==Running service verification tests for IBM Edge Application Manager==     SUCCESS: IBM Edge Application Manager Exchange API is operational     SUCCESS: IBM Edge Application Manager Cloud Sync Service is operational     SUCCESS: IBM Edge Application Manager Agbot database heartbeat is current     SUCCESS: IBM Edge Application Manager SDO API is operational     SUCCESS: IBM Edge Application Manager UI is properly requiring valid authentication     ==All expected services are up and running==
    ```

   * Si hay anomalías de mandato **service_healthcheck.sh**, si experimenta problemas al ejecutar los mandatos siguientes o si hay problemas durante el tiempo de ejecución, consulte [resolución de problemas](../admin/troubleshooting.md).

## Configuración posterior a la instalación
{: #postconfig}

El proceso siguiente debe ejecutarse en un host que soporte la instalación de la CLI **hzn**, que actualmente se puede instalar en un host Linux basado en Debian/apt, amd64 Red Hat/rpm Linux o macOS. Estos pasos utilizan el mismo soporte descargado desde PPA en la sección de verificación de la instalación.

1. Instale la CLI **hzn** utilizando las instrucciones para la plataforma soportada:
  * Vaya al directorio **agent** y desempaquete los archivos de agente:
    ```
    cd ibm-eam-{{site.data.keyword.semver}}-bundle/agent &amp;TWBAMP;&amp;TWBAMP; \ tar -zxvf edge-packages-{{site.data.keyword.semver}}.tar.gz
    ```
    {: codeblock}

    * Ejemplo de Debian {{site.data.keyword.linux_notm}}:
      ```
      sudo apt-get install ./edge-packages-{{site.data.keyword.semver}}/linux/deb/amd64/horizon-cli*.deb
      ```
      {: codeblock}

    * Ejemplo de Red Hat {{site.data.keyword.linux_notm}}:
      ```
      sudo dnf install -yq ./edge-packages-{{site.data.keyword.semver}}/linux/rpm/x86_64/horizon-cli-*.x86_64.rpm
      ```
      {: codeblock}

    * Ejemplo de macOS:
      ```
      sudo security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain edge-packages-{{site.data.keyword.semver}}/macos/pkg/x86_64/horizon-cli.crt && \       sudo installer -pkg edge-packages-{{site.data.keyword.semver}}/macos/pkg/x86_64/horizon-cli-*.pkg -target /
      ```
      {: codeblock}

2. Ejecute el script posterior a la instalación. Este script realiza toda la inicialización necesaria para crear la primera organización. (Las organizaciones son cómo {{site.data.keyword.ieam}} separa los recursos y los usuarios para habilitar la multitenencia. Inicialmente, esta primera organización es suficiente. Puede configurar más organizaciones más adelante. Para obtener más información, consulte [Multitenencia](../admin/multi_tenancy.md).

   **Nota**: **IBM** y **root** son organizaciones de uso interno y no se pueden elegir como su organización inicial. Un nombre de organización no puede contener caracteres de subrayado (_), comas (,), espacios en blanco (), comillas simples (') o signos de interrogación (?).

   ```
   ./post_install.sh <elija-nombre-su-org>
   ```
   {: codeblock}

3. Ejecute el siguiente mandato para ver el enlace de la consola de gestión de {{site.data.keyword.ieam}} para la instalación:
   ```
   echo https://$(oc get cm management-ingress-ibmcloud-cluster-info -o jsonpath='{.data.cluster_ca_domain}')/edge
   ```
   {: codeblock}

## Autenticación 

La autenticación de usuario es necesaria para acceder a la consola de gestión de {{site.data.keyword.ieam}}. Esta instalación ha creado una cuenta de administrador inicial que se puede indicar mediante el mandato siguiente:
```
echo "$(oc -n ibm-common-services get secret platform-auth-idp-credentials -o jsonpath='{.data.admin_username}' | base64 --decode) // $(oc -n ibm-common-services get secret platform-auth-idp-credentials -o jsonpath='{.data.admin_password}' | base64 --decode)"
```
{: codeblock}

Puede utilizar esta cuenta de administrador para la autenticación inicial y, además, [configurar LDAP](https://www.ibm.com/support/knowledgecenter/SSHKN6/iam/3.x.x/configure_ldap.html) accediendo al enlace de la consola de gestión indicado por el siguiente mandato:
```
echo https://$(oc get cm management-ingress-ibmcloud-cluster-info -o jsonpath='{.data.cluster_ca_domain}')
```
{: codeblock}

Después de establecer una conexión LDAP, cree un equipo, otorgue a ese equipo acceso al espacio de nombres en el que se ha desplegado el operador de {{site.data.keyword.edge_notm}} y añada usuarios a dicho equipo. Esto otorga a los usuarios individuales el permiso para crear claves de API.

Las claves de API se utilizan para la autenticación con la CLI de {{site.data.keyword.edge_notm}}. Los permisos asociados a las claves de API son idénticos a los del usuario con el que se generan.

Aunque no haya creado una conexión LDAP, puede crear claves de API utilizando las credenciales de administrador iniciales, pero tenga en cuenta que la clave de API tendrá privilegios de **Administrador de clústeres**.

## Qué hacer a continuación

Siga el proceso detallado en la página [Recopilar archivos de nodo periférico](gather_files.md) para preparar el soporte de instalación para los nodos periféricos.
