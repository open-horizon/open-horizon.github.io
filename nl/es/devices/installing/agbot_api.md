---

copyright:
years: 2020
lastupdated: "2020-04-9"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# API de Agbot
{: #agbot_api}

En {{site.data.keyword.edge_notm}} ({{site.data.keyword.edge_ieam}}), el software de agbot
de {{site.data.keyword.horizon}} se ejecuta automáticamente. Cada agbot es responsable de comunicarse con todos los agentes que están registrados para ejecutar el patrón de despliegue asignado para el agbot, incluido cualesquiera servicios para el patrón. Los agbots negocian acuerdos a través de los agentes. Con las API REST de agbot puede configurar el agbot mediante `http://localhost:8046`. Los mandatos `hzn agbot` interactúan con estas API REST.

Para obtener más información, consulte [{{site.data.keyword.horizon}} agbot REST API ![Se abre en otro separador](../../images/icons/launch-glyph.svg "Se abre en otro separador")](https://github.com/open-horizon/anax/blob/master/doc/agreement_bot_api.md).

{{site.data.keyword.horizon_exchange}} también expone las API REST de configuración de agbot, a las que se accede mediante el mandato `hzn exchange agbot`.
