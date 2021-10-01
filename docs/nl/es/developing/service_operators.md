---

copyright:
years: 2020
lastupdated: "2020-04-27"

---

{:shortdesc: .shortdesc}
{:new_window: target="_blank"}
{:codeblock: .codeblock}
{:pre: .pre}
{:screen: .screen}
{:tip: .tip}
{:download: .download}

# Desarrollo de un operador de Kubernetes
{: #kubernetes_operator}

En general, el desarrollo de un servicio para ejecutarlo en un clúster periférico es similar al desarrollo de un servicio periférico que se ejecuta en un dispositivo periférico. El servicio periférico se desarrolla utilizando el desarrollo de [Procedimientos recomendados de desarrollo nativo periférico](../OH/docs/developing/best_practices.md) y se empaqueta en un contenedor. La diferencia está en cómo se despliega el servicio periférico.

Para desplegar un servicio periférico contenerizado en un clúster periférico, un desarrollador debe crear
primero un operador de Kubernetes que despliegue el servicio periférico contenerizado en un clúster
Kubernetes. Una vez que se ha escrito y probado el operador, el desarrollador crea y publica el operador como
un servicio de {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}). Este proceso permite que un administrador de {{site.data.keyword.ieam}} despliegue el servicio de operador como se hace para cualquier servicio de {{site.data.keyword.ieam}}, con política o patrones. No es necesario crear una definición de servicio de {{site.data.keyword.ieam}} para el servicio periférico. Cuando el administrador de {{site.data.keyword.ieam}} despliega el servicio de operador, el operador despliega el servicio periférico.

Hay disponibles diversas fuentes de información al escribir un operador de Kubernetes. En primer lugar, lea [Conceptos de Kubernetes - Patrón de operador](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/). Este sitio es un buen recurso para obtener información sobre los operadores. Después de familiarizarse con los conceptos de operador, la escritura de un operador se lleva a cabo utilizando la [Infraestructura de operador](https://operatorframework.io/). Este sitio web proporciona más detalles sobre lo que es un operador y ofrece una guía paso a paso para crear un operador simple, utilizando el Kit de desarrollo de software (SDK) del operador.

## Consideraciones sobre el desarrollo de un operador para {{site.data.keyword.ieam}}

Se trata de una práctica recomendada para hacer un uso libre de la capacidad de estado del operador porque {{site.data.keyword.ieam}} informa de cualquier estado que el operador cree en el centro de gestión de {{site.data.keyword.ieam}}. Cuando se escribe un operador, la infraestructura de operador genera una definición de recurso personalizada (CRD) de Kubernetes para el operador. Cada CRD de operador tiene un objeto de estado que se debe llenar con información de estado importante sobre el estado del operador y del servicio periférico que está desplegando. Kubernetes no lo hace automáticamente; es necesario que el desarrollador de operador lo escriba en la implementación del operador. El agente de {{site.data.keyword.ieam}} en un clúster periférico recopila periódicamente el estado de operador y lo notifica al centro de gestión.

El operador puede optar por conectar las variables de entorno {{site.data.keyword.ieam}} específicas del servicio a cualquier servicio que inicie. Cuando se inicia el operador, el agente de {{site.data.keyword.ieam}} crea un configmap de Kubernetes denominado `hzn-env-vars` que contiene las variables de entorno específicas del servicio. Opcionalmente, el operador puede adjuntar dicha correlación de configuración a cualquier despliegue que cree, lo que permite que los servicios que inicie reconozcan las mismas variables de entorno específicas de servicio. Se trata de las mismas variables de entorno que se inyectan en servicios que se ejecutan en dispositivos periféricos. La única excepción son las variables de entorno ESS*, porque el Sistema de gestión de modelos (MMS) todavía no está soportado en los servicios de clúster periférico.

Si se desea, los operadores desplegados por {{site.data.keyword.ieam}} se pueden desplegar en un espacio de nombres distinto del espacio de nombres predeterminado. Esto lo lleva a cabo el desarrollador de operador modificando los archivos yaml de operador para que apunten al espacio de nombres. Existen dos formas de realizar esto:

* Modifique la definición de despliegue del operador (normalmente denominada **./deploy/operator.yaml**) para especificar un espacio de nombres

o

* Incluya un archivo yaml de definición de espacio de nombres con los archivos de definición yaml del operador; por ejemplo, en el directorio **./deploy** del proyecto de operador.

**Nota**: Cuando un operador se despliega en un espacio de nombres no predeterminado, {{site.data.keyword.ieam}} crea el espacio de nombres si no existe y lo elimina cuando {{site.data.keyword.ieam}} retira el despliegue del operador.

## Empaquetado de un operador para {{site.data.keyword.ieam}}

Una vez que un operador se ha escrito y probado, debe empaquetarse para que {{site.data.keyword.ieam}} lo despliegue:

1. Asegúrese de que el operador está empaquetado para ejecutarse como un despliegue dentro de un clúster. Esto significa que el operador se crea en un contenedor y se envía al registro de contenedor del que se recupera el contenedor cuando {{site.data.keyword.ieam}} lo despliega. Normalmente, esto se lleva a cabo creando el operador con el uso de los mandatos **operator-sdk build** seguidos de los mandatos **docker push**. Esto se describe en [Guía de aprendizaje del operador](https://sdk.operatorframework.io/docs/building-operators/golang/tutorial/#2-run-as-a-deployment-inside-the-cluster).

2. Asegúrese de que el contenedor o los contenedores de servicio desplegados por el operador también se envían al registro desde el que el operador los desplegará.

3. Cree un archivo que contenga los archivos de definición de yaml del operador desde el proyecto de operador:

   ```bash
   cd <proyecto-operador>/<nombre-operador>/deploy    tar -zcvf <nombre-archivo>.tar.gz ./*
   ```
   {: codeblock}

   **Nota**: Para los usuarios de {{site.data.keyword.macos_notm}}, considere la posibilidad de crear un archivo tar.gz de archivado limpio para garantizar que no existen archivos ocultos en el archivo tar.gz. Por ejemplo, un archivo .DS_store puede causar problemas al desplegar un operador helm. Si sospecha que existe un archivo oculto, extraiga el archivo tar.gz en el sistema {{site.data.keyword.linux_notm}}. Para obtener más información, consulte [Mandato tar en macos](https://stackoverflow.com/questions/8766730/tar-command-in-mac-os-x-adding-hidden-files-why).

   ```bash
   tar -xzpvf x.tar --exclude=".*"
   ```
   {: codeblock}

4. Utilice las herramientas de creación de servicio de {{site.data.keyword.ieam}} para crear una definición de servicio para el servicio de operador, por ejemplo:

   1. Cree un proyecto nuevo:

      ```bash
      hzn dev service new -V <a version> -s <a service name> -c cluster
      ```
      {: codeblock}

   2. Edite el archivo **horizon/service.definition.json** para que apunte al archivo yaml del operador creado anteriormente en el paso 3.

   3. Cree una clave de firma de servicio o utilice una que ya haya creado.

   4. Publique el servicio

      ```
      hzn exchange service publish -k <clave_firma> -f ./horizon/service.definition.json
      ```
      {: codeblock}

5. Cree una política o patrón de despliegue para desplegar el servicio de operador en un clúster periférico.
