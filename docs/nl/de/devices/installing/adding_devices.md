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

# Edge-Einheit vorbereiten
{: #installing_the_agent}

Die folgenden Anweisungen führen Sie durch den Prozess zur Installation der erforderlichen Software auf Ihrer Edge-Einheit und zur Registrierung der Edge-Einheit bei {{site.data.keyword.edge_notm}} {{site.data.keyword.ieam}}. 

## Unterstützte Architekturen und Betriebssysteme
{: #suparch-horizon}

{{site.data.keyword.ieam}} unterstützt Systeme mit den folgenden Hardwarearchitekturen: 

* {{site.data.keyword.linux_bit_notm}}-Einheiten oder virtuelle Maschinen, auf denen 18.x (Bionic), Ubuntu 16.x (Xenial), Debian 10 (Buster) oder Debian 9 (Stretch) ausgeführt wird
* {{site.data.keyword.linux_notm}} on ARM (32-Bit); beispielsweise Raspberry Pi, auf denen Raspbian Buster oder Stretch ausgeführt wird
* {{site.data.keyword.linux_notm}} on ARM (64-Bit); beispielsweise NVIDIA Jetson Nano, TX1 oder TX2, auf denen Ubuntu 18.x (Bionic) ausgeführt wird
* {{site.data.keyword.macOS_notm}}

## Dimensionierung
{: #size}

Für den Agenten bestehen die folgenden Voraussetzungen: 

1. 100 MB Arbeitsspeicher (einschließlich Docker). Darüber hinaus sind pro Vereinbarung (Agreement) weitere 100 KB Arbeitsspeicher (RAM) erforderlich sowie zusätzlicher Hauptspeicher für Workloads, die auf der Einheit ausgeführt werden.
2. 400 MB Plattenspeicherplatz (einschließlich Docker). Darüber hinaus ist abhängig von der Größe der von Workloads verwendeten Container-Images und der Größe der für die Einheit bereitgestellten Modellobjekte (multipliziert mit 2) zusätzlicher Plattenspeicherplatz erforderlich. 

# Agent installieren
{: #installing_the_agent}

Die folgenden Anweisungen führen Sie durch den Prozess zur Installation der erforderlichen Software auf Ihrer Edge-Einheit und zur Registrierung der Edge-Einheit bei {{site.data.keyword.ieam}}. 

## Vorgehensweise
{: #install-config}

Klicken Sie auf den Link für den Typ Ihrer Edge-Einheit, um Informationen zum Installieren und Konfigurieren der Edge-Einheit anzuzeigen:

* [{{site.data.keyword.linux_bit_notm}}-Einheiten oder virtuelle Maschinen](#x86-machines)
* [{{site.data.keyword.linux_notm}} on ARM (32-Bit)](#arm-32-bit); beispielsweise Raspberry Pi unter Raspbian
* [{{site.data.keyword.linux_notm}} on ARM (64-Bit)](#arm-64-bit); beispielsweise NVIDIA Jetson Nano, TX1 oder TX2
* [{{site.data.keyword.macOS_notm}}](#mac-os-x)

## {{site.data.keyword.linux_bit_notm}}-Einheiten oder virtuelle Maschinen
{: #x86-machines}

### Hardwarevoraussetzungen
{: #hard-req-x86}

* 64-Bit-Intel-Einheit oder -AMD-Einheit oder virtuelle Maschine
* Internetverbindung für Ihre Einheit (kabelgebunden oder WiFi)
* (Optional) Sensorenhardware: Zahlreiche {{site.data.keyword.horizon}}-Insight-Anwendungen können spezialisierte Sensorenhardware benötigen.

### Vorgehensweise
{: #proc-x86}

Bereiten Sie die Einheit vor. Installieren Sie dazu eine Debian- oder Ubuntu-Variante von {{site.data.keyword.linux_notm}}. Die Anweisungen in dieser Dokumentation gelten für eine Einheit, die mit Ubuntu 18.x arbeitet.

Ihre Edge-Einheit ist jetzt vorbereitet. Fahren Sie fort mit [Agent installieren](registration.md).

## {{site.data.keyword.linux_notm}} on ARM (32-Bit)
{: #arm-32-bit}

### Hardwarevoraussetzungen
{: #hard-req-pi}

* Raspberry Pi 3A+, 3B, 3B+ oder 4 (bevorzugt)
* Raspberry Pi A+, B+, 2B, Zero-W oder Zero-WH
* MicroSD-Flashkarte (32 GB bevorzugt)
* Geeignete Energiequelle für Ihre Einheit (mindestens 2 Ampere bevorzugt)
* Internetverbindung für Ihre Einheit (kabelgebunden oder WiFi)
  Hinweis: Bestimmte Einheiten können zusätzliche Hardware zur WiFi-Unterstützung benötigen.
* (Optional) Sensorenhardware: Zahlreiche {{site.data.keyword.horizon}}-Insight-Anwendungen können spezialisierte Sensorenhardware benötigen.

### Vorgehensweise
{: #proc-pi}

1. Bereiten Sie die Raspberry Pi-Einheit vor.
   1. Kopieren Sie das [Raspbian ![Wird in einer neuen Registerkarte geöffnet](../../images/icons/launch-glyph.svg "Wird in einer neuen Registerkarte geöffnet")](https://www.raspberrypi.org/downloads/raspbian/) {{site.data.keyword.linux_notm}}-Image auf Ihre MicroSD-Karte (Flash-Speicherung).

      Weitere Einzelheiten zur Flash-Speicherung von Images auf MicroSD-Karten für zahlreiche Plattformen finden Sie in den Informationen der [Raspberry Pi Foundation ![Wird in einer neuen Registerkarte geöffnet](../../images/icons/launch-glyph.svg "Wird in einer neuen Registerkarte geöffnet")](https://www.raspberrypi.org/documentation/installation/installing-images/README.md).
      In diesen Anweisungen wird Raspbian für WiFi- und SSH-Konfigurationen verwendet.  

      **Warnung:** Durch die Flash-Speicherung eines Images auf Ihrer MicroSD-Karte werden die bereits auf der Karte befindlichen Daten dauerhaft gelöscht.

   2. (Optional) Wenn Sie zur Herstellung der Verbindung zu Ihrer Einheit WiFi verwenden wollen, dann bearbeiten Sie das neu erstellte Flash-Image, um die korrekten WPA2-WiFi-Berechtigungsnachweise anzugeben. 

      Wenn Sie den Einsatz einer kabelgebundenen Netzverbindung planen, müssen Sie diesen Schritt nicht ausführen.  

      Erstellen Sie auf der MicroSD-Karte im Ordner auf Stammverzeichnisebene eine Datei mit dem Namen `wpa_supplicant.conf`, die Ihre WiFi-Berechtigungsnachweise enthält. Zu diesen Berechtigungsnachweisen gehören der Name der Netz-SSID und die entsprechende Kennphrase. Verwenden Sie für Ihre Datei das folgende Format: 
      
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

   3. (Optional) Wenn Sie die Raspberry Pi-Einheit ohne Monitor oder Tastatur ausführen müssen oder wollen, dann muss der Zugriff auf Ihre Einheit über eine SSH-Verbindung aktiviert werden. Der SSH-Zugriff ist standardmäßig inaktiviert. 

      Zur Herstellung einer SSH-Verbindung müssen Sie eine leere Datei auf Ihrer MicroSD-Karte erstellen und ihr den Namen `ssh` zuordnen. Speichern Sie diese Datei auf Ihrer Karte im Ordner auf Stammverzeichnisebene. Die Einbindung dieser Datei ermöglicht Ihnen die Herstellung einer Verbindung zu Ihrer Einheit mithilfe der Standardberechtigungsnachweise. 

   4. Entfernen Sie die MicroSD-Karte. Vergewissern Sie sich, dass die Karte sicher aus der Einheit entfernt wurde, die Sie zur Bearbeitung der Karte verwendet haben, um sicherzustellen, dass alle Änderungen geschrieben wurden.

   5. Legen Sie die MicroSD-Karte in Ihre Raspberry Pi-Einheit ein. Schließen Sie die optionale Sensorenhardware an und verbinden Sie die Einheit mit der Stromversorgung.

   6. Starten Sie die Einheit.

   7. Ändern Sie das Standardkennwort Ihrer Einheit. In Raspbian-Flash-Images verwendet das Standardkonto den Anmeldenamen `pi` und das Standardkennwort `raspberry`.

      Melden Sie sich bei diesem Konto an. Benutzen Sie den standardmäßigen {{site.data.keyword.linux_notm}}-Befehl `passwd`, um das Standardkennwort zu ändern:

      ```
      passwd
      Enter new UNIX password:  
      Retype new UNIX password: 
      passwd: password updated successfully
      ```
      {: codeblock}

Ihre Edge-Einheit ist jetzt vorbereitet. Fahren Sie fort mit [Agent installieren](registration.md).

## {{site.data.keyword.linux_notm}} on ARM (64-Bit)
{: #arm-64-bit}

### Hardwarevoraussetzungen
{: #hard-req-nvidia}

* NVIDIA Jetson Nano oder TX2 (empfohlen)
* NVIDIA Jetson TX1
* HDMI Business Monitor, USB-Hub, USB-Tastatur, USB-Maus
* Speicher: Mindestens 10 GB (SSD empfohlen)
* Internetverbindung für Ihre Einheit (kabelgebunden oder WiFi)
* (Optional) Sensorenhardware: Zahlreiche {{site.data.keyword.horizon}}-Insight-Anwendungen können spezialisierte Sensorenhardware benötigen.

### Vorgehensweise
{: #proc-nvidia}

1. Bereiten Sie die NVIDIA Jetson-Einheit vor.
   1. Installieren Sie das neueste NVIDIA JetPack auf Ihrer Einheit. Weitere Informationen finden Sie in den folgenden Abschnitten:
      * (TX1) [Jetson TX1 ![Wird in einer neuen Registerkarte geöffnet](../../images/icons/launch-glyph.svg "Wird in einer neuen Registerkarte geöffnet")](https://elinux.org/Jetson_TX1) 
      * (TX2) [Harness AI at the Edge with the Jetson TX2 Developer Kit ![Wird in einer neuen Registerkarte geöffnet](../../images/icons/launch-glyph.svg "Wird in einer neuen Registerkarte geöffnet")](https://developer.nvidia.com/embedded/jetson-tx2-developer-kit) 
      * (Nano) [Getting Started With Jetson Nano Developer Kit ![Wird in einer neuen Registerkarte geöffnet](../../images/icons/launch-glyph.svg "Wird in einer neuen Registerkarte geöffnet")](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit) 

      Sie müssen diese Software und alle vorausgesetzten Softwarekomponenten installieren, bevor Sie die {{site.data.keyword.horizon}}-Software installieren.

   2. Ändern Sie das Standardkennwort. In der JetPack-Installationsprozedur verwendet das Standardkonto den Anmeldenamen `nvidia` und das Standardkennwort `nvidia`. 

      Melden Sie sich bei diesem Konto an. Benutzen Sie den standardmäßigen {{site.data.keyword.linux_notm}}-Befehl `passwd`, um das Standardkennwort zu ändern:

      ```
      passwd
      Enter new UNIX password:  
      Retype new UNIX password: 
      passwd: password updated successfully
      ```
      {: codeblock}

Ihre Edge-Einheit ist jetzt vorbereitet. Fahren Sie fort mit [Agent installieren](registration.md).

## {{site.data.keyword.macOS_notm}}
{: #mac-os-x}

### Hardwarevoraussetzungen
{: #hard-req-mac}

* {{site.data.keyword.intel}}-Mac-Einheit ab 2010
mit 64-Bit-Architektur
* MMU-Virtualisierung (erforderlich)
* Mac OS X Version 10.11 ("El Capitan") oder höher
* Internetverbindung für Ihre Maschine (kabelgebunden oder WiFi)
* (Optional) Sensorenhardware: Zahlreiche {{site.data.keyword.horizon}}-Insight-Anwendungen können spezialisierte Sensorenhardware benötigen.

### Vorgehensweise
{: #proc-mac}

1. Bereiten Sie die Einheit vor.
   1. Installieren Sie die **neueste Docker-Version** auf Ihrer Einheit. Weitere Einzelheiten hierzu finden Sie in den Informationen zur [Installation von Docker ![Wird in einer neuen Registerkarte geöffnet](../../images/icons/launch-glyph.svg "Wird in einer neuen Registerkarte geöffnet")](https://docs.docker.com/docker-for-mac/install/).

   2. **Installieren Sie 'socat'**. Sie können **eine** der folgenden Methoden verwenden, um 'socat' zu installieren: 

      * [Verwenden Sie zur Installation von 'socat' Homebrew ![Wird in einer neuen Registerkarte geöffnet](../../images/icons/launch-glyph.svg "Wird in einer neuen Registerkarte geöffnet")](https://brewinstall.org/install-socat-on-mac-with-brew/).
   
      * Wenn Sie bereits MacPorts installiert haben, können Sie MacPorts wie folgt zum Installieren von 'socat' verwenden:
        ```
        sudo port install socat
        ```
        {: codeblock}

## Weitere Schritte

* [Agent aktualisieren](updating_the_agent.md)
* [Agent installieren](registration.md)


## Zugehörige Informationen

* [Management-Hub installieren](../../hub/offline_installation.md)
* [Erweiterte manuelle Installation und Registrierung eines Agenten](advanced_man_install.md)
