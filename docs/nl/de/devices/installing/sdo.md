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

# SDO-Agenteninstallation und -registrierung
{: #sdo}

**Technologievorschau**: Derzeit sollte die SDO-Unterstützung ausschließlich zum Testen des SDO-Prozesses sowie zur Planung für das Produkt bei einer beabsichtigten zukünftigen Verwendung genutzt werden. In einem künftigen Release wird die SDO-Unterstützung für den Produktionseinsatz verfügbar sein.

Bei [SDO ![Wird in einer neuen Registerkarte geöffnet](../../images/icons/launch-glyph.svg "Wird in einer neuen Registerkarte geöffnet")](https://software.intel.com/en-us/secure-device-onboard) (Secure Device Onboard) handelt es sich um eine Technologie, die von Intel für eine einfache und sichere Konfiguration von Edge-Einheiten und die Zuordnung der Einheiten zu einem Management-Hub geschaffen wurde. In {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) wurde nun die Unterstützung für SDO-fähige Einheiten hinzugefügt, sodass der Agent auf der Einheit installiert und beim {{site.data.keyword.ieam}}-Management-Hub registriert wird, ohne dass dazu spezielle Maßnahmen erforderlich sind. Die Einheit muss dazu lediglich eingeschaltet werden.

## SDO im Überblick
{: #sdo-overview}

Zu SDO gehören die folgenden vier Komponenten:

1. Das SDO-Modul auf der Edge-Einheit (wird normalerweise vom Gerätehersteller installiert)
2. Ein Eigentumsnachweis (eine Datei, die dem Einheitenkäufer mit der physischen Einheit übergeben wird)
3. Der SDO-Rendezvous-Server (der Server, den ein SDO-fähiges Gerät standardmäßig beim ersten Booten kontaktiert)
4. SDO-Eignerservices (Services, die mit dem {{site.data.keyword.ieam}}-Management-Hub, der die Einheit mit der jeweiligen {{site.data.keyword.ieam}}-Instanz verbindet, ausgeführt werden)

### Unterschiede bei der Technologievorschau
{: #sdo-tech-preview-differences}

- **SDO-fähige Einheit:** Für SDO-Tests wird ein Script bereitgestellt, um das SDO-Modul zu einer VM hinzuzufügen, sodass sich das Modul beim Booten wie eine SDO-fähige-Einheit verhält. Auf diese Weise können Sie die SDO-Integration mit {{site.data.keyword.ieam}} testen, ohne eine SDO-fähige Einheit zu erwerben.
- **Eigentumsnachweis:** Normalerweise erhalten Sie von dem Gerätehersteller einen Eigentumsnachweis. Wenn Sie das im vorherigen Punkt erwähnte Script verwenden, um das SDO-Modul zu einer VM hinzuzufügen, wird auch ein Eigentumsnachweis in der VM erstellt. Das Kopieren dieses VM-Nachweises entspricht dem Erhalt eines Eigentumsnachweises vom Gerätehersteller.
- **Rendezvous-Server:** In einer Produktionsumgebung würde die Booteinheit eine Verbindung zum globalen SDO-Rendezvous-Server von Intel herstellen. Für Entwicklungs- und Testzwecke in Verbindung mit der vorliegenden Technologievorschau verwenden Sie einen Rendezvous-Entwicklungsserver, auf dem die SDO-Eignerservices ausgeführt werden.
- **SDO-Eignerservices:** In dieser Technologievorschau werden die SDO-Eignerservices nicht automatisch auf dem {{site.data.keyword.ieam}}-Management-Hub installiert. Es wird stattdessen ein benutzerfreundliches Script zum Starten der SDO-Eignerservices auf einem beliebigen Server bereitgestellt, der über einen Netzzugriff auf den {{site.data.keyword.ieam}}-Management-Hub verfügt und für die SDO-Einheiten über das Netz zugänglich ist.

## SDO verwenden
{: #using-sdo}

Gehen Sie zum Ausprobieren von SDO und zum Verfolgen der automatischen Installation und Registrierung des {{site.data.keyword.ieam}}-Agenten bei Ihrem {{site.data.keyword.ieam}}-Management-Hub wie in der [Readme-Datei im Repository unter 'open-horizon/SDO-support' ![Wird in einer neuen Registerkarte geöffnet](../../images/icons/launch-glyph.svg "Wird in einer neuen Registerkarte geöffnet")](https://github.com/open-horizon/SDO-support/blob/master/README.md) beschrieben vor.
