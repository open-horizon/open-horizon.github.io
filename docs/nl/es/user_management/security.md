---

copyright:
years: 2019
lastupdated: "2019-09-04"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Seguridad 
{: #security}

{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}), basado en [Open Horizon](https://github.com/open-horizon), utiliza varias tecnologías de seguridad para garantizar su seguridad contra los ataques y proteger la privacidad. Para obtener más información sobre la seguridad y los roles de {{site.data.keyword.ieam}}, consulte:

* [Seguridad y privacidad](../OH/docs/user_management/security_privacy.md)
* [Control de acceso basado en roles](rbac.md)
* Consideraciones acerca de [{{site.data.keyword.edge_notm}} para la disposición de GDPR](gdpr.md)
{: childlinks}

Para obtener más información sobre la creación de claves de firma de carga de trabajo si todavía no tiene sus propias claves RSA, consulte [Preparación para crear un servicio periférico](../developing/service_containers.md). Utilice estas claves para firmar servicios al publicarlos en Exchange y habilitar el agente de {{site.data.keyword.ieam}} para verificar que ha iniciado una carga de trabajo válida.
