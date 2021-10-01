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

# Backup e recuperação de dados
{: #data_backup}

## Backup e recuperação do {{site.data.keyword.open_shift_cp}}

Para obter mais informações sobre backup e recuperação de dados em todo o cluster, consulte:

* [Backup do {{site.data.keyword.open_shift_cp}} 4.6 etcd](https://docs.openshift.com/container-platform/4.6/backup_and_restore/backing-up-etcd.html).

## Backup e recuperação do {{site.data.keyword.edge_notm}}

Os procedimentos de backup do {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) diferem um pouco dependendo do tipo de bancos de dados que você está usando. Esses bancos de dados são chamados de locais ou remotos.

|Tipo de banco de dados|Descrição|
|-------------|-----------|
|Local|Esses bancos de dados são instalados (por padrão) como recursos do {{site.data.keyword.open_shift}} em seu cluster do {{site.data.keyword.open_shift}}|
|Remoto|Esses bancos de dados são provisionados externamente ao cluster. Por exemplo, esses bancos de dados podem ser locais ou uma oferta de SaaS de provedor em nuvem.|

A definição de configuração que rege quais bancos de dados são usados é definida durante o tempo de instalação em seu recurso customizado como **spec.ieam\_local\_databases** e é verdadeira por padrão.

Para determinar o valor ativo para uma instância instalada do {{site.data.keyword.ieam}}, execute:

```
oc get eamhub ibm-edge -o jsonpath="{.spec.ieam_local_databases}"
```
{: codeblock}

Para obter mais informações sobre como configurar bancos de dados remotos no momento da instalação, consulte a página [Configuração](../hub/configuration.md).

**Nota**: a alternância entre bancos de dados locais e remotos não é suportada.

O produto {{site.data.keyword.edge_notm}} não faz backup automático de seus dados. Você é responsável por fazer backup do conteúdo na cadência escolhida e por armazenar esses backups em um local seguro separado para garantir a capacidade de recuperação. Como os backups secretos contêm conteúdo de autenticação codificado para conexões com o banco de dados e autenticação de aplicativo do {{site.data.keyword.mgmt_hub}}, armazene-os em um local seguro.

Se você estiver usando os seus próprios bancos de dados remotos, certifique-se de fazer backup desses bancos de dados. Esta documentação não descreve como fazer backup dos dados desses bancos de dados remotos.

O procedimento de backup do {{site.data.keyword.ieam}} também requer `yq` v3.

### Procedimento de Backup

1. Assegure-se de que você esteja conectado ao seu cluster com **cloudctl login** ou **oc login** como administrador de cluster. Faça backup de seus dados e segredos com o script a seguir, localizado na mídia descompactada usada para a instalação do {{site.data.keyword.mgmt_hub}} a partir do Passport Advantage. Execute o script com **-h** para uso:

   ```
   ibm-eam-{{site.data.keyword.semver}}-bundle/tools/ieam-backup.sh -h
   ```
   {: codeblock}
   
   **Note**: o script de backup detecta automaticamente o tipo dos bancos de dados que são usados durante a instalação.

   * Se você executar o exemplo a seguir sem opções, ele gerará uma pasta onde o script foi executado. A pasta segue este padrão de nomenclatura **ibm-edge-backup/$DATE/**:

     ```
     ibm-eam-{{site.data.keyword.semver}}-bundle/tools/ieam-backup.sh
     ```
     {: codeblock}
     
     Se foi detectada uma instalação de **banco de dados local**, seu backup conterá um diretório **customresource**, um diretório **databaseresources** e dois arquivos yaml:

     ```
     $ ls -l ibm-edge-backup/20201026_215107/   	  drwxr-xr-x  3 staff  staff     96 Oct 26 21:51 customresource 	  drwxr-xr-x  5 staff  staff    160 Oct 26 21:51 databaseresources 	  -rw-r--r--  1 staff  staff  13308 Oct 26 21:51 ibm-edge-auth-secret.yaml 	  -rw-r--r--  1 staff  staff   3689 Oct 26 21:51 ibm-edge-config.yaml
     ```
     {: codeblock}
     
	  Se uma instalação de **banco de dados remoto** for detectada, você verá os mesmos diretórios listados anteriormente, mas três arquivos yaml em vez de 2.
	  
	  ```
     $ ls -l ibm-edge-backup/20201026_215518/ 	  drwxr-xr-x  3 staff  staff     96 Oct 26 21:55 customresource 	  drwxr-xr-x  3 staff  staff     96 Oct 26 21:55 databaseresources 	  -rw-r--r--  1 staff  staff  10477 Oct 26 21:55 ibm-edge-auth-overrides.yaml 	  -rw-r--r--  1 staff  staff  11433 Oct 26 21:55 ibm-edge-auth-secret.yaml 	  -rw-r--r--  1 staff  staff   2499 Oct 26 21:55 ibm-edge-config.yaml
     ```
     {: codeblock}

### Procedimento de Restauração

**Nota**: quando bancos de dados locais são usados ou restaurados para bancos de dados remotos novos ou vazios, o design autônomo do {{site.data.keyword.ieam}} resulta em um desafio conhecido quando restaura backups para o {{site.data.keyword.mgmt_hub}}.

Para restaurar backups, um {{site.data.keyword.mgmt_hub}} idêntico deve ser instalado. Se esse novo hub for instalado sem a inserção de **ieam\_maintenance\_mode** durante a instalação inicial, provavelmente todos os nós de borda, que foram registrados anteriormente, cancelarão seus próprios registros. Isso exige que eles sejam registrados novamente.

Essa situação ocorre quando o nó de borda reconhece que não existe mais na troca porque o banco de dados agora está vazio. Ative **ieam\_maintenance\_mode** para evitar isso iniciando os recursos do banco de dados apenas para o {{site.data.keyword.mgmt_hub}}. Isso permite que a restauração seja concluída antes que os recursos do {{site.data.keyword.mgmt_hub}} restantes (que usam esses bancos de dados) sejam iniciados.

**Notas**: 

* Quando o seu arquivo **Recurso Customizado** foi feito o backup, ele foi modificado automaticamente para entrar **ieam\_maintenance\_mode** imediatamente após a reaplicação ao cluster.

* Os scripts de restauração automaticamente determinam que tipo de banco de dados foi usado anteriormente examinando o arquivo **\<path/to/backup\>/customresource/eamhub-cr.yaml**.

1. Como administrador do cluster, certifique-se de estar conectado ao cluster com **cloudctl login** ou **oc login** e que um backup válido tenha sido criado. No cluster no qual o backup foi feito, execute o comando a seguir para excluir o recurso customizado **eamhub** (isso assume que o nome padrão de **ibm-edge** foi usado para o recurso customizado):
	```
	oc delete eamhub ibm-edge
	```
	{: codeblock}

2. Verifique se **ieam\_maintenance\_mode** está configurado corretamente:
	```
	yq r ibm-edge-backup/20201026_215738/customresource/eamhub-cr.yaml 'items[0].spec.ieam_maintenance_mode'
	```
	{: codeblock}
	

3. Execute o script `ieam-restore-k8s-resources.sh` com a opção **-f** definida para apontar para seu backup:
	```
	ibm-eam-{{site.data.keyword.semver}}-bundle/tools/ieam-restore-k8s-resources.sh -f ibm-edge-backup/20201026_215738/
	```
	{: codeblock}

   Espere até que todos os pods de banco de dados e de SDO estejam em execução antes de prosseguir.
	
4. Edite o recurso customizado **ibm-edge** para pausar o operador:
	```
	oc patch eamhub ibm-edge --type merge --patch '{"spec":{"pause_control_loop": true}}'
	```
	{: codeblock}

5. Edite o conjunto stateful **ibm-edge-sdo** para aumentar o número de réplicas para **1**:
	```
	oc patch statefulset ibm-edge-sdo --type merge --patch '{"spec":{"replicas": 1}}'
	```
	{: codeblock}

6. Aguarde até que o pod **ibm-edge-sdo-0** entre em estado de execução:
	```
   	watch oc get pods -n ibm-edge | grep ibm-edge-sdo-0
   	```
	{: codeblock}

7. Execute o script `ieam-restore-data.sh` com a opção **-f** definida para apontar para o seu backup:
	```
	ibm-eam-{{site.data.keyword.semver}}-bundle/tools/ieam-restore-data.sh -f ibm-edge-backup/20201026_215738/
	```
	{: codeblock}
	
8. Após o script ser concluído e seus dados serem restaurados, remova a pausa no operador para continuar o loop de controle:
	```
	oc patch eamhub ibm-edge --type merge --patch '{"spec":{"pause_control_loop": false}}'
	```
	{: codeblock}

