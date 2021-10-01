---

copyright:
years: 2021
lastupdated: "2021-07-20"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Présentation de Secrets Manager
{: #overviewofsm}

Les services déployés sur le bord ont souvent besoin d'accéder aux services de cloud, ce qui signifie que le service a besoin de données d'identification pour s'authentifier auprès du service cloud. Le gestionnaire des secrets fournit un mécanisme sécurisé qui permet le stockage, le déploiement et la gestion des données d'identification sans exposer les détails dans les {{site.data.keyword.ieam}} métadonnées (par exemple, définitions de service et règles), ou à d'autres utilisateurs du système qui ne doivent pas avoir accès au secret. Secrets Manager est un composant connectable de {{site.data.keyword.ieam}}. Actuellement, HashiCorp Vault est le seul Secrets Manager pris en charge.

Un secret est un ID utilisateur / mot de passe, un certificat, une clé RSA ou tout autre droit d'accès qui accorde l'accès à une ressource protégée dont une application Edge a besoin pour s'acquitter de sa fonction. Les secrets sont stockés dans le Secrets Manager. Un secret a un nom, qui est utilisé pour identifier le secret, mais qui ne fournit aucune information sur les détails du secret lui-même. Les secrets sont administrés par l' {{site.data.keyword.ieam}} interface de ligne de commande ou par un administrateur, à l'aide de l'interface utilisateur ou de l'interface de ligne de commande de Secrets Manager.

Un développeur de services déclare la nécessité d'un secret dans une {{site.data.keyword.ieam}} définition de service. Le déployeur de service associe (ou lie) un secret de Secrets Manager au déploiement du service, en associant le service à un secret de Secrets Manager. Par exemple, supposons qu'un développeur ait besoin d'accéder au service de cloud XYZ via l'authentification de base. Le développeur met à jour la {{site.data.keyword.ieam}} définition de service pour inclure un secret appelé myCloudServiceCred. Le déployeur de services voit que le service a besoin d'un secret pour le déployer et est au courant d'un secret dans Secrets Manager nommé cloudServiceXYZSecret qui contient les données d'identification de base. Le déployeur de services met à jour la règle de déploiement (ou le modèle) pour indiquer que le secret du service nommé myCloudServiceCreds doit contenir les données d'identification du secret de Secrets Manager nommé cloudServiceXYZSecret. Lorsque le déployeur de services publie la règle de déploiement (ou modèle), {{site.data.keyword.ieam}} déploie en toute sécurité les détails de cloudServiceXYZSecret sur tous les nœuds de périphérie compatibles avec la règle de déploiement (ou modèle).
