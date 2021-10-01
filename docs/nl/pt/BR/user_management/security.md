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

# Segurança 
{: #security}

O {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}), com base em [Open Horizon](https://github.com/open-horizon), usa várias tecnologias de segurança para assegurar que é seguro contra ataques e protege a privacidade. Para obter mais informações sobre a segurança e as funções do {{site.data.keyword.ieam}}, consulte:

* [Segurança e privacidade](../OH/docs/user_management/security_privacy.md)
* [Controle de acesso baseado na função](rbac.md)
* [Considerações do {{site.data.keyword.edge_notm}} para a preparação para o RGPD](gdpr.md)
{: childlinks}

Para obter mais informações sobre a criação de chaves de assinatura de carga de trabalho, caso ainda não tenha suas próprias chaves RSA, consulte [Preparando para criar um serviço de borda](../developing/service_containers.md). Use essas chaves para assinar serviços ao publicá-los no Exchange e habilitar o agente {{site.data.keyword.ieam}} para verificar se ele iniciou uma carga de trabalho válida.
