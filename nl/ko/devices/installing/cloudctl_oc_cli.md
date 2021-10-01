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

{{site.data.keyword.edge_notm}} 관리 허브와 엣지 클러스터를 관리하려면 명령행 도구가 필요합니다. 다음 단계를 통해 이를 설치하십시오.

* **cloudctl 및 kubectl:** {{site.data.keyword.edge_notm}} 웹 UI(`https://<CLUSTER_URL>/common-nav/cli`)에서 IBM Cloud Pak CLI(**cloudctl**) 및 kubernetes CLI(**kubeclt**)를 얻으십시오. 

  * {{site.data.keyword.macOS_notm}}에 **kubectl**을 설치하는 다른 방법은 [homebrew ![새 탭에서 열림](../../images/icons/launch-glyph.svg "새 탭에서 열림")](https://brew.sh/)를 사용하는 것입니다.
  
    ```bash
    brew install kubernetes-cli`
    ```
    {: codeblock}

* **oc:** [OpenShift 클라이언트 CLI(oc) ![새 탭에서 열기](../../images/icons/launch-glyph.svg "새 탭에서 열기")](https://mirror.openshift.com/pub/openshift-v4/clients/ocp/latest/)에서 {{site.data.keyword.open_shift_cp}} CLI를 얻으십시오.

  * {{site.data.keyword.macOS_notm}}에 **oc**를 설치하는 다른 방법은 [homebrew ![새 탭에서 열림](../../images/icons/launch-glyph.svg "새 탭에서 열림")](https://brew.sh/)를 사용하는 것입니다.
  
    ```bash
    brew install openshift-cli`
    ```
    {: codeblock}
