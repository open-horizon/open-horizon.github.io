---

copyright:
years: 2020
lastupdated: "2020-8-25"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Retrait d'un agent du cluster de périphérie
{: #remove_agent}

Pour annuler l'enregistrement d'un cluster de périphérie et retirer l'agent d'{{site.data.keyword.ieam}} de ce cluster, procédez comme suit :

1. Extrayez le contenu du script **agent-uninstall.sh** du fichier tar :

   ```bash
   tar -zxvf agentInstallFiles-x86_64-Cluster.tar.gz agent-uninstall.sh
   ```
   {: codeblock}

2. Exportez vos données d'identification d'utilisateur Horizon Exchange :

   ```bash
   export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>
   ```
   {: codeblock}

3. Retirez l'agent :

   ```bash
   ./agent-uninstall.sh -u $HZN_EXCHANGE_USER_AUTH -d
   ```
   {: codeblock}

Remarque : Il arrive parfois que la suppression de l'espace de nom se bloque à l'état "Arrêt en cours". Dans ce cas, voir [A namespace is stuck in the Terminating state](https://www.ibm.com/support/knowledgecenter/SSBS6K_3.1.1/troubleshoot/ns_terminating.html) pour supprimer manuellement l'espace de nom.
