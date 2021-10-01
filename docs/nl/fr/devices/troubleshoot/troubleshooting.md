---

copyright:
years: 2019
lastupdated: "2019-06-25"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Traitement des incidents
{: #troubleshooting}

Consultez les conseils de dépannage et les problèmes courants qui se produisent sous {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) pour vous aider à résoudre tous les problèmes que vous rencontrez.
{:shortdesc}

Les guides de dépannage ci-après décrivent les composants principaux d'un système {{site.data.keyword.ieam}} ainsi que la manière d'analyser les interfaces intégrées pour déterminer l'état du système.

## Outils de traitement des incidents
{: #ts_tools}

De nombreuses interfaces intégrées à {{site.data.keyword.ieam}} fournissent des informations qui peuvent servir à diagnostiquer des problèmes. Ces informations sont disponibles via la {{site.data.keyword.gui}}, les API REST HTTP et un outil shell {{site.data.keyword.linux_notm}}, `hzn`.

Sur une machine de périphérie, vous pouvez être amené à dépanner des problèmes liés à l'hôte, au logiciel Horizon ou à Docker, ou des problèmes liés à la configuration ou au code de vos conteneurs de service. Les problèmes d'hôte de machine de périphérie dépassent la portée du présent document. Si vous devez corriger des problèmes liés à Docker, de nombreuses commandes et interfaces Docker sont mises à votre disposition. Pour plus d'informations, consultez la documentation Docker.

Si les conteneurs de service que vous exécutez utilisent {{site.data.keyword.message_hub_notm}} (basé sur Kafka) pour la messagerie, vous pouvez vous connecter manuellement aux flux Kafka pour {{site.data.keyword.ieam}} afin de diagnostiquer les problèmes. Vous pouvez vous abonner à une rubrique de message pour voir les éléments reçus par {{site.data.keyword.message_hub_notm}}, ou publier dans une rubrique de message pour simuler des messages à partir d'un autre dispositif. La commande {{site.data.keyword.linux_notm}} `kafkacat` constitue un moyen simple de publier ou de s'abonner à {{site.data.keyword.message_hub_notm}}. Utilisez la version la plus récente de cet outil. {{site.data.keyword.message_hub_notm}} fournit également des pages Web graphiques que vous pouvez utiliser pour accéder aux informations.

Sur les machines sur lesquelles {{site.data.keyword.horizon}} est installé, la commande `hzn` permet de déboguer les problèmes liés à l'agent {{site.data.keyword.horizon}} local et à l'application {{site.data.keyword.horizon_exchange}} distante. En interne, la commande `hzn` interagit avec les interfaces de programmation HTTP REST fournies. La commande `hzn` simplifie l'accès et offre une meilleure expérience utilisateur que les interfaces REST. Elle offre des descriptions plus détaillées dans sa sortie et bénéficie d'un système d'aide en ligne intégré. Utilisez ce dernier pour obtenir des informations et des détails sur les commandes à utiliser et sur la syntaxe et les arguments de commandes. Pour afficher les informations d'aide, exécutez les commandes `hzn --help` ou `hzn \<subcommand\> --help`.

Sur les noeuds sur lesquels les packages {{site.data.keyword.horizon}} ne sont pas installés ni pris en charge, vous pouvez directement interagir avec les API HTTP REST sous-jacentes. Vous pouvez par exemple exécuter l'utilitaire `curl` ou d'autres utilitaires d'interface de ligne de commande d'API REST. Vous pouvez également écrire un programme dans un langage qui prend en charge les requêtes REST. 

## Conseils relatifs au traitement des incidents
{: #ts_tips}

Pour vous aider à dépanner des problèmes spécifiques, lisez les questions relatives à l'état de votre système, ainsi que les conseils associés dans les rubriques ci-après. Pour chaque question, il vous sera expliqué pourquoi celle-ci est importante pour vous aider à dépanner votre système. Parfois, des conseils ou une explication détaillée seront fournis pour savoir où trouver les informations appropriées pour votre système.

Ces questions sont fondées sur la nature des problèmes de débogage et sont liées à des environnements différents. Par exemple, lorsque vous dépannez des problèmes sur un noeud de périphérie, vous pouvez avoir besoin d'un accès et d'un contrôle total sur le noeud, afin de pouvoir collecter et visualiser davantage d'informations.

* [Conseils relatifs au traitement des incidents](troubleshooting_devices.md)

  Consultez les problèmes courants susceptibles de se produire lorsque vous utilisez {{site.data.keyword.ieam}}.
