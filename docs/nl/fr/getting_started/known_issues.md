---

copyright:
  years: 2019, 2020
lastupdated: "2021-08-31"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Problèmes connus et limitations  
{: #knownissues}

Il s'agit de problèmes connus et de limitations de {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}).

Pour obtenir une liste complète des problèmes ouverts pour la couche {{site.data.keyword.ieam}} OpenSource, consultez les problèmes GitHub dans chacun des [référentiels Open Horizon](https://github.com/open-horizon/).

{:shortdesc}

## Problèmes connus de {{site.data.keyword.ieam}} {{site.data.keyword.version}}

Il s'agit de problèmes connus et de limitations pour {{site.data.keyword.ieam}} {{site.data.keyword.version}}.

* {{site.data.keyword.ieam}} n'effectue pas d'analyse de logiciels malveillants ou de virus sur les données téléchargées sur le système de gestion de modèles (MMS). Pour plus d'informations sur la sécurité MMS, voir [Sécurité et confidentialité](../OH/docs/user_management/security_privacy.md#malware).

* L'option **-f <directory>** de **edgeNodeFiles.sh** n'a pas l'effet prévu. En revanche, les fichiers sont collectés dans le répertoire en cours. Pour plus d'informations, voir [Problème 2187](https://github.com/open-horizon/anax/issues/2187). Pour résoudre le problème, exécutez la commande en procédant comme suit :

   ```bash
   (cd <dir> && edgeNodeFiles.sh ... )
   ```
   {: codeblock}



* Dans le cadre de l'installation de {{site.data.keyword.ieam}}, selon la version de {{site.data.keyword.common_services}} installée, des certificats peuvent avoir été créés avec une durée de vie courte entraînant leur renouvellement automatique. Vous pouvez rencontrer les problèmes de certificat suivants ([qui peuvent être résolus avec ces étapes](cert_refresh.md)) :
  * La sortie JSON inattendue s'affiche avec le message « Request failed with status code 502 » lorsque vous accédez à la console de gestion {{site.data.keyword.ieam}}.
  * Les nœuds de périphérie ne sont pas mis à jour lorsqu'un certificat est renouvelé et doivent être mis à jour manuellement pour garantir la réussite de la communication avec le {{site.data.keyword.ieam}} concentrateur.

* Lors de l'utilisation{{site.data.keyword.ieam}} avec des bases de données locales, si le **pod cssdb** est supprimé et recréé, que ce soit manuellement ou automatiquement via le planificateur Kubernetes, cela entraînera une perte de données pour la base de données Mongo. Consultez la documentation sur la [sauvegarde et la récupération](../admin/backup_recovery.md) afin d'atténuer la perte de données.

* Lors de l'utilisation{{site.data.keyword.ieam}} de bases de données locales, si les ressources du travail** create-agbotdb-cluster** ou **create-exchangedb-cluster** sont supprimées, le travail ré-exécutera et réinitialisera la base de données respective, ce qui entraîne une perte de données. Consultez la documentation sur la [sauvegarde et la récupération](../admin/backup_recovery.md) afin d'atténuer la perte de données.

* Lorsque vous utilisez des bases de données locales, l'une ou les deux bases de données postgres peuvent ne plus répondre. Pour résoudre ce problème, redémarrez tous les Sentinels et les proxys pour la base de données qui ne répond pas. Modifiez et exécutez les commandes suivantes avec l'application impactée et votre ressource personnalisée (CR) `oc rollout restart deploy <CR_NAME>-<agbot|exchange>db-sentinel` et `oc rollout restart deploy <CR_NAME>-<agbot|exchange>db-proxy` (exemple exchange sentinelexam : `oc rollout restart deploy ibm-edge-exchangedb-sentinel`).

* Si vous exécutez **hzn service log **on{{site.data.keyword.rhel}} avec une architecture quelconque, la commande se bloque. Pour plus d'informations, voir [Problème 2826](https://github.com/open-horizon/anax/issues/2826). Pour contourner cette condition, obtenez les journaux du conteneur (vous pouvez également spécifier -f pour le fichier) :

   ```
   Conteneur de dockers &amp;TWBLT; conteneur &gt;
   ```
   {: codeblock}


## Limitations de {{site.data.keyword.ieam}} {{site.data.keyword.version}}

* La documentation du produit {{site.data.keyword.ieam}} est traduite pour les unités géographiques concernées par ce produit, mais la version anglaise est continuellement mise à jour. Des différences entre la version anglaise et les versions traduites peuvent apparaître entre deux cycles de traduction. Dans la version anglaise, vérifiez si des différences ont été résolues après la publication des versions traduites.

* Si vous modifiez les attributs **owner** ou **public** des services, des canevas ou des règles de déploiement dans l'échange, l'accès à ces ressources pour afficher la modification peut prendre jusqu'à cinq minutes. De même, lorsque vous accordez le droit d'administration à un utilisateur d'échange, la propagation de cette modification à toutes les instances d'échange peut prendre jusqu'à cinq minutes. Cette durée peut être réduite en définissant le paramètre `api.cache.resourcesTtlSeconds` sur une valeur plus faible (la valeur par défaut est de 300 secondes) dans le fichier Exchange `config.json`, mais les performances seront légèrement moins bonnes.

* L'agent ne prend pas en charge le [système de gestion de modèle](../developing/model_management_system.md) (MMS) pour les services dépendants.

* La liaison secrète ne fonctionne pas pour un service sans accord défini dans un modèle.
 
* L'agent de cluster d'arête ne prend pas en charge K3S v1.21.3+k3s1 car le répertoire de volume monté ne dispose que de 0700 autorisations. Voir [Impossible d'écrire des données dans le PVC local](https://github.com/k3s-io/k3s/issues/3704) pour une solution temporaire.
 
* Chaque {{site.data.keyword.ieam}} agent de noeud de périphérie lance toutes les connexions réseau avec le {{site.data.keyword.ieam}} concentrateur de gestion. Le concentrateur de gestion ne lance jamais de connexions à ses noeuds de périphérie. Par conséquent, un noeud de périphérie peut être derrière un pare-feu NAT si le pare-feu dispose de la connectivité TCP vers le concentrateur de gestion. Toutefois, les noeuds de périphérie ne peuvent pas communiquer actuellement avec le concentrateur de gestion via un proxy SOCKS.
  
* L'installation des dispositifs de périphérie avec Fedora ou SuSE n'est prise en charge que par la méthode [Procédure manuelle avancée d'installation et d'enregistrement d'un agent](../installing/advanced_man_install.md).
