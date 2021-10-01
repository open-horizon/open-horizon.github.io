---

copyright:
years: 2019,2020
lastupdated: "2020-01-28"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Preparación para crear un servicio periférico
{: #service_containers}

Utilice {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) para desarrollar
servicios en contenedores de {{site.data.keyword.docker}} contenedores para los
dispositivos periféricos. Puede utilizar cualesquiera base de {{site.data.keyword.linux_notm}} base, lenguajes de programación, bibliotecas o programas de utilidad apropiados para crear los servicios periféricos.
{:shortdesc}

Después de enviar, firmar y publicar los servicios, {{site.data.keyword.edge_notm}}
({{site.data.keyword.ieam}}) utiliza agentes totalmente autónomos en los dispositivos periféricos
para descargar, validar, configurar, instalar y supervisar los servicios. 

A menudo, los servicios periféricos utilizan servicios de ingestión de nube para almacenar y procesar más los resultados del análisis periférico. Este proceso incluye el flujo de trabajo del desarrollo para el código periférico y de nube.

{{site.data.keyword.ieam}} se basa en el proyecto de
[{{site.data.keyword.horizon_open}}
![Se abre en otro separador](../../images/icons/launch-glyph.svg "Se abre en otro separador")](https://github.com/open-horizon/)
de código abierto y utiliza el mandato `hzn` de
{{site.data.keyword.horizon}} {{site.data.keyword.linux_notm}} para ejecutar algunos procesos.

## Antes de empezar
{: #service_containers_begin}

1. Configure el host de desarrollo para utilizarlo con {{site.data.keyword.ieam}} instalando el agente {{site.data.keyword.horizon}} en el host y registrar el host con {{site.data.keyword.horizon_exchange}}. Consulte [Instalar el agente {{site.data.keyword.horizon}} en el dispositivo periférico y registrarlo con el ejemplo hello world](../installing/registration.md).

2. Cree un ID de [Docker Hub ![Se abre en otro separador](../../images/icons/launch-glyph.svg "Se abre en otro separador")](https://hub.docker.com/). Esto es necesario porque las instrucciones de esta sección incluyen la publicación de la imagen del contenedor de servicios en Docker Hub.

## Procedimiento
{: #service_containers_procedure}

Nota: Consulte [Convenciones utilizadas en este documento](../../getting_started/document_conventions.md)
para obtener más información sobre la sintaxis de mandato.

1. Cuando siguió los pasos de [Instalar el agente {{site.data.keyword.horizon}} en el dispositivo periférico y registrarla con el ejemplo hello world](../installing/registration.md) estableció las credenciales de Exchange. Confirme que las credenciales siguen definidas correctamente verificando que este mandato no muestra ningún error:

  ```
  hzn exchange user list
  ```
  {: codeblock}

2. Si está utilizando {{site.data.keyword.macOS_notm}} como el host de desarrollo, configure Docker para almacenar las credenciales en `~/.docker`:

   1. Abra el diálogo **Preferencias** de Docker.
   2. Desmarque **Almacenar de forma segura los inicios de sesión de Docker en la cadena de claves de Mac OS**.
  
     * Si no puede desmarcar este recuadro, siga estos pasos:
     
       1. Marque **Incluir VM en copias de seguridad de Time Machine**. 
       2. Desmarque **Almacenar de forma segura los inicios de sesión de Docker en la cadena de claves de Mac OS**.
       3. (Opcional) Desmarque **Incluir VM en copias de seguridad de Time Machine**.
       4. Pulse **Aplicar & Reiniciar**.
   3. Si tiene un archivo denominado `~/.docker/plaintext-passwords.json`, elimínelo.   

3. Inicie la sesión en Docker Hub con el ID de Docker Hub que ha creado previamente:

  ```
  export DOCKER_HUB_ID="<dockerhubid>"
  echo "<dockerhubpassword>" | docker login -u $DOCKER_HUB_ID --password-stdin
  ```
  {: codeblock}

  Ejemplo de salida:
  ```
  ¡AVISO! La contraseña se almacenará sin cifrar en ~userName/.docker/config.json. Configure un ayudante de credencial para eliminar este aviso. Consulte https://docs.docker.com/engine/reference/commandline/login/#credentials-store

  Inicio de sesión satisfactorio
  ```

4. Cree un par de claves de firma criptográfica. Esto le permite firmar servicios al publicarlos en Exchange. 

   Nota: Solo tiene que realizar este paso una vez.

  ```
  hzn key create "<companyname>" "<youremailaddress>"
  ```
  {: codeblock}
  
  Donde `companyname` se utiliza como la organización x509 y `youremailaddress` se utiliza como x509 CN.

5. Instale unas pocas herramientas de desarrollo:

  En **{{site.data.keyword.linux_notm}}**:

  ```
  sudo apt install -y git jq make
  ```
  {: codeblock}

  En **{{site.data.keyword.macOS_notm}}**:

  ```
  brew install git jq make
  ```
  {: codeblock}
  
  Nota: Consulte [homebrew ![Se abre en otro separador](../../images/icons/launch-glyph.svg "Se abre en otro separador")](https://brew.sh/) para obtener detalles sobre
la instalación de brew si es necesario.

## Qué hacer a continuación
{: #service_containers_what_next}

Utilice las credenciales y la clave de firma para completar los ejemplos de desarrollo. Estos ejemplos le muestran cómo crear servicios periféricos simples y aprender los conceptos básicos para el desarrollo de {{site.data.keyword.edge_devices_notm}}.
