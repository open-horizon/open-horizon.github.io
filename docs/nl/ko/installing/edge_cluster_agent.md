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

**참고**: {{site.data.keyword.ieam}} 에이전트 설치에는 에지 클러스터에 대한 클러스터 관리자 액세스 권한이 필요합니다.

다음 유형의 Kubernetes 에지 클러스터 중 하나에 {{site.data.keyword.edge_notm}} 에이전트를 설치하여 시작하십시오.

* [{{site.data.keyword.ocp}}Kubernetes 에지 클러스터에 에이전트 설치](#install_kube)
* [k3s 및 microk8s 에지 클러스터에 에이전트 설치](#install_lite)

그런 다음 에지 서비스를 에지 클러스터에 배치하십시오.

* [에지 클러스터에 서비스 배치](#deploying_services)

에이전트를 제거해야 하는 경우 다음을 수행하십시오.

* [에지 클러스터에서 에이전트 제거](../using_edge_services/removing_agent_from_cluster.md)

## {{site.data.keyword.ocp}} Kubernetes 에지 클러스터에 에이전트 설치
{: #install_kube}

이 컨텐츠는 {{site.data.keyword.ocp}} 에지 클러스터에 {{site.data.keyword.ieam}} 에이전트를 설치하는 방법을 설명합니다. 에지 클러스터에 대한 관리자 액세스 권한이 있는 호스트에서 다음 단계를 수행하십시오.

1. **admin**으로 에지 클러스터에 로그인하십시오.

   ```bash
   oc login https://<api_endpoint_host>:<port> -u <admin_user> -p <admin_password> --insecure-skip-tls-verify=true
   ```
   {: codeblock}

2. [API 키 작성](../hub/prepare_for_edge_nodes.md)의 단계를 완료하지 않은 경우 지금 수행하십시오. 이 프로세스는 API 키를 작성하고 일부 파일을 찾은 후 에지 노드 설정 시 필요한 환경 변수 값을 수집합니다. 이 에지 클러스터에서 동일한 환경 변수를 설정하십시오.

  ```bash
  export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>   export HZN_ORG_ID=<your-exchange-organization>   export HZN_FSS_CSSURL=https://<ieam-management-hub-ingress>/edge-css/
  ```
  {: codeblock}

3. 에이전트 네임스페이스를 해당 기본값(또는 명시적으로 에이전트를 설치하려는 네임스페이스)으로 설정하십시오.

   ```bash
   export AGENT_NAMESPACE=openhorizon-agent
   ```
   {: codeblock}

4. 에이전트에서 사용할 스토리지 클래스를 기본 제공 스토리지 클래스 또는 사용자가 작성한 클래스로 설정하십시오. 다음 두 개의 명령 중 첫 번째 명령으로 사용 가능한 스토리지 클래스를 확인한 후 사용할 스토리지 클래스의 이름을 두 번째 명령에 대체할 수 있습니다. 하나의 스토리지 클래스가 `(default)`로 레이블 지정되어야 합니다.

   ```bash
   oc get storageclass    export EDGE_CLUSTER_STORAGE_CLASS=<rook-ceph-cephfs-internal>
   ```
   {: codeblock}

5. {{site.data.keyword.open_shift}} 이미지 레지스트리의 기본 라우트가 클러스터 외부에서 액세스할 수 있도록 작성되었는지 여부를 판별하십시오.

   ```bash
   oc get route default-route -n openshift-image-registry --template='{{ .spec.host }}'
   ```
   {: codeblock}

   명령 응답이 **default-route**를 찾을 수 없음을 표시하는 경우 이를 노출해야 합니다(세부사항은 [레지스트리 노출](https://docs.openshift.com/container-platform/4.6/registry/securing-exposing-registry.html) 참조).

   ```bash
   oc patch configs.imageregistry.operator.openshift.io/cluster --patch '{"spec":{"defaultRoute":true}}' --type=merge
   ```
   {: codeblock}

6. 사용할 저장소 라우트 이름을 검색하십시오.

   ```bash
   export OCP_IMAGE_REGISTRY=`oc get route default-route -n openshift-image-registry --template='{{ .spec.host }}'`
   ```
   {: codeblock}

7. 이미지를 저장할 새 프로젝트를 작성하십시오.

   ```bash
   export OCP_PROJECT=$AGENT_NAMESPACE    oc new-project $OCP_PROJECT
   ```
   {: codeblock}

8. 사용자가 선택한 이름으로 서비스 계정을 작성하십시오.

   ```bash
   export OCP_USER=<service-account-name>    oc create serviceaccount $OCP_USER
   ```
   {: codeblock}

9. 현재 프로젝트의 서비스 계정에 역할을 추가하십시오.

   ```bash
   oc policy add-role-to-user edit system:serviceaccount:$OCP_PROJECT:$OCP_USER
   ```
   {: codeblock}

10. 서비스 액세스 토큰을 다음 환경 변수로 설정하십시오.

   ```bash
   export OCP_TOKEN=`oc serviceaccounts get-token $OCP_USER`
   ```
   {: codeblock}

11. {{site.data.keyword.open_shift}} 인증서를 가져오고 Docker가 이를 신뢰하게 하십시오.

   ```bash
   echo | openssl s_client -connect $OCP_IMAGE_REGISTRY:443 -showcerts | sed -n "/-----BEGIN CERTIFICATE-----/,/-----END CERTIFICATE-----/p" > ca.crt
   ```
   {: codeblock}

   {{site.data.keyword.linux_notm}}의 경우:

   ```bash
   mkdir -p /etc/docker/certs.d/$OCP_IMAGE_REGISTRY    cp ca.crt /etc/docker/certs.d/$OCP_IMAGE_REGISTRY    systemctl restart docker.service
   ```
   {: codeblock}

   {{site.data.keyword.macOS_notm}}의 경우:

   ```bash
   mkdir -p ~/.docker/certs.d/$OCP_IMAGE_REGISTRY    cp ca.crt ~/.docker/certs.d/$OCP_IMAGE_REGISTRY
   ```
   {: codeblock}

   {{site.data.keyword.macOS_notm}}에서 데스크탑 메뉴 표시줄의 오른쪽에 있는 Docker 데스크탑 아이콘을 통해 드롭 다운 메뉴에서 **다시 시작**을 클릭하여 Docker를 다시 시작하십시오.

12. {{site.data.keyword.ocp}} Docker 호스트에 로그인하십시오.

   ```bash
   echo "$OCP_TOKEN" | docker login -u $OCP_USER --password-stdin $OCP_IMAGE_REGISTRY
   ```
   {: codeblock}

13. 이미지 레지스트리 액세스를 위한 추가 신뢰 저장소를 구성하십시오.   

    ```bash
    oc create configmap registry-config --from-file=$OCP_IMAGE_REGISTRY=ca.crt -n openshift-config
    ```
    {: codeblock}

14. 새 `registry-config`를 편집하십시오.

    ```bash
    oc edit image.config.openshift.io cluster
    ```
    {: codeblock}

15. `spec:` 섹션을 업데이트하십시오.

    ```bash
    spec:       additionalTrustedCA:        name: registry-config
    ```
    {: codeblock}

16. **agent-install.sh** 스크립트는 {{site.data.keyword.ieam}} 에이전트를 에지 클러스터 컨테이너 레지스트리에 저장합니다. 다음과 같이 레지스트리 사용자, 비밀번호 및 전체 이미지 경로(태그 제외)를 설정하십시오.

   ```bash
   export EDGE_CLUSTER_REGISTRY_USERNAME=$OCP_USER    export EDGE_CLUSTER_REGISTRY_TOKEN="$OCP_TOKEN"    export IMAGE_ON_EDGE_CLUSTER_REGISTRY=$OCP_IMAGE_REGISTRY/$OCP_PROJECT/amd64_anax_k8s
   ```
   {: codeblock}

   **참고**: {{site.data.keyword.ieam}} 에이전트 이미지는 에지 클러스터 Kubernetes에서 계속 액세스해야 하기 때문에 다시 시작하거나 다른 팟(Pod)으로 이동하는 경우에 대비하여 로컬 에지 클러스터 레지스트리에 저장됩니다.

17. CSS(Cloud Sync Service)에서 **agent-install.sh** 스크립트를 다운로드하여 실행 가능하게 하십시오.

   ```bash
   curl -u "$HZN_ORG_ID/$HZN_EXCHANGE_USER_AUTH" -k -o agent-install.sh $HZN_FSS_CSSURL/api/v1/objects/IBM/agent_files/agent-install.sh/data    chmod +x agent-install.sh
   ```
   {: codeblock}

18. **agent-install.sh**를 실행하여 CSS에서 필요한 파일을 가져오고 {{site.data.keyword.horizon}} 에이전트를 설치 및 구성하고 에지 클러스터를 정책과 함께 등록하십시오.

   ```bash
   ./agent-install.sh -D cluster -i 'css:'
   ```
   {: codeblock}

   **참고**:
   * 사용 가능한 모든 플래그를 보려면 다음을 실행하십시오. **./agent-install.sh -h**
   * 오류로 인해 **agent-install.sh**가 실패하는 경우 오류를 정정하고 **agent-install.sh**를 다시 실행하십시오. 이 방법이 작동하지 않으면 **agent-install.sh**를 다시 실행하기 전에 **agent-uninstall.sh**를 실행하십시오([에지 클러스터에서 에이전트 제거](../using_edge_services/removing_agent_from_cluster.md) 참조).

19. 에이전트 네임스페이스(프로젝트라고도 함)를 변경하고 에이전트 팟(Pod)이 실행 중인지 확인하십시오.

   ```bash
   oc project $AGENT_NAMESPACE    oc get pods
   ```
   {: codeblock}

20. 에이전트가 에지 클러스터에 설치되었으므로 에이전트와 연관된 Kubernetes 리소스를 숙지하려는 경우 다음 명령을 실행할 수 있습니다.

   ```bash
   oc get namespace $AGENT_NAMESPACE    oc project $AGENT_NAMESPACE   # ensure this is the current namespace/project    oc get deployment -o wide    oc get deployment agent -o yaml   # get details of the deployment    oc get configmap openhorizon-agent-config -o yaml    oc get secret openhorizon-agent-secrets -o yaml    oc get pvc openhorizon-agent-pvc -o yaml   # persistent volume
   ```
   {: codeblock}

21. 종종 정책에 맞게 에지 클러스터가 등록되었지만 사용자 지정 노드 정책이 없는 경우 에지 서비스를 배치하는 배치 정책이 없습니다. 이는 Horizon 예의 경우에 해당합니다. 에지 서비스가 이 에지 클러스터에 배치되도록 [에지 클러스터에 서비스 배치](#deploying_services)로 진행하여 노드 정책을 설정하십시오.

## k3s 및 microk8s 에지 클러스터에 에이전트 설치
{: #install_lite}

이 컨텐츠는 [k3s](https://k3s.io/) 또는 [microk8s](https://microk8s.io/), 경량 및 소형 Kubernetes 클러스터에 {{site.data.keyword.ieam}} 에이전트를 설치하는 방법에 대해 설명합니다.

1. **root**로 에지 클러스터에 로그인하십시오.

2. [API 키 작성](../hub/prepare_for_edge_nodes.md)의 단계를 완료하지 않은 경우 지금 수행하십시오. 이 프로세스는 API 키를 작성하고 일부 파일을 찾은 후 에지 노드 설정 시 필요한 환경 변수 값을 수집합니다. 이 에지 클러스터에서 동일한 환경 변수를 설정하십시오.

  ```bash
  export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>   export HZN_ORG_ID=<your-exchange-organization>   export HZN_FSS_CSSURL=https://<ieam-management-hub-ingress>/edge-css/
  ```
  {: codeblock}

3. **agent-install.sh** 스크립트를 새 에지 클러스터로 복사하십시오.

4. **agent-install.sh** 스크립트에서는 에지 클러스터 이미지 레지스트리에 {{site.data.keyword.ieam}} 에이전트를 저장합니다. 사용해야 하는 전체 이미지 경로(태그 제외)를 설정하십시오. 예를 들면, 다음과 같습니다.

   * k3s:

      ```bash
      REGISTRY_ENDPOINT=$(kubectl get service docker-registry-service | grep docker-registry-service | awk '{print $3;}'):5000       export IMAGE_ON_EDGE_CLUSTER_REGISTRY=$REGISTRY_ENDPOINT/openhorizon-agent/amd64_anax_k8s
      ```
      {: codeblock}

   * microk8s:

      ```bash
      export IMAGE_ON_EDGE_CLUSTER_REGISTRY=localhost:32000/openhorizon-agent/amd64_anax_k8s
      ```
      {: codeblock}

   **참고**: {{site.data.keyword.ieam}} 에이전트 이미지는 에지 클러스터 Kubernetes에서 계속 액세스해야 하기 때문에 다시 시작하거나 다른 팟(Pod)으로 이동하는 경우에 대비하여 로컬 에지 클러스터 레지스트리에 저장됩니다.

5. 기본 스토리지 클래스를 사용하도록 **agent-install.sh**에 지시하십시오.

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

6. **agent-install.sh**를 실행하여 CSS(Cloud Sync Service)에서 필요한 파일을 가져오고 {{site.data.keyword.horizon}} 에이전트를 설치 및 구성한 후 정책과 함께 에지 클러스터를 등록하십시오.

   ```bash
   ./agent-install.sh -D cluster -i 'css:'
   ```
   {: codeblock}

   **참고**:
   * 사용 가능한 모든 플래그를 보려면 다음을 실행하십시오. **./agent-install.sh -h**
   * 오류가 발생하여 **agent-install.sh**가 완료되지 않으면 표시된 오류를 수정하고 **agent-install.sh**를 다시 실행하십시오. 이 방법이 작동하지 않으면 **agent-install.sh**를 다시 실행하기 전에 **agent-uninstall.sh**를 실행하십시오([에지 클러스터에서 에이전트 제거](../using_edge_services/removing_agent_from_cluster.md) 참조).

7. 에이전트 팟(Pod)이 실행 중인지 확인하십시오.

   ```bash
   kubectl get namespaces    kubectl -n openhorizon-agent get pods
   ```
   {: codeblock}

8. 일반적으로 정책에 맞게 에지 클러스터가 등록되었지만 사용자 지정 노드 정책이 없는 경우 에지 서비스를 배치하는 배치 정책이 없습니다. 이는 예상되는 상황입니다. 에지 서비스가 이 에지 클러스터에 배치되도록 [에지 클러스터에 서비스 배치](#deploying_services)로 진행하여 노드 정책을 설정하십시오.

## 에지 클러스터에 서비스 배치
{: #deploying_services}

이 에지 클러스터에 노드 정책을 설정하면 배치 정책이 여기에 에지 서비스를 배치할 수 있습니다. 이 컨텐츠는 이 작업을 수행하는 예를 보여줍니다.

1. `hzn` 명령을 보다 편리하게 실행할 수 있도록 일부 별명을 설정하십시오. (`hzn` 명령은 에이전트 컨테이너에 있지만, 이 별명을 통해 이 호스트에서 `hzn`을 실행할 수 있습니다.)

   ```bash
   cat << 'END_ALIASES' >> ~/.bash_aliases    alias getagentpod='kubectl -n openhorizon-agent get pods --selector=app=agent -o jsonpath={.items[*].metadata.name}'    alias hzn='kubectl -n openhorizon-agent exec -i $(getagentpod) -- hzn'    END_ALIASES    source ~/.bash_aliases
   ```
   {: codeblock}

2. 에지 노드가 구성({{site.data.keyword.ieam}} 관리 허브에 등록)되었는지 확인하십시오.

   ```bash
   hzn node list
   ```
   {: codeblock}

3. 에지 클러스터 에이전트를 테스트하려면 예제 helloworld 연산자와 서비스를 이 에지 노드에 배치하는 특성을 사용하여 노드 정책을 설정하십시오.

   ```bash
   cat << 'EOF' > operator-example-node.policy.json    {
     "properties": [
       { "name": "openhorizon.example", "value": "operator" }      ]
   }    EOF

   cat operator-example-node.policy.json | hzn policy update -f-    hzn policy list
   ```
   {: codeblock}

   **참고**:
   * 실제 **hzn** 명령은 에이전트 컨테이너 내부에서 실행되므로 입력 파일이 필요한 `hzn` 하위 명령의 경우 해당 컨텐츠가 컨테이너로 전송되도록 파일을 명령에 파이프해야 합니다.

4. 잠시 후 계약 및 실행 중인 에지 연산자 및 서비스 컨테이너를 확인하십시오.

   ```bash
   hzn agreement list    kubectl -n openhorizon-agent get pods
   ```
   {: codeblock}

5. 이전 명령의 팟(Pod) ID를 사용하여 에지 연산자와 서비스 로그를 확인하십시오.

   ```bash
   kubectl -n openhorizon-agent logs -f <operator-pod-id>    # control-c to get out    kubectl -n openhorizon-agent logs -f <service-pod-id>    # control-c to get out
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
  cat <new-node-policy>.json | hzn policy update -f-   hzn policy list
  ```
  {: codeblock}

   1-2분 후에 새 서비스가 이 에지 클러스터에 배치됩니다.

* **참고**: microk8s를 사용하는 일부 VM에서는 중지(대체)되는 서비스 팟(Pod)이 **종료 중** 상태에 고착될 수 있습니다. 이러한 경우 다음을 실행하십시오.

  ```bash
  kubectl delete pod <pod-id> -n openhorizon-agent --force --grace-period=0   pkill -fe <service-process>
  ```
  {: codeblock}

* 정책이 아니라 패턴을 사용하여 에지 클러스터에서 서비스를 실행하려면 다음을 수행하십시오.

  ```bash
  hzn unregister -f   hzn register -n $HZN_EXCHANGE_NODE_AUTH -p <pattern-name>
  ```
  {: codeblock}
