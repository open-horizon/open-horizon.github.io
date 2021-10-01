---

copyright:
years: 2020
lastupdated: "2020-02-03"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Installation de l'agent
{: #registration}

Lorsque vous installez le logiciel agent d'{{site.data.keyword.horizon}} sur votre dispositif de périphérie, vous pouvez enregistrer ce dernier auprès d'{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) pour l'ajouter au domaine de gestion de l'informatique Edge et exécuter les services de périphérie. Les instructions ci-dessous permettent d'enregistrer votre nouveau dispositif de périphérie avec l'exemple de service de périphérie helloworld minimal pour confirmer que le dispositif de périphérie fonctionne correctement. Le service de périphérie helloworld peut facilement être arrêté lorsque vous êtes prêt à exécuter vos propres services de périphérie sur le dispositif de périphérie.
{:shortdesc}

## Avant de commencer
{: #before_begin}

Vous devez avoir suivi les étapes de la section [Préparation d'un dispositif de périphérie](adding_devices.md).

## Installation et enregistrement des dispositifs de périphérie
{: #installing_registering}

Il existe quatre méthodes différentes pour installer l'agent et enregistrer les dispositifs de périphérie, chacune étant utile dans des circonstances différentes :

* [Procédure automatique d'installation et d'enregistrement d'un agent](automated_install.md) : Permet d'installer et d'enregistrer un dispositif de périphérie avec un minimum d'étapes. **Les nouveaux utilisateurs doivent utiliser cette méthode.**
* [Procédure manuelle avancée d'installation et d'enregistrement de l'agent](advanced_man_install.md) : Suivez vous-même chaque étape pour installer et enregistrer un dispositif de périphérie. Privilégiez cette méthode si vous devez choisir des options particulières et que le script utilisé dans la méthode 1 n'offre pas la flexibilité nécessaire. Cette méthode peut également être utile si vous voulez connaître précisément les éléments requis pour l'installation d'un dispositif de périphérie.
* [Installation et enregistrement d'un agent en bloc](many_install.md#batch-install) - installez et enregistrez de nombreux dispositifs de périphérie à un moment donné.
* [Installation et enregistrement d'agent SDO](sdo.md) : Permet une installation automatique à l'aide des dispositifs SDO.

## Questions et traitement des incidents
{: #questions_ts}

Si vous rencontrez des difficultés au cours de l'une des étapes de cette section, consultez la rubrique relative au traitement des incidents ainsi que celle concernant la foire aux questions. Pour plus d'informations, voir :
  * [Traitement des incidents ](../troubleshoot/troubleshooting.md)
  * [Foire aux questions](../getting_started/faq.md)
