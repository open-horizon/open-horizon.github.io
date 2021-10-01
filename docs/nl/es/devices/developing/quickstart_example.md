---

copyright:
years: 2019
lastupdated: "2019-06-24"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Empaquete un contenedor Docker existente como un servicio periférico
{: #quickstart_ex}

Este ejemplo le guía a través de los pasos para publicar un contenedor Docker existente como un servicio periférico, crear un patrón de despliegue asociado y registrar los nodos periféricos para ejecutar dicho patrón de despliegue.
{:shortdesc}

## Antes de empezar
{: #quickstart_ex_begin}

Complete los pasos de requisito previo en [Preparación para crear un servicio periférico](service_containers.md). Como resultado, estas variables de entorno se deben establecer, estos mandatos deben estar instalados y estos archivos deben existir.
```
echo "HZN_ORG_ID=$HZN_ORG_ID, HZN_EXCHANGE_USER_AUTH=$HZN_EXCHANGE_USER_AUTH, DOCKER_HUB_ID=$DOCKER_HUB_ID"
which git jq
ls ~/.hzn/keys/service.private.key ~/.hzn/keys/service.public.pem
cat /etc/default/horizon
```
{: codeblock}

## Procedimiento
{: #quickstart_ex_procedure}

Nota: Consulte [Convenciones utilizadas en este documento](../getting_started/document_conventions.md)
para obtener más información sobre la sintaxis de mandato.

1. Cree un directorio de proyecto.

  1. En el host de desarrollo, vaya al directorio del proyecto Docker existente. **Si no tiene un proyecto Docker existente, pero sigue deseando continuar con este ejemplo**, utilice estos mandatos para crear un Dockerfile simple que se puede utilizar con el resto de este procedimiento:

    ```
    cat << EndOfContent > Dockerfile
    FROM alpine:latest
    CMD while :; do echo "Hello, world."; sleep 3; done
    EndOfContent
    ```
    {: codeblock}

  2. Cree metadatos de servicio periférico para el proyecto:

    ```
    hzn dev service new -s myservice -V 1.0.0 -i $DOCKER_HUB_ID/myservice --noImageGen
    ```
    {: codeblock}

    Este mandato crea `horizon/service.definition.json` para describir el servicio y `horizon/pattern.json` para describir el patrón de despliegue. Puede abrir estos archivos y examinar su contenido.

2. Cree y pruebe el servicio.

  1. Construya el contenedor. El nombre de la imagen del contenedor debe coincidir con lo que se hace referencia en `horizon/service.definition.json`.

    ```
    eval $(hzn util configconv -f horizon/hzn.json)
    export ARCH=$(hzn architecture)
    sudo docker build -t "${DOCKER_IMAGE_BASE}_$ARCH:$SERVICE_VERSION" .
    unset DOCKER_IMAGE_BASE SERVICE_NAME SERVICE_VERSION
    ```
    {: codeblock}

  2. Ejecute este contenedor de servicios en el entorno de agente simulado de {{site.data.keyword.horizon}}:

    ```
    hzn dev service start -S
    ```
    {: codeblock}

  3. Verifique que el contenedor de servicios está en ejecución:

    ```
    sudo docker ps
    ```
    {: codeblock}

  4. Vea las variables de entorno que se han pasado al contenedor cuando se inició. (Estas son las mismas variables de entorno que el agente completo pasa al contenedor de servicios.)

    ```
    sudo docker inspect $(sudo docker ps -q --filter name=myservice) | jq '.[0].Config.Env'
    ```
    {: codeblock}

  5. Vea el registro del contenedor de servicios:

    En **{{site.data.keyword.linux_notm}}**:

    ```
    sudo tail -f /var/log/syslog | grep myservice[[]
    ```
    {: codeblock}

    En **{{site.data.keyword.macOS_notm}}**:
    ```
    sudo docker logs -f $(sudo docker ps -q --filter name=myservice)
    ```
    {: codeblock}

  6. Detenga el servicio:

    ```
    hzn dev service stop
    ```
    {: codeblock}

3. Publique el servicio en {{site.data.keyword.edge_devices_notm}}. Ahora que ha verificado que el código de servicio se ejecuta tal como se esperaba en el entorno de agente simulado, publique el servicio en {{site.data.keyword.horizon_exchange}} para que pase a estar disponible para el despliegue en los nodos periféricos.

  El mandato **publish** siguiente utiliza el archivo `horizon/service.definition.json` y el par de claves para firmar y publicar el servicio en {{site.data.keyword.horizon_exchange}}. También envía la imagen de contenedor a Docker Hub.

  ```
  hzn exchange service publish -f horizon/service.definition.json
  hzn exchange service list
  ```
  {: codeblock}

4. Publique un patrón de despliegue para el servicio. Este patrón de despliegue puede ser utilizado por nodos periféricos para hacer que {{site.data.keyword.edge_devices_notm}} despliegue el servicio en los mismos:

  ```
  hzn exchange pattern publish -f horizon/pattern.json
    hzn exchange pattern list
  ```
  {: codeblock}

5. Registre el nodo periférico para ejecutar el patrón de despliegue.

  1. De la misma forma que ha registrado previamente los nodos periféricos con los patrones de despliegue público en la organización `IBM`, registre el nodo periférico con el patrón de despliegue que ha publicado bajo su propia organización:

    ```
    hzn register -p pattern-myservice-$(hzn architecture) -s myservice --serviceorg $HZN_ORG_ID
    ```
    {: codeblock}

  2. Liste el servicio periférico del contenedor Docker que se ha iniciado como resultado:

    ```
    sudo docker ps
    ```
    {: codeblock}

  3. Vea la salida del servicio periférico myservice:

    ```
    sudo hzn service log -f myservice
    ```
    {: codeblock}

6. Vea el nodo, el servicio y el patrón que ha creado en la consola {{site.data.keyword.edge_devices_notm}}. Puede mostrar el URL de la consola con:

  ```
  echo "$(awk -F '=|ec-exchange' '/^HZN_EXCHANGE_URL/ {print $2}' /etc/default/horizon)edge"
  ```
  {: codeblock}

7. Anule el registro del nodo periférico y detenga el servicio `myservice`:

  ```
  hzn unregister -f
  ```
  {: codeblock}

## Qué hacer a continuación
{: #quickstart_ex_what_next}

* Pruebe los otros ejemplos de servicio periférico en [Desarrollo de servicios periféricos con {{site.data.keyword.edge_devices_notm}}](developing.md).
