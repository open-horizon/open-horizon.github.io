---

copyright:
years: 2020
lastupdated: "2020-02-5" 

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Traitement de périphérie de la radio logicielle
{: #defined_radio_ex}

Cet exemple utilise une radio logicielle comme exemple de traitement de périphérie. Avec une radio logicielle, vous pouvez envoyer des données brutes via l'ensemble du spectre radio à un serveur cloud à des fins de traitement. Le noeud de périphérie traite les données localement, et soumet des volumes moins importants de données à plus forte valeur ajoutée à un service de traitement cloud en vue d'un traitement supplémentaire.
{:shortdesc}

Le diagramme ci-dessous illustre l'architecture de cet exemple de radio logicielle :

<img src="../../images/edge/08_sdrarch.svg" width="70%" alt="Exemple d'architecture">

Le traitement de périphérie de radio logicielle est un parfait exemple d'une station radio avec extraction des paroles et conversion en texte. Cet exemple effectue une analyse des sentiments sur le texte et met à disposition les résultats et les données via une interface utilisateur à partir de laquelle vous pouvez afficher les détails des données pour chaque noeud de périphérie. Utilisez cet exemple pour en découvrir davantage sur le traitement de périphérie.

La radio logicielle reçoit les signaux radio par le biais du circuit numérique d'une unité centrale afin de se charger de la demande d'une série de circuits analogiques spécialisés. Ce circuit analogique est généralement limité par la largeur du spectre radio qu'il peut recevoir. Un récepteur radio analogique intégré pour recevoir les stations de radio en modulation de fréquence (FM), par exemple, ne peut pas recevoir les signaux radio provenant d'un autre endroit sur le spectre. La radio logicielle a accès à une grande partie du spectre. Si vous ne disposez pas du matériel de radio logicielle, vous pouvez utiliser des données fictives. Lorsque vous utilisez des données fictives, l'audio du flux Internet est traité comme s'il était diffusé sur la modulation de fréquence (FM) et reçu sur votre noeud de périphérie.

Avant d'effectuer cette tâche, procédez à l'enregistrement et à l'annulation de l'enregistrement comme indiqué dans [Installation de l'agent](registration.md).

Ce code contient les composants principaux ci-dessous.

|Composant|Description|
|---------|-----------|
|[sdr service ![S'ouvre dans un nouvel onglet](../../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://github.com/open-horizon/examples/tree/master/edge/services/sdr)|Le service de niveau inférieur a accès au matériel sur le noeud de périphérie|
|[ssdr2evtstreams service ![S'ouvre dans un nouvel onglet](../../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://github.com/open-horizon/examples/tree/master/edge/evtstreams/sdr2evtstreams)|Le service de niveau supérieur reçoit des données du service sdr de niveau inférieur et effectue une analyse locale des données sur le noeud de périphérie. Le service sdr2evtstreams envoie ensuite les données traitées au logiciel dorsal de cloud.|
|[Logiciel dorsal de cloud ![S'ouvre dans un nouvel onglet](../../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://github.com/open-horizon/examples/tree/master/cloud/sdr)|Le logiciel dorsal de cloud reçoit les données des noeuds de périphérie à des fins d'analyse approfondie. L'implémentation dorsale peut alors afficher une carte des noeuds de périphérie, entre autres, dans une interface utilisateur Web.|
{: caption="Tableau 1. Radio logicielle sur les composants principaux d'{{site.data.keyword.message_hub_notm}}" caption-side="top"}

## Enregistrement de votre dispositif

Bien qu'il soit possible d'exécuter ce service sur n'importe quel dispositif de périphérie à l'aide de données fictives, si vous utilisez un dispositif de périphérie tel qu'un Raspberry Pi avec le matériel de radio logicielle, vous devez configurer un module de noyau pour prendre en charge votre matériel. Vous devez configurer manuellement ce module. Les conteneurs Docker peuvent établir une distribution différente de Linux dans leurs contextes, mais le conteneur ne peut pas installer les modules de noyau. 

Procédez comme suit pour configurer le module :

1. En tant qu'utilisateur root, créez un fichier nommé `/etc/modprobe.d/rtlsdr.conf`.
   ```
   sudo nano /etc/modprobe.d/rtlsdr.conf
   ```
   {: codeblock}

2. Ajoutez les lignes suivantes au fichier :
   ```
   blacklist rtl2830
     blacklist rtl2832
     blacklist dvb_usb_rtl28xxu
   ```
   {: codeblock}

3. Sauvegardez le fichier et redémarrez avant de poursuivre :
   ```
   sudo reboot
   ```
   {: codeblock}   

4. Définissez la clé d'interface de programmation {{site.data.keyword.message_hub_notm}} suivante dans votre environnement. Cette clé est créée spécifiquement pour cet exemple et sert à alimenter les données traitées qui sont collectées par votre noeud de périphérie dans l'interface utilisateur de la radio logicielle.
   ```
   export EVTSTREAMS_API_KEY=X2e8cSjbDAMk-ztJLaoi3uffy8qsQTnZttUjcHCfm7cp
    export EVTSTREAMS_BROKER_URL=broker-3-y420pyyyvhhmttz0.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-5-y420pyyyvhhmttz0.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-4-y420pyyyvhhmttz0.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-1-y420pyyyvhhmttz0.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-0-y420pyyyvhhmttz0.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-2-y420pyyyvhhmttz0.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093
   ```
   {: codeblock}

5. Pour exécuter l'exemple de service sdr2evtstreams sur votre noeud de périphérie, enregistrez ce dernier auprès du pattern de déploiement IBM/pattern-ibm.sdr2evtstreams. Suivez les étapes de la page [Preconditions for Using the SDR To IBM Event Streams Example Edge Service ![S'ouvre dans un nouvel onglet](../../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://www.ibm.com/links?url=https%3A%2F%2Fgithub.com%2Fopen-horizon%2Fexamples%2Ftree%2Fmaster%2Fedge%2Fevtstreams%2Fsdr2evtstreams). 

6. Vérifiez l'interface utilisateur Web de l'exemple pour voir si le noeud de périphérie envoie des résultats. Pour plus d'informations, voir [software-defined radio example web UI ![S'ouvre dans un nouvel onglet](../../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://sdr-poc-sdr-poc-app-delightful-leopard.mybluemix.net). Connectez-vous à l'aide des données d'identification suivantes :

   * Nom d'utilisateur : guest@ibm.com
   * Mot de passe : guest123

## Détails relatifs à l'implémentation d'une radio logicielle (SDR)

### Service de bas niveau sdr
{: #sdr}

Le niveau le plus bas de la pile de logiciels pour ce service inclut l'implémentation du service `sdr`. Celui-ci a accès au matériel de radio logicielle local en utilisant la bibliothèque `librtlsdr` et les utilitaires dérivés `rtl_fm` et `rtl_power` avec le daemon `rtl_rpcd`. Pour plus d'informations sur la bibliothèque `librtlsdr`, voir [librtlsdr ![S'ouvre dans un nouvel onglet](../../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://github.com/librtlsdr/librtlsdr).

Le service `sdr` contrôle directement le matériel de radio logicielle pour ajuster le matériel à une certaine fréquence afin de recevoir les données transmises ou de mesurer l'amplitude du signal sur un spectre donné. Un flux de travail type pour ce service peut être de l'ajuster sur une fréquence particulière pour recevoir les données d'une station à cette même fréquence. Ensuite, le service peut traiter les données collectées.

### Service de haut niveau sdr2evtstreams
{: #sdr2evtstreams}

L'implémentation du service de haut niveau `sdr2evtstreams` utilise à la fois l'API REST du service `sdr` et l'API REST du service `gps` sur le réseau Docker virtuel privé. Le service `sdr2evtstreams` reçoit les données du service `sdr`, puis effectue un certain niveau d'analyse locale sur les données pour sélectionner les meilleures stations pour la parole. Le service `sdr2evtstreams` fait ensuite appel à Kafka pour publier des clips audio dans le cloud à l'aide d'{{site.data.keyword.message_hub_notm}}.

### IBM Functions
{: #ibm_functions}

IBM Functions orchestre le côté cloud de l'exemple d'application de radio logicielle. Il est basé sur OpenWhisk et permet d'effectuer des calculs sans serveur. Les calculs sans serveur permettent de déployer les composants de code sans l'aide d'une infrastructure, telle qu'un système d 'exploitation ou un système de langage de programmation. Grâce à IBM Functions, vous vous concentrez sur votre code, et vous laissez IBM se charger de toutes les opérations de mise à l'échelle, sécurité et maintenance continue. Aucun matériel n'a besoin d'être mis à disposition, et aucune machine virtuelle ni aucun conteneur ne sont requis.

Les composants de code sans serveur sont configurés pour se déclencher (s'exécuter) en réponse à des événements. Dans cet exemple, l'événement déclencheur est la réception des messages à partir de vos noeuds de périphérie dans {{site.data.keyword.message_hub_notm}} chaque fois que des clips audio sont publiés par les noeuds de périphérie dans {{site.data.keyword.message_hub_notm}}. Les actions de l'exemple sont déclenchées pour réceptionner les données et agir sur elles. Elles utilisent le service de reconnaissance vocale d'IBM Watson pour convertir les données audio entrantes en texte. Ce texte est ensuite envoyé au service de compréhension du langage naturel IBM Watson pour analyser le sentiment qui se dégage de chacun des mots qu'il contient. Pour plus d'informations, voir [IBM Functions action code ![S'ouvre dans un nouvel onglet](../../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://github.com/open-horizon/examples/blob/master/cloud/sdr/data-processing/ibm-functions/actions/msgreceive.js).

### Base de données IBM
{: #ibm_database}

Le code d'action IBM Functions se termine par le stockage du résultat des sentiments analysés dans les bases de données IBM. Le serveur Web et le logiciel client travaillent ensuite à présenter ces données dans les navigateurs Web utilisateur à partir de la base de données.

### Interface Web
{: #web_interface}

L'interface utilisateur Web de l'application de radio logicielle permet aux utilisateurs de parcourir les données de sentiment qui sont issues des bases de données IBM. Elle affiche également une carte des noeuds de périphérie ayant fournis les données. La carte est créée avec les données issues du service IBM `gps`, qui est utilisé par le code du noeud de périphérie pour le service `sdr2evtstreams`. Le service `gps` peut soit servir d'interface avec le matériel GPS, soit recevoir les informations du propriétaire de l'unité au sujet de la localisation. En l'absence de ces deux éléments, à savoir le matériel GPS et l'emplacement du propriétaire de l'unité, le service `gps` peut estimer la position du noeud de périphérie en se basant sur l'adresse IP du noeud de périphérie pour rechercher l'emplacement géographique. Grâce à ce service, `sdr2evtstreams` est en mesure de fournir des données de localisation au cloud lorsque le service envoie des clips audio. Pour plus d'informations, voir [software-defined radio application web UI code ![S'ouvre dans un nouvel onglet](../../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://github.com/open-horizon/examples/tree/master/cloud/sdr/ui/sdr-app).

IBM Functions, les bases de données IBM et le code de l'interface utilisateur Web peuvent éventuellement être déployés dans IBM Cloud si vous souhaitez créer votre propre interface Web d'exemple de radio logicielle. Pour ce faire, une seule commande est nécessaire après avoir [créé un compte payant![S'ouvre dans un nouvel onglet](../../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://cloud.ibm.com/login). Pour plus d'informations, voir [deployment repository content  ![S'ouvre dans un nouvel onglet](../../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://www.ibm.com/links?url=https%3A%2F%2Fgithub.com%2Fopen-horizon%2Fexamples%2Ftree%2Fmaster%2Fcloud%2Fsdr%2Fdeploy%2Fibm). 

Remarque : Ce processus de déploiement nécessite des services payant qui impliquent des frais sur votre compte {{site.data.keyword.cloud_notm}}.

## Etape suivante

Si vous voulez déployer votre propre logiciel vers un noeud de périphérie, vous devez créer vos propres services de périphérie, ainsi que le pattern ou la règle de déploiement associé(e). Pour plus d'informations, voir [Développement d'un service de périphérie pour les dispositifs](../developing/developing.md).
