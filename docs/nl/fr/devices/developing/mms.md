---

copyright:
  years: 2019
lastupdated: "2019-06-24"

---

{:shortdesc: .shortdesc}
{:new_window: target="_blank"}
{:codeblock: .codeblock}
{:pre: .pre}
{:screen: .screen}
{:tip: .tip}
{:download: .download}

# Service de périphérie utilisant le service du système de gestion des modèles (MMS)
{: #mms}

L'exemple suivant vous aide à développer des {{site.data.keyword.edge_service}} qui font appel au système de gestion des modèles (MMS). Vous pouvez recourir à ce système pour déployer et mettre à jour les modèles d'apprentissage automatique utilisés par les services de périphérie qui s'exécutent sur vos noeuds de périphérie.
{:shortdesc}

## Avant de commencer
{: #mms_begin}

Effectuez les étapes préalables décrites dans la section [Préparation de la création d'un service de périphérie](service_containers.md). Ainsi, les variables d'environnement ci-dessous doivent être définies, les commandes doivent être installées et les fichiers doivent exister :

```bash
echo "HZN_ORG_ID=$HZN_ORG_ID, HZN_EXCHANGE_USER_AUTH=$HZN_EXCHANGE_USER_AUTH, DOCKER_HUB_ID=$DOCKER_HUB_ID"
which git jq make
ls ~/.hzn/keys/service.private.key ~/.hzn/keys/service.public.pem
cat /etc/default/horizon
```

## Procédure
{: #mms_procedure}

Cet exemple fait partie du projet [{{site.data.keyword.horizon_open}} ![S'ouvre dans un nouvel onglet](../../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://github.com/open-horizon/) en open source. Suivez les étapes de la page [Creating Your Own Hello MMS Edge Service ![S'ouvre dans un nouvel onglet](../../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://github.com/open-horizon/examples/blob/master/edge/services/helloMMS/CreateService.md), puis revenez ici.

## Etape suivante
{: #mms_what_next}

* Testez les autres exemples de service de périphérie de la rubrique [Développement de services de périphérie avec {{site.data.keyword.edge_devices_notm}}](developing.md).

## Lecture supplémentaire

* [Système de gestion des modèles](model_management_system.md)
