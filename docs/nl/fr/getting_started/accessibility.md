---

copyright:
  years: 2016, 2019
lastupdated: "2019-03-14"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Fonctions d'accessibilité

Les fonctions d'accessibilité aident les utilisateurs souffrant d'un handicap (comme une mobilité réduite ou une vision limitée) à se servir des contenus des technologies de l'information.
{:shortdesc}

## Présentation

{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) inclut les fonctions d'accessibilité majeures suivantes :

* Opérations par clavier uniquement
* Opérations par lecteur d'écran
* Interface de ligne de commande (CLI) permettant de gérer le cluster {{site.data.keyword.ieam}}

{{site.data.keyword.ieam}} utilise la norme W3C Standard la plus récente, [WAI-ARIA 1.0 ![Icône de lien externe](../images/icons/launch-glyph.svg "Icône de lien externe")](http://www.w3.org/TR/wai-aria/){: new_window}, afin de garantir la conformité avec les directives [Section 508 Standards for Electronic and Information Technology ![Icône de lien externe](../images/icons/launch-glyph.svg "Icône de lien externe")](http://www.access-board.gov/guidelines-and-standards/communications-and-it/about-the-section-508-standards/section-508-standards){: new_window} et [Web Content Accessibility Guidelines (WCAG) 2.0 ![Icône de lien externe](../images/icons/launch-glyph.svg "Icône de lien externe")](http://www.w3.org/TR/WCAG20/){: new_window}. Pour tirer parti des fonctions d'accessibilité, utilisez la dernière version de votre lecteur d'écran et du navigateur pris en charge par {{site.data.keyword.ieam}}.

La documentation du produit en ligne {{site.data.keyword.ieam}} dans la documentation IBM est activée pour l'accessibilité. Pour des informations d'ordre général sur l'accessibilité, voir [Accessibilité dans IBM ![Icône de lien externe](../images/icons/launch-glyph.svg "Icône de lien externe")](http://www.ibm.com/accessibility/us/en/){: new_window}.

## Hyperliens

Tous les liens externes, qui sont des liens vers du contenu hébergé en dehors de la documentation IBM, s'ouvrent dans une nouvelle fenêtre. Ces liens externes sont également signalés par une icône de lien externe (![Icône de lien externe](../images/icons/launch-glyph.svg "Icône de lien externe")).

## Navigation au clavier

{{site.data.keyword.ieam}} utilise les touches de navigation.

{{site.data.keyword.ieam}} utilise les raccourcis-clavier suivants.

|Action|Raccourci pour Internet Explorer|Raccourci pour Firefox|
|------|------------------------------|--------------------|
|Accéder au cadre de la vue Contenu|Alt+C, puis appuyer sur Entrée et Maj+F6|Maj+Alt+C et Maj+F6|
{: caption="Tableau 1. Raccourcis-clavier dans {{site.data.keyword.ieam}}" caption-side="top"}

## Informations d'interface

Utilisez la version la plus récente d'un lecteur d'écran avec {{site.data.keyword.ieam}}.

Les interfaces utilisateur {{site.data.keyword.ieam}} ne comportent pas de contenu clignotant 2 à 55 fois par seconde.

L'interface utilisateur Web {{site.data.keyword.ieam}} repose sur des feuilles de style en cascade (CSS) pour rendre correctement le contenu et fournir une expérience utilisable. L'application permet aux utilisateurs ayant une vision réduite d'utiliser les paramètres d'affichage du système, dont un mode à fort contraste, via une méthode équivalente. Vous pouvez contrôler la taille de la police en utilisant les paramètres de l'unité ou du navigateur Web.

Pour accéder à la {{site.data.keyword.gui}}, ouvrez un navigateur Web et accédez à l'URL suivante :

`https://<Cluster Master Host>:<Cluster Master API Port>/edge`

Le nom d'utilisateur et le mot de passe sont définis dans le fichier config.yaml.

La {{site.data.keyword.gui}} ne s'appuie pas sur des feuilles CSS pour rendre correctement le contenu et fournir une expérience utilisable. Toutefois, la documentation du produit, qui est disponible dans la documentation IBM Knowledge, repose sur des feuilles de style en cascade. {{site.data.keyword.ieam}} permet aux utilisateurs ayant une vision réduite d'utiliser les paramètres d'affichage du système, dont un mode à fort contraste, via une méthode équivalente. Il est possible de contrôler la taille de police dans les paramètres de l'unité ou du navigateur. Notez que la documentation produit comporte des chemins d'accès aux fichiers, des variables d'environnement, des commandes et autres contenus qui peuvent être mal prononcés par les lecteurs d'écran standard. Pour des descriptions les plus précises possibles, configurez vos paramètres de lecteur d'écran de façon à lire la totalité de la ponctuation.


## Logiciels fournisseur

{{site.data.keyword.ieam}} inclut certains logiciels de fournisseurs qui ne sont pas couverts par le contrat de licence IBM. IBM décline toute responsabilité concernant les fonctions d'accessibilité de ces produits. Pour obtenir des informations d'accessibilité sur ces derniers, contactez le fournisseur concerné.

## Informations d'accessibilité connexes

Outre les sites Web de support et le centre d'assistance IBM standard, un service de téléphone par téléscripteur est fourni pour les clients sourds ou malentendants afin qu'ils puissent accéder aux services de support et de vente :

Service TTY  
 800-IBM-3383 (800-426-3383)  
 (en Amérique du Nord)

Pour plus d'informations sur l'engagement d'IBM en matière d'accessibilité, voir [IBM Accessibility Research![Icône de lien externe](../images/icons/launch-glyph.svg "Icône de lien externe")](http://www.ibm.com/able){: new_window}.
