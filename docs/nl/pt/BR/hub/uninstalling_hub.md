---

copyright:
years: 2020
lastupdated: "2020-10-30"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}



# Uninstall
{: #uninstalling_hub}

**Aviso:** a exclusão do recurso customizado **EamHub** remove imediatamente os recursos do qual o hub de gerenciamento do {{site.data.keyword.ieam}} depende, incluindo os componentes do IBM Cloud Platform Common Services. Certifique-se de que essa é sua intenção antes de prosseguir.

Consulte a página [backup e recuperação](../admin/backup_recovery.md) se esta desinstalação estiver sendo executada para facilitar a restauração a um estado anterior.

* Efetue login no cluster como um administrador de cluster usando **cloudctl** ou **oc login**, para o namespace no qual o seu operador do {{site.data.keyword.ieam}} está instalado.
* Execute o seguinte para excluir o recurso customizado (padrão **ibm-edge**):
  ```
  oc delete eamhub ibm-edge
  ```
  {: codeblock}
* Assegure-se de que todos os pods de hub de gerenciamento do {{site.data.keyword.ieam}} tenham sido finalizados e apenas os dois pods do operador que são mostrados aqui estejam em execução antes de continuar para a próxima etapa:
  ```
  $ oc get pods   NAME                                           READY   STATUS    RESTARTS   AGE   ibm-common-service-operator-794f868789-gdt2z   1/1     Running   0          20h   ibm-eamhub-operator-7455c95496-nf48z           1/1     Running   0          20h
  ```
* Desinstale o operador de hub de gerenciamento do {{site.data.keyword.ieam}} usando o console do cluster do OpenShift. Selecione o namespace onde seu operador do {{site.data.keyword.ieam}} está instalado e navegue até **Operadores** > **Operadores Instalados** > o ícone do menu overflow de **Hub de gerenciamento do IEAM** > **Desinstalar Operador**.
* Siga as instruções **Desinstalando todos os serviços** na página [Desinstalação](https://www.ibm.com/docs/en/cpfs?topic=online-uninstalling-foundational-services) do IBM Cloud Platform Common Services, substituindo quaisquer ocorrências do namespace **common-service** pelo namespace no qual o seu operador do {{site.data.keyword.ieam}} está instalado.
