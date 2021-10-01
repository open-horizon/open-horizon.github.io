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

[SDO](https://software.intel.com/en-us/secure-device-onboard) (Secure Device Onboard), das von Intel erstellt wurde, macht es einfach und sicher, Edge-Einheiten zu konfigurieren und mit einem Edge-Management-Hub zu verknüpfen. {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) unterstützt SDO-fähige Einheiten, sodass der Agent auf den Einheiten installiert und beim {{site.data.keyword.ieam}}-Management-Hub registriert wird, ohne dass dazu spezielle Maßnahmen erforderlich sind. Die Einheiten müssen dazu lediglich eingeschaltet werden.

## SDO im Überblick
{: #sdo-overview}

Zu SDO gehören die folgenden Komponenten:

* Das SDO-Modul auf der Edge-Einheit (wird normalerweise vom Gerätehersteller installiert)
* Ein Eigentumsnachweis (eine Datei, die dem Einheitenkäufer mit der physischen Einheit übergeben wird)
* Der SDO-Rendezvous-Server (der Server, den eine SDO-fähige Einheit standardmäßig beim ersten Starten kontaktiert)
* SDO-Eignerservices (Services, die auf dem {{site.data.keyword.ieam}}-Management-Hub ausgeführt werden und die Einheit für die Verwendung der jeweiligen {{site.data.keyword.ieam}}-Instanz konfigurieren)

**Hinweis:** SDO unterstützt nur Edge-Einheiten und keine Edge-Cluster.

### Ablauf bei SDO

<img src="../OH/docs/images/edge/09_SDO_device_provisioning.svg" style="margin: 3%" alt="SDO installation overview">

## Vorbereitende Schritte
{: #before_begin}

Für SDO ist es erforderlich, dass die Agentendateien in {{site.data.keyword.ieam}} Cloud Sync Service (CSS) gespeichert werden. Ist dies noch nicht geschehen, bitten Sie Ihren Administrator, einen der folgenden Befehle wie unter [Edge-Knotendateien zusammenstellen](../hub/gather_files.md) beschrieben auszuführen:

  `edgeNodeFiles.sh ALL -c ...`

## SDO ausprobieren
{: #trying-sdo}

Bevor Sie SDO-fähige Edge-Einheiten erwerben, können Sie die SDO-Unterstützung in {{site.data.keyword.ieam}} mit einer VM testen, die eine SDO-fähiges Einheit simuliert:

1. Sie benötigen einen API-Schlüssel. Anweisungen zum Erstellen eines API-Schlüssels finden Sie unter [API-Schlüssel erstellen](../hub/prepare_for_edge_nodes.md), wenn Sie nicht bereits über einen API-Schlüssel verfügen.

2. Erfragen Sie bei Ihrem {{site.data.keyword.ieam}}-Administrator die Werte für die folgenden Umgebungsvariablen. (Sie benötigen sie im nächsten Schritt.)

   ```bash
   export HZN_ORG_ID=<exchange-organisation>    export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-schlüssel>    export HZN_SDO_SVC_URL=https://<ieam-management-hub-ingress>/edge-sdo-ocs/api    export HZN_MGMT_HUB_CERT_PATH=<pfad_zum_selbst_signierten_zertifikat_des_management-hubs>    export CURL_CA_BUNDLE=$HZN_MGMT_HUB_CERT_PATH
   ```

3. Befolgen Sie die Schritte im [open-horizon/SDO-Support-Repository](https://github.com/open-horizon/SDO-support/blob/master/README-1.10.md), um zu beobachten, ob SDO den {{site.data.keyword.ieam}}-Agenten auf einer Einheit automatisch installiert und mit Ihrem {{site.data.keyword.ieam}}-Management-Hub registriert.

## SDO-fähige Einheiten zu Ihrer {{site.data.keyword.ieam}}-Domäne hinzufügen
{: #using-sdo}

Gehen Sie folgendermaßen vor, wenn Sie SDO-fähige Einheiten erworben haben und sie in Ihre {{site.data.keyword.ieam}}-Domäne integrieren wollen:

1. [Melden Sie sich an der {{site.data.keyword.ieam}} Managementkonsole](../console/accessing_ui.md)an.

2. Klicken Sie auf der Registerkarte **Knoten** auf **Knoten hinzufügen**. 

   Geben Sie die Informationen ein, die erforderlich sind, um einen privaten Eigentumsschlüssel im SDO-Service zu erstellen, und laden Sie den entsprechenden öffentlichen Schlüssel herunter.
   
3. Geben Sie die erforderlichen Informationen ein, um die Eigentumsnachweise (Ownership Vouchers) zu importieren, die Sie beim Kauf der Einheiten erhalten haben.

4. Verbinden Sie die Einheiten mit dem Netz und schalten Sie sie ein.

5. Sehen Sie sich in der Managementkonsole den Fortschritt der Einheiten an, wenn sie online sind, indem Sie die Übersichtsseite **Knoten** anzeigen und den Installationsnamen filtern.
