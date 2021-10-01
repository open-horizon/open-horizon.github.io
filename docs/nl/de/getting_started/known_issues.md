---

copyright:
  years: 2019, 2020
lastupdated: "2021-08-31"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Bekannte Probleme und Einschränkungen  
{: #knownissues}

Dies sind bekannte Probleme und Einschränkungen für {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}).

Die vollständige Liste der ungelösten Probleme für die {{site.data.keyword.ieam}}-OpenSource-Ebene finden Sie in den GitHub-Problemen der einzelnen [Open Horizon-Repositories](https://github.com/open-horizon/).

{:shortdesc}

## Bekannte Probleme für {{site.data.keyword.ieam}} {{site.data.keyword.version}}

Dies sind bekannte Probleme und Einschränkungen für {{site.data.keyword.ieam}} {{site.data.keyword.version}}.

* {{site.data.keyword.ieam}} führt keine Malware- oder Virenprüfung für Daten aus, die in das Modellverwaltungssystem (MMS) hochgeladen werden. Weitere Informationen zur MMS-Sicherheit finden Sie unter [Sicherheit und Datenschutz](../OH/docs/user_management/security_privacy.md#malware).

* Das Flag **-f &lt;verzeichnis&gt;** von **edgeNodeFiles.sh** hat nicht die beabsichtigte Wirkung. Stattdessen werden die Dateien im aktuellen Verzeichnis erfasst. Details hierzu finden Sie in den Informationen zu [Problem Nr. 2187](https://github.com/open-horizon/anax/issues/2187). Die Problemumgehung besteht darin, den Befehl wie folgt auszuführen:

   ```bash
   (cd <dir> && edgeNodeFiles.sh ... )
   ```
   {: codeblock}



* Als Teil der {{site.data.keyword.ieam}}-Installation wurden je nach Version von {{site.data.keyword.common_services}} Zertifikate möglicherweise mit einer kurzen Lebensdauer erstellt, die zu ihrer automatischen Verlängerung führt. Möglicherweise stoßen Sie auf die folgenden Zertifikatsprobleme ([die mit diesen Schritten gelöst werden können](cert_refresh.md)):
  * Es wird eine unerwartete JSON-Ausgabe mit der Nachricht "Request failed with status code 502" angezeigt, wenn auf die {{site.data.keyword.ieam}}-Managementkonsole zugegriffen wird.
  * Edge-Knoten werden nicht aktualisiert, wenn ein Zertifikat erneuert wird, und müssen manuell aktualisiert werden, um eine erfolgreiche Kommunikation mit dem {{site.data.keyword.ieam}}-Hub zu gewährleisten.

* Bei Verwendung von {{site.data.keyword.ieam}} mit lokalen Datenbanken, wenn der Pod **cssdb** gelöscht und entweder manuell oder automatisch über den Kubernetes-Scheduler erneut erstellt wird, führt dies zu einem Datenverlust für die Mongo-Datenbank. Führen Sie die Schritte in der Dokumentation [Sicherung und Wiederherstellung](../admin/backup_recovery.md) durch, um den Datenverlust zu verhindern.

* Bei Verwendung von {{site.data.keyword.ieam}} mit lokalen Datenbanken, wenn die Jobressourcen **create-agbotdb-cluster** oder **create-exchangedb-cluster** gelöscht werden, wird der Job erneut ausgeführt und initialisiert die entsprechende Datenbank erneut, was zu Datenverlust führt. Führen Sie die Schritte in der Dokumentation [Sicherung und Wiederherstellung](../admin/backup_recovery.md) durch, um den Datenverlust zu verhindern.

* Wenn lokale Datenbanken verwendet werden, kann es vorkommen, dass mindestens eine der Postgres-Datenbanken nicht mehr reagiert. Um dies zu beheben, müssen Sie alle Sentinels und Proxys für die nicht reagierende Datenbank erneut starten. Ändern Sie die Befehle `oc rollout restart deploy <CR_NAME>-<agbot|exchange>db-sentinel` und `oc rollout restart deploy <CR_NAME>-<agbot|exchange>db-proxy` (Beispiel für Exchange-Sentinel: `oc rollout restart deploy ibm-edge-exchangedb-sentinel`) und führen Sie sie mit der betroffenen Anwendung und Ihrer angepassten Ressource aus.

* Wenn Sie **hzn service log** unter {{site.data.keyword.rhel}} mit einer beliebigen Architektur ausführen, blockiert der Befehl. Weitere Informationen finden Sie unter [Ausgabe 2826](https://github.com/open-horizon/anax/issues/2826). Um diese Bedingung zu umgehen, rufen Sie die Containerprotokolle ab (Sie können auch -f für den Nachsatz angeben):

   ```
   Docker-Protokolle &amp;TWBLT; Container &gt;
   ```
   {: codeblock}


## Einschränkungen für {{site.data.keyword.ieam}} {{site.data.keyword.version}}

* Die Produktdokumentation zu {{site.data.keyword.ieam}} wurde für beteiligte Ländergruppen übersetzt, die englische Version wird jedoch kontinuierlich aktualisiert. Je nach Übersetzungszyklen kann es zu Abweichungen zwischen englischer und landessprachlicher Version kommen. Überprüfen Sie anhand der englischen Version, ob möglicherweise vorhandene Abweichungen nach der Veröffentlichung der landessprachlichen Versionen behoben wurden.

* Wenn Sie das Attribut **owner** oder **public** von Services, Mustern oder Bereitstellungsrichtlinien in Exchange ändern, kann es bis zu fünf Minuten dauern, bis Sie auf diese Ressourcen zugreifen können, um die Änderung anzuzeigen. Auch wenn Sie einem Exchange-Benutzer die Administratorberechtigung erteilen, kann es bis zu fünf Minuten dauern, bis diese Änderung an alle Exchange-Instanzen weitergeben wurde. Diese Zeitdauer kann verkürzt werden, indem Sie den Parameter `api.cache.resourcesTtlSeconds` in der Datei `config.json` des Exchange auf einen niedrigeren Wert einstellen (der Standardwert ist 300 Sekunden). Dadurch wird allerdings die Leistung geringfügig beeinträchtigt.

* Der Agent unterstützt nicht das [Model Management System](../developing/model_management_system.md) (MMS) für abhängige Services.

* Die Bindung für den geheimen Schlüssel funktioniert nicht für einen vereinbarungslosen Service, der in einem Muster definiert wurde.
 
* Der Edge-Cluster-Agent unterstützt K3S v1.21.3+k3s1 nicht, da das angehängte Datenträgerverzeichnis nur die 0700-Berechtigung hat. Informationen zu einer temporären Lösung finden Sie unter [Kann Daten nicht in lokales PVC schreiben](https://github.com/k3s-io/k3s/issues/3704) .
 
* Jeder {{site.data.keyword.ieam}} Edge Node Agent initiiert alle Netzverbindungen mit dem {{site.data.keyword.ieam}} Management Hub. Das Management-Hub leitet keine Verbindungen zu seinen Edge-Knoten ein. Daher kann ein Edge-Knoten hinter einer NAT-Firewall stehen, wenn die Firewall TCP-Konnektivität zu dem Management-Hub hat. Die Edge-Knoten können derzeit jedoch nicht über einen SOCKS-Proxy mit dem Management-Hub kommunizieren.
  
* Die Installation von Edge-Einheiten mit Fedora oder SuSE wird nur bei der Methode der  [erweiterten manuellen Agenteninstallation und -registrierung](../installing/advanced_man_install.md) unterstützt.
