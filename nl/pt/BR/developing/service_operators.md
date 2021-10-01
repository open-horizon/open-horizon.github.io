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

# Desenvolvendo um operador de Kubernetes
{: #kubernetes_operator}

Em geral, o desenvolvimento de um serviço que será executado em um cluster de borda é semelhante ao desenvolvimento de um serviço de borda que é executado em um dispositivo de borda. O serviço de borda é desenvolvido por meio da ampliação das [Boas práticas de desenvolvimento de borda nativa](../OH/docs/developing/best_practices.md) e vem empacotado em um contêiner. A diferença está no modo como o serviço de borda é implementado.

Para implementar um serviço de borda conteinerizado em um cluster de borda, um desenvolvedor deve primeiro construir um operador do Kubernetes que implementa o serviço de borda conteinerizado em um cluster do Kubernetes. Depois que o operador é gravado e testado, o desenvolvedor cria e publica o operador como um serviço {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}). Este processo permite que um administrador do {{site.data.keyword.ieam}} implemente o serviço do operador tal como faria para qualquer serviço {{site.data.keyword.ieam}}, com política ou padrões. Não é necessário de criar uma definição de serviço {{site.data.keyword.ieam}} para o serviço de borda. Quando o administrador do {{site.data.keyword.ieam}} implementa o serviço do operador, o operador implementa o serviço de borda.

Várias fontes de informação estão disponíveis quando você escreve um operador Kubernetes. Primeiro, leia [Conceitos de Kubernetes - Padrão do operador](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/). Este site é um bom recurso para aprender sobre os operadores. Depois que você estiver familiarizado com os conceitos do operador, a gravação de um operador é realizada usando o [Operator Framework](https://operatorframework.io/). Este website fornece mais detalhes sobre o que é um operador e apresenta instruções sobre como criar um operador simples usando Software Development Kit (SDK).

## Considerações ao desenvolver um operador para o {{site.data.keyword.ieam}}

É uma melhor prática fazer uso liberal da capacidade de status do operador porque o {{site.data.keyword.ieam}} relata qualquer que seja o status que o operador cria no hub de gerenciamento do {{site.data.keyword.ieam}}. Ao gravar um operador, a estrutura do operador gera uma Custom Resource Definition (CRD) do Kubernetes para o operador. O CRD de todo operador possui um objeto de status, que deve ser preenchido com informações de status importantes sobre o estado do operador e do serviço de borda que ele está implementando. Isso não é feito automaticamente pelo Kubernetes; ele precisa ser gravado na implementação do operador pelo desenvolvedor do operador. O agente {{site.data.keyword.ieam}} em um cluster de borda reúne periodicamente o status do operador e o relata ao hub de gerenciamento.

O operador pode optar por conectar as variáveis de ambiente específicas do serviço {{site.data.keyword.ieam}} a quaisquer serviços que ele iniciar. Quando o operador é iniciado, o agente {{site.data.keyword.ieam}} cria um configmap do Kubernetes chamado `hzn-env-vars` que contém as variáveis de ambiente específicas do serviço. O operador pode, opcionalmente, anexar esse mapa de configuração a quaisquer implementações que ele cria, o que permite que os serviços que ele inicia reconheçam as mesmas variáveis de ambiente específicas do serviço. Essas são as mesmas variáveis de ambiente que são injetadas em serviços que são executados em dispositivos de borda. A única exceção são as variáveis de ambiente ESS*, pois o Model Management System (MMS) ainda não é suportado para serviços de cluster de borda.

Se desejado, os operadores que são implementados pelo {{site.data.keyword.ieam}} podem ser implementados em um namespace diferente do namespace padrão. Isso é executado pelo desenvolvedor do operador, que modifica os arquivos YAML do operador para apontar para o namespace. Existem duas formas de fazer isso:

* Modifique a definição de Implantação do operador (geralmente chamada **./deploy/operator.yaml**) para especificar um namespace

ou

* Inclua um arquivo YAML de definição de namespace com os arquivos YAML de definição do operador; por exemplo, no diretório **./deploy** do projeto do operador.

**Nota**: quando um operador é implementado em um namespace não padrão, o {{site.data.keyword.ieam}} cria o namespace se ele não existe e o remove quando a implementação do operador é removida pelo {{site.data.keyword.ieam}}.

## Empacotando um operador para o {{site.data.keyword.ieam}}

Depois que um operador é gravado e testado, ele precisa ser empacotado para implementação pelo {{site.data.keyword.ieam}}:

1. Assegure-se de que o operador seja empacotado para ser executado como uma implementação dentro de um cluster. Isso significa que o operador é construído em um contêiner e enviado por push para o registro de contêiner a partir do qual o contêiner é recuperado quando implementado pelo {{site.data.keyword.ieam}}. Normalmente, isso é feito construindo o operador por meio do **operator-sdk build** seguido pelos comandos **docker push**. Isto é descrito em [Tutorial do operador](https://sdk.operatorframework.io/docs/building-operators/golang/tutorial/#2-run-as-a-deployment-inside-the-cluster).

2. Assegure-se de que o um ou mais contêineres de serviço que são implementados pelo operador também sejam enviados por push para o registro a partir do qual o operador irá implementá-los.

3. Crie um archive que contenha os arquivos de definição de yaml do operador a partir do projeto do operador:

   ```bash
   cd <operator-project>/<operator-name>/deploy    tar -zcvf <archive-name>.tar.gz ./*
   ```
   {: codeblock}

   **Nota**: para usuários do {{site.data.keyword.macos_notm}}, considere criar um archive tar.gz limpo para assegurar que não haja arquivos ocultos no tar.gz. Por exemplo, um arquivo .DS_store pode causar problemas ao implementar um operador Helm. Se você suspeitar que existe um arquivo oculto, extraia o tar.gz em seu sistema {{site.data.keyword.linux_notm}}. Para obter mais informações, consulte [Comando Tar em macos](https://stackoverflow.com/questions/8766730/tar-command-in-mac-os-x-adding-hidden-files-why).

   ```bash
   tar -xzpvf x.tar --exclude=".*"
   ```
   {: codeblock}

4. Use as ferramentas de criação de serviço do {{site.data.keyword.ieam}} para criar uma definição de serviço para o serviço do operador, por exemplo:

   1. Crie um novo projeto:

      ```bash
      hzn dev service new -V <a version> -s <a service name> -c cluster
      ```
      {: codeblock}

   2. Edite o arquivo **horizon/service.definition.json** para apontar para o arquivo yaml do operador criado anteriormente na etapa 3.

   3. Crie uma chave de assinatura de serviço ou use uma que você já criou.

   4. Publique o serviço

      ```
      hzn exchange service publish -k <signing key> -f ./horizon/service.definition.json
      ```
      {: codeblock}

5. Crie uma política de implementação ou um padrão para implementar o serviço do operador em um cluster de borda.
