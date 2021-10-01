---

copyright:
years: 2020
lastupdated: "2020-04-01"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Convenciones utilizadas en este documento
{: #document_conventions}

Este documento utiliza convenciones de contenido para transmitir un significado específico.  

## Convenciones de mandatos

Sustituya el contenido de variable que se muestra en < > por valores específicos para sus necesidades. No incluya caracteres < > en el mandato.

### Ejemplo

  ```
  hzn key create "<companyname>" "<su_dirección_correo_electrónico>"
  ```
  {: codeblock}
   
## Series literales

El contenido que se ve en el centro de gestión o en el código es una serie literal. Este contenido se muestra como texto en **negrita**.
   
 ### Ejemplo
   
 Si examina
el código `service.sh`, verá que utiliza estas variables de configuración y otras
para controlar el comportamiento. **PUBLISH** controla si el código intenta enviar
mensajes a IBM Event Streams. **MOCK** controla si service.sh intenta
ponerse en contacto con las API REST y sus servicios dependientes (cpu y gps) o si
`service.sh` crea datos falsos.
  
