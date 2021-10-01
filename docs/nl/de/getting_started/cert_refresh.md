---

copyright:
  years: 2021
lastupdated: "2021-02-09"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Zertifikatsaktualisierung
{: #certrefresh}

Als Teil der {{site.data.keyword.ieam}}-Installation wurden je nach Version von {{site.data.keyword.common_services}} Zertifikate möglicherweise mit einer kurzen Lebensdauer erstellt, die zu ihrer automatischen Verlängerung führt.

Melden Sie sich bei Ihrem Cluster an, in dem {{site.data.keyword.ieam}} installiert ist, und überprüfen Sie die aktuelle Version von {{site.data.keyword.common_services}} durch runniIng:
```
$ oc get csv -A | grep -E 'ibm-common-service-operator|NAME' NAMESPACE NAME DISPLAY VERSION REPLACES PHASE ibm-common-services ibm-common-service-operator.v3.6.4 IBM Cloud Platform Common Services 3.6.4 ibm-Common-service-operator.v3.6.3 Succeeded ibm-edge ibm-common-service-operator.v3.6.4 IBM Cloud Platform Common Services 3.6.4 ibm-common-service-operator.v3.6.3 Succeeded
```

Sie sollten (mindestens) zwei Instanzen desselben Operators sehen: Eine im Namespace `ibm-common-services` und eine im Namespace, in dem {{site.data.keyword.ieam}} installiert wurde. Stellen Sie sicher, dass die beiden Versionen übereinstimmen und dass die Version `3.6.4` oder höher ist. Wenn die Versionen nicht übereinstimmen oder es sich um eine frühere Version handelt, sehen Sie in der {{site.data.keyword.open_shift}}-Konsole nach, wenn Sie Subskriptionsaktualisierungen auf manuell gesetzt haben, oder um alle zugrunde liegenden Probleme zu ermitteln, die aufgrund eines vorherigen Upgradeversuchs möglicherweise vorhanden sind.

Wenn ein Zertifikat automatisch erneuert wurde, ist eine manuelle Aktion erforderlich, um sicherzustellen, dass {{site.data.keyword.ieam}} das neue Zertifikat ordnungsgemäß verwendet:
1. Fordern Sie das neue Zertifikat an und aktualisieren Sie die {{site.data.keyword.ieam}}-Ressourcen.
2. Stellen Sie das Zertifikat bereit und teilen Sie den Besitzern der Edge-Knoten die unten stehenden Anweisungen mit, um sie darauf hinzuweisen, dass sie dieses neue Zertifikat auf jeden Edge-Knoten anwenden müssen.

## Task 1: Fordern Sie das neue Zertifikat an und aktualisieren Sie die {{site.data.keyword.ieam}}-Ressourcen
{: #task1}
1. Melden Sie sich als Clusteradministrator bei dem Cluster an, auf dem Ihr {{site.data.keyword.ieam}}-Hub installiert ist. Prüfen Sie das Erstellungs- und Verfallsdatum auf Ihrem vorhandenen Zertifikat:
   ```
   echo "$(oc get secret management-ingress-ibmcloud-cluster-ca-cert -o jsonpath="{.data['ca\.crt']}" -n ibm-common-services | base64 --decode)" | openssl x509 -text -noout | grep -A 2 Validity
   ```
   {: codeblock}

   **Hinweis**: Wenn das Erstellungsdatum nicht mit dem Zeitpunkt übereinstimmt, an dem die Kommunikationsprobleme begannen, ist es unwahrscheinlich, dass das Problem auf eine Zertifikatserneuerung zurückzuführen ist, und Sie sollten mit dem Rest dieses Prozesses nicht fortfahren.

2. Exportieren Sie das neue Zertifikat in eine Datei:
   ```
   oc get secret cs-ca-certificate-secret -o jsonpath="{.data['ca\.crt']}" -n ibm-common-services | base64 --decode > /tmp/cs-ca.crt
   ```
   {: codeblock}

3. Aktualisieren Sie {{site.data.keyword.ieam}} Exchange und die SDO-Pods (dies führt zu einer kurzen Unterbrechung der {{site.data.keyword.ieam}}-Kommunikation):
   ```
   oc delete pod -l app.kubernetes.io/component=sdo -n ibm-edge
   ```
   {: codeblock}

4. Aktualisieren Sie die CSS-Installation **agent_files** mit dem neuen Zertifikat. Dies stellt sicher, dass künftige Edge-Knoten-Installationen dem neuen Zertifikat vertrauen:
   ```
   echo '{"objectID": "agent-install.crt","objectType": "agent_files","destinationOrgID": "IBM","version": "","public": true}' > /tmp/agent-cert-mms.json    hzn mms -o IBM object publish -m /tmp/agent-cert-mms.json -f /tmp/cs-ca.crt
   ```
   {: codeblock}

   Benachrichtigen Sie alle Edge-Knoten-Besitzer. Fügen Sie eine Kopie dieser Zertifikatsdatei und einen direkten Link zu den Anweisungen von [Task 2](cert_refresh.md#task2) ein, um Endbenutzern zu ermöglichen, ihren Knoten mit dem neuen Zertifikat zu konfigurieren.

## Task 2: Neues Zertifikat auf Edge-Knoten anwenden
{: #task2}
### Für Edge-Einheit
1. Melden Sie sich bei dem Host an und ersetzen Sie die neue Zertifikatsdatei manuell, oder führen Sie den folgenden Befehl aus (ersetzen Sie &amp;TWBLT; DEVICE_HOST&gt; mit dem Hostnamen oder der IP Ihres Knotens und &amp;TWBLT; CA_CERT_FILE&gt; mit dem Speicherort der Zertifikatsdatei, die Sie erhalten haben):
   ```
   ssh root@<EINHEITENHOST> "source /etc/default/horizon; echo -e '$(cat <CA-ZERTIFIKATSDATEI>)' > \$HZN_MGMT_HUB_CERT_PATH"
   ```
   {: codeblock}

2. Prüfen Sie, ob das alte Zertifikat ersetzt wurde:
   ```
   ssh root@<EINHEITENHOST> "source /etc/default/horizon; cat \$HZN_MGMT_HUB_CERT_PATH"
   ```
   {: codeblock}

### Für Edge-Cluster
1. Melden Sie sich an dem Namespace an, in dem Ihr Agent-POD ausgeführt wird, ersetzen Sie das vorhandene abgelaufene Zertifikat (ersetzen Sie &amp;TWBLT; CA_CERT_FILE&gt; mit dem Speicherort der neuen Zertifikatsdatei, die Sie erhalten haben):
   ```
   oc patch secret openhorizon-agent-secrets --type=merge --patch '{"data": {"agent-install.crt": "'$(cat &amp;TWBLT;CA_CERT_FILE&gt; | base64 | tr -d '\n')'"}}'
   ```
   {: codeblock}

2. Prüfen Sie, ob der geheime Schlüssel aktualisiert wurde:
   ```
   oc get secret openhorizon-agent-secrets -o jsonpath="{.data['agent-install\.crt']}" | base64 --decode
   ```
   {: codeblock}

3. Führen Sie für den {{site.data.keyword.ieam}}-Agentenpod einen Neustart durch:
   ```
   oc delete pod $(oc get pods | grep 'agent-' | awk '{print $1}')
   ```
   {: codeblock}
