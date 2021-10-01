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

# Utilisation d'un registre de conteneur privé
{: #container_registry}

Si une image de service de périphérie contient des actifs qui n'ont pas lieu d'être dans un registre public, vous pouvez faire appel à un registre de conteneur Docker privé, tel qu'{{site.data.keyword.open_shift}} Image Registry ou {{site.data.keyword.ibm_cloud}} Container Registry, dont les accès sont strictement contrôlés.
{:shortdesc}

Si ce n'est pas déjà fait, suivez les étapes de la section [Développement d'un service de périphérie pour les dispositifs](developing.md) pour créer et déployer au moins un exemple de service de périphérie et vérifier que vous êtes à l'aise avec le processus de base.

Cette page présente deux registres dans lesquels vous pouvez stocker les images de votre service de périphérie :
* [Utilisation du registre d'images d'{{site.data.keyword.open_shift}}](#ocp_image_registry)
* [Utilisation du registre de conteneurs d'{{site.data.keyword.cloud_notm}}](#ibm_cloud_container_registry)

Ils illustrent également la façon dont vous pouvez utiliser un registre d'images privé avec {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}).

## Utilisation du registre d'images d'{{site.data.keyword.open_shift}}
{: #ocp_image_registry}

### Avant de commencer

* Si ce n'est pas déjà fait, installez la [commande cloudctl![S'ouvre dans un nouvel onglet](../../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://www.ibm.com/support/knowledgecenter/SSFC4F_1.3.0/cloudctl/install_cli.html)
* Si ce n'est pas déjà fait, installez la [commande oc d'{{site.data.keyword.open_shift}}![S'ouvre dans un nouvel onglet](../../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://docs.openshift.com/container-platform/4.4/cli_reference/openshift_cli/getting-started-cli.html)
* Dans {{site.data.keyword.macOS_notm}}, vous pouvez installer la commande **oc** d'{{site.data.keyword.open_shift}} à l'aide de [homebrew ![S'ouvre dans un nouvel onglet](../../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://docs.brew.sh/Installation)

    ```bash
    brew install openshift-cli
    ```
    {: codeblock}

### Procédure

Remarque : Pour plus d'informations sur la syntaxe de commande, voir [Conventions de ce guide](../../getting_started/document_conventions.md).

1. Vérifiez que vous êtes connecté à votre cluster {{site.data.keyword.open_shift}} avec les droits d'administrateur du cluster.

   ```bash
   cloudctl login -a <cluster-url> -u <user> -p <password> -n kube-system --skip-ssl-validation
   ```
   {: codeblock}

2. Regardez si une route par défaut a été créée pour le registre d'images d'{{site.data.keyword.open_shift}} de sorte qu'il soit accessible de l'extérieur du cluster :

   ```bash
   oc get route default-route -n openshift-image-registry --template='{{ .spec.host }}'
   ```
   {: codeblock}

   Si la réponse de la commande indique que le paramètre **default-route** est introuvable, créez-le (voir [Exposing the registry ![S'ouvre dans un nouvel onglet](../../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://docs.openshift.com/container-platform/4.4/registry/securing-exposing-registry.html) pour plus de détails) :

   ```bash
   oc patch configs.imageregistry.operator.openshift.io/cluster --patch '{"spec":{"defaultRoute":true}}' --type=merge
   ```
   {: codeblock}

3. Récupérez le nom de la route du référentiel que vous voulez utiliser :

   ```bash
   export OCP_DOCKER_HOST=`oc get route default-route -n openshift-image-registry --template='{{ .spec.host }}'`
   ```
   {: codeblock}

4. Créez un projet dans lequel stocker vos images :

   ```bash
   export OCP_PROJECT=<your-new-project>
   oc new-project $OCP_PROJECT
   ```
   {: codeblock}

5. Créez un compte de service avec le nom de votre choix :

   ```bash
   export OCP_USER=<service-account-name>
   oc create serviceaccount $OCP_USER
   ```
   {: codeblock}

6. Ajoutez un rôle à votre compte de service pour le projet en cours :

   ```bash
   oc policy add-role-to-user edit system:serviceaccount:$OCP_PROJECT:$OCP_USER
   ```
   {: codeblock}

7. Affectez le jeton à votre compte de service :

   ```bash
   export OCP_TOKEN=`oc serviceaccounts get-token $OCP_USER`
   ```
   {: codeblock}

8. Procurez-vous le certificat {{site.data.keyword.open_shift}} et informez Docker de la validité du certificat :

   ```bash
   echo | openssl s_client -connect $OCP_DOCKER_HOST:443 -showcerts | sed -n "/-----BEGIN CERTIFICATE-----/,/-----END CERTIFICATE-----/p" > ca.crt
   ```
   {: codeblock}

   Sous {{site.data.keyword.linux_notm}} :

   ```bash
   mkdir -p /etc/docker/certs.d/$OCP_DOCKER_HOST
   cp ca.crt /etc/docker/certs.d/$OCP_DOCKER_HOST
   systemctl restart docker.service
   ```
   {: codeblock}

   Sous {{site.data.keyword.macOS_notm}} :

   ```bash
   mkdir -p ~/.docker/certs.d/$OCP_DOCKER_HOST
   cp ca.crt ~/.docker/certs.d/$OCP_DOCKER_HOST
   ```
   {: codeblock}

   Sous {{site.data.keyword.macOS_notm}}, redémarrez Docker en cliquant sur l'icône en forme de baleine située sur le côté droit de la barre de menus du bureau et en sélectionnant **Redémarrer**.

9. Connectez-vous à l'hôte Docker d'{{site.data.keyword.ocp}} :

   ```bash
   echo "$OCP_TOKEN" | docker login -u $OCP_USER --password-stdin $OCP_DOCKER_HOST
   ```
   {: codeblock}

10. Générez votre image en suivant ce format de chemin, par exemple :

   ```bash
   export BASE_IMAGE_NAME=myservice
   docker build -t $OCP_DOCKER_HOST/$OCP_PROJECT/${BASE_IMAGE_NAME}_amd64:1.2.3 -f ./Dockerfile.amd64 .
   ```
   {: codeblock}

11. En vue de la publication de votre service de périphérie, modifiez votre fichier **service.definition.json** de sorte que sa section **Déploiement** référence le chemin d'accès à votre registre d'images. Vous pouvez créer des fichiers de définition de service et de pattern, comme suit :

   ```bash
   hzn dev service new -s $BASE_IMAGE_NAME -i $OCP_DOCKER_HOST/$OCP_PROJECT/$BASE_IMAGE_NAME
   ```
   {: codeblock}

   Le paramètre **&lt;base-image-name&gt;** doit correspondre au nom de votre image de base sans la valeur d'architecture ni de version. Vous pouvez modifier les variables dans le fichier que vous avez créé **horizon/hzn.json** si nécessaire.

   Ou, si vous avez créé votre propre fichier de définition de service, assurez-vous que la zone **deployment.services.&lt;service-name&gt;.image** référence le chemin d'accès à votre registre d'images.

12. Lorsque votre image de service est prête à être publiée, envoyez-la vers votre registre de conteneurs privé et publiez l'image dans {{site.data.keyword.horizon}} Exchange :

   ```bash
   hzn exchange service publish -r "$OCP_DOCKER_HOST:$OCP_USER:$OCP_TOKEN" -f horizon/service.definition.json
   ```
   {: codeblock}

   L'argument **-r "$OCP_DOCKER_HOST:$OCP_USER:$OCP_TOKEN"** fournit les données d'identification aux noeuds de périphérie {{site.data.keyword.horizon_open}} pour pouvoir extraire l'image du service.

   La commande effectue les tâches ci-dessous :

   * Envoie les images Docker vers votre registre de conteneur {{site.data.keyword.cloud_notm}} et récupère le digest de l'image dans le processus.
   * Signe le digest et les informations de déploiement avec votre clé privée.
   * Place les métadonnées du service (y compris la signature) dans {{site.data.keyword.horizon}} Exchange.
   * Place votre clé publique dans {{site.data.keyword.horizon}} Exchange sous la définition de service pour que les noeuds de périphérie {{site.data.keyword.horizon}} puissent automatiquement extraire la définition pour vérifier vos signatures si nécessaire.
   * Place l'utilisateur et le jeton OpenShift dans {{site.data.keyword.horizon}} Exchange sous la définition de service afin que les noeuds de périphérie {{site.data.keyword.horizon}} puissent automatiquement extraire la définition, le cas échéant.
   
### Utilisation de votre service sur des noeuds de périphérie {{site.data.keyword.horizon}}
{: #using_service}

Pour permettre à vos noeuds de périphérie d'extraire les images de service nécessaires à partir du registre d'images {{site.data.keyword.ocp}}, vous devez configurer Docker sur chaque noeud de périphérie de sorte qu'il fasse confiance au certificat {{site.data.keyword.open_shift}}. Copiez le fichier **ca.crt** sur chaque noeud de périphérie, puis :

Sous {{site.data.keyword.linux_notm}} :

```bash
mkdir -p /etc/docker/certs.d/$OCP_DOCKER_HOST
cp ca.crt /etc/docker/certs.d/$OCP_DOCKER_HOST
systemctl restart docker.service
```
{: codeblock}

Sous {{site.data.keyword.macOS_notm}} :

```bash
mkdir -p ~/.docker/certs.d/$OCP_DOCKER_HOST
cp ca.crt ~/.docker/certs.d/$OCP_DOCKER_HOST
```
{: codeblock}

Sous {{site.data.keyword.macOS_notm}}, redémarrez Docker en cliquant sur l'icône en forme de baleine située sur le côté droit de la barre de menus du bureau, puis en sélectionnant **Redémarrer**.

{{site.data.keyword.horizon}} dispose maintenant de tous les éléments requis pour extraire cette image de service de périphérie à partir du registre d'images d'{{site.data.keyword.open_shift}} et pour la déployer sur les noeuds de périphérie, tel que spécifié par le pattern ou la règle de déploiement que vous avez créé(e).

## Utilisation du registre de conteneurs d'{{site.data.keyword.cloud_notm}}
{: #ibm_cloud_container_registry}

### Avant de commencer

* Installez [l'outil d'interface de ligne de commande (ibmcloud) {{site.data.keyword.cloud_notm}}![S'ouvre dans un nouvel onglet](../../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://cloud.ibm.com/docs/cli?topic=cloud-cli-install-ibmcloud-cli).
* Assurez-vous de disposer d'un niveau d'accès de type **administrateur de cluster** ou **administrateur d'équipe** dans votre compte {{site.data.keyword.cloud_notm}}.

### Procédure

1. Connectez-vous à {{site.data.keyword.cloud_notm}} et recherchez votre organisation :

   ```bash
   ibmcloud login -a cloud.ibm.com -u <cloud-username> -p <cloud-password
   ibmcloud target -o <organization-id> -s <space-id>
   ```
   {: codeblock}

   Si vous ne connaissez pas votre ID d'organisation ni votre ID d'espace, connectez-vous à la console [{{site.data.keyword.cloud_notm}} ![S'ouvre dans un nouvel onglet](../../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://cloud.ibm.com/) pour les rechercher ou les créer.

2. Créez une clé d'API Cloud :

   ```bash
   ibmcloud iam api-key-create <key-name> -d "<key-description>"
   ```
   {: codeblock}

   Sauvegardez la valeur de clé d'API (affichée sur la ligne commençant par **Clé d'API**) dans un endroit sûr et définissez dans la variable d'environnement ci-dessous :

   ```bash
   export CLOUD_API_KEY=<your-cloud-api-key>
   ```
   {: codeblock}

   Remarque : Cette clé d'API est différente de la clé d'API d'{{site.data.keyword.open_shift}} que vous avez créée pour pouvoir exécuter la commande `hzn`.

3. Procurez-vous le plug-in container-registry et créez le nom d'espace de votre registre privé. (Ce nom d'espace de registre fera partie du chemin utilisé pour identifier votre image Docker.)

   ```bash
   ibmcloud plugin install container-registry
   export REGISTRY_NAMESPACE=<your-registry-namespace>
   ibmcloud cr namespace-add $REGISTRY_NAMESPACE
   ```
   {: codeblock}

4. Connectez-vous à l'espace de nom de votre registre Docker :

   ```bash
   ibmcloud cr login
   ```
   {: codeblock}

   Pour plus d'informations sur l'utilisation de la commande **ibmcloud cr**, voir la [Documentation Web sur l'interface de ligne de commande ibmcloud cr![S'ouvre dans un nouvel onglet](../../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://cloud.ibm.com/docs/services/Registry/). Vous pouvez également exécuter la commande ci-dessous pour afficher des informations d'aide :

   ```bash
   ibmcloud cr --help
   ```
   {: codeblock}

   Une fois que vous êtes connecté à votre espace de nom privé dans {{site.data.keyword.cloud_registry}}, vous n'avez plus besoin d'utiliser `docker login` pour vous connecter au registre. Vous pouvez utiliser des chemins d'accès au registre de conteneurs similaires à celui qui suit dans vos commandes **docker push** et **docker pull** :

   ```bash
   us.icr.io/$REGISTRY_NAMESPACE/<base-image-name>_<arch>:<version>
   ```
   {: codeblock}

5. Générez votre image en suivant ce format de chemin, par exemple :

   ```bash
   export BASE_IMAGE_NAME=myservice
   docker build -t us.icr.io/$REGISTRY_NAMESPACE/${BASE_IMAGE_NAME}_amd64:1.2.3 -f ./Dockerfile.amd64 .
   ```
   {: codeblock}

6. En vue de la publication de votre service de périphérie, modifiez votre fichier **service.definition.json** de sorte que sa section **Déploiement** référence le chemin d'accès à votre registre d'images. Vous pouvez créer des fichiers de définition de service et de pattern, comme suit :

   ```bash
   hzn dev service new -s $BASE_IMAGE_NAME -i us.icr.io/$REGISTRY_NAMESPACE/$BASE_IMAGE_NAME
   ```
   {: codeblock}

   Le paramètre **&lt;base-image-name&gt;** doit correspondre au nom de votre image de base sans la valeur d'architecture ni de version. Vous pouvez modifier les variables dans le fichier que vous avez créé **horizon/hzn.json** si nécessaire.

   Ou, si vous avez créé votre propre fichier de définition de service, assurez-vous que la zone **deployment.services.&lt;service-name&gt;.image** référence le chemin d'accès à votre registre d'images.

7. Lorsque votre image de service est prête à être publiée, envoyez-la vers votre registre de conteneurs privé et publiez l'image dans {{site.data.keyword.horizon}} Exchange :

   ```bash
   hzn exchange service publish -r "us.icr.io:iamapikey:$CLOUD_API_KEY" -f horizon/service.definition.json
   ```
   {: codeblock}

   L'argument **-r "us.icr.io:iamapikey:$CLOUD_API_KEY"** fournit les données d'identification aux noeuds de périphérie {{site.data.keyword.horizon_open}} pour qu'ils puissent extraire l'image de service.

   La commande effectue les tâches ci-dessous :

   * Envoie les images Docker vers votre registre de conteneur {{site.data.keyword.cloud_notm}} et récupère le digest de l'image dans le processus.
   * Signe le digest et les informations de déploiement avec votre clé privée.
   * Place les métadonnées du service (y compris la signature) dans {{site.data.keyword.horizon}} Exchange.
   * Place votre clé publique dans {{site.data.keyword.horizon}} Exchange sous la définition de service pour que les noeuds de périphérie {{site.data.keyword.horizon}} puissent automatiquement extraire la définition pour vérifier vos signatures si nécessaire.
   * Place votre clé d'API {{site.data.keyword.cloud_notm}} dans {{site.data.keyword.horizon}} Exchange sous la définition de service afin que les noeuds de périphérie {{site.data.keyword.horizon}} puissent automatiquement extraire la définition lorsqu'ils ont en besoin.

8. Vérifiez que votre image de service a été envoyée à {{site.data.keyword.cloud_notm}} Container Registry :

   ```bash
   ibmcloud cr images
   ```
   {: codeblock}

9. Publiez un pattern ou une règle de déploiement qui servira à déployer votre service sur certains noeuds de périphérie. Par exemple :

   ```bash
   hzn exchange pattern publish -f horizon/pattern.json
   ```
   {: codeblock}

{{site.data.keyword.horizon}} dispose maintenant de tout ce dont il a besoin pour récupérer cette image de service de périphérie à partir d'{{site.data.keyword.cloud_notm}} Container Registry et pour la déployer sur les noeuds de périphérie, tel que spécifié dans le pattern ou le règle de déploiement que vous avez créé(e).
