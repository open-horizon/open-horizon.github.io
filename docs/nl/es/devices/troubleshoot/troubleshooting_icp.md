---

copyright:
years: 2019
lastupdated: "2019-09-18"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Sugerencias de resolución de problemas en el entorno {{site.data.keyword.icp_notm}}
{: #troubleshooting_icp}

Consulte este contenido para ayudarle a resolver problemas comunes en los entornos {{site.data.keyword.icp_notm}} relacionados con {{site.data.keyword.edge_devices_notm}}. Las sugerencias y guías de cada pregunta pueden ayudarle a resolver problemas comunes y obtener información para identificar las causas raíz.
{:shortdesc}

   * [¿Se han configurado correctamente las credenciales de {{site.data.keyword.edge_devices_notm}} para su uso en el entorno {{site.data.keyword.icp_notm}}?](#setup_correct)

### ¿Se han configurado correctamente las credenciales de {{site.data.keyword.edge_devices_notm}} para su uso en el entorno {{site.data.keyword.icp_notm}}?
{: #setup_correct}

Necesita una cuenta de usuario de {{site.data.keyword.icp_notm}} para completar cualquier acción dentro de {{site.data.keyword.edge_devices_notm}} en este entorno. También necesita una clave de API creada desde esa cuenta.

Para verificar las credenciales de {{site.data.keyword.edge_devices_notm}} en este entorno, ejecute este mandato:

   ```
   hzn exchange user list
   ```
   {: codeblock}

Si se devuelve desde Exchange una entrada con formato JSON que muestra uno o más usuarios, las credenciales de {{site.data.keyword.edge_devices_notm}} se han configurado correctamente.

Si se devuelve una respuesta de error, puede realizar pasos para solucionar los problemas de configuración de las credenciales.

Si el mensaje de error indica una clave de API incorrecta, puede crear una nueva clave de API que utilice los mandatos siguientes.

**Nota:** en primer lugar, establezca los valores adecuados para todas las variables de entorno que están precedidas por `$` en estos mandatos:

   ```
   cloudctl login -a $ICP_URL -u $USER -p $PW -n kube-public --skip-ssl-validation
   cloudctl iam api-key-create "$KEY_NAME" -d "$KEY_DESC"
   ```
   {: codeblock}

Si el mensaje de error indica que el certificado no es válido, utilice este mandato para crear un nuevo certificado autofirmado:

   ```
   kubectl -n kube-public get secret ibmcloud-cluster-ca-cert -o jsonpath="{.data['ca\.crt']}" | base64 --decode > icp.crt
   ```
   {: codeblock}

A continuación, indique al sistema operativo que debe confiar en este certificado. En una máquina Linux, ejecute este mandato:

   ```
   sudo cp icp.crt /usr/local/share/ca-certificates &&  sudo update-ca-certificates
   ````
   {: codeblock}

En una máquina MacOS, ejecute este mandato:

   ```
   sudo security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain icp.crt
   ```
   {: codeblock}
