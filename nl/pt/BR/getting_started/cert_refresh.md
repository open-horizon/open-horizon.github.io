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

# Atualização de certificado
{: #certrefresh}

Como parte da instalação do {{site.data.keyword.ieam}}, dependendo da versão do {{site.data.keyword.common_services}} instalado, certificados podem ter sido criados com uma curta expectativa de vida levando à sua renovação automática.

Faça login em seu cluster onde o {{site.data.keyword.ieam}} está instalado e valide a versão atual de {{site.data.keyword.common_services}} executando:
```
$ oc get csv -A | grep -E 'ibm-common-service-operator|NAME' NAMESPACE                              NAME                                            DISPLAY                                VERSION   REPLACES                                        PHASE ibm-common-services                    ibm-common-service-operator.v3.6.4              IBM Cloud Platform Common Services     3.6.4     ibm-Common-service-operator.v3.6.3              Succeeded ibm-edge                               ibm-common-service-operator.v3.6.4              IBM Cloud Platform Common Services     3.6.4     ibm-common-service-operator.v3.6.3              Succeeded
```

Deve-se ver (pelo menos) duas instâncias do mesmo operador. Um no namespace `ibm-common-services` e um no namespace onde o {{site.data.keyword.ieam}} foi instalado. Assegure a correspondência de duas versões e que a versão seja `3.6.4` ou mais recente. Se as versões não combinarem, ou forem uma versão anterior, consulte o console do {{site.data.keyword.open_shift}} se você tiver configurado a atualizações de assinatura para manual, ou para determinar quaisquer problemas subjacentes que possam estar presentes devido a uma tentativa de upgrade anterior.

Se um certificado foi renovado automaticamente, a ação manual é necessária para assegurar que o {{site.data.keyword.ieam}} use o novo certificado adequadamente:
1. Obtenha o novo certificado e atualize os recursos do {{site.data.keyword.ieam}}.
2. Forneça o certificado e comunique as instruções do nó de borda abaixo com seus proprietários de nós de borda para alertá-los de que eles devem aplicar esse novo certificado em cada nó de borda.

## Tarefa 1: Obter o novo certificado e atualizar os recursos do {{site.data.keyword.ieam}}
{: #task1}
1. Como administrador do cluster, efetue login no cluster em que o Hub do {{site.data.keyword.ieam}} está instalado. Valide a criação e a data de expiração no seu certificado existente:
   ```
   echo "$(oc get secret management-ingress-ibmcloud-cluster-ca-cert -o jsonpath="{.data['ca\.crt']}" -n ibm-common-services | base64 --decode)" | openssl x509 -text -noout | grep -A 2 Validity
   ```
   {: codeblock}

   **Nota**: se a data de criação não coincidir com os problemas de comunicação de tempo iniciados, é improvável que o problema seja devido a uma renovação de certificado e você não deve prosseguir com o restante desse processo.

2. Exporte o novo certificado para um arquivo:
   ```
   oc get secret cs-ca-certificate-secret -o jsonpath="{.data['ca\.crt']}" -n ibm-common-services | base64 --decode > /tmp/cs-ca.crt
   ```
   {: codeblock}

3. Atualize a troca do {{site.data.keyword.ieam}} e os pods do SDO (isso causa uma breve indisponibilidade de comunicação do {{site.data.keyword.ieam}}):
   ```
   oc delete pod -l app.kubernetes.io/component=exchange -n ibm-edge    oc delete pod -l app.kubernetes.io/component=sdo -n ibm-edge
   ```
   {: codeblock}

4. Atualize a instalação do CSS **agent_files** com o novo certificado; isso assegura que as futuras instalações de nó de borda confiem no novo certificado:
   ```
   echo '{"objectID": "agent-install.crt","objectType": "agent_files","destinationOrgID": "IBM","version": "","public": true}' > /tmp/agent-cert-mms.json    hzn mms -o IBM object publish -m /tmp/agent-cert-mms.json -f /tmp/cs-ca.crt
   ```
   {: codeblock}

   Notifique todos os proprietários de nós de borda. Inclua uma cópia desse arquivo de certificado e um link direto para as instruções [Tarefa 2](cert_refresh.md#task2) para permitir que os usuários finais configurem o(s) seu(s) nó(s) com o novo certificado.

## Tarefa 2: aplique o novo certificado aos seus nós de borda
{: #task2}
### Para um dispositivo de borda
1. Efetue login no host e substitua manualmente o novo arquivo de certificado ou execute o comando a seguir (substitua &amp;TWBLT;DEVICE_HOST&gt; pelo nome do host ou IP de seus nós e &amp;TWBLT;CA_CERT_FILE&gt; pela localização do arquivo de certificado fornecido a você):
   ```
   ssh root@<DEVICE_HOST> "source /etc/default/horizon; echo -e '$(cat <CA_CERT_FILE>)' > \$HZN_MGMT_HUB_CERT_PATH"
   ```
   {: codeblock}

2. Valide se o certificado antigo foi substituído:
   ```
   ssh root@<DEVICE_HOST> "source /etc/default/horizon; cat \$HZN_MGMT_HUB_CERT_PATH"
   ```
   {: codeblock}

### Para um cluster de borda
1. Efetue login no namespace em que seu POD do agente está em execução, substitua o certificado expirado existente (substitua &amp;TWBLT;CA_CERT_FILE&gt; pela localização do arquivo fornecido a você, que contém o novo certificado):
   ```
   oc patch secret openhorizon-agent-secrets --type=merge --patch '{"data": {"agent-install.crt": "'$(cat &amp;TWBLT;CA_CERT_FILE&gt; | base64 | tr -d '\n')'"}}'
   ```
   {: codeblock}

2. Valide se o segredo foi atualizado:
   ```
   oc get secret openhorizon-agent-secrets -o jsonpath="{.data['agent-install\.crt']}" | base64 --decode
   ```
   {: codeblock}

3. Reinicie o pod do agente do {{site.data.keyword.ieam}}:
   ```
   oc delete pod $(oc get pods | grep 'agent-' | awk '{print $1}')
   ```
   {: codeblock}
