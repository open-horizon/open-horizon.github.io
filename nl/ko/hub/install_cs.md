---

copyright:
years: 2020
lastupdated: "2020-06-03"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Common Services 설치

## 선행 조건
{: #prereq}

### {{site.data.keyword.ocp_tm}}
[적절하게 크기가
지정](cluster_sizing.md)되고 지원되는 {{site.data.keyword.open_shift_cp}} 설치가 있는지 확인하십시오. 클러스터에 설치되어 작동 중인 레지스트리와 스토리지 서비스를 포함합니다. {{site.data.keyword.open_shift_cp}} 설치에 대한 자세한 정보는 아래 지원되는 버전의 {{site.data.keyword.open_shift}} 문서를 참조하십시오.

* [{{site.data.keyword.open_shift_cp}} 4.3 문서 ![새 탭에서 열림](../images/icons/launch-glyph.svg "새 탭에서 열림")](https://www.ibm.com/links?url=https%3A%2F%2Fdocs.openshift.com%2Fcontainer-platform%2F4.3%2Fwelcome%2Findex.html)
* [{{site.data.keyword.open_shift_cp}} 4.4 문서 ![새 탭에서 열림](../images/icons/launch-glyph.svg "새 탭에서 열림")](https://www.ibm.com/links?url=https%3A%2F%2Fdocs.openshift.com%2Fcontainer-platform%2F4.4%2Fwelcome%2Findex.html)

### 기타 필수 소프트웨어

* Docker 1.13+
* [{{site.data.keyword.open_shift}} 클라이언트 CLI(oc) 4.4 ![새 탭에서 열림](../images/icons/launch-glyph.svg "새 탭에서 열림")](https://mirror.openshift.com/pub/openshift-v4/clients/ocp/latest-4.4/)

## 설치 프로세스

1. 설치 환경으로 [
IBM Passport Advantage에서 원하는 패키지를 다운로드](part_numbers.md)하고 설치 매체의 압축을 푸십시오.
    ```
    tar -zxvf ibm-eam-{{site.data.keyword.semver}}-x86_64.tar.gz
    cd ibm-eam-{{site.data.keyword.semver}}-x86_64
    ```
    {: codeblock}

2. 설치에서 사용될 디렉토리를 준비하고, 설치의 일부로 허용될 라이센스 zip 파일을 복사하십시오.

    ```
    mkdir -p /opt/common-services-3.2.7/ibm-eam-{{site.data.keyword.semver}}-licenses && \
    cp ibm-eam-{{site.data.keyword.semver}}-licenses.zip /opt/common-services-3.2.7/ibm-eam-{{site.data.keyword.semver}}-licenses
    ```
    {: codeblock}

3. Docker 서비스가 실행 중인지 확인하고 설치 tarball로부터 Docker 이미지를 압축 풀기/로드하십시오.

    ```
    systemctl enable docker
    systemctl start docker
    tar -zvxf common-services-boeblingen-2004-x86_64.tar.gz -O | sudo docker load
    ```
    {: codeblock}

    **참고:** 여러 이미지의 압축을 풀기 때문에 출력이 표시되기까지 몇 분이 걸릴 수 있습니다.

4. 설치 구성을 준비하고 추출하십시오.

    ```
    cd /opt/common-services-3.2.7 && \
    sudo docker run --rm -v $(pwd):/data:z -e LICENSE=accept -v $(pwd)/ibm-eam-{{site.data.keyword.semver}}-licenses:/installer/cfc-files/license:z --security-opt label:disable ibmcom/icp-inception-amd64:3.2.7 cp -r cluster /data
    ```
    {: codeblock}

5. 새 KUBECONFIG 위치를 설정하고, 아래의 **oc login** 명령({{site.data.keyword.open_shift}} 클러스터 설치에서 확보함)에 **적절한 클러스터 정보를 채우고**, **$KUBECONFIG** 파일을 설치 구성 디렉토리에 복사하십시오.

    ```
    export KUBECONFIG=$(pwd)/myclusterconfig
    ```
    {: codeblock}

    ```
    oc login https://<API_ENDPOINT_HOST>:<PORT> -u <ADMIN_USER> -p <ADMIN_PASSWORD> --insecure-skip-tls-verify=true && \
    cp $KUBECONFIG $(pwd)/cluster/kubeconfig && \
    cd cluster
    ```
    {: codeblock}

6. config.yaml 파일을 업데이트하십시오.

   * 스케줄링될 {{site.data.keyword.common_services}}를 구성할 노드를 판별하고 **마스터** 노드는 사용하지 마십시오.

     ```
     # oc get nodes
     NAME               STATUS   ROLES    AGE  VERSION
     master0.test.com   Ready    master   8h   v1.17.1
     master1.test.com   Ready    master   8h   v1.17.1
     master2.test.com   Ready    master   8h   v1.17.1
     worker0.test.com   Ready    worker   8h   v1.17.1
     worker1.test.com   Ready    worker   8h   v1.17.1
     worker2.test.com   Ready    worker   8h   v1.17.1
    ```

     cluster/config.yaml(**master** 여기서는 {{site.data.keyword.common_services}}의 일부인 서비스의 특정 세트를 의미하며 **master** 노드 역할을 의미하는 것이 **아닙니다**) 내부에서

     ```
     # A list of OpenShift nodes that used to run services components
     cluster_nodes:
       master:
         - worker0.test.com
       proxy:
         - worker0.test.com
       management:
         - worker0.test.com
     ```
     참고: master, proxy, management 매개변수의 값은 배열이며 다중 노드를 가질 수 있습니다. 또한 동일한 노드가 각 매개변수에 사용될 수 있습니다. 위의 구성은
**최소** 설치를 위한 것이며, **프로덕션** 설치의 경우 각 매개변수에 대해 3개의 작업자 노드를 포함하십시오.

   * 동적 스토리지를 이용하도록 지속 데이터의 선호 **storage_class**를 선택하십시오.

     ```
     # oc get storageclass
     NAME                               PROVISIONER                     AGE
     rook-ceph-block-internal           rook-ceph.rbd.csi.ceph.com      8h
     rook-ceph-cephfs-internal          rook-ceph.cephfs.csi.ceph.com   8h
     rook-ceph-delete-bucket-internal   ceph.rook.io/bucket             8h
     ```

     cluster/config.yaml 내부에서,

     ```
# Storage Class
storage_class: rook-ceph-cephfs-internal
     ```

     [지원되는 동적 {{site.data.keyword.open_shift}} 스토리지 옵션과 구성 지침![새 탭에 열림](../images/icons/launch-glyph.svg "새 탭에 열림")](https://docs.openshift.com/container-platform/4.4/storage/understanding-persistent-storage.html)은 다음을 참조하십시오.

   * 32자 이상의 영숫자 **default_admin_password**를 정의하십시오.

     ```
     # default_admin_password:
     # password_rules:
     #   - '^([a-zA-Z0-9\-]{32,})$'
     default_admin_password: <YOUR-32-CHARACTER-OR-LONGER-ADMIN-PASSWORD>
     ```

   * **cluster_name**을 정의하는 하나의 행을 추가하여 클러스터를 고유하게 식별하십시오.

     ```
     cluster_name: <INSERT_YOUR_UNIQUE_CLUSTER_NAME>
     ```

     참고: 이 정의가 없으면 **mycluster** 이름의 기본값이 선택됩니다. 이 단계는 {{site.data.keyword.edge_notm}}의 여러 컴포넌트를 정의하는 데 **cluster_name**을 사용하므로 클러스터의 이름을 적절하게 지정하는 데 중요합니다.

7. 내부 {{site.data.keyword.open_shift}} 이미지 레지스트리로의 기본 라우트를 여십시오.

    ```
    oc patch configs.imageregistry.operator.openshift.io/cluster --type merge -p '{"spec":{"defaultRoute":true}}'
    ```
    {: codeblock}

8. {{site.data.keyword.common_services}} 설치

    ```
    sudo docker run -t --net=host -e LICENSE=accept -v $(pwd)/../ibm-eam-{{site.data.keyword.semver}}-licenses:/installer/cfc-files/license:z -v $(pwd):/installer/cluster:z -v /var/run:/var/run:z -v /etc/docker:/etc/docker:z --security-opt label:disable ibmcom/icp-inception-amd64:3.2.7 install-with-openshift
    ```
    {: codeblock}
    **참고:** 네트워크 속도에 따라 설치 시간은 달라집니다. '이미지 로드 중' 태스크 중에
잠시 동안 출력이 표시되지 않습니다.

설치 출력에서 URL을 기록해 두십시오. 이 URL은 [{{site.data.keyword.ieam}} 설치](offline_installation.md)의 다음 단계에 필요합니다.
