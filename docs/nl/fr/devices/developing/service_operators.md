---

copyright:
years: 2020
lastupdated: "2020-04-27"

---

{:shortdesc: .shortdesc}
{:new_window: target="_blank"}
{:codeblock: .codeblock}
{:pre: .pre}
{:screen: .screen}
{:tip: .tip}
{:download: .download}

# Développement d'un opérateur Kubernetes
{: #kubernetes_operator}

Généralement, le développement d'un service prévu pour s'exécuter dans un cluster de périphérie est similaire à celui d'un service de périphérie s'exécutant sur un dispositif de périphérie. Le service de périphérie est développé en suivant les instructions de la rubrique [Pratiques de développement Edge natif](best_practices.md), puis est packagé dans un conteneur. La différence réside dans la façon dont le service de périphérie est déployé.

Pour déployer un service de périphérie conteneurisé sur un cluster de périphérie, les développeurs doivent d'abord concevoir un opérateur Kubernetes destiné à déployer le service de périphérie conteneurisé dans un cluster Kubernetes. Une fois l'opérateur testé, les développeurs créent et publient l'opérateur sous forme de service {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}). Les administrateurs d'{{site.data.keyword.ieam}} peuvent ensuite déployer le service de l'opérateur comme ils le feraient pour n'importe quel service d'{{site.data.keyword.ieam}}, avec une règle ou des patterns. Il est inutile de créer une définition de service d'{{site.data.keyword.ieam}} pour le service de périphérie. Lorsqu'un administrateur d'{{site.data.keyword.ieam}} déploie le service de l'opérateur, l'opérateur déploie le service de périphérie.

Plusieurs options s'offrent à vous lors de la conception d'un opérateur Kubernetes. Commencez par lire [Kubernetes Concepts - Operator pattern ![S'ouvre dans un nouvel onglet](../../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/). Ce site constitue une excellente ressource pour en savoir plus sur les opérateurs. Une fois que vous connaissez bien les concepts de l'opérateur, vous pouvez concevoir votre opérateur à l'aide de l'infrastructure d'opérateur à l'adresse [Operator Framework ![S'ouvre dans un nouvel onglet](../../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://github.com/operator-framework/getting-started). Cet article fournit des détails supplémentaires sur la nature d'un opérateur et traite de la création d'un opérateur simple à l'aide du kit de développement logiciel (SDK) de l'opérateur.

## Considérations à prendre en compte lors du développement d'un opérateur pour {{site.data.keyword.ieam}}

Vous pouvez utiliser pleinement la fonction de statut de l'opérateur, car {{site.data.keyword.ieam}} indique tous les statuts créés par l'opérateur dans le concentrateur de gestion d'{{site.data.keyword.ieam}}. Lorsque vous élaborez un opérateur, l'infrastructure correspondante génère une définition de ressource personnalisée (CRD) Kubernetes pour l'opérateur. Chaque définition d'opérateur comporte un objet de statut qui fournit des informations de statut importantes au sujet de l'état de l'opérateur et du service en cours de déploiement. Cette opération n'est pas automatique dans Kubernetes, et le développeur de l'opérateur doit l'écrire dans l'implémentation de l'opérateur. L'agent d'{{site.data.keyword.ieam}} d'un cluster de périphérie agent rassemble périodiquement le statut de l'opérateur et le signale au concentrateur de gestion.

Si besoin, l'opérateur peut joindre les variables d'environnement d'{{site.data.keyword.ieam}} qui sont spécifiques au service à n'importe lequel des services qui démarrent. Lorsque l'opérateur est démarré, l'agent d'{{site.data.keyword.ieam}} crée une configmap Kubernetes appelée `hzn-env-vars` qui content les variables d'environnement spécifiques au service. L'opérateur peut éventuellement joindre cette mappe de configuration à n'importe quel déploiement qu'il crée afin de permettre aux services qu'il démarre de reconnaître les mêmes variables d'environnement spécifiques au service. Il s'agit des mêmes variables d'environnement que celles qui sont injectées dans les services qui s'exécutent sur des dispositifs de périphérie. La seule exception concerne les variables d'environnement du composant ESS*, car le système de gestion des modèles (MMS) n'est pas encore compatible avec les services de cluster de périphérie.

Les opérateurs déployés par {{site.data.keyword.ieam}} peuvent également être déployés dans un espace de nom autre que celui par défaut. Pour cela, le développeur de l'opérateur modifie les fichiers yaml afin qu'ils pointent vers l'espace de nom. Il existe deux façons de procéder :

 * Modifier la définition de déploiement de l'opérateur (habituellement appelée **./deploy/operator.yaml**) afin de spécifier un espace de nom

ou

* Inclure un fichier de définition d'espace de nom dans les fichiers de définition yaml de l'opérateur, par exemple dans le répertoire **./deploy** du projet de l'opérateur.

Remarque : Lorsqu'un opérateur est déployé sur un espace de nom autre que celui par défaut, {{site.data.keyword.ieam}} crée l'espace de nom s'il n'existe pas et le supprime lorsque le déploiement de l'opérateur est annulé par {{site.data.keyword.ieam}}.

## Développement d'un opérateur pour {{site.data.keyword.ieam}}

Après avoir développé et testé un opérateur, un package doit être créé en vue de son déploiement par {{site.data.keyword.ieam}} :

1. Assurez-vous que l'opérateur a été mis en package pour s'exécuter en tant que déploiement dans un cluster. Cela signifie que l'opérateur est développé dans un conteneur et envoyé par commande push vers le registre de conteneur à partir duquel le conteneur est récupéré lorsqu'il est déployé par {{site.data.keyword.ieam}}. Généralement, pour ce faire, vous générez l'opérateur à l'aide des commandes **operator-sdk build** suivies par **docker push**. Cette procédure est décrite à la page [Operator Framework ![S'ouvre dans un nouvel onglet](../../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://github.com/operator-framework/getting-started#1-run-as-a-deployment-inside-the-cluster).

2. Assurez-vous que le ou les conteneurs de service qui sont développés par l'opérateur sont également envoyés vers le registre à partir duquel l'opérateur les déploiera.

3. Créez une archive contenant les fichiers de définition yaml de l'opérateur qui proviennent du projet de l'opérateur :

   ```bash
   cd <operator-project>/<operator-name>/deploy
    tar -zcvf <archive-name>.tar.gz
   ```
   {: codeblock}

4. Utilisez les outils de création de service d'{{site.data.keyword.ieam}} pour créer une définition de service pour le service de l'opérateur, par exemple, en suivant les étapes ci-dessous :

   1. Créez un projet :

      ```bash
      hzn dev service new -V <a version> -s <a service name> -c cluster
      ```
      {: codeblock}

   2. Modifiez le fichier **horizon/service.definition.json** afin qu'il pointe vers l'archive yaml de l'opérateur créée à l'étape 3.

   3. Créez une clé de signature de service ou utilisez-en une existante.

   4. Publiez le service.

      ```
      hzn exchange service publish -k <signing key> -f ./horizon/service.definition.json
      ```
      {: codeblock}

5. Créez une règle ou un pattern de déploiement pour déployer le service d'opérateur sur un cluster de périphérie.
