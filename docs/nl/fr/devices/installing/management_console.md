---

copyright:
years: 2020
lastupdated: "2020-1-31"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Utilisation de la console d'{{site.data.keyword.edge_notm}}
{: #accessing_ui}

La console permet d'effectuer des fonctions de gestion de l'informatique Edge. 
 
## Navigation dans la console d'{{site.data.keyword.edge_notm}}

1. Accédez à la console d'{{site.data.keyword.edge_notm}} à partir de l'adresse `https://<cluster-url>/edge`, où `<cluster-url>` désigne le contrôleur ingress externe du cluster.
2. Entrez vos informations d'identification utilisateur. La page de connexion {{site.data.keyword.mcm}} s'affiche.
3. Dans la barre d'adresse de votre navigateur, retirez `/multicloud/welcome` de la fin de l'URL et ajoutez `/edge`, puis appuyez sur la touche **Entrée**. La page {{site.data.keyword.edge_notm}} s'affiche.

## Navigateurs pris en charge

{{site.data.keyword.edge_notm}} a été testé avec succès avec ces navigateurs.

|Plateforme|Navigateurs pris en charge|
|--------|------------------|
|Microsoft Windows™|<ul><li>Mozilla Firefox - version la plus récente pour Windows</li><li>Google Chrome - version la plus récente pour Windows</li></ul>|
|{{site.data.keyword.macOS_notm}}|<ul><li>Mozilla Firefox - version la plus récente pour Mac</li><li>Google Chrome - version la plus récente pour Mac</li></ul>|
{: caption="Tableau 1. Navigateurs pris en charge dans {{site.data.keyword.edge_notm}}" caption-side="top"}


## Découverte de la console d'{{site.data.keyword.edge_notm}}
{: #exploring-management-console}

Les fonctionnalités de la console d'{{site.data.keyword.edge_notm}} sont les suivantes :

* Processus d'intégration convivial grâce aux liens de site fournissant une solide prise en charge
* Fonctions de visibilité et de gestion étendues :
  * Vues graphiques complètes, comportant des informations sur le statut du noeud, l'architecture et les erreurs
  * Détails d'erreur avec les liens permettant de résoudre le problème
  * Informations relatives à l'emplacement et au filtrage, notamment : 
    * Propriétaire
    * Architecture 
    * Signal de présence (par exemple, les 10 dernières minutes, aujourd'hui, etc.)
    * Etat du noeud (Actif, Inactif, Comporte une erreur, etc.)
    * Type de déploiement (règle ou pattern)
  * Détails utiles sur les noeuds de périphérie Exchange, y compris :
    * Propriétés
    * Contraintes 
    * Déploiements
    * Services actifs

* Fonctions d'affichage puissantes

  * Possibilité de localiser et de filtrer rapidement par : 
    * Propriétaire
    * Architecture
    * Version
    * Public (true ou false)
  * Vues de services sous forme de liste ou de carte
  * Regroupement des services partageant un même nom
  * Détails sur chaque service Exchange, notamment : 
    * Propriétés
    * Contraintes
    * Déploiements
    * Variables de service
    * Dépendances de services
  
* Gestion des règles de déploiement

  * Possibilité de localiser et de filtrer rapidement par :
    * Identificateur de règle
    * Propriétaire
    * Etiquette
  * Déploiement des services à partir d'Exchange
  * Ajout de propriétés aux règles de déploiement
  * Générateur de contraintes pour les expressions 
  * Mode avancé d'écriture de contraintes directement dans le fichier JSON
  * Possibilité d'ajuster les retours vers une version de déploiement antérieure et les paramètres de santé du noeud
  * Affichage et modification des détails de la règle, notamment :
    * Propriétés de service et de déploiement
    * Contraintes
    * Retours vers une édition antérieure
    * Paramètres de santé du noeud
  
