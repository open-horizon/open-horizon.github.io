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

# 에지 디바이스 준비
{: #installing_the_agent}

다음 지시사항은 에지 디바이스에서 필수 소프트웨어를 설치하고 {{site.data.keyword.edge_notm}}({{site.data.keyword.ieam}})에 등록하는 프로세스를 안내합니다.

## 지원되는 아키텍처 및 운영 체제
{: #suparch-horizon}

{{site.data.keyword.ieam}}에서는 다음 하드웨어 아키텍처로 아키텍처 및 운영 체제를 지원합니다.

* x86_64
   * Ubuntu 20.x(focal), Ubuntu 18.x(bionic), Debian 10(buster) 또는 Debian 9(stretch)를 실행하는 {{site.data.keyword.linux_bit_notm}} 디바이스 또는 가상 머신
   * {{site.data.keyword.rhel}} 8.1, 8.2 및 8.3
   * Fedora Workstation 32
   * CentOS 8.1, 8.2 및 8.3
   * SuSE 15 SP2
* ppc64le
   * {{site.data.keyword.linux_ppc64le_notm}} Ubuntu 20.x(focal) 또는 Ubuntu 18.x(bionic)를 실행하는 디바이스 또는 가상 머신
   * {{site.data.keyword.rhel}} 7.6, 7.9, 8.1, 8.2 및 8.3
* ARM(32비트)
   * Raspbian buster 또는 stretch를 실행하는 ARM(32비트)의 {{site.data.keyword.linux_notm}}(예: Raspberry Pi)
* ARM(64비트)
   * Ubuntu 18.x(bionic)을 실행하는 ARM(64비트)의 {{site.data.keyword.linux_notm}}(예: NVIDIA Jetson Nano, TX1 또는 TX2)
* Mac
   * {{site.data.keyword.macOS_notm}}

**참고**: 

* Fedora 또는 SuSE에 에지 디바이스의 설치는 [고급 수동 에이전트 설치 및 등록](../installing/advanced_man_install.md) 방법에서만 지원됩니다.
* CentOS 및 {{site.data.keyword.ieam}} {{site.data.keyword.version}}의 {{site.data.keyword.rhel}}에서는 컨테이너 엔진으로 Docker만 지원합니다.
* {{site.data.keyword.ieam}} {{site.data.keyword.version}}에서는 Docker를 사용하여 {{site.data.keyword.rhel}} 8.x를 실행하는 것을 지원하지만 {{site.data.keyword.rhel}}에서는 공식적으로 지원되지 않습니다.

## 크기 조정
{: #size}

에이전트에는 다음이 필요합니다.

* Docker를 포함하는 100MB RAM(Random Access Memory). RAM은 계약당 약 100K 및 디바이스에서 실행되는 워크로드에 필요한 추가 메모리만큼 이 크기를 증가시킵니다.
* 400MB 디스크(Docker 포함). 디스크는 디바이스에 배치된 모델 오브젝트 크기(2배) 및 워크로드에서 사용되는 컨테이너 이미지의 크기에 따라 이 크기를 증가시킵니다.

# 에이전트 설치
{: #installing_the_agent}

다음 지시사항은 에지 디바이스에서 필수 소프트웨어를 설치하고 {{site.data.keyword.ieam}}에 등록하는 프로세스를 안내합니다.

## 프로시저
{: #install-config}

에지 디바이스를 설치 및 구성하려면 에지 디바이스 유형을 나타내는 링크를 클릭하십시오.

* [{{site.data.keyword.linux_bit_notm}} 디바이스 또는 가상 머신](#x86-machines)
* [{{site.data.keyword.rhel}} 8.x 디바이스 또는 가상 머신](#rhel8)
* [{{site.data.keyword.linux_ppc64le_notm}} 디바이스 또는 가상 머신](#ppc64le-machines)
* [ARM의 {{site.data.keyword.linux_notm}}(32비트)](#arm-32-bit). 예: Raspbian을 실행하는 Raspberry Pi
* [ARM의 {{site.data.keyword.linux_notm}}(64비트)](#arm-64-bit). 예: NVIDIA Jetson Nano, TX1 또는 TX2
* [{{site.data.keyword.macOS_notm}}](#mac-os-x)

## {{site.data.keyword.linux_bit_notm}} 디바이스 또는 가상 머신
{: #x86-machines}

### 하드웨어 요구사항
{: #hard-req-x86}

* 64비트 Intel&reg;, AMD 디바이스 또는 가상 머신
* 디바이스에 대한 인터넷 연결(유선 또는 wifi)
* (선택사항) 센서 하드웨어: 많은 {{site.data.keyword.horizon}} 에지 서비스에는 특수한 센서 하드웨어가 필요합니다.

### 프로시저
{: #proc-x86}

Debian, {{site.data.keyword.rhel}} 7.x 또는 Ubuntu {{site.data.keyword.linux_notm}}을(를) 설치하여 디바이스를 준비하십시오. 이 컨텐츠의 지시사항은 Ubuntu 18.x를 사용하는 디바이스를 기반으로 합니다.

디바이스에 최신 버전의 Docker를 설치하십시오. 자세한 정보는 [Docker 설치](https://docs.docker.com/engine/install/ubuntu/)를 참조하십시오.

에지 서비스가 준비되었습니다. [에이전트 설치](registration.md)를 계속하십시오.

## {{site.data.keyword.rhel}} 8.x 디바이스 또는 가상 머신
{: #rhel8}

### 하드웨어 요구사항
{: #hard-req-rhel8}

* 64비트 Intel&reg; 디바이스, AMD 디바이스, ppc64le 디바이스 또는 가상 머신
* 디바이스에 대한 인터넷 연결(유선 또는 wifi)
* (선택사항) 센서 하드웨어: 많은 {{site.data.keyword.horizon}} 에지 서비스에는 특수한 센서 하드웨어가 필요합니다.

### 프로시저
{: #proc-rhel8}

{{site.data.keyword.rhel}} 8.x를 설치하여 디바이스를 준비하십시오.

Podman및 기타 사전에 포함된 패키지를 제거한 후 여기에 설명된 대로 Docker를 설치하십시오.

1. 다음과 같이 패키지를 설치 제거하십시오.
   ```
   yum remove buildah skopeo podman containers-common atomic-registries docker container-tools
   ```
   {: codeblock}

2. 나머지 아티팩트 &amp;TWBAMP; 파일을 제거하려면 다음을 수행하십시오.
   ```
   rm -rf /etc/containers/* /var/lib/containers/* /etc/docker /etc/subuid* /etc/subgid*
   ```
   {: codeblock}

3. 연관된 컨테이너 스토리지를 삭제하십시오.
   ```
   cd ~ && rm -rf /.local/share/containers/
   ```
   {: codeblock}

4. [Docker CENTOS 설치](https://docs.docker.com/engine/install/centos/)에 대한 지시사항을 따라 Docker를 설치하십시오.

5. 기본적으로 부팅 시 시작하도록 Docker를 구성하고 다른 [Docker 설치 후 단계](https://docs.docker.com/engine/install/linux-postinstall/)를 수행하십시오.
   ```
   sudo systemctl enable docker.service sudo systemctl enable containerd.service
   ```
   {: codeblock}

에지 서비스가 준비되었습니다. [에이전트 설치](registration.md)를 계속하십시오.

## {{site.data.keyword.linux_ppc64le_notm}} 디바이스 또는 가상 머신
{: #ppc64le-machines}

### 하드웨어 요구사항
{: #hard-req-ppc64le}

* ppc64le 디바이스 또는 가상 머신
* 디바이스에 대한 인터넷 연결(유선 또는 wifi)
* (선택사항) 센서 하드웨어: 많은 {{site.data.keyword.horizon}} 에지 서비스에는 특수한 센서 하드웨어가 필요합니다.

### 프로시저
{: #proc-ppc64le}

{{site.data.keyword.rhel}}을(를) 설치하여 디바이스를 준비하십시오.

디바이스에 최신 버전의 Docker를 설치하십시오. 

에지 서비스가 준비되었습니다. [에이전트 설치](registration.md)를 계속하십시오.

## ARM의 {{site.data.keyword.linux_notm}}(32비트)
{: #arm-32-bit}

### 하드웨어 요구사항
{: #hard-req-pi}

* Raspberry Pi 3A+, 3B, 3B+ 또는 4(선호)
* Raspberry Pi A+, B+, 2B, Zero-W 또는 Zero-WH
* MicroSD 플래시 카드(32GB 선호)
* 디바이스에 적합한 전원 공급 장치(2Amp 이상이 선호됨)
* 디바이스에 대한 인터넷 연결(유선 또는 wifi).
  **참고**: 일부 디바이스의 경우 wifi를 지원하기 위해 추가적인 하드웨어가 필요합니다.
* (선택사항) 센서 하드웨어: 많은 {{site.data.keyword.horizon}} 에지 서비스에는 특수한 센서 하드웨어가 필요합니다.

### 프로시저
{: #proc-pi}

1. Raspberry Pi 디바이스를 준비하십시오.
   1. [Raspbian](https://www.raspberrypi.org/downloads/raspbian/) {{site.data.keyword.linux_notm}} 이미지를 MicroSD 카드에 플래시하십시오.

      여러 운영 체제에서 MicroSD 이미지를 플래시하는 방법에 대한 자세한 정보는 [Raspberry Pi Foundation](https://www.raspberrypi.org/documentation/installation/installing-images/README.md)을 참조하십시오.
      이러한 지시사항에서는 wifi 및 SSH 구성을 위해 Raspbian을 사용합니다.  

      **경고:** 이미지를 MicroSD 카드에 플래시하면 이미 카드에 있는 데이터가 영구적으로 지워집니다.

   2. (선택사항) wifi를 사용하여 디바이스에 연결하려면 새로 플래시된 메모리를 편집하여 적절한 WPA2 wifi 인증 정보를 제공하십시오. 

      유선 네트워크 연결을 사용하려는 경우 이 단계를 완료하지 않아도 됩니다.  

      MicroSD 카드에서 루트 레벨 폴더 내에 wifi 인증 정보가 포함된 `wpa_supplicant.conf`라는 파일을 작성하십시오. 이러한 인증 정보에는 네트워크 SSID 이름 및 비밀번호 문구가 포함됩니다. 파일에 다음 형식을 사용하십시오. 
      
      ```
      country=US       ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev update_config=1       network={
      ssid=“<your-network-ssid>”       psk=“<your-network-passphrase”       key_mgmt=WPA-PSK>       }
      ```
      {: codeblock}

   3. (선택사항) 모니터 또는 키보드 없이 Raspberry Pi 디바이스를 실행하려고 하거나 실행해야 하는 경우 디바이스에 대한 SSH 연결 액세스를 사용으로 설정해야 합니다. 기본적으로 SSH 액세스는 사용할 수 없습니다.

      SSH 연결을 사용으로 설정하려면 MicroSD 카드에 `ssh`라는 비어 있는 파일을 작성하십시오. 카드의 루트 레벨 폴더에 이 파일을 포함하십시오. 이 파일이 포함되어 있으면 기본 인증 정보로 디바이스에 연결할 수 있는 기능이 제공됩니다. 

   4. MicroSD 카드를 마운트 해제하십시오. 모든 변경사항이 기록되도록 카드를 편집하기 위해 사용 중인 디바이스에서 카드를 안전하게 꺼내야 합니다.

   5. MicroSD 카드를 Raspberry Pi 디바이스에 삽입하십시오. 선택적 센서 하드웨어를 연결하고 디바이스를 전원 공급 장치에 연결하십시오.

   6. 디바이스를 시작하십시오.

   7. 디바이스의 기본 비밀번호를 변경하십시오. Raspbian 플래시 이미지에서 기본 계정은 로그인 이름 `pi` 및 기본 비밀번호 `raspberry`를 사용합니다.

      이 계정에 로그인하십시오. 기본 비밀번호를 사용하려면 표준 {{site.data.keyword.linux_notm}} `passwd` 명령을 사용하십시오.

      ```
      passwd       Enter new UNIX password:  
      Retype new UNIX password:        passwd: password updated successfully
      ```
      {: codeblock}
     
   8. 디바이스에 최신 버전의 Docker를 설치하십시오. 자세한 정보는 [Docker 설치](https://docs.docker.com/engine/install/debian/)를 참조하십시오. 

에지 서비스가 준비되었습니다. [에이전트 설치](registration.md)를 계속하십시오.

## ARM의 {{site.data.keyword.linux_notm}}(64비트)
{: #arm-64-bit}

### 하드웨어 요구사항
{: #hard-req-nvidia}

* NVIDIA Jetson Nano 또는 TX2(권장)
* NVIDIA Jetson TX1
* HDMI 비즈니스 모니터, USB 허브, USB 키보드, USB 마우스
* 스토리지: 최소 10GB(SSD가 권장됨)
* 디바이스에 대한 인터넷 연결(유선 또는 wifi)
* (선택사항) 센서 하드웨어: 많은 {{site.data.keyword.horizon}} 에지 서비스에는 특수한 센서 하드웨어가 필요합니다.

### 프로시저
{: #proc-nvidia}

1. NVIDIA Jetson 디바이스를 준비하십시오.
   1. 디바이스에 최신 NVIDIA JetPack을 설치하십시오. 자세한 정보는 다음을 참조하십시오.
      * (TX1) [Jetson TX1](https://elinux.org/Jetson_TX1)
      * (TX2) [Jetson TX2 개발자 킷을 사용하는 에지의 Harness AI](https://developer.nvidia.com/embedded/jetson-tx2-developer-kit)
      * (Nano) [Jetson Nano 개발자 킷 시작하기](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit)

      {{site.data.keyword.horizon}} 소프트웨어를 설치하기 전에 이 소프트웨어와 모든 필수 소프트웨어를 설치해야 합니다.

   2. 기본 비밀번호를 변경하십시오. JetPack 설치 프로시저에서 기본 계정은 로그인 이름 `nvidia` 및 기본 비밀번호 `nvidia`를 사용합니다. 

      이 계정에 로그인하십시오. 기본 비밀번호를 사용하려면 표준 {{site.data.keyword.linux_notm}} `passwd` 명령을 사용하십시오.

      ```
      passwd       Enter new UNIX password:  
      Retype new UNIX password:        passwd: password updated successfully
      ```
      {: codeblock}
      
   3. 디바이스에 최신 버전의 Docker를 설치하십시오. 자세한 정보는 [Docker 설치](https://docs.docker.com/engine/install/debian/)를 참조하십시오. 

에지 서비스가 준비되었습니다. [에이전트 설치](registration.md)를 계속하십시오.

## {{site.data.keyword.macOS_notm}}
{: #mac-os-x}

### 하드웨어 요구사항
{: #hard-req-mac}

* 2010 이상 64비트 {{site.data.keyword.intel}} Mac 디바이스
* MMU 가상화가 필요합니다.
* MacOS X 버전 10.11("El Capitan") 이상
* 머신에 대한 인터넷 연결(유선 또는 wifi)
* (선택사항) 센서 하드웨어: 많은 {{site.data.keyword.horizon}} 에지 서비스에는 특수한 센서 하드웨어가 필요합니다.
### 프로시저
{: #proc-mac}

1. 디바이스를 준비하십시오.
   1. 디바이스에 최신 버전의 Docker를 설치하십시오. 자세한 정보는 [Docker 설치](https://docs.docker.com/docker-for-mac/install/)를 참조하십시오.

   2. **socat을 설치**하십시오. 다음 방법 중 하나를 사용하여 socat을 설치할 수 있습니다.

      * [Homebrew를 사용하여 socat을 설치](https://brewinstall.org/install-socat-on-mac-with-brew/)하십시오.
   
      * MacPorts가 이미 설치되어 있는 경우 이를 사용하여 socat을 설치하십시오.
        ```
        sudo port install socat
        ```
        {: codeblock}

## 다음 수행할 작업

* [에이전트 설치](registration.md)
* [에이전트 업데이트](updating_the_agent.md)

## 관련 정보

* [{{site.data.keyword.ieam}} 설치](../hub/online_installation.md)
* [에이전트의 고급 수동 설치 및 등록](advanced_man_install.md)
