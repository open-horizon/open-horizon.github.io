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

# 에이전트 설치
{: #importing_clusters}

다음 유형의 Kubernetes 에지 클러스터 중 하나에 {{site.data.keyword.edge_notm}} 에이전트를 설치하여 시작하십시오.

* [{{site.data.keyword.ocp}}Kubernetes 에지 클러스터에 에이전트 설치](#install_kube)
* [k3s 및 microk8s 에지 클러스터에 에이전트 설치](#install_lite)

그런 다음 에지 서비스를 에지 클러스터에 배치하십시오.

* [에지 클러스터에 서비스 배치](#deploying_services)

에이전트를 제거해야 하는 경우 다음을 수행하십시오.

* [에지 클러스터에서 에이전트 제거](#remove_agent)

## {{site.data.keyword.ocp}} Kubernetes 에지 클러스터에 에이전트 설치
{: #install_kube}

이 절에서는 {{site.data.keyword.ocp}} 에지 클러스터에 {{site.data.keyword.ieam}} 에이전트를 설치하는 방법을 설명합니다. 에지 클러스터에 대한 관리자 액세스 권한을 가진 호스트에서 다음 단계를 수행하십시오.

1. **admin**으로 에지 클러스터에 로그인하십시오.

   ```bash
	oc login https://<API_ENDPOINT_HOST>:<PORT> -u <ADMIN_USER> -p <ADMIN_PASSWORD> --insecure-skip-tls-verify=true
   ```
   {: codeblock}

2. 에이전트 네임스페이스를 해당 기본값(또는 명시적으로 에이전트를 설치하려는 네임스페이스)으로 설정하십시오.

   ```bash
      export AGENT_NAMESPACE=openhorizon-agent
   ```
   {: codeblock}

3. 에이전트에서 사용하게 할 스토리지 클래스를 기본 제공 스토리지 클래스 또는 사용자가 작성한 클래스로 설정하십시오. 예를 들면, 다음과 같습니다.

   ```bash
   export EDGE_CLUSTER_STORAGE_CLASS=rook-ceph-cephfs-internal
   ```
   {: codeblock}

4. 에지 클러스터에 이미지 레지스트리를 설정하려면 다음과 같이 하나만 변경하여
[OpenShift 이미지 레지스트리 사용](../developing/container_registry.md##ocp_image_registry)의
2-8단계를 수행하십시오. 4단계에서 **OCP_PROJECT**를 **$AGENT_NAMESPACE**로 설정하십시오.

5. **agent-install.sh** 스크립트에서는 에지 클러스터 컨테이너 레지스트리에 {{site.data.keyword.ieam}}
에이전트를 저장합니다. 사용해야 하는 레지스트리 사용자, 비밀번호 및 전체 이미지 경로(태그 제외)를 설정하십시오.

   ```bash
   export EDGE_CLUSTER_REGISTRY_USERNAME=$OCP_USER
   export EDGE_CLUSTER_REGISTRY_TOKEN="$OCP_TOKEN"
   export IMAGE_ON_EDGE_CLUSTER_REGISTRY=$OCP_DOCKER_HOST/$OCP_PROJECT/amd64_anax_k8s
   ```
   {: codeblock}

   **참고:** {{site.data.keyword.ieam}} 에이전트 이미지는 에지 클러스터 Kubernetes에서 계속 액세스해야 하므로,
다시 시작하거나 다른 팟(pod)으로 이동해야 하는 경우에 대비하여 로컬 에지 클러스터 레지스트리에 저장됩니다.

6. Horizon Exchange 사용자 인증 정보를 가져오십시오.

   ```bash
  export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>
   ```
   {: codeblock}

7. 관리자로부터 **agentInstallFiles-x86_64-Cluster.tar.gz** 파일 및 API 키를 얻으십시오. [에지 클러스터에 필요한 정보 및 파일 수집](preparing_edge_cluster.md)에서 이미 작성되었어야 합니다. 

8. tar 파일로부터 **agent-install.sh** 스크립트를 추출하십시오.

   ```bash
   tar -zxvf agentInstallFiles-x86_64-Cluster.tar.gz agent-install.sh
   ```
   {: codeblock}

9. **agent-install.sh** 명령을 실행하여 Horizon 에이전트를 설치 및 구성하고 정책에 에지 클러스터를 등록하십시오.

   ```bash
   ./agent-install.sh -D cluster -z agentInstallFiles-x86_64-Cluster.tar.gz -d <node-id>
   ```
   {: codeblock}

   **참고:**
   * 사용 가능한 모든 플래그를 보려면 다음을 실행하십시오. **./agent-install.sh -h**
   * **agent-install.sh**로 인해 오류가 발생하여 완료되지 않는 경우 **agent-uninstall.sh**([에지 클러스터에서 에이전트 제거](#remove_agent) 참조)를 실행한 후 이 절의 단계를 반복하십시오.

10. 에이전트의 네임스페이스/프로젝트로 변경하고 에이전트 팟이 실행 중인지 확인하십시오.

   ```bash
   oc project $AGENT_NAMESPACE
   oc get pods
   ```
   {: codeblock}

11. 이제 에이전트가 에지 클러스터에 설치되므로, 에이전트와 연관된 Kubernetes 리소스를 숙지하려면
다음 명령을 실행할 수 있습니다.

   ```bash
   oc get namespace $AGENT_NAMESPACE
   oc project $AGENT_NAMESPACE   # ensure this is the current namespace/project
   oc get deployment -o wide
   oc get deployment agent -o yaml   # get details of the deployment
   oc get configmap openhorizon-agent-config -o yaml
   oc get secret openhorizon-agent-secrets -o yaml
   oc get pvc openhorizon-agent-pvc -o yaml   # persistent volume
   ```
   {: codeblock}

12. 정책에 맞게 에지 클러스터가 등록되었지만 사용자 지정 노드 정책이 없는 경우
에지 서비스를 배치하는 배치 정책이 없습니다. 이는 Horizon 예의 경우에 해당합니다. 에지 서비스가 이 에지 클러스터에 배치되도록 [에지 클러스터에 서비스 배치](#deploying_services)로
진행하여 노드 정책을 설정하십시오.

## k3s 및 microk8s 에지 클러스터에 에이전트 설치
{: #install_lite}

이 절에서는 k3s 또는 microk8s, 경량 및 소규모 Kubernetes 클러스터에 {{site.data.keyword.ieam}} 에이전트를 설치하는 방법을설명합니다.

1. **root**로 에지 클러스터에 로그인하십시오.

2. 관리자로부터 **agentInstallFiles-x86_64-Cluster.tar.gz** 파일 및 API 키를 얻으십시오. [에지 클러스터에 필요한 정보 및 파일 수집](preparing_edge_cluster.md)에서 이미 작성되었어야 합니다. 

3. tar 파일로부터 **agent-install.sh** 스크립트를 추출하십시오.

   ```bash
   tar -zxvf agentInstallFiles-x86_64-Cluster.tar.gz agent-install.sh
   ```
   {: codeblock}

4. Horizon Exchange 사용자 인증 정보를 가져오십시오.

   ```bash
  export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>
   ```
   {: codeblock}

5. **agent-install.sh** 스크립트에서는 에지 클러스터 이미지 레지스트리에 {{site.data.keyword.ieam}} 에이전트를 저장합니다. 사용해야 하는 전체 이미지 경로(태그 제외)를 설정하십시오. 예를 들면, 다음과 같습니다.

   ```bash
   export IMAGE_ON_EDGE_CLUSTER_REGISTRY=$REGISTRY_ENDPOINT/openhorizon-agent/amd64_anax_k8s
   ```
   {: codeblock}

   **참고:** {{site.data.keyword.ieam}} 에이전트 이미지는 에지 클러스터 Kubernetes에서 계속 액세스해야 하므로,
다시 시작하거나 다른 팟(pod)으로 이동해야 하는 경우에 대비하여 로컬 에지 클러스터 레지스트리에 저장됩니다.

6. 기본 스토리지 클래스를 사용하도록 **agent-install.sh**에 지시하십시오.

   * k3s:

      ```bash
      export EDGE_CLUSTER_STORAGE_CLASS=local-path
      ```
      {: codeblock}

   * microk8s:

      ```bash
      export EDGE_CLUSTER_STORAGE_CLASS=microk8s-hostpath
      ```
      {: codeblock}

7. **agent-install.sh** 명령을 실행하여 Horizon 에이전트를 설치 및 구성하고 정책에 에지 클러스터를 등록하십시오.

   ```bash
   ./agent-install.sh -D cluster -z agentInstallFiles-x86_64-Cluster.tar.gz -d <node-id>
   ```
   {: codeblock}

   **참고:**
   * 사용 가능한 모든 플래그를 보려면 다음을 실행하십시오. **./agent-install.sh -h**
   * **agent-install.sh**로 인해 오류가 발생하여 완료되지 않는 경우 **agent-install.sh**를 다시 실행하기 전에 **agent-uninstall.sh**([에지 클러스터에서 에이전트 제거](#remove_agent) 참조)를 실행하십시오.

8. 에이전트 팟(Pod)이 실행 중인지 확인하십시오.

   ```bash
   kubectl get namespaces
   kubectl -n openhorizon-agent get pods
   ```
   {: codeblock}

9. 정책에 맞게 에지 클러스터가 등록되었지만 사용자 지정 노드 정책이 없는 경우
에지 서비스를 배치하는 배치 정책이 없습니다. 이는 Horizon 예의 경우에 해당합니다. 에지 서비스가 이 에지 클러스터에 배치되도록 [에지 클러스터에 서비스 배치](#deploying_services)로
진행하여 노드 정책을 설정하십시오.

## 에지 클러스터에 서비스 배치
{: #deploying_services}

이 에지 클러스터에 노드 정책을 설정하면 배치 정책이 여기에 에지 서비스를 배치할 수 있습니다. 이 절에서는
해당 작업의 예를 보여줍니다.

1. `hzn` 명령을 보다 편리하게 실행할 수 있도록 일부 별명을 설정하십시오. (`hzn` 명령은 에이전트 컨테이너에 있지만, 이 별명을 통해 이 호스트에서
`hzn`을 실행할 수 있습니다.)

   ```bash
   cat << 'END_ALIASES' >> ~/.bash_aliases
   alias getagentpod='kubectl -n openhorizon-agent get pods --selector=app=agent -o jsonpath={.items[*].metadata.name}'
   alias hzn='kubectl -n openhorizon-agent exec -i $(getagentpod) -- hzn'
   END_ALIASES
   source ~/.bash_aliases
   ```
   {: codeblock}

2. 에지 노드가 구성({{site.data.keyword.ieam}} 관리 허브에 등록)되었는지 확인하십시오.

   ```bash
      hzn node list
   ```
   {: codeblock}

3. 에지 클러스터 에이전트를 테스트하려면 예제 helloworld 연산자와 서비스를 이 에지 노드에 배치하는
특성을 사용하여 노드 정책을 설정하십시오.

   ```bash
   cat << 'EOF' > operator-example-node.policy.json
   {
     "properties": [
       { "name": "openhorizon.example", "value": "operator" }
     ]
   }
   EOF

   cat operator-example-node.policy.json | hzn policy update -f-
   hzn policy list
   ```
   {: codeblock}

   **참고:**
   * 실제 **hzn** 명령은 에이전트 컨테이너 내부에서 실행되므로 입력 파일이 필요한 `hzn` 하위 명령의 경우 해당 컨텐츠가 컨테이너로 전송되도록 파일을 명령에 파이프해야 합니다.

4. 잠시 후 계약 및 실행 중인 에지 연산자 및 서비스 컨테이너를 확인하십시오.

   ```bash
   hzn agreement list
   kubectl -n openhorizon-agent get pods
   ```
   {: codeblock}

5. 이전 명령의 팟(Pod) ID를 사용하여 에지 연산자와 서비스 로그를 확인하십시오.

   ```bash
   kubectl -n openhorizon-agent logs -f <operator-pod-id>
   # control-c to get out
   kubectl -n openhorizon-agent logs -f <service-pod-id>
   # control-c to get out
   ```
   {: codeblock}

6. 또한 에이전트가 에지 서비스로 전달하는 환경 변수를 확인할 수도 있습니다.

   ```bash
   kubectl -n openhorizon-agent exec -i <service-pod-id> -- env | grep HZN_
   ```
   {: codeblock}

### 에지 클러스터에 배치되는 서비스 변경
{: #changing_services}

* 에지 클러스터에 배치되는 서비스를 변경하려면 노드 정책을 변경하십시오.

  ```bash
  cat <new-node-policy>.json | hzn policy update -f-
  hzn policy list
  ```
  {: codeblock}

   1-2분 후에 새 서비스가 이 에지 클러스터에 배치됩니다.

* 참고: 일부 VM 유형에서 microk8s를 사용하면 중지(대체)되는 서비스 팟(pod)이
**종료 중** 상태에 고착될 수 있습니다. 이 경우 다음을 실행하여 정리할 수 있습니다.

  ```bash
  kubectl delete pod <pod-id> -n openhorizon-agent --force --grace-period=0
  pkill -fe <service-process>
  ```
  {: codeblock}

* 정책이 아니라 패턴을 사용하여 에지 클러스터에서 서비스를 실행하려면 다음을 수행하십시오.

  ```bash
  hzn unregister -f
  hzn register -n $HZN_EXCHANGE_NODE_AUTH -p <pattern-name>
  ```
  {: codeblock}

## 에지 클러스터에서 에이전트 제거
{: #remove_agent}

에지 클러스터를 등록 취소하고 해당 클러스터에서 {{site.data.keyword.ieam}} 에이전트를 제거하려면 다음 단계를 수행하십시오.

1. tar 파일로부터 **agent-uninstall.sh** 스크립트를 추출하십시오.

   ```bash
   tar -zxvf agentInstallFiles-x86_64-Cluster.tar.gz agent-uninstall.sh
   ```
   {: codeblock}

2. Horizon Exchange 사용자 인증 정보를 가져오십시오.

   ```bash
  export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>
   ```
   {: codeblock}

3. 에이전트를 제거하십시오.

   ```bash
   ./agent-uninstall.sh -u $HZN_EXCHANGE_USER_AUTH -d
   ```
   {: codeblock}

참고: 네임스페이스 삭제가 "종료 중" 상태에서 중지하는 경우가 있습니다. 이 상황에서 [네임스페이스가 종료 중 상태에 빠짐 ![새 탭에서 열림](../../images/icons/launch-glyph.svg "새 탭에서 열림")](https://www.ibm.com/support/knowledgecenter/SSBS6K_3.1.1/troubleshoot/ns_terminating.html)의 내용을 참조하여 네임스페이스를 수동으로 삭제하십시오.
