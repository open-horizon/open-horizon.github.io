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

# Renovación de certificados
{: #certrefresh}

Como parte de la instalación de {{site.data.keyword.ieam}}, en función de la versión de {{site.data.keyword.common_services}} instalada, es posible que se hayan creado certificados cuya vida útil sea corta, lo que conduciría a su renovación automática.

Inicie sesión en el clúster donde se haya instalado {{site.data.keyword.ieam}} y valide la versión actual de {{site.data.keyword.common_services}} ejecutando:
```
$ oc get csv -A | grep -E 'ibm-common-service-operator|NAME' NAMESPACE NAME DISPLAY VERSION REPLACES PHASE ibm-common-services ibm-common-service-operator.v3.6.4 IBM Cloud Platform Common Services 3.6.4 ibm-Common-service-operator.v3.6.3 Succeeded ibm-edge ibm-common-service-operator.v3.6.4 IBM Cloud Platform Common Services 3.6.4 ibm-common-service-operator.v3.6.3 Succeeded
```

Debería ver (como mínimo) dos instancias del mismo operador. Una debería estar en el espacio de nombres `ibm-common-services` y la otra, en el espacio de nombres donde se haya instalado {{site.data.keyword.ieam}}. Asegúrese de que las dos versiones coincidan y de que la versión sea la `3.6.4` o una posterior. Si las versiones no coinciden o se trata de una versión anterior, consulte la consola de {{site.data.keyword.open_shift}}, sea porque ha establecido las actualizaciones de suscripción en la opción manual, sea para determinar los problemas subyacentes que podrían haberse generado a partir de un intento de actualización anterior.

Si se ha renovado automáticamente un certificado, es necesario realizar una acción manual para asegurarse de que {{site.data.keyword.ieam}} utiliza el nuevo certificado correctamente:
1. Obtenga el nuevo certificado y renueve los recursos de {{site.data.keyword.ieam}}.
2. Suministre el certificado y comunique las instrucciones siguientes del nodo periférico a los propietarios del nodo periférico, a fin de alertarles de que deben aplicar este nuevo certificado a cada nodo periférico.

## Tarea 1: obtener el nuevo certificado y renovar los recursos de {{site.data.keyword.ieam}}
{: #task1}
1. Como administrador del clúster, inicie sesión en el clúster donde se haya instalado {{site.data.keyword.ieam}} Hub. Valide la fecha de creación y la de caducidad en el certificado existente:
   ```
   echo "$(oc get secret management-ingress-ibmcloud-cluster-ca-cert -o jsonpath="{.data['ca\.crt']}" -n ibm-common-services | base64 --decode)" | openssl x509 -text -noout | grep -A 2 Validity
   ```
   {: codeblock}

   **Nota**: Si la fecha de creación no coincide con el momento en el que comenzaron los problemas de comunicación, es poco probable que el problema se deba a una renovación de certificado, por lo que no tiene que seguir con el resto de este proceso.

2. Exporte el nuevo certificado a un archivo:
   ```
   oc get secret cs-ca-certificate-secret -o jsonpath="{.data['ca\.crt']}" -n ibm-common-services | base64 --decode > /tmp/cs-ca.crt
   ```
   {: codeblock}

3. Renueve los pods {{site.data.keyword.ieam}} Exchange y SDO (esto provoca una breve interrupción en la comunicación de {{site.data.keyword.ieam}}):
   ```
   oc delete pod -l app.kubernetes.io/component=exchange -n ibm-edge    oc delete pod -l app.kubernetes.io/component=sdo -n ibm-edge
   ```
   {: codeblock}

4. Renueve los **agent_files** de la instalación de CSS con el nuevo certificado; así, se garantiza que las futuras instalaciones de nodos periféricos confíen en el nuevo certificado:
   ```
   echo '{"objectID": "agent-install.crt","objectType": "agent_files","destinationOrgID": "IBM","version": "","public": true}' > /tmp/agent-cert-mms.json   hzn mms -o IBM object publish -m /tmp/agent-cert-mms.json -f /tmp/cs-ca.crt
   ```
   {: codeblock}

   Envíe notificaciones a todos los propietarios de nodos periféricos. Incluya una copia de este archivo de certificado y un enlace directo a las instrucciones de la [Tarea 2](cert_refresh.md#task2) para permitir a los usuarios finales configurar sus nodos con el nuevo certificado.

## Tarea 2: Aplicar el nuevo certificado a los nodos periféricos
{: #task2}
### Para un dispositivo periférico
1. Inicie sesión en el host y sustituya manualmente el nuevo archivo de certificado o ejecute el mandato siguiente (sustituya &amp;TWBLT;DEVICE_HOST&gt; por el nombre de host o la dirección IP de los nodos y &amp;TWBLT;CA_CERT_FILE&gt; por la ubicación del archivo de certificado que se le ha proporcionado):
   ```
   ssh root@<DEVICE_HOST> "source /etc/default/horizon; echo -e '$(cat <CA_CERT_FILE>)' > \$HZN_MGMT_HUB_CERT_PATH"
   ```
   {: codeblock}

2. Valide que el certificado antiguo se haya sustituido:
   ```
   ssh root@<DEVICE_HOST> "source /etc/default/horizon; cat \$HZN_MGMT_HUB_CERT_PATH"
   ```
   {: codeblock}

### Para un clúster periférico
1. Inicie sesión en el espacio de nombres en el que se esté ejecutando el POD de agente y sustituya el certificado caducado existente (sustituya &amp;TWBLT;CA_CERT_FILE&gt; por la ubicación del archivo que se ha proporcionado con el nuevo certificado):
   ```
   oc patch secret openhorizon-agent-secrets --type=merge --patch '{"data": {"agent-install.crt": "'$(cat &amp;TWBLT;CA_CERT_FILE&gt; | base64 | tr -d '\n')'"}}'
   ```
   {: codeblock}

2. Valide que el secreto se ha actualizado:
   ```
   oc get secret openhorizon-agent-secrets -o jsonpath="{.data['agent-install\.crt']}" | base64 --decode
   ```
   {: codeblock}

3. Reinicie el pod del agente de {{site.data.keyword.ieam}}:
   ```
   oc delete pod $(oc get pods | grep 'agent-' | awk '{print $1}')
   ```
   {: codeblock}
