---

copyright:
years: 2019, 2020
lastupdated: "2020-01-22"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Preparación de un dispositivo periférico
{: #installing_the_agent}

Las instrucciones siguientes le guían a través del proceso de instalación del software necesario en el dispositivo periférico y de registrarlo con {{site.data.keyword.edge_notm}} {{site.data.keyword.ieam}}.

## Arquitecturas y sistemas operativos soportados
{: #suparch-horizon}

{{site.data.keyword.ieam}} da soporte a los sistemas con las arquitecturas de hardware siguientes:

* Dispositivos o máquinas virtuales de {{site.data.keyword.linux_bit_notm}} que ejecutan Ubuntu 18.x (bionic), Ubuntu 16.x (xenial), Debian 10 (buster) o Debian 9 (stretch)
* {{site.data.keyword.linux_notm}} en ARM (32 bits), por ejemplo Raspberry Pi que ejecuta Raspbian buster o stretch
* {{site.data.keyword.linux_notm}} en ARM (64 bits), por ejemplo NVIDIA Jetson Nano, TX1 o TX2 que ejecuta Ubuntu 18.x (bionic)
* {{site.data.keyword.macOS_notm}}

## Dimensionamiento
{: #size}

El agente requiere:

1. 100 MB RAM (incluido docker). La RAM aumenta por encima de esta cantidad en aproximadamente 100 K por acuerdo, además de cualquier memoria adicional necesaria para las cargas de trabajo que se ejecutan en el dispositivo.
2. 400 MB de disco (incluido docker). El disco aumenta por encima de esta cantidad en función del tamaño de las imágenes de contenedor utilizadas por las cargas de trabajo y del tamaño de los objetos de modelo (multiplicado por 2) que se despliegan en el dispositivo.

# Instalación del agente
{: #installing_the_agent}

Las instrucciones siguientes le guían a través del proceso de instalación del software necesario en el dispositivo periférico y de registrarlo con {{site.data.keyword.ieam}}.

## Procedimientos
{: #install-config}

Para instalar y configurar el dispositivo periférico, pulse el enlace que representa el tipo de dispositivo periférico:

* [Dispositivos o máquinas virtuales de {{site.data.keyword.linux_bit_notm}}](#x86-machines)
* [{{site.data.keyword.linux_notm}} en ARM (32 bits)](#arm-32-bit); por ejemplo, Raspberry Pi ejecutando Raspbian
* [{{site.data.keyword.linux_notm}} en ARM (64 bits)](#arm-64-bit); por ejemplo, NVIDIA Jetson Nano, TX1 o TX2
* [{{site.data.keyword.macOS_notm}}](#mac-os-x)

## Dispositivos o máquinas virtuales de {{site.data.keyword.linux_bit_notm}}
{: #x86-machines}

### Requisitos de hardware
{: #hard-req-x86}

* Dispositivo Intel o AMD de 64-bits en máquina virtual
* Una conexión a Internet para el dispositivo (por cable o wifi)
* (Opcional) Hardware de sensor: muchas aplicaciones de conocimiento de {{site.data.keyword.horizon}} pueden necesitar hardware de sensor especializado.

### Procedimiento
{: #proc-x86}

Prepare el dispositivo instalando un {{site.data.keyword.linux_notm}} Debian o Ubuntu. Las instrucciones de este contenido se basan en un dispositivo que utiliza Ubuntu 18.x.

Ahora que el dispositivo periférico está preparado, continúe en [Instalación del agente](registration.md).

## {{site.data.keyword.linux_notm}} en ARM (32 bits)
{: #arm-32-bit}

### Requisitos de hardware
{: #hard-req-pi}

* Raspberry Pi 3A+, 3B, 3B+ o 4 (preferentemente)
* Raspberry Pi A+, B+, 2B, Zero-W o Zero-WH
* Tarjeta flash MicroSD (32 GB preferentemente)
* Una fuente de alimentación apropiada para el dispositivo (2 Amp o superior preferentemente)
* Una conexión a Internet para el dispositivo (por cable o wifi).
  Nota: algunos dispositivos pueden necesitar hardware adicional para soportar wifi.
* (Opcional) Hardware de sensor: muchas aplicaciones de conocimiento de
{{site.data.keyword.horizon}} pueden necesitar hardware de sensor especializado.

### Procedimiento
{: #proc-pi}

1. Prepare el dispositivo Raspberry Pi.
   1. Muestre la imagen de [Raspbian ![Se abre en otro separador](../../images/icons/launch-glyph.svg "Se abre en otro separador")](https://www.raspberrypi.org/downloads/raspbian/) {{site.data.keyword.linux_notm}} en la tarjeta MicroSD.

      Para obtener más información acerca de cómo copiar imágenes MicroSD de muchas plataformas, consulte [Raspberry Pi Foundation ![Se abre en otro separador](../../images/icons/launch-glyph.svg "Se abre en otro separador")](https://www.raspberrypi.org/documentation/installation/installing-images/README.md).
      Estas instrucciones utilizan configuraciones de Raspbian para wifi y SSH.  

      **Aviso:** al copiar una imagen en la tarjeta MicroSD se borran permanentemente los datos que haya en la tarjeta.

   2. (Opcional) Si va a utilizar wifi para conectar con el dispositivo, edite la imagen recién copiada para proporcionar las credenciales de wifi WPA2 adecuadas. 

      Si va a utilizar una conexión de red por cable, no es necesario seguir este paso.  

      En la tarjeta MicroSD cree un archivo llamado `wpa_supplicant.conf` en la carpeta de nivel raíz, que contenga las credenciales de wifi. Estas credenciales incluyen el nombre de SSID de red y la frase de contraseña. Utilice el formato siguiente para el archivo: 
      
      ```
      country=US
      ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev update_config=1
      network={
      ssid=“<su-ssid-red>”
      psk=“<su-frase-contraseña-red”
      key_mgmt=WPA-PSK>
      }
      ```
      {: codeblock}

   3. (Opcional) Si desea o necesita ejecutar un dispositivo Raspberry Pi sin monitor o teclado, debe habilitar el acceso de conexión SSH al dispositivo. El acceso SSH está inhabilitado de forma predeterminada.

      Para habilitar la conexión SSH, cree un archivo vacío en la tarjeta MicroSD que se llame `ssh`. Incluya este archivo en la carpeta de nivel raíz de la tarjeta. La inclusión de este archivo proporciona la posibilidad de conectarse al dispositivo con las credenciales predeterminadas. 

   4. Desmonte la tarjeta MicroSD. Asegúrese de extraer la tarjeta de forma segura del dispositivo que está utilizando para editar la tarjeta, de modo que todos los cambios queden grabados.

   5. Inserte la tarjeta MicroSD en el dispositivo Raspberry Pi. Conecte cualquier hardware de sensor opcional y conecte el dispositivo a la fuente de alimentación.

   6. Inicie el dispositivo.

   7. Cambie la contraseña predeterminada para el dispositivo. En las imágenes flash de Raspbian, la cuenta predeterminada utiliza el nombre de inicio de sesión `pi` y la contraseña predeterminada `raspberry`.

      Inicie la sesión en esta cuenta. Utilice el mandato `passwd` de {{site.data.keyword.linux_notm}} estándar para cambiar la contraseña predeterminada:

      ```
      passwd
      Enter new UNIX password:  
      Retype new UNIX password:
      passwd: password updated successfully
      ```
      {: codeblock}

Ahora que el dispositivo periférico está preparado, continúe en
[Instalación del agente](registration.md).

## {{site.data.keyword.linux_notm}} en ARM (64 bits)
{: #arm-64-bit}

### Requisitos de hardware
{: #hard-req-nvidia}

* NVIDIA Jetson Nano o TX2 (recomendado)
* NVIDIA Jetson TX1
* HDMI Business Monitor, hub USB, teclado USB, ratón USB
* Almacenamiento: como mínimo 10 GB (se recomienda SSD)
* Una conexión a Internet para el dispositivo (por cable o wifi)
* (Opcional) Hardware de sensor: muchas aplicaciones de conocimiento de
{{site.data.keyword.horizon}} pueden necesitar hardware de sensor especializado.

### Procedimiento
{: #proc-nvidia}

1. Prepare el dispositivo NVIDIA Jetson.
   1. Instale el NVIDIA JetPack más reciente en el dispositivo. Para obtener más información, consulte:
      * (TX1) [Jetson TX1 ![se abre en otro separador](../../images/icons/launch-glyph.svg "Se abre en otro separador")](https://elinux.org/Jetson_TX1)
      * (TX2) [Harness AI at the Edge with the Jetson TX2 Developer Kit ![Se abre en otro separador](../../images/icons/launch-glyph.svg "Se abre en otro separador")](https://developer.nvidia.com/embedded/jetson-tx2-developer-kit)
      * (Nano) [Getting Started With Jetson Nano Developer Kit ![Se abre en otro separador](../../images/icons/launch-glyph.svg "Se abre en otro separador")](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit)

      Es necesario instalar este software y cualquier software de requisito previo antes de instalar el software de {{site.data.keyword.horizon}}.

   2. Cambie la contraseña predeterminada. En el procedimiento de instalación de JetPack, la cuenta predeterminada utiliza el nombre de inicio de sesión `nvidia` y la contraseña predeterminada `nvidia`. 

      Inicie la sesión en esta cuenta. Utilice el mandato `passwd` de {{site.data.keyword.linux_notm}} estándar para cambiar la contraseña predeterminada:

      ```
      passwd
      Enter new UNIX password:  
      Retype new UNIX password:
      passwd: password updated successfully
      ```
      {: codeblock}

Ahora que el dispositivo periférico está preparado, continúe en [Instalación del agente](registration.md).

## {{site.data.keyword.macOS_notm}}
{: #mac-os-x}

### Requisitos de hardware
{: #hard-req-mac}

* Dispositivo Mac {{site.data.keyword.inte
}} de 65 bits de 2010 o posterior

* Se necesita la virtualización MMU.
* MacOS X versión 10.11 ("El Capitán") o posterior
* Una conexión a Internet para la máquina (por cable o wifi)
* (Opcional) Hardware de sensor: muchas aplicaciones de conocimiento de {{site.data.keyword.horizon}} pueden necesitar hardware de sensor especializado.

### Procedimiento
{: #proc-mac}

1. Prepare el dispositivo.
   1. Instale la **versión más reciente de Docker** en el dispositivo. Para obtener más información, consulte [Instalar Docker ![Se abre en otro separador](../../images/icons/launch-glyph.svg "Se abre en otro separador")](https://docs.docker.com/docker-for-mac/install/).

   2. **Instale socat**. Puede utilizar **cualquiera** de los métodos siguientes para instalar socat:

      * [Use Homebrew to install socat ![Se abre en otro separador](../../images/icons/launch-glyph.svg "Se abre en otro separador")](https://brewinstall.org/install-socat-on-mac-with-brew/).
   
      * Si ya ha instalado MacPorts, utilícelo para instalar socat:
        ```
        sudo port install socat
        ```
        {: codeblock}

## Qué hacer a continuación

* [Actualización del agente](updating_the_agent.md)
* [Instalación del agente](registration.md)


## Información relacionada

* [Instalación del centro de gestión](../../hub/offline_installation.md)
* [Instalación y registro manuales avanzados de un agente ](advanced_man_install.md)
