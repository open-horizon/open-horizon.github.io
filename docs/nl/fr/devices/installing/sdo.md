---

copyright:
years: 2020
lastupdated: "2020-4-24"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Procédure d'installation et d'enregistrement d'un agent SDO
{: #sdo}

**Aperçu technique** : A ce stade, le support SDO ne doit être utilisé que pour tester le processus SDO et se familiariser avec celui-ci, en vue de planifier son utilisation future. Il sera prochainement disponible pour une utilisation en production.

[SDO ![S'ouvre dans un nouvel onglet](../../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://software.intel.com/en-us/secure-device-onboard) (Secure Device Onboard) est une technologie Intel qui permet de configurer des noeuds de périphérie et de les associer à un concentrateur de gestion de manière simple et sécurisée. {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) intègre désormais une prise en charge des dispositifs basés sur SDO pour que l'agent puisse être installé sur le dispositif et enregistré auprès du concentrateur de gestion {{site.data.keyword.ieam}} sans aucune intervention humaine (simplement en mettant le dispositif sous tension).

## Présentation de SDO
{: #sdo-overview}

SDO se compose des quatre composants suivants :

1. Le module SDO sur le dispositif de périphérie (généralement installé par le fabricant du dispositif)
2. Un fichier coupon de propriété (fichier fourni à l'acquéreur avec le dispositif physique)
3. Un serveur SDO Rendezvous (serveur connu contacté en premier par le dispositif activé pour SDO lors de sa première initialisation)
4. Des services propriétaires SDO (services s'exécutant avec le concentrateur de gestion {{site.data.keyword.ieam}} qui connecte le dispositif à cette instance spécifique d'{{site.data.keyword.ieam}})

### Différences avec l'aperçu technique
{: #sdo-tech-preview-differences}

- **Dispositif activé pour SDO** : Dans le cadre des tests SDO, un script est fourni pour ajouter le module SDO à une machine virtuelle afin qu'il se comporte comme un dispositif activé pour SDO au démarrage. Ceci vous permet de tester l'intégration SDO à {{site.data.keyword.ieam}} sans avoir à acheter un dispositif activé pour SDO.
- **Fichier coupon de propriété** : Normalement, le fabricant de dispositif vous remet un certificat de propriété lors de l'achat. Si vous exécutez le script mentionné ci-dessus pour ajouter le module SDO à une machine virtuelle, il créera également le coupon de propriété sur la machine virtuelle. Copier ce fichier depuis la machine virtuelle équivaut à "recevoir le coupon de propriété du fabricant de dispositif".
- **Serveur Rendezvous** : En phase de production, le dispositif d'amorçage contacte le serveur SDO global d'Intel. En phase de développement et de test de cet aperçu technique, vous utilisez un serveur Rendezvous de développement fourni avec les services propriétaires SDO.
- **Services propriétaires SDO** : Dans le cadre de cet aperçu technique, les services propriétaires SDO ne sont pas installés automatiquement sur le concentrateur de gestion {{site.data.keyword.ieam}}. A la place, nous fournissons un script permettant de démarrer facilement les services propriétaires SDO sur n'importe quel serveur disposant d'un accès réseau au concentrateur de gestion {{site.data.keyword.ieam}} et étant accessibles par les dispositifs SDO sur le réseau.

## Utilisation de SDO
{: #using-sdo}

Si vous voulez que SDO installe automatiquement l'agent {{site.data.keyword.ieam}} et qu'il l'enregistre auprès de votre concentrateur de gestion {{site.data.keyword.ieam}}, suivez les étapes de la page [open-horizon/SDO-support repository ![S'ouvre dans un nouvel onglet](../../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://github.com/open-horizon/SDO-support/blob/master/README.md).
