---

copyright:
years: 2019, 2020
lastupdated: "2020-01-22"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 개인 컨테이너 레지스트리 사용
{: #container_registry}

에지 서비스 이미지가 공용 레지스트리에 포함시키기에 적합하지 않은 자산을 포함하는 경우 개인용 Docker 컨테이너 레지스트리(예: 액세스가 엄격하게 제어되는 {{site.data.keyword.open_shift}} Image Registry 또는 {{site.data.keyword.ibm_cloud}} Container Registry)를 사용할 수 있습니다.
{:shortdesc}

아직 수행하지 않은 경우 [디바이스를 위한 에지 서비스 개발](developing.md)의 단계를 따라 하나 이상의 예제 에지 서비스를 작성 및 배치하고 기본 프로세스에 익숙하도록 하십시오.

이 페이지는 에지 서비스 이미지를 저장할 수 있는 다음 두 개의 레지스트리를 설명합니다.
* [{{site.data.keyword.open_shift}} 이미지 레지스트리](#ocp_image_registry) 사용
* [{{site.data.keyword.cloud_notm}} Container Registry](#ibm_cloud_container_registry) 사용

이들은 또한 {{site.data.keyword.edge_notm}}({{site.data.keyword.ieam}})와 함께 임의의 개인용 이미지 레지스트리를 사용할 수 있는 방법의 예를 제공합니다.

## {{site.data.keyword.open_shift}} 이미지 레지스트리 사용
{: #ocp_image_registry}

### 시작하기 전에

* 아직 수행하지 않은 경우 [cloudctl 명령![새 탭에서 열림](../../images/icons/launch-glyph.svg "새 탭에서 열림")](https://www.ibm.com/support/knowledgecenter/SSFC4F_1.3.0/cloudctl/install_cli.html)을 설치하십시오.
* 아직 수행하지 않은 경우 [{{site.data.keyword.open_shift}} oc 명령![새 탭에서 열림](../../images/icons/launch-glyph.svg "새 탭에서 열림")](https://docs.openshift.com/container-platform/4.4/cli_reference/openshift_cli/getting-started-cli.html)을 설치하십시오.
* {{site.data.keyword.macOS_notm}}에서 [homebrew ![새 탭에서 열림](../../images/icons/launch-glyph.svg "새 탭에서 열림")](https://docs.brew.sh/Installation)를 사용하여 {{site.data.keyword.open_shift}} **oc** 명령을 설치할 수 있습니다.

    ```bash
    brew install openshift-cli
    ```
    {: codeblock}

### 프로시저

참고: 명령 구문에 대한 자세한 정보는 [이 문서에서 사용된 규칙](../../getting_started/document_conventions.md)을 참조하십시오.

1. 클러스터 관리자 권한으로 {{site.data.keyword.open_shift}} 클러스터에 연결했는지 확인하십시오.

   ```bash
   cloudctl login -a <cluster-url> -u <user> -p <password> -n kube-system --skip-ssl-validation
   ```
   {: codeblock}

2. {{site.data.keyword.open_shift}} 이미지 레지스트리의 기본 라우트가 클러스터 외부에서 액세스할 수 있도록 작성되었는지 여부를 판별하십시오.

   ```bash
   oc get route default-route -n openshift-image-registry --template='{{ .spec.host }}'
   ```
   {: codeblock}

   명령 응답이 **default-route**를 찾을 수 없음을 표시하는 경우, 작성하십시오(자세한 내용은 [레지스트리 탐색![새 탭에서 열림](../../images/icons/launch-glyph.svg "새 탭에서 열림")](https://docs.openshift.com/container-platform/4.4/registry/securing-exposing-registry.html)을 참조하십시오).

   ```bash
   oc patch configs.imageregistry.operator.openshift.io/cluster --patch '{"spec":{"defaultRoute":true}}' --type=merge
   ```
   {: codeblock}

3. 사용해야 하는 저장소 라우트 이름을 검색하십시오.

   ```bash
   export OCP_DOCKER_HOST=`oc get route default-route -n openshift-image-registry --template='{{ .spec.host }}'`
   ```
   {: codeblock}

4. 이미지를 저장할 새 프로젝트를 작성하십시오.

   ```bash
   export OCP_PROJECT=<your-new-project>
   oc new-project $OCP_PROJECT
   ```
   {: codeblock}

5. 사용자가 선택한 이름으로 서비스 계정을 작성하십시오.

   ```bash
   export OCP_USER=<service-account-name>
   oc create serviceaccount $OCP_USER
   ```
   {: codeblock}

6. 현재 프로젝트의 서비스 계정에 역할을 추가하십시오.

   ```bash
   oc policy add-role-to-user edit system:serviceaccount:$OCP_PROJECT:$OCP_USER
   ```
   {: codeblock}

7. 서비스 계정에 토큰이 지정되도록 하십시오.

   ```bash
   export OCP_TOKEN=`oc serviceaccounts get-token $OCP_USER`
   ```
   {: codeblock}

8. {{site.data.keyword.open_shift}} 인증서를 가져오고 Docker가 이를 신뢰하게 하십시오.

   ```bash
   echo | openssl s_client -connect $OCP_DOCKER_HOST:443 -showcerts | sed -n "/-----BEGIN CERTIFICATE-----/,/-----END CERTIFICATE-----/p" > ca.crt
   ```
   {: codeblock}

   {{site.data.keyword.linux_notm}}의 경우:

   ```bash
   mkdir -p /etc/docker/certs.d/$OCP_DOCKER_HOST
   cp ca.crt /etc/docker/certs.d/$OCP_DOCKER_HOST
   systemctl restart docker.service
   ```
   {: codeblock}

   {{site.data.keyword.macOS_notm}}의 경우:

   ```bash
   mkdir -p ~/.docker/certs.d/$OCP_DOCKER_HOST
   cp ca.crt ~/.docker/certs.d/$OCP_DOCKER_HOST
   ```
   {: codeblock}

   {{site.data.keyword.macOS_notm}}에서 데스크탑 메뉴 표시줄의 오른편에 있는 고래 아이콘을 클릭하고 **다시 시작**을 선택하여 Docker를 다시 시작하십시오.

9. {{site.data.keyword.ocp}} Docker 호스트에 로그인하십시오.

   ```bash
   echo "$OCP_TOKEN" | docker login -u $OCP_USER --password-stdin $OCP_DOCKER_HOST
   ```
   {: codeblock}

10. 이 경로 형식을 갖는 이미지를 빌드하십시오. 예를 들어,

   ```bash
   export BASE_IMAGE_NAME=myservice
   docker build -t $OCP_DOCKER_HOST/$OCP_PROJECT/${BASE_IMAGE_NAME}_amd64:1.2.3 -f ./Dockerfile.amd64 .
   ```
   {: codeblock}

11. 에지 서비스 공개 준비에서 그의 **deployment** 섹션이 사용자의 이미지 레지스트리 경로를 참조하도록 **service.definition.json** 파일을 수정하십시오. 다음을 사용하여 이와 비슷한 서비스 및 패턴 정의 파일을 작성할 수 있습니다.

   ```bash
   hzn dev service new -s $BASE_IMAGE_NAME -i $OCP_DOCKER_HOST/$OCP_PROJECT/$BASE_IMAGE_NAME
   ```
   {: codeblock}

   **&lt;base-image-name&gt;**이 arch 또는 version 없이 기본 이미지 이름이어야 합니다. 그런 다음 작성된 **horizon/hzn.json** 파일에서 필요에 따라 변수를 편집할 수 있습니다.

   또는, 고유한 서비스 정의 파일을 작성한 경우 **deployment.services.&lt;service-name&gt;.image** 필드가 이미지 레지스트리 경로를 참조하는지 확인하십시오.

12. 서비스 이미지를 공개할 준비가 되었을 때, 이미지를 개인용 컨테이너 레지스트리로 푸시하고 이미지를 {{site.data.keyword.horizon}} exchange에 공개하십시오.

   ```bash
   hzn exchange service publish -r "$OCP_DOCKER_HOST:$OCP_USER:$OCP_TOKEN" -f horizon/service.definition.json
   ```
   {: codeblock}

   **-r "$OCP_DOCKER_HOST:$OCP_USER:$OCP_TOKEN"** 인수는 {{site.data.keyword.horizon_open}} 에지 노드에 서비스 이미지를 가져올 수 있는 인증 정보를 제공합니다.

   명령은 다음 태스크를 완료합니다.

   * Docker 이미지를 {{site.data.keyword.cloud_notm}} Container Registry에 푸시하고, 프로세스에서 이미지의 다이제스트를 가져옵니다.
   * 개인 키로 다이제스트 및 배치 정보에 서명합니다.
   * 서비스 메타데이터(서명 포함)를 {{site.data.keyword.horizon}} exchange에 넣습니다.
   * 공개 키를 서비스 정의 아래의 {{site.data.keyword.horizon}} exchange에 넣어서 {{site.data.keyword.horizon}} 에지 노드가 필요할 때 서명을 확인하기 위해 정의를 자동으로 검색합니다.
   * OpenShift 사용자 및 토큰을 서비스 정의 아래의 {{site.data.keyword.horizon}} exchange에 넣어서 {{site.data.keyword.horizon}} 에지 노드가 필요할 때 정의를 자동으로 검색할 수 있습니다.
   
### {{site.data.keyword.horizon}} 에지 노드에서 서비스 사용
{: #using_service}

에지 노드가 {{site.data.keyword.ocp}} 이미지 레지스트리에서 필요한 서비스 이미지를 가져올 수 있도록 하려면 {{site.data.keyword.open_shift}} 인증서를 신뢰하도록 각 에지 노드에 Docker를 구성해야 합니다. **ca.crt** 파일을 각 에지 노드에 복사한 후,

{{site.data.keyword.linux_notm}}의 경우:

```bash
mkdir -p /etc/docker/certs.d/$OCP_DOCKER_HOST
cp ca.crt /etc/docker/certs.d/$OCP_DOCKER_HOST
systemctl restart docker.service
```
{: codeblock}

{{site.data.keyword.macOS_notm}}의 경우:

```bash
mkdir -p ~/.docker/certs.d/$OCP_DOCKER_HOST
cp ca.crt ~/.docker/certs.d/$OCP_DOCKER_HOST
```
{: codeblock}

{{site.data.keyword.macOS_notm}}에서 데스크탑 메뉴 표시줄의 오른편에 있는 고래 아이콘을 클릭하고 **다시 시작**을 선택하여 Docker를 다시 시작하십시오.

이제 {{site.data.keyword.horizon}}가 {{site.data.keyword.open_shift}} 이미지 레지스트리에서 이 에지 서비스 이미지를 가져오고 사용자가 작성한 배치 패턴이나 정책이 지정한 대로 에지 노드에 배치하기 위해 필요한 모든 것을 갖고 있습니다.

## {{site.data.keyword.cloud_notm}} Container Registry 사용
{: #ibm_cloud_container_registry}

### 시작하기 전에

* [{{site.data.keyword.cloud_notm}} CLI 도구(ibmcloud)![새 탭에서 열림](../../images/icons/launch-glyph.svg "새 탭에서 열림")](https://cloud.ibm.com/docs/cli?topic=cloud-cli-install-ibmcloud-cli)를 설치하십시오.
* {{site.data.keyword.cloud_notm}} 계정에서 **클러스터 관리자** 또는 **팀 관리자** 액세스 레벨을 갖고 있는지 확인하십시오.

### 프로시저

1. {{site.data.keyword.cloud_notm}}에 로그인하고 조직을 대상으로 하십시오.

   ```bash
   ibmcloud login -a cloud.ibm.com -u <cloud-username> -p <cloud-password
   ibmcloud target -o <organization-id> -s <space-id>
   ```
   {: codeblock}

   조직 ID와 공간 ID를 모르는 경우 [{{site.data.keyword.cloud_notm}} 콘솔![새 탭에서 열림](../../images/icons/launch-glyph.svg "새 탭에서 열림")](https://cloud.ibm.com/)에 로그인하고 찾거나 작성할 수 있습니다.

2. 클라우드 API 키를 작성하십시오.

   ```bash
   ibmcloud iam api-key-create <key-name> -d "<key-description>"
   ```
   {: codeblock}

   안전한 장소에 API 키(**API 키**로 시작하는 행에 표시됨)를 보관하고 다음 환경 변수에서 설정하십시오.

   ```bash
   export CLOUD_API_KEY=<your-cloud-api-key>
   ```
   {: codeblock}

   참고: 이 API 키는 `hzn` 명령과 함께 사용하기 위해 작성한 {{site.data.keyword.open_shift}} API 키와는 다릅니다.

3. container-registry 플러그인을 가져오고 개인 레지스트리 네임스페이스를 작성하십시오. (이 레지스트리 네임스페이스는 Docker 이미지를 식별하는 데 사용되는 경로의 일부가 됩니다.)

   ```bash
   ibmcloud plugin install container-registry
   export REGISTRY_NAMESPACE=<your-registry-namespace>
   ibmcloud cr namespace-add $REGISTRY_NAMESPACE
   ```
   {: codeblock}

4. Docker 레지스트리 네임스페이스에 로그인하십시오.

   ```bash
    ibmcloud cr login
   ```
   {: codeblock}

   **ibmcloud cr** 사용에 대한 자세한 정보는 [ibmcloud cr CLI 웹 문서![새 탭에서 열림](../../images/icons/launch-glyph.svg "새 탭에서 열림")](https://cloud.ibm.com/docs/services/Registry/)를 참조하십시오. 추가로 다음 명령을 실행하여 도움말 정보를 볼 수 있습니다.

   ```bash
ibmcloud cr --help
   ```
   {: codeblock}

   {{site.data.keyword.cloud_registry}}의 개인 네임스페이스에 로그인한 후에는 `docker login`을 사용하여 레지스트리에 로그인할 필요가 없습니다. **docker push** 및 **docker pull** 명령 안에서 다음과 비슷한 컨테이너 레지스트리 경로를 사용할 수 있습니다.

   ```bash
   us.icr.io/$REGISTRY_NAMESPACE/<base-image-name>_<arch>:<version>
   ```
   {: codeblock}

5. 이 경로 형식을 갖는 이미지를 빌드하십시오. 예를 들어,

   ```bash
   export BASE_IMAGE_NAME=myservice
   docker build -t us.icr.io/$REGISTRY_NAMESPACE/${BASE_IMAGE_NAME}_amd64:1.2.3 -f ./Dockerfile.amd64 .
   ```
   {: codeblock}

6. 에지 서비스 공개 준비에서 그의 **deployment** 섹션이 사용자의 이미지 레지스트리 경로를 참조하도록 **service.definition.json** 파일을 수정하십시오. 다음을 사용하여 이와 비슷한 서비스 및 패턴 정의 파일을 작성할 수 있습니다.

   ```bash
   hzn dev service new -s $BASE_IMAGE_NAME -i us.icr.io/$REGISTRY_NAMESPACE/$BASE_IMAGE_NAME
   ```
   {: codeblock}

   **&lt;base-image-name&gt;**이 arch 또는 version 없이 기본 이미지 이름이어야 합니다. 그런 다음 작성된 **horizon/hzn.json** 파일에서 필요에 따라 변수를 편집할 수 있습니다.

   또는, 고유한 서비스 정의 파일을 작성한 경우 **deployment.services.&lt;service-name&gt;.image** 필드가 이미지 레지스트리 경로를 참조하는지 확인하십시오.

7. 서비스 이미지를 공개할 준비가 되었을 때, 이미지를 개인용 컨테이너 레지스트리로 푸시하고 이미지를 {{site.data.keyword.horizon}} exchange에 공개하십시오.

   ```bash
   hzn exchange service publish -r "us.icr.io:iamapikey:$CLOUD_API_KEY" -f horizon/service.definition.json
   ```
   {: codeblock}

   **-r "us.icr.io:iamapikey:$CLOUD_API_KEY"** 인수는 {{site.data.keyword.horizon_open}} 에지 노드에 서비스 이미지를 가져올 수 있는 인증 정보를 제공합니다.

   명령은 다음 태스크를 완료합니다.

   * Docker 이미지를 {{site.data.keyword.cloud_notm}} Container Registry에 푸시하고, 프로세스에서 이미지의 다이제스트를 가져옵니다.
   * 개인 키로 다이제스트 및 배치 정보에 서명합니다.
   * 서비스 메타데이터(서명 포함)를 {{site.data.keyword.horizon}} exchange에 넣습니다.
   * 공개 키를 서비스 정의 아래의 {{site.data.keyword.horizon}} exchange에 넣어서 {{site.data.keyword.horizon}} 에지 노드가 필요할 때 서명을 확인하기 위해 정의를 자동으로 검색합니다.
   * {{site.data.keyword.cloud_notm}} API 키를 서비스 정의 아래의 {{site.data.keyword.horizon}} exchange에 넣어서 {{site.data.keyword.horizon}} 에지 노드가 필요할 때 정의를 자동으로 검색할 수 있습니다.

8. 서비스 이미지가 {{site.data.keyword.cloud_notm}} Container Registry에 푸시되었는지 확인하십시오.

   ```bash
   ibmcloud cr images
   ```
   {: codeblock}

9. 서비스를 일부 에지 노드에 배치할 배치 패턴이나 정책을 공개하십시오. 예를 들면, 다음과 같습니다.

   ```bash
   hzn exchange pattern publish -f horizon/pattern.json
   ```
   {: codeblock}

이제 {{site.data.keyword.horizon}}가 {{site.data.keyword.cloud_notm}} Container Registry에서 이 에지 서비스 이미지를 가져오고 사용자가 작성한 배치 패턴이나 정책이 지정한 대로 에지 노드에 배치하기 위해 필요한 모든 것을 갖고 있습니다.
