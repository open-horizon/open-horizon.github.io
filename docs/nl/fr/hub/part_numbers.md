---

copyright:
years: 2020
lastupdated: "2020-02-10"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Passport Advantage
{: #part_numbers}

Procédez comme suit télécharger vos packages {{site.data.keyword.ieam}} :

1. Recherchez votre référence {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}).
2. Accédez à l'onglet IBM Passport Advantage Online sur [Passport Advantage](https://www.ibm.com/software/passportadvantage/) et connectez-vous avec votre ID IBM.
2. Recherchez vos fichiers à l'aide des numéros de référence répertoriés dans les [{{site.data.keyword.ieam}} packages et numéros de référence](#part_numbers_table) :
3. Téléchargez vos fichiers dans un répertoire de votre ordinateur.

## Packages et références d'{{site.data.keyword.ieam}}
{: #part_numbers_table}

|Description du composant|Référence Passport Advantage|
|----------------|------------------------------|
|{{site.data.keyword.edge_notm}}  Unité de valeur par ressource : Licence + Abonnement logiciel & Support 12 mois|D2840LL|
|{{site.data.keyword.edge_notm}}  Unité de valeur par ressource : Abonnement logiciel annuel & Renouvellement support 12 mois|E0R0HLL|
|{{site.data.keyword.edge_notm}}  Unité de valeur par ressource : Abonnement logiciel annuel & Rétablissement support 12 mois|D2841LL|
|{{site.data.keyword.edge_notm}}  Unité de valeur par ressource : Licence mensuelle|D283ZLL|
|{{site.data.keyword.edge_notm}}  Licence temporaire validée par l'unité de valeur par ressource|D28I1LL|
{: caption="Tableau 1. Packages et références d'{{site.data.keyword.ieam}}" caption-side="top"}

## Licence
{: #licensing}

Les exigences en matière de licence sont calculées sur la base du total des noeuds enregistrés. Sur n'importe quel système ayant installé l'interface de ligne de commande **hzn** qui a été configurée pour l'authentification auprès de votre concentrateur de gestion, déterminez le nombre total de noeuds enregistrés :

  ```
  hzn exchange status | jq .numberOfNodes
  ```
  {: codeblock}

La sortie est un entier, comme dans l'exemple suivant :

  ```
  $ hzn exchange status | jq .numberOfNodes   2641
  ```

Utilisez le tableau de conversion suivant dans le [{{site.data.keyword.ieam}}document Licence](https://ibm.biz/ieam-43-license) pour calculer les licences requises, avec le nombre de nœuds renvoyé pour votre environnement par la commande précédente :

  ```
  From 1 to 10 Resources, 1.00 UVU per Resource   From 11 to 50 Resources, 10.0 UVUs plus 0.87 UVUs per Resource above 10   From 51 to 100 Resources, 44.8 UVUs plus 0.60 UVUs per Resource above 50   From 101 to 500 Resources, 74.8 UVUs plus 0.25 UVUs per Resource above 100   From 501 to 1,000 Resources, 174.8.0 UVUs plus 0.20 UVUs per Resource above 500   From 1,001 to 10,000 Resources, 274.8 UVUs plus 0.07 UVUs per Resource above 1,000   From 10,001 to 25,000 Resources, 904.8 UVUs plus 0.04 UVUs per Resource above 10,000   From 25,001 to 50,000 Resources, 1,504.8 UVUs plus 0.03 UVUs per Resource above 25,000   From 50,001 to 100,000 Resources, 2,254.8 UVUs plus 0.02 UVUs per Resource above 50,000   For more than 100,000 Resources, 3,254.8 UVUs plus 0.01 UVUs per Resource above 100,000
  ```

L'exemple suivant présente le calcul des licences requises pour **2641** noeuds, qui nécessiterait l'achat d'**au moins 390** licences :

  ```
  274.8 + ( .07 * ( 2641 - 1000 ) )
  274.8 + ( .07 * 1641 )   274.8 + 114.87   389.67
  ```

## Génération de rapports sur la licence

{{site.data.keyword.edge_notm}} L'utilisation est automatiquement calculée et téléchargée périodiquement vers un service de licence commun installé localement sur votre cluster. Pour plus d'informations sur le service d'octroi de licences, notamment sur la manière de visualiser l'utilisation actuelle, de générer des rapports d'utilisation et plus encore, consultez la [documentation du service d'octroi de licences](https://www.ibm.com/docs/en/cpfs?topic=operator-overview).
