---

copyright:
years: 2019, 2020
lastupdated: "2020-01-22"

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

As instruções a seguir guiam você no processo de instalação do software necessário em seu dispositivo de borda e do registro dele com o {{site.data.keyword.edge_notm}} {{site.data.keyword.ieam}}.

## Arquiteturas e sistemas operacionais suportados
{: #suparch-horizon}

O {{site.data.keyword.ieam}} suporta sistemas com as seguintes arquiteturas de hardware:

* Dispositivos ou máquinas virtuais {{site.data.keyword.linux_bit_notm}} que executam Ubuntu 18.x (bionic), Ubuntu 16.x (xenial), Debian 10 (buster) ou Debian 9 (stretch)
* {{site.data.keyword.linux_notm}} no ARM (32 bits), por exemplo, Raspberry Pi, que executa o Raspbian buster ou stretch
* {{site.data.keyword.linux_notm}} no ARM (64 bits), por exemplo NVIDIA Jetson Nano, TX1 ou TX2, que executam o Ubuntu 18.x (biônico)
* {{site.data.keyword.macOS_notm}}

## Dimensionando
{: #size}

O agente requer:

1. 100 MB de RAM (incluindo docker). A RAM aumenta acima desse valor em aproximadamente 100 K por contrato, além de qualquer memória adicional que seja necessária por cargas de trabalho que são executadas no dispositivo.
2. 400 MB de disco (incluindo docker). O disco aumenta acima dessa quantia com base no tamanho das imagens do contêiner que são usadas por cargas de trabalho e no tamanho dos objetos do modelo (vezes 2) que são implementados no dispositivo.

# Instalando o Agente
{: #installing_the_agent}

As instruções a seguir guiam você no processo de instalação do software necessário em seu dispositivo de borda e do registro dele com o {{site.data.keyword.ieam}}.

## Procedimentos
{: #install-config}

Para instalar e configurar o seu dispositivo de borda, clique no link que representa seu tipo de dispositivo de borda:

* [Dispositivos ou máquinas virtuais do {{site.data.keyword.linux_bit_notm}}](#x86-machines)
* [{{site.data.keyword.linux_notm}} no ARM (32 bits)](#arm-32-bit); por exemplo, Raspberry Pi executando Raspbian
* [{{site.data.keyword.linux_notm}} no ARM (64 bits)](#arm-64-bit); por exemplo, NVIDIA Jetson Nano, TX1 ou TX2
* [{{site.data.keyword.macOS_notm}}](#mac-os-x)

## Dispositivos ou máquinas virtuais do {{site.data.keyword.linux_bit_notm}}
{: #x86-machines}

### Requisitos de hardware;
{: #hard-req-x86}

* Máquina virtual ou dispositivo Intel ou AMD de 64-bits
* Uma conexão de Internet para o seu dispositivo (com fio ou wifi)
* (Opcional) Hardware de sensor: muitos aplicativos de insight do {{site.data.keyword.horizon}} podem requerer um hardware de sensor especializado.

### Procedimento
{: #proc-x86}

Prepare o dispositivo, instalando um {{site.data.keyword.linux_notm}} Debian ou Ubuntu. As instruções nesse conteúdo são baseadas em um dispositivo que usa o Ubuntu 18.x.

Agora que o dispositivo de borda está preparado, continue com [Instalando o agente](registration.md).

## {{site.data.keyword.linux_notm}} no ARM (32 bits)
{: #arm-32-bit}

### Requisitos de hardware;
{: #hard-req-pi}

* Raspberry Pi 3A+, 3B, 3B + ou 4 (preferencial)
* Raspberry Pi A+, B+, 2B, Zero-W ou Zero-WH
* Cartão de memória flash MicroSD (de 32 GB preferencialmente)
* Uma fonte de alimentação apropriada para o dispositivo (2 Amp ou mais preferencialmente)
* Uma conexão de Internet para o seu dispositivo (com fio ou wifi).
  Nota: alguns dispositivos podem requerer hardware extra para suportar wi-fi.
* (Opcional) Hardware de sensor: muitos aplicativos de insight do {{site.data.keyword.horizon}} podem requerer um hardware de sensor especializado.

### Procedimento
{: #proc-pi}

1. Prepare o dispositivo Raspberry Pi.
   1. Atualize a imagem do [Raspbian ![Abre em uma novaguia](../../images/icons/launch-glyph.svg "Abre em uma nova guia")](https://www.raspberrypi.org/downloads/raspbian/) {{site.data.keyword.linux_notm}} no seu cartão MicroSD.


      Para obter mais informações de como atualizar imagens do MicroSD de várias plataformas, consulte [Raspberry Pi Foundation ![Abre em uma nova guia](../../images/icons/launch-glyph.svg "Abre em uma nova guia")](https://www.raspberrypi.org/documentation/installation/installing-images/README.md).
      Estas instruções usam o Raspbian para as configurações de wi-fi e SSH.  

      **Aviso:** atualizar uma imagem no cartão MicroSD permanentemente apaga todos os dados que já estão no cartão.

   2. (Opcional) Se você planeja usar o wi-fi para conectar-se ao dispositivo, edite sua imagem recém-atualizada para fornecer as credenciais de wi-fi WPA2 apropriadas. 

      Se você planeja usar uma conexão de rede com fio, não é necessário concluir esta etapa.  

      No cartão MicroSD, crie um arquivo denominado `wpa_supplicant.conf` dentro da pasta no nível raiz que contém suas credenciais de wi-fi. Essas credenciais incluem seu nome SSID e sua passphrase da rede. Use o formato a seguir para o arquivo: 
      
      ```
      country=US
      ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev update_config=1
      network={
      ssid=“<your-network-ssid>”
      psk=“<your-network-passphrase”
      key_mgmt=WPA-PSK>
      }
      ```
      {: codeblock}

   3. (Opcional) Se você deseja ou precisa executar um dispositivo Raspberry Pi sem nenhum monitor ou teclado, é necessário ativar o acesso de conexão SSH para o dispositivo. O acesso SSH é desativado por padrão.

      Para ativar a conexão SSH, crie um arquivo vazio no cartão MicroSD denominado `ssh`. Inclua esse arquivo na pasta no nível raiz do cartão. A inclusão desse arquivo oferece a capacidade de conectar-se ao dispositivo com as credenciais padrão. 

   4. Desmonte o cartão MicroSD. Assegure-se de ejetar o cartão com segurança do dispositivo usado para editá-lo para que todas as mudanças sejam gravadas.

   5. Insira o cartão MicroSD no dispositivo Raspberry Pi. Conecte qualquer hardware de sensor opcional e o dispositivo à fonte de alimentação.

   6. Inicie o dispositivo.

   7. Mude a senha padrão do dispositivo. Nas imagens flash do Raspbian, a conta padrão usa o nome de login `pi` e a senha padrão `raspberry`.

      Efetue login nessa conta. Use o comando {{site.data.keyword.linux_notm}}`passwd` padrão para alterar a senha padrão:

      ```
      passwd
      Insira a nova senha do UNIX:  
      Retype new UNIX password:
      passwd: password updated successfully
      ```
      {: codeblock}

Agora que o dispositivo de borda está preparado, continue com [Instalando o agente](registration.md).

## {{site.data.keyword.linux_notm}} no ARM (64 bits)
{: #arm-64-bit}

### Requisitos de hardware;
{: #hard-req-nvidia}

* NVIDIA Jetson Nano ou TX2 (recomendado)
* NVIDIA Jetson TX1
* HDMI Business Monitor, hub USB, teclado USB, mouse USB
* Armazenamento: pelo menos 10 GB (SSD recomendado)
* Uma conexão de Internet para o seu dispositivo (com fio ou wifi)
* (Opcional) Hardware de sensor: muitos aplicativos de insight do {{site.data.keyword.horizon}} podem requerer um hardware de sensor especializado.

### Procedimento
{: #proc-nvidia}

1. Prepare o dispositivo NVIDIA Jetson.
   1. Instale o NVIDIA JetPack mais recente em seu dispositivo. Para obter informações adicionais, consulte
      * (TX1) [NVIDIA Jetson TX1 ![Abre em uma nova guia](../../images/icons/launch-glyph.svg "Abre em uma nova guia")](https://elinux.org/Jetson_TX1)
      * (TX2) [Harness AI no Edge com o Jetson TX2 Developer Kit ![Abre em uma nova guia](../../images/icons/launch-glyph.svg "Abre em uma nova guia")](https://developer.nvidia.com/embedded/jetson-tx2-developer-kit)
      * (Nano) [Introdução ao Jetson Nano Developer Kit ![Abre em uma nova guia](../../images/icons/launch-glyph.svg "Abre em uma nova guia")](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit)

      É necessário instalar este software e qualquer software obrigatório antes de instalar o software {{site.data.keyword.horizon}}.

   2. Mude a senha padrão. No procedimento de instalação do JetPack, a conta padrão usa o nome de login `nvidia` e a senha padrão `nvidia`. 

      Efetue login nessa conta. Use o comando {{site.data.keyword.linux_notm}}`passwd` padrão para alterar a senha padrão:

      ```
      passwd
      Insira a nova senha do UNIX:  
      Retype new UNIX password:
      passwd: password updated successfully
      ```
      {: codeblock}

Agora que o dispositivo de borda está preparado, continue com [Instalando o agente](registration.md).

## {{site.data.keyword.macOS_notm}}
{: #mac-os-x}

### Requisitos de hardware;
{: #hard-req-mac}

* Dispositivo {{site.data.keyword.inte}} Mac de 2010 ou mais recente de 64 bits

* A virtualização de MMU é necessária.
* MacOS X versão 10.11 ("El Capitan") ou posterior
* Uma conexão de Internet com a máquina (com fio ou wi-fi)
* (Opcional) Hardware de sensor: muitos aplicativos de insight do {{site.data.keyword.horizon}} podem requerer um hardware de sensor especializado.

### Procedimento
{: #proc-mac}

1. Prepare o dispositivo.
   1. Instale a **versão mais recente do Docker** em seu dispositivo. Para obter mais informações, consulte [Instalação do Docker ![Abre em uma nova guia](../../images/icons/launch-glyph.svg "Abre em uma nova guia")](https://docs.docker.com/docker-for-mac/install/).

   2. **Instalar socat**. É possível usar **qualquer** um dos métodos a seguir para instalar o socat:

      * [Use o Homebrew para instalar o socat ![Abre em uma nova guia](../../images/icons/launch-glyph.svg "Abre em uma nova guia")](https://brewinstall.org/install-socat-on-mac-with-brew/).
   
      * Se você já tiver o MacPorts instalado, use-o para instalar o socat:
        ```
        sudo port install socat
        ```
        {: codeblock}

## O que vem a seguir

* [Atualizando o agente](updating_the_agent.md)
* [Instalando o agente](registration.md)


## Informações relacionadas

* [Instalando o hub de gerenciamento](../../hub/offline_installation.md)
* [Instalação e registro manuais avançados de um agente](advanced_man_install.md)
