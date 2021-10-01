---

copyright:
years: 2019, 2020, 2021
lastupdated: "2021-09-01"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Conseils relatifs au traitement des incidents
{: #troubleshooting_devices}

Examinez les questions ci-dessous lorsque vous rencontrez un problème avec {{site.data.keyword.edge_notm}}. Les conseils et les guides fournis à chaque question peuvent vous aider à résoudre les problématiques communes et obtenir des informations en vue de déceler les causes premières.
{:shortdesc}

  * [Les dernières versions des packages {{site.data.keyword.horizon}} sont-elles installées ?](#install_horizon)
  * [L'agent {{site.data.keyword.horizon}} est-il opérationnel et en cours d'exécution ?](#setup_horizon)
  * [Le noeud de périphérie est-il configuré pour interagir avec {{site.data.keyword.horizon_exchange}} ?](#node_configured)
  * [Les conteneurs Docker requis pour le noeud de périphérie en cours d'exécution sont-ils en route ?](#node_running)
  * [Les versions attendues du conteneur de services sont-elles en cours d'exécution ?](#run_user_containers)
  * [Les conteneurs attendus sont-ils stables ?](#containers_stable)
  * [Vos conteneurs Docker sont-ils en réseau ?](#container_networked)
  * [Les conteneurs de dépendance sont-ils accessibles dans le contexte de votre conteneur ?](#setup_correct)
  * [Vos conteneurs définis par l'utilisateur envoient-ils des messages d'erreur au journal ?](#log_user_container_errors)
  * [Pouvez-vous utiliser l'instance du courtier Kafka {{site.data.keyword.message_hub_notm}} de votre organisation ?](#kafka_subscription)
  * [Vos conteneurs sont-ils publiés dans {{site.data.keyword.horizon_exchange}} ?](#publish_containers)
  * [Votre pattern de déploiement publié inclut-il tous les services et versions requis ?](#services_included)
  * [Conseils relatifs au traitement des incidents dans l'environnement {{site.data.keyword.open_shift_cp}}](#troubleshooting_icp)
  * [Dépannage des erreurs de noeud](#troubleshooting_node_errors)
  * [Comment désinstaller Podman sur RHEL ?](#uninstall_podman)

## Les dernières versions des packages {{site.data.keyword.horizon}} sont-elles installées ?
{: #install_horizon}

Vérifiez que le logiciel {{site.data.keyword.horizon}} installé sur vos noeuds de périphérie correspond toujours à la version la plus récente.

Sur un système {{site.data.keyword.linux_notm}}, vous pouvez vérifier la version des packages {{site.data.keyword.horizon}} installés à l'aide de la commande suivante :  
```
dpkg -l | grep horizon
```
{: codeblock}

Vous pouvez mettre à jour vos packages {{site.data.keyword.horizon}} qui utilisent le gestionnaire de package sur votre système. Par exemple, sur un système {{site.data.keyword.linux_notm}} basé sur Ubuntu, utilisez les commandes ci-dessous pour mettre à jour {{site.data.keyword.horizon}} vers la version en cours :
```
sudo apt update sudo apt install -y blue horizon
```

## L'agent {{site.data.keyword.horizon}} est-il opérationnel et en cours d'exécution ?
{: #setup_horizon}

Vous pouvez vérifier que l'agent est en cours d'exécution en utilisant la commande de l'interface de ligne de commande {{site.data.keyword.horizon}} suivante :
```
hzn node list | jq .
```
{: codeblock}

Vous pouvez également utiliser le logiciel de gestion des systèmes hôte pour vérifier le statut de l'agent {{site.data.keyword.horizon}}. Par exemple, sur un système {{site.data.keyword.linux_notm}} basé sur Ubuntu, exécutez l'utilitaire `systemctl` comme suit :
```
sudo systemctl status horizon
```
{: codeblock}

Une ligne similaire à celle ci-dessous s'affiche si l'agent est actif :
```
Active: active (running) since Thu 2020-10-01 17:56:12 UTC; 2 weeks 0 days ago
```
{: codeblock}

## Le noeud de périphérie est-il configuré pour interagir avec {{site.data.keyword.horizon_exchange}} ? 
{: #node_configured}

Pour vérifier que vous pouvez communiquer avec {{site.data.keyword.horizon_exchange}}, exécutez la commande suivante :
```
hzn exchange version
```
{: codeblock}

Pour vérifier que votre {{site.data.keyword.horizon_exchange}} est accessible, exécutez la commande suivante :
```
hzn exchange user list
```
{: codeblock}

Lorsque vous avez enregistré votre noeud de périphérie auprès d'{{site.data.keyword.horizon}}, vérifiez s'il interagit avec {{site.data.keyword.horizon_exchange}} en affichant la configuration de l'agent {{site.data.keyword.horizon}} local. Exécutez la commande ci-dessous pour afficher la configuration de l'agent :
```
hzn node list | jq .configuration.exchange_api
```
{: codeblock}

## Les conteneurs Docker requis pour le noeud de périphérie sont-ils en cours d'exécution ?
{: #node_running}

Lorsque votre noeud de périphérie est enregistré avec {{site.data.keyword.horizon}}, un agbot {{site.data.keyword.horizon}} crée un accord avec votre noeud de périphérie pour exécuter les services qui sont référencés dans votre type de passerelle (pattern de déploiement). Si cet accord n'est pas créé, effectuez les vérifications suivantes pour corriger le problème.

Confirmez l'état `configured` de votre noeud de périphérie et vérifiez ses valeurs `id` et `organization`. Par ailleurs, confirmez que l'architecture pour laquelle {{site.data.keyword.horizon}} produit des rapports est la même que celle utilisée dans les métadonnées pour vos services. Exécutez la commande ci-dessous pour dresser la liste de ces paramètres :
```
hzn node list | jq .
```
{: codeblock}

Si ces valeurs sont conformes à celles attendues, vous pouvez vérifier le statut d'accord du noeud de périphérie en exécutant la commande suivante : 
```
hzn agreement list | jq .
```
{: codeblock}

Si la commande ne renvoie aucun accord, il se peut qu'un accord ait été formé mais qu'un problème a été rencontré. Si cela se produit, l'accord peut être annulé avant même d'apparaître dans la sortie de la commande précédente. En cas d'annulation, l'accord annulé figure avec le statut `terminated_description` dans la liste des accords archivés. Vous pouvez consulter cette liste en exécutant la commande : 
```
hzn agreement list -r | jq .
```
{: codeblock}

Un problème peut également se produire avant qu'un accord ne soit créé. Dans ce cas, examinez le journal des événements de l'agent {{site.data.keyword.horizon}} pour identifier les erreurs possibles. Exécutez la commande suivante pour afficher le journal : 
```
hzn eventlog list
``` 
{: codeblock}

Le journal des événements peut indiquer les erreurs suivantes : 

* La signature des métadonnées de service, en particulier la zone `deployment`, ne peut pas être vérifiée. Cette erreur indique généralement que votre clé publique de signature n'est pas importée dans votre noeud de périphérie. Vous pouvez importer la clé à l'aide de la commande `hzn key import -k <pubkey>`. Vous pouvez afficher les clés qui sont importées dans votre noeud de périphérie local en exécutant la commande `hzn key list`. Vous pouvez vérifier que les métadonnées de service dans {{site.data.keyword.horizon_exchange}} sont signées avec votre clé en utilisant la commande suivante :
  ```
  hzn exchange service verify -k $PUBLIC_KEY_FILE <service-id>
  ```
  {: codeblock} 

Remplacez `<service-id>` par l'ID de votre service. Celui-ci peut ressembler à l'exemple qui suit : `workload-cpu2wiotp_${CPU2WIOTP_VERSION}_${ARCH2}`.

* Le chemin de l'image Docker dans la zone `deployment` du service est incorrect. Confirmez que votre noeud de périphérie peut exécuter la commande `docker pull` pour extraire le chemin d'accès à cette image.
* L'agent {{site.data.keyword.horizon}} sur votre noeud de périphérie n'a pas accès au registre Docker qui stocke vos images Docker. Si les images Docker contenues dans le registre Docker distant ne sont pas accessibles en lecture à tous, ajoutez vos données d'identification à votre noeud de périphérie via la commande `docker login`. Vous n'avez besoin d'effectuer cette étape qu'une seule fois, car les données d'identification sont mémorisées sur le noeud de périphérie.
* Si un conteneur redémarre continuellement, consultez le journal du conteneur pour plus de détails. Un conteneur peut redémarrer continuellement lorsqu'il s'affiche l'espace de quelques secondes seulement ou qu'il reste affiché comme étant en cours de redémarrage lorsque vous exécutez la commande `docker ps`. Vous pouvez afficher le journal du conteneur pour obtenir plus de détails en exécutant la commande :
  ```
  grep --text -E ' <service-id>\[[0-9]+\]' /var/log/syslog
  ```
  {: codeblock}

## Les versions attendues du conteneur de service sont-elles en cours d'exécution ?
{: #run_user_containers}

Les versions de votre conteneur sont régies par un accord qui est créé après avoir ajouté votre service au pattern de déploiement et après avoir enregistré votre noeud de périphérie auprès de ce pattern. Vérifiez que votre noeud de périphérie possède un accord en cours avec votre pattern, en exécutant la commande :

```
hzn agreement list | jq .
```
{: codeblock}

Si vous avez confirmé que vous disposez d'un accord approprié pour votre pattern, utilisez la commande ci-dessous pour afficher les conteneurs en cours d'exécution. Vérifiez que les conteneurs définis par l'utilisateur sont répertoriés et qu'ils sont opérationnels :
```
docker ps
```
{: codeblock}

Plusieurs minutes peuvent être nécessaires à l'agent {{site.data.keyword.horizon}} après que l'accord ait été accepté, pour télécharger, vérifier et mettre en place les conteneurs correspondants. Cet accord dépend principalement de la taille des conteneurs à extraire des référentiels distants.

## Les conteneurs attendus sont-ils stables ?
{: #containers_stable}

Vérifiez si vos conteneurs sont stables en exécutant cette commande :
```
docker ps
```
{: codeblock}

A partir du résultat de la commande, contrôlez la durée d'exécution de chaque conteneur. Si vous observez que vos conteneurs redémarrent de manière inattendue, consultez les journaux du conteneur pour rechercher des erreurs éventuelles.

Une bonne pratique de développement consiste à configurer une consignation de service individuelle en exécutant les commandes suivantes (systèmes {{site.data.keyword.linux_notm}} uniquement) :
```bash
cat <<'EOF' > /etc/rsyslog.d/10-horizon-docker.conf $template DynamicWorkloadFile,"/var/log/workload/%syslogtag:R,ERE,1,DFLT:.*workload-([^\[]+)--end%.log"  :syslogtag, startswith, "workload-" -?DynamicWorkloadFile & stop :syslogtag, startswith, "docker/" -/var/log/docker_containers.log & stop :syslogtag, startswith, "docker" -/var/log/docker.log & stop EOF service rsyslog restart
```
{: codeblock}

Si vous avez exécuté l'étape précédente, les journaux de vos conteneurs sont enregistrés dans des fichiers séparés sous le répertoire `/var/log/workload/`. Exécutez la commande `docker ps` pour rechercher le nom complet de vos conteneurs. Vous trouverez le fichier journal correspondant, avec le suffixe `.log`, dans ce répertoire.

Si la journalisation des services individuels n'est pas configurée, vos journaux de service sont ajoutés au journal système avec tous les autres messages de journal. Pour consulter les données de vos conteneurs, recherchez le nom du conteneur dans la sortie du journal système sous `/var/log/syslog`. Par exemple, exécutez une commande similaire à celle qui suit pour faire une recherche dans le journal :
```
grep --text -E 'YOURSERVICENAME\[[0-9]+\]' /var/log/syslog
```
{: codeblock}

## Vos conteneurs Docker sont-ils en réseau ?
{: #container_networked}

Vérifiez que vos conteneurs Docker sont correctement mis en réseau pour permettre l'accès aux services requis. Exécutez la commande ci-dessous pour afficher les réseaux virtuels Docker actifs sur votre noeud de périphérie :
```
docker network list
```
{: codeblock}

Pour afficher des informations supplémentaires sur un réseau particulier, utilisez la commande `docker inspect X`, où `X` est le nom du réseau. Le résultat de la commande répertorie tous les conteneurs qui s'exécutent sur le réseau virtuel.

Vous pouvez également exécuter la commande `docker inspect Y` sur chaque conteneur, où `Y` est le nom du conteneur, pour en savoir encore davantage. Par exemple, examinez les informations de conteneur `NetworkSettings`, puis recherchez le conteneur `Networks`. Dans ce conteneur, vous pouvez afficher la chaîne ID de réseau appropriée, ainsi que des informations sur la manière dont le conteneur est représenté sur le réseau. Parmi ces informations figurent le conteneur `IPAddress` et la liste de tous les alias réseau qui se trouvent sur ce réseau. 

Des noms d'alias sont mis à la disposition de tous les conteneurs de ce réseau virtuel, et ces noms sont généralement utilisés par les conteneurs dans votre pattern de déploiement de code pour découvrir d'autres conteneurs sur le réseau virtuel. Par exemple, vous pouvez nommer votre service `myservice`. Ensuite, d'autres conteneurs peuvent utiliser ce nom directement pour y accéder sur le réseau, par exemple à l'aide de la commande `ping myservice`. Le nom d'alias de votre conteneur est spécifié dans la zone `deployment` de son fichier de définition de service que vous avez transmis à la commande `hzn exchange service publish`.

Pour plus d'informations sur les commandes prises en charge par l'interface de ligne de commande Docker, voir [Docker command reference](https://docs.docker.com/engine/reference/commandline/docker/#child-commands).

## Les conteneurs de dépendance sont-ils accessibles dans le contexte de votre conteneur ?
{: #setup_correct}

Entrez le contexte de votre conteneur actif afin de résoudre les problèmes au moment de l'exécution en utilisant la commande `docker exec`. Utilisez la commande `docker ps` pour rechercher l'identificateur de votre conteneur en cours d'exécution, puis lancez une commande similaire à celle indiquée ci-après pour entrer le contexte. Remplacez `CONTAINERID` par l'identificateur de votre conteneur :
```
docker exec -it CONTAINERID /bin/sh
```
{: codeblock}

Si votre conteneur inclut la valeur bash, vous pouvez spécifier `/bin/bash` à la fin de la commande ci-dessus au lieu de `/bin/sh`.

Une fois dans le contexte du conteneur, vous pouvez utiliser des commandes telles que `ping` ou `curl` pour interagir avec les conteneurs dont elle a besoin et vérifier la connectivité.

Pour plus d'informations sur les commandes prises en charge par l'interface de ligne de commande Docker, voir [Docker command reference](https://docs.docker.com/engine/reference/commandline/docker/#child-commands).

## Vos conteneurs définis par les utilisateurs envoient-ils des messages d'erreur au journal ?
{: #log_user_container_errors}

Si vous avez configuré la journalisation de service individuel, chacun de vos conteneurs se connecte à un fichier distinct dans le répertoire `/var/log/workload/`. Exécutez la commande `docker ps` pour rechercher le nom complet de vos conteneurs. Recherchez ensuite le fichier portant ce nom, suivi du suffixe `.log`, dans ce répertoire.

Si la consignation de service individuelle n'est pas configurée, vos journaux de service sont consignés dans le journal système avec d'autres informations. Pour consulter les données, recherchez le journal du conteneur dans la sortie du journal système sous le répertoire `/var/log/syslog`. Par exemple, exécutez une commande similaire à celle qui suit pour faire une recherche dans le journal :
```
grep --text -E 'YOURSERVICENAME\[[0-9]+\]' /var/log/syslog
```
{: codeblock}

## Pouvez-vous utiliser l'instance du courtier Kafka {{site.data.keyword.message_hub_notm}} de votre organisation ?
{: #kafka_subscription}

L'abonnement à l'instance Kafka de votre organisation à partir d'{{site.data.keyword.message_hub_notm}} peut vous aider à vérifier que vos données d'identification de l'utilisateur Kafka sont correctes. Il peut également vous aider à vérifier que votre instance de service Kafka est en cours d'exécution dans le cloud, et que votre noeud de périphérie envoie les données lorsque des données sont publiées.

Pour vous abonner à votre courtier Kafka, installez le programme `kafkacat`. Par exemple, sur un système {{site.data.keyword.linux_notm}} Ubuntu, exécutez la commande :

```bash
sudo apt install kafkacat
```
{: codeblock}

Une fois le programme installé, abonnez-vous en exécutant une commande similaire à l'exemple ci-dessous qui a recours aux données d'identification généralement utilisées dans les références de variables d'environnement :

```bash
kafkacat -C -q -o end -f "%t/%p/%o/%k: %s\n" -b $EVTSTREAMS_BROKER_URL -X api.version.request=true -X security.protocol=sasl_ssl -X sasl.mechanisms=PLAIN -X sasl.username=token -X sasl.password=$EVTSTREAMS_API_KEY -t $EVTSTREAMS_TOPIC
```
{: codeblock}

Où `EVTSTREAMS_BROKER_URL` est l'adresse URL de votre courtier Kafka, `EVTSTREAMS_TOPIC` est votre rubrique Kafka et `EVTSTREAMS_API_KEY` est votre clé d'interface de programmation pour l'authentification avec l'API {{site.data.keyword.message_hub_notm}}.

Si la commande d'abonnement aboutit, la commande est indéfiniment bloquée. Elle attend une publication dans votre courtier Kafka et extrait et affiche les messages qui en découlent. Si aucun message n'est reçu de votre noeud de périphérie au bout de plusieurs minutes, consultez le journal du service à la recherche de messages d'erreur.

Par exemple, pour consulter le journal du service `cpu2evtstreams`, exécutez la commande suivante :

* Pour {{site.data.keyword.linux_notm}} et {{site.data.keyword.windows_notm}} 

```bash
tail -n 500 -f /var/log/syslog | grep -E 'cpu2evtstreams\[[0-9]+\]:'
```
{: codeblock}

* Pour macOS

```bash
docker logs -f $(docker ps --filter 'name=-cpu2evtstreams' | tail -n +2 | awk '{print $1}')
```
{: codeblock}

## Vos conteneurs sont-ils publiés dans {{site.data.keyword.horizon_exchange}} ?
{: #publish_containers}

{{site.data.keyword.horizon_exchange}} est l'entrepôt central des métadonnées relatives au code qui est publié pour vos noeuds de périphérie. Si vous n'avez pas signé ni publié votre code dans {{site.data.keyword.horizon_exchange}}, il ne peut pas être extrait vers vos noeuds de périphérie, qui sont vérifiés et exécutés.

Exécutez la commande `hzn` avec les arguments ci-dessous pour afficher la liste des codes publiés et vérifier que tous vos conteneurs de service ont été correctement publiés :

```
hzn exchange service list | jq .
hzn exchange service list $ORG_ID/$SERVICE | jq .
```
{: codeblock}

Le paramètre `$ORG_ID` est votre ID d'organisation et `$SERVICE` est le nom du service au sujet duquel vous récupérez des informations.

## Votre pattern de dépliement inclut-il tous les services et versions requis ?
{: #services_included}

Sur n'importe quel noeud de périphérie  où la commande `hzn` est installée, vous pouvez utiliser cette commande pour obtenir des détails sur les patterns de déploiement. Exécutez la commande `hzn` avec les arguments suivants pour extraire la liste des patterns de déploiement à partir de l'{{site.data.keyword.horizon_exchange}} : 

```
hzn exchange pattern list | jq .
hzn exchange pattern list $ORG_ID/$PATTERN | jq .
```
{: codeblock}

Le paramètre `$ORG_ID` est votre ID d'organisation et `$PATTERN` est le nom du pattern de déploiement au sujet duquel vous récupérez des informations.

## Conseils relatifs au traitement des incidents dans l'environnement {{site.data.keyword.open_shift_cp}}
{: #troubleshooting_icp}

Prenez connaissance des questions suivantes pour vous aider à résoudre les problèmes les plus courants dans les environnements {{site.data.keyword.open_shift_cp}} au sujet d'{{site.data.keyword.edge_notm}}. Ces conseils peuvent vous aider à résoudre les problématiques communes et obtenir des informations en vue de déceler les causes premières.
{:shortdesc}

### Vos données d'identification {{site.data.keyword.edge_notm}} sont-elles configurées correctement pour l'environnement {{site.data.keyword.open_shift_cp}} ?
{: #setup_correct}

Vous avez besoin d'un compte utilisateur {{site.data.keyword.open_shift_cp}} pour effectuer une action dans cet environnement {{site.data.keyword.edge_notm}}. Vous avez également besoin d'une clé d'interface de programmation créée à partir de ce compte.

Pour vérifier vos données d'identification {{site.data.keyword.edge_notm}} dans cet environnement, exécutez la commande suivante :

   ```
   hzn exchange user list
   ```
   {: codeblock}

Si une entrée au format JSON, indiquant un ou plusieurs utilisateurs, est renvoyée par Exchange, les données d'identification {{site.data.keyword.edge_notm}} sont correctement configurées.

Si la réponse renvoyée est une erreur, prenez les mesures nécessaires pour dépanner la configuration de vos données d'identification.

Si le message d'erreur indique une clé d'interface de programmation incorrecte, créez une clé qui utilise les commandes ci-dessous.

Voir [Création de votre clé d'API](../hub/prepare_for_edge_nodes.md).

## Dépannage des erreurs de noeud
{: #troubleshooting_node_errors}

{{site.data.keyword.edge_notm}} publie un sous-ensemble des journaux d'événements sur le réseau Exchange, que vous pouvez consulter depuis la {{site.data.keyword.gui}}. Ces erreurs sont associées à des conseils de dépannage.
{:shortdesc}

  - [Erreur liée au chargement d'image](#eil)
  - [Erreur liée à la configuration du déploiement](#eidc)
  - [Erreur liée au démarrage du conteneur](#esc)
  - [Erreur interne TLS de cluster de périphérie OCP](#tls_internal)

### Erreur liée au chargement d'image
{: #eil}

Cette erreur survient lorsque l'image de service référencée dans la définition de service n'existe pas dans le référentiel d'images. Pour la résoudre, procédez comme suit :

1. Republiez le service sans l'indicateur **-I**.
    ```
    hzn exchange service publish -f <service-definition-file>
    ```
    {: codeblock}

2. Envoyez l'image de service directement vers le référentiel d'images. 
    ```
    docker push <image name>
    ```
    {: codeblock} 
    
### Erreur liée à la configuration du déploiement
{: #eidc}

Cette erreur se produit lorsque les configurations de déploiement des définitions de service indiquent une liaison vers un fichier protégé par des droits d'accès root. Pour la résoudre, procédez comme suit :

1. Liez le conteneur à un fichier qui n'est pas protégé par des droits d'accès root.
2. Modifiez les droits d'accès au fichier afin de permettre aux utilisateurs de lire et d'écrire dans le fichier.

### Erreur liée au démarrage du conteneur
{: #esc}

Cette erreur se produit lorsque Docker rencontre un problème au démarrage du conteneur de service. Le message d'erreur peut contenir des détails indiquant la raison pour laquelle le conteneur n'a pas pu démarrer. Les étapes de résolution dépendent de l'erreur elle-même. Les erreurs suivantes peuvent se produire :

1. Le dispositif utilise déjà un port publié défini par les configurations de déploiement. Pour résoudre l'erreur : 

    - Mappez un port différent vers le port du conteneur de service. Le numéro de port affiché ne doit pas obligatoirement être identique à celui du service.
    - Arrêtez le programme qui utilise le même port.

2. Un port publié spécifié par les configurations de déploiement n'est pas un numéro de port valide. Les numéros de port doivent être compris entre 1 et 65535.
3. Un nom de volume dans les configurations de déploiement n'est pas un chemin d'accès valide. Les chemins de volume doivent être définis par leurs chemins d'accès absolus (et non relatifs). 

### Erreur interne TLS de cluster de périphérie OCP

  ```
  Error from server: error dialing backend: remote error: tls: internal error
  ```
  {: codeblock} 

Si cette erreur apparaît à la fin du processus d'installation d'agent de cluster ou lors de la tentative d'interaction avec le pod d'agent, il se peut qu'il y ait un problème au niveau des demandes de signature de certificat de votre cluster OCP. 

1. Vérifiez si vous avez des demandes de signature de certificat à l'état En attente :

    ```
    oc get csr
    ```
    {: codeblock} 

2. Approuvez les demandes de signature de certificat en attente :

  ```
  oc adm certificate approve <csr-name>
  ```
  {: codeblock}
    
**Remarque** : vous pouvez approuver toutes les demandes de signature de certificat à l'aide d'une seule commande :

  ```
  for i in `oc get csr |grep Pending |awk '{print $1}'`; do oc adm certificate approve $i; done
  ```
  {: codeblock}

### Renseignements supplémentaires

Pour plus d'informations, voir :
  * [Traitement des incidents ](../troubleshoot/troubleshooting.md)
