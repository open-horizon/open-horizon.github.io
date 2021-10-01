---

copyright:
years: 2020
lastupdated: "2020-10-13"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Creación de la clave de API
{: #prepare_for_edge_nodes}

En este contenido se explica cómo crear una clave de API y obtener algunos archivos y valores de variables de entorno que son necesarios al configurar nodos periféricos. Realice estos pasos en un host que se pueda conectar al clúster de centro de gestión de {{site.data.keyword.ieam}}.

## Antes de empezar

* Si todavía no ha instalado **cloudctl**, consulte [Instalación de cloudctl, oc y kubectl](../cli/cloudctl_oc_cli.md) para hacerlo.
* Póngase en contacto con el administrador de {{site.data.keyword.ieam}} para obtener la información que necesita para iniciar la sesión en el centro de gestión mediante **cloudctl**.

## Procedimiento

Si ha configurado una conexión LDAP, puede utilizar las credenciales de usuario añadidas para iniciar la sesión y crear claves de API, o bien utilizar las credenciales de administrador iniciales indicadas mediante el siguiente mandato:
```
echo "$(oc -n ibm-common-services get secret platform-auth-idp-credentials -o jsonpath='{.data.admin_username}' | base64 --decode) // $(oc -n ibm-common-services get secret platform-auth-idp-credentials -o jsonpath='{.data.admin_password}' | base64 --decode)"
```
{: codeblock}

1. Utilice `cloudctl` para iniciar la sesión en el centro de gestión de {{site.data.keyword.ieam}}. Especifique el usuario para el que desea crear una clave de API:

   ```bash
   cloudctl login -a <url-clúster> -u <usuario> -p <contraseña> --skip-ssl-validation
   ```
   {: codeblock}

2. Cada usuario que está configurando nodos periféricos debe tener una clave de API. Puede utilizar la misma clave de API para configurar todos los nodos periféricos (no se guarda en los nodos periféricos). Cree una clave de API:

   ```bash
   cloudctl iam api-key-create "<elija-un-nombre-de-clave-de-API>" -d "<elija-una-descripción-de-clave-de-API>"
   ```
   {: codeblock}

   Busque el valor de clave en la salida de mandato; es la línea que empieza por **API Key**. Guarde el valor de clave para utilizarlo en el futuro, porque posteriormente no podrá consultarlo en el sistema.

3. Póngase en contacto con el administrador de {{site.data.keyword.ieam}} para obtener ayuda para establecer estas variables de entorno:

  ```bash
  export HZN_EXCHANGE_USER_AUTH=iamapikey:<clave-api>   export HZN_ORG_ID=<su-organización-exchange>   mgmtHubIngress=$(oc get cm management-ingress-ibmcloud-cluster-info -o jsonpath='{.data.cluster_ca_domain}')   export HZN_FSS_CSSURL=https://$mgmtHubIngress/edge-css/   echo "export HZN_FSS_CSSURL=$HZN_FSS_CSSURL"
  ```
  {: codeblock}

## Qué hacer a continuación

Cuando esté preparado para configurar nodos periféricos, siga los pasos de [Instalación de nodos periféricos](../installing/installing_edge_nodes.md).

