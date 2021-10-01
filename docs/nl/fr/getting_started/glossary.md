{:shortdesc: .shortdesc}
{:new_window: target="_blank"}

# Glossaire
*Dernière mise à jour : 6 mai 2021*

Ce glossaire comporte des termes et des définitions pour {{site.data.keyword.edge}}.
{:shortdesc}

Les références croisées suivantes sont utilisées dans ce glossaire :

- *Voir* renvoie d'un terme non préféré vers le terme préféré ou d'une abréviation vers sa forme non abrégée.
- *Voir aussi* renvoie à un terme connexe ou opposé.

<!--If you do not want letter links at the top of your glossary, delete the text between these comment tags.-->

[A](#glossa) [B](#glossb) [C](#glossc) [D](#glossd) [E](#glosse) [F](#glossf) [G](#glossg) [H](#glossh) [I](#glossi) [K](#glossk) [L](#glossl) [M](#glossm) [N](#glossn) [O](#glosso) [P](#glossp) [R](#glossr) [S](#glosss) [T](#glosst) [V](#glossv) [W](#glossw)

<!--end letter link tags-->

## A
{: #glossa}

### clé d'API
{: #x8051010}

Code unique transmis à une API pour identifier l'application ou l'utilisateur appelant. Cette clé sert à suivre et à contrôler la façon dont l'API est utilisée, pour empêcher, par exemple, son utilisation malveillante ou abusive.

### application
{: #x2000166}

Un ou plusieurs logiciels ou composants logiciels qui fournissent une fonction en support direct d'un ou de plusieurs processus métier spécifiques.

### zone de disponibilité
{: #x7018171}

Segment d'infrastructure réseau, indépendant des fonctionnalités et affecté par opérateur.

## B
{: #glossb}

### noeud d'amorçage
{: #x9520233}

Noeud qui est utilisé pour exécuter l'installation, la configuration, la mise à l'échelle de noeud et les mises à jour de cluster.

### stratégie métier
{: #x62309388}

(obsolète) Terme précédemment utilisé pour la stratégie de déploiement.

## C
{: #glossc}

### catalogue
{: #x2000504}

Emplacement centralisé qui peut être utilisé pour rechercher et installer des packages dans un cluster.

### cluster
{: #x2017080}

Ensemble de ressources, noeuds worker, réseaux et unités de stockage qui assurent une haute disponibilité des applications et les rendent prêtes à être déployées dans des conteneurs.

### contraintes
{: #x62309387}

Expressions logiques en termes de propriétés. Les contraintes sont utilisées pour contrôler et gérer le déploiement de logiciels sur des nœuds de périphérie.

### conteneur
{: #x2010901}

Construction système qui permet aux utilisateurs d'exécuter simultanément des instances de système d'exploitation logiques distinctes. Les conteneurs utilisent des couches de systèmes de fichier pour réduire la taille des images et promouvoir la réutilisation. Voir aussi [image](#x2024928), [couche](#x2028320), [registre](#x2064940).

### image de conteneur
{: #x8941555}

Dans Docker, logiciel exécutable, autonome, qui inclut du code et des outils système, pouvant être utilisé pour exécuter une application.

### orchestration de conteneur
{: #x9773849}

Processus de gestion du cycle de vie des conteneurs, incluant la mise à disposition, le déploiement et la disponibilité.

## D
{: #glossd}

### déploiement
{: #x2104544}

Processus qui extrait des packages ou des images et les installe à un emplacement défini pour permettre de les tester ou de les exécuter.

### pattern de déploiement
{: #x623093810}

Liste de services déployables spécifiques. Les modèles sont une simplification du mécanisme de règles d'administration plus général et plus compétent. Les nœuds de périphérie peuvent s'enregistrer avec un pattern de déploiement pour entraîner le déploiement de l'ensemble de services du pattern.

### règle de déploiement
{: #x62309386}

Ensemble de propriétés et de contraintes liées au déploiement d'un service spécifique avec un identificateur de la version de service à déployer et d'autres informations, telles que la façon dont les annulations doivent être gérées en cas d'échec.

### DevOps
{: #x5784896}

Méthodologie logicielle qui intègre le développement d'une application et les opérations informatiques de sorte que les équipes puissent fournir du code plus rapidement au service de production et itérer en continu en fonction des réactions du marché.

### Docker
{: #x7764788}

Plateforme ouverte pouvant être utilisée par les développeurs et les administrateurs système pour générer, livrer et exécuter des applications distribuées.

## E
{: #glosse}

### Informatique Edge
{: #x9794155}

Modèle informatique distribué qui tire profit de la capacité de calcul disponible en dehors des centres de données traditionnels et dans le cloud. Un modèle d'informatique Edge place une charge de travail au plus proche de là où les données associées sont créées et les mesures appropriées sont prises après analyse de ces données. Le fait d'installer les données et la charge de travail sur des dispositifs de périphérie diminue le temps d'attente, réduit les besoins sur la bande passante du réseau, améliore la protection des informations sensibles et autorise les opérations pendant les interruptions réseau.

### dispositif de périphérie
{: #x2026439}

Appareil, par exemple une machine d'assemblage dans un atelier, un distributeur automatique de billets, une caméra intelligente, une automobile, qui possède une capacité de calcul intégrée à partir de laquelle effectuer des tâches utiles et collecter et produire des données.

### passerelle de périphérie
{: #x9794163}

Cluster de périphérie qui offre des services d'exécution de fonctions réseau telles que la conversion de protocole, la terminaison de réseau, la tunnellisation, la protection par pare-feu ou les connexions sans fil. Une passerelle de périphérie sert de point de connexion entre un dispositif ou un cluster de périphérie et le cloud ou un réseau plus grand.

### noeud de périphérie
{: #x8317015}

Tout dispositif, cluster ou passerelle de périphérie où s'exécute l'informatique Edge.

### cluster de périphérie
{: #x2763197}

Ordinateur distant qui exécute les charges de travail des applications et les services partagés de l'entreprise. Un cluster de périphérie peut être utilisé pour se connecter à un dispositif de périphérie ou un autre serveur de périphérie, ou servir de passerelle de périphérie pour la connexion au cloud ou à un réseau plus vaste.

### service de périphérie
{: #x9794170}

Service conçu spécialement pour être déployé sur un cluster de périphérie, une passerelle de périphérie ou un dispositif de périphérie. La reconnaissance visuelle, les données acoustiques et la reconnaissance vocale sont des exemples de services de périphérie potentiels.

### charge de travail de périphérie
{: #x9794175}

Tout service, microservice ou logiciel qui exécute des tâches utiles sur un noeud de périphérie.

### noeud final
{: #x2026820}

Adresse de destination réseau qui est exposée par des ressources Kubernetes, comme des services ou des contrôleurs Ingress.

## F
{: #glossf}

## G
{: #glossg}

### Grafana
{: #x9773864}

Plateforme d'analyse et de visualisation open source pour surveiller, rechercher, analyser et visualiser les métriques.

## H
{: #glossh}

### HD
{: #x2404289}

Voir [haute disponibilité](#x2284708).

### charte Helm
{: #x9652777}

Package Helm qui contient des informations relatives à l'installation d'un ensemble de ressources Kubernetes dans un cluster Kubernetes.

### édition Helm
{: #x9756384}

Instance d'une charte Helm qui s'exécute dans un cluster Kubernetes.

### référentiel Helm
{: #x9756389}

Collection de chartes.

### haute disponibilité
{: #x2284708}

Capacité des services informatiques à faire face à toutes les indisponibilités et à poursuivre les traitements conformément à des niveaux de service prédéfinis. Les indisponibilités couvertes sont les événements planifiés, comme la maintenance et les sauvegardes, et les événements non planifiés, comme les incidents logiciels, matériels, les coupures d'alimentation et les sinistres. Voir aussi [tolérance aux pannes](#x2847028).

## I
{: #glossi}

### package IBM Cloud Pak
{: #x9773840}

Package qui comprend une ou plusieurs offres IBM Certified Container de niveau entreprise, sécurisées et gérées par cycle de vie, qui sont regroupées et intégrées dans l'environnement IBM Cloud.

### image
{: #x2024928}

Système de fichiers et ses paramètres d'exécution qui sont utilisés dans un environnement d'exécution de conteneur pour créer un conteneur. Le système de fichiers est composé de plusieurs couches, associées lors de l'exécution, qui sont créées lorsque l'image est générée par des mises à jour successives. L'image ne conserve pas son état lors de l'exécution du conteneur. Voir aussi [conteneur](#x2010901), [couche](#x2028320), [registre](#x2064940).

### registre d'images
{: #x3735328}

Emplacement centralisé pour la gestion des images.

### ingress
{: #x7907732}

Collection de règles autorisant des connexions entrantes vers les services de cluster Kubernetes.

### isolement
{: #x2196809}

Processus de confinement des déploiements de charge de travail vers des ressources virtuelles et physiques dédiées pour la prise en charge du partage de services.

## K
{: #glossk}

### Klusterlet
{: #x9773879}

Dans IBM Multicloud Manager, agent responsable d'un cluster Kubernetes unique.

### Kubernetes
{: #x9581829}

Outil d'orchestration open-source pour les conteneurs.

## L
{: #glossl}

### couche
{: #x2028320}

Version modifiée d'une image parent. Les images sont composées de couches, où la version modifiée est placée sur l'image parent, afin de créer la nouvelle image. Voir aussi [conteneur](#x2010901), [image](#x2024928).

### équilibreur de charge
{: #x2788902}

Logiciel ou matériel qui répartit la charge de travail sur un ensemble de serveurs afin d'assurer que ces derniers ne sont pas surchargés. L'équilibreur de charge dirige également les utilisateurs vers un autre serveur en cas de défaillance du serveur initial.

## M
{: #glossm}

### console de gestion
{: #x2398932}

Interface utilisateur graphique d'{{site.data.keyword.edge_notm}}.

### concentrateur de gestion
{: #x3954437}

Cluster qui héberge les composants {{site.data.keyword.edge_notm}} centraux.

### place du marché
{: #x2118141}

Liste des services activés à partir desquels les utilisateurs peuvent mettre à disposition des ressources.

### noeud maître
{: #x4790131}

Noeud qui fournit des services de gestion et contrôle les noeuds worker dans un cluster. Les noeuds maître hébergent les processus responsables de l'allocation des ressources, de la maintenance des états, de la planification et de la surveillance.

### microservice
{: #x8379238}

Ensemble constitué de composants d'architecture petits et indépendants, associés chacun à un objectif spécifique et communiquant via une API simple commune.

### multi-cloud
{: #x9581814}

Modèle de cloud dans lequel une entreprise utilise une combinaison d'architecture de cloud privé, public et sur site.

## N
{: #glossn}

### espace de nom
{: #x2031005}

Cluster virtuel au sein d'un cluster Kubernetes qui peut être utilisé pour organiser et diviser des ressources entre plusieurs utilisateurs.

### système NFS (Network File System)
{: #x2031282}

Protocole permettant à un ordinateur d'accéder à des fichiers sur un réseau comme s'ils se trouvaient sur ses disques locaux.

### NFS
{: #x2031508}

Voir [système NFS (Network File System)](#x2031282).

### règle de nœud
{: #x62309384}

Ensemble de propriétés et de contraintes liées à un nœud de périphérie (nœud de périphérie Linux autonome ou nœud de cluster Kubernetes).

## O
{: #glosso}

### org
{: #x7470494}

Voir [organisation](#x2032585).

### organisation (org)
{: #x2032585}

Le méta-objet le plus important de l'infrastructure {{site.data.keyword.edge_notm}} qui représente les objets d'un client.

## P
{: #glossp}

### schéma
{: #x62309389}

Voir [pattern de déploiement](#x623093810).

### volume persistant
{: #x9532496}

Stockage en réseau dans un cluster mis à disposition par un administrateur.

### réservation de volume persistant
{: #x9520297}

Demande de stockage de cluster.

### pod
{: #x8461823}

Groupe de conteneurs qui s'exécutent sur un cluster Kubernetes. Un pod est une unité de travail exécutable qui peut être une application autonome ou un microservice.

### politique de sécurité de pod
{: #x9520302}

Politique utilisée pour configurer un contrôle de niveau cluster sur ce que peut faire un pod et ce à quoi il peut accéder.

### policy
{: #x62309382}

Collection de zéro ou plusieurs propriétés et zéro ou plusieurs contraintes, parfois avec des zones de données supplémentaires. Voir [règle de nœud](#x62309384), [règle de service](#x62309385)et [règle de déploiement](#x62309386).

### Prometheus
{: #x9773892}

Kit d'outils d'alerte et de surveillance de systèmes open source.

### caractéristiques
{: #x62309381}

Paires nom/valeur, souvent utilisées pour décrire les attributs de nœud (modèle, numéro de série, rôle, fonctions, matériel connecté, etc.) ou les attributs d'un service ou d'un déploiement. Voir [règle](#x62309382).

### noeud proxy
{: #x6230938}

Noeud qui transmet des demandes externes aux services qui sont créés dans un cluster.

## R
{: #glossr}

### RBAC (Role-Based Access Control)
{: #x5488132}

Voir [contrôle d'accès à base de rôles](#x2403611).

### registre
{: #x2064940}

Stockage d'image de conteneur public ou privé et service de distribution. Voir aussi [conteneur](#x2010901), [image](#x2024928).

### réf
{: #x7639721}

Voir [référentiel](#x2036865).

### référentiel
{: #x2036865}

Zone de stockage persistant pour les données et les autres ressources d'application.

### ressource
{: #x2004267}

Composant physique ou logique pouvant être mis à disposition ou réservé pour une application ou une instance de service. Exemples de ressources : base de données, comptes, limites de processeur, de mémoire ou de stockage.

### contrôle d'accès à base de rôles
{: #x2403611}

Processus (également appelé RBAC, pour Role-Based Access Control) consistant à limiter l'accès à des composants globaux d'un système en fonction de l'authentification, des rôles et des autorisations de l'utilisateur.

## S
{: #glosss}

### courtier de services
{: #x7636561}

Composant d'un service qui implémente un catalogue d'offres et de plans de service et interprète les appels de mise à disposition, d'annulation de mise à disposition, de liaison et d'annulation de liaison.

### règle de service
{: #x62309385}

Ensemble de propriétés et de contraintes liées à un service déployable spécifique.

### noeud de stockage
{: #x3579301}

Noeud utilisé pour fournir le stockage de backend et le système de fichiers afin de stocker les données dans un système.

### syslog
{: #x3585117}

Voir [journal système](#x2178419).

### journal système (syslog)
{: #x2178419}

Journal qui est produit par les composants de Cloud Foundry.

## T
{: #glosst}

### équipe
{: #x3135729}

Entité qui regroupe des utilisateurs et des ressources.

## V
{: #glossv}

### VSAN
{: #x4592600}

Voir [réseau VSAN (Virtual Storage Area Network)](#x4592596).

## W
{: #glossw}

### noeud worker
{: #x5503637}

Dans un cluster, machine physique ou virtuelle effectuant les déploiements et les services qui constituent une application.

### charge de travail
{: #x2012537}

Une série de serveurs virtuels qui remplissent un objectif collectif défini par le client. Une charge de travail peut être considérée généralement comme une application multi-niveau. Chaque charge de travail est associée à un ensemble de politiques définissant des objectifs de performance et de consommation d'énergie.
