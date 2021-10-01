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

**Avance de novedades tecnológicas**: actualmente el soporte de SDO
sólo se debe utilizar para probar el proceso de SDO y familiarizarse con él,
a fin de planificar su uso en el futuro. En un futuro release, el soporte de SDO estará disponible
para utilizarse en producción.

[SDO ![Se abre en otro separador](../../images/icons/launch-glyph.svg "Se abre en otro separador")](https://software.intel.com/en-us/secure-device-onboard) (Incorporación de dispositivo seguro) es una tecnología creada por Intel para facilitar y asegurar la configuración de dispositivos periféricos y asociarlos con un centro de gestión periférico. {{site.data.keyword.edge_notm}}
({{site.data.keyword.ieam}}) ha añadido soporte para dispositivos habilitados para SDO
para que el agente se instale en el dispositivo y se registre en el centro de gestión de
{{site.data.keyword.ieam}} sin tocar nada (simplemente encendiendo en el dispositivo).

## Visión general de SDO
{: #sdo-overview}

SDO consta de cuatro componentes:

1. El módulo SDO en el dispositivo periférico (normalmente instalado allí por el fabricante de dispositivo)
2. Un cupón de propiedad (un archivo que se proporciona al comprador del dispositivo junto con
el dispositivo físico)
3. El servidor de encuentro SDO (el servidor conocido con el que un dispositivo habilitado para SDO
se pone en contacto por primera vez cuando arranca por primera vez)
4. Servicios de propietario de SDO (servicios ejecutados con el centro de gestión de
{{site.data.keyword.ieam}} que conectan el dispositivo a esta instancia específica de
{{site.data.keyword.ieam}})

### Diferencias en el avance de novedades tecnológicas
{: #sdo-tech-preview-differences}

- **Dispositivo habilitado para SDO:** para pruebas de SDO, se proporciona un script
para añadir el módulo SDO a una máquina virtual, para que se comporte de la misma manera que lo hace
un dispositivo habilitado para SDO al arrancar. Esto le permite probar la integración de SDO con
{{site.data.keyword.ieam}} sin tener que comprar un dispositivo habilitado para SDO.
- **Cupón de propiedad:** normalmente recibirá un cupón de propiedad del
fabricante del dispositivo. Si utiliza el script mencionado en la viñeta anterior para añadir el módulo SDO a
una máquina virtual, también creará el cupón de propiedad en la máquina virtual. La copia de ese cupón de la
máquina virtual representa "recibir el cupón de propiedad del fabricante de dispositivo."
- **Servidor de encuentro:** en producción, el dispositivo de arranque
se pondrá en contacto con el servidor de encuentro de SDO de Intel. Para el
desarrollo y la prueba de este avance de novedades tecnológicas, utilizará un servidor de encuentro
de desarrollo que se empaqueta con los servicios de propietario de SDO. 
- **Servicios de propietario de SDO:** en este avance de novedades tecnológicas.
los servicios de propietario de SDO no se instalarán automáticamente en el centro de gestión de
{{site.data.keyword.ieam}}  En lugar de ello, proporcionamos un script de utilidad
para iniciar los servicios de propietario de SDO en cualquier servidor que tenga acceso de red
al centro de gestión de {{site.data.keyword.ieam}} y que los dispositivos SDO puedan tener acceso
a través de la red.

## Utilización de SDO
{: #using-sdo}

Para probar SDO y verlo instalar automáticamente el agente de {{site.data.keyword.ieam}} y registrarlo en el centro de gestión de {{site.data.keyword.ieam}}, siga los pasos del [repositorio de soporte open-horizon/SDO ![Se abre en otro separador](../../images/icons/launch-glyph.svg "Se abre en otro separador")](https://github.com/open-horizon/SDO-support/blob/master/README.md).
