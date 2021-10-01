---

copyright:
  years: 2020
lastupdated: "2020-5-11"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 'cloudctl', 'kubectl' und 'oc' installieren
{: #cloudctl_oc_cli}

Mit den hier beschriebenen Schritten können Sie die Befehlszeilentools installieren, die zur Verwaltung bestimmter Aspekte des Management-Hubs und der Edge-Cluster von {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) benötigt werden.

## cloudctl

1. Öffnen Sie in einem Browser die Webbenutzerschnittstelle von {{site.data.keyword.ieam}} mit der Adresse `https://<CLUSTER_URL>/common-nav/cli`.

2. Erweitern Sie den Abschnitt für die **IBM Cloud Pak-CLI** und wählen Sie Ihr **Betriebssystem** aus.

3. Kopieren Sie den angezeigten **curl**-Befehl und führen Sie ihn aus, um die Binärdatei für **cloudctl** herunterzuladen.

4. Machen Sie die Datei ausführbar und verschieben Sie sie an die Position **/usr/local/bin**:
  
   ```bash
   chmod 755 cloudctl-*    sudo mv cloudctl-* /usr/local/bin/cloudctl
   ```
   {: codeblock}

5. Vergewissern Sie sich, dass **/usr/local/bin** in Ihrer PATH-Angabe enthalten ist und prüfen Sie anschließend, ob **cloudctl** funktioniert:
  
   ```bash
   cloudctl --help
   ```
   {: codeblock}

## oc

1. Laden Sie die {{site.data.keyword.open_shift_cp}}-CLI-tar-Datei von [OpenShift-Client-CLI (oc)](https://mirror.openshift.com/pub/openshift-v4/clients/ocp/latest/) herunter. Wählen Sie die für Ihr Betriebssystem geeignete Datei **openshift-client-\*-\*.tar.gz** aus.

2. Wechseln Sie an die Position der heruntergeladenen TAR-Datei und entpacken Sie sie:
  
   ```bash
   tar -zxvf openshift-client-*-*.tar.gz
   ```
   {: codeblock}

3. Verschieben Sie den Befehl **oc** in das Verzeichnis **/usr/local/bin**:
  
   ```bash
   sudo mv oc /usr/local/bin/
   ```
   {: codeblock}

4. Vergewissern Sie sich, dass **/usr/local/bin** in Ihrer PATH-Angabe enthalten ist und prüfen Sie, ob **oc** funktioniert:
  
   ```bash
   oc --help
   ```
   {: codeblock}

Alternativ können Sie [homebrew](https://brew.sh/) verwenden, um **oc** unter {{site.data.keyword.macOS_notm}} zu installieren:
  
   ```bash
   brew install openshift-cli
   ```
   {: codeblock}

## Kubectl

Befolgen Sie die Anweisungen in [kubectl installieren und konfigurieren](https://kubernetes.io/docs/tasks/tools/install-kubectl/).
