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

# Partage de services
{: #multit}

## Locataires dans {{site.data.keyword.edge_notm}}
{: #tenants}

{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) utilise le concept informatique général de partage de services par organisations, où chaque locataire possède sa propre organisation. Les organisations séparent les ressources. Par conséquent, les utilisateurs d'une organisation donnée ne peuvent pas créer ou modifier de ressources dans une autre organisation. En outre, les ressources d'une organisation ne peuvent être consultées que par les utilisateurs de cette organisation, à moins que les ressources ne soient marquées comme étant publiques.

### Scénarios d'utilisation courants

Deux cas d'utilisation d'ordre général sont utilisés pour optimiser la multi-location dans {{site.data.keyword.ieam}} :

* Une entreprise possède plusieurs unités commerciales, chacune étant une organisation distincte dans le même {{site.data.keyword.ieam}} concentrateur de gestion. Examinez les raisons juridiques, commerciales ou techniques pour lesquelles chaque unité commerciale doit être une organisation distincte avec son propre ensemble de ressources {{site.data.keyword.ieam}} qui sont, par défaut, non accessibles aux autres unités commerciales. Même avec des organisations distinctes, l'entreprise a la possibilité d'utiliser un groupe commun d'administrateurs d'organisation pour gérer toutes les organisations.
* Une entreprise héberge {{site.data.keyword.ieam}} en tant que service pour ses clients, et chaque client possède une ou plusieurs organisations dans le concentrateur de gestion. Dans ce cas, les administrateurs de l'organisation sont uniques pour chaque client.

Le cas d'utilisation que vous choisissez détermine la façon dont vous configurez {{site.data.keyword.ieam}} et Identity and Access Manager ([IAM](https://www.ibm.com/support/knowledgecenter/SSHKN6/iam/landing_iam.html)).

### Types d'utilisateurs {{site.data.keyword.ieam}}
{: #user-types}

{{site.data.keyword.ieam}} prend en charge les rôles utilisateur suivants :

| **Rôle** | **Accès** |
|--------------|-----------------|
| **Administrateur de concentrateur** | Gère la liste des organisations {{site.data.keyword.ieam}}en créant, modifiant et supprimant des organisations si nécessaire et en créant des administrateurs d'organisation au sein de chaque organisation. |
| **Administrateur d'organisation** | Gère les ressources dans une ou plusieurs organisations {{site.data.keyword.ieam}}. Les administrateurs d'organisation peuvent créer, afficher ou modifier n'importe quelle ressource (utilisateur, noeud, service, règle ou canevas) au sein de l'organisation, même s'ils ne sont pas le propriétaire de la ressource. |
| **Utilisateur standard** | Crée des noeuds, services, règles et canevas au sein de l'organisation et modifie ou supprime les ressources qu'il a créées. Affiche tous les services, règles et canevas de l'organisation qui ont été créés par d'autres utilisateurs. |
{: caption="Tableau 1. {{site.data.keyword.ieam}} rôles utilisateur" caption-side="top"}

Voir  [Contrôle d'accès à base de rôles](../user_management/rbac.md) pour consulter la description de tous les rôles {{site.data.keyword.ieam}}.

## Relation entre IAM et {{site.data.keyword.ieam}}
{: #iam-to-ieam}

Le service IAM (Identity and Access Manager) gère les utilisateurs pour tous les produits basés sur Cloud Pak, y compris {{site.data.keyword.ieam}}. IAM utilise à son tour LDAP pour stocker les utilisateurs. Chaque utilisateur IAM peut être membre d'une ou plusieurs équipes IAM. Comme chaque équipe IAM est associée à un compte IAM, un utilisateur IAM peut indirectement être membre d'un ou plusieurs comptes IAM. Pour plus de détails, voir [Multi-location IAM](https://www.ibm.com/support/knowledgecenter/SSHKN6/iam/3.x.x/multitenancy/multitenancy.html).

L'échange {{site.data.keyword.ieam}} fournit des services d'authentification et d'autorisation pour les autres composants {{site.data.keyword.ieam}}. Exchange délègue l'authentification des utilisateurs à IAM, ce qui signifie que les informations d'identification des utilisateurs IAM sont transmises à Exchange et demande à IAM de déterminer si elles sont valides. Chaque rôle utilisateur (administrateur de concentrateur, administrateur d'organisation ou utilisateur standard) est défini dans l'échange, ce qui détermine les actions que les utilisateurs sont autorisés à effectuer dans {{site.data.keyword.ieam}}.

Chaque organisation de l'échange {{site.data.keyword.ieam}} est associée à un compte IAM. Par conséquent, les utilisateurs IAM dans un compte IAM font automatiquement partie de l'organisation {{site.data.keyword.ieam}} correspondante. La seule exception à cette règle est que le rôle d'administrateur de concentrateur {{site.data.keyword.ieam}} est considéré comme étant externe à une organisation spécifique, donc peu importe le compte IAM dans lequel se trouve l'utilisateur IAM d'administration de concentrateur.

Pour récapituler le mappage entre IAM et {{site.data.keyword.ieam}} :

| **IAM** | **Relation** | **{{site.data.keyword.ieam}}** |
|--------------|----------|-----------------|
| Compte IAM | correspond à | Organisation {{site.data.keyword.ieam}} |
| Utilisateur IAM | correspond à | Utilisateur {{site.data.keyword.ieam}} |
| Il n'existe pas de contrepartie IAM pour le rôle | Aucun | rôle {{site.data.keyword.ieam}} |
{: caption="Tableau 2. Mappage IAM - {{site.data.keyword.ieam}}" caption-side="top"}

Les données d'identification permettant la connexion à la console {{site.data.keyword.ieam}} sont l'ID utilisateur et le mot de passe IAM. Les données d'identification utilisées pour l'interface de ligne de commande {{site.data.keyword.ieam}} (`hzn`) sont une clé d'API IAM.

## L'organisation initiale
{: #initial-org}

Par défaut, une organisation a été créée lors de l'installation d'{{site.data.keyword.ieam}} sous le nom que vous avez indiqué. Si vous n'avez pas besoin des fonctions de multi-location de {{site.data.keyword.ieam}}, cette organisation initiale suffit pour utiliser {{site.data.keyword.ieam}} et vous pouvez ignorer le reste de cette page.

## Création d'un administrateur de concentrateur
{: #create-hub-admin}

La première étape de l'utilisation de la multi-location {{site.data.keyword.ieam}} consiste à créer un ou plusieurs administrateurs de concentrateur pouvant créer et gérer les organisations. Pour ce faire, vous devez créer ou choisir un compte IAM et un utilisateur auquel le rôle d'administrateur de concentrateur sera affecté.

1. Utilisez `cloudctl` pour vous connecter au concentrateur de gestion {{site.data.keyword.ieam}} en tant qu'administrateur de cluster. (Si vous n'avez pas encore installé `cloudctl`, consultez la rubrique [Installation de cloudctl, kubectl et oc](../cli/cloudctl_oc_cli.md) pour obtenir des instructions.)

   ```bash
   cloudctl login -a <cluster-url> -u admin -p <password> --skip-ssl-validation
   ```
   {: codeblock}

2. Si vous n'avez pas déjà connecté une instance LDAP à IAM, faites-le maintenant en suivant la rubrique [Connexion à votre annuaire LDAP](https://www.ibm.com/support/knowledgecenter/SSHKN6/iam/3.x.x/configure_ldap.html).

3. L'administrateur de concentrateur doit se trouver dans un compte IAM. (N'importe quel compte.) Si vous ne disposez pas déjà d'un compte IAM dont vous souhaitez que l'administrateur de concentrateur fasse partie, créez-en un :

   ```bash
   IAM_ACCOUNT_NAME='hub admin account'   # or choose another name   cloudctl iam account-create "$IAM_ACCOUNT_NAME" -d 'account for the hub admin users' IAM_ACCOUNT_ID=$(cloudctl iam account "$IAM_ACCOUNT_NAME" | grep -E '^ID' | awk '{print $2}')
   IAM_TEAM_ID=$(cloudctl iam teams -s | grep -m 1 "$IAM_ACCOUNT_NAME" | awk '{print $1}')
   ```
   {: codeblock}

4. Créez ou choisissez un utilisateur LDAP qui sera dédié au rôle d'administrateur de concentrateur {{site.data.keyword.ieam}}. N'utilisez pas le même utilisateur comme administrateur de concentrateur {{site.data.keyword.ieam}} et administrateur d'organisation {{site.data.keyword.ieam}} (ou utilisateur standard {{site.data.keyword.ieam}})

5. Importez l'utilisateur dans IAM :

   ```bash
   HUB_ADMIN_USER=<le nom d'utilisateur IAM/LDAP de l'administrateur de concentrateur> cloudctl iam user-import -u $HUB_ADMIN_USER cloudctl iam user-onboard $IAM_ACCOUNT_ID -r PRIMARY_OWNER -u $HUB_ADMIN_USER IAM_RESOURCE_ID=$(cloudctl iam resources | grep ':n/ibm-edge:')
   cloudctl iam resource-add $IAM_TEAM_ID -r $IAM_RESOURCE_ID
   ```
   {: codeblock}

6. Attribuez le rôle d'administrateur de concentrateur à l'utilisateur IAM :

   ```bash
   EXCHANGE_ROOT_PW=<password for the exchange root user>   export HZN_ORG_ID=root   export HZN_EXCHANGE_USER_AUTH=root/root:$EXCHANGE_ROOT_PW   export HZN_EXCHANGE_URL=<the URL of your exchange>   hzn exchange user create -H $HUB_ADMIN_USER ""
   ```
   {: codeblock}

7. Vérifiez que l'utilisateur dispose du rôle d'administrateur de concentrateur. Dans la sortie de la commande suivante, `"hubAdmin": true` doit s'afficher.

   ```bash
   hzn exchange user list $HUB_ADMIN_USER
   ```
   {: codeblock}

### Utilisez l'administrateur de concentrateur à l'aide de l'interface de ligne de commande {{site.data.keyword.ieam}}
{: #verify-hub-admin}

Créez une clé d'API pour l'administrateur de concentrateur et vérifiez qu'elle possède les fonctions d'administration de concentrateur :

1. Utilisez `cloudctl` pour vous connecter au concentrateur de gestion {{site.data.keyword.ieam}} en tant qu'administrateur de concentrateur :

   ```bash
   cloudctl login -a <cluster-url> -u $HUB_ADMIN_USER -p <motdepasse-admin-concentrateur> -c $IAM_ACCOUNT_ID --skip-ssl-validation
   ```
   {: codeblock}

2. Créez une clé d'API pour l'administrateur de concentrateur :

   ```bash
   cloudctl iam api-key-create "${HUB_ADMIN_USER}-api-key" -d "API key for $HUB_ADMIN_USER"
   ```
   {: codeblock}

   Recherchez la valeur de clé d'API sur la ligne de sortie de commande qui commence par **API Key**. Sauvegardez la valeur de clé dans un emplacement sûr pour une utilisation ultérieure car vous ne pouvez pas l'interroger ultérieurement à partir du système. De même, définissez-la dans la variable suivante pour les commandes ultérieures :

   ```bash
   HUB_ADMIN_API_KEY=<clé d'API IAM que vous venez de créer>
   ```
   {: codeblock}

3. Affichez toutes les organisations dans le concentrateur de gestion. Vous devez voir l'organisation initiale créée lors de l'installation, ainsi que les organisations **root** et **IBM** :

   ```bash
   export HZN_ORG_ID=root export HZN_EXCHANGE_USER_AUTH=root/iamapikey:$HUB_ADMIN_API_KEY   hzn exchange org list -o root
   ```
   {: codeblock}

4. Connectez-vous à la [{{site.data.keyword.ieam}} console de gestion](../console/accessing_ui.md) à l'aide de votre ID utilisateur et de votre mot de passe IAM d'administrateur de concentrateur. La console d'administration de l'organisation s'affiche, car vos identifiants de connexion ont le rôle d'administrateur de concentrateur. Utilisez cette console pour afficher, gérer et ajouter des organisations. Ou vous pouvez ajouter des organisations en utilisant la CLI dans la section suivante.

## Création d'une organisation à l'aide de l'interface CLI
{: #create-org}

Vous pouvez créer des organisations à l'aide de l'interface CLI au lieu d'utiliser la console d'administration d'organisation {{site.data.keyword.ieam}}. Une condition préalable à la création d'une organisation consiste à créer ou choisir un compte IAM qui sera associé à l'organisation. Une autre condition préalable consiste à créer ou choisir un utilisateur IAM auquel sera affecté le rôle d'administrateur d'organisation.

**Remarque**: Un nom d'organisation ne peut pas contenir de traits de soulignement (_), de virgules (,), d'espaces blancs (), de guillemets simples (') ou de points d'interrogation (?).

Procédez comme suit :

1. Si vous ne l'avez pas encore fait, créez un administrateur de concentrateur en effectuant les étapes de la section précédente. Vérifiez que la clé d'API d'administration de concentrateur est définie dans la variable suivante :

   ```bash
   HUB_ADMIN_API_KEY=<clé d'API IAM de l'administrateur de concentrateur>
   ```
   {: codeblock}

2. Utilisez `cloudctl` pour vous connecter au concentrateur de gestion {{site.data.keyword.ieam}} en tant qu'administrateur de cluster et créez un compte IAM auquel la nouvelle organisation {{site.data.keyword.ieam}} sera associée. (Si vous n'avez pas encore installé `cloudctl`, consultez la section [Installation de cloudctl, kubectl et oc](../cli/cloudctl_oc_cli.md).)

   ```bash
   cloudctl login -a <url-cluster> -u admin -p <motdepasse> --skip-ssl-validation   NEW_ORG_ID=<nom de la nouvelle organisation>   IAM_ACCOUNT_NAME="$NEW_ORG_ID" cloudctl iam account-create "$IAM_ACCOUNT_NAME" -d "$IAM_ACCOUNT_NAME account"   IAM_ACCOUNT_ID=$(cloudctl iam account "$IAM_ACCOUNT_NAME" | grep -E '^ID' | awk '{print $2}')
   IAM_TEAM_ID=$(cloudctl iam teams -s | grep -m 1 "$IAM_ACCOUNT_NAME" | awk '{print $1}')
   ```
   {: codeblock}

3. Créez ou choisissez un utilisateur LDAP auquel sera affecté le rôle d'administration d'organisation, puis importez-le dans IAM. Vous ne pouvez pas utiliser un administrateur de concentrateur, mais vous pouvez utiliser le même administrateur d'organisation dans plusieurs comptes IAM. Cela leur permet donc de gérer plusieurs  organisations.{{site.data.keyword.ieam}}.

   ```bash
   ORG_ADMIN_USER=<le nom d'utilisateur IAM/LDAP de l'administrateur d'organisation> cloudctl iam user-import -u $ORG_ADMIN_USER cloudctl iam user-onboard $IAM_ACCOUNT_ID -r PRIMARY_OWNER -u $ORG_ADMIN_USER   IAM_RESOURCE_ID=$(cloudctl iam resources | grep ':n/ibm-edge:')
   cloudctl iam resource-add $IAM_TEAM_ID -r $IAM_RESOURCE_ID
   ```
   {: codeblock}

4. Définissez les variables d'environnement suivantes, créez l'organisation {{site.data.keyword.ieam}} et vérifiez qu'elle existe :
   ```bash
   export HZN_ORG_ID=root   export HZN_EXCHANGE_USER_AUTH=root/iamapikey:$HUB_ADMIN_API_KEY   export HZN_EXCHANGE_URL=<URL de votre échange> hzn exchange org create -a IBM/agbot -t "cloud_id=$IAM_ACCOUNT_ID" --description "$NEW_ORG_ID organization" $NEW_ORG_ID hzn exchange agbot addpattern IBM/agbot IBM '*' $NEW_ORG_ID hzn exchange org list $NEW_ORG_ID
   ```
   {: codeblock}

5. Attribuez le rôle d'administrateur d'organisation à l'utilisateur IAM que vous avez précédemment choisi et vérifiez que l'utilisateur a été créé dans l'échange {{site.data.keyword.ieam}} avec le rôle d'administrateur d'organisation :

   ```bash
   hzn exchange user create -o $NEW_ORG_ID -A $ORG_ADMIN_USER "" "<adresse-email>" hzn exchange user list -o $NEW_ORG_ID $ORG_ADMIN_USER
   ```
   {: codeblock}

   La liste de l'utilisateur doit afficher : `"admin": true`

<div class="note"><span class="notetitle">Remarque :</span> Si vous créez plusieurs organisations et que vous souhaitez que le même administrateur d'organisation gère toutes les organisations, utilisez la même valeur pour `ORG_ADMIN_USER` à chaque fois dans cette section.</div>

L'administrateur d'organisation peut désormais utiliser la [{{site.data.keyword.ieam}} console de gestion](../console/accessing_ui.md) pour gérer les ressources {{site.data.keyword.ieam}} au sein de cette organisation.

### Activation de l'administrateur d'organisation pour l'utilisation de l'interface de ligne de commande

Pour qu'un administrateur d'organisation puisse utiliser la commande `hzn exchange` pour gérer les ressources {{site.data.keyword.ieam}} à l'aide de la CLI, l'administrateur doit :

1. Utilisez `cloudctl` pour vous connecter au concentrateur de gestion {{site.data.keyword.ieam}} et créer une clé d'API :

   ```bash
   cloudctl login -a <url-cluster> -u $ORG_ADMIN_USER -p <motdepasse-admin-concentrateur> -c $IAM_ACCOUNT_ID --skip-ssl-validation cloudctl iam api-key-create "${ORG_ADMIN_USER}-api-key" -d "API key for $ORG_ADMIN_USER"
   ```
   {: codeblock}

   Recherchez la valeur de clé d'API sur la ligne de sortie de commande qui commence par **API Key**. Sauvegardez la valeur de clé dans un emplacement sûr pour une utilisation ultérieure car vous ne pouvez pas l'interroger ultérieurement à partir du système. De même, définissez-la dans la variable suivante pour les commandes ultérieures :

   ```bash
   ORG_ADMIN_API_KEY=<clé d'API IAM que vous venez de créer>
   ```
   {: codeblock}

   **Conseil :** si vous ajoutez cet utilisateur à des comptes IAM supplémentaires à l'avenir, vous n'avez pas besoin de créer une clé d'API pour chaque compte. La même clé d'API fonctionne dans tous les comptes IAM dont l'utilisateur fait partie et, par conséquent, dans toutes les organisations {{site.data.keyword.ieam}} dont cet utilisateur fait partie.

2. Vérifiez que la clé d'API fonctionne avec la commande `hzn exchange` :

   ```bash
   export HZN_ORG_ID=<id de l'organisation> export HZN_EXCHANGE_USER_AUTH=root/iamapikey:$ORG_ADMIN_API_KEY   hzn exchange user list
   ```
   {: codeblock}


La nouvelle organisation est prête à être utilisée. Pour définir un nombre maximal de noeuds de périphérie dans cette organisation ou personnaliser les paramètres de signal de présence de noeud de périphérie par défaut, voir [Configuration de l'organisation](#org-config).

## Utilisateurs non administrateurs au sein d'une organisation
{: #org-users}

Un nouvel utilisateur peut être ajouté à une organisation via l'importation et l'intégration de l'utilisateur IAM (en tant que `MEMBRE`) au compte IAM correspondant. Il n'est pas nécessaire d'ajouter explicitement l'utilisateur à Exchange {{site.data.keyword.ieam}}, car cette opération est exécutée automatiquement, si nécessaire.

L'utilisateur peut ensuite utiliser la [{{site.data.keyword.ieam}} console de gestion](../console/accessing_ui.md). Pour que l'utilisateur puisse utiliser l'interface de ligne de commande `hzn exchange`, il doit :

1. Utilisez `cloudctl` pour vous connecter au concentrateur de gestion {{site.data.keyword.ieam}} et créer une clé d'API :

   ```bash
   IAM_USER=<utilisateur iam> cloudctl login -a <cluster-url> -u $IAM_USER -p <motdepasse-admin-concentrateur> -c $IAM_ACCOUNT_ID --skip-ssl-validation cloudctl iam api-key-create "${IAM_USER}-api-key" -d "API key for $IAM_USER"
   ```
   {: codeblock}

   Recherchez la valeur de clé d'API sur la ligne de sortie de commande qui commence par **API Key**. Sauvegardez la valeur de clé dans un emplacement sûr pour une utilisation ultérieure car vous ne pouvez pas l'interroger ultérieurement à partir du système. De même, définissez-la dans la variable suivante pour les commandes ultérieures :

   ```bash
   IAM_USER_API_KEY=< Clé d'API IAM que vous venez de créer >
   ```
   {: codeblock}

3. Définissez les variables d'environnement suivantes et vérifiez l'utilisateur :

```bash
export HZN_ORG_ID=<id-organisation>export HZN_EXCHANGE_USER_AUTH=iamapikey:$IAM_USER_API_KEYhzn exchange user list
```
{: codeblock}

## L'organisation IBM
{: #ibm-org}

L'organisation IBM est une organisation unique qui fournit des services et canevas prédéfinis conçus pour être des exemples de technologie utilisables par n'importe quel utilisateur dans n'importe quelle organisation. L'organisation IBM est automatiquement créée lorsque le {{site.data.keyword.ieam}} concentrateur de gestion est installé.

**Remarque** : bien que les ressources de l'organisation IBM soient publiques, l'organisation IBM n'est pas censée contenir tout le contenu public dans le concentrateur de gestion {{site.data.keyword.ieam}}.

## Configuration de l'organisation
{: #org-config}

Chaque organisation {{site.data.keyword.ieam}} possède les paramètres ci-dessous. Les valeurs par défaut de ces paramètres sont souvent suffisantes. Si vous choisissez de personnaliser l'un des paramètres, exécutez la commande `hzn exchange org update -h` pour afficher les options de commande pouvant être utilisées.

| **Paramètre** | **Description** |
|--------------|-----------------|
| `description` | Description de l'entreprise. |
| `label` | Nom de l'organisation. Cette valeur permet d'afficher le nom de l'organisation dans la console de gestion {{site.data.keyword.ieam}}. |
| `heartbeatIntervals` | Fréquence à laquelle les agents de noeud de périphérie de l'organisation interrogent le concentrateur de gestion pour obtenir des instructions. Pour plus d'informations, consultez la section ci-après. |
| `limits` | Limites de cette organisation. Actuellement, la seule limite est `maxNodes`, qui est le nombre maximal de nœuds de périphérie autorisés dans cette organisation. Il existe une limite pratique au nombre total de noeuds de périphérie pouvant être pris en charge par un seul concentrateur de gestion {{site.data.keyword.ieam}}. Ce paramètre permet à l'administrateur de concentrateur de limiter le nombre de noeuds que chaque organisation peut posséder, ce qui empêche une organisation d'utiliser la totalité de la capacité. La valeur `0` signifie qu'il n'y a pas de limite. |
{: caption="Tableau 3. Paramètres de l'organisation" caption-side="top"}

### Intervalle d'interrogation de signal de présence de l'agent
{: #agent-hb}

L'agent {{site.data.keyword.ieam}} qui est installé sur chaque noeud de périphérie envoie régulièrement des signaux de présence au concentrateur de gestion pour lui indiquer qu'il est toujours en cours d'exécution et connecté, et pour recevoir des instructions. Il vous suffit de modifier ces paramètres pour des environnements à très grande échelle.

L'intervalle entre les signaux de présence est le délai d'attente pendant lequel l'agent attend entre les signaux de présence émis au concentrateur de gestion. L'intervalle est ajusté automatiquement au fil du temps pour optimiser la réactivité et réduire la charge sur le concentrateur de gestion. L'ajustement de l'intervalle est contrôlé par trois paramètres :

| **Paramètre** | **Description**|
|-------------|----------------|
| `minInterval` | Délai le plus court (en secondes) pendant lequel l'agent doit attendre entre les signaux de présence émis au concentrateur de gestion. Lorsqu'un agent est enregistré, il démarre l'interrogation en fonction de cet intervalle. L'intervalle ne sera jamais inférieur à cette valeur. La valeur `0` signifie l'utilisation de la valeur par défaut. |
| `maxInterval` | Délai le plus long (en secondes) pendant lequel l'agent doit attendre entre les signaux de présence émis au concentrateur de gestion. La valeur `0` signifie l'utilisation de la valeur par défaut. |
| `intervalajustement` | Nombre de secondes à ajouter à l'intervalle de signal de présence actuel lorsque l'agent détecte qu'il peut augmenter l'intervalle. Une fois que les signaux de présence sont envoyés au concentrateur de gestion mais qu'aucune instruction n'est reçue pendant un certain temps, l'intervalle entre les signaux de présence augmente progressivement jusqu'à ce qu'il atteigne l'intervalle maximal. De même, lorsque des instructions sont reçues, l'intervalle des signaux de présence est diminué pour garantir un traitement rapide des instructions suivantes. La valeur `0` signifie l'utilisation de la valeur par défaut. |
{: caption="Tableau 4. Paramètres heartbeatIntervals" caption-side="top"}

Les paramètres d'intervalle d'interrogation de signal de présence dans l'organisation sont appliqués aux noeuds qui n'ont pas configuré explicitement l'intervalle des signaux de présence. Pour vérifier si un noeud a défini explicitement l'intervalle entre les signaux de présence, utilisez la commande `hzn exchange node list <node id>`.

Pour plus d'informations sur la configuration des paramètres dans des environnements à grande échelle, voir [Mise à l'échelle de la configuration](../hub/configuration.md#scale).
