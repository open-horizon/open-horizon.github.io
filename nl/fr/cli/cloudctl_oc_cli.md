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

# Installation de cloudctl, kubectl et oc
{: #cloudctl_oc_cli}

Pour installer les outils de ligne de commande nécessaires à la gestion des aspects du concentrateur de gestion {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) et des clusters de périphérie, procédez comme suit :

## cloudctl

1. Naviguez dans votre {{site.data.keyword.ieam}} interface utilisateur web à l'adresse `https://<CLUSTER_URL>/common-nav/cli`

2. Développez la section **Interface de ligne de commande d'IBM Cloud Pak** et sélectionnez votre **système d'exploitation**.

3. Copiez la commande **curl** affichée et exécutez-la pour télécharger le fichier binaire **cloudctl**.

4. Définissez le fichier comme exécutable et déplacez-le vers **/usr/local/bin** :
  
   ```bash
   chmod 755 cloudctl-*    sudo mv cloudctl-* /usr/local/bin/cloudctl
   ```
   {: codeblock}

5. Vérifiez que **/usr/local/bin** se trouve dans la variable PATH, puis vérifiez que **cloudctl** fonctionne correctement :
  
   ```bash
   cloudctl --help
   ```
   {: codeblock}

## oc

1. Téléchargez le fichier tar CLI {{site.data.keyword.open_shift_cp}}à partir de l'[interface de ligne de commande du client OpenShift (oc)](https://mirror.openshift.com/pub/openshift-v4/clients/ocp/latest/). Sélectionnez le fichier **openshift-client- \ *-\ * .tar.gz** correspondant à votre système d'exploitation.

2. Recherchez le fichier tar téléchargé et décompressez-le :
  
   ```bash
   tar -zxvf openshift-client-*-*.tar.gz
   ```
   {: codeblock}

3. Déplacez la commande **oc** vers **/usr/local/bin** :
  
   ```bash
   sudo mv oc /usr/local/bin/
   ```
   {: codeblock}

4. Vérifiez que **/usr/local/bin** se trouve dans la variable PATH, puis vérifiez que **oc** fonctionne correctement :
  
   ```bash
   oc --help
   ```
   {: codeblock}

Vous pouvez également utiliser [homebrew](https://brew.sh/) pour installer **oc** sur {{site.data.keyword.macOS_notm}} :
  
   ```bash
   brew install openshift-cli
   ```
   {: codeblock}

## Kubectl

Suivez les instructions de la rubrique [Installer et configurer kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/).
