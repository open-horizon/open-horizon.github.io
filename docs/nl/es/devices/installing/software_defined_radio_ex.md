---

copyright:
years: 2020
lastupdated: "2020-02-5" 

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Proceso periférico de radio definida por software
{: #defined_radio_ex}

Este ejemplo utiliza la radio definida por software (SDR) como ejemplo de proceso periférico. Con SDR,
puede enviar datos en bruto a través del espectro de radio completo a un servidor de nube para su proceso. El
nodo periférico procesa los datos localmente y a continuación envía menos volumen de datos más valiosos
a un servicio de procesamiento de nube para su proceso adicional.
{:shortdesc}

Este diagrama muestra la arquitectura de este ejemplo de SDR:

<img src="../../images/edge/08_sdrarch.svg" width="70%" alt="Arquitectura de ejemplo">

El proceso periférico SDR es un ejemplo completo que consume audio de estación de radio,
extrae voz y convierte la voz extraída en texto. El ejemplo completa el análisis de emoción sobre el texto y hace que los datos y los resultados estén disponibles a través de una interfaz de usuario en la que puede ver los detalles de los datos para cada nodo periférico. Utilice este ejemplo para obtener más información sobre el proceso periférico.

SDR recibe señales de radio utilizando el circuito digital en una CPU de sistema para manejar el trabajo
de necesitar un conjunto de circuitos analógicos especializados. Ese circuito analógico
está normalmente restringido por la amplitud del espectro de radio que puede recibir. Un receptor
de radio analógico construido para recibir estaciones de radio FM, por ejemplo, no puede recibir señales de radio
de ningún otro lugar del espectro de radio. El SDR puede acceder a grandes sectores del espectro. Si no
tiene el hardware de SDR, puede utilizar datos simulados. Cuando utiliza datos simulados, el audio de la corriente de Internet se trata como si se transmitiera a través de FM y se recibiera en el nodo periférico.

Antes de realizar esta tarea, registre y anule el registro del dispositivo periférico realizando los pasos de
[Instalación del agente](registration.md).

Este código contiene estos componentes principales.

|Componente|Descripción|
|---------|-----------|
|[Servicio sdr ![Se abre en otro separador](../../images/icons/launch-glyph.svg "Se abre en otro separador")](https://github.com/open-horizon/examples/tree/master/edge/services/sdr)|El servicio de nivel inferior accede al hardware del nodo periférico|
|[Servicio ssdr2evtstreams ![Se abre en otro separador](../../images/icons/launch-glyph.svg "Se abre en otro separador")](https://github.com/open-horizon/examples/tree/master/edge/evtstreams/sdr2evtstreams)|El servicio de nivel superior recibe datos del servicio de sdr de nivel inferior y realiza
el análisis local de los datos en el nodo periférico. A continuación, el servicio sdr2evtstreams envía
los datos procesados al software de programa de fondo en la nube.|
|[Software de programa de fondo en la nube ![Se abre en otro separador](../../images/icons/launch-glyph.svg "Se abre en otro separador")](https://github.com/open-horizon/examples/tree/master/cloud/sdr)|El
software de programa de fondo en la nube recibe datos de los nodos periféricos para realizar un análisis adicional. La implementación de programa de fondo puede presentar entonces un mapa de nodos periféricos y más cosas dentro de una interfaz de usuario basada en web.|
{: caption="Tabla 1. Radio definida por software para los componentes principalesde {{site.data.keyword.message_hub_notm}}" caption-side="top"}


## Registro del dispositivo

Aunque este servicio se puede ejecutar utilizando datos simulados en cualquier dispositivo periférico,
si está utilizando un dispositivo periférico como Raspberry Pi con el hardware de SDR, configure primero un módulo
de kernel para soportar el hardware SDR. Debe configurar manualmente este módulo. Los contenedores de Docker
pueden establecer una distribución diferente de Linux en los contextos, pero el contenedor no puede instalar
los módulos de kernel. 

Complete estos pasos para configurar este módulo:

1. Como usuario root, cree un archivo llamado `/etc/modprobe.d/rtlsdr.conf`.
   ```
   sudo nano /etc/modprobe.d/rtlsdr.conf
   ```
   {: codeblock}

2. Añada las líneas siguientes al archivo:
   ```
   blacklist rtl2830
     blacklist rtl2832
     blacklist dvb_usb_rtl28xxu
   ```
   {: codeblock}

3. Guarde el archivo y, a continuación, reinicie antes de continuar:
   ```
   sudo reboot
   ```
   {: codeblock}   

4. Establezca la clave de API de {{site.data.keyword.message_hub_notm}} en su entorno. Esta
clave se crea para utilizarla con este ejemplo y se utiliza para alimentar con los datos procesados recopilados por
el nodo periférico a la interfaz de usuario de radio definida por el software de IBM.
   ```
   export EVTSTREAMS_API_KEY=X2e8cSjbDAMk-ztJLaoi3uffy8qsQTnZttUjcHCfm7cp
    export EVTSTREAMS_BROKER_URL=broker-3-y420pyyyvhhmttz0.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-5-y420pyyyvhhmttz0.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-4-y420pyyyvhhmttz0.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-1-y420pyyyvhhmttz0.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-0-y420pyyyvhhmttz0.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-2-y420pyyyvhhmttz0.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093
   ```
   {: codeblock}

5. Para ejecutar el ejemplo de servicio sdr2evtstreams en el nodo periférico,
debe registrar el nodo periférico en el patrón de despliegue de IBM/pattern-ibm.sdr2evtstreams. Realice los pasos de [Condiciones previas para utilizar el SDR en el servicio periférico de ejemplo de IBM Event Streams ![Se abre en otro separador](../../images/icons/launch-glyph.svg "Se abre en otro separador")](https://www.ibm.com/links?url=https%3A%2F%2Fgithub.com%2Fopen-horizon%2Fexamples%2Ftree%2Fmaster%2Fedge%2Fevtstreams%2Fsdr2evtstreams). 

6. Compruebe la interfaz de usuario web de ejemplo para ver si el nodo periférico está enviando resultados. Para obtener más información, consulte [Interfaz de usuario web de ejemplo de radio definida por software ![Se abre en otro separador](../../images/icons/launch-glyph.svg "Se abre en otro separador")](https://sdr-poc-sdr-poc-app-delightful-leopard.mybluemix.net). Inicie
la sesión con estas credenciales:

   * Nombre de usuario: guest@ibm.com
   * Contraseña: guest123

## Detalles de implementación de SDR

### Servicio de nivel bajo sdr
{: #sdr}

El nivel más bajo de la pila de software para este servicio incluye la implementación
de servicio `sdr`. Este servicio accede al hardware de radio definido por el software
local utilizando la popular biblioteca `librtlsdr` y los programas de utilidad
`rtl_fm` y `rtl_power` derivados junto con
el daemon `rtl_rpcd`. Para obtener más información acerca de la biblioteca `librtlsdr`, consulte [librtlsdr ![Se abre en otro separador](../../images/icons/launch-glyph.svg "Se abre en otro separador")](https://github.com/librtlsdr/librtlsdr).

El servicio `sdr` controla directamente el hardware de radio definido por el software
para ajustar el hardware a una frecuencia determinada para recibir los datos transmitidos o para
medir la potencia de señal en un espectro especificado. Se puede ajustar un flujo de trabajo típico
para el servicio a una frecuencia determinada para recibir datos de la estación en esa frecuencia.
A continuación, el servicio puede procesar los datos recopilados.

### servicio de alto nivel sdr2evtstreams
{: #sdr2evtstreams}

La implementación de servicio de alto nivel `sdr2evtstreams` utiliza la API REST de
servicio `sdr` y la API REST de servicio `gps`
a través de la red privada virtual de Docker local. El servicio `sdr2evtstreams` recibe datos
del servicio `sdr` y realiza alguna inferencia local en los datos para seleccionar
las mejores estaciones para voz. A continuación, el servicio `sdr2evtstreams`
utiliza Kafka para publicar clips de audio en la nube utilizando
{{site.data.keyword.message_hub_notm}}.

### IBM Functions
{: #ibm_functions}

IBM Functions orquesta el lado de nube de la aplicación de radio definido por el software de ejemplo.
IBM Functions se basa en OpenWhisk y permiten la informática sin servidor. La
informática sin servidor significa que los componentes de código se pueden desplegar sin ninguna
infraestructura de soporte, por ejemplo un sistema operativo o sistema de lenguaje de programación.
Mediante el uso de IBM Functions puede concentrarse en su propio código y dejar que IBM
maneje el escalado, la seguridad y el mantenimiento continuo de todo lo demás.
No hay que suministrar ningún hardware: no se necesitan máquinas virtuales ni contenedores.

Los componentes de código sin servidor se configuran para que se desencadenen (ejecuten)
en respuesta a los sucesos. En este ejemplo, el suceso desencadenante es la recepción de mensajes de los nodos
periféricos en {{site.data.keyword.message_hub_notm}} siempre que
los nodos periféricos publican clips de audio en
{{site.data.keyword.message_hub_notm}}. Las acciones de ejemplo se desencadenan para ingerir
los datos y actuar en ellos. Utilizan el servicio de IBM Watson Speech-To-Text (STT) para convertir a texto
los datos de audio de entrada. A continuación, dicho texto se envía al servicio de IBM Watson
Natural Language Understanding (NLU) para que analice el sentimiento que se expresa a cada
uno de los nombres que contiene. Para obtener más información, consulte [Código de acción de IBM Functions ![Se abre en otro separador](../../images/icons/launch-glyph.svg "Se abre en otro separador")](https://github.com/open-horizon/examples/blob/master/cloud/sdr/data-processing/ibm-functions/actions/msgreceive.js).

### Base de datos de IBM
{: #ibm_database}

El código de acción de IBM Functions concluye almacenando los resultados de sentimiento calculados en las
bases de datos de IBM. A continuación, el software de cliente y servidor web trabajan para presentar estos datos a
los navegadores web de usuario desde la base de datos. 

### Interfaz web
{: #web_interface}

La interfaz de usuario de web para la aplicación de radio definido por el software permite a los usuarios
examinar los datos de sentimiento, que se presentan desde las bases de datos de IBM. Esta interfaz de usuario
también representa un mapa que muestra los nodos periféricos que han proporcionado los datos. El
mapa se crea con datos del servicio `gps` proporcionado por IBM,
utilizado por el código de nodo periférico para el servicio `sdr2evtstreams`. El servicio
`gps` puede intercambiar información con el hardware GPS o recibir información del
propietario de dispositivo acerca de la ubicación. En ausencia de ambos, el hardware GPS y
la ubicación de propietario de dispositivo, el servicio `gps` puede
estimar la ubicación de nodo periférico utilizando la dirección IP de nodo periférico
para buscar la ubicación geográfica. Mediante este servicio, `sdr2evtstreams` puede
proporcionar datos de ubicación a la nube cuando el servicio envía clips de audio. Para obtener más información, consulte [Código de interfaz de usuario web de aplicación de radio definido por el software ![Se abre en otro separador](../../images/icons/launch-glyph.svg "Se abre en otro separador")](https://github.com/open-horizon/examples/tree/master/cloud/sdr/ui/sdr-app).

Opcionalmente, se pueden desplegar el código de IBM Functions,  bases de datos de IBM e
interfaz de usuario web en IBM Cloud si desea crear su propia interfaz de usuario web
de ejemplo de radio definida por el software. Puede hacerlo con un único mandato después de [crear una cuenta de pago ![Se abre en otro separador](../../images/icons/launch-glyph.svg "Se abre en otro separador")](https://cloud.ibm.com/login). Para obtener más información, consulte [contenido de repositorio de despliegue ![Se abre en otro separador](../../images/icons/launch-glyph.svg "Se abre en otro separador")](https://www.ibm.com/links?url=https%3A%2F%2Fgithub.com%2Fopen-horizon%2Fexamples%2Ftree%2Fmaster%2Fcloud%2Fsdr%2Fdeploy%2Fibm). 

Nota: Este proceso de despliegue necesita servicios de pago que incurren en cargos en
la cuenta de {{site.data.keyword.cloud_notm}}.

## Qué hacer a continuación

Si desea desplegar su propio software en un nodo periférico, debe crear sus propios servicios periféricos y el patrón de despliegue asociado o la política de despliegue. Para
obtener más información, consulte [Desarrollo de un servicio periférico para dispositivos](../developing/developing.md).
