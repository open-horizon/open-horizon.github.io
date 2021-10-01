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

{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) prend en charge plusieurs rôles. Votre rôle détermine les actions que vous êtes autorisé à effectuer.
{:shortdesc}

## Organisations
{: #orgs}

{{site.data.keyword.ieam}} utilise le concept général de partage de services par organisations, où chaque locataire possède sa propre organisation. Les organisations séparent les ressources. Par conséquent, les utilisateurs d'une organisation donnée ne peuvent pas créer ou modifier de ressources dans une autre organisation. En outre, les ressources d'une organisation ne peuvent être consultées que par les utilisateurs de cette organisation (sauf si les ressources sont définies comme publiques). Les ressources définies comme publiques sont les seules ressources qui peuvent être consultées dans l'ensemble des organisations.

L'organisation IBM fournit des services et des modèles prédéfinis. Bien que les ressources de cette organisation soient publiques, elle n'est pas conçue pour inclure tous les contenus publics dans le concentrateur de gestion {{site.data.keyword.ieam}}.

Par défaut, une organisation est créée lors de l'installation d'{{site.data.keyword.ieam}} avec le nom de votre choix. Vous pouvez créer des organisations supplémentaires si nécessaire. Pour plus d'informations sur l'ajout d'organisations à votre concentrateur de gestion, voir [Partage de services](../admin/multi_tenancy.md).

## Identités
{: #ids}

Il existe quatre types d'identités dans {{site.data.keyword.ieam}} :

* Utilisateurs Identity and Access Management (IAM) : Les utilisateurs d'IAM sont reconnus par tous les composants d'{{site.data.keyword.ieam}} : interface utilisateur, Exchange, interface de ligne de commande **hzn**, interface de ligne de commande **cloudctl**, interface de ligne de commande  **oc**, interface de ligne de commande **kubectl**.
  * IAM fournit un plug-in LDAP pour que les utilisateurs LDAP connectés à IAM se comportent comme des utilisateurs IAM
  * Les clés d'API IAM (utilisées avec la commande **hzn**) se comportent comme des utilisateurs IAM
* Utilisateurs d'Exchange uniquement : l'utilisateur root d'Exchange en est un exemple. En général, vous n'avez pas besoin de créer d'autres utilisateurs locaux pour Exchange uniquement. Une meilleure pratique consiste à gérer les utilisateurs dans IAM et utiliser les données d'identification de ces utilisateurs (ou les clés d'API associées à ces utilisateurs) pour s'authentifier auprès d'{{site.data.keyword.ieam}}.
* Noeuds Exchange (dispositifs ou clusters de périphérie)
* Agbots Exchange

### Contrôle d'accès à base de rôles (RBAC)
{: #rbac_roles}

{{site.data.keyword.ieam}} inclut les rôles suivants :

| **Rôle**    | **Accès**    |  
|---------------|--------------------|
| Utilisateur IAM | Grâce à IAM, ces utilisateurs peuvent recevoir les rôles de concentrateur de gestion suivants : Administrateur de cluster, Administrateur, Opérateur, Editeur et Visualiseur. Un rôle IAM est affecté à des utilisateurs ou à des groupes d'utilisateurs lorsque vous les ajoutez à une équipe IAM. L'accès d'une équipe aux ressources peut être contrôlé par l'espace de nom de Kubernetes. Les utilisateurs d'IAM peuvent également recevoir n'importe lequel des rôles Exchange ci-dessous à l'aide de l'interface de ligne de commande **hzn exchange**. |
| Utilisateur root Exchange | Privilège illimité dans Exchange. Cet utilisateur est défini dans le fichier de configuration Exchange. Vous pouvez le désactiver si besoin. |
| Utilisateur administrateur du concentrateur Exchange | Peut afficher la liste des organisations, afficher les utilisateurs dans une organisation et créer ou supprimer des organisations. |
| Utilisateur administrateur d'une organisation Exchange | Possède un privilège Exchange illimité au sein de l'organisation. |
| Utilisateur Exchange | Possibilité de création de ressources Exchange (noeuds, services, patterns, règles) dans l'organisation. Possibilité de mise à jour ou de suppression des ressources détenues par cet utilisateur. Peut lire tous les services, patterns et règles dans l'organisation, ainsi que les services et patterns publics dans les autres organisations. Peut lire des noeuds appartenant à cet utilisateur. |
| Noeuds Exchange | Peut lire son propre noeud dans Exchange, ainsi que tous les services, patterns et règles dans l'organisation, et tous les services et patterns publics dans les autres organisations. Il s'agit des seules données d'identification qui doivent être sauvegardées dans le noeud de périphérie, car elles disposent des droits d'accès minimaux nécessaires au fonctionnement du noeud de périphérie.|
| Agbots Exchange | Les agbots d'IBM peuvent lire tous les noeuds, services, patterns et règles de toutes les organisations. |
{: caption="Tableau 1. Rôles RBAC" caption-side="top"}
