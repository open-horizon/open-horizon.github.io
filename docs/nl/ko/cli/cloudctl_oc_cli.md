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

# cloudctl, kubectl 및 oc 설치
{: #cloudctl_oc_cli}

다음 단계를 수행하여 {{site.data.keyword.edge_notm}}({{site.data.keyword.ieam}}) 관리 허브 및 에지 클러스터의 측면을 관리하는 데 필요한 명령행 도구를 설치하십시오.

## cloudctl

1. 다음 위치에서 {{site.data.keyword.ieam}} 웹 UI를 찾아보십시오. `https://<CLUSTER_URL>/common-nav/cli`

2. **IBM Cloud Pak CLI** 섹션을 펼치고 **OS**를 선택하십시오.

3. 표시된 **curl** 명령을 복사하고 실행하여 **cloudctl** 2진을 다운로드하십시오.

4. 파일 실행 파일을 작성하고 **/usr/local/bin**으로 이동하십시오.
  
   ```bash
   chmod 755 cloudctl-*    sudo mv cloudctl-* /usr/local/bin/cloudctl
   ```
   {: codeblock}

5. **/usr/local/bin**이 PATH에 있는지 확인하고 **cloudctl**이 작업 중인지 확인하십시오.
  
   ```bash
   cloudctl --help
   ```
   {: codeblock}

## oc

1. [OpenShift 클라이언트 CLI(oc)](https://mirror.openshift.com/pub/openshift-v4/clients/ocp/latest/)에서 {{site.data.keyword.open_shift_cp}} CLI tar 파일을 다운로드하십시오. 운영 체제에 대한 **openshift-client-\*-\*.tar.gz** 파일을 선택하십시오.

2. 다운로드한 tar 파일을 찾아 압축 해제하십시오.
  
   ```bash
   tar -zxvf openshift-client-*-*.tar.gz
   ```
   {: codeblock}

3. **oc** 명령을 **/usr/local/bin**으로 이동하십시오.
  
   ```bash
   sudo mv oc /usr/local/bin/
   ```
   {: codeblock}

4. **/usr/local/bin**이 PATH에 있는지 확인하고 **oc**가 작업 중인지 확인하십시오.
  
   ```bash
   oc --help
   ```
   {: codeblock}

또는 [homebrew](https://brew.sh/)를 사용하여 {{site.data.keyword.macOS_notm}}에 **oc**를 설치하십시오.
  
   ```bash
   brew install openshift-cli
   ```
   {: codeblock}

## kubectl

[kubectl 설치 및 설정](https://kubernetes.io/docs/tasks/tools/install-kubectl/)의 지시사항을 따르십시오.
