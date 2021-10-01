---

copyright:
years: 2020
lastupdated: "2020-4-24"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Installation et enregistrement d'agent SDO
{: #sdo}

[SDO](https://software.intel.com/en-us/secure-device-onboard) (Secure Device Onboard), créé par Intel, permet de configurer facilement et en toute sécurité les unités de périphérie et de les associer à un concentrateur de gestion de périphérie. {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) prend en charge les dispositifs compatibles SDO de sorte que l'agent soit installé sur les dispositifs et enregistré sur le concentrateur de gestion {{site.data.keyword.ieam}} sans intervention (par la simple mise sous tension des dispositifs).

## Présentation de SDO
{: #sdo-overview}

SDO est constitué des composants suivants :

* Le module SDO sur le dispositif de périphérie (généralement installé par le fabricant du dispositif)
* Un fichier coupon de propriété (fichier fourni à l'acquéreur avec le dispositif physique)
* Le serveur SDO rendezvous (le serveur bien connu qu'un dispositif compatible SDO contacte en premier lorsqu'il démarre pour la première fois)
* Services de propriétaire SDO (les services s'exécutent sur le concentrateur de gestion {{site.data.keyword.ieam}} qui configure l'unité afin qu'elle utilise cette instance spécifique d'{{site.data.keyword.ieam}})

**Remarque** : SDO prend uniquement en charge les dispositifs de périphérie et non les clusters de périphérie.

### Flux SDO

<img src="../OH/docs/images/edge/09_SDO_device_provisioning.svg" style="margin: 3%" alt="SDO installation overview">

## Avant de commencer
{: #before_begin}

SDO exige que les fichiers d'agent soient stockés dans le CSS {{site.data.keyword.ieam}} (Cloud Sync Service). Si cela n'a pas été fait, demandez à votre administrateur d'exécuter l'une des commandes suivantes, comme décrit dans [Collecter les fichiers de nœud de périphérie](../hub/gather_files.md) :

  `edgeNodeFiles.sh ALL -c ...`

## Essai de SDO
{: #trying-sdo}

Avant d'acheter des dispositifs de périphérie SDO, vous pouvez essayer le support SDO dans {{site.data.keyword.ieam}} avec une machine virtuelle simulant un dispositif de périphérie SDO :

1. Vous avez besoin d'une clé d'API. Pour obtenir des instructions sur la création d'une clé d'API, si vous n'en avez pas déjà, voir [Création de votre clé d'API](../hub/prepare_for_edge_nodes.md).

2. Contactez votre administrateur {{site.data.keyword.ieam}} pour obtenir les valeurs de ces variables d'environnement. (Vous en avez besoin à l'étape suivante.)

   ```bash
   export HZN_ORG_ID=<exchange-org>    export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>    export HZN_SDO_SVC_URL=https://<ieam-mgmt-hub-ingress>/edge-sdo-ocs/api    export HZN_MGMT_HUB_CERT_PATH=<path-to-mgmt-hub-self-signed-cert>    export CURL_CA_BUNDLE=$HZN_MGMT_HUB_CERT_PATH
   ```

3. Procédez comme indiqué dans le [référentiel open-horizon/SDO-support](https://github.com/open-horizon/SDO-support/blob/master/README-1.10.md) pour voir si SDO installe automatiquement l'agent {{site.data.keyword.ieam}} sur un dispositif, puis enregistrez-le auprès de votre concentrateur de gestion {{site.data.keyword.ieam}}.

## Ajout de dispositifs compatibles SDO à votre domaine {{site.data.keyword.ieam}}
{: #using-sdo}

Si vous avez acheté des dispositifs SDO et souhaitez les incorporer à votre domaine {{site.data.keyword.ieam}} :

1. [Connectez-vous à la {{site.data.keyword.ieam}} console de gestion](../console/accessing_ui.md).

2. Dans l'onglet **Noeuds**, cliquez sur **Ajouter un noeud**. 

   Entrez les informations nécessaires pour créer une clé de propriété privée dans le service SDO et téléchargez la clé publique correspondante.
   
3. Entrez les renseignements nécessaires pour importer les coupons de propriété que vous avez reçus lorsque vous avez acheté les dispositifs.

4. Connectez les dispositifs au réseau et mettez-les sous tension.

5. Dans la console de gestion, regardez la progression des unités en ligne en affichant la page de présentation **Noeud** et en filtrant le nom de l'installation.
