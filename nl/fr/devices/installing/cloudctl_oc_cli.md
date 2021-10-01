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

Les outils de ligne de commande sont nécessaires pour gérer les divers aspects des clusters de périphérie et du concentrateur de gestion d'{{site.data.keyword.edge_notm}}. Installez-les en suivant les étapes ci-dessous :

* **cloudctl et kubectl** : Procurez-vous l'interface de ligne de commande IBM Cloud Pak (**cloudctl**) et l'interface de ligne de commande Kubernetes (**kubeclt**) depuis votre interface utilisateur Web d'{{site.data.keyword.edge_notm}} à l'adresse `https://<CLUSTER_URL>/common-nav/cli`

  * Une autre solution pour installer **kubectl** sur {{site.data.keyword.macOS_notm}} consiste à utiliser [homebrew ![S'ouvre dans un nouvel onglet](../../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://brew.sh/) :
  
    ```bash
    brew install kubernetes-cli`
    ```
    {: codeblock}

* **oc** : Procurez-vous l'interface de ligne de commande {{site.data.keyword.open_shift_cp}} sur la page [OpenShift client CLI (oc) ![S'ouvre dans un nouvel onglet](../../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://mirror.openshift.com/pub/openshift-v4/clients/ocp/latest/).

  * Une autre solution pour installer **oc** sur {{site.data.keyword.macOS_notm}} consiste à utiliser [homebrew ![S'ouvre dans un nouvel onglet](../../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://brew.sh/) :
  
    ```bash
    brew install openshift-cli`
    ```
    {: codeblock}
