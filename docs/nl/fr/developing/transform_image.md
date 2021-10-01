---

copyright:
years: 2020
lastupdated: "2020-04-09"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Transformation d'une image en un service de périphérie
{: #transform_image}

Cet exemple vous guide tout au long des étapes de publication d'une image Docker existante en tant que service de périphérie, de création d'un pattern de déploiement associé et d'enregistrement de vos noeuds de périphérie pour exécuter ce pattern.
{:shortdesc}

## Avant de commencer
{: #quickstart_ex_begin}

Effectuez les étapes préalables décrites dans la section [Préparation de la création d'un service de périphérie](service_containers.md). Ainsi, les variables d'environnement ci-dessous doivent être définies, les commandes doivent être installées et les fichiers doivent exister :

```bash
echo "HZN_ORG_ID=$HZN_ORG_ID, HZN_EXCHANGE_USER_AUTH=$HZN_EXCHANGE_USER_AUTH, DOCKER_HUB_ID=$DOCKER_HUB_ID" which git jq ls ~/.hzn/keys/service.private.key ~/.hzn/keys/service.public.pem cat /etc/default/horizon
```
{: codeblock}

## Procédure
{: #quickstart_ex_procedure}

**Remarque** : consultez [Conventions utilisées dans ce document](../getting_started/document_conventions.md) pour plus d'informations sur la syntaxe de commande.

1. Créez un répertoire de projet.

  1. Sur votre hôte de développement, accédez à votre répertoire de projet Docker existant. **Si vous ne possédez pas de projet Docker existant, mais que vous souhaitez continuer à parcourir cet exemple**, utilisez les commandes ci-dessous pour créer un fichier Docker simple à utiliser dans le cadre de cette procédure :

    ```bash
    cat << EndOfContent > Dockerfile     FROM alpine:latest     CMD while :; do echo "Hello, world."; sleep 3; done     EndOfContent
    ```
    {: codeblock}

  2. Créez des métadonnées de service de périphérie pour votre projet :

    ```bash
    hzn dev service new -s myservice -V 1.0.0 -i $DOCKER_HUB_ID/myservice --noImageGen
    ```
    {: codeblock}

    Cette commande crée le fichier **horizon/service.definition.json** qui décrit votre service et le fichier **horizon/pattern.json** qui décrit le pattern de déploiement. Vous pouvez ouvrir ces fichiers et parcourir leur contenu.

2. Générez et testez votre service.

  1. Générez votre image Docker. Le nom de l'image doit correspondre à celui indiqué dans le fichier **horizon/service.definition.json**.

    ```bash
    eval $(hzn util configconv -f horizon/hzn.json)     export ARCH=$(hzn architecture)     sudo docker build -t "${DOCKER_IMAGE_BASE}_$ARCH:$SERVICE_VERSION" .
    unset DOCKER_IMAGE_BASE SERVICE_NAME SERVICE_VERSION
    ```
    {: codeblock}

  2. Exécutez cette image de conteneur de service dans l'environnement d'agent simulé {{site.data.keyword.horizon}} :

    ```bash
    hzn dev service start -S
    ```
    {: codeblock}

  3. Vérifiez que votre conteneur de service est en cours d'exécution :

    ```bash
    sudo docker ps
    ```
    {: codeblock}

  4. Examinez les variables d'environnement qui ont été transmises au conteneur au moment de son démarrage. (Il s'agit des mêmes variables d'environnement que celles transmises par l'agent au conteneur de service.)

    ```bash
    sudo docker inspect $(sudo docker ps -q --filter name=myservice) | jq '.[0].Config.Env'
    ```
    {: codeblock}

  5. Affichez le journal du conteneur de service :

    Sous **{{site.data.keyword.linux_notm}}** :

    ```bash
    sudo tail -f /var/log/syslog | grep myservice[[]
    ```
    {: codeblock}

    Sous **{{site.data.keyword.macOS_notm}}** :

    ```bash
    sudo docker logs -f $(sudo docker ps -q --filter name=myservice)
    ```
    {: codeblock}

  6. Arrêtez le service :

    ```bash
    hzn dev service stop
    ```
    {: codeblock}

3. Publiez votre service dans {{site.data.keyword.edge_notm}}. Maintenant que vous avez vérifié que votre code de service s'exécute correctement dans l'environnement de l'agent simulé, publiez le service dans {{site.data.keyword.horizon_exchange}} afin qu'il soit disponible au déploiement sur vos noeuds de périphérie.

  La commande **publish** ci-dessous utilise le fichier **horizon/service.definition.json** et votre paire de clés pour signer et publier votre service dans {{site.data.keyword.horizon_exchange}}. Elle envoie également votre image vers Docker Hub.

  ```bash
  hzn exchange service publish -f horizon/service.definition.json   hzn exchange service list
  ```
  {: codeblock}

4. Publiez un pattern de déploiement pour le service. Ce pattern de déploiement peut être utilisé par les noeuds de périphérie pour qu'{{site.data.keyword.edge_notm}} déploie le service dessus :

  ```bash
  hzn exchange pattern publish -f horizon/pattern.json     hzn exchange pattern list
  ```
  {: codeblock}

5. Enregistrez votre noeud de périphérie pour exécuter votre pattern de déploiement.

  1. Tout comme vous avez enregistré vos noeuds de périphérie auprès des patterns de déploiement publics de l'organisation **IBM**, enregistrez votre noeud de périphérie auprès du pattern de déploiement de votre propre organisation :

    ```bash
    hzn register -p pattern-myservice-$(hzn architecture) -s myservice --serviceorg $HZN_ORG_ID
    ```
    {: codeblock}

  2. Affichez le service de périphérie du conteneur Docker qui a été démarré à la suite de cela :

    ```bash
    sudo docker ps
    ```
    {: codeblock}

  3. Examinez la sortie du service de périphérie myservice :

    ```bash
    sudo hzn service log -f myservice
    ```
    {: codeblock}

6. Examinez le noeud, le service et le pattern que vous avez créés dans la console {{site.data.keyword.edge_notm}}. Vous pouvez afficher l'adresse URL de la console à l'aide de la commande :

  ```bash
  echo "$(awk -F '=|edge-exchange' '/^HZN_EXCHANGE_URL/ {print $2}' /etc/default/horizon)edge"
  ```
  {: codeblock}

7. Annulez l'enregistrement de votre noeud de périphérie et arrêtez le service **myservice** :

  ```bash
  hzn unregister -f
  ```
  {: codeblock}

## Etape suivante
{: #quickstart_ex_what_next}

* Essayez les autres exemples de services de périphérie de la section [Déploiement de services de périphérie](../using_edge_services/detailed_policy.md).
