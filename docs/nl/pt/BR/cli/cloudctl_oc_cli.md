---

copyright:
  years: 2020
lastupdated: "2020-5-11"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Instalando o cloudctl, o kubectl e o oc
{: #cloudctl_oc_cli}

Siga estas etapas para instalar as ferramentas de linha de comandos que são necessárias para gerenciar aspectos do hub de gerenciamento e de clusters de borda do {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}):

## cloudctl

1. Navegue em sua IU da web do {{site.data.keyword.ieam}}: `https://<CLUSTER_URL>/common-nav/cli`

2. Expanda a seção **CLI do IBM Cloud Pak** e selecione o seu **S.O.**.

3. Copie o comando **curl** exibido e execute-o para fazer download do binário **cloudctl**.

4. Torne o arquivo executável e mova-o para **/usr/local/bin**:
  
   ```bash
   chmod 755 cloudctl-*    sudo mv cloudctl-* /usr/local/bin/cloudctl
   ```
   {: codeblock}

5. Certifique-se de que **/usr/local/bin** esteja em seu caminho e, em seguida, verifique se o **cloudctl** está funcionando:
  
   ```bash
   cloudctl -- help
   ```
   {: codeblock}

## oc

1. Faça o download do arquivo tar do {{site.data.keyword.open_shift_cp}} CLI em [OpenShift client CLI (oc)](https://mirror.openshift.com/pub/openshift-v4/clients/ocp/latest/). Selecione o arquivo **openshift-client-\*-\*.tar.gz** para seu sistema operacional.

2. Localize o arquivo tar transferido por download e descompacte-o:
  
   ```bash
   tar -zxvf openshift-client-*-*.tar.gz
   ```
   {: codeblock}

3. Mova o comando **oc** para **/usr/local/bin**:
  
   ```bash
   sudo mv oc /usr/local/bin/
   ```
   {: codeblock}

4. Certifique-se de que **/usr/local/bin** esteja em seu caminho e, em seguida, verifique se o **oc** está funcionando:
  
   ```bash
   oc --help
   ```
   {: codeblock}

Como alternativa, use [homebrew](https://brew.sh/) para instalar o **oc** no {{site.data.keyword.macOS_notm}}:
  
   ```bash
   brew install openshift-cli
   ```
   {: codeblock}

## Kubectl

Siga as instruções em [Instalar e configurar kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/).
