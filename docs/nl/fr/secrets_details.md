---

copyright:
years: 2021
lastupdated: "2021-08-16"

---

{:shortdesc: .shortdesc}
{:new_window: target="_blank"}
{:codeblock: .codeblock}
{:pre: .pre}
{:screen: .screen}
{:tip: .tip}
{:download: .download}

# Développement d'un service à l'aide de secrets
{: #using secrets}

<img src="../images/edge/10_Secrets.svg" style="margin: 3%" alt="Developing a service using secrets"> 

# Détails de Secrets Manager
{: #secrets_details}

Secrets Manager fournit un stockage sécurisé pour les informations sensibles telles que les données d'authentification ou les clés de chiffrement. Ces secrets sont déployés en toute sécurité par {{site.data.keyword.ieam}} afin que seuls les services configurés pour recevoir un secret y aient accès. L' [exemple Hello Secret World](https://github.com/open-horizon/examples/blob/master/edge/services/helloSecretWorld/CreateService.md) fournit un aperçu de la manière d'exploiter des secrets dans un service de périphérie.

{{site.data.keyword.ieam}} prend en charge l'utilisation de [Hashicorp Vault](https://www.vaultproject.io/) en tant que Secrets Manager. Les secrets créés à l'aide de l'interface de ligne de commande hzn sont mappés sur des secrets de coffre à l'aide du moteur [KV V2 Secrets](https://www.vaultproject.io/docs/secrets/kv/kv-v2). Cela signifie que les détails de chaque {{site.data.keyword.ieam}} secret sont composés d'une clé et d'une valeur. Les deux sont stockés dans le cadre des détails du secret, et les deux peuvent être définis sur n'importe quelle valeur de chaîne. Une utilisation courante de cette fonction est de fournir le type de secret sur la clé et les informations sensibles comme valeur. Par exemple, définissez la clé sur "basicauth" et définissez la valeur sur "user:password". Ce faisant, le développeur de services peut interroger le type de secret, ce qui permet au code de service de gérer correctement la valeur.

Les noms des secrets dans Secrets Manager ne sont jamais connus par une implémentation de service. Il n'est pas possible de transmettre des informations du coffre à une implémentation de service à l'aide du nom d'un secret.

Les secrets sont stockés dans le moteur KV V2 Secrets en préfixant le nom secret avec openhorizon et l'organisation de l'utilisateur. Cela garantit que les secrets créés par {{site.data.keyword.ieam}} les utilisateurs sont isolés des autres utilisations du coffre par d'autres intégrations, et garantit le maintien de l'isolement entre plusieurs locataires.

Les noms secrets sont gérés par {{site.data.keyword.ieam}} org admins (ou utilisateurs lors de l'utilisation de secrets privés de l'utilisateur). Les listes de contrôle d'accès au coffre-fort (ACL) contrôlent les secrets qu'un {{site.data.keyword.ieam}} utilisateur est capable de gérer. Ceci est réalisé par le biais d'un plug-in d'authentification Vault qui délègue l'authentification d'utilisateur à {{site.data.keyword.ieam}} l'échange. Lors de l'authentification réussie d'un utilisateur, le plug-in d'authentification dans le coffre-fort créera un ensemble de règles ACL spécifiques à cet utilisateur. Un utilisateur disposant de droits d'administration dans l'échange peut :
- Ajouter, supprimer, lire et répertorier tous les secrets au niveau de l'organisation.
- Ajouter, supprimer, lire et répertorier tous les secrets privés de cet utilisateur.
- Supprimer et lister les secrets privés des autres utilisateurs de l'organisation, mais ne peut as les ajouter ou les lire.

Un utilisateur sans privilèges d'administrateur peut :
- Répertorier tous les secrets de l'organisation, mais ne peut pas les ajouter, les supprimer ou les lire.
- Ajouter, supprimer, lire et répertorier tous les secrets privés de cet utilisateur.

Le {{site.data.keyword.ieam}} bot d'accord a également accès aux secrets afin de pouvoir les déployer sur des nœuds de périphérie. Le bot d'accord gère une connexion renouvelable au coffre et possède des règles ACL spécifiques à ses objectifs. Un bot d'accord peut :
- Lire les secrets de l'organisation et tout secret privé de l'utilisateur dans n'importe quelle organisation, mais il ne peut pas ajouter, supprimer ou lister des secrets.

L'utilisateur de la racine Exchange et les administrateurs du concentrateur Exchange n'ont pas de droits d'accès dans le coffre. Pour plus d'informations sur ces rôles, voir [Contrôle d'accès basé sur les rôles](../user_management/rbac.html) .
