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

* 다음 유형의 에지 클러스터 중 하나를 설치하십시오.
  * [OCP 에지 클러스터 설치](#install_ocp_edge_cluster)
  * [k3s 에지 클러스터 설치 및 구성](#install_k3s_edge_cluster)
  * [microk8s 에지 클러스터 설치 및 구성](#install_microk8s_edge_cluster)(개발 및
테스트용이며 프로덕션에는 권장되지 않음)
* [에지 클러스터에 필요한 정보 및 파일 수집](#gather_info)

## OCP 에지 클러스터 설치
{: #install_ocp_edge_cluster}

1. [{{site.data.keyword.open_shift_cp}} 문서 ![새 탭에서 열림](../../images/icons/launch-glyph.svg "새 탭에서 열림")](https://docs.openshift.com/container-platform/4.4/welcome/index.html)의 설치 지시사항에 따라 OCP를 설치하십시오.

2. OCP 클러스터를 관리하는 관리자 호스트(에이전트 설치 스크립트를 실행할 호스트와 동일)에 Kubenetes CLI(**kubectl**) 및 Openshift 클라이언트 CLI(**oc**)를 설치하십시오. [cloudctl, kubectl 및 oc 설치](../installing/cloudctl_oc_cli.md)를 참조하십시오.

## k3s 에지 클러스터 설치 및 구성
{: #install_k3s_edge_cluster}

이 절에서는 Ubuntu 18.04에 가볍고 작은 Kubernetes 클러스터인 k3s(rancher)를 설치하는 방법을 요약합니다(자세한 지시사항은 [k3s 문서 ![새 탭에서 열림](../../images/icons/launch-glyph.svg "새 탭에서 열림")](https://rancher.com/docs/k3s/latest/en/) 참조).

1. **root**로 로그인하거나 `sudo -i`를 사용하여
**root**로 올리십시오.

2. k3s를 설치하십시오.

   ```bash
   curl -sfL https://get.k3s.io | sh -
   ```
   {: codeblock}

3. 이미지 레지스트리 서비스를 작성하십시오.

   1. 다음 컨텐츠를 사용하여 **k3s-registry-deployment.yml**이라는 파일을 작성하십시오.

      ```yaml
      apiVersion: apps/v1
      kind: Deployment
      metadata:
        name: docker-registry
        labels:
          app: docker-registry
      spec:
        replicas: 1
        selector:
          matchLabels:
            app: docker-registry
        template:
          metadata:
            labels:
              app: docker-registry
          spec:
            containers:
            - name: docker-registry
              image: registry
              ports:
              - containerPort: 5000
              volumeMounts:
              - name: storage
                mountPath: /var/lib/registry
            volumes:
            - name: storage
              emptyDir: {} # FIXME: make this a persistent volume if using in production
      ---
      apiVersion: v1
      kind: Service
      metadata:
        name: docker-registry-service
      spec:
        selector:
          app: docker-registry
        type: NodePort
        ports:
          - protocol: TCP
            port: 5000
      ```
      {: codeblock}

   2. 레지스트리 서비스를 작성하십시오.

      ```bash
      kubectl apply -f k3s-registry-deployment.yml
      ```
      {: codeblock}

   3. 서비스가 작성되었는지 확인하십시오.

      ```bash
      kubectl get deployment
      kubectl get service
      ```
      {: codeblock}

   4. 레지스트리 엔드포인트를 정의하십시오.

      ```bash
      export REGISTRY_ENDPOINT=$(kubectl get ep docker-registry-service | grep docker-registry-service | awk '{print $2}')
      cat << EOF >> /etc/rancher/k3s/registries.yaml
      mirrors:
        "$REGISTRY_ENDPOINT":
          endpoint:
            - "http://$REGISTRY_ENDPOINT"
      EOF
      ```
      {: codeblock}

   5. k3s를 다시 시작하여 **/etc/rancher/k3s/registries.yaml**의 변경사항을 적용하십시오.

      ```bash
      systemctl restart k3s
      ```
      {: codeblock}

4. 비보안 레지스트리로 docker에 이 레지스트리를 정의하십시오.

   1. **/etc/docker/daemon.json**에 추가하거나 작성하십시오(`$REGISTRY_ENDPOINT`의 값 대체).

      ```json
      {
        "insecure-registries": [ "$REGISTRY_ENDPOINT" ]
      }
      ```
      {: codeblock}

   2. docker를 다시 시작하여 변경사항을 적용하십시오.

      ```bash
      systemctl restart docker
      ```
      {: codeblock}

## microk8s 에지 클러스터 설치 및 구성
{: #install_microk8s_edge_cluster}

이 절에서는 Ubuntu 18.04에 가볍고 작은 Kubernetes 클러스터인 microk8s를 설치하는 방법을 요약합니다(자세한 지시사항은 [microk8s 문서 ![새 탭에서 열림](../../images/icons/launch-glyph.svg "새 탭에서 열림")](https://microk8s.io/docs) 참조).

참고: 이 유형의 에지 클러스터는 개발 및 테스트를 위한 것입니다. 단일 작업자 노드 Kubernetes 클러스터는 확장성이나 고가용성을 제공하지 않기 때문입니다.

1. microk8s를 설치하십시오.

   ```bash
   sudo snap install microk8s --classic --channel=stable
   ```
   {: codeblock}

2. **root**로 실행 중이지 않은 경우 사용자를 **microk8s** 그룹에 추가하십시오.

   ```bash
   sudo usermod -a -G microk8s $USER
   sudo chown -f -R $USER ~/.kube
   su - $USER   # create new session for group update to take place
   ```
   {: codeblock}

3. microk8s에서 dns 및 스토리지 모듈을 사용으로 설정하십시오.

   ```bash
   microk8s.enable dns
   microk8s.enable storage
   ```
   {: codeblock}

4. 상태를 확인하십시오.

   ```bash
   microk8s.status --wait-ready
   ```
   {: codeblock}

5. microK8s의 kubectl 명령은 **microk8s.kubectl**이라고 하며 이미 설치된 **kubectl** 명령과의 충돌을 방지합니다. **kubectl**이 설치되지 않았다고 가정하면 **microk8s.kubectl**에 대해 이 별명을 추가하십시오.

   ```bash
   echo 'alias kubectl=microk8s.kubectl' >> ~/.bash_aliases
   source ~/.bash_aliases
   ```
   {: codeblock}

6. 컨테이너 레지스트리를 사용으로 설정하고 비보호 레지스트리를 허용하도록 Docker를 구성하십시오.

   1. 컨테이너 레지스트리를 사용으로 설정하십시오.

      ```bash
      microk8s.enable registry
      export REGISTRY_ENDPOINT=localhost:32000
      ```
      {: codeblock}

   2. docker를 설치하십시오(아직 설치되지 않은 경우).

      ```bash
      curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
      add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
      apt-get install docker-ce docker-ce-cli containerd.io
      ```
      {: codeblock}

   3. 비보안 레지스트리로 docker에 이 레지스트리를 정의하십시오. **/etc/docker/daemon.json**에 추가하거나 작성하십시오(`$REGISTRY_ENDPOINT`의 값 대체).

      ```json
      {
        "insecure-registries": [ "$REGISTRY_ENDPOINT" ]
      }
      ```
      {: codeblock}

   4. docker를 다시 시작하여 변경사항을 적용하십시오.

      ```bash
      sudo systemctl restart docker
      ```
      {: codeblock}

## 다음 수행할 작업

* [에이전트 설치](edge_cluster_agent.md)
