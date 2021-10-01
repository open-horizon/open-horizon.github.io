# IBM&reg; Edge Application Manager

## Introduction

IBM Edge Application Manager fournit une **plateforme de gestion d'applications** de bout en bout pour les applications déployées sur les dispositifs de périphérie types des déploiements IoT. Cette plateforme automatise complètement le processus et libère les développeurs d'applications de la tâche fastidieuse de déploiement des révisions des charges de travail de périphérie sur des milliers de dispositifs de périphérie déployés sur le terrain. Ce changement permet aux développeurs de se concentrer pleinement sur la tâche d'écriture du code d'application dans n'importe quel langage de programmation comme un conteneur Docker pouvant être déployé de manière indépendante. La plateforme se charge de déployer la solution métier complète sous la forme d'une orchestration à plusieurs niveaux de conteneurs Docker sur tous les dispositifs, de façon fluide et sécurisée.

https://www.ibm.com/cloud/edge-application-manager

## Prérequis

Consultez la section [Prérequis](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.1/hub/offline_installation.html#prereq).

## Conditions requises pour Red Hat OpenShift SecurityContextConstraints

Le nom `SecurityContextConstraints` par défaut : [`restricted`](https://ibm.biz/cpkspec-scc) a été vérifié pour cette charte. Cette édition est limitée au déploiement dans l'espace de nom `kube-system` et crée des comptes de service pour la charte principale et des comptes de service additionnels pour les sous-chartes de la base de données locale par défaut.

## Détails de la charte

La présente charte Helm installe et configure les conteneurs certifiés IBM Edge Application Manager dans un environnement OpenShift. Les composants suivants seront installés :

* IBM Edge Application Manager - Exchange
* IBM Edge Application Manager - AgBots
* IBM Edge Application Manager - Cloud Sync Service (partie du système de gestion des modèles)
* IBM Edge Application Manager - Interface utilisateur (console de gestion)

## Ressources requises

Consultez la section [Dimensionnement](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.1/hub/cluster_sizing.html).

## Besoins en stockage et en bases de données

Trois instances de bases de données sont nécessaires au stockage des données des composants IBM Edge Application Manager.

Par défaut, la charte installe trois bases de données persistantes dont les dimensions sont indiquées ci-dessous, en utilisant une classe de stockage dynamique Kubernetes définie par défaut (ou configurée par l'utilisateur). Si vous utilisez une classe de stockage qui ne permet pas d'augmenter le volume, assurez-vous d'autoriser correctement l'extension.

**Remarque** : Ces bases de données par défaut ne sont pas destinées à une utilisation en production. Pour utiliser vos propres bases de données gérées, consultez les exigences ci-dessous et suivez les instructions de la section **Configuration des bases de données distantes**.

* PostgreSQL : Stocke les données Exchange et AgBot
  * Deux instances distinctes sont nécessaires, chacune disposant au moins de 20 Go de stockage
  * L'instance doit prendre en charge au moins 100 connexions
  * En cas de production, ces instances doivent être hautement disponibles
* MongoDB : Stocke les données du service de synchronisation Cloud
  * Une instance avec au moins 50 Go de stockage est nécessaire. **Remarque** : La taille requise dépend de taille et du nombre de modèles de service de périphérie et de fichiers que vous stockez et que vous utilisez.
  * En cas de production, cette instance doit être hautement disponible

**Remarque** : Vous êtes responsable des procédures/fréquences de sauvegarde pour ces bases de données par défaut, ainsi que de celles de vos propres bases de données gérées.
Consultez la section **Sauvegarde et récupération** pour connaître les procédures de la base de données par défaut.

## Surveillance des ressources

Une fois IBM Edge Application Manager installé, il configure automatiquement la surveillance de base des ressources du produit qui s'exécutent dans Kubernetes. Les données de surveillance peuvent être consultées dans le tableau de bord Grafana de la console de gestion à l'adresse suivante :

* `https://<MANAGEMENT_URL:PORT>/grafana/d/kube-system-ibm-edge-overview/ibm-edge-overview`

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
  name: ibm-edge-remote-dbs
  labels:
    release: ibm-edge
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

Pour modifier l'un des paramètres de configuration Helm par défaut, examinez les paramètres et leur description en exécutant la commande `grep` ci-dessous, puis affichez/modifiez les valeurs correspondantes dans le fichier `values.yaml` :

```bash
grep -v -E '(^ *#|__metadata)' ibm_cloud_pak/values-metadata.yaml
vi values.yaml   # or use any editor
```

## Installation de la charte

**Remarques :**

* Cette installation ne peut être effectuée que par le biais de l'interface de ligne de commande, et non de l'interface graphique utilisateur.

* Vous devez déjà avoir effectué les étapes de la page [Installation de l'infrastructure d'IBM Edge Application Manager infrastructure - Processus d'installation](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.1/hub/offline_installation.html#process).
* Vous ne pouvez avoir qu'une seule instance d'IBM Edge Application Manager installée par cluster, et celle-ci ne peut être installée que dans l'espace de nom `kube-system`.
* La mise à niveau vers IBM Edge Application Manager 4.0 n'est pas prise en charge

Exécutez le script d'installation fourni pour installer IBM Edge Application Manager. Les grandes étapes suivies par le script sont les suivantes : installation de la charte Helm et configuration de l'environnement à l'issue de l'installation (création de l'agbot, de l'organisation et des patterns/règles).

```bash
ibm_cloud_pak/pak_extensions/support/ieam-install.sh
```

**Remarque** : Selon la vitesse de votre réseau, le téléchargement des images et le déploiement de toutes les ressources de la charte peuvent prendre plusieurs minutes.

### Vérification de la charte

* Le script ci-dessus vérifie que les pods sont en cours d'exécution et que l'abgbot et le réseau Exchange répondent. Recherchez le message "RUNNING" et "PASSED" vers la fin de l'installation.
* Si le message "FAILED" s'affiche, la sortie vous invite à consulter des journaux spécifiques pour en savoir plus.
* Si le message "PASSED" s'affiche, la sortie affiche le détail des tests qui ont été exécutés, ainsi que l'adresse URL de l'interface utilisateur de gestion.
  * Accédez à la console de l'interface utilisateur d'IBM Edge Application Manager à l'URL indiquée à la fin du journal.
    * `https://<MANAGEMENT_URL:PORT>/edge`

## Post-installation

Suivez les instructions de la page [Configuration après l'installation](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.1/hub/post_install.html).

## Désinstallation de la charte

Suivez les étapes de [désinstallation du concentrateur de gestion](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.1/hub/uninstall.html).

## Accès basé sur les rôles

* Vous devez disposer d'un droit d'accès administrateur dans l'espace de nom `kube-system` pour pouvoir installer et gérer ce produit.
* Les comptes de service, les rôles et les liaisons de rôle sont créés pour cette charte et les sous-chartes en fonction du nom de l'édition.
* Authentification et rôles liés à Exchange :
  * L'authentification de tous les administrateurs et utilisateurs Exchange est réalisée par IAM via des clés d'API générées à l'aide de la commande `cloudctl`.
  * Les administrateurs Exchange doivent recevoir le privilège `admin` dans Exchange. Celui-ci leur permet de gérer tous les utilisateurs, noeuds, services, patterns et règles présents dans leur organisation Exchange.
  * Les utilisateurs Exchange qui ne disposent pas du privilège administrateur peuvent seulement gérer les utilisateurs, les noeuds, les services, les patterns et les règles qu'ils ont créés.

## Sécurité

* Le protocole TLS est utilisé pour toutes les données qui entrent/sortent du cluster OpenShift via ingress. Dans cette édition, TLS n'est pas utilisé **dans** le cluster OpenShift pour les communications entre les noeuds. Si vous le souhaitez, vous pouvez configurer le maillage de service Red Hat OpenShift pour les communications entre les microservices. Voir [Understanding Red Hat OpenShift Service Mesh](https://docs.openshift.com/container-platform/4.4/service_mesh/service_mesh_arch/understanding-ossm.html#understanding-ossm).
* La charte ne chiffre pas les données au repos.  Il incombe à l'administrateur de configurer le stockage lors du chiffrement au repos.

## Sauvegarde et récupération

Suivez les étapes de la page [Sauvegarde et récupération](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.1/admin/backup_recovery.html).

## Limitations

* Limites d'installation : Ce produit ne peut être installé qu'une seule fois, et seulement sur l'espace de nom `kube-system`.

## Documentation

* Consultez la documentation d'[installation](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.1/hub/hub.html) d'IBM Knowledge Center pour obtenir des informations supplémentaires.

## Copyright

© Copyright IBM Corporation 2020. Tous droits réservés.
