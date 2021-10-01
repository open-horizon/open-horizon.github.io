---

copyright:
years: 2019
lastupdated: "2019-09-27"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Contrôle d'accès à base de rôles
{: #rbac}

{{site.data.keyword.edge_notm}} {{site.data.keyword.ieam}} prend en charge plusieurs rôles. Votre rôle détermine les actions que vous êtes autorisé à effectuer.
{:shortdesc}

## Organisations
{: #orgs}

Les organisations d'{{site.data.keyword.ieam}} sont conçues pour séparer les accès aux ressources. Les ressources d'une organisation ne peuvent être consultées que par l'organisation sauf si elles sont explicitement marquées comme étant publiques. Les ressources qui sont publiques sont les seules à pouvoir être affichées par toutes les organisations.

IBM vous fournit des services et des patterns prédéfinis.

Au sein d'{{site.data.keyword.ieam}}, le nom de votre organisation est également le nom de votre cluster.

## Identités
{: #ids}

Les trois types d'identité disponibles dans {{site.data.keyword.ieam}} sont les suivants :

* Utilisateurs : les deux types d'utilisateurs suivants peuvent accéder à la console {{site.data.keyword.ieam}} et à Exchange
  * Utilisateurs Identity and Access Management (IAM) : les utilisateurs IAM sont détectés par le réseau Exchange d'{{site.data.keyword.ieam}}.
    * IAM fournit un plug-in LDAP pour que les utilisateurs LDAP connectés à IAM se comportent comme des utilisateurs IAM
    * Les clés d'API IAM (utilisées avec la commande **hzn**) se comportent comme des utilisateurs IAM
  * Utilisateurs Exchange locaux : l'utilisateur root Exchange est un exemple de ces utilisateurs. Vous n'avez généralement pas besoin de créer d'autres utilisateurs Exchange locaux.
* Noeuds (dispositifs ou clusters de périphérie)
* Agbots

### Contrôle d'accès à base de rôles (RBAC)
{: #rbac_roles}

{{site.data.keyword.ieam}} inclut les rôles suivants :

| **Rôle**    | **Accès**    |  
|---------------|--------------------|
| Utilisateur root Exchange | Privilège illimité dans Exchange. Cet utilisateur est défini dans le fichier de configuration Exchange. Vous pouvez le désactiver si besoin. |
| Administrateur ou clé d'API | Privilège illimité dans l'organisation. |
| Utilisateur non administrateur ou clé d'API | Possibilité de création de ressources Exchange (noeuds, services, patterns, règles) dans l'organisation. Possibilité de mise à jour ou de suppression des ressources détenues par cet utilisateur. Peut lire tous les services, patterns et règles dans l'organisation, ainsi que les services et patterns publics dans les autres organisations. |
| Noeud | Peut lire son propre noeud dans Exchange, ainsi que tous les services, patterns et règles dans l'organisation, et tous les services et patterns publics dans les autres organisations. |
| Agbot | Les agbots d'IBM peuvent lire tous les noeuds, services, patterns et règles de toutes les organisations. |
{: caption="Tableau 1. Rôles RBAC" caption-side="top"}
