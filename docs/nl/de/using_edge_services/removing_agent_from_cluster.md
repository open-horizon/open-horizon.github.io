---

copyright:
years: 2020
lastupdated: "2020-8-25"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Agenten in Edge-Cluster entfernen
{: #remove_agent}

Führen Sie die folgenden Schritte aus, um die Registrierung eines Edge-Clusters aufzuheben und den {{site.data.keyword.ieam}}-Agenten in dem betreffenden Cluster zu entfernen:

1. Extrahieren Sie das Script **agent-uninstall.sh** aus der TAR-Datei:

   ```bash
   tar -zxvf agentInstallFiles-x86_64-Cluster.tar.gz agent-uninstall.sh
   ```
   {: codeblock}

2. Exportieren Sie Ihre Benutzerberechtigungsnachweise für Horizon Exchange:

   ```bash
   export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-schlüssel>
   ```
   {: codeblock}

3. Entfernen Sie den Agenten:

   ```bash
   ./agent-uninstall.sh -u $HZN_EXCHANGE_USER_AUTH -d
   ```
   {: codeblock}

Hinweis: Das Löschen des Namensbereichs führt gelegentlich zu einer Blockierung im Beendigungsstatus (Terminating). In dieser Situation finden Sie Informationen zum manuellen Löschen des Namespace unter [Ein Namensraum steckt im Status Beendigung fest](https://www.ibm.com/support/knowledgecenter/SSBS6K_3.1.1/troubleshoot/ns_terminating.html).
