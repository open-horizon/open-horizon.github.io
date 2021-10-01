---

copyright:
years: 2020
lastupdated: "2020-04-27"

---

{:shortdesc: .shortdesc}
{:new_window: target="_blank"}
{:codeblock: .codeblock}
{:pre: .pre}
{:screen: .screen}
{:tip: .tip}
{:download: .download}

# Kubernetes-Operator entwickeln
{: #kubernetes_operator}

Im Allgemeinen gleicht die Entwicklung eines Service, der in einem Edge-Cluster ausgeführt werden soll, der Entwicklung eines Edge-Service, der auf einer Edge-Einheit ausgeführt wird. Der Edge-Service wird auf Basis der [Best Practices für die edge-native Entwicklung](best_practices.md) entwickelt und in einem Container gepackt. Die Unterschiede bestehen bei der Bereitstellung des Edge-Service.

Wenn Sie einen containerisierten Edge-Service in einem Edge-Cluster bereitstellen möchten, muss von einem Entwickler zunächst ein Kubernetes-Operator erstellt werden, der den containerisierten Edge-Service in einem Kubernetes-Cluster bereitstellt. Nachdem der Operator geschrieben und getestet worden ist, erstellt und publiziert der Entwickler den Operator als Service von {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}). Dieser Prozess versetzt einen {{site.data.keyword.ieam}}-Administrator in die Lage, den Operatorservice wie jeden anderen  {{site.data.keyword.ieam}}-Service mit einer Richtlinie oder mit Mustern bereitzustellen. Die Erstellung einer  {{site.data.keyword.ieam}}-Servicedefinition für den Edge-Service ist nicht erforderlich. Sobald der {{site.data.keyword.ieam}}-Administrator den Operatorservice bereitstellt, wird der Edge-Service vom Operator bereitgestellt.

Beim Schreiben eines Kubernetes-Operators gibt es mehrere Möglichkeiten. Zunächst sollten Sie die Informationen unter [Kubernetes-Konzepte - Operatormuster ![Wird auf einer neuen Registerkarte geöffnet](../../images/icons/launch-glyph.svg "Wird auf einer neuen Registerkarte geöffnet")](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/) lesen. Diese Seite ist eine gute Lernressource für Operatoren. Nachdem Sie sich mit den Konzepten von Operatoren vertraut gemacht haben, können Sie mit dem [Operator-Framework ![Wird auf einer neuen Registerkarte geöffnet](../../images/icons/launch-glyph.svg "Wird auf einer neuen Registerkarte geöffnet")](https://github.com/operator-framework/getting-started) einen Operator schreiben. Der Artikel auf dieser verlinkten Seite beschreibt Operatoren genauer und erläutert Schritt für Schritt die Erstellung eines einfachen Operators mithilfe des Software-Development-Kit (SDK) für Operatoren.

## Hinweise zur Entwicklung eines Operators für {{site.data.keyword.ieam}}

Es hat sich bewährt, großzügig Gebrauch von der Statusfunktionalität des Operators zu machen, da {{site.data.keyword.ieam}} jeden denkbaren Status, den der Operator erstellt, im {{site.data.keyword.ieam}}-Management-Hub meldet. Beim Schreiben eines Operators generiert das Operator-Framework für den Operator eine angepasste Ressourcendefinition (Custom Resource Definition, CRD) von Kubernetes. Jede Operator-CRD ist mit einem Statusobjekt ausgestattet, das mit wichtigen Statusinformationen zum Zustand des Operators und zum bereitgestellten Edge-Service gefüllt werden sollte. Dies erfolgt nicht automatisch durch Kubernetes, sondern muss vom Entwickler des Operators in die Implementierung des Operators geschrieben werden. Der {{site.data.keyword.ieam}}-Agent in einem Edge-Cluster erfasst regelmäßig den Operatorstatus und meldet ihn an den Management-Hub.

Soweit gewünscht, kann der Operator die servicespezifischen {{site.data.keyword.ieam}}-Umgebungsvariablen mit jedem von ihm gestarteten Service verknüpfen. Sobald der Operator gestartet wird, erstellt der {{site.data.keyword.ieam}}-Agent eine Kubernetes-Konfigurationszuordnung (Configmap) namens `hzn-env-vars`, die die servicespezifischen Umgebungsvariablen enthält. Der Operator kann diese Konfigurationszuordnung optional mit jeder von ihm erstellten Bereitstellung verknüpfen, wodurch die von ihm gestarteten Services dieselben servicespezifischen Umgebungsvariablen erkennen können. Hierbei handelt es sich um dieselben Umgebungsvariablen, die in Services eingefügt werden, deren Ausführung auf Edge-Einheiten erfolgt. Ausgenommen sind lediglich die ESS*-Umgebungsvariablen, da Model Management System (MMS) noch nicht für Edge-Cluster-Services unterstützt wird.

Auf Wunsch können die von {{site.data.keyword.ieam}} bereitgestellten Operatoren in einem anderen als dem Standardnamensbereich bereitgestellt werden. Hierzu muss der Entwickler des Operators die YAML-Dateien für den Operator so ändern, dass sie auf den Namensbereich verweisen. Es gibt zwei Möglichkeiten, dies zu erreichen:

 * Ändern Sie die Bereitstellungsdefinition des Operators (sie heißt normalerweise **./deploy/operator.yaml**) und geben Sie einen Namensbereich an.

Alternativ:

* Beziehen Sie in die YAML-Definitionsdateien des Operators in eine YAML-Datei mit einer Namensbereichsdefinition ein, beispielsweise im Verzeichnis  **./deploy** des Operatorprojekts.

Hinweis: Wenn ein Operator nicht im Standardnamensbereich bereitgestellt wird, erstellt {{site.data.keyword.ieam}} den Namensbereich, falls er nicht vorhanden ist, und entfernt den Namensbereich, wenn die Bereitstellung des Operators durch {{site.data.keyword.ieam}} zurückgenommen wird.

## Operator für {{site.data.keyword.ieam}} schreiben

Nachdem ein Operator geschrieben und getestet worden ist, muss er für die Bereitstellung durch {{site.data.keyword.ieam}} paketiert werden:

1. Stellen Sie sicher, dass der Operator für die Ausführung als Bereitstellung innerhalb eines Clusters paketiert wird. Dies bedeutet, dass der Operator in einem Container erstellt und mit einer Push-Operation in die Container-Registry übertragen wird, aus der der Container bei der Bereitstellung durch {{site.data.keyword.ieam}} abgerufen wird. In der Regel erreichen Sie dies, indem Sie den Operator mit dem Befehl **operator-sdk build** und anschließend mit dem Befehl **docker push** erstellen. Dieser Vorgang wird unter [Operator-Framework ![Wird auf einer neuen Registerkarte geöffnet](../../images/icons/launch-glyph.svg "Wird auf einer neuen Registerkarte geöffnet")](https://github.com/operator-framework/getting-started#1-run-as-a-deployment-inside-the-cluster) beschrieben.

2. Stellen Sie sicher, dass der/die vom Operator bereitgestellten Service-Container ebenfalls mit einer Push-Operation in die Registry übertragen werden, aus der sie vom Operator bereitgestellt werden.

3. Erstellen Sie ein Archiv, das die YAML-Definitionsdateien des Operators aus dem Operatorprojekt enthält:

   ```bash
    cd <operatorprojekt>/<operatorname>/deploy
    tar -zcvf <archivname>.tar.gz
    ```
   {: codeblock}

4. Erstellen Sie mit den {{site.data.keyword.ieam}}-Serviceerstellungstools eine Servicedefinition für den Operator; führen Sie hierzu beispielsweise die folgenden Schritte aus:

   1. Erstellen Sie ein neues Projekt:

      ```bash
       hzn dev service new -V <a version> -s <a service name> -c cluster
       ```
      {: codeblock}

   2. Bearbeiten Sie die Datei **horizon/service.definition.json** so, dass sie auf das in Schritt 3 erstellte YAML-Archiv für den Operator verweist.

   3. Erstellen Sie einen Signierschlüssel für den Service oder verwenden Sie einen bereits vorhandenen Signierschlüssel.

   4. Veröffentlichen Sie den Service.

      ```
        hzn exchange service publish -k <signierschlüssel> -f ./horizon/service.definition.json
        ```
      {: codeblock}

5. Erstellen Sie eine Bereitstellungsrichtlinie oder ein Muster für die Bereitstellung des Operatorservice in einem Edge-Cluster.
