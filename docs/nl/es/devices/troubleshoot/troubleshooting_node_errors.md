---

copyright:
years: 2019
lastupdated: "2019-09-18"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Resolución de errores de nodo
{: #troubleshooting_node_errors}

{{site.data.keyword.edge_devices_notm}} publica un subconjunto de registros de sucesos en Exchange que se puede visualizar en la {{site.data.keyword.gui}}. Estos errores se enlazan a la orientación para la resolución de
{:shortdesc}

  - [error_image_load](#eil)
  - [error_in_deployment_configuration](#eidc)
  - [error_start_container](#esc)

## error_image_load
{: #eil}

Este error se produce cuando la imagen de servicio a la que se hace referencia en la definición de servicio no existe en el repositorio de imágenes. Para solucionar este error:

1. Vuelva a publicar el servicio sin el distintivo **-I**.
    ```
    hzn exchange service publish -f <archivo-definición-servicio>
    ```
    {: codeblock}

2. Envíe la imagen de servicio directamente al repositorio de imágenes. 
    ```
    docker push <nombre de imagen>
    ```
    {: codeblock} 
    
## error_in_deployment_configuration
{: #eidc}

Este error se produce cuando las configuraciones de despliegue de definiciones de servicio especifican un enlace a un archivo protegido por root. Para solucionar este error:

1. Enlace el contenedor con un archivo que no esté protegido por root.
2. Cambie los permisos de archivo para que los usuarios puedan leer y escribir en el archivo.

## error_start_container
{: #esc}

Este error se produce cuando docker encuentra un error al iniciar el contenedor de servicio. Es posible que el mensaje de error contenga detalles que indiquen por qué el inicio del contenedor ha fallado. Los pasos de resolución dependen del error. Se pueden producir los errores siguientes:

1. El dispositivo ya está utilizando un puerto publicado que se especifica en las configuraciones de despliegue. Para resolver el error: 

    - Correlacione un puerto diferente con el puerto de contenedor de servicio. El número de puerto visualizado no tiene que coincidir con el número de puerto de servicio.
    - Detenga el programa que está utilizando el mismo puerto.

2. Un puerto publicado que se especifica en las configuraciones de despliegue no es un número de puerto válido. Los números de puerto deben ser un número en el rango 1-65535.
3. Un nombre de volumen de las configuraciones de despliegue no es una vía de acceso de archivo válida. Las vías de acceso de volumen deben especificarse por sus vías de acceso absolutas (no relativas). 

## Información adicional

Para obtener más información, consulte:
  * [Guía de resolución de problemas de {{site.data.keyword.edge_devices_notm}}](../troubleshoot/troubleshooting.md)
