---

copyright:
years: 2020
lastupdated: "2020-2-2"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Mise à jour de l'agent
{: #updating_the_agent}

Si vous avez reçu des packages mis à jour de l'agent {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}), vous pouvez facilement actualiser votre dispositif de périphérie :

1. Suivez les étapes de la rubrique [Collecte des informations et des fichiers nécessaires aux dispositifs de périphérie](../../hub/gather_files.md#prereq_horizon) pour créer le fichier **agentInstallFiles-&lt;edge-device-type&gt;.tar.gz** mis à jour avec les nouveaux packages d'agent.
  
2. Pour chaque dispositif de périphérie, suivez les étapes de la section [Procédure automatique d'installation et d'enregistrement d'un agent](automated_install.md#method_one), sauf lorsque vous exécutez la commande **agent-install.sh** où vous devez spécifier le service et le pattern ou la règle que vous souhaitez exécuter sur le dispositif de périphérie.
