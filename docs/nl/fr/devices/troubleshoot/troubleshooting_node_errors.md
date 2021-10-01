---

copyright:
years: 2019
lastupdated: "2019-09-18"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Dépannage des erreurs de noeud
{: #troubleshooting_node_errors}

{{site.data.keyword.edge_devices_notm}} publie un sous-ensemble des journaux d'événements sur le réseau Exchange, que vous pouvez consulter depuis la {{site.data.keyword.gui}}. Ces erreurs sont associées à des conseils de dépannage.
{:shortdesc}

  - [error_image_load](#eil)
  - [error_in_deployment_configuration](#eidc)
  - [error_start_container](#esc)

## error_image_load
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
    
## error_in_deployment_configuration
{: #eidc}

Cette erreur se produit lorsque les configurations de déploiement des définitions de service indiquent une liaison vers un fichier protégé par des droits d'accès root. Pour la résoudre, procédez comme suit :

1. Liez le conteneur à un fichier qui n'est pas protégé par des droits d'accès root.
2. Modifiez les droits d'accès au fichier afin de permettre aux utilisateurs de lire et d'écrire dans le fichier.

## error_start_container
{: #esc}

Cette erreur se produit lorsque Docker rencontre un problème au démarrage du conteneur de service. Le message d'erreur peut contenir des détails indiquant la raison pour laquelle le conteneur n'a pas pu démarrer. Les étapes de résolution dépendent de l'erreur elle-même. Les erreurs suivantes peuvent se produire :

1. Le dispositif utilise déjà un port publié défini par les configurations de déploiement. Pour résoudre l'erreur : 

    - Mappez un port différent vers le port du conteneur de service. Le numéro de port affiché ne doit pas obligatoirement être identique à celui du service.
    - Arrêtez le programme qui utilise le même port.

2. Un port publié spécifié par les configurations de déploiement n'est pas un numéro de port valide. Les numéros de port doivent être compris entre 1 et 65535.
3. Un nom de volume dans les configurations de déploiement n'est pas un chemin d'accès valide. Les chemins de volume doivent être définis par leurs chemins d'accès absolus (et non relatifs). 

## Renseignements supplémentaires

Pour plus d'informations, voir :
  * [Guide de dépannage d'{{site.data.keyword.edge_devices_notm}}](../troubleshoot/troubleshooting.md)
