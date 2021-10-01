---

copyright:
  years: 2019, 2020
lastupdated: "2020-02-13"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# IEAM이 있는 CP4MCM 사용
{: #using_cp4mcm}

{{site.data.keyword.edge_shared_notm}}의 사용을 구성하고 사용 설정하려면 다음 설치 단계를 수행하십시오. 이 설치는 {{site.data.keyword.edge_servers_notm}} 및 {{site.data.keyword.edge_devices_notm}}를 둘 다 지원합니다.
{:shortdesc}

## 선행 조건
{: #prereq}

{{site.data.keyword.icp_server_notm}}를 위한 [적절하게 크기 조정된](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.0/servers/cluster_sizing.html) 클러스터가 있는지 확인하십시오.

* Docker 1.13+
* [OpenShift 클라이언트 CLI(oc) 4.2 ![새 탭에서 열림](../images/icons/launch-glyph.svg "새 탭에서 열림")](https://mirror.openshift.com/pub/openshift-v4/clients/ocp/latest-4.2/)

## 설치 프로세스

1. 어떤 제품을 구매했는지에 따라서 IBM Passport Advantage에서 {{site.data.keyword.edge_servers_notm}} 또는 {{site.data.keyword.edge_devices_notm}}를 위한 **ibm-cp4mcm-core** 및 **ibm-ecm** 번들을 설치 환경으로 다운로드하십시오.

2. 설치에서 사용될 디렉토리를 준비하고, 설치의 일부로 허용될 라이센스 zip 파일의 압축을 푸십시오.

    ```
    mkdir -p /opt/ibm-multicloud-manager-1.2 && \
    tar -C /opt/ibm-multicloud-manager-1.2 -zxvf ibm-ecm-4.0.0-x86_64.tar.gz ibm-ecm-4.0.0-x86_64/ibm-ecm-licenses-4.0.zip
    ```
    {: codeblock}

3. Docker 서비스가 실행 중인지 확인하고 설치 tarball로부터 Docker 이미지를 압축 풀기/로드하십시오.

    ```
    tar -zvxf ibm-cp4mcm-core-1.2-x86_64.tar.gz -O | sudo docker load
    ```
    {: codeblock}

4. 설치 구성을 준비하고 추출하십시오.

    ```
    cd /opt/ibm-multicloud-manager-1.2 && \
    sudo docker run --rm -v $(pwd):/data:z -e LICENSE=accept -v $(pwd)/ibm-ecm-4.0.0-x86_64:/installer/cfc-files/license:z --security-opt label:disable ibmcom/mcm-inception-amd64:3.2.3 cp -r cluster /data
    ```
    {: codeblock}

5. 새로운 KUBECONFIG 위치를 지정하고, 아래의 **oc login** 명령(OpenShift 클러스터 설치에서 확보함)에 **적절한 클러스터 정보를 채우고**, **$KUBECONFIG** 파일을 설치 구성 디렉토리에 복사하십시오.

    ```
    export KUBECONFIG=$(pwd)/myclusterconfig
    ```
    {: codeblock}

    ```
    oc login https://<API_ENDPOINT_HOST>:<PORT> -u <ADMIN_USER> -p <ADMIN_PASSWORD> --insecure-skip-tls-verify=true && \
    cp $KUBECONFIG /opt/ibm-multicloud-manager-1.2/cluster/kubeconfig && \
    cd cluster
    ```
    {: codeblock}

6. config.yaml 파일을 업데이트하십시오.

  * 스케줄링될 {{site.data.keyword.edge_shared_notm}} 서비스를 구성할 노드를 판별하십시오. **master** 노드 사용을 피할 것을 강력히 권고합니다.

     ```
     # oc get nodes
     NAME               STATUS   ROLES    AGE  VERSION
     master0.test.com   Ready    master   8h   v1.14.6+c07e432da
     master1.test.com   Ready    master   8h   v1.14.6+c07e432da
     master2.test.com   Ready    master   8h   v1.14.6+c07e432da
     worker0.test.com   Ready    worker   8h   v1.14.6+c07e432da
     worker1.test.com   Ready    worker   8h   v1.14.6+c07e432da
     worker2.test.com   Ready    worker   8h   v1.14.6+c07e432da
     ```

     cluster/config.yaml(**master** 여기서는 {{site.data.keyword.edge_servers_notm}}의 일부인 서비스의 특정 세트를 의미하며 **master** 노드 역할을 의미하는 것이 **아닙니다**) 내부에서

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

   * 지속적 데이터에 대해서는 선호하는 **storage_class**를 선택하십시오.

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

     참고: 이 정의가 없으면 **mycluster** 이름의 기본값이 선택됩니다. {{site.data.keyword.edge_devices_notm}}도 설치 중인 경우, 이것은 클러스터를 적절하게 지명하는 중요한 단계입니다. **cluster_name**이 해당 제품의 여러 컴포넌트를 정의하는 데 사용됩니다.

7. 내부 OpenShift 이미지 레지스트리로의 기본 라우트를 여십시오.

    ```
    oc patch configs.imageregistry.operator.openshift.io/cluster --type merge -p '{"spec":{"defaultRoute":true}}'
    ```
    {: codeblock}

8. {{site.data.keyword.edge_shared_notm}}를 설치하십시오.

    ```
    sudo docker run -t --net=host -e LICENSE=accept -v $(pwd)/../ibm-ecm-4.0.0-x86_64:/installer/cfc-files/license:z -v $(pwd):/installer/cluster:z -v /var/run:/var/run:z -v /etc/docker:/etc/docker:z --security-opt label:disable ibmcom/mcm-inception-amd64:3.2.3 install-with-openshift
    ```
    {: codeblock}

<!--## Importing a cluster to be managed
There is a known issue with importing clusters, we are working on providing functional documentation steps for this process.

## Next steps
If this installation was done as part of a prerequisite for {{site.data.keyword.edge_devices_notm}}, [return to continue that installation](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.0/devices/installing/install.html).-->
