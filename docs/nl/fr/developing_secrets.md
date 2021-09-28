---

copyright:
years: 2021
lastupdated: "2021-08-16"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Hello world avec un secret
{: #secrets}

Cet exemple vous apprend à développer un {{site.data.keyword.edge_service}} qui utilise des secrets. Les secrets veillent à ce que les données d'identification de connexion et les autres informations sensibles soient conservées en lieu sûr.
{:shortdesc}

## Avant de commencer
{: #secrets_begin}

Effectuez les étapes préalables décrites dans la section [Préparation de la création d'un service de périphérie](service_containers.md). Ainsi, les variables d'environnement ci-dessous doivent être définies, les commandes doivent être installées et les fichiers doivent exister :

```bash
echo "HZN_ORG_ID=$HZN_ORG_ID, HZN_EXCHANGE_USER_AUTH=$HZN_EXCHANGE_USER_AUTH, DOCKER_HUB_ID=$DOCKER_HUB_ID" which git jq make ls ~/.hzn/keys/service.private.key ~/.hzn/keys/service.public.pem cat /etc/default/horizon
```

## Procédure
{: #secrets_procedure}

Cet exemple fait partie du projet open source [{{site.data.keyword.horizon_open}}](https://github.com/open-horizon/). Suivez les étapes de la section [Création de votre propre service Hello Secret](https://github.com/open-horizon/examples/blob/master/edge/services/helloSecretWorld/CreateService.md)), puis revenez ici.

## Etape suivante
{: #secrets_what_next}

* Testez les autres exemples de service de périphérie de la rubrique [Développement d'un service de périphérie pour les dispositifs](developing.md).

## Lecture supplémentaire

* [Utilisation des secrets](../developing/secrets_details.md)
