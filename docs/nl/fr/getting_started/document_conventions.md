---

copyright:
years: 2020
lastupdated: "2020-04-01"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Conventions de ce guide
{: #document_conventions}

Ce document utilise des conventions pour véhiculer un certain sens.  

## Conventions des commandes

Remplacez le contenu de la variable signalée par < > par des valeurs adaptées à vos besoins. N'incluez pas le signe < > dans la commande.

### Exemple

  ```
  hzn key create "<companyname>" "<youremailaddress>"
  ```
  {: codeblock}
   
## Chaînes littérales

Le contenu qui s'affiche dans le concentrateur de gestion ou dans le code est une chaîne littérale. Il apparaît sous la forme d'un texte en **gras**.
   
 ### Exemple
   
 Si vous examinez le code `service.sh`, vous constatez qu'il utilise les variables de configuration suivantes, entre autres, pour contrôler son comportement. La variable **PUBLISH** vérifie si le code tente d'envoyer des messages à IBM Event Streams. La variable **MOCK** vérifie si service.sh tente de contacter les API REST et ses services dépendants (cpu et gps) ou si `service.sh` crée des données fictives.
  
