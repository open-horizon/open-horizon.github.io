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

# Edge-Einheit vorbereiten
{: #installing_the_agent}

Die folgenden Anweisungen führen Sie durch den Prozess zur Installation der erforderlichen Software auf Ihrer Edge-Einheit und zur Registrierung der Edge-Einheit bei {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}).

## Unterstützte Architekturen und Betriebssysteme
{: #suparch-horizon}

{{site.data.keyword.ieam}} unterstützt Architekturen und Betriebssysteme mit den folgenden Hardwarearchitekturen:

* x86_64
   * {{site.data.keyword.linux_bit_notm}}-Einheiten oder virtuelle Maschinen, auf denen Ubuntu 20.x (Focal), Ubuntu 18.x (Bionic), Debian 10 (Buster) oder Debian 9 (Stretch) ausgeführt wird
   * {{site.data.keyword.rhel}} 8.1, 8.2 und 8.3
   * Fedora Workstation 32
   * CentOS 8.1, 8.2 und 8.3
   * SuSE 15 SP2
* ppc64le
   * {{site.data.keyword.linux_ppc64le_notm}} Einheiten oder virtuelle Maschinen, die Ubuntu 20.x (fokal) oder Ubuntu 18.x (bionic) ausführen
   * {{site.data.keyword.rhel}} 7.6, 7.9, 8.1, 8.2 und 8.3
* ARM (32-Bit)
   * {{site.data.keyword.linux_notm}} on ARM (32-Bit); beispielsweise Raspberry Pi, auf denen Raspbian Buster oder Stretch ausgeführt wird
* ARM (64-Bit)
   * {{site.data.keyword.linux_notm}} on ARM (64-Bit); beispielsweise NVIDIA Jetson Nano, TX1 oder TX2, auf denen Ubuntu 18.x (Bionic) ausgeführt wird
* Mac
   * {{site.data.keyword.macOS_notm}}

**Hinweise:** 

* Die Installation von Edge-Einheiten mit Fedora oder SuSE wird nur bei der Methode der  [erweiterten manuellen Agenteninstallation und -registrierung](../installing/advanced_man_install.md) unterstützt.
* CentOS und {{site.data.keyword.rhel}} auf {{site.data.keyword.ieam}} {{site.data.keyword.version}} unterstützen Docker nur als Container-Engine.
* {{site.data.keyword.ieam}} {{site.data.keyword.version}} unterstützt die Ausführung von {{site.data.keyword.rhel}} 8.x mit Docker, wird jedoch offiziell nicht unterstützt von {{site.data.keyword.rhel}}.

## Dimensionierung
{: #size}

Für den Agenten bestehen die folgenden Voraussetzungen:

* 100 MB Arbeitsspeicher (RAM), inklusive Docker. Darüber hinaus sind pro Vereinbarung (Agreement) weitere 100 KB Arbeitsspeicher (RAM) erforderlich sowie zusätzlicher Hauptspeicher für Workloads, die auf der Einheit ausgeführt werden.
* 400 MB Plattenspeicherplatz (einschließlich Docker). Darüber hinaus ist abhängig von der Größe der von Workloads verwendeten Container-Images und der Größe der für die Einheit bereitgestellten Modellobjekte (multipliziert mit 2) zusätzlicher Plattenspeicherplatz erforderlich.

# Agent installieren
{: #installing_the_agent}

Die folgenden Anweisungen führen Sie durch den Prozess zur Installation der erforderlichen Software auf Ihrer Edge-Einheit und zur Registrierung der Edge-Einheit bei {{site.data.keyword.ieam}}.

## Vorgehensweise
{: #install-config}

Klicken Sie auf den Link für den Typ Ihrer Edge-Einheit, um Informationen zum Installieren und Konfigurieren der Edge-Einheit anzuzeigen:

* [{{site.data.keyword.linux_bit_notm}}-Einheiten oder virtuelle Maschinen](#x86-machines)
* [{{site.data.keyword.rhel}} 8.x-Einheiten oder virtuelle Maschinen](#rhel8)
* [{{site.data.keyword.linux_ppc64le_notm}}-Einheiten oder virtuelle Maschinen](#ppc64le-machines)
* [{{site.data.keyword.linux_notm}} on ARM (32-Bit)](#arm-32-bit); beispielsweise Raspberry Pi unter Raspbian
* [{{site.data.keyword.linux_notm}} on ARM (64-Bit)](#arm-64-bit); beispielsweise NVIDIA Jetson Nano, TX1 oder TX2
* [{{site.data.keyword.macOS_notm}}](#mac-os-x)

## {{site.data.keyword.linux_bit_notm}}-Einheiten oder virtuelle Maschinen
{: #x86-machines}

### Hardwarevoraussetzungen
{: #hard-req-x86}

* 64-Bit-Intel&reg;-Einheit oder -AMD-Einheit oder virtuelle Maschine
* Internetverbindung für Ihre Einheit (kabelgebunden oder WiFi)
* (Optional) Sensorenhardware: Zahlreiche {{site.data.keyword.horizon}}-Edge-Services benötigen spezialisierte Sensorenhardware.

### Vorgehensweise
{: #proc-x86}

Bereiten Sie Ihre Einheit vor, indem Sie einen Debian-, {{site.data.keyword.rhel}} 7.x-oder Ubuntu- {{site.data.keyword.linux_notm}}installieren. Die Anweisungen in dieser Dokumentation gelten für eine Einheit, die mit Ubuntu 18.x arbeitet.

Installieren Sie die neueste Docker-Version auf Ihrer Einheit. Weitere Informationen finden Sie unter [Install Docker](https://docs.docker.com/engine/install/ubuntu/).

Ihre Edge-Einheit ist jetzt vorbereitet. Fahren Sie fort mit [Agent installieren](registration.md).

## {{site.data.keyword.rhel}} 8.x-Einheiten oder virtuelle Maschinen
{: #rhel8}

### Hardwarevoraussetzungen
{: #hard-req-rhel8}

* 64-Bit-Intel-&reg; -Einheit, AMD-Einheit, ppc64le-Einheit oder virtuelle Maschine
* Internetverbindung für Ihre Einheit (kabelgebunden oder WiFi)
* (Optional) Sensorenhardware: Zahlreiche {{site.data.keyword.horizon}}-Edge-Services benötigen spezialisierte Sensorenhardware.

### Vorgehensweise
{: #proc-rhel8}

Bereiten Sie Ihr Gerät vor, indem Sie {{site.data.keyword.rhel}} 8.x installieren.

Entfernen Sie Podman und andere vorinstallierte Pakete, und installieren Sie anschließend Docker wie hier beschrieben.

1. Pakete deinstallieren:
   ```
   yum remove buildah skopeo podman containers-common atomic-registries docker container-tools
   ```
   {: codeblock}

2. Entfernen Sie verbleibende Artefakte &amp;TWBAMP; Dateien:
   ```
   rm -rf /etc/containers/* /var/lib/containers/* /etc/docker /etc/subuid* /etc/subgid*
   ```
   {: codeblock}

3. Löschen Sie den zugehörigen Containerspeicher:
   ```
   cd ~ && rm -rf /.local/share/containers/
   ```
   {: codeblock}

4. Installieren Sie Docker, indem Sie die Anweisungen für [Docker CENTOS Installation](https://docs.docker.com/engine/install/centos/) befolgen.

5. Konfigurieren Sie Docker, um standardmäßig mit dem Booten zu starten und alle anderen [Docker-Post-Installationsschritte](https://docs.docker.com/engine/install/linux-postinstall/)zu befolgen.
   ```
   sudo systemctl enable docker.service sudo systemctl enable containerd.service
   ```
   {: codeblock}

Ihre Edge-Einheit ist jetzt vorbereitet. Fahren Sie fort mit [Agent installieren](registration.md).

## {{site.data.keyword.linux_ppc64le_notm}}-Einheiten oder virtuelle Maschinen
{: #ppc64le-machines}

### Hardwarevoraussetzungen
{: #hard-req-ppc64le}

* ppc64le-Einheit oder virtuelle Maschine
* Internetverbindung für Ihre Einheit (kabelgebunden oder WiFi)
* (Optional) Sensorenhardware: Zahlreiche {{site.data.keyword.horizon}}-Edge-Services benötigen spezialisierte Sensorenhardware.

### Vorgehensweise
{: #proc-ppc64le}

Bereiten Sie Ihr Gerät vor, indem Sie {{site.data.keyword.rhel}}installieren.

Installieren Sie die neueste Docker-Version auf Ihrer Einheit. 

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
  **Hinweis:** Bestimmte Einheiten benötigen zusätzliche Hardware zur WiFi-Unterstützung.
* (Optional) Sensorenhardware: Zahlreiche {{site.data.keyword.horizon}}-Edge-Services benötigen spezialisierte Sensorenhardware.

### Vorgehensweise
{: #proc-pi}

1. Bereiten Sie die Raspberry Pi-Einheit vor.
   1. Flashen Sie das [Raspbian](https://www.raspberrypi.org/downloads/raspbian/) {{site.data.keyword.linux_notm}}-Image auf Ihre MicroSD-Karte.

      Weitere Informationen zum Flashen von MicroSD-Images von vielen Betriebssystemen finden Sie unter [Raspberry Pi Foundation](https://www.raspberrypi.org/documentation/installation/installing-images/README.md).
      In diesen Anweisungen wird Raspbian für WiFi- und SSH-Konfigurationen verwendet.  

      **Warnung:** Durch die Flash-Speicherung eines Images auf Ihrer MicroSD-Karte werden die bereits auf der Karte befindlichen Daten dauerhaft gelöscht.

   2. (Optional) Wenn Sie zur Herstellung der Verbindung zu Ihrer Einheit WiFi verwenden wollen, dann bearbeiten Sie das neu erstellte Flash-Image, um die korrekten WPA2-WiFi-Berechtigungsnachweise anzugeben. 

      Wenn Sie den Einsatz einer kabelgebundenen Netzverbindung planen, müssen Sie diesen Schritt nicht ausführen.  

      Erstellen Sie auf der MicroSD-Karte im Ordner auf Stammverzeichnisebene eine Datei mit dem Namen `wpa_supplicant.conf`, die Ihre WiFi-Berechtigungsnachweise enthält. Zu diesen Berechtigungsnachweisen gehören der Name der Netz-SSID und die entsprechende Kennphrase. Verwenden Sie für Ihre Datei das folgende Format: 
      
      ```
      country=US       ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev update_config=1       network={
      ssid=“<ihre_netz-ssid>”       psk=“<ihre_netzkennphrase”       key_mgmt=WPA-PSK>       }
      ```
      {: codeblock}

   3. (Optional) Wenn Sie die Raspberry Pi-Einheit ohne Monitor oder Tastatur ausführen müssen oder wollen, dann muss der Zugriff auf Ihre Einheit über eine SSH-Verbindung aktiviert werden. Der SSH-Zugriff ist standardmäßig nicht verfügbar.

      Zur Herstellung einer SSH-Verbindung müssen Sie eine leere Datei auf Ihrer MicroSD-Karte erstellen und ihr den Namen `ssh` zuordnen. Speichern Sie diese Datei auf Ihrer Karte im Ordner auf Stammverzeichnisebene. Die Einbindung dieser Datei ermöglicht Ihnen die Herstellung einer Verbindung zu Ihrer Einheit mithilfe der Standardberechtigungsnachweise. 

   4. Entfernen Sie die MicroSD-Karte. Vergewissern Sie sich, dass die Karte sicher aus der Einheit entfernt wurde, die Sie zur Bearbeitung der Karte verwendet haben, um sicherzustellen, dass alle Änderungen geschrieben wurden.

   5. Legen Sie die MicroSD-Karte in Ihre Raspberry Pi-Einheit ein. Schließen Sie die optionale Sensorenhardware an und verbinden Sie die Einheit mit der Stromversorgung.

   6. Starten Sie die Einheit.

   7. Ändern Sie das Standardkennwort Ihrer Einheit. In Raspbian-Flash-Images verwendet das Standardkonto den Anmeldenamen `pi` und das Standardkennwort `raspberry`.

      Melden Sie sich bei diesem Konto an. Benutzen Sie den standardmäßigen {{site.data.keyword.linux_notm}}-Befehl `passwd`, um das Standardkennwort zu ändern:

      ```
      passwd       Enter new UNIX password:  
      Retype new UNIX password:        passwd: password updated successfully
      ```
      {: codeblock}
     
   8. Installieren Sie die neueste Docker-Version auf Ihrer Einheit. Weitere Informationen finden Sie unter [Install Docker](https://docs.docker.com/engine/install/debian/). 

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
* (Optional) Sensorenhardware: Zahlreiche {{site.data.keyword.horizon}}-Edge-Services benötigen spezialisierte Sensorenhardware.

### Vorgehensweise
{: #proc-nvidia}

1. Bereiten Sie die NVIDIA Jetson-Einheit vor.
   1. Installieren Sie das neueste NVIDIA JetPack auf Ihrer Einheit. Weitere Informationen finden Sie im folgenden Abschnitt:
      * (TX1) [Jetson TX1](https://elinux.org/Jetson_TX1)
      * (TX2) [KI mit dem Jetson TX2 Developer Kit in der Peripherie nutzen](https://developer.nvidia.com/embedded/jetson-tx2-developer-kit)
      * (Nano) [Erste Schritte mit Jetson Nano Developer Kit](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit)

      Sie müssen diese Software und alle vorausgesetzten Softwarekomponenten installieren, bevor Sie die {{site.data.keyword.horizon}}-Software installieren.

   2. Ändern Sie das Standardkennwort. In der JetPack-Installationsprozedur verwendet das Standardkonto den Anmeldenamen `nvidia` und das Standardkennwort `nvidia`. 

      Melden Sie sich bei diesem Konto an. Benutzen Sie den standardmäßigen {{site.data.keyword.linux_notm}}-Befehl `passwd`, um das Standardkennwort zu ändern:

      ```
      passwd       Enter new UNIX password:  
      Retype new UNIX password:        passwd: password updated successfully
      ```
      {: codeblock}
      
   3. Installieren Sie die neueste Docker-Version auf Ihrer Einheit. Weitere Informationen finden Sie unter [Install Docker](https://docs.docker.com/engine/install/debian/). 

Ihre Edge-Einheit ist jetzt vorbereitet. Fahren Sie fort mit [Agent installieren](registration.md).

## {{site.data.keyword.macOS_notm}}
{: #mac-os-x}

### Hardwarevoraussetzungen
{: #hard-req-mac}

* {{site.data.keyword.intel}}-Mac-Einheit ab 2010 mit 64-Bit-Architektur
* MMU-Virtualisierung (erforderlich)
* Mac OS X Version 10.11 ("El Capitan") oder höher
* Internetverbindung für Ihre Maschine (kabelgebunden oder WiFi)
* (Optional) Sensorenhardware: Zahlreiche {{site.data.keyword.horizon}}-Edge-Services benötigen spezialisierte Sensorenhardware.
### Vorgehensweise
{: #proc-mac}

1. Bereiten Sie die Einheit vor.
   1. Installieren Sie die neueste Docker-Version auf Ihrer Einheit. Weitere Informationen finden Sie unter [Install Docker](https://docs.docker.com/docker-for-mac/install/).

   2. **Installieren Sie 'socat'**. Sie können eine der folgenden Methoden verwenden, um 'socat' zu installieren:

      * [Verwenden Sie Homebrew, um Socat zu installieren](https://brewinstall.org/install-socat-on-mac-with-brew/).
   
      * Wenn bereits MacPorts installiert sind, können Sie MacPorts wie folgt zum Installieren von 'socat' verwenden:
        ```
        sudo port install socat
        ```
        {: codeblock}

## Weitere Schritte

* [Agent installieren](registration.md)
* [Agent aktualisieren](updating_the_agent.md)

## Zugehörige Informationen

* [Installation von {{site.data.keyword.ieam}}](../hub/online_installation.md)
* [Erweiterte manuelle Installation und Registrierung eines Agenten](advanced_man_install.md)
