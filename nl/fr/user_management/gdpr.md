---

copyright:
years: 2020
lastupdated: "2020-10-7"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Considérations relatives au RGPD

## Avis
{: #notice}
<!-- This is boilerplate text provided by the GDPR team. It cannot be changed. -->

Le présent document a pour but de vous aider à vous préparer à la mise en conformité avec le RGPD. Il fournit des informations sur les fonctionnalités d'{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) que vous pouvez configurer, ainsi que sur des aspects de l'utilisation du produit à prendre en compte lors de la préparation de votre organisation au RGPD. Ces informations ne sont pas exhaustives. Les clients peuvent choisir et configurer des fonctionnalités et utiliser le produit de nombreuses façons différentes et avec des applications et des systèmes tiers.

<p class="ibm-h4 ibm-bold">Il incombe aux clients de veiller à leur propre conformité aux différentes lois et réglementations, y compris au Règlement général sur la protection des données (RGPD) de l'Union européenne. Il est de la responsabilité du client de faire appel à un conseiller juridique compétent pour identifier et interpréter les lois et réglementations applicables qui pourraient affecter ses opérations et toutes les actions qu'il pourrait être amené à entreprendre pour se conformer auxdites lois et réglementations.</p>

<p class="ibm-h4 ibm-bold">Les produits, services et autres fonctionnalités décrits ici ne sont pas adaptés à toutes les situations client et peuvent restreindre la disponibilité. IBM ne donne aucun avis juridique, comptable ou d'audit et ne garantit pas que ses produits ou services permettent aux clients de se conformer aux lois ou réglementations applicables.</p>

## Table des matières

* [RGPD](#overview)
* [Configuration du produit pour le règlement RGPD](#productconfig)
* [Cycle de vie des données](#datalifecycle)
* [Traitement des données](#dataprocessing)
* [Capacité de restreindre l'utilisation des données personnelles](#datasubjectrights)
* [Annexe](#appendix)

## RGPD
{: #overview}

<!-- This is boilerplate text provided by the GDPR team. It cannot be changed. -->
Le règlement général sur la protection des données (RGPD) a été adopté par l'Union européenne (UE) et est entré en vigueur le 25 mai 2018.

### Pourquoi le règlement RGPD est-il important ?

Le règlement RGPD met en place une structure réglementaire de protection des données plus contraignante pour le traitement des données personnelles des individus. Il apporte :

* Des droits nouveaux et renforcés aux individus
* Une définition plus large des données personnelles
* De nouvelles obligations pour les entreprises et organisations traitant des données à caractère personnel
* Des sanctions financières importantes en cas de non-respect
* Une notification obligatoire des atteintes à la protection des données

IBM a défini un programme de conformité internationale qui vise à préparer les processus internes et les offres commerciales d'IBM à la mise en conformité avec le RGPD.

### Informations complémentaires

* [Portail d'informations eugdpr.org](https://gdpr.eu/)
*  [Site Web ibm.com/GDPR](https://www.ibm.com/data-responsibility/gdpr/)

## Configuration du produit – considérations relatives à la conformité au règlement RGPD
{: #productconfig}

Les sections suivantes décrivent des aspects d'{{site.data.keyword.ieam}} et fournissent des informations sur diverses fonctionnalités afin d'aider les clients à se mettre en conformité avec les exigences du RGPD.

### Cycle de vie des données
{: #datalifecycle}

{{site.data.keyword.ieam}} est une application de développement et de gestion des applications conteneurisées sur site. Il s'agit d'un environnement intégré permettant de gérer les charges de travail de conteneur en périphérie. Il comprend l'orchestrateur de conteneurs Kubernetes, un registre d'images privé, une console de gestion, un agent de noeud de périphérie et des infrastructures de surveillance.

En tant que tel, {{site.data.keyword.ieam}} utilise principalement des données techniques liées à la configuration et à la gestion de l'application, dont certaines peuvent être assujetties au RGPD. {{site.data.keyword.ieam}} traite également des informations sur les utilisateurs qui gèrent l'application. Ces données sont décrites dans le présent document en vue de sensibiliser les clients chargés de la mise en conformité avec le RGPD.

Ces données sont conservées sur {{site.data.keyword.ieam}} sur des systèmes de fichiers locaux ou distants en tant que fichiers de configuration ou dans des bases de données. Les applications développées pour s'exécuter sur {{site.data.keyword.ieam}} peuvent utiliser d'autres formes de données personnelles assujetties au RGPD. Les mécanismes utilisés pour protéger et gérer les données sont également disponibles pour les applications s'exécutant dans {{site.data.keyword.ieam}}. Des mécanismes supplémentaires peuvent être nécessaires pour gérer et protéger les données personnelles collectées par les applications exécutées dans {{site.data.keyword.ieam}}.

Pour comprendre les flux de données {{site.data.keyword.ieam}}, vous devez comprendre le fonctionnement de Kubernetes, de Docker et d'Operators. Ces composants open source sont fondamentaux pour {{site.data.keyword.ieam}}. Vous utilisez {{site.data.keyword.ieam}} pour placer des instances de conteneurs d'applications (services de périphérie) sur des noeuds de périphérie. Les services de périphérie contiennent les détails de l'application, et les images Docker contiennent tous les progiciels que vos applications doivent exécuter.

{{site.data.keyword.ieam}} comprend un ensemble d'exemples de service de périphérie open source. Pour afficher la liste de tous les graphiques {{site.data.keyword.ieam}}, voir [open-horizon/examples](https://github.com/open-horizon/examples){:new_window}. Il incombe au client de déterminer et d'implémenter les contrôles RGPD appropriés pour ces derniers.

### Types de données transitant via {{site.data.keyword.ieam}}

{{site.data.keyword.ieam}} traite de plusieurs catégories de données techniques qui peuvent être considérées comme des données personnelles, par exemple :

* ID utilisateur et mot de passe de l'administrateur ou de l'opérateur
* Adresses IP
* Noms de noeud Kubernetes

Les informations relatives à la manière dont ces données techniques sont collectées et créées, stockées, consultées, sécurisées, journalisées et supprimées sont décrites dans les sections suivantes du présent document.

### Données personnelles utilisées pour le contact en ligne avec IBM

Les clients {{site.data.keyword.ieam}} peuvent soumettre des commentaires en ligne, des retours d'informations, et des demandes à IBM concernant des sujets relatifs à d'{{site.data.keyword.ieam}} de différentes manières, principalement :

* Communauté publique {{site.data.keyword.ieam}} Slack Community
* Zone de commentaires publics sur les pages de la documentation produit {{site.data.keyword.ieam}}
* Commentaires publics sur l'espace {{site.data.keyword.ieam}} de dW Answers

En général, seuls le nom du client et son adresse électronique sont utilisés pour activer les réponses personnelles sur le sujet de la prise de contact. Cette utilisation des données personnelles est conforme à la [Déclaration de confidentialité en ligne d'IBM](https://www.ibm.com/privacy/us/en/){:new_window}.

### Authentification

Le gestionnaire d'authentification {{site.data.keyword.ieam}} accepte les données d'identification de l'utilisateur à partir de la {{site.data.keyword.gui}} et transmet les données d'identification au fournisseur OIDC dorsal, qui valide les données d'identification de l'utilisateur par rapport au répertoire d'entreprise. Il retourne ensuite un cookie d'authentification (`auth-cookie`) avec le contenu d'un jeton `JWT` (JSON Web Token) au gestionnaire d'authentification. Le jeton JWT conserve des informations comme l'ID utilisateur et l'adresse e-mail, en plus de l'appartenance au groupe au moment de la demande d'authentification. Ce cookie d'authentification est ensuite renvoyé à la {{site.data.keyword.gui}}. Le cookie est actualisé durant la session. Il est valide pendant 12 heures après votre déconnexion de la {{site.data.keyword.gui}} ou la fermeture de votre navigateur Web.

Pour toutes les demandes d'authentification ultérieures effectuées à partir de la {{site.data.keyword.gui}}, le serveur NodeJS frontal décode le cookie d'authentification inclus dans la demande et valide la demande en appelant le gestionnaire d'authentification.

L'interface de ligne de commande d'{{site.data.keyword.ieam}} demande à l'utilisateur de fournir une clé d'API. Les clés API sont créées à l'aide de la commande `cloudctl`.

Les interfaces de ligne de commande  **cloudctl**, **kubectl** et **oc** exigent également des données d'identification pour accéder au cluster. Ces données d'identification, qui peuvent être obtenues depuis la console de gestion, expirent au bout de 12 heures.

### Mappage de rôle

{{site.data.keyword.ieam}} prend en charge le contrôle d'accès à base de rôles (RBAC). Dans l'étape de mappage des rôles, le nom d'utilisateur fourni dans l'étape d'authentification est mappé avec un rôle d'utilisateur ou un rôle de groupe. Les rôles sont utilisés pour autoriser les activités pouvant être exécutées par l'utilisateur authentifié. Pour plus d'informations sur les rôles {{site.data.keyword.ieam}}, voir [Contrôle d'accès à base de rôles](rbac.md).

### Sécurité du pod

Les règles de sécurité du pod sont utilisées pour configurer un concentrateur de gestion ou un contrôle de cluster de périphérie afin de déterminer les actions que le pod peut exécuter ou les éléments auxquels il peut accéder. Pour plus d'informations sur les pods, voir [Installation du concentrateur de gestion](../hub/hub.md) et [Clusters de périphérie](../installing/edge_clusters.md).

## Traitement des données
{: #dataprocessing}

Les utilisateurs d'{{site.data.keyword.ieam}} peuvent gérer la façon dont les données techniques qui sont liées à la configuration et à la gestion sont traitées et sécurisées via la configuration système.

* Le contrôle d'accès basé sur les rôles (RBAC) contrôle les données et les fonctions auxquelles les utilisateurs peuvent accéder.

* Les politiques de sécurité de pod sont utilisées pour configurer un contrôle de niveau cluster sur ce que peut faire un pod et ce à quoi il peut accéder.

* Les données en transit sont protégées par `TLS`. `HTTPS` (`TLS` sous-jacent) est utilisé pour sécuriser un transfert de données entre le client utilisateur et les services de back end. Les utilisateurs peuvent spécifier le certificat racine à utiliser durant l'installation.

* La protection des données au repos est prise en charge avec  `dm-crypt` qui chiffre les données.

* Les périodes de conservation des données pour la journalisation (ELK) et la surveillance (Prometheus) sont configurables et la suppression des données est prise en charge par les API fournies.

Les mêmes mécanismes que ceux utilisés pour gérer et sécuriser les données techniques {{site.data.keyword.ieam}} peuvent être utilisés pour gérer et sécuriser les données personnelles des applications développées ou fournies par l'utilisateur. Les clients peuvent développer leurs propres fonctionnalités pour implémenter d'autres contrôles.

Pour plus d'informations sur les certificats, voir [Installation d'{{site.data.keyword.ieam}}](../hub/installation.md).

## Capacité de restreindre l'utilisation des données personnelles
{: #datasubjectrights}

Grâce aux fonctionnalités décrites dans ce document, {{site.data.keyword.ieam}} permet à un utilisateur de restreindre l'utilisation de toutes les données techniques de l'application qui sont considérées comme des données personnelles.

Le règlement RGPD permet aux utilisateurs d'accéder, de modifier et de restreindre un traitement. Reportez-vous aux autres sections du présent document pour contrôler ce qui suit :
* Droit d'accès
  * Les administrateurs {{site.data.keyword.ieam}} peuvent utiliser les fonctions {{site.data.keyword.ieam}} pour permettre aux utilisateurs individuels d'accéder à leurs données.
  * Les administrateurs {{site.data.keyword.ieam}} peuvent utiliser les fonctions {{site.data.keyword.ieam}} pour fournir aux utilisateurs individuels des informations sur les données collectées et conservées par {{site.data.keyword.ieam}} à leur sujet.
* Droit de modification
  * Les administrateurs {{site.data.keyword.ieam}} peuvent utiliser les fonctions {{site.data.keyword.ieam}} pour permettre à un utilisateur individuel de modifier ou de corriger ses données.
  * Les administrateurs {{site.data.keyword.ieam}} peuvent utiliser les fonctions {{site.data.keyword.ieam}} pour corriger les données d'un utilisateur individuel à la place de ce dernier.
* Droit de restreindre un traitement
  * Les administrateurs {{site.data.keyword.ieam}} peuvent utiliser les fonctions {{site.data.keyword.ieam}} pour arrêter le traitement des données d'un utilisateur individuel.

## Annexe - Données journalisées par {{site.data.keyword.ieam}}
{: #appendix}

En tant qu'application, {{site.data.keyword.ieam}} traite de plusieurs catégories de données techniques qui peuvent être considérées comme des données personnelles :

* ID utilisateur et mot de passe de l'administrateur ou de l'opérateur
* Adresses IP
* Noms de noeud Kubernetes. 

{{site.data.keyword.ieam}} traite également des informations sur les utilisateurs qui gèrent les applications qui s'exécutent sur {{site.data.keyword.ieam}} et qui peuvent introduire d'autres catégories de données personnelles inconnues de l'application.

### Sécurité {{site.data.keyword.ieam}}

* Quelles sont les données consignées ?
  * ID utilisateur, nom d'utilisateur et adresse IP des utilisateurs connectés
* Quand les données sont-elles consignées ?
  * Avec les demandes de connexion
* Où les données sont-elles consignées ?
  * Dans les journaux d'audit, dans `/var/lib/icp/audit`???
  * Dans les journaux d'audit, dans `/var/log/audit`???
  * Journaux d'Exchange dans ???
* Comment supprimer les données ?
  * Recherchez les données et supprimez l'enregistrement du journal d'audit

### API {{site.data.keyword.ieam}}

* Quelles sont les données consignées ?
  * ID utilisateur, nom d'utilisateur et adresse IP du client dans les journaux du conteneur
  * Données d'état de cluster Kubernetes dans le serveur `etcd`
  * Données d'identification OpenStack et VMware dans le serveur `etcd`
* Quand les données sont-elles consignées ?
  * Avec les demandes d'API
  * Données d'identification stockées depuis la commande `credentials-set`
* Où les données sont-elles consignées ?
  * Dans les journaux de conteneur, Elasticsearch et le serveur `etcd`.
* Comment supprimer les données ?
  * Supprimez les journaux de conteneur (`platform-api`, `platform-deploy`) dans les conteneurs ou supprimez les entrées de journal concernant les utilisateurs à partir d'Elasticsearch.
  * Effacez la paire clé-valeur `etcd` en utilisant la commande `etcdctl rm`.
  * Retirez les données d'identification en appelant la commande `credentials-unset`.


Pour plus d'informations, voir :

  * [Logging Architecture](https://kubernetes.io/docs/concepts/cluster-administration/logging/){:new_window}
  * [etcdctl](https://github.com/coreos/etcd/blob/master/etcdctl/READMEv2.md){:new_window}

### Surveillance {{site.data.keyword.ieam}}

* Quelles sont les données consignées ?
  * Adresse IP, noms des pods, édition, image
  * Les données mises au rebut à partir d'applications développées par le client peuvent inclure des données personnelles.
* Quand les données sont-elles consignées ?
  * Quand Prometheus retire des métriques depuis les cibles configurées
* Où les données sont-elles consignées ?
  * Sur le serveur Prometheus ou dans les volumes persistants configurés
* Comment supprimer les données ?
  * Recherchez les données et supprimez-les en utilisant l'API Prometheus

Pour plus d'informations, voir la [documentation de Prometheus](https://prometheus.io/docs/introduction/overview/){:new_window}.


### {{site.data.keyword.ieam}} Kubernetes

* Quelles sont les données consignées ?
  * Topologie déployée en cluster (informations de noeud pour le contrôleur, noeud worker, le proxy et le va).
  * Configuration de service (mappe de configuration k8s) et secrets (secrets k8s)
  * ID utilisateur dans le journal apiserver
* Quand les données sont-elles consignées ?
  * Quand vous déployez un cluster
  * Quand vous déployez une application depuis le catalogue Helm
* Où les données sont-elles consignées ?
  * Topologie déployée en cluster dans `etcd`
  * Configuration et secret pour les applications déployées dans `etcd`
* Comment supprimer les données ?
  * Utilisez la {{site.data.keyword.gui}} {{site.data.keyword.ieam}}
  * Recherchez les données et supprimez-les en utilisant la {{site.data.keyword.gui}} k8s (`kubectl`) ou l'API REST `etcd`
  * Recherchez et supprimez les données du journal apiserver à l'aide de l'API Elasticsearch

Procédez avec prudence lorsque vous modifiez la configuration de cluster de Kubernetes ou que vous supprimez des données de cluster.

  Pour plus d'informations, voir [Kubernetes kubectl](https://kubernetes.io/docs/reference/kubectl/overview/){:new_window}.

### API Helm {{site.data.keyword.ieam}}

* Quelles sont les données consignées ?
  * Nom d'utilisateur et rôle
* Quand les données sont-elles consignées ?
  * Quand un utilisateur extrait des chartes ou des référentiels qui sont ajoutés à une équipe
* Où les données sont-elles consignées ?
  * Journaux de déploiement helm-api, Elasticsearch
* Comment supprimer les données ?
  * Recherchez les données de journal helm-api et supprimez-les en utilisant l'API Elasticsearch

### Courtier de services {{site.data.keyword.ieam}}

* Quelles sont les données consignées ?
  * ID utilisateur (uniquement au niveau de journalisation de débogage 10, pas au niveau de journalisation par défaut)
* Quand les données sont-elles consignées ?
  * Quand des demandes d'API sont transmises au courtier de services
  * Quand le courtier de services accède au catalogue de service
* Où les données sont-elles consignées ?
  * Journal de conteneur du courtier de services, Elasticsearch
* Comment supprimer les données ?
  * Recherchez et supprimez le journal apiserver qui utilise l'API Elasticsearch
  * Recherchez et supprimez le journal du conteneur apiserver
      ```
      kubectl logs $(kubectl get pods -n kube-system | grep  service-catalogapiserver | awk '{print $1}') -n kube-system | grep admin
      ```
      {: codeblock}


  Pour plus d'informations, voir [Kubernetes kubectl](https://kubernetes.io/docs/reference/kubectl/overview/){:new_window}.
