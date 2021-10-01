---

copyright:
years: 2020
lastupdated: "2020-4-24"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 에지 클러스터 준비
{: #preparing_edge_cluster}

에지 클러스터를 설치하고 {{site.data.keyword.edge_notm}} 에이전트를 준비하려면 다음 태스크를 수행하십시오.

이러한 에지 클러스터 중 하나를 설치하고 {{site.data.keyword.edge_notm}} 에이전트에 대해 준비하십시오.
* [OCP 에지 클러스터 설치](#install_ocp_edge_cluster)
* [k3s 에지 클러스터 설치 및 구성](#install_k3s_edge_cluster)
* [microk8s 에지 클러스터 설치 및 구성](#install_microk8s_edge_cluster)(개발 및 테스트용이며 프로덕션에는 권장되지 않음)

## OCP 에지 클러스터 설치
{: #install_ocp_edge_cluster}

1. [{{site.data.keyword.open_shift_cp}} 문서](https://docs.openshift.com/container-platform/4.6/welcome/index.html)의 설치 지시사항을 따라 OCP를 설치하십시오. ({{site.data.keyword.ieam}}은 x86_64 플랫폼에서만 OCP를 지원합니다.)

2. OCP 에지 클러스터를 관리하는 관리자 호스트에 Kubernetes CLI(**kubectl**), Openshift 클라이언트 CLI(**oc**) 및 Docker를 설치하십시오. 이는 에이전트 설치 스크립트를 실행하는 것과 동일한 호스트입니다. 자세한 정보는 [cloudctl, kubectl 및 oc 설치](../cli/cloudctl_oc_cli.md)를 참조하십시오.

## k3s 에지 클러스터 설치 및 구성
{: #install_k3s_edge_cluster}

이 컨텐츠는 Ubuntu 18.04에 작은 경량 Kubernetes 클러스터인 k3s(rancher)를 설치하는 방법을 제공합니다. 자세한 정보는 [k3s 문서](https://rancher.com/docs/k3s/latest/en/)를 참조하십시오.

**참고**: kubectl이 설치된 경우 다음 단계를 완료하기 전에 이를 설치 제거하십시오.

1. **root**로 로그인하거나 `sudo -i`를 사용하여 **root**로 올리십시오.

2. 시스템의 전체 호스트 이름에는 두 개 이상의 점이 포함되어야 합니다. 전체 호스트 이름을 확인하십시오.

   ```bash
   hostname
   ```
    {: codeblock}

   시스템의 전체 호스트 이름에 점이 두 개 미만 포함되어 있는 경우 호스트 이름을 변경하십시오.

   ```bash
   hostnamectl set-hostname <your-new-hostname-with-2-dots>
   ```
   {: codeblock}

   자세한 정보는 [github 문제](https://github.com/rancher/k3s/issues/53)를 참조하십시오.

3. k3s를 설치하십시오.

   ```bash
   curl -sfL https://get.k3s.io | sh -
   ```
   {: codeblock}

4. 이미지 레지스트리 서비스를 작성하십시오.
   1. 다음 컨텐츠를 사용하여 **k3s-persistent-claim.yml**이라는 파일을 작성하십시오.
      ```yaml       apiVersion: v1       kind: PersistentVolumeClaim       metadata:         name: docker-registry-pvc       spec:         storageClassName: "local-path"         accessModes:
          - ReadWriteOnce         resources:           requests:             storage: 10Gi
      ```
      {: codeblock}

   2. 지속적 볼륨 청구를 작성하십시오.

      ```bash
      kubectl apply -f k3s-persistent-claim.yml
      ```
      {: codeblock}

   3. 지속적 볼륨 청구가 작성되었고 "보류" 상태인지 확인하십시오.

      ```bash
      kubectl get pvc
      ```
      {: codeblock}

   4. 다음 컨텐츠를 사용하여 **k3s-registry-deployment.yml**이라는 파일을 작성하십시오.

      ```yaml
      apiVersion: apps/v1       kind: Deployment       metadata:         name: docker-registry         labels:           app: docker-registry       spec:         replicas: 1         selector:           matchLabels:             app: docker-registry         template:           metadata:             labels:               app: docker-registry           spec:             volumes:
            - name: registry-pvc-storage               persistentVolumeClaim:                 claimName: docker-registry-pvc             containers:
            - name: docker-registry               image: registry               ports:
              - containerPort: 5000               volumeMounts:
              - name: registry-pvc-storage                 mountPath: /var/lib/registry
      ---
      apiVersion: v1       kind: Service       metadata:         name: docker-registry-service       spec:         selector:           app: docker-registry         type: NodePort         ports:
          - protocol: TCP             port: 5000
      ```
      {: codeblock}

   5. 레지스트리 배치 및 서비스를 작성하십시오.

      ```bash
      kubectl apply -f k3s-registry-deployment.yml
      ```
      {: codeblock}

   6. 서비스가 작성되었는지 확인하십시오.

      ```bash
      kubectl get deployment       kubectl get service
      ```
      {: codeblock}

   7. 레지스트리 엔드포인트를 정의하십시오.

      ```bash
      export REGISTRY_ENDPOINT=$(kubectl get service docker-registry-service | grep docker-registry-service | awk '{print $3;}'):5000       cat << EOF >> /etc/rancher/k3s/registries.yaml       mirrors:         "$REGISTRY_ENDPOINT":           endpoint:
            - "http://$REGISTRY_ENDPOINT"       EOF
      ```
      {: codeblock}

   8. k3s를 다시 시작하여 **/etc/rancher/k3s/registries.yaml**의 변경사항을 적용하십시오.

      ```bash
      systemctl restart k3s
      ```
      {: codeblock}

5. 비보안 레지스트리로 docker에 이 레지스트리를 정의하십시오.

   1. **/etc/docker/daemon.json**을 작성하거나 여기에 추가하십시오(`<registry-endpoint>`를 이전 단계에서 얻은 `$REGISTRY_ENDPOINT` 환경 변수의 값으로 대체함).

      ```json
      {
        "insecure-registries": [ "<registry-endpoint>" ]       }
      ```
      {: codeblock}

   2. (선택사항) 필요한 경우 Docker가 시스템에 있는지 확인하십시오.

      ```bash
      curl -fsSL get.docker.com | sh
      ```
      {: codeblock}     

   3. docker를 다시 시작하여 변경사항을 적용하십시오.

      ```bash
      systemctl restart docker
      ```
      {: codeblock}

## microk8s 에지 클러스터 설치 및 구성
{: #install_microk8s_edge_cluster}

이 컨텐츠에서는 Ubuntu 18.04에 경량의 소형 Kubernetes 클러스터인 microk8s를 설치하는 방법에 대한 요약을 제공합니다. (자세한 지시사항은 [microk8s 문서](https://microk8s.io/docs)를 참조하십시오.)

**참고**: 이 유형의 에지 클러스터는 개발 및 테스트를 위한 것입니다. 단일 작업자 노드 Kubernetes 클러스터는 확장성이나 고가용성을 제공하지 않기 때문입니다.

1. microk8s를 설치하십시오.

   ```bash
   sudo snap install microk8s --classic --channel=stable
   ```
   {: codeblock}

2. **root**로 실행 중이지 않은 경우 사용자를 **microk8s** 그룹에 추가하십시오.

   ```bash
   sudo usermod -a -G microk8s $USER    sudo chown -f -R $USER ~/.kube    su - $USER   # create new session for group update to take place
   ```
   {: codeblock}

3. microk8s에서 dns 및 스토리지 모듈을 사용으로 설정하십시오.

   ```bash
   microk8s.enable dns    microk8s.enable storage
   ```
   {: codeblock}

   **참고**: 기본적으로 Microk8s에서는 업스트림 이름 서버로 `8.8.8.8` 및 `8.8.4.4`를 사용합니다. 이러한 이름 서버에서 관리 허브 호스트 이름을 해석할 수 없는 경우 microk8s에서 사용하는 이름 서버를 변경해야 합니다.
   
   1. `/etc/resolv.conf` 또는 `/run/systemd/resolve/resolv.conf`에서 업스트림 이름 서버의 목록을 검색하십시오.

   2. `kube-system` 네임스페이스에서 `coredns` configmap을 편집하십시오. `forward` 섹션에서 업스트림 이름 서버를 설정하십시오.
   
      ```bash
      microk8s.kubectl edit -n kube-system cm/coredns
      ```
      {: codeblock}
   
   3. Kubernetes DNS에 대한 자세한 정보는 [Kubernetes 문서](https://kubernetes.io/docs/tasks/administer-cluster/dns-custom-nameservers/)를 참조하십시오.


4. 상태를 확인하십시오.

   ```bash
   microk8s.status --wait-ready
   ```
   {: codeblock}

5. microK8s의 kubectl 명령은 **microk8s.kubectl**이라고 하며 이미 설치된 **kubectl** 명령과의 충돌을 방지합니다. **kubectl**이 설치되지 않았다고 가정하고 **microk8s.kubectl**에 대해 이 별명을 추가하십시오.

   ```bash
   echo 'alias kubectl=microk8s.kubectl' >> ~/.bash_aliases    source ~/.bash_aliases
   ```
   {: codeblock}

6. 컨테이너 레지스트리를 사용으로 설정하고 비보호 레지스트리를 허용하도록 Docker를 구성하십시오.

   1. 컨테이너 레지스트리를 사용으로 설정하십시오.

      ```bash
      microk8s.enable registry       export REGISTRY_ENDPOINT=localhost:32000
      ```
      {: codeblock}

   2. docker를 설치하십시오(아직 설치되지 않은 경우).

      ```bash
      curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -       add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"       apt-get install docker-ce docker-ce-cli containerd.io
      ```
      {: codeblock}

   3. 이 레지스트리를 안전하지 않은 것으로 Docker에 정의하십시오. **/etc/docker/daemon.json**을 작성하거나 여기에 추가하십시오(`<registry-endpoint>`를 이전 단계에서 얻은 `$REGISTRY_ENDPOINT` 환경 변수의 값으로 대체함).

      ```json
      {
        "insecure-registries": [ "<registry-endpoint>" ]       }
      ```
      {: codeblock}

   4. (선택사항) Docker가 시스템에 있는지 확인하십시오.

      ```bash
      curl -fsSL get.docker.com | sh
      ```
      {: codeblock}   

   5. docker를 다시 시작하여 변경사항을 적용하십시오.

      ```bash
      sudo systemctl restart docker
      ```
      {: codeblock}

## 다음 수행할 작업

* [에이전트 설치](edge_cluster_agent.md)
