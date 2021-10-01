---

copyright:
years: 2020
lastupdated: "2020-10-7"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Consideraciones sobre GDPR

## Aviso
{: #notice}
<!-- This is boilerplate text provided by the GDPR team. It cannot be changed. -->

Este documento está pensado para ayudarle a prepararse para la disposición de GDPR. Proporciona información de características de {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) que puede configurar y aspectos del uso del producto a tener en cuenta cuando se prepara la organización para GDPR. Esta información no es una lista exhaustiva. Los clientes pueden elegir y configurar características de muchas formas diferentes y utilizar el producto de muchas formas y con aplicaciones y sistemas de terceros.

<p class="ibm-h4 ibm-bold">Los clientes son responsables de garantizar el cumplimiento de las leyes y normativas aplicables, incluyendo el Reglamento general de protección de datos de la Unión Europea. Los clientes son los únicos responsables de obtener asesoramiento legal competente en cuanto a la identificación e interpretación de las leyes y regulaciones relevantes que puedan afectar a los negocios de los clientes y a las acciones que los clientes puedan necesitar realizar para cumplir con dichas leyes y regulaciones.</p>

<p class="ibm-h4 ibm-bold">Los productos, los servicios y otras prestaciones que se describen aquí no son adecuados para todas las situaciones de cliente y pueden restringir la disponibilidad. IBM no proporciona asesoramiento legal, contable ni de auditoría ni representa o garantiza que sus servicios o productos aseguren que los clientes cumplen con cualquier ley o reglamentación.</p>

## Tabla de contenido

* [GDPR](#overview)
* [Configuración del producto para GDPR](#productconfig)
* [Ciclo de vida de los datos](#datalifecycle)
* [Proceso de datos](#dataprocessing)
* [Capacidad para restringir el uso de datos personales](#datasubjectrights)
* [Apéndice](#appendix)

## GDPR
{: #overview}

<!-- This is boilerplate text provided by the GDPR team. It cannot be changed. -->
El Reglamento general de protección de datos (GDPR) fue adoptado por la Unión Europea (UE) y se aplica a partir del 25 de mayo de 2018.

### ¿Por qué es importante GDPR?

GDPR establece una infraestructura reguladora de protección de datos más sólida para el proceso de los datos personales de las personas. GDPR aporta:

* Derechos nuevos y mejorados para los individuos
* Definición ampliada de los datos personales
* Nuevas obligaciones para empresas y organizaciones que manejan datos personales
* Cuantiosas sanciones económicas por incumplimiento
* Notificación de infracción de datos obligatoria

IBM ha establecido un programa de preparación global que se encarga de que los procesos internos y las ofertas comerciales de IBM cumplan con el GDPR.

### Más información

* [Portal de información de GDPR de la UE](https://gdpr.eu/)
*  [Sitio web ibm.com/GDPR](https://www.ibm.com/data-responsibility/gdpr/)

## Configuración del producto: consideraciones para la disposición de GDPR
{: #productconfig}

Las siguientes secciones describen aspectos de {{site.data.keyword.ieam}} y proporcionan información sobre las prestaciones para ayudar a los clientes con los requisitos de GDPR.

### Ciclo de vida de los datos
{: #datalifecycle}

{{site.data.keyword.ieam}} es una aplicación para desarrollar y gestionar aplicaciones locales contenerizadas. Es un entorno integrado para gestionar cargas de trabajo de contenedor en la periferia. Incluye el orquestador de contenedores Kubernetes, un registro de imágenes privadas, una consola de gestión, un agente de nodo periférico e infraestructuras de supervisión.

De por sí, {{site.data.keyword.ieam}} funciona principalmente con datos técnicos relacionados con la configuración y la gestión de la aplicación, algunos de los cuales pueden estar sujetos a GDPR. {{site.data.keyword.ieam}} también se ocupa de la información sobre los usuarios que gestionan la aplicación. Estos datos se describen en todo este documento para el conocimiento de los clientes responsables de cumplir los requisitos de GDPR.

Estos datos se conservan en {{site.data.keyword.ieam}} en sistemas de archivos locales o remotos como archivos de configuración o en bases de datos. Las aplicaciones que se desarrollan para ejecutarse en {{site.data.keyword.ieam}} pueden utilizar otras formas de datos personales sujetas a GDPR. Los mecanismos que se utilizan para proteger y gestionar datos también están disponibles para las aplicaciones que se ejecutan en {{site.data.keyword.ieam}}. Es posible que se necesiten más mecanismos para gestionar y proteger los datos personales recopilados por las aplicaciones que se ejecutan en {{site.data.keyword.ieam}}.

Para comprender los flujos de datos de {{site.data.keyword.ieam}}, debe conocer cómo funcionan Kubernetes, Docker y Operators. Estos componentes de código abierto son fundamentales para {{site.data.keyword.ieam}}. {{site.data.keyword.ieam}} se utiliza para poner instancias de contenedores de aplicaciones (servicios periférico) en nodos periféricos. Los servicios periféricos contienen los detalles sobre la aplicación y las imágenes de Docker contienen todos los paquetes de software que las aplicaciones necesitan ejecutar.

{{site.data.keyword.ieam}} incluye un conjunto de ejemplos de servicio periférico de código abierto. Para ver una lista de todos los diagramas de {{site.data.keyword.ieam}}, consulte [open-horizon/examples](https://github.com/open-horizon/examples){:new_window}. Es responsabilidad del cliente determinar e implementar los controles de GDPR apropiados para el software de código abierto.

### Qué tipos de datos fluyen a través de {{site.data.keyword.ieam}}

{{site.data.keyword.ieam}} se ocupa de varias categorías de datos técnicos que pueden considerarse datos personales, como por ejemplo:

* ID de usuario y contraseña de administrador o de operador
* Direcciones IP
* Nombres de nodo de Kubernetes

En las secciones posteriores de este documento se describe la información sobre cómo se recopilan, crean y almacenan estos datos técnicos, cómo se accede a ellos y cómo se protegen, se registran y se suprimen.

### Datos personales utilizados para el contacto en línea con IBM

Los clientes de {{site.data.keyword.ieam}} pueden enviar comentarios en línea, feedback y solicitudes a IBM sobre los temas de {{site.data.keyword.ieam}} de varias formas, principalmente:

* La {{site.data.keyword.ieam}} Slack Community pública
* Área de comentarios públicos en las páginas de la documentación del producto {{site.data.keyword.ieam}}
* Comentarios públicos en el espacio de {{site.data.keyword.ieam}} de dW Answers

Normalmente, sólo se utilizan el nombre de cliente y la dirección de correo electrónico para habilitar las respuestas personales para el contacto. Este uso de datos personales se ajusta a la [Declaración de privacidad en línea de IBM](https://www.ibm.com/privacy/us/en/){:new_window}.

### Autenticación

El gestor de autenticación de {{site.data.keyword.ieam}} acepta las credenciales de usuario de la {{site.data.keyword.gui}} y reenvía las credenciales al proveedor de OIDC de fondo, lo que valida las credenciales de usuario en el directorio de empresa. El proveedor de OIDC devolverá entonces una cookie de autenticación (`auth-cookie`) con el contenido de una señal web JSON (`JWT`, JSON Web Token) al gestor de autenticación. La señal JWT conserva información como, por ejemplo, el ID de usuario y la dirección de correo electrónico, además de la pertenencia a grupos en el momento de la solicitud de autenticación. Esta cookie de autenticación se envía de nuevo a la {{site.data.keyword.gui}}. La cookie se renueva durante la sesión. Es válida durante las 12 horas posteriores al cierre de sesión de la {{site.data.keyword.gui}} o al cierre del navegador web.

Para todas las solicitudes de autenticación posteriores realizadas desde la {{site.data.keyword.gui}}, el servidor NodeJS frontal decodifica la cookie de autenticación disponible en la solicitud y valida la solicitud llamando al gestor de autenticación.

La CLI de {{site.data.keyword.ieam}} necesita que el usuario proporcione una clave de API. Las claves de API se crean utilizando el mandato `cloudctl`.

Las CLI **cloudctl**, **kubectl**y **oc** también necesitan credenciales para acceder al clúster. Estas credenciales se pueden obtener desde la consola de gestión y caducan tras 12 horas.

### Correlación de roles

{{site.data.keyword.ieam}} soporta el control de acceso basado en roles (RBAC). En la etapa de correlación de roles, el nombre de usuario que se proporciona en la etapa de autenticación se correlaciona con un rol de usuario o grupo. Los roles se utilizan para autorizar las actividades que el usuario autenticado puede llevar a cabo. Consulte [Control de acceso basado en roles](rbac.md) para obtener detalles sobre los roles de {{site.data.keyword.ieam}}.

### Seguridad de pods

Las política de seguridad de pod se utilizan para configurar el centro de gestión o el control de clúster periférico sobre lo que un pod puede hacer o a lo que puede acceder. Para obtener más información sobre los pods, consulte [Instalación del centro de gestión](../hub/hub.md) y [Clústeres periféricos](../installing/edge_clusters.md).

## Proceso de datos
{: #dataprocessing}

Los usuarios de {{site.data.keyword.ieam}} pueden controlar la forma en que se procesan y se protegen los datos técnicos relacionados con la configuración y la gestión mediante la configuración del sistema.

* El control de acceso basado en roles (RBAC) controla a qué datos y a qué funciones pueden acceder los usuarios.

* Las políticas de seguridad de los pods se utilizan para establecer un control a nivel de clúster con relación a lo que un pod puede hacer y a lo que puede acceder.

* Los datos en tránsito se protegen utilizando `TLS`. `HTTPS` (`TLS` subyacente) se utiliza para la transferencia de datos protegidos entre el cliente de usuario y los servicios de fondo. Los usuarios pueden especificar el certificado raíz que se utilizará durante la instalación.

* La protección de datos en reposo se soporta utilizando `dm-crypt` para cifrar los datos.

* Los periodos de retención de datos para el registro (ELK) y la supervisión (Prometheus) son configurables y se soporta la supresión de datos mediante las API proporcionadas.

Estos mismos mecanismos que se utilizan para gestionar y proteger los datos técnicos de {{site.data.keyword.ieam}} se pueden utilizar para gestionar y proteger los datos personales para las aplicaciones desarrolladas por el usuario o proporcionadas por el usuario. Los clientes pueden desarrollar sus propias funcionalidades para implementar más controles.

Para obtener más información sobre los certificados, consulte [Instalar {{site.data.keyword.ieam}}](../hub/installation.md).

## Capacidad para restringir el uso de datos personales
{: #datasubjectrights}

Utilizando los recursos resumidos en este documento, {{site.data.keyword.ieam}} permite a un usuario restringir el uso de los datos técnicos de la aplicación que se consideran datos personales.

Bajo GDPR, los usuarios tienen derecho a acceder, modificar y restringir el proceso. Consulte otras secciones de este documento para controlar:
* Derecho de acceso
  * Los administradores de {{site.data.keyword.ieam}} pueden utilizar las características de {{site.data.keyword.ieam}} para proporcionar a las personas acceso a los datos.
  * Los administradores de {{site.data.keyword.ieam}} pueden utilizar las características de {{site.data.keyword.ieam}} para proporcionar a las personas información sobre los datos que {{site.data.keyword.ieam}} recopila y retiene sobre la persona.
* Derecho a modificar
  * Los administradores de {{site.data.keyword.ieam}} pueden utilizar las características de {{site.data.keyword.ieam}} para permitir que una persona modifique o corrija los datos.
  * Los administradores de {{site.data.keyword.ieam}} pueden utilizar las características de {{site.data.keyword.ieam}} para corregir los datos de una persona para ellos.
* Derecho a restringir el proceso
  * Los administradores de {{site.data.keyword.ieam}} pueden utilizar las características de {{site.data.keyword.ieam}} para detener el proceso de los datos de una persona.

## Apéndice - Datos registrados por {{site.data.keyword.ieam}}
{: #appendix}

Como aplicación, {{site.data.keyword.ieam}} se ocupa de varias categorías de datos técnicos que se pueden considerar como datos personales:

* ID de usuario y contraseña de administrador o de operador
* Direcciones IP
* Nombres de nodo de Kubernetes. 

{{site.data.keyword.ieam}} también se ocupa de la información sobre los usuarios que gestionan las aplicaciones que se ejecutan en {{site.data.keyword.ieam}} y pueden introducir otras categorías de datos personales que son desconocidas para la aplicación.

### Seguridad de {{site.data.keyword.ieam}}

* Qué datos se registran
  * ID de usuario, nombre de usuario y dirección IP de usuarios que han iniciado sesión
* Cuándo se registran datos
  * Con solicitudes de inicio de sesión
* Dónde se registran los datos
  * En los registros de auditoría en `/var/lib/icp/audit`???
  * En los registros de auditoría en `/var/log/audit`???
  * Registro de Exchange en???
* Cómo suprimir los datos
  * Busque los datos y suprima el registro del registro de auditoría

### API de {{site.data.keyword.ieam}}

* Qué datos se registran
  * ID de usuario, nombre de usuario y dirección IP del cliente en los registros de contenedor
  * Datos de estado del clúster de Kubernetes en el servidor de `etcd`
  * Credenciales de OpenStack y VMware en el servidor de `etcd`
* Cuándo se registran datos
  * Con solicitudes de API
  * Credenciales almacenadas desde el mandato `credentials-set`
* Dónde se registran los datos
  * En los registros de contenedor, Elasticsearch y el servidor de `etcd`.
* Cómo suprimir los datos
  * Suprima los registros de contenedor (`platform-api`, `platform-deploy`) de los contenedores o suprima las entradas de registro específicas de usuario de Elasticsearch.
  * Borre los pares de clave-valor `etcd` seleccionados utilizando el mandato `etcdctl rm`.
  * Elimine credenciales llamando al mandato `credentials-unset`.


Para obtener más información, consulte:

  * [Registro de Kubernetes](https://kubernetes.io/docs/concepts/cluster-administration/logging/){:new_window}
  * [etcdctl](https://github.com/coreos/etcd/blob/master/etcdctl/READMEv2.md){:new_window}

### Supervisión de {{site.data.keyword.ieam}}

* Qué datos se registran
  * Dirección IP, nombres de pods, release, imagen
  * Los datos extraídos de las aplicaciones desarrolladas por el cliente pueden incluir datos personales
* Cuándo se registran datos
  * Cuando Prometheus extrae medidas de destinos configurados
* Dónde se registran los datos
  * En el servidor de Prometheus o en los volúmenes persistentes configurados
* Cómo suprimir los datos
  * Busque y suprima datos utilizando la API de Prometheus

Para obtener más información, consulte [Documentación de Prometheus](https://prometheus.io/docs/introduction/overview/){:new_window}.


### {{site.data.keyword.ieam}} Kubernetes

* Qué datos se registran
  * Topología desplegada en clúster (información de nodo para controlador, trabajador, proxy y va)
  * Configuración de servicio (mapa de configuración k8s) y secretos (secretos k8s)
  * ID de usuario en el registro de apiserver
* Cuándo se registran datos
  * Al desplegar un clúster
  * Al desplegar una aplicación del catálogo de Helm
* Dónde se registran los datos
  * Topología desplegada en clúster en `etcd`
  * Configuración y secreto para aplicaciones desplegadas en `etcd`
* Cómo suprimir los datos
  * Utilice la {{site.data.keyword.gui}} de {{site.data.keyword.ieam}}
  * Busque y suprima datos utilizando la {{site.data.keyword.gui}} de k8s (`kubectl`) o la API REST `etcd`
  * Busque y suprima datos de registro de apiserver utilizando la API de Elasticsearch

Tenga cuidado al modificar la configuración de clúster de Kubernetes o al suprimir datos de clúster.

  Para obtener más información, consulte [Kubernetes kubectl](https://kubernetes.io/docs/reference/kubectl/overview/){:new_window}.

### API de Helm de {{site.data.keyword.ieam}}

* Qué datos se registran
  * Nombre de usuario y rol
* Cuándo se registran datos
  * Cuando un usuario recupera gráficas o repositorios que se añaden a un equipo
* Dónde se registran los datos
  * Registros de despliegue de helm-api, Elasticsearch
* Cómo suprimir los datos
  * Buscar y suprimir datos de registro de helm-api utilizando la API de Elasticsearch

### Intermediario de servicio de {{site.data.keyword.ieam}} Service Broker

* Qué datos se registran
  * ID de usuario (solo en el nivel de registro de depuración 10, no en el nivel de registro predeterminado)
* Cuándo se registran datos
  * Cuando se realizan solicitudes de API en el intermediario de servicio
  * Cuando el intermediario de servicio accede al catálogo de servicios
* Dónde se registran los datos
  * Registro de contenedor del intermediario de servicio, Elasticsearch
* Cómo suprimir los datos
  * Buscar y suprimir el registro de apiserver que utiliza la API de Elasticsearch
  * Buscar y suprimir el registro del contenedor de apiserver
      ```
      kubectl logs $(kubectl get pods -n kube-system | grep  service-catalogapiserver | awk '{print $1}') -n kube-system | grep admin
      ```
      {: codeblock}


  Para obtener más información, consulte [Kubernetes kubectl](https://kubernetes.io/docs/reference/kubectl/overview/){:new_window}.
