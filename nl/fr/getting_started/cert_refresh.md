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

# Actualisation du certificat
{: #certrefresh}

Dans le cadre de l'installation de {{site.data.keyword.ieam}}, selon la version de {{site.data.keyword.common_services}} installée, des certificats peuvent avoir été créés avec une durée de vie courte entraînant leur renouvellement automatique.

Connectez-vous à votre cluster dans lequel {{site.data.keyword.ieam}} est installé et validez la version actuelle de {{site.data.keyword.common_services}} en exécutant :
```
$ oc get csv -A | grep -E 'ibm-common-service-operator|NAME' NAMESPACE NAME DISPLAY VERSION REPLACES PHASE ibm-common-services ibm-common-service-operator.v3.6.4 IBM Cloud Platform Common Services 3.6.4 ibm-Common-service-operator.v3.6.3 Succeeded ibm-edge ibm-common-service-operator.v3.6.4 IBM Cloud Platform Common Services 3.6.4 ibm-common-service-operator.v3.6.3 Succeeded
```

Vous devriez voir (au moins) deux instances du même opérateur. Une dans l'espace de nom `ibm-common-services`, l'autre dans l'espace de nom où {{site.data.keyword.ieam}} a été installé. Vérifiez que les deux versions correspondent et que la version est `3.6.4` ou supérieure. Si les versions ne correspondent pas, ou qu'il s'agit d'une version antérieure, reportez-vous à la console {{site.data.keyword.open_shift}} si vous avez défini des mises à jour d'abonnement manuelles, ou pour déterminer les éventuels problèmes sous-jacents dus à une précédente tentative de mise à niveau.

Si un certificat a été renouvelé automatiquement, une action manuelle est requise pour s'assurer que {{site.data.keyword.ieam}} utilise correctement le nouveau certificat :
1. Procurez-vous le nouveau certificat et actualisez les ressources {{site.data.keyword.ieam}}.
2. Fournissez le certificat et communiquez les instructions ci-dessous à vos propriétaires de nœuds de périphérie pour les avertir qu'ils doivent appliquer ce nouveau certificat à chaque nœud de périphérie.

## Tâche 1 : Procurez-vous le nouveau certificat et actualisez les ressources {{site.data.keyword.ieam}}.
{: #task1}
1. En tant qu'administrateur de cluster, connectez-vous au cluster sur lequel votre concentrateur {{site.data.keyword.ieam}} est installé. Validez la date de création et d'expiration de votre certificat existant :
   ```
   echo "$(oc get secret management-ingress-ibmcloud-cluster-ca-cert -o jsonpath="{.data['ca\.crt']}" -n ibm-common-services | base64 --decode)" | openssl x509 -text -noout | grep -A 2 Validity
   ```
   {: codeblock}

   **Remarque** : si la date de création ne coïncide pas avec le début des problèmes de communication, il est peu probable que le problème soit dû à un renouvellement de certificat et vous ne devez pas poursuivre ce processus.

2. Exportez le nouveau certificat dans un fichier :
   ```
   oc get secret cs-ca-certificate-secret -o jsonpath="{.data['ca\.crt']}" -n ibm-common-services | base64 --decode > /tmp/cs-ca.crt
   ```
   {: codeblock}

3. Actualisez les {{site.data.keyword.ieam}} pods d'échange et SDO (ce qui entraîne une brève interruption de la communication {{site.data.keyword.ieam}}) :
   ```
   oc delete pod -l app.kubernetes.io/component=exchange -n ibm-edge  oc delete pod -l app.kubernetes.io/component=sdo -n ibm-edge
   ```
   {: codeblock}

4. Actualisez l'installation CSS **agent_files** avec le nouveau certificat, ce qui garantit que les futures installations de nœud de périphérie font confiance au nouveau certificat :
   ```
   echo '{"objectID": "agent-install.crt","objectType": "agent_files","destinationOrgID": "IBM","version": "","public": true}' > /tmp/agent-cert-mms.json   hzn mms -o IBM object publish -m /tmp/agent-cert-mms.json -f /tmp/cs-ca.crt
   ```
   {: codeblock}

   Notifiez tous les propriétaires de nœud de périphérie. Incluez une copie de ce fichier de certificat et un lien direct vers les instructions de la [Tâche 2](cert_refresh.md#task2) pour permettre aux utilisateurs finaux de configurer leur(s) nœud(s) avec le nouveau certificat.

## Tâche 2 : Appliquer le nouveau certificat à vos nœuds de périphérie
{: #task2}
### Pour un dispositif de périphérie
1. Connectez-vous à l'hôte et remplacez manuellement le nouveau fichier de certificat ou exécutez la commande suivante (remplacez &amp;TWBLT;DEVICE_HOST&gt; par le nom d'hôte ou l'adresse IP de vos nœuds et &amp;TWBLT;CA_CERT_FILE&gt; par l'emplacement du fichier de certificat que vous avez reçu) :
   ```
   ssh root@<DEVICE_HOST> "source /etc/default/horizon; echo -e '$(cat <CA_CERT_FILE>)' > \$HZN_MGMT_HUB_CERT_PATH"
   ```
   {: codeblock}

2. Vérifiez que l'ancien certificat a été remplacé :
   ```
   ssh root@<DEVICE_HOST> "source /etc/default/horizon; cat \$HZN_MGMT_HUB_CERT_PATH"
   ```
   {: codeblock}

### Pour un cluster de périphérie
1. Connectez-vous à l'espace de nom dans lequel votre POD d'agent est en cours d'exécution et remplacez le certificat existant arrivé à expiration (remplacez &amp;TWBLT;CA_CERT_FILE&gt; par l'emplacement du fichier que vous avez reçu et qui contient le nouveau certificat) :
   ```
   oc patch secret openhorizon-agent-secrets --type=merge --patch '{"data": {"agent-install.crt": "'$(cat &amp;TWBLT;CA_CERT_FILE&gt; | base64 | tr -d '\n')'"}}'
   ```
   {: codeblock}

2. La validation du secret a été mise à jour :
   ```
   oc get secret openhorizon-agent-secrets -o jsonpath="{.data['agent-install\.crt']}" | base64 --decode
   ```
   {: codeblock}

3. Redémarrez le pod d'agent {{site.data.keyword.ieam}} :
   ```
   oc delete pod $(oc get pods | grep 'agent-' | awk '{print $1}')
   ```
   {: codeblock}
