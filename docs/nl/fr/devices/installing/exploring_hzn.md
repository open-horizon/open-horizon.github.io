---

copyright:
years: 2019
lastupdated: "2019-11-17"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Informations sur la commande hzn
{: #exploring-hzn}

Sur les noeuds de périphérie {{site.data.keyword.horizon}}, utilisez la commande `hzn` pour étudier de nombreux aspects de l'état du système local, et plus globalement, de l'écosystème {{site.data.keyword.edge_devices_notm}} en dehors de votre noeud de périphérie. La commande `hzn` permet également d'interagir avec le système et d'apporter des modifications à l'état des ressources dont vous êtes propriétaire.

Pour obtenir de l'aide sur la commande `hzn`, notamment des informations détaillées sur n'importe quelle sous-commande mentionnée dans ce guide, exécutez l'indicateur `--help` (ou `-h`) au niveau de la sous-commande de votre choix. Par exemple, testez les commandes suivantes :

```
hzn --help
  hzn node --help
  hzn exchange pattern --help
```
{: codeblock}

Utilisez l'indicateur `--verbose` (ou `-v`) dans la commande `hzn` pour obtenir une sortie encore plus détaillée. Les commandes `hzn` constituent des encapsuleurs relativement pratiques sur les interfaces de programmation REST fournies par les composants {{site.data.keyword.horizon}}, tandis que l'indicateur `--verbose` affiche généralement les détails des interactions REST en arrière-plan. Par exemple, testez la commande :

```
hzn node list -v
```  
{: codeblock}

La sortie de cette commande indique les deux appels de méthode REST `GET` sur les adresses URL `localhost` à partir desquelles l'agent {{site.data.keyword.horizon}} local répond aux requêtes REST.

Par exemple :

```
[verbose] GET http://localhost:8510/node
[verbose] HTTP code: 200
...
[verbose] GET http://localhost:8510/status
[verbose] HTTP code: 200
```  
{: codeblock}
