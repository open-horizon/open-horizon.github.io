---

copyright:
years: 2019
lastupdated: "2019-06-24"  

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Création de votre propre service de périphérie Hello world
{: #dev_start_ex}

L'exemple ci-dessous s'appuie sur un service `Hello World` simple pour vous aider à en savoir plus sur le développement pour {{site.data.keyword.edge_devices_notm}} ({{site.data.keyword.ieam}}). Vous allez développer un service de périphérie unique qui prend en charge trois architectures matérielles et utilise les outils de développement {{site.data.keyword.horizon}}.
{:shortdesc}

## Avant de commencer
{: #dev_start_ex_begin}

Effectuez les étapes préalables décrites dans la section [Préparation de la création d'un service de périphérie](service_containers.md). Ainsi, les variables d'environnement ci-dessous doivent être définies, les commandes doivent être installées et les fichiers doivent exister :
```
echo "HZN_ORG_ID=$HZN_ORG_ID, HZN_EXCHANGE_USER_AUTH=$HZN_EXCHANGE_USER_AUTH, DOCKER_HUB_ID=$DOCKER_HUB_ID"
which git jq make
ls ~/.hzn/keys/service.private.key ~/.hzn/keys/service.public.pem
cat /etc/default/horizon
```

## Procédure
{: #dev_start_ex_procedure}

Cet exemple fait partie du projet [{{site.data.keyword.horizon_open}} ![S'ouvre dans un nouvel onglet](../../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://github.com/open-horizon/) en open source. Suivez les étapes de la page [Building and Publishing Your Own Hello World Example Edge Service ![S'ouvre dans un nouvel onglet](../../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://github.com/open-horizon/examples/blob/master/edge/services/helloworld/CreateService.md#build-publish-your-hw), puis revenez ici.

## Etape suivante
{: #dev_start_ex_what_next}

* Testez les autres exemples de service de périphérie de la rubrique [Développement de services de périphérie avec {{site.data.keyword.edge_devices_notm}}](developing.md).
