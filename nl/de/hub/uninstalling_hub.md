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



# Deinstallation durchführen
{: #uninstalling_hub}

**Achtung:** Das Löschen der angepassten Ressource **EamHub** löst unverzüglich das Entfernen der Komponenten aus, von denen der {{site.data.keyword.ieam}}-Management-Hub abhängig ist; dies gilt auch für die Komponenten von IBM Cloud Platform Common Services. Vergewissern Sie sich, dass dies beabsichtigt ist, bevor Sie fortfahren.

Wenn diese Deinstallation ausgeführt wird, um eine Wiederherstellung in einem vorherigen Zustand zu erleichtern, finden Sie auf der Seite [Sicherung und Wiederherstellung](../admin/backup_recovery.md) weiterführende Informationen.

* Melden Sie sich beim Cluster als Clusteradministrator mit **cloudctl** oder **oc login** für den Namensbereich an, in dem der {{site.data.keyword.ieam}}-Operator installiert ist.
* Führen Sie den folgenden Befehl aus, um die angepasste Ressource (Standardname ist **ibm-edge**) zu löschen:
  ```
  oc delete eamhub ibm-edge
  ```
  {: codeblock}
* Stellen Sie vor dem nächsten Schritt sicher, dass alle Pods des {{site.data.keyword.ieam}}-Management-Hubs beendet worden sind und nur die beiden folgenden Operatorpods noch aktiv sind:
  ```
  $ oc get pods   NAME                                           READY   STATUS    RESTARTS   AGE   ibm-common-service-operator-794f868789-gdt2z   1/1     Running   0          20h   ibm-eamhub-operator-7455c95496-nf48z           1/1     Running   0          20h
  ```
* Deinstallieren Sie den Operator für den {{site.data.keyword.ieam}}-Management-Hub mithilfe der OpenShift-Clusterkonsole. Wählen Sie den Namensbereich aus, in dem der {{site.data.keyword.ieam}}-Operator installiert ist, und navigieren Sie zu **Operatoren** > **Installierte Operatoren**, wählen Sie dann das Überlaufmenüsymbol für den **IEAM-Management-Hub** und danach **Operator deinstallieren** aus.
* Befolgen Sie die unter **Alle Services deinstallieren** auf der IBM Cloud Platform Common Services-Seite für die [Deinstallation](https://www.ibm.com/docs/en/cpfs?topic=online-uninstalling-foundational-services) verfügbaren Anweisungen und ersetzen Sie hierbei alle Vorkommen des Namensbereichs **common-service** durch den Namensbereich, in dem der {{site.data.keyword.ieam}}-Operator installiert ist.
