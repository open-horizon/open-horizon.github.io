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

# Configurar {{site.data.keyword.ieam}}

## Configuração de Recursos Customizados do EamHub
{: #cr}

A configuração principal para o {{site.data.keyword.ieam}} é feita através do recurso customizado do EamHub, particularmente o campo **spec** desse recurso customizado.

Este documento assume:
* O namespace para o qual você está executando estes comandos é o local onde o operador de hub de gerenciamento do {{site.data.keyword.ieam}} é implementado.
* O nome de recurso customizado do EamHub é o **ibm-edge** padrão. Se for diferente, altere os comandos para substituir **ibm-edge**.
* O binário **jq** é instalado, o que assegura que a saída seja exibida em um formato legível.


O **spec** de padrão definido é mínimo, contendo apenas a aceitação da licença, que você pode ver com:
```
$ oc get eamhub ibm-edge -o yaml ... spec:   license:     accept: true ...
```

### Loop de controle do operador
{: #loop}

O operador do hub de gerenciamento do {{site.data.keyword.ieam}} é executado em um loop idempotente contínuo para sincronizar o estado atual dos recursos com o estado esperado dos recursos.

Devido a esse loop contínuo, será necessário entender duas coisas ao tentar configurar os seus recursos gerenciados pelo operador:
* Qualquer mudança no recurso customizado será lida assincronamente pelo loop de controle. Após você fazer a mudança, pode levar alguns minutos para que essa mudança seja implementada por meio do operador.
* Qualquer mudança manual que for feita em um recurso que o operador controla poderá ser sobrescrita (desfeita) pelo operador aplicando um estado específico. 

Verifique os logs do pod do operador para observar este loop:
```
oc logs $(oc get pods | grep ibm-eamhub-operator | awk '{print $1}') --tail 20 -f
```
{: codeblock}

Quando um loop termina, ele gera um resumo **PLAY RECAP**. Para ver o resumo mais recente, execute:
```
oc logs $(oc get pods | grep ibm-eamhub-operator | awk '{print $1}') --tail 5000 | grep -A 1 '^PLAY RECAP' | tail -n 1
```
{: codeblock}

O seguinte indica um loop que foi concluído sem nenhuma operação ocorrendo (em seu estado atual, o **PLAY RECAP** sempre mostrará **changed=1**):
```
$ oc logs $(oc get pods | grep ibm-eamhub-operator | awk '{print $1}') --tail 5000 | grep -A 1 '^PLAY RECAP' | tail -n 1 localhost                  : ok=51   changed=1    unreachable=0    failed=0    skipped=11   rescued=0    ignored=0
```
{: codeblock}

Revise estes três campos ao fazer mudanças na configuração:
* **changed**: quando maior que **1**, indica que o operador realizou uma tarefa que alterou o estado de um ou mais recursos (pode ser mediante sua solicitação, alterando o recurso customizado, ou por meio do operador, revertendo uma mudança manual realizada).
* **rescued**: uma tarefa falhou; entretanto, essa era uma possível falha conhecida e a tarefa será tentada novamente no próximo loop.
* **failed**: na instalação inicial, existem algumas falhas esperadas; se você estiver vendo a mesma falha repetidamente e a mensagem não for clara (ou oculta), isso provavelmente indica um problema.

### Opções de Configuração Comum do EamHub

Várias mudanças na configuração podem ser feitas, mas algumas são mais propensas a serem mudadas do que outras. Esta seção descreve algumas das configurações mais comuns.

| Valor de configuração | Padrão | Descrição |
| :---: | :---: | :---: |
| Valores globais | -- | -- |
| pause_control_loop | falso | Pausa o loop de controle mencionado acima para permitir mudanças manuais provisórias para depuração. Não deve ser usado para estado estável. |
| ieam_maintenance_mode | falso | Configura todas as contagens de réplicas de pods sem armazenamento persistente como 0. Usado para fins de restauração de backup. |
| ieam_local_databases | verdadeiro | Ativa ou desativa bancos de dados locais. Alternar entre estados não é suportado. Consulte [configuração do banco de dados remoto](./configuration.md#remote). |
| ieam_database_HA | verdadeiro | Ativa ou desativa o modo HA para bancos de dados locais. Isso configura a contagem de réplicas para todos os pods do banco de dados como **3** quando **verdadeiro** e **1** quando **falso**. |
| hide_sensitive_logs | verdadeiro | Oculta os registros do operador que lidam com a configuração de **Segredos do Kubernetes**, se configurado como **falso** falhas na tarefa podem resultar nos valores de autenticação codificados do registro do operador. |
| storage_class_name | "" | Usa a classe de armazenamento padrão se não for configurada. |
| ieam_enable_tls | falso | Ativa ou desativa o TLS interno para tráfego entre os componentes do {{site.data.keyword.ieam}}. **Cuidado:** Se substituindo a configuração padrão pelo Exchange, CSS ou Vault, a configuração do TLS deve ser modificada manualmente na substituição de configuração. |
| ieam_local_secrets_manager | verdadeiro | Ativa ou desabilita o componente gerenciador de segredos local (vault). |


### Opções de configuração de ajuste de escala do componente EamHub

| Valor de ajuste de escala do componente | Número padrão de réplicas | Descrição |
| :---: | :---: | :---: |
| exchange_replicas | 3 | O número padrão de réplicas para o Exchange. Se substituindo a configuração padrão do Exchange (exchange_config), o **maxPoolSize** deve ser ajustado manualmente usando esta fórmula `((exchangedb_max_connections - 8) / exchange_replicas)` |
| css_replicas | 3 | O número padrão de réplicas para o CSS. |
| ui_replicas | 3 | O número padrão de réplicas para a IU. |
| agbot_replicas | 2 | O número padrão de réplicas para o robô de contrato. Se substituindo a configuração padrão do robô de contrato (agbot_config), **MaxOpenConnections** deve ser ajustado manualmente usando esta formula `((agbotdb_max_connections-8) / agbot_replicas)` |


### Opções de configuração de recursos do componente EamHub

**Nota**: Uma vez que os operadores do Ansible requerem que um dicionário aninhado seja incluído como um todo, deve-se incluir valores aninhados de configuração em sua totalidade. Consulte [Ajuste de escala de configuração](./configuration.md#scale) para um exemplo.

<table>
<tr>
<td> Valor de recurso de componente </td> <td> Padrão </td> <td> Descrição </td>
</tr>
<tr>
<td> exchange_resources </td> 
<td>

```
  exchange_resources: requests: memory: 512Mi cpu: 10m limits: memory: 2Gi cpu: 2
```

</td>
<td>
As solicitações e limites padrão para o Exchange. 
</td>
</tr>
<tr>
<td> agbot_resources </td> 
<td>

```
  agbot_resources: requests: memory: 64Mi cpu: 10m limits: memory: 2Gi cpu: 2
```

</td>
<td>
As solicitações e limites padrão do robô de contrato. 
</td>
</tr>
<tr>
<td> css_resources </td> 
<td>

```
  css_resources: requests: memory: 64Mi cpu: 10m limits: memory: 2Gi cpu: 2
```

</td>
<td>
As solicitações e limites padrão para o CSS. 
</td>
</tr>
<tr>
<td> sdo_resources </td> 
<td>

```
  sdo_resources: requests: memory: 1024Mi cpu: 10m limits: memory: 2Gi cpu: 2
```

</td>
<td>
As solicitações e limites padrão para o SDO. 
</td>
</tr>
<tr>
<td> ui_resources </td> 
<td>

```
  ui_resources: requests: memory: 64Mi cpu: 10m limits: memory: 2Gi cpu: 2
```

</td>
<td>
As solicitações e limites padrão para a IU. 
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
As solicitações e limites padrão do gerenciador de segredos. 
</td>
</tr>
<tr>
<td> mongo_resources </td> 
<td>

```
  mongo_resources: limits: cpu: 2 memory: 2Gi requests: cpu: 100m memory: 256Mi
```

</td>
<td>
As solicitações e os limites padrão para o banco de dados mongo CSS. 
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
As solicitações e os limites padrão da sentinela postgres do Exchange. 
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
As solicitações e os limites padrão da proxy postgres do Exchange. 
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
As solicitações e os limites padrão do guardião postgres do Exchange. 
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
As solicitações e limites padrão da sentinela postgres do robô de contrato. 
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
As solicitações e limites padrão da proxy postgres do robô de contrato. 
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
As solicitações e limites padrão para o guardião postgres do robô de contrato. 
</td>
</tr>
</table>

### Opções de configuração do tamanho do banco de dados local do EamHub

| Valor de configuração do componente | Tamanho do volume persistente padrão | Descrição |
| :---: | :---: | :---: |
| postgres_exchangedb_storage_size | 20Gi | Tamanho do banco de dados do exchange. |
| postgres_agbotdb_storage_size | 20Gi | Tamanho do banco de dados postgres do robô de contrato. |
| mongo_cssdb_storage_size | 20Gi | Tamanho do banco de dados mongo do CSS. |

## Configuração da conversão de API de troca

É possível configurar a API de troca do {{site.data.keyword.ieam}} para retornar respostas em um idioma específico. Para isso, defina uma variável de ambiente com um **LANG** suportado de sua escolha (o padrão é **en**):

```
oc set env deployment <CUSTOM_RESOURCE_NAME>-exchange HZN_EXCHANGE_LANG=<LANG>
```
{: codeblock}

**Nota:** para obter uma lista de códigos de idioma suportados, consulte a primeira tabela na página [Idiomas suportados](../getting_started/languages.md).

## Configuração de banco de dados remoto
{: #remote}

**Nota**: a alternância entre bancos de dados locais e remotos não é suportada.

Para instalar com bancos de dados remotos, crie o recurso customizado do EamHub durante a instalação com o valor extra no campo **spec**.
```
spec:   ieam_local_databases: false   license:     accept: true
```
{: codeblock}

Conclua o modelo a seguir para criar um segredo de autenticação. Certifique-se de ler cada comentário para assegurar que eles sejam preenchidos com precisão e salve-os em **edge-auth-overrides.yaml**:
```
apiVersion: v1 kind: Secret metadata:   # NOTE: The name -must- be prepended by the name given to your Custom Resource, this defaults to 'ibm-edge'   #name: <CR_NAME>-auth-overrides   name: ibm-edge-auth-overrides type: Opaque stringData:   # agbot postgresql connection settings uncomment and replace with your settings to use   agbot-db-host: "<Single hostname of the remote database>"   agbot-db-port: "<Single port the database runs on>"   agbot-db-name: "<The name of the database to utilize on the postgresql instance>"   agbot-db-user: "<Username used to connect>"   agbot-db-pass: "<Password used to connect>"   agbot-db-ssl: "<disable|require|verify-full>"   # Ensure proper indentation (four spaces)   agbot-db-cert: |-     -----BEGIN CERTIFICATE-----
    ....
    -----END CERTIFICATE-----

  # exchange postgresql connection settings   exchange-db-host: "<Single hostname of the remote database>"   exchange-db-port: "<Single port the database runs on>"   exchange-db-name: "<The name of the database to utilize on the postgresql instance>"   exchange-db-user: "<Username used to connect>"   exchange-db-pass: "<Password used to connect>"   exchange-db-ssl: "<disable|require|verify-full>"   # Ensure proper indentation (four spaces)   exchange-db-cert: |-     -----BEGIN CERTIFICATE-----
    ....
    -----END CERTIFICATE-----

  # css mongodb connection settings   css-db-host: "<Comma separated list including ports: hostname.domain:port,hostname2.domain:port2 >"   css-db-name: "<The name of the database to utilize on the mongodb instance>"   css-db-user: "<Username used to connect>"   css-db-pass: "<Password used to connect>"   css-db-auth: "<The name of the database used to store user credentials>"   css-db-ssl: "<true|false>"   # Ensure proper indentation (four spaces)   css-db-cert: |-     -----BEGIN CERTIFICATE-----
    ....
    -----END CERTIFICATE-----
```
{: codeblock}

Crie o segredo:
```
oc apply -f edge-auth-overrides.yaml
```
{: codeblock}

Observe os logs do operador conforme documentado na seção [Loop de controle do operador](./configuration.md#remote).


## Configuração de ajuste de escala
{: #scale}

A configuração de recursos customizados do EamHub expõe parâmetros de configuração que podem ser necessários para aumentar os recursos para pods no hub de gerenciamento do {{site.data.keyword.ieam}} para oferecer suporte a altos números de nós de borda.
Os clientes devem monitorar o consumo de recursos dos pods do {{site.data.keyword.ieam}}, especialmente dos Exchanges e dos robôs de contrato (agbots) e incluir recursos quando necessário. Consulte [Acessando o Painel do Grafana do {{site.data.keyword.ieam}}](../admin/monitoring.md). A plataforma OpenShift reconhece essas atualizações e as aplica automaticamente os PODS do {{site.data.keyword.ieam}} em execução sob o {{site.data.keyword.ocp}}.

Restrições

Com as alocações de recursos padrão e o TLS interno entre os pods do {{site.data.keyword.ieam}} desativados, a IBM testou até 40.000 nós de borda cadastrados obtendo 40.000 instâncias de serviço implementadas com atualizações de políticas de implementação que impactam 25% (ou 10.000) dos serviços implementados.

Para oferecer suporte a 40.000 nós de borda registrados, quando o TLS interno entre os pods do {{site.data.keyword.ieam}} está ativado, os pods do Exchange requerem recursos adicionais de CPU. 
Faça a seguinte mudança na configuração de recursos customizados do EamHub

Inclua a seção a seguir em **spec**:

```
spec:   exchange_resources:     requests:       memory: 512Mi       cpu: 10m     limits:       memory: 2Gi       cpu: 5
```
{: codeblock}

Para oferecer suporte a mais de 90.000 implementações de serviços, faça a seguinte mudança na configuração de recursos customizados do EamHub.

Inclua a seção a seguir em **spec**:

```
spec: agbot_resources: requests: memory: 1Gi cpu: 10m limits: memory: 4Gi cpu: 2
```
{: codeblock}

