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

# Instalación y registro del agente de SDO
{: #sdo}

La tecnología [SDO](https://software.intel.com/en-us/secure-device-onboard) (Incorporación segura de dispositivos), creada por Intel, facilita la configuración segura de dispositivos periféricos y su asociación con un centro de gestión periférico. {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) da soporte a dispositivos habilitados para SDO para que el agente se instale en los dispositivos y se registre en el centro de gestión de {{site.data.keyword.ieam}} con toque cero (simplemente encendiendo los dispositivos).

## Visión general de SDO
{: #sdo-overview}

SDO consta de estos componentes:

* El módulo SDO en el dispositivo periférico (normalmente instalado allí por el fabricante de dispositivo)
* Un cupón de propiedad (un archivo que se proporciona al comprador del dispositivo junto con el dispositivo físico)
* El servidor de encuentro SDO (el servidor conocido con el que un dispositivo habilitado para SDO se pone en contacto por primera vez cuando se inicia por primera vez)
* Servicios de propietario de SDO (servicios ejecutados en el centro de gestión de {{site.data.keyword.ieam}} que configuran el dispositivo para utilizar esta instancia específica de {{site.data.keyword.ieam}})

**Nota**: SDO solo da soporte a dispositivos periféricos, no clústeres periféricos.

### Flujo de SDO

<img src="../OH/docs/images/edge/09_SDO_device_provisioning.svg" style="margin: 3%" alt="SDO installation overview">

## Antes de empezar
{: #before_begin}

SDO requiere que los archivos del agente estén almacenados en {{site.data.keyword.ieam}} Cloud Sync Service (CSS). Si esto no se ha hecho, solicite al administrador que ejecute los siguientes mandatos, tal como se describe en [Recopilar archivos de nodo periférico](../hub/gather_files.md):

  `edgeNodeFiles.sh ALL -c ...`

## Prueba de SDO
{: #trying-sdo}

Antes de comprar dispositivos periféricos habilitados para SDO, puede probar el soporte SDO en {{site.data.keyword.ieam}} con una VM que simule un dispositivo habilitado para SDO:

1. Necesita una clave de API. Consulte [Creación de la clave de API](../hub/prepare_for_edge_nodes.md) para obtener instrucciones sobre cómo crear una clave de API, si todavía no tiene una.

2. Póngase en contacto con el administrador de {{site.data.keyword.ieam}} para obtener los valores de estas variables de entorno. (Los necesitará en el siguiente paso.)

   ```bash
   export HZN_ORG_ID=<org-exchange>    export HZN_EXCHANGE_USER_AUTH=iamapikey:<clave-api>    export HZN_SDO_SVC_URL=https://<ingreso-centro-gestión-ieam>/edge-sdo-ocs/api    export HZN_MGMT_HUB_CERT_PATH=<vía_acceso-a-certificado-autofirmado-centro-gestión>    export CURL_CA_BUNDLE=$HZN_MGMT_HUB_CERT_PATH
   ```

3. Siga los pasos del [repositorio open-horizon/SDO-support](https://github.com/open-horizon/SDO-support/blob/master/README-1.10.md) para observar que SDO instala automáticamente el agente {{site.data.keyword.ieam}} en un dispositivo y lo registra en el centro de gestión de {{site.data.keyword.ieam}}.

## Adición de dispositivos habilitados para SDO al dominio de {{site.data.keyword.ieam}}
{: #using-sdo}

Si ha comprado dispositivos habilitados para SDO y desea incorporarlos al dominio de {{site.data.keyword.ieam}}:

1. [Inicie la sesión en la consola de gestión de {{site.data.keyword.ieam}}](../console/accessing_ui.md).

2. En el separador **Nodos**, pulse **Añadir nodo**. 

   Especifique la información necesaria para crear una clave de propiedad privada en el servicio SDO y descargue la clave pública correspondiente.
   
3. Rellene la información necesaria para importar los cupones de propiedad que ha recibido al comprar los dispositivos.

4. Conecte los dispositivos a la red y enciéndalos.

5. De nuevo en la consola de gestión, observe el progreso de los dispositivos a medida que se ponen en línea visualizando la página de visión general de **Nodo** y filtrando el nombre de la instalación.
