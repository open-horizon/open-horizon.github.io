---

copyright:
years: 2019, 2020, 2021
lastupdated: "2021-09-01"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Preparando um dispositivo de borda
{: #installing_the_agent}

As instruções a seguir orientam você no processo de instalação do software necessário em seu dispositivo de borda e como registrá-lo com o {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}).

## Arquiteturas e sistemas operacionais suportados
{: #suparch-horizon}

O {{site.data.keyword.ieam}} oferece suporte a arquiteturas e sistemas operacionais com as arquiteturas de hardware a seguir:

* x86_64
   * Dispositivos {{site.data.keyword.linux_bit_notm}}  ou máquinas virtuais que executam Ubuntu 20.x (focal), Ubuntu 18.x (biônico), Debian 10 (buster), Debian 9 (extensão)
   * {{site.data.keyword.rhel}} 8.1, 8.2 e 8.3
   * Fedora Workstation 32
   * CentOS 8.1, 8.2 e 8.3
   * SuSE 15 SP2
* ppc64le
   * Dispositivos ou máquinas virtuais do {{site.data.keyword.linux_ppc64le_notm}} que executam o Ubuntu 20.x (focal) ou o Ubuntu 18.x (bionic)
   * {{site.data.keyword.rhel}} 7.6, 7.9, 8.1, 8.2 e 8.3
* ARM (32 bits)
   * {{site.data.keyword.linux_notm}} no ARM (32 bits), por exemplo, Raspberry Pi, que executa o Raspbian buster ou stretch
* ARM (64 bits)
   * {{site.data.keyword.linux_notm}} no ARM (64 bits), por exemplo NVIDIA Jetson Nano, TX1 ou TX2, que executam o Ubuntu 18.x (biônico)
* Mac
   * {{site.data.keyword.macOS_notm}}

**Notas**: 

* A instalação de dispositivos de borda com Fedora ou SuSE é suportada apenas pelo método de [Registro e instalação manual avançada do agente](../installing/advanced_man_install.md).
* CentOS e {{site.data.keyword.rhel}} no {{site.data.keyword.ieam}} {{site.data.keyword.version}} apenas suportam o Docker como um mecanismo de contêiner.
* Enquanto o {{site.data.keyword.ieam}} {{site.data.keyword.version}} oferece suporte à execução do {{site.data.keyword.rhel}} 8.x com o Docker, ele é oficialmente não suportado pelo {{site.data.keyword.rhel}}.

## Dimensionando
{: #size}

O agente requer:

* 100 MB de memória de acesso aleatório (RAM), incluindo Docker. A RAM aumenta essa quantidade em aproximadamente 100 K por contrato mais qualquer memória adicional exigida pelas cargas de trabalho executadas no dispositivo.
* 400 MB de disco (incluindo Docker). O disco aumenta essa quantidade com base no tamanho das imagens de contêiner que são usadas por cargas de trabalho e no tamanho dos objetos modelo (vezes 2) que são implementados no dispositivo.

# Instalando o agente
{: #installing_the_agent}

As instruções a seguir guiam você no processo de instalação do software necessário em seu dispositivo de borda e do registro dele com o {{site.data.keyword.ieam}}.

## Procedimentos
{: #install-config}

Para instalar e configurar o seu dispositivo de borda, clique no link que representa seu tipo de dispositivo de borda:

* [{{site.data.keyword.linux_bit_notm}} dispositivos ou máquinas virtuais](#x86-machines)
* [Dispositivos ou máquinas virtuais do {{site.data.keyword.rhel}} 8.x](#rhel8)
* [{{site.data.keyword.linux_ppc64le_notm}} dispositivos ou máquinas virtuais](#ppc64le-machines)
* [{{site.data.keyword.linux_notm}} no ARM (32 bits)](#arm-32-bit); por exemplo, Raspberry Pi executando Raspbian
* [{{site.data.keyword.linux_notm}} no ARM (64 bits)](#arm-64-bit); por exemplo, NVIDIA Jetson Nano, TX1 ou TX2
* [{{site.data.keyword.macOS_notm}}](#mac-os-x)

## Dispositivos ou máquinas virtuais do {{site.data.keyword.linux_bit_notm}}
{: #x86-machines}

### Requisitos de hardware
{: #hard-req-x86}

* Dispositivo ou máquina virtual Intel&reg; ou AMD de 64 bits
* Uma conexão de Internet para o seu dispositivo (com fio ou wifi)
* (opcional) Hardware de sensor: muitos serviços de borda do {{site.data.keyword.horizon}} requerem hardware de sensor especializado.

### Procedimento
{: #proc-x86}

Prepare seu dispositivo instalando um Debian, {{site.data.keyword.rhel}} 7.x ou Ubuntu {{site.data.keyword.linux_notm}}. As instruções nesse conteúdo são baseadas em um dispositivo que usa o Ubuntu 18.x.

Instale a versão mais recente do Docker em seu dispositivo. Para obter mais informações, consulte  [ Instalar Docker ](https://docs.docker.com/engine/install/ubuntu/).

Agora que o dispositivo de borda está preparado, continue com [Instalando o agente](registration.md).

## Dispositivos ou máquinas virtuais do {{site.data.keyword.rhel}} 8.x
{: #rhel8}

### Requisitos de hardware
{: #hard-req-rhel8}

* Dispositivo Intel&reg; de 64 bits, dispositivo AMD, dispositivo ppc64le ou máquina virtual
* Uma conexão de Internet para o seu dispositivo (com fio ou wifi)
* (opcional) Hardware de sensor: muitos serviços de borda do {{site.data.keyword.horizon}} requerem hardware de sensor especializado.

### Procedimento
{: #proc-rhel8}

Prepare seu dispositivo instalando o {{site.data.keyword.rhel}} 8.x.

Remova o Podman e outros pacotes pré-incluídos e, em seguida, instale o Docker conforme descrito aqui.

1. Desinstale os pacotes:
   ```
   yum remove buildah skopeo podman containers-common atomic-registries docker container-tools
   ```
   {: codeblock}

2. Remover artefatos restantes &amp;TWBAMP; arquivos:
   ```
   rm -rf /etc/containers/* /var/lib/containers/* /etc/docker /etc/subuid* /etc/subgid*
   ```
   {: codeblock}

3. Exclua qualquer armazenamento de contêiner associado:
   ```
   cd ~ && rm -rf /.local/share/containers/
   ```
   {: codeblock}

4. Instale o Docker seguindo as instruções em [Instalação do Docker CENTOS](https://docs.docker.com/engine/install/centos/).

5. Configure o Docker para iniciar na inicialização por padrão e siga qualquer outra [etapa de pós-instalação do Docker](https://docs.docker.com/engine/install/linux-postinstall/).
   ```
   sudo systemctl enable docker.service    sudo systemctl enable containerd.service
   ```
   {: codeblock}

Agora que o dispositivo de borda está preparado, continue com [Instalando o agente](registration.md).

## Dispositivos ou máquinas virtuais do {{site.data.keyword.linux_ppc64le_notm}}
{: #ppc64le-machines}

### Requisitos de hardware
{: #hard-req-ppc64le}

* Dispositivo ou máquina virtual do ppc64le
* Uma conexão de Internet para o seu dispositivo (com fio ou wifi)
* (opcional) Hardware de sensor: muitos serviços de borda do {{site.data.keyword.horizon}} requerem hardware de sensor especializado.

### Procedimento
{: #proc-ppc64le}

Prepare seu dispositivo instalando o {{site.data.keyword.rhel}}.

Instale a versão mais recente do Docker em seu dispositivo. 

Agora que o dispositivo de borda está preparado, continue com [Instalando o agente](registration.md).

## {{site.data.keyword.linux_notm}} no ARM (32 bits)
{: #arm-32-bit}

### Requisitos de hardware
{: #hard-req-pi}

* Raspberry Pi 3A+, 3B, 3B + ou 4 (preferencial)
* Raspberry Pi A+, B+, 2B, Zero-W ou Zero-WH
* Cartão de memória flash MicroSD (de 32 GB preferencialmente)
* Uma fonte de alimentação apropriada para o dispositivo (2 Amp ou mais preferencialmente)
* Uma conexão de internet para o seu dispositivo (com fio ou wi-fi).
  **Nota**: alguns dispositivos requerem hardware extra para suportar wi-fi.
* (opcional) Hardware de sensor: muitos serviços de borda do {{site.data.keyword.horizon}} requerem hardware de sensor especializado.

### Procedimento
{: #proc-pi}

1. Prepare o dispositivo Raspberry Pi.
   1. Atualizar a imagem [Raspbian](https://www.raspberrypi.org/downloads/raspbian/) {{site.data.keyword.linux_notm}} para o seu cartão MicroSD.

      Para obter mais informações sobre como atualizar as imagens MicroSD de muitos sistemas operacionais, consulte [Raspberry Pi Foundation](https://www.raspberrypi.org/documentation/installation/installing-images/README.md).
      Estas instruções usam o Raspbian para as configurações de wi-fi e SSH.  

      **Aviso:** atualizar uma imagem no cartão MicroSD permanentemente apaga todos os dados que já estão no cartão.

   2. (opcional) Se você estiver planejando o uso do wi-fi para se conectar com seu dispositivo, edite a imagem recém-atualizada para fornecer as credenciais de wi-fi apropriadas do WPA2. 

      Se você planeja usar uma conexão de rede com fio, não é necessário concluir esta etapa.  

      No cartão MicroSD, crie um arquivo denominado `wpa_supplicant.conf` dentro da pasta no nível raiz que contém suas credenciais de wi-fi. Essas credenciais incluem seu nome SSID e sua passphrase da rede. Use o formato a seguir para o arquivo: 
      
      ```
      country=US       ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev update_config=1       network={
      ssid=“<your-network-ssid>”       psk=“<your-network-passphrase”       key_mgmt=WPA-PSK>       }
      ```
      {: codeblock}

   3. (opcional) Se você deseja ou precisa executar um dispositivo Raspberry Pi sem monitor ou teclado, é necessário habilitar o acesso de conexão SSH ao seu dispositivo. O acesso SSH está indisponível por padrão.

      Para ativar a conexão SSH, crie um arquivo vazio no cartão MicroSD denominado `ssh`. Inclua esse arquivo na pasta no nível raiz do cartão. A inclusão desse arquivo oferece a capacidade de conectar-se ao dispositivo com as credenciais padrão. 

   4. Desmonte o cartão MicroSD. Assegure-se de ejetar o cartão com segurança do dispositivo usado para editá-lo para que todas as mudanças sejam gravadas.

   5. Insira o cartão MicroSD no dispositivo Raspberry Pi. Conecte qualquer hardware de sensor opcional e o dispositivo à fonte de alimentação.

   6. Inicie o dispositivo.

   7. Mude a senha padrão do dispositivo. Nas imagens flash do Raspbian, a conta padrão usa o nome de login `pi` e a senha padrão `raspberry`.

      Efetue login nessa conta. Use o comando {{site.data.keyword.linux_notm}}`passwd` padrão para alterar a senha padrão:

      ```
      passwd       Insira a nova senha do UNIX:  
      Retype new UNIX password:       passwd: password updated successfully
      ```
      {: codeblock}
     
   8. Instale a versão mais recente do Docker em seu dispositivo. Para obter mais informações, consulte  [ Instalar Docker ](https://docs.docker.com/engine/install/debian/). 

Agora que o dispositivo de borda está preparado, continue com [Instalando o agente](registration.md).

## {{site.data.keyword.linux_notm}} no ARM (64 bits)
{: #arm-64-bit}

### Requisitos de hardware
{: #hard-req-nvidia}

* NVIDIA Jetson Nano ou TX2 (recomendado)
* NVIDIA Jetson TX1
* HDMI Business Monitor, hub USB, teclado USB, mouse USB
* Armazenamento: pelo menos 10 GB (SSD recomendado)
* Uma conexão de Internet para o seu dispositivo (com fio ou wifi)
* (opcional) Hardware de sensor: muitos serviços de borda do {{site.data.keyword.horizon}} requerem hardware de sensor especializado.

### Procedimento
{: #proc-nvidia}

1. Prepare o dispositivo NVIDIA Jetson.
   1. Instale o NVIDIA JetPack mais recente em seu dispositivo. Para obter informações adicionais, consulte
      * (TX1) [Jetson TX1](https://elinux.org/Jetson_TX1)
      * (TX2) [Harness AI no Edge com o Jetson TX2 Developer Kit](https://developer.nvidia.com/embedded/jetson-tx2-developer-kit)
      * (Nano) [Introdução ao Jetson Nano Developer Kit](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit)

      É necessário instalar este software e qualquer software obrigatório antes de instalar o software {{site.data.keyword.horizon}}.

   2. Mude a senha padrão. No procedimento de instalação do JetPack, a conta padrão usa o nome de login `nvidia` e a senha padrão `nvidia`. 

      Efetue login nessa conta. Use o comando {{site.data.keyword.linux_notm}}`passwd` padrão para alterar a senha padrão:

      ```
      passwd       Insira a nova senha do UNIX:  
      Retype new UNIX password:       passwd: password updated successfully
      ```
      {: codeblock}
      
   3. Instale a versão mais recente do Docker em seu dispositivo. Para obter mais informações, consulte  [ Instalar Docker ](https://docs.docker.com/engine/install/debian/). 

Agora que o dispositivo de borda está preparado, continue com [Instalando o agente](registration.md).

## {{site.data.keyword.macOS_notm}}
{: #mac-os-x}

### Requisitos de hardware
{: #hard-req-mac}

* Dispositivo {{site.data.keyword.intel}} Mac de 2010 ou mais recente de 64 bits
* A virtualização de MMU é necessária.
* MacOS X versão 10.11 ("El Capitan") ou posterior
* Uma conexão de Internet com a máquina (com fio ou wi-fi)
* (opcional) Hardware de sensor: muitos serviços de borda do {{site.data.keyword.horizon}} requerem hardware de sensor especializado.
### Procedimento
{: #proc-mac}

1. Prepare o dispositivo.
   1. Instale a versão mais recente do Docker em seu dispositivo. Para obter mais informações, consulte  [ Instalar Docker ](https://docs.docker.com/docker-for-mac/install/).

   2. **Instalar socat**. É possível usar qualquer um dos métodos a seguir para instalar o socat:

      * [Use Homebrew para instalar socat](https://brewinstall.org/install-socat-on-mac-with-brew/).
   
      * Se o MacPorts já estiver instalado, use-o para instalar o socat:
        ```
        sudo port install socat
        ```
        {: codeblock}

## O que vem depois

* [Instalando o agente](registration.md)
* [Atualizando o agente](updating_the_agent.md)

## Informações relacionadas

* [Instalação do {{site.data.keyword.ieam}}](../hub/online_installation.md)
* [Instalação e registro manuais avançados de um agente](advanced_man_install.md)
