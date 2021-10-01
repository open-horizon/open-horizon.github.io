---

copyright:
years: 2019, 2020, 2021
lastupdated: "2021-09-01"

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

Les instructions ci-dessous vous guident tout au long du processus d'installation du logiciel requis sur votre dispositif de périphérie et d'enregistrement de ce dernier avec {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}).

## Architectures et systèmes d'exploitation pris en charge
{: #suparch-horizon}

{{site.data.keyword.ieam}} prend en charge les architectures et les systèmes d'exploitation avec les architectures matérielles suivantes :

* x86_64
   * Dispositifs ou machines virtuelles {{site.data.keyword.linux_bit_notm}} exécutant Ubuntu 20.x (focal), Ubuntu 18.x (bionic), Debian 10 (buster), Debian 9 (stretch)
   * {{site.data.keyword.rhel}} 8.1, 8.2 et 8.3
   * Fedora Workstation 32
   * CentOS 8.1, 8.2 et 8.3
   * SuSE 15 SP2
* ppc64le
   * {{site.data.keyword.linux_ppc64le_notm}} périphériques ou machines virtuelles exécutant Ubuntu 20.x (focal) ou Ubuntu 18.x (bionique)
   * {{site.data.keyword.rhel}} 7.6, 7.9, 8.1, 8.2 et 8.3
* ARM (32 bits)
   * {{site.data.keyword.linux_notm}} sur ARM (32 bits), par exemple Raspberry Pi, fonctionnant sous Raspbian Buster ou Stretch
* ARM (64 bits)
   * {{site.data.keyword.linux_notm}} sur ARM (64 bits), par exemple NVIDIA Jetson Nano, TX1 ou TX2, fonctionnant sous Ubuntu 18.x (Bionic)
* Mac
   * {{site.data.keyword.macOS_notm}}

**Remarques** : 

* L'installation des dispositifs de périphérie avec Fedora ou SuSE n'est prise en charge que par la méthode [Procédure manuelle avancée d'installation et d'enregistrement d'un agent](../installing/advanced_man_install.md).
* CentOS et {{site.data.keyword.rhel}}les versions ultérieures{{site.data.keyword.ieam}} {{site.data.keyword.version}}ne prennent en charge que Docker comme moteur de conteneur.
* Bien qu'il {{site.data.keyword.ieam}} {{site.data.keyword.version}}soit possible d'exécuter {{site.data.keyword.rhel}} 8.x avec Docker, il n'est officiellement pas pris en charge par{{site.data.keyword.rhel}} .

## Dimensionnement
{: #size}

L'agent nécessite :

* Mémoire vive de 100 Mo (RAM), y compris Docker. La mémoire RAM augmente cette capacité d'environ 100 K par accord, plus toute autre capacité de mémoire supplémentaire requise par les charges de travail s'exécutant sur le dispositif.
* Disque de 400 Mo (Docker inclus). Le disque augmente cette capacité en fonction de la taille des images de conteneur utilisées par les charges de travail et de la taille des objets de modèle (fois 2) déployés sur le dispositif.

# Installation de l'agent
{: #installing_the_agent}

Les instructions ci-dessous vous guident tout au long du processus d'installation du logiciel requis sur votre dispositif de périphérie et d'enregistrement de ce dernier avec {{site.data.keyword.ieam}}.

## Procédures
{: #install-config}

Pour installer et configurer votre dispositif de périphérie, cliquez sur le lien qui correspond à votre type de dispositif de périphérie :

* [Dispositifs ou machines virtuelles {{site.data.keyword.linux_bit_notm}}](#x86-machines)
* [{{site.data.keyword.rhel}}  Périphériques ou machines virtuelles 8.x](#rhel8)
* [Dispositifs ou machines virtuelles {{site.data.keyword.linux_ppc64le_notm}}](#ppc64le-machines)
* [{{site.data.keyword.linux_notm}} sur ARM (32 bits)](#arm-32-bit), par exemple Raspberry Pi exécutant Raspbian
* [{{site.data.keyword.linux_notm}} sur ARM (64 bits)](#arm-64-bit), par exemple, NVIDIA Jetson Nano, TX1 ou TX2
* [{{site.data.keyword.macOS_notm}}](#mac-os-x)

## Dispositifs {{site.data.keyword.linux_bit_notm}} ou machines virtuelles
{: #x86-machines}

### Configuration matérielle requise
{: #hard-req-x86}

* Dispositif Intel&reg; ou AMD 64 bits ou machine virtuelle
* Connexion Internet pour votre dispositif (filaire ou WiFi)
* (Facultatif) Matériel de détection : La plupart des services {{site.data.keyword.horizon}} de périphérie nécessitent du matériel de détection spécialisé.

### Procédure
{: #proc-x86}

Préparez votre appareil en installant une version de Debian, {{site.data.keyword.rhel}}7.x, ou Ubuntu{{site.data.keyword.linux_notm}} . Les instructions ci-après sont basées sur un dispositif fonctionnant sous Ubuntu 18.x.

Installez la version Docker la plus récente sur votre dispositif. Pour plus d'informations, voir [Install Docker](https://docs.docker.com/engine/install/ubuntu/).

A présent que votre dispositif de périphérie est prêt, passez à l'étape [Installation de l'agent](registration.md).

## {{site.data.keyword.rhel}} Périphériques ou machines virtuelles 8.x
{: #rhel8}

### Configuration matérielle requise
{: #hard-req-rhel8}

* Périphérique Intel 64 bits&reg;, périphérique AMD, périphérique ppc64le ou machine virtuelle
* Connexion Internet pour votre dispositif (filaire ou WiFi)
* (Facultatif) Matériel de détection : La plupart des services {{site.data.keyword.horizon}} de périphérie nécessitent du matériel de détection spécialisé.

### Procédure
{: #proc-rhel8}

Préparez votre unité en installant {{site.data.keyword.rhel}} 8.x.

Supprimez Podman et d'autres packages pré-inclus, puis installez Docker comme décrit ici.

1. Désinstallez les packages :
   ```
   yum remove buildah skopeo podman containers-common atomic-registries docker container-tools
   ```
   {: codeblock}

2. Supprimez les fichiers restants &amp;TWBAMP;:
   ```
   rm -rf /etc/containers/* /var/lib/containers/* /etc/docker /etc/subuid* /etc/subgid*
   ```
   {: codeblock}

3. Supprimez tous les stockages de conteneur associés :
   ```
   cd ~ && rm -rf /.local/share/containers/
   ```
   {: codeblock}

4. Installez Docker en suivant les instructions de la section [Installation de Docker CENTOS](https://docs.docker.com/engine/install/centos/).

5. Configurez Docker pour qu'il démarre au démarrage par défaut et suivez toutes les autres [étapes de post-installation de Docker](https://docs.docker.com/engine/install/linux-postinstall/).
   ```
   sudo systemctl enable docker.service    sudo systemctl enable containerd.service
   ```
   {: codeblock}

A présent que votre dispositif de périphérie est prêt, passez à l'étape [Installation de l'agent](registration.md).

## Dispositifs {{site.data.keyword.linux_ppc64le_notm}} ou machines virtuelles
{: #ppc64le-machines}

### Configuration matérielle requise
{: #hard-req-ppc64le}

* Dispositifs ou machine virtuelle ppc64le
* Connexion Internet pour votre dispositif (filaire ou WiFi)
* (Facultatif) Matériel de détection : La plupart des services {{site.data.keyword.horizon}} de périphérie nécessitent du matériel de détection spécialisé.

### Procédure
{: #proc-ppc64le}

Préparez votre périphérique en installant {{site.data.keyword.rhel}}.

Installez la version Docker la plus récente sur votre dispositif. 

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
  **Remarque** : certains dispositifs nécessitent un matériel supplémentaire pour la prise en charge du WiFi.
* (Facultatif) Matériel de détection : La plupart des services {{site.data.keyword.horizon}} de périphérie nécessitent du matériel de détection spécialisé.

### Procédure
{: #proc-pi}

1. Préparez votre unité Raspberry Pi.
   1. Flashez l'image [Raspbian](https://www.raspberrypi.org/downloads/raspbian/) {{site.data.keyword.linux_notm}} sur votre carte MicroSD.

      Pour plus d'informations sur la façon de flasher des images MicroSD à partir de différents systèmes d'exploitation, voir [Raspberry Pi Foundation](https://www.raspberrypi.org/documentation/installation/installing-images/README.md).
      Ces instructions s'appuient sur Raspbian pour les configurations WiFi et SSH.  

      **Avertissement :** La copie flash d'une image sur votre carte MicroSD efface de façon permanente les données qui se trouvent sur votre carte.

   2. (Facultatif) Si vous envisagez d'utiliser le wifi pour vous connecter à votre dispositif, modifiez votre nouvelle image flash pour fournir les données d'identification de wifi WPA2 appropriées. 

      Si vous envisagez de vous connecter via une connexion filaire, cette étape est inutile.  

      Sur votre carte MicroSD, créez un fichier `wpa_supplicant.conf` dans le dossier niveau racine qui contient vos données d'identification WiFi. Ces données incluent votre nom SSID et phrase secrète. Utilisez le format suivant pour votre fichier : 
      
      ```
      country=US       ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev update_config=1       network={
      ssid=“<your-network-ssid>”       psk=“<your-network-passphrase”       key_mgmt=WPA-PSK>       }
      ```
      {: codeblock}

   3. (Facultatif) Si vous souhaitez ou devez exécuter un dispositif Raspberry Pi sans moniteur ni clavier, vous devez activer l'accès de connexion SSH à votre dispositif. L'accès SSH n'est pas disponible par défaut.

      Pour activer la connexion SSH, créez un fichier vide sur votre carte MicroSD appelé `ssh`. Placez-le dans le dossier niveau racine de votre carte. Vous pourrez ainsi vous connecter à votre unité à l'aide des données d'identification par défaut. 

   4. Démontez votre carte MicroSD. Assurez-vous de l'éjecter en toute sécurité de l'unité que vous utilisez pour modifier la carte de sorte que toutes vos modifications soient enregistrées.

   5. Insérez la carte MicroSD dans votre unité Raspberry Pi. Si besoin, connectez un matériel de détection supplémentaire et branchez l'unité à l'alimentation électrique.

   6. Démarrez l'unité.

   7. Modifiez le mot de passe par défaut de l'unité. Dans les images flash Raspbian, le compte par défaut utilise le nom de connexion `pi` et le mot de passe par défaut `raspberry`.

      Connectez-vous à ce compte. Utilisez la commande {{site.data.keyword.linux_notm}} `passwd` standard pour modifier le mot de passe par défaut :

      ```
      passwd       Enter new UNIX password:  
      Retype new UNIX password:        passwd: password updated successfully
      ```
      {: codeblock}
     
   8. Installez la version Docker la plus récente sur votre dispositif. Pour plus d'informations, voir [Install Docker](https://docs.docker.com/engine/install/debian/). 

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
* (Facultatif) Matériel de détection : La plupart des services {{site.data.keyword.horizon}} de périphérie nécessitent du matériel de détection spécialisé.

### Procédure
{: #proc-nvidia}

1. Préparez votre unité NVIDIA Jetson.
   1. Installez le dernier NVIDIA JetPack sur votre dispositif. Pour plus d'informations, voir :
      * (TX1) [Jetson TX1](https://elinux.org/Jetson_TX1)
      * (TX2) [Harness AI at the Edge with the Jetson TX2 Developer Kit](https://developer.nvidia.com/embedded/jetson-tx2-developer-kit)
      * (Nano) [Getting Started With Jetson Nano Developer Kit](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit)

      Vous devez installer ce logiciel ainsi que tous les logiciels prérequis avant d'installer le logiciel {{site.data.keyword.horizon}}.

   2. Modifiez le mot de passe par défaut. Dans la procédure d'installation JetPack, le compte par défaut utilise le nom de connexion `nvidia` et le mot de passe par défaut `nvidia`. 

      Connectez-vous à ce compte. Utilisez la commande {{site.data.keyword.linux_notm}} `passwd` standard pour modifier le mot de passe par défaut :

      ```
      passwd       Enter new UNIX password:  
      Retype new UNIX password:        passwd: password updated successfully
      ```
      {: codeblock}
      
   3. Installez la version Docker la plus récente sur votre dispositif. Pour plus d'informations, voir [Install Docker](https://docs.docker.com/engine/install/debian/). 

A présent que votre dispositif de périphérie est prêt, passez à l'étape [Installation de l'agent](registration.md).

## {{site.data.keyword.macOS_notm}}
{: #mac-os-x}

### Configuration matérielle requise
{: #hard-req-mac}

* Dispositif Mac {{site.data.keyword.intel}} 64 bits 2010 ou version ultérieure
* Virtualisation MMU obligatoire
* MacOS X version 10.11 ("El Capitan") ou ultérieure
* Connexion Internet pour votre machine (filaire ou WiFi)
* (Facultatif) Matériel de détection : La plupart des services {{site.data.keyword.horizon}} de périphérie nécessitent du matériel de détection spécialisé.
### Procédure
{: #proc-mac}

1. Préparez votre unité.
   1. Installez la version Docker la plus récente sur votre dispositif. Pour plus d'informations, voir [Install Docker](https://docs.docker.com/docker-for-mac/install/).

   2. **Installez socat**. Pour ce faire, utilisez l'une ou l'autre méthode ci-dessous :

      * [Use Homebrew to install socat](https://brewinstall.org/install-socat-on-mac-with-brew/).
   
      * Si MacPorts est déjà installé, utilisez-le pour installer socat :
        ```
        sudo port install socat
        ```
        {: codeblock}

## Etapes suivantes

* [Installation de l'agent](registration.md)
* [Mise à jour de l'agent](updating_the_agent.md)

## Rubriques connexes

* [Installation d'{{site.data.keyword.ieam}}](../hub/online_installation.md)
* [Procédure manuelle avancée d'installation et d'enregistrement d'un agent](advanced_man_install.md)
