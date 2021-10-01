---

copyright:
years: 2019
lastupdated: "2019-06-26"

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

***Note du rédacteur : contenu à fusionner avec software_defined_radio_ex.md lorsque Troy combine.***

Cet exemple utilise une radio logicielle comme exemple de traitement de périphérie. Avec une radio logicielle, vous pouvez envoyer des données brutes via l'ensemble du spectre radio à un serveur cloud à des fins de traitement. Le noeud de périphérie traite les données localement, et soumet des volumes moins importants de données à plus forte valeur ajoutée à un service de traitement cloud en vue d'un traitement supplémentaire.
{:shortdesc}

Le diagramme ci-dessous illustre l'architecture de cet exemple de radio logicielle :

<img src="../../images/edge/08_sdrarch.svg" width="70%" alt="Exemple d'architecture">

Le traitement de périphérie de radio logicielle est un parfait exemple d'une station radio avec extraction des paroles et conversion en texte. Cet exemple effectue une analyse des sentiments sur le texte et met à disposition les résultats et les données via une interface utilisateur à partir de laquelle vous pouvez afficher les détails des données pour chaque noeud de périphérie. Utilisez cet exemple pour en découvrir davantage sur le traitement de périphérie.

La radio logicielle reçoit les signaux radio par le biais du circuit numérique d'une unité centrale afin de se charger de la demande d'une série de circuits analogiques spécialisés. Ce circuit analogique est généralement limité par la largeur du spectre radio qu'il peut recevoir. Un récepteur radio analogique intégré pour recevoir les stations de radio en modulation de fréquence (FM), par exemple, ne peut pas recevoir les signaux radio provenant d'un autre endroit sur le spectre. La radio logicielle a accès à une grande partie du spectre. Si vous ne disposez pas du matériel de radio logicielle, vous pouvez utiliser des données fictives. Lorsque vous utilisez des données fictives, l'audio du flux Internet est traité comme s'il était diffusé sur la modulation de fréquence (FM) et reçu sur votre noeud de périphérie.

Avant d'effectuer cette tâche, procédez à l'enregistrement et à l'annulation de l'enregistrement du dispositif de périphérie comme indiqué à la section [Installation de l'agent Horizon sur votre dispositif de périphérie et enregistrement à l'aide de l'exemple Hello world](registration.md).

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

4. Définissez la clé d'interface de programmation {{site.data.keyword.message_hub_notm}} suivante dans votre environnement. Cette clé est créée spécifiquement pour cet exemple et sert à alimenter les données traitées recueillies par votre noeud de périphérie dans l'interface utilisateur de la radio logicielle.

   ```
   export EVTSTREAMS_API_KEY=X2e8cSjbDAMk-ztJLaoi3uffy8qsQTnZttUjcHCfm7cp
    export EVTSTREAMS_BROKER_URL=broker-3-y420pyyyvhhmttz0.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-5-y420pyyyvhhmttz0.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-4-y420pyyyvhhmttz0.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-1-y420pyyyvhhmttz0.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-0-y420pyyyvhhmttz0.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-2-y420pyyyvhhmttz0.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093
   ```
   {: codeblock}

5. Pour exécuter l'exemple de service sdr2evtstreams sur votre noeud de périphérie, enregistrez ce dernier auprès du pattern de déploiement IBM/pattern-ibm.sdr2evtstreams. Suivez les étapes de la page [Preconditions for Using the SDR To IBM Event Streams Example Edge Service ![S'ouvre dans un nouvel onglet](../../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://www.ibm.com/links?url=https%3A%2F%2Fgithub.com%2Fopen-horizon%2Fexamples%2Ftree%2Fmaster%2Fedge%2Fevtstreams%2Fsdr2evtstreams). 

6. Vérifiez l'interface utilisateur Web de l'exemple pour voir si le noeud de périphérie envoie des résultats. Pour plus d'informations, voir [software-defined radio example web UI ![S'ouvre dans un nouvel onglet](../../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://sdr-poc-sdr-poc-app-delightful-leopard.mybluemix.net). Connectez-vous à l'aide des données d'identification suivantes :

   * Nom d'utilisateur : guest@ibm.com
   * Mot de passe : guest123

## Déploiement sur le cloud

IBM Functions, les bases de données IBM et le code de l'interface utilisateur Web peuvent éventuellement être déployés dans IBM Cloud si vous souhaitez créer votre propre interface Web d'exemple de radio logicielle. Pour ce faire, une seule commande est nécessaire après avoir [créé un compte payant![S'ouvre dans un nouvel onglet](../../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://cloud.ibm.com/login).

Le code de déploiement se trouve dans le référentiel examples/cloud/sdr/deploy/ibm. Pour plus d'informations, voir [deployment repository content  ![S'ouvre dans un nouvel onglet](../../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://www.ibm.com/links?url=https%3A%2F%2Fgithub.com%2Fopen-horizon%2Fexamples%2Ftree%2Fmaster%2Fcloud%2Fsdr%2Fdeploy%2Fibm). 

Ce code inclut un fichier README.md avec des instructions détaillées et un script deploy.sh qui gère la charge de travail. Le référentiel contient également un fichier Makefile en tant qu'interface supplémentaire dans le script deploy.sh. Consultez les instructions du référentiel pour en savoir plus sur le déploiement de votre propre système dorsal cloud pour l'exemple de radio logicielle. 

Remarque : Ce processus de déploiement nécessite des services payant qui impliquent des frais sur votre compte {{site.data.keyword.cloud_notm}}.

## Etape suivante

Si vous voulez déployer votre propre logiciel vers un noeud de périphérie, vous devez créer vos propres services de périphérie, ainsi que le pattern ou la règle de déploiement associé(e). Pour plus d'informations, voir [Développement de services de périphérie avec IBM Edge Application Manager for Devices](../developing/developing.md).
