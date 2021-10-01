---

copyright:
years: 2020
lastupdated: "2020-10-28"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}


# Exigences relatives au dimensionnement et au système
{: #size}

## Considérations sur le dimensionnement

Le dimensionnement de votre cluster implique de nombreuses considérations. Ce contenu décrit certaines d'entre elles et fournit des conseils optimaux pour vous aider à dimensionner votre cluster.

La principale considération consiste à déterminer les services qui doivent être exécutés sur votre cluster. Ce contenu fournit des conseils de dimensionnement concernant les services suivants uniquement :

* {{site.data.keyword.common_services}}
* Concentrateur de gestion {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}})

(Facultatif) Vous pouvez également installer la [journalisation de cluster {{site.data.keyword.open_shift_cp}}](../admin/accessing_logs.md#ocp_logging).

## Considérations relatives à la base de données {{site.data.keyword.ieam}}

Deux configurations de base de données prises en charge ont une incidence sur le dimensionnement du concentrateur de gestion {{site.data.keyword.ieam}} :

* Les bases de données **locales** sont installées (par défaut) en tant que ressources {{site.data.keyword.open_shift}} sur votre cluster {{site.data.keyword.open_shift}}.
* Les bases de données **distantes** sont des bases de données que vous avez mises à disposition, qui sont situées  sur site, ou qui sont des offres SaaS d'un fournisseur cloud, etc.

### {{site.data.keyword.ieam}} exigences de stockage local

Outre le composant Secure Device Onboarding (SDO) toujours installé, **les bases de données locales** et le gestionnaire de secrets nécessitent un stockage persistant. Ce stockage utilise des classes de stockage dynamique qui sont configurées pour votre {{site.data.keyword.open_shift}}cluster.

Pour plus d'informations, voir les [options de stockage {{site.data.keyword.open_shift}} dynamiques prises en charge et les instructions de configuration](https://docs.openshift.com/container-platform/4.6/storage/understanding-persistent-storage.html).

Vous êtes responsable de l'activation du cryptage au repos au moment de la création du cluster. Il peut souvent être inclus dans le cadre de la création de clusters sur des plateformes de cloud. Pour plus d'informations, voir la [documentation suivante](https://docs.openshift.com/container-platform/4.6/installing/installing-fips.html).

Une considération majeure concernant le type de classe de stockage choisi consiste à déterminer si cette classe de stockage prend en charge **allowVolumeExpansion**. Si c'est le cas, la commande suivante renvoie la valeur **true** :

```
oc get storageclass <desired storage class> -o json | jq .allowVolumeExpansion
```
{: codeblock}

Si la classe de stockage autorise une augmentation du volume, la taille peut être ajustée après l'installation (à condition que l'espace de stockage sous-jacent puisse être attribué). Si la classe de stockage n'autorise pas l'augmentation de volume, vous devez préallouer le stockage correspondant à votre cas d'utilisation. 

Si un espace de stockage supplémentaire est nécessaire après l'installation initiale avec une classe de stockage ne permettant pas l'augmentation de volume, vous devez exécuter une réinstallation en suivant les étapes décrites dans la page [Sauvegarde et récupération.](../admin/backup_recovery.md).

Les allocations peuvent être modifiées avant l'installation du concentrateur de gestion {{site.data.keyword.ieam}} en modifiant les valeurs **Stockage**, comme décrit dans la page [Configuration](configuration.md). Les allocations sont paramétrées sur les valeurs par défaut :

* PostgreSQL Exchange (stocke les données Exchange, la taille variant en fonction de l'utilisation, mais le paramètre de stockage par défaut peut prendre en charge jusqu'à 10 000 nœuds de périphérie).
  * 20 Go
* PostgreSQL AgBot (stocke les données pour AgBot. Le paramètre de stockage par défaut peut prendre en charge jusqu'à la limite annoncée de nœuds de périphérie)
  * 20 Go
* MongoDB Cloud Sync Service (stocke le contenu pour le service Model Management Service (MMS)). En fonction du nombre et de la taille de vos modèles, vous pouvez modifier cette dotation par défaut.
  * 50 Go
* Volume persistant Hashicorp Vault (stocke les secrets utilisés par les services de périphériques)
  * 10 Go (Cette taille de volume n'est pas configurable)
* Volume persistant Secure Device Onboarding (stocke les coupons de propriété du dispositif, les options de configuration du dispositif, et le statut de déploiement de chaque dispositif).
  * 1 Go (cette taille de volume n'est pas configurable)

* **Remarques :**
  * Les volumes {{site.data.keyword.ieam}} sont créés avec le mode d'accès **ReadWriteOnce**.
  * IBM Cloud Platform Common Services a des exigences de stockage supplémentaires pour ses services. Les volumes suivants sont créés dans l'espace de nom **ibm-common-services** lors de l'installation avec les valeurs par défaut d'{{site.data.keyword.ieam}} :
    ```
    NAME                                                                                     STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE     alertmanager-ibm-monitoring-alertmanager-db-alertmanager-ibm-monitoring-alertmanager-0   Bound    pvc-3979805f-8e3b-44d6-a039-cd438a3dbb25   10Gi       RWO            csi-cephfs     20h     mongodbdir-icp-mongodb-0                                                                 Bound    pvc-e21604a7-14e4-4049-824e-a5a9feb472c8   20Gi       RWO            csi-cephfs     20h     mongodbdir-icp-mongodb-1                                                                 Bound    pvc-eaecfa29-5c6a-45c2-9d26-58a393103791   20Gi       RWO            csi-cephfs     20h     mongodbdir-icp-mongodb-2                                                                 Bound    pvc-42282c2b-bde8-4adf-86ad-006d2f07df91   20Gi       RWO            csi-cephfs     19h     prometheus-ibm-monitoring-prometheus-db-prometheus-ibm-monitoring-prometheus-0           Bound    pvc-90237949-6f13-481b-8afa-7d86883b8a4f   10Gi       RWO            csi-cephfs     20h
    ```

    Vous pouvez en savoir plus sur les conditions de stockage et les options de configuration d'IBM Cloud Platform Common Services [ici](https://www.ibm.com/support/knowledgecenter/SSHKN6/installer/3.x.x/custom_resource.html).

### Considérations relatives aux bases de données distantes {{site.data.keyword.ieam}}

L'utilisation de vos propres bases de données **distantes** réduit les besoins de la classe en stockage et du traitement pour cette installation, sauf si elles sont mises à disposition sur le même cluster.

Au minimum, provisionnez les bases de données **distantes** avec les ressources et les paramètres suivants :

* 2vCPU
* 2 Go de RAM
* Les tailles de stockage par défaut mentionnées dans la section précédente
* Pour les bases de données PostgreSQL, 100 **connexions_max** (valeur par défaut généralement)

## Dimensionnement des noeuds worker

Les services qui utilisent les [ressources de calcul Kubernetes](https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container) sont planifiés sur les nœuds de travail disponibles.

### Exigences minimales pour la configuration par défaut {{site.data.keyword.ieam}}
| Nombre de noeuds worker | vCPU par noeud worker | Mémoire par noeud worker (Go) | Stockage de disque local par noeud worker (Go) |
| :---: | :---: | :---: | :---: |
| 3	| 8	| 32	| 100 	|

**Remarque : **certains environnements clients peuvent nécessiter des vCPU supplémentaires par nœud de travail ou des nœuds de travail supplémentaires, de sorte que davantage de capacité CPU puisse être allouée au composant Exchange.


&nbsp;
&nbsp;

Une fois que vous avez déterminé le dimensionnement approprié pour votre cluster, vous pouvez commencer l'[installation](online_installation.md).
