---

copyright:
years: 2020
lastupdated: "2020-10-15"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Conseils pour le traitement des incidents et FAQ
{: #troubleshooting}

Consultez les conseils pour le traitement des incidents et la FAQ (Foire aux questions) pour vous résoudre les problèmes éventuels.
{:shortdesc}

* [Conseils relatifs au traitement des incidents](troubleshooting_devices.md)
* [Foire aux questions](../getting_started/faq.md)

Le contenu de traitement des incidents suivant décrit les principaux composants d'{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) et explique comment analyser les interfaces incluses pour déterminer l'état du système.

## Outils de traitement des incidents
{: #ts_tools}

De nombreuses interfaces intégrées à {{site.data.keyword.ieam}} fournissent des informations qui peuvent servir à diagnostiquer des problèmes. Ces informations sont disponibles via la {{site.data.keyword.gui}}, les API REST HTTP et un outil shell {{site.data.keyword.linux_notm}}, `hzn`.

Sur un noeud de périphérie, il peut être nécessaire de résoudre les problèmes de l'hôte, du logiciel Horizon, de Docker, de votre configuration ou du code dans les conteneurs de service. Les problèmes liés à l'hôte d'un noeud de périphérie n'entrent pas dans le cadre de ce document. Si vous devez résoudre les problèmes liés à Docker, vous pouvez utiliser de nombreuses commandes et interfaces Docker. Pour plus d'informations, consultez la documentation Docker.

Si les conteneurs de service que vous exécutez utilisent {{site.data.keyword.message_hub_notm}} (basé sur Kafka) pour la messagerie, vous pouvez vous connecter manuellement aux flux Kafka pour {{site.data.keyword.ieam}} afin de diagnostiquer les problèmes. Vous pouvez vous abonner à une rubrique de message pour voir les éléments reçus par {{site.data.keyword.message_hub_notm}}, ou publier dans une rubrique de message pour simuler des messages à partir d'un autre dispositif. La commande `kafkacat` {{site.data.keyword.linux_notm}} permet de publier sur {{site.data.keyword.message_hub_notm}} ou de s'y abonner. Utilisez la version la plus récente de cet outil. {{site.data.keyword.message_hub_notm}} fournit également des pages Web graphiques que vous pouvez utiliser pour accéder aux informations.

Sur tout noeud de périphérie où {{site.data.keyword.horizon}} est installé, utilisez la commande `hzn` pour déboguer les problèmes liés à  l'agent local {{site.data.keyword.horizon}} et à l'{{site.data.keyword.horizon_exchange}} distant. En interne, la commande `hzn` interagit avec les interfaces de programmation HTTP REST fournies. La commande `hzn` simplifie l'accès et offre une meilleure expérience utilisateur que les interfaces REST. Elle offre des descriptions plus détaillées dans sa sortie et bénéficie d'un système d'aide en ligne intégré. Utilisez ce dernier pour obtenir des informations et des détails sur les commandes à utiliser et sur la syntaxe et les arguments de commandes. Pour afficher ces informations d'aide, exécutez les commandes `hzn -- help` ou `hzn <subcommand> -- help`.

Sur les noeuds de périphérie où les packages {{site.data.keyword.horizon}} ne sont pas pris en charge ou installés, vous pouvez interagir directement avec les API REST HTTP sous-jacentes. Vous pouvez par exemple exécuter l'utilitaire `curl` ou d'autres utilitaires d'interface de ligne de commande d'API REST. Vous pouvez également écrire un programme dans un langage qui prend en charge les requêtes REST.

Par exemple, exécutez l'utilitaire `curl` pour vérifier l'état de votre noeud de périphérie :
```
curl localhost:8510/status
```
{: codeblock}

## Conseils relatifs au traitement des incidents
{: #ts_tips}

Pour vous aider à dépanner des problèmes spécifiques, lisez les questions relatives à l'état de votre système, ainsi que les conseils associés dans les rubriques ci-après. Pour chaque question, une description indiquant pourquoi la question est pertinente pour le traitement des incidents dans votre système est fournie. Parfois, des conseils ou une explication détaillée seront fournis pour savoir où trouver les informations appropriées pour votre système.

Ces questions sont fondées sur la nature des problèmes de débogage et sont liées à des environnements différents. Par exemple, lors du traitement des incidents sur un noeud de périphérie, vous pouvez avoir besoin d'un accès complet au noeud ainsi que d'un contrôle complet, ce qui améliore votre capacité de collecte et de visualisation des informations.

* [Conseils relatifs au traitement des incidents](troubleshooting_devices.md)

  Consultez les problèmes courants susceptibles de se produire lorsque vous utilisez {{site.data.keyword.ieam}}.
  
## Risques liés à {{site.data.keyword.ieam}} et résolution
{: #risks}

Si {{site.data.keyword.ieam}} offre des opportunités uniques, il pose également des défis importants. Par exemple, il dépasse les frontières physiques des centres de données cloud, ce qui peut vous exposer à des risques de sécurité, d'adressabilité, de gestion, de propriété et de conformité. Plus important encore, il décuple les problèmes de mise à l'échelle des techniques de gestion du cloud.

Les réseaux de périphérie augmentent de manière significative le nombre de noeuds de traitement. Les passerelles de périphérie sont également appelées à augmenter à un rythme encore plus soutenu. Quant aux dispositifs de périphérie, ils sont multipliés par 3 ou 4 puissances de dix. Si DevOps (distribution et déploiement continus) est essentiel à la gestion d'une infrastructure cloud à hyper grande échelle, les opérations sans intervention humaine sont vitales pour la gestion à l'échelle massive représentée par {{site.data.keyword.ieam}}.

Il est indispensable de déployer, mettre à jour, surveiller et récupérer l'espace de calcul de périphérie sans aucune intervention humaine. Toutes ces activités et tous ces processus doivent être :

* entièrement automatisés ;
* capables de prendre des décisions indépendantes pour allouer des travaux
* capables de reconnaître et de s'adapter aux conditions changeantes sans aucune intervention.

Toutes ces activités doivent être sécurisées, traçables et défendables.
