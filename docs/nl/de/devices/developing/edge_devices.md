---

copyright:
years: 2020
lastupdated: "2020-4-8"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Edge-Einheiten
{: #edge_devices}

# Vorbereitende Schritte

Für die Arbeit mit Edge-Einheiten müssen Sie die folgenden Voraussetzungen kennen:

* [Edge-Einheit vorbereiten](#adding-devices)
* [Unterstützte Architekturen und Betriebssysteme](#suparch-horizon)
* [Dimensionierung](#size)

Hinweis: Edge-Einheiten werden auch als Agenten bezeichnet. Eine Beschreibung von Edge-Einheiten und Clustern finden Sie unter HINWEIS FÜR AUTOR.

## Edge-Einheit vorbereiten
{: #adding-devices}

{{site.data.keyword.edge_devices_notm}} verwendet die Projektsoftware [{{site.data.keyword.horizon_open}} ![Wird in einer neuen Registerkarte geöffnet](../../images/icons/launch-glyph.svg "Wird in einer neuen Registerkarte geöffnet")](https://github.com/open-horizon/). Die {{site.data.keyword.horizon_agents}} auf Ihren Edge-Einheiten kommunizieren mit anderen {{site.data.keyword.horizon}}-Komponenten, um so die sichere Orchestrierung des Software-Lifecycle-Managements auf den Einheiten durchzuführen.
{:shortdesc}

Im folgenden Diagramm sind die typischen Interaktionen zwischen den Komponenten in {{site.data.keyword.horizon}} dargestellt.

<img src="../../images/edge/installers.svg" width="90%" alt="Interaktion der Komponenten in {{site.data.keyword.horizon}}">

Daher muss die {{site.data.keyword.horizon_agent}}-Software  für alle Edge-Einheiten (Edge-Knoten) installiert sein. Der {{site.data.keyword.horizon_agent}} ist darüber hinaus von der [Docker-Software ![Wird in einer neuen Registerkarte geöffnet](../../images/icons/launch-glyph.svg "Wird in einer neuen Registerkarte geöffnet")](https://www.docker.com/) abhängig.  

Das folgende Diagramm konzentriert sich auf die Edge-Einheit und zeigt den Ablauf der Schritte zum Einrichten der Edge-Einheit sowie die Funktionen des Agenten nach seinem Start an. 

<img src="../../images/edge/registration.svg" width="80%" alt="{{site.data.keyword.horizon_exchange}}, Agbots und Agenten">

Die folgenden Anweisungen führen Sie durch den Prozess zur Installation der erforderlichen Software auf Ihrer Edge-Einheit und zur Registrierung der Edge-Einheit bei {{site.data.keyword.edge_devices_notm}}. 

## Unterstützte Architekturen und Betriebssysteme
{: #suparch-horizon}

{{site.data.keyword.edge_devices_notm}} unterstützt Systeme mit den folgenden Hardwarearchitekturen: 

* {{site.data.keyword.linux_bit_notm}}-Einheiten oder virtuelle Maschinen, auf denen 18.x (Bionic), Ubuntu 16.x (Xenial), Debian 10 (Buster) oder Debian 9 (Stretch) ausgeführt wird
* {{site.data.keyword.linux_notm}} on ARM (32-Bit); beispielsweise Raspberry Pi, auf denen Raspbian Buster oder Stretch ausgeführt wird
* {{site.data.keyword.linux_notm}} on ARM (64-Bit); beispielsweise NVIDIA Jetson Nano, TX1 oder TX2, auf denen Ubuntu 18.x (Bionic) ausgeführt wird
* {{site.data.keyword.macOS_notm}}

## Dimensionierung
{: #size}

Für den Agenten bestehen die folgenden Voraussetzungen: 

1. 100 MB Arbeitsspeicher (einschließlich Docker). Darüber hinaus sind pro Vereinbarung (Agreement) weitere 100 KB Arbeitsspeicher (RAM) erforderlich, sowie zusätzlicher Hauptspeicher für Workloads, die auf dem Knoten ausgeführt werden. 
2. 400 MB Plattenspeicherplatz (einschließlich Docker). Darüber hinaus ist abhängig von der Größe der von Workloads verwendeten Container-Images und der Größe der im Knoten bereitgestellten Modellobjekte (multipliziert mit 2) zusätzlicher Plattenspeicherplatz erforderlich. 

## Weitere Schritte

[Agent installieren](installing_the_agent.md)
