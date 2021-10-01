---

copyright:
years: 2019, 2020
lastupdated: "2020-01-22"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Private Container-Registry verwenden
{: #container_registry}

Wenn das Image eines Edge-Service Assets enthält, die nicht in eine öffentliche Registry aufgenommen werden können, dann können Sie eine private Docker-Container-Registry verwenden, z. B. die {{site.data.keyword.open_shift}}-Image-Registry oder die {{site.data.keyword.ibm_cloud}}-Container-Registry, in der der Zugriff streng kontrolliert wird.
{:shortdesc}

Wenn Sie dies noch nicht getan haben, führen Sie die Schritte im Abschnitt [Edge-Service für Einheiten entwickeln](developing.md) aus, um mindestens einen Beispiel-Edge-Service zu erstellen und bereitzustellen und so sicherzustellen, dass Sie mit dem grundlegenden Prozess vertraut sind.

Auf dieser Seite werden zwei Registrys beschrieben, in denen Sie Edge-Service-Images speichern können:
* [{{site.data.keyword.open_shift}}-Image-Registry verwenden](#ocp_image_registry)
* [{{site.data.keyword.cloud_notm}}-Container-Registry verwenden](#ibm_cloud_container_registry)

Diese dienen auch als Beispiele dafür, wie Sie eine private Image-Registry mit {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) verwenden können.

## {{site.data.keyword.open_shift}}-Image-Registry verwenden
{: #ocp_image_registry}

### Vorbereitende Schritte

* Falls noch nicht geschehen, installieren Sie den [cloudctl-Befehl ![Wird in einer neuen Registerkarte geöffnet](../../images/icons/launch-glyph.svg "Wird in einer neuen Registerkarte geöffnet")](https://www.ibm.com/support/knowledgecenter/SSFC4F_1.3.0/cloudctl/install_cli.html)
* Falls noch nicht geschehen, installieren Sie den [{{site.data.keyword.open_shift}} oc-Befehl ![Wird in einer neuen Registerkarte geöffnet](../../images/icons/launch-glyph.svg "Wird in einer neuen Registerkarte geöffnet")](https://docs.openshift.com/container-platform/4.4/cli_reference/openshift_cli/getting-started-cli.html)
* Unter {{site.data.keyword.macOS_notm}} können Sie den Befehl {{site.data.keyword.open_shift}} **oc** mittels [homebrew ![Wird auf einer neuen Registerkarte geöffnet](../../images/icons/launch-glyph.svg "Wird auf einer neuen Registerkarte geöffnet")](https://docs.brew.sh/Installation) installieren.

    ```bash
    brew install openshift-cli
    ```
    {: codeblock}

### Vorgehensweise

Hinweis: Weitere Informationen zur Befehlssyntax finden Sie im Abschnitt [In diesem Dokument verwendete Konventionen](../../getting_started/document_conventions.md).

1. Vergewissern Sie sich, dass eine Verbindung zum {{site.data.keyword.open_shift}}-Cluster mit Berechtigung als Clusteradministrator besteht. 

   ```bash
   cloudctl login -a <cluster-url> -u <user> -p <password> -n kube-system --skip-ssl-validation
   ```
   {: codeblock}

2. Stellen Sie fest, ob eine Standardroute für die {{site.data.keyword.open_shift}}-Image-Registry erstellt wurde, sodass sie von außerhalb des Clusters zugänglich ist:

   ```bash
   oc get route default-route -n openshift-image-registry --template='{{ .spec.host }}'
   ```
   {: codeblock}

   Wenn die Befehlsantwort anzeigt, dass die Standardroute (**default-route**) nicht gefunden wurde, erstellen Sie sie (nähere Einzelheiten siehe [Registry zugänglich machen ![Wird in einer neuen Registerkarte geöffnet](../../images/icons/launch-glyph.svg "Wird in einer neuen Registerkarte geöffnet")](https://docs.openshift.com/container-platform/4.4/registry/securing-exposing-registry.html)):

   ```bash
   oc patch configs.imageregistry.operator.openshift.io/cluster --patch '{"spec":{"defaultRoute":true}}' --type=merge
   ```
   {: codeblock}

3. Rufen Sie den Namen der Repository-Route ab, die Sie verwenden müssen:

   ```bash
   export OCP_DOCKER_HOST=`oc get route default-route -n openshift-image-registry --template='{{ .spec.host }}'`
   ```
   {: codeblock}

4. Erstellen Sie ein neues Projekt, in dem Ihre Images gespeichert werden sollen:

   ```bash
   export OCP_PROJECT=<neues_projekt>
   oc new-project $OCP_PROJECT
   ```
   {: codeblock}

5. Erstellen Sie Servicekonto mit einem Namen Ihrer Wahl:

   ```bash
   export OCP_USER=<servicekontoname>
   oc create serviceaccount $OCP_USER
   ```
   {: codeblock}

6. Fügen Sie zu Ihrem Servicekonto eine Rolle für das aktuelle Projekt hinzu:

   ```bash
   oc policy add-role-to-user edit system:serviceaccount:$OCP_PROJECT:$OCP_USER
   ```
   {: codeblock}

7. Rufen Sie das Token ab, das Ihrem Servicekonto zugeordnet ist:

   ```bash
   export OCP_TOKEN=`oc serviceaccounts get-token $OCP_USER`
   ```
   {: codeblock}

8. Rufen Sie das {{site.data.keyword.open_shift}}-Zertifikat ab und stellen Sie eine Vertrauensbeziehung für Docker her:

   ```bash
   echo | openssl s_client -connect $OCP_DOCKER_HOST:443 -showcerts | sed -n "/-----BEGIN CERTIFICATE-----/,/-----END CERTIFICATE-----/p" > ca.crt
   ```
   {: codeblock}

   Unter {{site.data.keyword.linux_notm}}:
    

   ```bash
   mkdir -p /etc/docker/certs.d/$OCP_DOCKER_HOST
   cp ca.crt /etc/docker/certs.d/$OCP_DOCKER_HOST
   systemctl restart docker.service
   ```
   {: codeblock}

   Unter {{site.data.keyword.macOS_notm}}:
    

   ```bash
   mkdir -p ~/.docker/certs.d/$OCP_DOCKER_HOST
   cp ca.crt ~/.docker/certs.d/$OCP_DOCKER_HOST
   ```
   {: codeblock}

   Unter {{site.data.keyword.macOS_notm}} starten Sie Docker neu, indem Sie auf das Wal-Symbol rechts in der Desktop-Menüleiste klicken und **Neustart** auswählen.

9. Melden Sie sich beim {{site.data.keyword.ocp}} Docker-Host an:

   ```bash
   echo "$OCP_TOKEN" | docker login -u $OCP_USER --password-stdin $OCP_DOCKER_HOST
   ```
   {: codeblock}

10. Erstellen Sie Ihr Image mit diesem Pfadformat, z. B.:

   ```bash
   export BASE_IMAGE_NAME=myservice
   docker build -t $OCP_DOCKER_HOST/$OCP_PROJECT/${BASE_IMAGE_NAME}_amd64:1.2.3 -f ./Dockerfile.amd64 .
   ```
   {: codeblock}

11. Ändern Sie bei der Vorbereitung für die Publizierung Ihres Edge-Service die Datei **service.definition.json** so, dass ihr Abschnitt **deployment** auf Ihren Image-Registry-Pfad verweist. Sie können solche Service- und Musterdefinitionsdateien wie folgt verwenden:

   ```bash
   hzn dev service new -s $BASE_IMAGE_NAME -i $OCP_DOCKER_HOST/$OCP_PROJECT/$BASE_IMAGE_NAME
   ```
   {: codeblock}

   **&lt;base-image-name&gt;** sollte Ihr Basisimagename ohne Architektur oder Version sein. Anschließend können Sie die Variablen in der erstellten Datei **horizon/hzn.json** nach Bedarf bearbeiten.

   Alternativ, wenn Sie eine eigene Servicedefinitionsdatei erstellt haben, stellen Sie sicher, dass das Feld **deployment.services.&lt;service-name&gt;.image** auf Ihren Image-Registry-Pfad verweist.

12. Wenn Ihr Service-Image für die Publizierung bereit ist, übertragen Sie das Image mit Push-Operation an ihre private Container-Registry und publizieren Sie das Image in {{site.data.keyword.horizon}} Exchange:

   ```bash
   hzn exchange service publish -r "$OCP_DOCKER_HOST:$OCP_USER:$OCP_TOKEN" -f horizon/service.definition.json
   ```
   {: codeblock}

   Das Argument **-r "$OCP_DOCKER_HOST:$OCP_USER:$OCP_TOKEN"** gibt {{site.data.keyword.horizon_open}}-Edge-Knoten die notwendigen Berechtigungsnachweise, um das Service-Image mit Pull-Operation zu übertragen.

   Der Befehl führt die folgenden Tasks aus:

   * Übertragen der Docker-Images mit Push-Operation an Ihre {{site.data.keyword.cloud_notm}}-Container-Registry und Abrufen der Digestdaten des Images im Prozess.
   * Signieren der Digest- und Bereitstellungsdaten mit Ihrem privaten Schlüssel.
   * Anordnen der Servicemetadaten (einschließlich Signatur) in {{site.data.keyword.horizon}} Exchange.
   * Anordnen des öffentlichen Schlüssels in {{site.data.keyword.horizon}} Exchange unter der Servicedefinition, sodass {{site.data.keyword.horizon}}-Edge-Knoten automatisch die Definition abrufen können, um Ihre Signaturen bei Bedarf zu verifizieren.
   * Anordnen des OpenShift-Benutzers und des Tokens in {{site.data.keyword.horizon}} Exchange unter der Servicedefinition, sodass {{site.data.keyword.horizon}}-Edge-Knoten bei Bedarf automatisch die Definition abrufen können.
   
### Eigenen Service auf {{site.data.keyword.horizon}}-Edge-Knoten verwenden
{: #using_service}

Damit Ihre Edge-Knoten die erforderlichen Service-Images per Pull-Operation aus dem {{site.data.keyword.ocp}}-Image-Registry übertragen können, müssen Sie Docker auf jedem Edge-Knoten so konfigurieren, dass er dem {{site.data.keyword.open_shift}}-Zertifikat vertraut. Kopieren Sie die Datei **ca.crt** auf jeden Edge-Knoten und gehen Sie anschließend wie folgt vor:

Unter {{site.data.keyword.linux_notm}}:
    

```bash
mkdir -p /etc/docker/certs.d/$OCP_DOCKER_HOST
cp ca.crt /etc/docker/certs.d/$OCP_DOCKER_HOST
systemctl restart docker.service
```
{: codeblock}

Unter {{site.data.keyword.macOS_notm}}:
    

```bash
mkdir -p ~/.docker/certs.d/$OCP_DOCKER_HOST
cp ca.crt ~/.docker/certs.d/$OCP_DOCKER_HOST
```
{: codeblock}

Unter {{site.data.keyword.macOS_notm}} starten Sie Docker neu, indem Sie auf das Wal-Symbol rechts in der Desktop-Menüleiste klicken und **Neustart** auswählen.

Jetzt verfügt {{site.data.keyword.horizon}} über alles Erforderliche, um dieses Edge-Service-Image aus der {{site.data.keyword.open_shift}}-Image-Registry abzurufen und es auf den Edge-Knoten bereitzustellen, wie in dem von Ihnen erstellten Bereitstellungsmuster oder der Richtlinie angegeben.

## {{site.data.keyword.cloud_notm}}-Container-Registry verwenden
{: #ibm_cloud_container_registry}

### Vorbereitende Schritte

* Installieren Sie das [{{site.data.keyword.cloud_notm}}-CLI-Tool (ibmcloud) ![Wird in einer neuen Registerkarte geöffnet](../../images/icons/launch-glyph.svg "Wird in einer neuen Registerkarte geöffnet")](https://cloud.ibm.com/docs/cli?topic=cloud-cli-install-ibmcloud-cli).
* Vergewissern Sie sich, dass Sie über die Zugriffsebene **Clusteradministrator** oder **Teamadministrator** in Ihrem {{site.data.keyword.cloud_notm}}-Konto verfügen.

### Vorgehensweise

1. Melden Sie sich bei {{site.data.keyword.cloud_notm}} an und richten Sie Ihre Organisation als Ziel ein:

   ```bash
   ibmcloud login -a cloud.ibm.com -u <cloud-username> -p <cloud-password
   ibmcloud target -o <organization-id> -s <space-id>
   ```
   {: codeblock}

   Wenn Sie Ihre Organisations-ID und Bereichs-ID nicht kennen, können Sie sich bei der [{{site.data.keyword.cloud_notm}}-Konsole anmelden und sie dort ![Wird in einer neuen Registerkarte geöffnet](../../images/icons/launch-glyph.svg "Wird in einer neuen Registerkarte geöffnet")](https://cloud.ibm.com/) suchen oder erstellen.

2. Erstellen Sie einen Cloud-API-Schlüssel:

   ```bash
   ibmcloud iam api-key-create <key-name> -d "<key-description>"
   ```
   {: codeblock}

   Speichern Sie den API-Schlüsselwert (angezeigt in der Zeile, die mit **API-Key** beginnt) an einer sicheren Position und legen Sie ihn in dieser Umgebungsvariablen fest:

   ```bash
   export CLOUD_API_KEY=<your-cloud-api-key>
   ```
   {: codeblock}

   Hinweis: Dieser API-Schlüssel unterscheidet sich von dem {{site.data.keyword.open_shift}}-API-Schlüssel, den Sie für die Verwendung mit dem Befehl `hzn` erstellt haben.

3. Rufen Sie das Container-Registry-Plug-in ab und erstellen Sie Ihren privaten Registry-Namensbereich. (Dieser Registry-Namensbereich wird Teil des Pfads, der zum Identifizieren Ihres Docker-Image verwendet wird.)

   ```bash
   ibmcloud plugin install container-registry
   export REGISTRY_NAMESPACE=<your-registry-namespace>
   ibmcloud cr namespace-add $REGISTRY_NAMESPACE
   ```
   {: codeblock}

4. Melden Sie sich bei Ihrem Docker-Registry-Namensbereich an:

   ```bash
    ibmcloud cr login
    ```
   {: codeblock}

   Weitere Informationen zur Verwendung des Befehls **ibmcloud cr** finden Sie unter [CLI-Webdokumentation zu 'ibmcloud cr' ![Wird in einer neuen Registerkarte geöffnet](../../images/icons/launch-glyph.svg "Wird in einer neuen Registerkarte geöffnet")](https://cloud.ibm.com/docs/services/Registry/). Darüber hinaus können Sie diesen Befehl ausführen, um Hilfeinformationen anzuzeigen:

   ```bash
ibmcloud cr --help
    ```
   {: codeblock}

   Nachdem Sie sich bei Ihrem privaten Namensbereich in der {{site.data.keyword.cloud_registry}} angemeldet haben, müssen Sie `docker login` nicht verwenden, um sich bei der Registry anzumelden. In Ihren Befehlen **docker push** und **docker pull** können Sie Container-Registry-Pfade ähnlich den folgenden verwenden:

   ```bash
   us.icr.io/$REGISTRY_NAMESPACE/<base-image-name>_<arch>:<version>
   ```
   {: codeblock}

5. Erstellen Sie Ihr Image mit diesem Pfadformat, z. B.:

   ```bash
   export BASE_IMAGE_NAME=myservice
   docker build -t us.icr.io/$REGISTRY_NAMESPACE/${BASE_IMAGE_NAME}_amd64:1.2.3 -f ./Dockerfile.amd64 .
   ```
   {: codeblock}

6. Ändern Sie bei der Vorbereitung für die Publizierung Ihres Edge-Service die Datei **service.definition.json** so, dass ihr Abschnitt **deployment** auf Ihren Image-Registry-Pfad verweist. Sie können solche Service- und Musterdefinitionsdateien wie folgt verwenden:

   ```bash
   hzn dev service new -s $BASE_IMAGE_NAME -i us.icr.io/$REGISTRY_NAMESPACE/$BASE_IMAGE_NAME
   ```
   {: codeblock}

   **&lt;base-image-name&gt;** sollte Ihr Basisimagename ohne Architektur oder Version sein. Anschließend können Sie die Variablen in der erstellten Datei **horizon/hzn.json** nach Bedarf bearbeiten.

   Alternativ, wenn Sie eine eigene Servicedefinitionsdatei erstellt haben, stellen Sie sicher, dass das Feld **deployment.services.&lt;service-name&gt;.image** auf Ihren Image-Registry-Pfad verweist.

7. Wenn Ihr Service-Image für die Publizierung bereit ist, übertragen Sie das Image mit Push-Operation an ihre private Container-Registry und publizieren Sie das Image in {{site.data.keyword.horizon}} Exchange:

   ```bash
   hzn exchange service publish -r "us.icr.io:iamapikey:$CLOUD_API_KEY" -f horizon/service.definition.json
   ```
   {: codeblock}

   Das Argument **-r "us.icr.io:iamapikey:$CLOUD_API_KEY"** gibt {{site.data.keyword.horizon_open}}-Edge-Knoten die notwendigen Berechtigungsnachweise, um das Service-Image mit Pull-Operation zu übertragen.

   Der Befehl führt die folgenden Tasks aus:

   * Übertragen der Docker-Images mit Push-Operation an Ihre {{site.data.keyword.cloud_notm}}-Container-Registry und Abrufen der Digestdaten des Images im Prozess.
   * Signieren der Digest- und Bereitstellungsdaten mit Ihrem privaten Schlüssel.
   * Anordnen der Servicemetadaten (einschließlich Signatur) in {{site.data.keyword.horizon}} Exchange.
   * Anordnen des öffentlichen Schlüssels in {{site.data.keyword.horizon}} Exchange unter der Servicedefinition, sodass {{site.data.keyword.horizon}}-Edge-Knoten automatisch die Definition abrufen können, um Ihre Signaturen bei Bedarf zu verifizieren.
   * Anordnen des {{site.data.keyword.cloud_notm}}-API-Schlüssels in {{site.data.keyword.horizon}} Exchange unter der Servicedefinition, sodass {{site.data.keyword.horizon}}-Edge-Knoten bei Bedarf automatisch die Definition abrufen können.

8. Stellen Sie sicher, dass Ihr Service-Image mit Push-Operation in die {{site.data.keyword.cloud_notm}}-Container-Registry verschoben wurde:

   ```bash
   ibmcloud cr images
   ```
   {: codeblock}

9. Publizieren Sie ein Bereitstellungsmuster oder eine Bereitstellungsrichtlinie, das bzw. die Ihren Service auf einigen Edge-Knoten bereitstellen wird. Beispiel:

   ```bash
   hzn exchange pattern publish -f horizon/pattern.json
   ```
   {: codeblock}

Jetzt verfügt {{site.data.keyword.horizon}} über alles Erforderliche, um dieses Edge-Service-Image aus der {{site.data.keyword.cloud_notm}}-Container-Registry abzurufen und es auf den Edge-Knoten bereitzustellen, wie in dem von Ihnen erstellten Bereitstellungsmuster oder der Richtlinie angegeben.
