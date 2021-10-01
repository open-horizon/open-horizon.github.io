---

copyright:
years: 2020
lastupdated: "2020-10-30"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}



# Désinstallation
{: #uninstalling_hub}

**Avertissement :** La suppression de la ressource personnalisée **EamHub** retire immédiatement les ressources dont dépend le concentrateur de gestion {{site.data.keyword.ieam}}, y compris les composants IBM Cloud Platform Common Services. Assurez-vous que ce résultat est bien celui que vous souhaitez avant de poursuivre.

Voir la page [Sauvegarde et récupération](../admin/backup_recovery.md) si cette désinstallation est effectuée pour restaurer un état précédent.

* Connectez-vous au cluster en tant qu'administrateur de cluster en utilisant **cloudctl** ou **oc login**, dans l'espace de nom dans lequel votre opérateur {{site.data.keyword.ieam}} est installé.
* Exécutez la commande suivante pour supprimer la ressource personnalisée (par défaut **ibm-edge**) :
  ```
  oc delete eamhub ibm-edge
  ```
  {: codeblock}
* Avant de passer à l'étape suivante, assurez-vous que tous les pods du concentrateur de gestion {{site.data.keyword.ieam}} sont arrêtés et que seuls les deux pods d'opérateur présentés ici sont en cours d'exécution :
  ```
  $ oc get pods   NAME                                           READY   STATUS    RESTARTS   AGE   ibm-common-service-operator-794f868789-gdt2z   1/1     Running   0          20h   ibm-eamhub-operator-7455c95496-nf48z           1/1     Running   0          20h
  ```
* Désinstallez l'opérateur du concentrateur de gestion {{site.data.keyword.ieam}} à l'aide de la console de cluster OpenShift. Sélectionnez l'espace de nom dans lequel votre opérateur {{site.data.keyword.ieam}} est installé, puis sélectionnez **Operators** > **Installed Operators** > l'icône du menu déroulant dynamique du **concentrateur de gestion IEAM** > **Uninstall Operator**.
* Suivez les instructions de la section **Désinstallation de tous les services** de la page [Désinstallation](https://www.ibm.com/docs/en/cpfs?topic=online-uninstalling-foundational-services) d'IBM Cloud Platform Common Services, afin de remplacer toutes les occurrences de l'espace de nom **common-service** par l'espace de nom dans lequel votre opérateur {{site.data.keyword.ieam}} est installé.
