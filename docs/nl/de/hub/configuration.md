---

copyright:
  years: 2020
lastupdated: "2020-10-28"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# {{site.data.keyword.ieam}} konfigurieren

## Konfiguration der angepassten Ressource 'EamHub'
{: #cr}

Die Hauptkonfiguration für {{site.data.keyword.ieam}} erfolgt über die angepasste Ressource 'EamHub', insbesondere über das Feld **spec** dieser angepassten Ressource.

In diesem Dokument wird Folgendes vorausgesetzt:
* Der Namensbereich, für den Sie diese Befehle ausführen, stellt die Position dar, an der der Operator für den {{site.data.keyword.ieam}}-Management-Hub bereitgestellt wird.
* Der Name der angepassten EamHub-Ressource lautet standardmäßig **ibm-edge**. Wenn Sie einen anderen Namen verwenden wollen, dann ändern Sie die Befehle und ersetzen Sie **ibm-edge** durch den gewünschten Wert.
* Die Binärdatei **jq** wird installiert, damit Ausgabe garantiert in einem lesbaren Format angezeigt wird.


Die mit **spec** definierte Standardspezifikation ist minimal und enthält lediglich die Lizenzannahme; Sie können sie mit dem folgenden Befehl anzeigen:
```
$ oc get eamhub ibm-edge -o yaml ... spec:   license:     accept: true ...
```

### Operatorsteuerschleife
{: #loop}

Der Operator für den {{site.data.keyword.ieam}}-Management-Hub wird in einer fortlaufenden idempotenten Schleife ausgeführt, um den aktuellen Status von Ressourcen mit dem erwarteten Status von Ressourcen zu synchronisieren.

Aufgrund dieser fortlaufenden Schleife müssen Sie zwei Dinge wissen, wenn Sie versuchen, Ihre vom Operator verwalteten Ressourcen zu konfigurieren:
* Alle Änderungen an der angepassten Ressource werden von der Steuerschleife asynchron gelesen. Nachdem Sie die Änderung durchgeführt haben, kann es einige Minuten dauern, bis diese Änderung durch den Operator umgesetzt wird.
* Jede manuelle Änderung, die an einer vom Operator gesteuerten Ressource vorgenommen wird, kann durch den Operator bei Durchsetzung eines bestimmten Status überschrieben (also rückgängig gemacht) werden. 

Behalten Sie die Operatorpodprotokolle im Blick, um diese Schleife zu überwachen:
```
oc logs $(oc get pods | grep ibm-eamhub-operator | awk '{print $1}') --tail 20 -f
```
{: codeblock}

Wenn eine Schleife beendet ist, generiert sie eine Zusammenfassung namens **PLAY RECAP**. Mit dem folgenden Befehl können Sie die neueste Zusammenfassung anzeigen:
```
oc logs $(oc get pods | grep ibm-eamhub-operator | awk '{print $1}') --tail 5000 | grep -A 1 '^PLAY RECAP' | tail -n 1
```
{: codeblock}

Die folgende Ausgabe zeigt eine Schleife, die ohne stattgefundene Operationen beendet wurde (im aktuellen Status ist für **PLAY RECAP** immer **changed=1** angegeben):
```
$ oc logs $(oc get pods | grep ibm-eamhub-operator | awk '{print $1}') --tail 5000 | grep -A 1 '^PLAY RECAP' | tail -n 1 localhost                  : ok=51   changed=1    unreachable=0    failed=0    skipped=11   rescued=0    ignored=0
```
{: codeblock}

Achten Sie bei Konfigurationsänderungen auf die drei folgenden Felder:
* **changed**: Ein größerer Wert als **1** gibt an, dass der Operator eine Task ausgeführt hat, die den Status von einer oder mehreren Ressourcen geändert hat (dies könnte auf Ihre Anforderung hin durch eine Änderung der angepassten Ressource oder über die Zurücksetzung einer manuell vorgenommenen Änderung durch den Operator verursacht worden sein).
* **rescued**: Eine Task ist fehlgeschlagen. Es handelt sich jedoch um einen bekannten möglichen Fehler und der Taskversuch wird in der nächsten Schleife wiederholt.
* **failed**: Bei der Erstinstallation sind einige erwartete Fehler aufgetreten. Falls derselbe Fehler wiederholt angezeigt wird und die Nachricht nicht gelöscht (oder ausgeblendet) wird, deutet dies aller Wahrscheinlichkeit nach auf ein Problem hin.

### Allgemeine Konfigurationsoptionen für EamHub

Es können verschiedene Änderungen an der Konfiguration vorgenommen werden. Einige Änderungen sind jedoch wahrscheinlicher als andere. In diesem Abschnitt sind einige der gängigeren Einstellungen beschrieben.

| Konfigurationswert | Standardwert | Beschreibung |
| :---: | :---: | :---: |
| Globale Werte | -- | -- |
| pause_control_loop | false | Hält die oben beschriebene Steuerschleife an, damit für ein Debug vorübergehend manuelle Änderungen vorgenommen werden können. Wird nicht für einen stabilen Zustand verwendet. |
| ieam_maintenance_mode | false | Setzt alle Podreplikatzähler ohne persistenten Speicher auf 0. Wird zur Wiederherstellung von Sicherungen verwendet. |
| ieam_local_databases | true | Aktiviert oder inaktiviert lokale Datenbanken. Ein Wechsel zwischen den Statuswerten wird nicht unterstützt. Weitere Informationen enthält der Abschnitt [Konfiguration von fernen Datenbanken](./configuration.md#remote). |
| ieam_database_HA | true | Aktiviert oder inaktiviert den Hochverfügbarkeitsmodus für lokale Datenbanken. Hierdurch wird der Replikatzähler für alle Datenbankpods auf **3** gesetzt (bei Verwendung des Wertes **true**) bzw. auf **1** (bei Verwendung von **false**). |
| hide_sensitive_logs | true | Blendet Operatorprotokolle mit Bezug auf die Einstellung für **geheime Kubernetes-Schlüssel** aus. Eine Verwendung des Wertes **false** kann Fehler verursachen, weil der Operator verschlüsselte Authentifizierungswerte protokolliert. |
| storage_class_name | "" | Verwendet die Standardspeicherklasse, wenn sie nicht festgelegt ist. |
| ieam_enable_tls | false | Aktiviert oder deaktiviert interne TLS für den Datenverkehr zwischen {{site.data.keyword.ieam}} -Komponenten. **Vorsicht:** Wenn die Standardkonfiguration für den Austausch, die CSS-oder die Vault-Konfiguration überschrieben wird, muss die TLS-Konfiguration in der Konfigurationsüberschreibung manuell geändert werden. |
| ieam_local_secrets_manager | true | Aktiviert oder deaktiviert die lokale Secrets Manager-Komponente (Vault). |


### Konfigurationsoptionen für EamHub-Komponentenskalierung

| Komponentenskalierungswert | Standardanzahl der Replikate | Beschreibung |
| :---: | :---: | :---: |
| exchange_replicas | 3 | Die Standardanzahl der Replikate für den Austausch. Wenn Sie die Standardaustauschkonfiguration überschreiben (exchange_config), **muss maxPoolSize** manuell mit dieser Formel `((exchangedb_max_connections-8)/exchange_replikate)` angepasst werden |
| css_replicas | 3 | Die Standardanzahl der Replikate für das CSS. |
| ui_replicas | 3 | Die Standardanzahl der Replikate für die Benutzerschnittstelle. |
| agbot_replicas | 2 | Die Standardanzahl der Replikate für den agbot. Wenn Sie die Standardagbot-Konfiguration (agbot_config) überschreiben, muss **MaxOpenConnections** manuell mit dieser Formel `((agbotdb_max_connections-8)/agbot_replikate)` angepasst werden |


### Optionen für die Ressourcenkonfiguration der eamHub-Komponente

**Hinweis**: Da für Ansible-Operatoren ein verschachteltes Wörterverzeichnis als Ganzes hinzugefügt werden muss, müssen Sie verschachtelte Konfigurationswerte in ihrer Gesamtheit hinzufügen. Ein Beispiel finden Sie unter [Scaling Configuration](./configuration.md#scale) .

<table>
<tr>
<td> Komponentenressourcenwert </td> <td> Standardwert </td> <td> Beschreibung </td>
</tr>
<tr>
<td> exchange_resources </td> 
<td>

```
  exchange_resources: anforderungen: memory: 512Mi cpu: 10m limits: memory: 2Gi cpu: 2
```

</td>
<td>
Die Standardanforderungen und -begrenzungen für den Austausch. 
</td>
</tr>
<tr>
<td> agbot_resources </td> 
<td>

```
  agbot_resources: Zugriffe: Speicher: 64Mi cpu: 10m Limits: Speicher: 2Gi cpu: 2
```

</td>
<td>
Die Standardanforderungen und -begrenzungen für den agbot. 
</td>
</tr>
<tr>
<td> css_resources </td> 
<td>

```
  agbot_resources: Zugriffe: Speicher: 64Mi cpu: 10m Limits: Speicher: 2Gi cpu: 2
```

</td>
<td>
Die Standardanforderungen und -begrenzungen für das CSS. 
</td>
</tr>
<tr>
<td> sdo_resources </td> 
<td>

```
  sdo_resources: Zugriffe: Speicher: 1024Mi cpu: 10m limits: memory: 2Gi cpu: 2
```

</td>
<td>
Die Standardanforderungen und -grenzwerte für SDO. 
</td>
</tr>
<tr>
<td> ui_resources </td> 
<td>

```
  ui_resources: Zugriffe: Speicher: 64Mi cpu: 10m limits: memory: 2Gi cpu: 2
```

</td>
<td>
Die Standardanforderungen und -grenzwerte für die Benutzerschnittstelle. 
</td>
</tr>
<tr>
<td> vault_resources </td> 
<td>

```
  vault_resources: requests: memory: 1024Mi cpu: 10m limits: memory: 2Gi cpu: 2
```

</td>
<td>
Die Standardanforderungen und -grenzwerte für den Secrets Manager. 
</td>
</tr>
<tr>
<td> mongo_resources </td> 
<td>

```
  mongo_resources:limits:  cpu: 2 memory: 2Gi requests: cpu: 100m memory: 256Mi
```

</td>
<td>
Die Standardanforderungen und -grenzwerte für die CSS-Mongo-Datenbank. 
</td>
</tr>
<tr>
<td> postgres_exchangedb_sentinel </td> 
<td>

```
  postgres_exchangedb_sentinel: resources: requests: cpu: "100m" memory: "256Mi" limits: cpu: 1 memory: 1Gi
```

</td>
<td>
Die Standardanforderungen und -grenzen für den Austausch von Postgres-Sentinel. 
</td>
</tr>
<tr>
<td> postgres_exchangedb_proxy </td> 
<td>

```
  postgres_exchangedb_proxy: resources: requests: cpu: "100m" memory: "256Mi" limits: cpu: 1 memory: 1Gi
```

</td>
<td>
Die Standardanforderungen und -grenzwerte für den Exchange-Postgres-Proxy. 
</td>
</tr>
<tr>
<td> postgres_exchangedb_keeper </td> 
<td>

```
  postgres_exchangedb_keeper: resources: requests: cpu: "100m" memory: "256Mi" limits: cpu: 2 memory: 2Gi
```

</td>
<td>
Die Standardanforderungen und -grenzwerte für den Austausch-Postgres-Keeper. 
</td>
</tr>
<tr>
<td> postgres_agbotdb_sentinel </td> 
<td>

```
  postgres_agbotdb_sentinel: resources: requests: cpu: "100m" memory: "256Mi" limits: cpu: 1 memory: 1Gi
```

</td>
<td>
Die Standardanforderungen und -grenzen für die agbot-Postgres-Sentinel. 
</td>
</tr>
<tr>
<td> postgres_agbotdb_proxy </td> 
<td>

```
  postgres_agbotdb_proxy: resources: requests: cpu: "100m" memory: "256Mi" limits: cpu: 1 memory: 1Gi
```

</td>
<td>
Die Standardanforderungen und -grenzen für den agbot-Postgres-Proxy. 
</td>
</tr>
<tr>
<td> postgres_agbotdb_keeper </td> 
<td>

```
  postgres_agbotdb_keeper: resources: requests: cpu: "100m" memory: "256Mi" limits: cpu: 2 memory: 2Gi
```

</td>
<td>
Die Standardanforderungen und -grenzen für den agbot-Postgres-Keeper. 
</td>
</tr>
</table>

### Optionen für die Konfiguration der lokalen Datenbankgröße von EamHub

| Komponentenkonfigurationswert | Standardgröße des persistenten Datenträgers | Beschreibung |
| :---: | :---: | :---: |
| postgres_exchangedb_storage_size | 20 Gi | Größe der Postgres-Austauschdatenbank. |
| postgres_agbotdb_storage_size | 20 Gi | Größe der Postgres-Agbot-Datenbank. |
| mongo_cssdb_storage_size | 20 Gi | Größe der Mongo CSS-Datenbank. |

## Übersetzungskonfiguration für Exchange-API

Sie können die Exchange-API für {{site.data.keyword.ieam}} so konfigurieren, dass Antworten in einer bestimmten Sprache zurückgegeben werden. Definieren Sie dazu eine Umgebungsvariable mit einer unterstützten Sprache (**LANG**) Ihrer Wahl (der Standardwert ist **en**):

```
oc set env deployment <CUSTOM_RESOURCE_NAME>-exchange HZN_EXCHANGE_LANG=<LANG>
```
{: codeblock}

**Hinweis:** Eine Liste der unterstützten Sprachencodes finden Sie in der ersten Tabelle auf der Seite [Unterstützte Sprachen](../getting_started/languages.md).

## Konfiguration von fernen Datenbanken
{: #remote}

**Hinweis:** Ein Wechsel zwischen lokalen und fernen Datenbanken wird nicht unterstützt.

Zur Installation mit fernen Datenbanken erstellen Sie die angepasste Ressource 'EamHub' während der Installation mit dem zusätzlichen Wert im Feld  **spec**:
```
spec:   ieam_local_databases: false   license:     accept: true
```
{: codeblock}

Füllen Sie die folgende Vorlage aus, um einen geheimen Schlüssel für die Authentifizierung zu erstellen. Lesen Sie unbedingt alle Kommentare, um sicherzustellen, dass Sie die Vorlage richtig ausgefüllt haben, und speichern Sie sie unter dem Namen **edge-auth-overrides.yaml**:
```
apiVersion: v1 kind: Secret metadata:   # HINWEIS: Dem Namen muss der Name vorangestellt sein, den Sie für Ihre angepasste Ressource vergeben haben (Standardwert: 'ibm-edge').   #name: <NAME_DER_ANGEPASSTEN_RESSOURCE>-auth-overrides   name: ibm-edge-auth-overrides type: Opaque stringData:   # Entfernen Sie die Kommentarzeichen bei den Einstellungen für die Agbot-Postgresql-Verbindung und setzen Sie Ihre gewünschten Einstellungen ein.   agbot-db-host: "<einzelner_hostname_der_fernen_datenbank>"   agbot-db-port: "<einzelner_port_für_die_ausführung_der_datenbank>"   agbot-db-name: "<name_der_datenbank_zur_verwendung_in_der_postgresql-instanz>"   agbot-db-user: "<benutzername_für_die_verbindung>"   agbot-db-pass: "<kennwort_für_die_verbindung>"   agbot-db-ssl: "<disable|require|verify-full>"   # Achten Sie auf die korrekte Einrückung (vier Leerzeichen)   agbot-db-cert: |-     -----BEGIN CERTIFICATE-----
    ....
    -----END CERTIFICATE-----

  # Einstellungen für Exchange-Postgresql-Verbindung   exchange-db-host: "<einzelner_hostname_der_fernen_datenbank>"   exchange-db-port: "<einzelner_port_für_die_ausführung_der_datenbank>"   exchange-db-name: "<name_der_datenbank_zur_verwendung_in_der_postgresql-instanz>"   exchange-db-user: "<benutzername_für_die_verbindung>"   exchange-db-pass: "<kennwort_für_die_verbindung>"   exchange-db-ssl: "<disable|require|verify-full>"   # Achten Sie auf die korrekte Einrückung (vier Leerzeichen)   exchange-db-cert: |-     -----BEGIN CERTIFICATE-----
    ....
    -----END CERTIFICATE-----

  # Einstellungen für CSS-MongoDB-Verbindung   css-db-host: "<durch_kommas_getrennte_liste_inklusive_ports: hostname.domäne:port,hostname2.domäne:port2 >"   css-db-name: "<name_der_datenbank_zur_verwendung_in_der_mongodb-instanz>"   css-db-user: "<benutzername_für_die_verbindung>"   css-db-pass: "<kennwort_für_die_verbindung>"   css-db-auth: "<name_der_datenbank_zum_speichern_von_benutzerberechtigungsnachweisen>"   css-db-ssl: "<true|false>"   # Achten Sie auf die korrekte Einrückung (vier Leerzeichen)   css-db-cert: |-     -----BEGIN CERTIFICATE-----
    ....
    -----END CERTIFICATE-----
```
{: codeblock}

Erstellen Sie den geheimen Schlüssel:
```
oc apply -f edge-auth-overrides.yaml
```
{: codeblock}

Überwachen Sie die Operatorprotokolle wie im Abschnitt [Operatorsteuerschleife](./configuration.md#remote) beschrieben.


## Skalierungskonfiguration
{: #scale}

Die benutzerdefinierte EamHub-Ressourcenkonfiguration stellt Konfigurationsparameter bereit, die erforderlich sein könnten, um Ressourcen auf dem {{site.data.keyword.ieam}} Management Hub zu erhöhen, um eine hohe Anzahl von Edge-Knoten zu unterstützen.
Die Kunden sollten den Ressourcenverbrauch der {{site.data.keyword.ieam}} -Pods überwachen, insbesondere die Exchanges-und Agreement-Bots (agbots), und bei Bedarf Ressourcen hinzufügen. Weitere Informationen finden Sie unter [Zugriff auf das {{site.data.keyword.ieam}} Grafana-Dashboard](../admin/monitoring.md) . Die OpenShift-Plattform erkennt diese Aktualisierungen und wendet sie automatisch auf die {{site.data.keyword.ieam}} PODS-Ausführung unter {{site.data.keyword.ocp}}an.

Einschränkungen

Wenn die Standardressourcenzuordnungen und internen TLS zwischen den {{site.data.keyword.ieam}} -Pods deaktiviert sind, hat IBM bis zu 40.000 registrierte Edge-Knoten getestet, die 40.000 Serviceinstanzen mit Implementierungsrichtlinien-Updates implementiert haben, die Auswirkungen auf 25 % (oder 10.000) der implementierten Services haben.

Um 40.000 registrierte Edge-Knoten zu unterstützen, wenn interne TLS zwischen den {{site.data.keyword.ieam}} -Pods aktiviert ist, benötigen die Exchange-Pods zusätzliche CPU-Ressourcen. 
Nehmen Sie die folgende Änderung in der Konfiguration der angepassten EamHub-Ressource vor.

Fügen Sie den folgenden Abschnitt unter **spec** hinzu:

```
spec:   exchange_resources:     requests:       memory: 512Mi       cpu: 10m     limits:       memory: 2Gi       cpu: 5
```
{: codeblock}

Wenn Sie mehr als 90.000 Servicebereitstellungen unterstützen möchten, müssen Sie die folgende Änderung in der Konfiguration der angepassten EamHub-Ressource vornehmen.

Fügen Sie den folgenden Abschnitt unter **spec** hinzu:

```
spec: agbot_resources: requests: memory: 1Gi cpu: 10m limits: memory: 4Gi cpu: 2
```
{: codeblock}

