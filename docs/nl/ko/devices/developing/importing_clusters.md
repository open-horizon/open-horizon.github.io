---

copyright:
  years: 2020
lastupdated: "2020-04-9"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 에이전트 설치 및 에지 클러스터 등록
{: #importing_clusters}

해당 에지 클러스터에 에이전트를 설치할 수 있습니다.

* Kubernetes
* 경량 소형 Kuberetes(테스트에 권장됨)

## Kubernetes 에지 클러스터에 에이전트 설치
{: #install_kube}

`agent-install.sh` 스크립트를 실행하여 자동화된 에이전트 설치를 사용할 수 있습니다. 

에이전트 설치 스크립트가 실행되는 환경에서 해당 단계를 따르십시오.

1. 관리자로부터 `agentInstallFiles-x86_64-Cluster.tar.gz` 파일 및 API 키를 얻으십시오. [에지 클러스터에 필요한 정보 및 파일 수집](preparing_edge_cluster.md)에서 이미 작성되었어야 합니다. 

2. 후속 단계에 대해 환경 변수에서 파일 이름을 설정하십시오.

   ```
   export AGENT_TAR_FILE=agentInstallFiles-x86_64-Cluster.tar.gz
   ```
   {: codeblock}

3. tar 파일에서 파일을 추출하십시오.

   ```
   tar -zxvf agentInstallFiles-x86_64-Cluster.tar.gz
   ```
   {: codeblock}

4. 해당 양식 중 하나일 수 있는, Horizon exchange 사용자 인증 정보를 내보내십시오.

   ```
  export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>
   ```
   {: codeblock}

   또는

   ```
   export HZN_EXCHANGE_USER_AUTH=<username>/<username>:<password>
   ```
   {: codeblock}

5. `agent-install.sh` 명령을 실행하여 Horizon 에이전트를 설치 및 구성하고 에지 클러스터를 등록하여 helloworld 샘플 에지 서비스를 실행하십시오.

   ```
   ./agent-install.sh -u $HZN_EXCHANGE_USER_AUTH -k agent-install.cfg  -D cluster -p
   ```
   {: codeblock}

   참고: 에이전트 설치 중에 다음 프롬프트가 표시될 수 있습니다. **horizon을 겹쳐쓰시겠습니까?[y/N]: **. **y**를 선택하고 **Enter**를 누르십시오. `agent-install.sh`가 구성을 올바르게 설정합니다.

6. (선택사항) 사용 가능한 `agent-install.sh` 플래그 설명을 보려면 다음을 실행하십시오. 

   ```
  ./agent-install.sh -h
   ```
   {: codeblock}

7. Kubernetes에서 실행 중인 에이전트 리소스를 나열하십시오. 이제 에이전트가 에지 클러스터에 설치되고 에지 클러스터가 등록되었으며 다음 에지 클러스터 리소스를 나열할 수 있습니다.

   * 네임스페이스:

   ```
   kubectl get namespace openhorizon-agent
   ```
   {: codeblock}

   * 배치:

   ```
   kubectl get deployment -n openhorizon-agent
   ```
   {: codeblock}

   에이전트 배치의 세부사항을 나열하려면 다음을 실행하십시오.

   ```
   kubectl get deployment -n openhorizon-agent -o yaml
   ```
   {: codeblock}

   * Configmap:

   ```
   kubectl get configmap openhorizon-agent-config -n openhorizon-agent -o yaml
   ```
   {: codeblock}

   * 시크릿:
   
   ```
   kubectl get secret openhorizon-agent-secrets -n openhorizon-agent -o yaml
   ```
   {: codeblock}

   * PersistentVolumeClaim:
   
   ```
   kubectl get pvc openhorizon-agent-pvc -n openhorizon-agent -o yaml
   ```
   {: codeblock}

   * 팟(Pod):

   ```
   kubectl get pod -n openhorizon-agent
   ```
   {: codeblock}

8. 로그를 보고 팟(Pod) ID를 얻은 후 다음을 실행하십시오. 

   ```
   kubectl logs <pod-id> -n openhorizon-agent
   ```
   {: codeblock}

9. 에이전트 컨테이너 내의 에이전트 컨테이너 내에서 `hzn` 명령을 실행하십시오.

   ```
   kubectl exec -it <pod-id> -n openhorizon-agent /bin/bash
   hzn --help
   ```
   {: codeblock}

10. `hzn` 명령 플래그 및 하위 명령을 탐색하십시오.

   ```
  hzn --help
   ```
   {: codeblock}

## 경량 소형 Kubernetes 에지 클러스터에 에이전트 설치

이 컨텐츠는 다음을 포함하여 로컬로 설치 및 구성할 수 있는 에이전트(microk8s), 경량 소형 kubernetes 클러스터를 설치하는 방법을 설명합니다.

* microk8s 설치 및 구성
* microk8s에서 에이전트 설치

### microk8s 설치 및 구성

1. microk8s를 설치하십시오.

   ```
   sudo snap install microk8s --classic --channel=1.14/stable
   ```
   {: codeblock}

2. microk8s.kubectl의 별명을 설정하십시오.

   참고: microk8s에서 테스트하려는 경우 `kubectl` 명령이 없는지 확인하십시오. 

  * MicroK8s는 네임스페이스 kubectl 명령을 사용하여 기존 kubectl 설치와의 충돌을 예방합니다. 기존 설치가 없는 경우 별명(`append to ~/.bash_aliases`)을 추가하는 것이 더 쉽습니다. 
   
   ```
   alias kubectl='microk8s.kubectl' 
   ```
   {: codeblock}
  
   * 그런 다음,

   ```
   source ~/.bash_aliases
   ```
   {: codeblock}

3. microk8s에서 dns 및 스토리지 모듈을 사용으로 설정하십시오.

   ```
   microk8s.enable dns storage
   ```
   {: codeblock}

4. microk8s에서 스토리지 클래스를 작성하십시오. 에이전트 설치 스크립트는 `gp2`를 지속적 볼륨 청구를 위한 기본 스토리지 클래스로 사용합니다. 이 스토리지 클래스는 에이전트를 설치하기 전에 microk8s 환경에서 작성해야 합니다. 에지 클러스터 에이전트가 다른 스토리지 클래스를 사용하는 경우 먼저 작성되어야 합니다. 

   다음은 `gp2`를 스토리지 클래스로 작성하는 예제입니다.  

   1. storageClass.yml 파일을 작성하십시오. 

      ```
      apiVersion: storage.k8s.io/v1
      kind: StorageClass
      metadata:
       name: gp2
      provisioner: microk8s.io/hostpath
      reclaimPolicy: Delete
      volumeBindingMode: Immediate
      ```
      {: codeblock}

   2. `kubectl` 명령을 사용하여 microk8s에서 storageClass 오브젝트를 작성하십시오.

      ```
      kubectl apply -f storageClass.yml
      ```
      {: codeblock}

### microk8s에서 에이전트 설치

해당 단계를 따라 microk8s에서 에이전트를 설치하십시오.

1. [1 - 3단계](#install_kube)를 완료하십시오.

2. `agent-install.sh` 명령을 실행하여 Horizon 에이전트를 설치 및 구성하고 에지 클러스터를 등록하여 helloworld 샘플 에지 서비스를 실행하십시오.

   ```
   source agent-install.sh -u $HZN_EXCHANGE_USER_AUTH -k agent-install.cfg  -D cluster -p "IBM/pattern-ibm.helloworld"
   ```
   {: codeblock}

   참고: 에이전트 설치 중에 다음 프롬프트가 표시될 수 있습니다. **horizon을 겹쳐쓰시겠습니까?[y/N]: **. **y**를 선택하고 **Enter**를 누르십시오. `agent-install.sh`가 구성을 올바르게 설정합니다.

## Kubernetes 경량 클러스터에서 에이전트를 제거하십시오. 

참고: 에이전트 설치 제거 스크립트가 이 릴리스에서 완료되지 않아 openhorizon-agent 네임스페이스를 삭제하여 에이전트 제거가 완료됩니다.

1. 네임스페이스를 삭제하십시오.

   ```
   kubectl delete namespace openhorizon-agent
   ```
   {: codeblock}

      참고: 네임스페이스 삭제가 "종료 중" 상태에서 중지하는 경우가 있습니다. 이 상황에서 [네임스페이스가 종료 중 상태에 빠짐 ![새 탭에서 열림](../../images/icons/launch-glyph.svg "새 탭에서 열림")](https://www.ibm.com/support/knowledgecenter/SSBS6K_3.1.1/troubleshoot/ns_terminating.html)의 내용을 참조하여 네임스페이스를 수동으로 삭제하십시오.

2. clusterrolebinding을 삭제하십시오. 

   ```
   kubectl delete clusterrolebinding openhorizon-agent-cluster-rule
   ```
   {: codeblock}

<!--If this installation was done as part of a prerequisite for {{site.data.keyword.edge_devices_notm}}, [return to continue that installation](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.0/devices/installing/install.html).-->
