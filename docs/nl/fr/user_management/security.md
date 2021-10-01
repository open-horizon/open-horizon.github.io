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

# Sécurité 
{: #security}

{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}), basé sur [Open Horizon](https://github.com/open-horizon), utilise plusieurs technologies de sécurité pour s'assurer qu'il est protégé contre les attaques et qu'il protège la confidentialité. Pour plus d'informations sur la sécurité et les rôles dans {{site.data.keyword.ieam}}, voir :

* [Sécurité et confidentialité](../OH/docs/user_management/security_privacy.md)
* [Contrôle d'accès à base de rôles](rbac.md)
* [{{site.data.keyword.edge_notm}} - considérations relatives à la conformité au règlement RGPD](gdpr.md)
{: childlinks}

Pour plus d'informations sur la création de clés de signature de charge de travail si vous ne disposez pas déjà de vos propres clés RSA, voir [Préparation de la création d'un service de périphérie](../developing/service_containers.md). Utilisez ces clés pour signer les services lorsque vous les publiez dans Exchange et activez l'agent {{site.data.keyword.ieam}} pour vérifier qu'il a démarré une charge de travail valide.
