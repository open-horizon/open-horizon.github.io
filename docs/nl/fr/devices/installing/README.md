# IBM Edge Computing Manager

## Introduction

IBM Edge Computing Manager for Devices fournit une **plateforme de gestion d'applications** de bout en bout pour les applications déployées sur les dispositifs de périphérie typiques des déploiements IoT. Cette plateforme automatise complètement le processus et libère les développeurs d'applications de la tâche fastidieuse de déploiement des révisions des charges de travail de périphérie sur des milliers de dispositifs de périphérie déployés sur le terrain. Ce changement permet aux développeurs de se concentrer pleinement sur la tâche d'écriture du code d'application dans n'importe quel langage de programmation comme un conteneur Docker pouvant être déployé de manière indépendante. La plateforme se charge de déployer la solution métier complète sous la forme d'une orchestration à plusieurs niveaux de conteneurs Docker sur tous les dispositifs, de façon fluide et sécurisée.

## Prérequis

* Red Hat OpenShift Container Platform 4.2
* IBM Multicloud Management core 1.2
* Si vous hébergez vos propres bases de données, prévoyez deux instances de PostgreSQL et une instance de MongoDB pour stocker les données des composants IBM Edge Computing Manager for Devices. Pour plus de renseignements, consultez la section **Stockage** ci-après.
* Hôte Ubuntu Linux ou macOS sur lequel exécuter l'installation. Les logiciels suivants doivent être installés sur l'hôte :
  * [Interface de ligne de commande Kubernetes (kubectl)](https://kubernetes.io/docs/tasks/tools/install-kubectl/) version 1.14.0 ou ultérieure
  * [Interface de ligne de commande IBM Cloud Pak (cloudctl)](https://www.ibm.com/support/knowledgecenter/SSFC4F_1.2.0/cloudctl/icp_cli.html)
  * [Interface de ligne de commande OpenShift (oc)](https://docs.openshift.com/container-platform/4.2/cli_reference/openshift_cli/getting-started-cli.html)
  * [Interface de ligne de commande Helm](https://helm.sh/docs/using_helm/#installing-the-helm-client) version 2.9.1 ou ultérieure
  * Autres packages logiciels :
    * jq
    * git
    * docker (version 18.06.01 ou ultérieure)
    * make

## Conditions requises pour Red Hat OpenShift SecurityContextConstraints

Le nom `SecurityContextConstraints` par défaut : [`restricted`](https://ibm.biz/cpkspec-scc) a été vérifié pour cette charte. Cette édition est limitée au déploiement dans l'espace de nom `kube-system` et utilise le compte de service `default` en plus de créer ses propres comptes de service pour les sous-chartes de la base de données locale en option.

## Détails de la charte

La présente charte Helm installe et configure les conteneurs certifiés IBM Edge Computing Manager for Devices dans un environnement OpenShift. Les composants suivants seront installés :

* IBM Edge Computing Manager for Devices - Exchange
* IBM Edge Computing Manager for Devices - AgBots
* IBM Edge Computing Manager for Devices - Service de synchronisation Cloud (partie du système de gestion des modèles)
* IBM Edge Computing Manager for Devices - Interface utilisateur (console de gestion)

## Ressources requises

Pour plus d'informations sur les ressources requises, voir [Installation - Dimensionnement](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.0/devices/installing/install.html#size).

## Besoins en stockage et en bases de données

Trois instances de bases de données sont nécessaires au stockage des données des composants IBM Edge Computing Manager for Devices.

Par défaut, la charte installe trois bases de données persistantes dont les dimensions sont indiquées ci-dessous, en utilisant une classe de stockage dynamique Kubernetes définie par défaut (ou configurée par l'utilisateur).

**Remarque** : Ces bases de données par défaut ne sont pas destinées à une utilisation en production. Pour utiliser vos propres bases de données gérées, consultez les exigences ci-dessous et suivez les instructions de la section **Configuration des bases de données distantes**.

* PostgreSQL : Stocke les données Exchange et AgBot
  * Deux instances distinctes sont nécessaires, chacune disposant au moins de 10 Go de stockage
  * L'instance doit prendre en charge au moins 100 connexions
  * En cas de production, ces instances doivent être hautement disponibles
* MongoDB : Stocke les données du service de synchronisation Cloud
  * Une instance avec au moins 50 Go de stockage est nécessaire. **Remarque** : La taille requise dépend de taille et du nombre de modèles de service de périphérie et de fichiers que vous stockez et que vous utilisez.
  * En cas de production, cette instance doit être hautement disponible

**Remarque** : Vous êtes responsable des procédures de sauvegarde/restauration si vous utilisez vos propres bases de données gérées.
Consultez la section **Sauvegarde et récupération** pour connaître les procédures de la base de données par défaut.

## Surveillance des ressources

Une fois IBM Edge Computing Manager for Devices installé, il configure automatiquement la surveillance du produit et des pods sur lesquels il s'exécute. Les données de surveillance peuvent être consultées dans le tableau de bord Grafana de la console de gestion aux adresses suivantes :

* `https://<MANAGEMENT_URL:PORT>/grafana/d/kube-system-edge-computing-overview/edge-computing-overview`
* `https://<MANAGEMENT_URL:PORT>/grafana/d/kube-system-edge-computing-pod-overview/edge-computing-pod-overview`

## Configuration

#### Configuration des bases de données distantes

1. Pour utiliser vos propres bases de données gérées, recherchez le paramètre de configuration Helm suivant dans le fichier `values.yaml` et remplacez sa valeur par `false` :

```yaml
localDBs:
  enabled: true
```

2. Créez un fichier (par exemple, `dbinfo.yaml`) commençant par le contenu suivant :

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: edge-computing-remote-dbs
  labels:
    release: edge-computing
type: Opaque
stringData:
  # agbot postgresql connection settings
  agbot-db-host: "Single hostname of the remote database"
  agbot-db-port: "Single port the database runs on"
  agbot-db-name: "The name of the database to utilize on the postgresql instance"
  agbot-db-user: "Username used to connect"
  agbot-db-pass: "Password used to connect"
  agbot-db-ssl: "SSL Options: <disable|require|verify-full>"

  # exchange postgresql connection settings
  exchange-db-host: "Single hostname of the remote database"
  exchange-db-port: "Single port the database runs on"
  exchange-db-name: "The name of the database to utilize on the postgresql instance"
  exchange-db-user: "Username used to connect"
  exchange-db-pass: "Password used to connect"
  exchange-db-ssl: "SSL Options: <disable|require|verify-full>"

  # css mongodb connection settings
  css-db-host: "Comma separate <hostname>:<port>,<hostname2>:<port2>"
  css-db-name: "The name of the database to utilize on the mongodb instance"
  css-db-user: "Username used to connect"
  css-db-pass: "Password used to connect"
  css-db-auth: "The name of the database used to store user credentials"
  css-db-ssl: "SSL Options: <true|false>"

  trusted-certs: |-
    -----BEGIN CERTIFICATE-----
    ....
    -----END CERTIFICATE-----
    -----BEGIN CERTIFICATE-----
    ....
    -----END CERTIFICATE-----
```

3. Modifiez le fichier `dbinfo.yaml` afin d'indiquer les informations d'accès aux bases de données que vous avez mises à disposition. Renseignez toutes les informations entre guillemets doubles. Lorsque vous ajoutez les certificats de confiance, vérifiez que chaque ligne débute par quatre espaces afin de faciliter la lecture du fichier yaml. Si plusieurs bases de données utilisent le même certificat, celui-ci n'a **pas** besoin d'être répété dans le fichier `dbinfo.yaml`. Sauvegardez le fichier et exécutez la commande :

```bash
oc --namespace kube-system apply -f dbinfo.yaml
```


#### Configuration avancée

Pour modifier l'un des paramètres de configuration Helm par défaut, examinez les paramètres et leur description en exécutant la commande `grep` ci-dessous, puis affichez/modifiez les valeurs correspondantes dans le fichier `values.yaml`:

```bash
grep -v -E '(^ *#|__metadata)' ibm_cloud_pak/values-metadata.yaml
vi values.yaml   # or use your preferred editor
```

## Installation de la charte

**Remarques :**

* Cette installation ne peut être effectuée que par le biais de l'interface de ligne de commande, et non de l'interface graphique utilisateur.

* Vous devez déjà avoir effectué les étapes de la page [Installation de l'infrastructure d'IBM Edge Computing Manager for Devices infrastructure - Processus d'installation](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.0/devices/installing/install.html#process)
* Vous ne pouvez avoir qu'une seule instance d'IBM Edge Computing Manager for Devices installée par cluster, et celle-ci ne peut être installée que l'espace de nom `kube-system`.
* La mise à niveau à partir d'IBM Edge Computing Manager for Devices 3.2 n'est pas prise en charge

Exécutez le script d'installation fourni avec IBM Edge Computing Manager for Devices. Les grandes étapes suivies par le script sont les suivantes : installation de la charte Helm et configuration de l'environnement à l'issue de l'installation (création de l'agbot, de l'organisation et des patterns/règles).

```bash
ibm_cloud_pak/pak_extensions/full-install/install-edge-computing.sh
```

**Remarque** : Selon la vitesse de votre réseau, le téléchargement des images, le passage des pods à l'état RUNNING et la mise en route de tous les services peut prendre plusieurs minutes.

### Vérification de la charte

* Le script ci-dessus vérifie que les pods sont en cours d'exécution et que l'abgbot et le réseau Exchange répondent. Recherchez le message "RUNNING" et "PASSED" vers la fin de l'installation.
* Si le message "FAILED" s'affiche, la sortie vous invite à consulter des journaux spécifiques pour en savoir plus.
* Si le message "PASSED" s'affiche, la sortie affiche le détail des tests qui ont été exécutés, ainsi que deux éléments supplémentaires à vérifier.
  * Accédez à la console de l'interface utilisateur d'IBM Edge Computing Manager à l'URL donnée à la fin du journal.
    * `https://<MANAGEMENT_URL:PORT>/edge`

## Post-installation

Suivez les instructions de la page [Configuration après l'installation](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.0/devices/installing/install.html#postconfig).

## Désinstallation de la charte

**Remarque** : Si vous désinstallez la charte alors que des bases de données locales sont configurées, **toutes les données sont supprimées**. Pour conserver ces données, consultez la section **Procédure de sauvegarde** ci-après.

Revenez à l'emplacement de ce fichier README.md et exécutez le script de désinstallation fourni pour automatiser les tâches correspondantes. Les grandes étapes du script concernent la désinstallation des chartes Helm et le retrait des secrets. Tout d'abord, connectez-vous au cluster en tant qu'administrateur de cluster via `cloudctl`. Exécutez ensuite la commande ci-dessous :

```bash
ibm_cloud_pak/pak_extensions/uninstall/uninstall-edge-computing.sh <cluster-name>
```

**Remarque** : Si vous utilisez des bases de données distantes, le secret d'authentification est supprimé, mais aucune tâche n'est exécutée pour supprimer les données de ces bases de données distantes. Si vous souhaitez supprimer ces données, faites-le maintenant.

## Accès basé sur les rôles

* Vous devez disposer d'un droit d'accès administrateur dans l'espace de nom `kube-system` pour pouvoir installer et gérer ce produit.
* Authentification et rôles liés à Exchange :
  * L'authentification de tous les administrateurs et utilisateurs Exchange est réalisée par IAM via des clés d'API générées à l'aide de la commande `cloudctl`.
  * Les administrateurs Exchange doivent recevoir le privilège `admin` dans Exchange. Celui-ci leur permet de gérer tous les utilisateurs, noeuds, services, patterns et règles présents dans leur organisation Exchange.
  * Les utilisateurs Exchange qui ne disposent pas du privilège administrateur peuvent seulement gérer les utilisateurs, les noeuds, les services, les patterns et les règles qu'ils ont créés.

## Sécurité

* Le protocole TLS est utilisé pour toutes les données qui entrent/sortent du cluster OpenShift via ingress. Dans cette édition, TLS n'est pas utilisé **dans** le cluster OpenShift pour les communications entre les noeuds. Si vous le souhaitez, vous pouvez configurer le maillage de service Red Hat OpenShift pour les communications entre les microservices. Voir [Understanding Red Hat OpenShift Service Mesh](https://docs.openshift.com/container-platform/4.2/service_mesh/service_mesh_arch/understanding-ossm.html#understanding-ossm).
* La charte ne chiffre pas les données au repos.  Il incombe à l'administrateur de configurer le chiffrement du stockage.

## Sauvegarde et récupération

### Procédure de sauvegarde

Exécutez les commandes ci-dessous après vous être connecté à votre cluster depuis un emplacement qui dispose de suffisamment d'espace pour stocker les sauvegardes.


1. Créez un répertoire pour stocker les sauvegardes ci-dessous, et ajustez-le selon vos besoins :

```bash
export BACKUP_DIR=/tmp/edge-computing-backup/$(date +%Y%m%d_%H%M%S)
mkdir -p $BACKUP_DIR
```

2. Exécutez la commande suivantes pour sauvegarder les données d'authentification/secrets

```bash
oc -n kube-system get secret edge-computing -o yaml > $BACKUP_DIR/edge-computing-secret.yaml && \
oc -n kube-system get secret edge-computing-agbotdb-postgresql-auth-secret -o yaml > $BACKUP_DIR/edge-computing-agbotdb-postgresql-auth-secret-backup.yaml && \
oc -n kube-system get secret edge-computing-exchangedb-postgresql-auth-secret -o yaml > $BACKUP_DIR/edge-computing-exchangedb-postgresql-auth-secret-backup.yaml && \
oc -n kube-system get secret edge-computing-css-db-ibm-mongodb-auth-secret -o yaml > $BACKUP_DIR/edge-computing-css-db-ibm-mongodb-auth-secret-backup.yaml
```

3. Exécutez la commande suivante pour sauvegarder le contenu de la base de données :

```bash
oc -n kube-system exec edge-computing-exchangedb-keeper-0 -- bash -c "export PGPASSWORD=$(oc -n kube-system get secret edge-computing -o jsonpath="{.data.exchange-db-pass}" | base64 --decode) && pg_dump -U admin -h edge-computing-exchangedb-proxy-svc -F t postgres > /stolon-data/exchange-backup.tar" && \
oc -n kube-system cp edge-computing-exchangedb-keeper-0:/stolon-data/exchange-backup.tar $BACKUP_DIR/exchange-backup.tar
```

```bash
oc -n kube-system exec edge-computing-agbotdb-keeper-0 -- bash -c "export PGPASSWORD=$(oc -n kube-system get secret edge-computing -o jsonpath="{.data.agbot-db-pass}" | base64 --decode) && pg_dump -U admin -h edge-computing-agbotdb-proxy-svc -F t postgres > /stolon-data/agbot-backup.tar" && \
oc -n kube-system cp edge-computing-agbotdb-keeper-0:/stolon-data/agbot-backup.tar $BACKUP_DIR/agbot-backup.tar
```

```bash
oc -n kube-system exec edge-computing-cssdb-server-0 -- bash -c "mkdir -p /data/db/backup; mongodump -u admin -p $(oc -n kube-system get secret edge-computing -o jsonpath="{.data.css-db-pass}" | base64 --decode) --out /data/db/css-backup" && \
oc -n kube-system cp edge-computing-cssdb-server-0:/data/db/css-backup $BACKUP_DIR/css-backup
```

4. Une fois les sauvegardes vérifiées, retirez les sauvegardes des conteneurs sans état :

```bash
oc -n kube-system exec edge-computing-exchangedb-keeper-0 -- bash -c "rm -f /stolon-data/exchange-backup.tar"
```

```bash
oc -n kube-system exec edge-computing-agbotdb-keeper-0 -- bash -c "rm -f /stolon-data/agbot-backup.tar"
```

```bash
oc -n kube-system exec edge-computing-cssdb-server-0 -- bash -c "rm -rf /data/db/css-backup"
```

### Procédure de restauration

**Remarque** : Si vous effectuez la restauration sur un nouveau cluster, ce dernier doit porter le même nom que celui sur lequel les sauvegardes ont été exécutées.

1. Supprimez tous les secrets préexistants de votre cluster
```bash
oc -n kube-system delete secret edge-computing edge-computing-agbotdb-postgresql-auth-secret edge-computing-exchangedb-postgresql-auth-secret edge-computing-css-db-ibm-mongodb-auth-secret;
```

2. Exportez ces valeurs vers votre machine locale

```bash
export BACKUP_DIR=/tmp/edge-computing-backup/<Insert desired backup datestamp YYYYMMDD_HHMMSS>
```

3. Exécutez la commande suivante pour restaurer les données d'authentification/secrets

```bash
oc apply -f $BACKUP_DIR
```

4. Avant de poursuivre, réinstallez IBM Edge Computing Manager en suivant les instructions de la section **Installation de la charte**.

5. Exécutez les commandes ci-dessous pour copier les sauvegardes dans les conteneurs et pour les restaurer

```bash
oc -n kube-system cp $BACKUP_DIR/exchange-backup.tar edge-computing-exchangedb-keeper-0:/stolon-data/exchange-backup.tar && \
oc exec -n kube-system edge-computing-exchangedb-keeper-0 -- bash -c "export PGPASSWORD=$(oc get secret edge-computing -o jsonpath="{.data.exchange-db-pass}" | base64 --decode) && pg_restore -U admin -h edge-computing-exchangedb-proxy-svc -d postgres -c /stolon-data/exchange-backup.tar"
```

```bash
oc -n kube-system cp $BACKUP_DIR/agbot-backup.tar edge-computing-agbotdb-keeper-0:/stolon-data/agbot-backup.tar && \
oc exec -n kube-system edge-computing-agbotdb-keeper-0 -- bash -c "export PGPASSWORD=$(oc get secret edge-computing -o jsonpath="{.data.agbot-db-pass}" | base64 --decode) && pg_restore -U admin -h edge-computing-agbotdb-proxy-svc -d postgres -c /stolon-data/agbot-backup.tar"
```

```bash
oc -n kube-system cp $BACKUP_DIR/css-backup edge-computing-cssdb-server-0:/data/db/css-backup && \
oc exec -n kube-system edge-computing-cssdb-server-0 -- bash -c "mongorestore -u admin -p $(oc get secret edge-computing -o jsonpath="{.data.css-db-pass}" | base64 --decode) /data/db/css-backup";
```

6. Exécutez la commande suivante pour actualiser les connexions à la base de données du pod kubernetes
```bash
for POD in $(oc get pods -n kube-system | grep -E '\-agbot\-|\-css\-|\-exchange\-' | awk '{print $1}'); do oc delete pod $POD -n kube-system; done
```

## Limitations

* Limites d'installation : Ce produit ne peut être installé qu'une seule fois, et seulement sur l'espace de nom `kube-system`.
* Cette édition ne comporte pas de privilèges d'accès distincts pour l'administration du produit d'une part et l'utilisation du produit d'autre part.

## Documentation

* Consultez le document d'[installation](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.1/devices/installing/install.html) d'IBM Knowledge Center pour obtenir des instructions et mises à jour supplémentaires.

## Copyright

© Copyright IBM Corporation 2020. Tous droits réservés.
