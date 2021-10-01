---

copyright:
years: 2020
lastupdated: "2020-04-27"

---

{:shortdesc: .shortdesc}
{:new_window: target="_blank"}
{:codeblock: .codeblock}
{:pre: .pre}
{:screen: .screen}
{:tip: .tip}
{:download: .download}

# Kubernetes 연산자 개발
{: #kubernetes_operator}

일반적으로 에지 클러스터에서 실행할 서비스를 개발하는 것은 에지 디바이스에서 실행되는 에지 서비스를 개발하는 것과 유사합니다. 에지 서비스는 [Edge 고유 개발 우수 사례](../OH/docs/developing/best_practices.md) 개발을 사용하여 개발되었으며 컨테이너에 패키징되어 있습니다. 차이는 에지 서비스가 배치되는 방법입니다.

에지 클러스터에 컨테이너화된 에지 서비스를 배치하려면 개발자가 Kubernetes 클러스터에서 컨테이너화된 에지 서비스를 배치하는 Kubernetes 연산자를 먼저 빌드해야 합니다. 연산자가 작성되고 테스트된 후에 개발자가 {{site.data.keyword.edge_notm}}({{site.data.keyword.ieam}}) 서비스로 연산자를 작성하고 공개합니다. 이 프로세스는 정책 또는 패턴과 함께 {{site.data.keyword.ieam}} 서비스에 대해 수행되는 방식처럼 {{site.data.keyword.ieam}} 관리자가 연산자 서비스를 배치하도록 합니다. 에지 서비스에 대해 {{site.data.keyword.ieam}} 서비스 정의를 작성할 필요가 없습니다. {{site.data.keyword.ieam}} 관리자가 연산자 서비스를 배치하는 경우 연산자가 에지 서비스를 배치합니다.

Kubernetes 연산자를 작성할 때 여러 정보 소스를 사용할 수 있습니다. 먼저 [Kubernetes 개념 - 운영자 패턴](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/)을 읽으십시오. 이 사이트는 연산자에 대해 알아볼 수 있는 좋은 리소스입니다. 운영자 개념에 익숙해진 후 [운영자 프레임워크](https://operatorframework.io/)를 사용하여 운영자를 작성합니다. 이 웹 사이트에서는 운영자에 대한 자세한 정보 및 운영자 소프트웨어 개발 킷(SDK)을 사용하여 단순 운영자를 작성하는 방법에 대한 자세한 설명을 제공합니다.

## {{site.data.keyword.ieam}}의 연산자 개발 시 고려사항

{{site.data.keyword.ieam}}은 연산자가 {{site.data.keyword.ieam}} 관리 허브에 작성하는 모든 상태를 보고하기 때문에 연산자의 상태 기능을 자유롭게 사용하도록 하는 것이 가장 좋습니다. 연산자를 작성할 때 연산자 프레임워크는 연산자에 대해 Kubernetes 사용자 정의 리소스 정의(CRD)를 생성합니다. 모든 연산자 CRD에는 연산자 및 연산자가 배치되는 에지 서비스의 상태에 대한 중요한 상태 정보로 채워야 하는 상태 오브젝트가 있습니다. 이는 Kubernetes에서 자동으로 수행합니다. 연산자 개발자에 의해 연산자의 구현에 작성되어야 합니다. 에지 클러스터의 {{site.data.keyword.ieam}} 에이전트는 정기적으로 연산자 상태를 수집하여 관리 허브에 보고합니다.

운영자는 서비스 특정 {{site.data.keyword.ieam}} 환경 변수를 시작되는 임의의 서비스에 첨부하도록 선택할 수 있습니다. 운영자가 시작되면 {{site.data.keyword.ieam}} 에이전트는 서비스 특정 환경 변수가 포함된 `hzn-env-vars`라는 Kubernetes configmap을 작성합니다. 연산자는 선택적으로 연산자가 작성하는 모든 배치에 해당 구성 맵을 첨부할 수 있으며, 이는 연산자가 시작하는 서비스가 동일한 서비스 특정 환경 변수를 인식하도록 합니다. 에지 디바이스에서 실행되는 서비스에 삽입되는 동일한 환경 변수가 있습니다. 에지 클러스터 서비스의 경우 모델 관리 시스템(MMS)이 아직 지원되지 않기 때문에 유일한 예외는 ESS* 환경 변수입니다.

원하는 경우 {{site.data.keyword.ieam}}에서 배치하는 연산자를 기본 네임스페이스가 아닌 네임스페이스에 배치할 수 있습니다. 이는 네임스페이스를 가리키도록 연산자 yaml 파일을 수정하여 연산자 개발자에 의해 수행됩니다. 이를 수행하는 두 가지 방법이 있습니다.

* 연산자의 개발 정의를 수정하여 네임스페이스를 지정하십시오(일반적으로 **./deploy/operator.yaml**이라고 함).

또는

* 연산자의 yaml 정의 파일과 함께 네임스페이스 정의 yaml 파일을 포함하십시오(예를 들어, 연산자 프로젝트의 **./deploy** 디렉토리에서).

**참고**: 운영자가 비기본 네임스페이스에 배치되면 {{site.data.keyword.ieam}}에서 존재하지 않을 경우 네임스페이스를 작성한 후 {{site.data.keyword.ieam}}에서 운영자를 배치 해제하면 해당 네임스페이스를 제거합니다.

## {{site.data.keyword.ieam}}의 연산자 패키지

연산자가 작성되고 테스트된 후 {{site.data.keyword.ieam}}에서 배치를 위해 패키지해야 합니다.

1. 클러스터 내에서 배치로 실행하기 위해 연산자가 패키지되는지 확인하십시오. 이는 연산자가 빌드되어 {{site.data.keyword.ieam}}에 의해 배치될 때 컨테이너가 검색되는 컨테이너 레지스트리에 푸시됨을 의미합니다. 일반적으로 이 작업은 **operator-sdk build** 다음에 **docker push**가 오는 명령을 사용하여 운영자를 빌드함으로써 완료됩니다. 이는 [운영자 학습서](https://sdk.operatorframework.io/docs/building-operators/golang/tutorial/#2-run-as-a-deployment-inside-the-cluster)에 설명되어 있습니다.

2. 서비스 컨테이너 또는 연산자에 의해 배치되는 컨테이너가 연산자가 배치하는 레지스트리에도 푸시되는지 확인하십시오.

3. 연산자 프로젝트에서 연산자의 yaml 정의 파일을 포함하는 아카이브를 작성하십시오.

   ```bash
   cd <operator-project>/<operator-name>/deploy    tar -zcvf <archive-name>.tar.gz ./*
   ```
   {: codeblock}

   **참고**: {{site.data.keyword.macos_notm}} 사용자의 경우 tar.gz 파일에 숨겨진 파일이 존재하지 않도록 깨끗한 아카이브 tar.gz 파일을 작성하는 방법을 고려해 보십시오. 예를 들어, .DS_store 파일은 heml 운영자를 배치하는 경우 문제가 될 수 있습니다. 숨겨진 파일이 있다고 의심되면 {{site.data.keyword.linux_notm}}시스템에 tar.gz 압축을 푸십시오. 자세한 정보는 [macos의 Tar 명령](https://stackoverflow.com/questions/8766730/tar-command-in-mac-os-x-adding-hidden-files-why)을 참조하십시오.

   ```bash
   tar -xzpvf x.tar --exclude=".*"
   ```
   {: codeblock}

4. {{site.data.keyword.ieam}} 서비스 작성 도구를 사용하여 연산자 서비스에 대해 서비스 정의를 작성하십시오. 예를 들어, 다음을 수행하십시오.

   1. 새 프로젝트를 작성하십시오.

      ```bash
      hzn dev service new -V <a version> -s <a service name> -c cluster
      ```
      {: codeblock}

   2. 이전에 3단계에서 작성된 연산자의 yaml 아카이브를 가리키도록 **horizon/service.definition.json** 파일을 편집하십시오.

   3. 서비스 서명 키를 작성하거나 이미 작성한 서비스 서명 키를 사용하십시오.

   4. 서비스 공개

      ```
      hzn exchange service publish -k <signing key> -f ./horizon/service.definition.json
      ```
      {: codeblock}

5. 배치 정책 또는 패턴을 작성하여 연산자 서비스를 에지 클러스터에 배치하십시오.
