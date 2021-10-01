{:shortdesc: .shortdesc}
{:new_window: target="_blank"}

# Glosario
*Última actualización: 6 de mayo de 2021*

Este glosario proporciona términos y definiciones correspondientes para {{site.data.keyword.edge}}.
{:shortdesc}

En este glosario se emplean las siguientes referencias cruzadas:

- *Véase* le remite desde un término no preferido al término preferido o desde una abreviatura a la forma completa.
- *Véase también* le remite a un término relacionado u opuesto.

<!--If you do not want letter links at the top of your glossary, delete the text between these comment tags.-->

[A](#glossa) [B](#glossb) [C](#glossc) [D](#glossd) [E](#glosse) [F](#glossf) [G](#glossg) [H](#glossh) [I](#glossi) [K](#glossk) [L](#glossl) [M](#glossm) [N](#glossn) [O](#glosso) [P](#glossp) [R](#glossr) [S](#glosss) [T](#glosst) [V](#glossv) [W](#glossw)

<!--end letter link tags-->

## A
{: #glossa}

### clave de API
{: #x8051010}

Código exclusivo que se pasa a una API para identificar el usuario o la aplicación de llamada. Se utiliza una clave de API para realizar un seguimiento y controlar cómo se utiliza la API, por ejemplo, para evitar el uso malicioso o el abuso de la API.

### aplicación
{: #x2000166}

Uno o más programas informáticos o componentes de software que proporcionan una función de soporte directo de uno o más procesos de negocio específicos.

### zona de disponibilidad
{: #x7018171}

Segmento funcionalmente independiente, asignado por un operador, de la infraestructura de red.

## B
{: #glossb}

### nodo de arranque
{: #x9520233}

Nodo utilizado para ejecutar la instalación, la configuración, el escalado de nodos y las actualizaciones de clústeres.

### política de negocio
{: #x62309388}

(en desuso) Término anterior para la política de despliegue.

## C
{: #glossc}

### catálogo
{: #x2000504}

Ubicación centralizada que se puede utilizar para buscar e instalar paquetes en un clúster.

### clúster
{: #x2017080}

Conjunto de recursos, nodos de trabajador, redes y dispositivos de almacenamiento que permiten que las aplicaciones tengan alta disponibilidad y estén listas para desplegarse en contenedores.

### restricciones
{: #x62309387}

Expresiones lógicas en términos de propiedades. Las restricciones se utilizan para controlar y gestionar el despliegue de software en nodos periféricos.

### contenedor
{: #x2010901}

Construcción del sistema que permite a los usuarios ejecutar simultáneamente instancias distintas del sistema operativo lógico. Los contenedores utilizan capas de los sistemas de archivos para minimizar los tamaños de imágenes y promover la reutilización. Véase también [imagen](#x2024928), [capa](#x2028320), [registro](#x2064940).

### imagen de contenedor
{: #x8941555}

En Docker, software autónomo y ejecutable, que incluye código y herramientas del sistema, que se puede utilizar para ejecutar una aplicación.

### orquestación de contenedores
{: #x9773849}

Proceso de gestionar el ciclo de vida de los contenedores, incluido el suministro, el despliegue y la disponibilidad.

## D
{: #glossd}

### despliegue
{: #x2104544}

Proceso que recupera paquetes o imágenes y los instala en una ubicación definida para que se puedan probar o ejecutar.

### patrón de despliegue
{: #x623093810}

Una lista de servicios desplegables específicos. Los patrones son una simplificación del mecanismo de política más general y con más capacidad. Los nodos periféricos pueden registrarse en un patrón de despliegue para hacer que se despliegue el conjunto de servicios del patrón.

### política de despliegue
{: #x62309386}

Conjunto de propiedades y restricciones relacionadas con el despliegue de un servicio específico, junto con un identificador para la versión de servicio que se debe desplegar y otra información, por ejemplo, cómo deben manejarse las retrotracciones cuando se producen anomalías.

### DevOps
{: #x5784896}

Metodología de software que integra el desarrollo de aplicaciones y las operaciones de TI, de manera que los equipos puedan entregar el código a producción más rápido e iterar de forma continuada en función de los comentarios del mercado.

### Docker
{: #x7764788}

Plataforma abierta que los desarrolladores y administradores de sistemas pueden utilizar para compilar, enviar y ejecutar aplicaciones distribuidas.

## E
{: #glosse}

### Edge Computing
{: #x9794155}

Un modelo de informática distribuida que saca partido del cálculo disponible fuera de los centros de datos tradicionales y en la nube. Un modelo Edge Computing coloca una carga de trabajo más cerca de donde se crean los datos asociados y de donde se realizan acciones en respuesta al análisis de esos datos. La colocación de datos y cargas de trabajo en dispositivos periféricos reduce las latencias, baja la demanda de ancho de banda de red, aumenta la privacidad de la información confidencial y permite realizar operaciones durante las interrupciones de red.

### dispositivo periférico
{: #x2026439}

Una pieza de equipo, como por ejemplo una máquina de ensamblaje en una fábrica, un cajero automático, una cámara inteligente o un automóvil que tiene capacidad de cálculo integrada en la que se puede realizar trabajo significativo y se pueden recopilar o generar datos.

### pasarela periférica
{: #x9794163}

Un clúster periférico que tiene servicios que realizan funciones de red como por ejemplo la conversión de protocolos, la terminación de la red, el tunelado, la protección mediante cortafuegos o las conexiones inalámbricas. Una pasarela periférica sirve como punto de conexión entre un dispositivo periférico o un clúster periférico y la nube o una red más grande.

### nodo periférico
{: #x8317015}

Cualquier dispositivo periférico, clúster periférico o pasarela periférica en los que tiene lugar Edge Computing.

### clúster periférico
{: #x2763197}

Un sistema de una instalación operativa remota que ejecuta cargas de trabajo de aplicación de empresa y servicios compartidos. Un clúster periférico se puede utilizar para conectarse a un dispositivo periférico, conectarse a otro clúster periférico o servir como pasarela periférica para conectar con la nube o con una red más grande.

### servicio periférico
{: #x9794170}

Un servicio diseñado específicamente para desplegarse en un clúster periférico, una pasarela periférica o un dispositivo periférico. El reconocimiento visual, la percepción acústica y el reconocimiento de voz son todos ejemplos de posibles servicios periféricos.

### carga de trabajo periférica
{: #x9794175}

Cualquier servicio, microservicio o fragmento de software que realiza un trabajo significativo cuando se ejecuta en un nodo periférico.

### punto final
{: #x2026820}

Dirección de destino de red expuesta por los recursos de Kubernetes, como por ejemplo servicios e ingresos.

## F
{: #glossf}

## G
{: #glossg}

### Grafana
{: #x9773864}

Plataforma de análisis y visualización de código abierto para supervisar, buscar, analizar y visualizar métricas.

## H
{: #glossh}

### HA
{: #x2404289}

Véase [alta disponibilidad](#x2284708).

### gráfica de Helm
{: #x9652777}

Paquete de Helm que contiene información para instalar un conjunto de recursos de Kubernetes en un clúster de Kubernetes.

### release de Helm
{: #x9756384}

Instancia de una gráfica de Helm que se ejecuta en un clúster de Kubernetes.

### repositorio de Helm
{: #x9756389}

Colección de gráficas.

### alta disponibilidad (HA)
{: #x2284708}

Posibilidad de los servicios de TI de resistir todas las paradas y seguir proporcionando capacidad de proceso de acuerdo con un nivel de servicio predefinido. Las paradas cubiertas incluyen sucesos planificados, como el mantenimiento y las copias de seguridad, y sucesos no planificados, como las anomalías de software y hardware, anomalías en el suministro de energía y los desastres. Véase también [tolerancia al error](#x2847028).

## I
{: #glossi}

### IBM Cloud Pak
{: #x9773840}

Un paquete de una o varias ofertas de IBM Certified Container de nivel empresarial, seguras y gestionadas por el ciclo de vida que se empaquetan y se integran en el entorno de IBM Cloud.

### imagen
{: #x2024928}

Sistema de archivos y sus parámetros de ejecución que se utilizan en el tiempo de ejecución de un contenedor para crear un contenedor. El sistema de archivos consta de una serie de capas, combinadas en el tiempo de ejecución, que se crean a medida que se crea la imagen mediante actualizaciones sucesivas. La imagen no retiene el estado mientras se ejecuta el contenedor. Véase también [contenedor](#x2010901), [capa](#x2028320), [registro](#x2064940).

### registro de imágenes
{: #x3735328}

Ubicación centralizada para gestionar imágenes.

### ingress
{: #x7907732}

Colección de reglas para permitir las conexiones de entrada a los servicios de clúster de Kubernetes.

### aislamiento
{: #x2196809}

Proceso de confinar los despliegues de carga de trabajo a recursos virtuales y virtuales dedicados para lograr el soporte de multitenencia.

## K
{: #glossk}

### Klusterlet
{: #x9773879}

En IBM Multicloud Manager, agente responsable de un único clúster de Kubernetes.

### Kubernetes
{: #x9581829}

Herramienta de orquestación de código abierto para contenedores.

## L
{: #glossl}

### capa
{: #x2028320}

Versión modificada de una imagen padre. Las imágenes constan de capas, donde la versión modificada se coloca como una capa sobre la imagen padre para crear la nueva imagen. Véase también [contenedor](#x2010901), [imagen](#x2024928).

### equilibrador de carga
{: #x2788902}

Software o hardware que distribuye la carga entre un conjunto de servidores para procurar que dichos servidores no se saturen. Un equilibrador de carga también dirige a los usuarios a otro servidor cuando falla el primer servidor.

## M
{: #glossm}

### consola de gestión
{: #x2398932}

La interfaz gráfica de usuario de {{site.data.keyword.edge_notm}}.

### centro de gestión
{: #x3954437}

El clúster que aloja los componentes centrales de {{site.data.keyword.edge_notm}}.

### mercado
{: #x2118141}

Lista de servicios habilitados en los que los usuarios pueden suministrar recursos.

### nodo maestro
{: #x4790131}

Nodo que proporciona servicios de gestión y controla los nodos de trabajador de un clúster. El nodo maestro contiene los procesos responsables de la asignación de recursos, el mantenimiento del estado, la planificación y la supervisión.

### microservicio
{: #x8379238}

Conjunto de pequeños componentes arquitecturales independientes, cada uno con una única finalidad, que se comunican mediante una API ligera común.

### multicloud
{: #x9581814}

Modelo de computación en la nube en el que una empresa utiliza una combinación de arquitectura local, de cloud pública y de cloud privada.

## N
{: #glossn}

### namespace
{: #x2031005}

Clúster virtual de un clúster de Kubernetes que se puede utilizar para organizar y dividir los recursos entre varios usuarios.

### Network File System (NFS)
{: #x2031282}

Protocolo que posibilita que un sistema acceda a archivos a través de una red como si estuvieran en sus discos locales.

### NFS
{: #x2031508}

Consulte [Network File System](#x2031282).

### política de nodo
{: #x62309384}

Conjunto de propiedades y restricciones relacionadas con un nodo periférico (un nodo periférico autónomo de Linux o un nodo de clúster Kubernetes).

## O
{: #glosso}

### org
{: #x7470494}

Véase [organización](#x2032585).

### organización (org)
{: #x2032585}

El metaobjeto de nivel superior de la infraestructura de {{site.data.keyword.edge_notm}} que representa los objetos de un cliente.

## P
{: #glossp}

### patrón
{: #x62309389}

Consulte [patrón de despliegue](#x623093810).

### volumen persistente
{: #x9532496}

Almacenamiento en red en un clúster que suministra un administrador.

### reclamación de volumen persistente
{: #x9520297}

Solicitud de almacenamiento en clúster.

### pod
{: #x8461823}

Grupo de contenedores que se ejecutan en un clúster de Kubernetes. Un pod es una unidad de trabajo ejecutable, que puede ser una aplicación autónoma o un microservicio.

### política de seguridad de pods
{: #x9520302}

Política que se utiliza para configurar un control a nivel de clúster con relación a lo que un pod puede hacer y a lo que puede acceder.

### policy
{: #x62309382}

Colección de cero o más propiedades y cero o más restricciones, en ocasiones con campos de datos adicionales. Consulte [política de nodo](#x62309384), [política de servicios](#x62309385) y [política de despliegue](#x62309386).

### Prometheus
{: #x9773892}

kit de herramientas de alertas y supervisión de sistemas de código abierto.

### propiedades
{: #x62309381}

Pares nombre/valor, a menudo utilizados para describir atributos del nodo (como el modelo, el número de serie, el rol, las prestaciones, el hardware conectado, etc.) o atributos de un servicio o despliegue. Consulte [política](#x62309382).

### nodo proxy
{: #x6230938}

Nodo que transmite solicitudes externas a los servicios que se crean dentro de un clúster.

## R
{: #glossr}

### RBAC
{: #x5488132}

Véase [control de acceso basado en roles](#x2403611).

### registro
{: #x2064940}

Servicio de almacenamiento y distribución de imágenes de contenedor público o privado. Véase también [contenedor](#x2010901), [imagen](#x2024928).

### repositorio
{: #x7639721}

Véase [repositorio](#x2036865).

### repositorio
{: #x2036865}

Área de almacenamiento persistente para datos y otros recursos de las aplicaciones.

### recurso
{: #x2004267}

Componente físico o lógico que se puede suministrar o reservar para una instancia de servicio o aplicación. Los ejemplos de recursos incluyen base de datos, cuentas y límites de procesador, memoria y almacenamiento.

### control de acceso basado en roles (RBAC)
{: #x2403611}

Proceso de restricción de componentes integrales de un sistema basado en la autenticación de usuario, los roles y los permisos.

## S
{: #glosss}

### intermediario de servicio
{: #x7636561}

Componente de un servicio que implementa un catálogo de ofertas y planes de servicio, e interpreta las llamadas para el suministro y la anulación de suministro, el enlace y el desenlace.

### política de servicios
{: #x62309385}

Conjunto de propiedades y restricciones relacionadas con un servicio desplegable específico.

### nodo de almacenamiento
{: #x3579301}

Nodo que se utiliza para proporcionar el almacenamiento de fondo y el sistema de archivos para almacenar los datos en un sistema.

### syslog
{: #x3585117}

Véase [registro del sistema](#x2178419).

### registro del sistema (syslog)
{: #x2178419}

Registro que generan los componentes de Cloud Foundry.

## T
{: #glosst}

### equipo
{: #x3135729}

Entidad que agrupa a usuarios y recursos.

## V
{: #glossv}

### VSAN
{: #x4592600}

Véase [red de área de almacenamiento virtual](#x4592596).

## W
{: #glossw}

### nodo de trabajador
{: #x5503637}

En un clúster, máquina física o virtual que transporta los despliegues y los servicios que componen una aplicación.

### carga de trabajo
{: #x2012537}

Colección de servidores virtuales que llevan a cabo una finalidad colectiva definida por el cliente. Una carga de trabajo generalmente se puede ver como una aplicación de varios niveles. Cada carga de trabajo está asociada con un conjunto de políticas que definen los objetivos de rendimiento y consumo de energía.
