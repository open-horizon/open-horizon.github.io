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

Généralement, le développement d'un service prévu pour s'exécuter dans un cluster de périphérie est similaire à celui d'un service de périphérie s'exécutant sur un dispositif de périphérie. Le service de périphérie est développé en suivant le développement [Meilleures pratiques de développement natif Edge](../OH/docs/developing/best_practices.md) et il est intégré dans un conteneur. La différence réside dans la façon dont le service de périphérie est déployé.

Pour déployer un service de périphérie conteneurisé sur un cluster de périphérie, les développeurs doivent d'abord concevoir un opérateur Kubernetes destiné à déployer le service de périphérie conteneurisé dans un cluster Kubernetes. Une fois l'opérateur testé, les développeurs créent et publient l'opérateur sous forme de service {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}). Les administrateurs d'{{site.data.keyword.ieam}} peuvent ensuite déployer le service de l'opérateur comme ils le feraient pour n'importe quel service d'{{site.data.keyword.ieam}}, avec une règle ou des patterns. Il est inutile de créer une définition de service d'{{site.data.keyword.ieam}} pour le service de périphérie. Lorsqu'un administrateur d'{{site.data.keyword.ieam}} déploie le service de l'opérateur, l'opérateur déploie le service de périphérie.

Plusieurs sources d'information sont disponibles lors de la conception d'un opérateur Kubernetes. Commencez par lire [Kubernetes Concepts - Operator pattern](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/). Ce site constitue une excellente ressource pour en savoir plus sur les opérateurs. Une fois que vous connaissez bien les concepts de l'opérateur, vous pouvez concevoir votre opérateur à l'aide de l'infrastructure d'opérateur à l'adresse [Operator Framework](https://operatorframework.io/). Ce site Web fournit plus d'informations sur ce qu'est un opérateur et propose une méthode pour créer un opérateur simple à l'aide du kit de développement logiciel (SDK) d'opérateur.

## Considérations à prendre en compte lors du développement d'un opérateur pour {{site.data.keyword.ieam}}

Vous pouvez utiliser pleinement la fonction de statut de l'opérateur, car {{site.data.keyword.ieam}} indique tous les statuts créés par l'opérateur dans le concentrateur de gestion d'{{site.data.keyword.ieam}}. Lorsque vous élaborez un opérateur, l'infrastructure correspondante génère une définition de ressource personnalisée (CRD) Kubernetes pour l'opérateur. Chaque définition d'opérateur comporte un objet de statut qui fournit des informations de statut importantes au sujet de l'état de l'opérateur et du service en cours de déploiement. Cette opération n'est pas automatique dans Kubernetes, et le développeur de l'opérateur doit l'écrire dans l'implémentation de l'opérateur. L'agent d'{{site.data.keyword.ieam}} d'un cluster de périphérie agent rassemble périodiquement le statut de l'opérateur et le signale au concentrateur de gestion.

L'opérateur peut choisir d'attacher les variables d'environnement {{site.data.keyword.ieam}} spécifique au service à n'importe quels services qu'il démarre. Lorsque l'opérateur est démarré, l'agent {{site.data.keyword.ieam}} crée une mappe de configuration Kubernetes  `hzn-env-vars` qui content les variables d'environnement spécifiques au service. L'opérateur peut éventuellement joindre cette mappe de configuration à n'importe quel déploiement qu'il crée afin de permettre aux services qu'il démarre de reconnaître les mêmes variables d'environnement spécifiques au service. Il s'agit des mêmes variables d'environnement que celles qui sont injectées dans les services qui s'exécutent sur des dispositifs de périphérie. La seule exception concerne les variables d'environnement ESS*, car le système de gestion de modèle (MMS) n'est pas encore pris en charge pour les services de cluster de périphérie.

Les opérateurs déployés par {{site.data.keyword.ieam}} peuvent également être déployés dans un espace de nom autre que celui par défaut. Pour cela, le développeur de l'opérateur modifie les fichiers yaml afin qu'ils pointent vers l'espace de nom. Il existe deux façons de procéder :

* Modifier la définition de déploiement de l'opérateur (habituellement appelée **./deploy/operator.yaml**) afin de spécifier un espace de nom

ou

* Inclure un fichier de définition d'espace de nom dans les fichiers de définition yaml de l'opérateur, par exemple dans le répertoire **./deploy** du projet de l'opérateur.

**Remarque** : lorsqu'un opérateur est déployé dans un espace de nom autre que celui par défaut, {{site.data.keyword.ieam}} crée l'espace de nom s'il n'existe pas et le retire lorsque le déploiement de l'opérateur est annulé par {{site.data.keyword.ieam}}.

## Conditionnement d'un opérateur pour {{site.data.keyword.ieam}}

Après avoir développé et testé un opérateur, un package doit être créé en vue de son déploiement par {{site.data.keyword.ieam}} :

1. Assurez-vous que l'opérateur a été mis en package pour s'exécuter en tant que déploiement dans un cluster. Cela signifie que l'opérateur est développé dans un conteneur et envoyé par commande push vers le registre de conteneur à partir duquel le conteneur est récupéré lorsqu'il est déployé par {{site.data.keyword.ieam}}. Généralement, pour effectuer cette opération, vous générez l'opérateur à l'aide de la commande **operator-sdk build** suivie de la commande **docker push**. Cette procédure est décrite dans [Operator Tutorial](https://sdk.operatorframework.io/docs/building-operators/golang/tutorial/#2-run-as-a-deployment-inside-the-cluster).

2. Assurez-vous que le ou les conteneurs de service qui sont développés par l'opérateur sont également envoyés vers le registre à partir duquel l'opérateur les déploiera.

3. Créez une archive contenant les fichiers de définition yaml de l'opérateur qui proviennent du projet de l'opérateur :

   ```bash
   cd <operator-project>/<operator-name>/deploy    tar -zcvf <archive-name>.tar.gz ./*
   ```
   {: codeblock}

   **Remarque** : pour les utilisateurs {{site.data.keyword.macos_notm}}, pensez à créer un fichier archive tar.gz pour qu'aucun fichier caché ne s'y trouve. Par exemple, un fichier .DS_store peut provoquer des incidents lors du déploiement d'un opérateur Helm. Si vous pensez qu'un fichier caché existe, extrayez le fichier tar.gz sur votre système {{site.data.keyword.linux_notm}}. Pour plus d'informations, voir la [commande Tar dans macos](https://stackoverflow.com/questions/8766730/tar-command-in-mac-os-x-adding-hidden-files-why).

   ```bash
   tar -xzpvf x.tar --exclude=".*"
   ```
   {: codeblock}

4. Utilisez les outils de création de service d'{{site.data.keyword.ieam}} pour créer une définition de service pour le service de l'opérateur, par exemple :

   1. Créez un projet :

      ```bash
      hzn dev service new -V <a version> -s <a service name> -c cluster
      ```
      {: codeblock}

   2. Modifiez le fichier **horizon/service.definition.json** afin qu'il pointe vers l'archive yaml de l'opérateur créée précédemment à l'étape 3.

   3. Créez une clé de signature de service, ou utilisez-en une déjà créée.

   4. Publiez le service.

      ```
      hzn exchange service publish -k <signing key> -f ./horizon/service.definition.json
      ```
      {: codeblock}

5. Créez une règle ou un pattern de déploiement pour déployer le service d'opérateur sur un cluster de périphérie.
