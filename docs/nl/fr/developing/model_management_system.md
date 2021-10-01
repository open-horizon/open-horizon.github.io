---

copyright:
years: 2020
lastupdated: "2020-02-6"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Hello world à l'aide de la gestion des modèles
{: #model_management_system}

Cet exemple vous aide à développer un {{site.data.keyword.edge_service}} ({{site.data.keyword.ieam}}) qui utilise le système de gestion des modèles (MMS). Vous pouvez recourir à ce système pour déployer et mettre à jour les modèles d'apprentissage automatique utilisés par les services de périphérie qui s'exécutent sur vos noeuds de périphérie.
{:shortdesc}

## Avant de commencer
{: #mms_begin}

Effectuez les étapes préalables décrites dans la section [Préparation de la création d'un service de périphérie](service_containers.md). Ainsi, les variables d'environnement ci-dessous doivent être définies, les commandes doivent être installées et les fichiers doivent exister :

```bash
echo "HZN_ORG_ID=$HZN_ORG_ID, HZN_EXCHANGE_USER_AUTH=$HZN_EXCHANGE_USER_AUTH, DOCKER_HUB_ID=$DOCKER_HUB_ID" which git jq make ls ~/.hzn/keys/service.private.key ~/.hzn/keys/service.public.pem cat /etc/default/horizon
```
{: codeblock}

## Procédure
{: #mms_procedure}

Cet exemple fait partie du projet open source [{{site.data.keyword.horizon_open}}](https://github.com/open-horizon/). Suivez les étapes de la page [Creating Your Own Hello MMS Edge Service](https://github.com/open-horizon/examples/blob/master/edge/services/helloMMS/CreateService.md)), puis revenez ici.

## Etape suivante
{: #mms_what_next}

* Testez les autres exemples de service de périphérie de la rubrique [Développement d'un service de périphérie pour les dispositifs](../OH/docs/developing/developing.md).

## Lecture supplémentaire

* [Système de gestion des modèles](../OH/docs/developing/model_management_details.md)
