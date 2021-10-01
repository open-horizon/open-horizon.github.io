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

# Instalando a CLI do hzn
{: #using_hzn_cli}

O comando `hzn` é a interface da linha de comandos do {{site.data.keyword.ieam}}. Ao instalar o software do agente {{site.data.keyword.ieam}} no nó de borda, a CLI do `hzn` é instalada automaticamente. Mas também é possível instalar a CLI `hzn` sem o agente. Por exemplo, um administrador de borda pode querer consultar a troca de {{site.data.keyword.ieam}} ou um desenvolvedor de borda pode querer testar com comandos `hzn` sem o agente completo.

1. Obtenha o pacote `horizon-cli`. Dependendo do que sua organização fez na etapa [Reunir arquivos de nó de borda](../hub/gather_files.md), é possível obter o pacote `horizon-cli` do CSS ou do arquivo tar `agentInstallFiles-<edge-node-type>.tar.gz`:

   * Acesse o pacote `horizon-cli` do CSS:

      * Se você ainda não tem uma chave API, crie uma seguindo as etapas em [Criando sua chave de API](../hub/prepare_for_edge_nodes.md). Configure as variáveis de ambiente dessa etapa:

         ```bash
         export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>   export HZN_ORG_ID=<your-exchange-organization>   export HZN_FSS_CSSURL=https://<ieam-management-hub-ingress>/edge-css/
         ```
         {: codeblock}

      * Configure `HOST_TYPE` para um destes valores que corresponde ao tipo de host no qual você está instalando o pacote `horizon-cli`:

         * linux-deb-amd64
         * linux-deb-arm64
         * linux-deb-armhf
         * linux-rpm-x86_64
         * linux-rpm-ppc64le
         * macos-pkg-x86_64

         ```bash
         HOST_TYPE=<host-type>
         ```
         {: codeblock}

      * Faça download do certificado, arquivo de configuração e arquivo tar contendo o pacote `horizon-cli` do CSS:

         ```bash
         curl -sSL -w "%{http_code}" -u "$HZN_ORG_ID/$HZN_EXCHANGE_USER_AUTH" -k -o agent-install.crt $HZN_FSS_CSSURL/api/v1/objects/IBM/agent_files/agent-install.crt/data          curl -sSL -w "%{http_code}" -u "$HZN_ORG_ID/$HZN_EXCHANGE_USER_AUTH" --cacert agent-install.crt -o agent-install.cfg $HZN_FSS_CSSURL/api/v1/objects/IBM/agent_files/agent-install.cfg/data          curl -sSL -w "%{http_code}" -u "$HZN_ORG_ID/$HZN_EXCHANGE_USER_AUTH" --cacert agent-install.crt -o horizon-agent-$HOST_TYPE.tar.gz $HZN_FSS_CSSURL/api/v1/objects/IBM/agent_files/horizon-agent-$HOST_TYPE.tar.gz/data
         ```
         {: codeblock}

      * Extraia o pacote `horizon-cli` de seu arquivo tar:

         ```bash
         rm -f horizon-cli*   # remova quaisquer versões anteriores          tar -zxvf horizon-agent-$HOST_TYPE.tar.gz
         ```
         {: codeblock}

   * Como alternativa, obtenha o pacote `horizon-cli` do arquivo tar `agentInstallFiles-<edge-node-type>.tar.gz`:

      * Obtenha o arquivo `agentInstallFiles-<edge-node-type>.tar.gz` do administrador de hub de gerenciamento, em que `<edge-node-type>` corresponde ao host no qual você está instalando o `horizon-cli`. Copie esse arquivo nesse host.

      * Descompacte o arquivo tar:

         ```bash
         tar -zxvf agentInstallFiles-<edge-device-type>.tar.gz
         ```
         {: codeblock}

2. Crie ou atualize `/etc/default/horizon`:

   ```bash
   sudo cp agent-install.cfg /etc/default/horizon    sudo cp agent-install.crt /etc/horizon    sudo sh -c "echo 'HZN_MGMT_HUB_CERT_PATH=/etc/horizon/agent-install.crt' >> /etc/default/horizon"
   ```
   {: codeblock}

3. Instale o pacote `horizon-cli`:

   * Confirme se a versão do pacote é a mesma do agente de dispositivo listado em [Components](../getting_started/components.md).

   * Em um distro baseado em Debian:

     ```bash
     sudo apt update && sudo apt install ./horizon-cli*.deb
     ```
     {: codeblock}

   * Em um distro baseado em RPM:

     ```bash
     sudo yum install ./horizon-cli*.rpm
     ```
     {: codeblock}

   * No {{site.data.keyword.macOS_notm}}:

     ```bash
     sudo security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain horizon-cli.crt      sudo installer -pkg horizon-cli-*.pkg -target /      pkgutil --pkg-info com.github.open-horizon.pkg.horizon-cli   # confirme a versão instalada
     ```
     {: codeblock}

## Desinstalando a CLI do hzn

Se você deseja remover o pacote `horizon-cli` de um host:

* Desinstale o `horizon-cli` a partir de um distro baseado em Debian:

  ```bash
  sudo apt-get remove horizon-cli
  ```
  {: codeblock}

* Desinstale o `horizon-cli` de um distro baseado em RPM:

  ```bash
  sudo yum remove horizon-cli
  ```
  {: codeblock}

* Ou desinstale o `horizon-cli` do {{site.data.keyword.macOS_notm}}:

  ```bash
  sudo horizon-cli-uninstall.sh
  ```
  {: codeblock}
