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

L'exemple ci-dessous s'appuie sur un service `Hello World` simple pour vous aider à en savoir plus sur le développement pour {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}). Vous allez développer un service de périphérie unique qui prend en charge trois architectures matérielles et utilise les outils de développement {{site.data.keyword.horizon}}.
{:shortdesc}

## Avant de commencer
{: #dev_start_ex_begin}

Effectuez les étapes préalables décrites dans la section [Préparation de la création d'un service de périphérie](service_containers.md). Ainsi, les variables d'environnement ci-dessous doivent être définies, les commandes doivent être installées et les fichiers doivent exister :
```
echo "HZN_ORG_ID=$HZN_ORG_ID, HZN_EXCHANGE_USER_AUTH=$HZN_EXCHANGE_USER_AUTH, DOCKER_HUB_ID=$DOCKER_HUB_ID" which git jq make ls ~/.hzn/keys/service.private.key ~/.hzn/keys/service.public.pem cat /etc/default/horizon
```
{: codeblock}

## Procédure
{: #dev_start_ex_procedure}

Cet exemple fait partie du projet open source [{{site.data.keyword.horizon_open}}](https://github.com/open-horizon/). Suivez les étapes de la page [Building and Publishing Your Own Hello World Example Edge Service](https://github.com/open-horizon/examples/blob/master/edge/services/helloworld/CreateService.md#build-publish-your-hw), puis revenez ici.

## Etape suivante
{: #dev_start_ex_what_next}

* Essayez les autres exemples de services de périphérie à la page [Développer un service de périphérie pour les appareils}](../OH/docs/developing/developing.md).
