---

copyright:
years: 2019
lastupdated: "2019-11-17"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Exploración de la CLI de hzn
{: #exploring-hzn}

En los nodos periféricos de {{site.data.keyword.horizon}}, utilice el mandato `hzn` para inspeccionar muchos aspectos del estado del sistema local y del ecosistema de {{site.data.keyword.edge_notm}} más grande fuera del nodo periférico. Utilice el mandato `hzn` para interactuar con el sistema y cambiar el estado de los recursos que posee.

Puede obtener ayuda para el mandato `hzn`, incluyendo más detalles sobre cualquiera de los submandatos utilizando el distintivo `--help` (o `-h`) en cualquier nivel de submandato. Por ejemplo, intente los mandatos siguientes:

```
hzn --help hzn node --help hzn exchange pattern --help
```
{: codeblock}

Puede utilizar el distintivo `--verbose` (o `-v`) en el mandato `hzn` para proporcionar una salida más detallada. A menudo los mandatos `hzn` son envoltorios de conveniencia sobre las API REST proporcionadas por los componentes de {{site.data.keyword.horizon}} y el distintivo `--verbose` muestra normalmente los detalles de las interacciones de REST en segundo plano. Por ejemplo, pruebe lo siguiente:

```
hzn node list -v
```  
{: codeblock}

La salida de ese mandato muestra las dos invocaciones de método `GET` de REST en los URL de `localhost` donde el agente {{site.data.keyword.horizon}} local responde a las solicitudes REST.

Por ejemplo:

```
[verbose] GET http://localhost:8510/node [verbose] HTTP code: 200 ...
[verbose] GET http://localhost:8510/status [verbose] HTTP code: 200
```  
{: codeblock}
