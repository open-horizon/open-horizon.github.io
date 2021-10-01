---

copyright:
  years: 2020
lastupdated: "2020-5-11"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Installation de l'interface de ligne de commande hzn
{: #using_hzn_cli}

Lorsque vous installez le logiciel agent d'{{site.data.keyword.ieam}} sur un noeud de périphérie, l'interface de ligne de commande **hzn** est automatiquement installée. Vous pouvez aussi l'installer sans l'agent. Par exemple, un administrateur de périphérie peut vouloir interroger {{site.data.keyword.ieam}} Exchange ou un développeur de périphérie peut vouloir faire des tests avec les commandes **hzn dev**.

1. Procurez-vous l'archive **agentInstallFiles-&lt;edge-device-type&gt;.tar.gz** auprès de l'administrateur du concentrateur de gestion, où **&lt;edge-device-type&gt;** correspond à l'hôte sur lequel vous installerez l'interface de ligne de commande **hzn**. Celle-ci doit avoir été créée à la section [Collecte des informations et des fichiers nécessaires aux dispositifs de périphérie](../../hub/gather_files.md#prereq_horizon). Copiez ce fichier sur l'hôte sur lequel vous souhaitez installer l'interface de ligne de commande **hzn**.

2. Définissez le nom de fichier dans une variable d'environnement pour les étapes suivantes :

   ```bash
   export AGENT_TAR_FILE=agentInstallFiles-<edge-device-type>.tar.gz
   ```
   {: codeblock}

3. Extrayez le package d'interface de ligne de commande du fichier tar :

   ```bash
   tar -zxvf $AGENT_TAR_FILE 'horizon-cli*'
   ```
   {: codeblock}

   * Vérifiez que la version de package est la même que celle de l'agent de dispositif mentionné dans la section [Composants](../getting_started/components.md).

4. Installez le package **horizon-cli** :

   * Sur une distribution Debian :

     ```bash
     sudo apt update && sudo apt install horizon-cli*.deb
     ```
     {: codeblock}

   * Sous {{site.data.keyword.macOS_notm}} :

     ```bash
     sudo installer -pkg horizon-cli-*.pkg -target /
     ```
     {: codeblock}

     Remarque : Sous {{site.data.keyword.macOS_notm}}, vous pouvez également installer le fichier du package horizon-cli à partir de Finder. Cliquez deux fois sur le fichier pour ouvrir le programme d'installation. Si vous recevez un message d'erreur indiquant que le programme "ne peut pas s'ouvrir car il provient d'un développeur non identifié", cliquez avec le bouton droit de la souris sur le fichier et sélectionnez **Ouvrir**. Cliquez de nouveau sur **Ouvrir** lorsqu'une invite vous demandant si vous voulez vraiment l'ouvrir s'affiche. Ensuite, suivez les messages du système pour installer le package de l'interface de ligne de commande Horizon, en vérifiant que votre ID dispose des droits d'administration.

## Désinstallation de l'interface de ligne de commande hzn

Si vous voulez désinstaller le package **horizon-cli** d'un hôte :

* Désinstallez **horizon-cli** d'une distribution Debian :

  ```bash
  sudo apt-get remove horizon-cli
  ```
  {: codeblock}

* Ou désinstallez **horizon-cli** d'{{site.data.keyword.macOS_notm}} :

  * Ouvrez le dossier client hzn (/usr/local/bin) et faites glisser l'application `hzn` dans la corbeille (à la fin de Dock).
