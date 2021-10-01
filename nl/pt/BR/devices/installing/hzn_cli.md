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

Ao instalar o software do agente {{site.data.keyword.ieam}} no nó de borda, a CLI do **hzn** é instalada automaticamente. No entanto, também é possível instalar a CLI do **hzn** sem o agente. Por exemplo, é possível que um administrador de borda queira consultar o {{site.data.keyword.ieam}} Exchange ou que um desenvolvedor de borda queira fazer testes usando comandos **hzn dev**.

1. Obtenha o arquivo **agentInstallFiles-&lt;edge-device-type&gt;.tar.gz** junto ao administrador de hub de gerenciamento, em que **&lt;edge-device-type&gt;** corresponde ao host no qual o **hzn** será instalado. Ele já deve ter sido criado em [Reúna as informações e os arquivos necessários para os dispositivos de borda](../../hub/gather_files.md#prereq_horizon). Copie este arquivo para o host no qual você deseja instalar o **hzn**.

2. Configure o nome do arquivo em uma variável de ambiente para etapas subsequentes:

   ```bash
   export AGENT_TAR_FILE=agentInstallFiles-<edge-device-type>.tar.gz
   ```
   {: codeblock}

3. Extraia o pacote da CLI do Horizon a partir do arquivo tar:

   ```bash
   tar -zxvf $AGENT_TAR_FILE 'horizon-cli*'
   ```
   {: codeblock}

   * Confirme se a versão do pacote é a mesma que a do agente de dispositivo listado em [Componentes](../getting_started/components.md).

4. Instale o pacote **horizon-cli**:

   * Em um distro baseado em Debian:

     ```bash
     sudo apt update && sudo apt install horizon-cli*.deb
     ```
     {: codeblock}

   * No {{site.data.keyword.macOS_notm}}:

     ```bash
     sudo installer -pkg horizon-cli-*.pkg -target /
     ```
     {: codeblock}

     Nota: no {{site.data.keyword.macOS_notm}}, também é possível instalar o arquivo de pacote horizon-cli a partir do Finder: dê um clique duplo no arquivo para abrir o instalador. Se você receber uma mensagem de erro
informando que "não é possível abrir o programa, pois ele provém de um dispositivo não identificado", clique com o botão direito no arquivo e selecione **Abrir**. Ao receber o prompt "Tem certeza de que deseja abrir o arquivo?", clique novamente em **Abrir**. Em seguida, siga os prompts para instalar o pacote da CLI do Horizon, assegurando-se de que seu ID tenha privilégios de administrador.

## Desinstalando a CLI do hzn

Se você deseja remover o pacote **horizon-cli** de um host:

* Desinstale o **horizon-cli** a partir de um distro baseado em Debian:

  ```bash
  sudo apt-get remove horizon-cli
  ```
  {: codeblock}

* Ou desinstale o **horizon-cli** do {{site.data.keyword.macOS_notm}}:

  * Abra a pasta do cliente hzn (/usr/local/bin) e arraste o aplicativo `hzn` para a Lixeira (no final do Dock).
