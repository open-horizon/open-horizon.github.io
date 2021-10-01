---

copyright:
years: 2019, 2020
lastupdated: "2020-01-22"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Préparation d'un dispositif de périphérie
{: #installing_the_agent}

Les instructions ci-dessous vous guident tout au long du processus d'installation du logiciel requis sur votre dispositif de périphérie et d'enregistrement de ce dernier avec {{site.data.keyword.edge_notm}} {{site.data.keyword.ieam}}.

## Architectures et systèmes d'exploitation pris en charge
{: #suparch-horizon}

{{site.data.keyword.ieam}} prend en charge les systèmes avec les architectures matérielles suivantes :

* Les dispositifs ou les machines virtuelles {{site.data.keyword.linux_bit_notm}} fonctionnant sous Ubuntu 18.x (Bionic), Ubuntu 16.x (Xenial), Debian 10 (Buster) ou Debian 9 (Stretch)
* {{site.data.keyword.linux_notm}} sur ARM (32 bits), par exemple Raspberry Pi, fonctionnant sous Raspbian Buster ou Stretch
* {{site.data.keyword.linux_notm}} sur ARM (64 bits), par exemple NVIDIA Jetson Nano, TX1 ou TX2, fonctionnant sous Ubuntu 18.x (Bionic)
* {{site.data.keyword.macOS_notm}}

## Dimensionnement
{: #size}

L'agent nécessite :

1. 100 Mo de RAM (Docker inclus). La taille de la mémoire RAM augmente d'environ 100 K par accord, plus toute autre mémoire requise par les charges de travail qui s'exécutent sur le dispositif.
2. Disque de 400 Mo (Docker inclus). La taille de disque peut augmenter en fonction de la taille des images de conteneur qui sont utilisées par les charges de travail et de la taille des objets de modèle (x2) qui sont déployés sur le dispositif.

# Installation de l'agent
{: #installing_the_agent}

Les instructions ci-dessous vous guident tout au long du processus d'installation du logiciel requis sur votre dispositif de périphérie et d'enregistrement de ce dernier avec {{site.data.keyword.ieam}}.

## Procédures
{: #install-config}

Pour installer et configurer votre dispositif de périphérie, cliquez sur le lien qui correspond à votre type de dispositif de périphérie :

* [Dispositifs {{site.data.keyword.linux_bit_notm}} ou machines virtuelles](#x86-machines)
* [{{site.data.keyword.linux_notm}} sur ARM (32 bits)](#arm-32-bit), par exemple Raspberry Pi exécutant Raspbian
* [{{site.data.keyword.linux_notm}} sur ARM (64 bits)](#arm-64-bit), par exemple, NVIDIA Jetson Nano, TX1 ou TX2
* [{{site.data.keyword.macOS_notm}}](#mac-os-x)

## Dispositifs {{site.data.keyword.linux_bit_notm}} ou machines virtuelles
{: #x86-machines}

### Configuration matérielle requise
{: #hard-req-x86}

* Dispositif Intel ou AMD 64 bits, ou machine virtuelle
* Connexion Internet pour votre dispositif (filaire ou WiFi)
* (Facultatif) Matériel de détection : De nombreuses applications d'analyse {{site.data.keyword.horizon}} peuvent avoir besoin d'un matériel de détection spécialisé.

### Procédure
{: #proc-x86}

Préparez votre dispositif en installant une version {{site.data.keyword.linux_notm}} Debian ou Ubuntu. Les instructions ci-après sont basées sur un dispositif fonctionnant sous Ubuntu 18.x.

A présent que votre dispositif de périphérie est prêt, passez à l'étape [Installation de l'agent](registration.md).

## {{site.data.keyword.linux_notm}} sur ARM (32 bits)
{: #arm-32-bit}

### Configuration matérielle requise
{: #hard-req-pi}

* Raspberry Pi 3A+, 3B, 3B+ ou 4 (recommandé)
* Raspberry Pi A+, B+, 2B, Zero-W ou Zero-WH
* Carte de mémoire flash MicroSD (32 Go recommandés)
* Alimentation électrique adaptée à votre dispositif (2 Amp ou supérieur de préférence)
* Connexion Internet pour votre dispositif (filaire ou WiFi).
  Remarque : Certains dispositifs peuvent avoir besoin de matériel supplémentaire pour prendre en charge le wifi.
* (Facultatif) Matériel de détection : De nombreuses applications d'analyse {{site.data.keyword.horizon}} peuvent avoir besoin d'un matériel de détection spécialisé.

### Procédure
{: #proc-pi}

1. Préparez votre unité Raspberry Pi.
   1. Faites une copie flash de l'image [Raspbian ![S'ouvre dans un nouvel onglet](../../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://www.raspberrypi.org/downloads/raspbian/) {{site.data.keyword.linux_notm}} sur votre carte MicroSD.

      Pour de plus amples informations sur la copie flash des images MicroSD à partir de plusieurs plateformes, voir [Raspberry Pi Foundation ![S'ouvre dans un nouvel onglet](../../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://www.raspberrypi.org/documentation/installation/installing-images/README.md).
      Ces instructions s'appuient sur Raspbian pour les configurations WiFi et SSH.  

      **Avertissement :** La copie flash d'une image sur votre carte MicroSD efface de façon permanente les données qui se trouvent sur votre carte.

   2. (Facultatif) Si vous envisagez de vous connecter à votre unité via une connexion WiFi, modifiez votre nouvelle image copiée afin de fournir les données d'identification WiFi WPA2 appropriées. 

      Si vous envisagez de vous connecter via une connexion filaire, cette étape est inutile.  

      Sur votre carte MicroSD, créez un fichier `wpa_supplicant.conf` dans le dossier niveau racine qui contient vos données d'identification WiFi. Ces données incluent votre nom SSID et phrase secrète. Utilisez le format suivant pour votre fichier : 
      
      ```
      country=US
      ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev update_config=1
      network={
      ssid=“<your-network-ssid>”
      psk=“<your-network-passphrase”
      key_mgmt=WPA-PSK>
      }
      ```
      {: codeblock}

   3. (Facultatif) Si vous souhaitez ou devez exécuter une unité Raspberry Pi sans écran ni clavier, activez l'accès à la connexion SSH pour votre unité. L'accès SSH est désactivé par défaut.

      Pour activer la connexion SSH, créez un fichier vide sur votre carte MicroSD appelé `ssh`. Placez-le dans le dossier niveau racine de votre carte. Vous pourrez ainsi vous connecter à votre unité à l'aide des données d'identification par défaut. 

   4. Démontez votre carte MicroSD. Assurez-vous de l'éjecter en toute sécurité de l'unité que vous utilisez pour modifier la carte de sorte que toutes vos modifications soient enregistrées.

   5. Insérez la carte MicroSD dans votre unité Raspberry Pi. Si besoin, connectez un matériel de détection supplémentaire et branchez l'unité à l'alimentation électrique.

   6. Démarrez l'unité.

   7. Modifiez le mot de passe par défaut de l'unité. Dans les images flash Raspbian, le compte par défaut utilise le nom de connexion `pi` et le mot de passe par défaut `raspberry`.

      Connectez-vous à ce compte. Utilisez la commande {{site.data.keyword.linux_notm}} `passwd` standard pour modifier le mot de passe par défaut :

      ```
      passwd
      Enter new UNIX password:  
      Retype new UNIX password: 
      passwd: password updated successfully
      ```
      {: codeblock}

A présent que votre dispositif de périphérie est prêt, passez à l'étape [Installation de l'agent](registration.md).

## {{site.data.keyword.linux_notm}} sur ARM (64 bits)
{: #arm-64-bit}

### Configuration matérielle requise
{: #hard-req-nvidia}

* NVIDIA Jetson Nano, ou TX2 (recommandé)
* NVIDIA Jetson TX1
* Ecran HDMI Business, concentrateur USB, clavier USB, souris USB
* Stockage : 10 Go minimum (SSD recommandé)
* Connexion Internet pour votre dispositif (filaire ou WiFi)
* (Facultatif) Matériel de détection : De nombreuses applications d'analyse {{site.data.keyword.horizon}} peuvent avoir besoin d'un matériel de détection spécialisé.

### Procédure
{: #proc-nvidia}

1. Préparez votre unité NVIDIA Jetson.
   1. Installez le dernier NVIDIA JetPack sur votre dispositif. Pour plus d'informations, voir :
      * (TX1) [Jetson TX1 ![S'ouvre dans un nouvel onglet](../../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://elinux.org/Jetson_TX1)
      * (TX2) [Harness AI at the Edge with the Jetson TX2 Developer Kit ![S'ouvre dans un nouvel onglet](../../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://developer.nvidia.com/embedded/jetson-tx2-developer-kit)
      * (Nano) [Getting Started With Jetson Nano Developer Kit ![S'ouvre dans un nouvel onglet](../../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit)

      Vous devez installer ce logiciel ainsi que tous les logiciels prérequis avant d'installer le logiciel {{site.data.keyword.horizon}}.

   2. Modifiez le mot de passe par défaut. Dans la procédure d'installation JetPack, le compte par défaut utilise le nom de connexion `nvidia` et le mot de passe par défaut `nvidia`. 

      Connectez-vous à ce compte. Utilisez la commande {{site.data.keyword.linux_notm}} `passwd` standard pour modifier le mot de passe par défaut :

      ```
      passwd
      Enter new UNIX password:  
      Retype new UNIX password: 
      passwd: password updated successfully
      ```
      {: codeblock}

A présent que votre dispositif de périphérie est prêt, passez à l'étape [Installation de l'agent](registration.md).

## {{site.data.keyword.macOS_notm}}
{: #mac-os-x}

### Configuration matérielle requise
{: #hard-req-mac}

* Dispositif Mac {{site.data.keyword.inte}} 64 bits 2010 ou version ultérieure

* Virtualisation MMU obligatoire
* MacOS X version 10.11 ("El Capitan") ou ultérieure
* Connexion Internet pour votre machine (filaire ou WiFi)
* (Facultatif) Matériel de détection : De nombreuses applications d'analyse {{site.data.keyword.horizon}} peuvent avoir besoin d'un matériel de détection spécialisé.

### Procédure
{: #proc-mac}

1. Préparez votre unité.
   1. Installez la **version Docker la plus récente** sur votre dispositif. Pour plus d'informations, voir [Install Docker ![S'ouvre dans un nouvel onglet](../../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://docs.docker.com/docker-for-mac/install/).

   2. **Installez socat**. Pour ce faire, utilisez **l'une ou l'autre** méthode ci-dessous :

      * [Use Homebrew to install socat ![S'ouvre dans un nouvel onglet](../../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://brewinstall.org/install-socat-on-mac-with-brew/).
   
      * Si vous avez déjà installé MacPorts, servez-vous en pour installer socat :
        ```
        sudo port install socat
        ```
        {: codeblock}

## Etapes suivantes

* [Mise à jour de l'agent](updating_the_agent.md)
* [Installation de l'agent](registration.md)


## Rubriques connexes

* [Installation du concentrateur de gestion](../../hub/offline_installation.md)
* [Procédure manuelle avancée d'installation et d'enregistrement d'un agent](advanced_man_install.md)
