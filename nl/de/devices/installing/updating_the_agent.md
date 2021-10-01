---

copyright:
years: 2020
lastupdated: "2020-2-2"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Agent aktualisieren
{: #updating_the_agent}

Wenn Sie aktualisierte {{site.data.keyword.edge_notm}}-Agentenpakete ({{site.data.keyword.ieam}}-Agentenpakete) erhalten haben, können Sie Ihre Edge-Einheit einfach aktualisieren:

1. Führen Sie die Schritte im Abschnitt [Erforderliche Informationen und Dateien für Edge-Einheiten zusammenstellen](../../hub/gather_files.md#prereq_horizon) aus, um die aktualisierte Datei **agentInstallFiles-&lt;edge-einheitentyp&gt;.tar.gz** mit den neueren Agentenpaketen zu erstellen.
  
2. Führen Sie für jede Edge-Einheit die Schritte in [Automatisierte Agenteninstallation und -registrierung](automated_install.md#method_one), abgesehen von der folgenden Angabe, aus. Geben Sie beim Befehl **agent-install.sh** den Service und das Muster bzw. die Richtlinie an, die auf der Edge-Einheit ausgeführt werden sollen.
