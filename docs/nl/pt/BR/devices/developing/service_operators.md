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

Em geral, o desenvolvimento de um serviço que será executado em um cluster de borda é semelhante ao desenvolvimento de um serviço de borda que é executado em um dispositivo de borda. O serviço de borda é criado usando as [Melhores práticas de desenvolvimento nativo de borda](best_practices.md) e é empacotado em um contêiner. A diferença está no modo como o serviço de borda é implementado.

Para implementar um serviço de borda conteinerizado em um cluster de borda, um desenvolvedor deve primeiro construir um operador do Kubernetes que implementa o serviço de borda conteinerizado em um cluster do Kubernetes. Depois que o operador é gravado e testado, o desenvolvedor cria e publica o operador como um serviço {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}). Este processo permite que um administrador do {{site.data.keyword.ieam}} implemente o serviço do operador tal como faria para qualquer serviço {{site.data.keyword.ieam}}, com política ou padrões. Não é necessário de criar uma definição de serviço {{site.data.keyword.ieam}} para o serviço de borda. Quando o administrador do {{site.data.keyword.ieam}} implementa o serviço do operador, o operador implementa o serviço de borda.

Várias opções estão disponíveis quando você grava um operador do Kubernetes. Primeiro, leia [Conceitos do Kubernetes - Padrão do operador ![Abre em uma nova guia](../../images/icons/launch-glyph.svg "Abre em uma nova guia")](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/). Este site é um bom recurso para aprender sobre os operadores. Depois que você está familiarizado com os conceitos do operador, a gravação de um operador é feita usando a [Estrutura do operador ![Abre em uma nova guia](../../images/icons/launch-glyph.svg "Abre em uma nova guia")](https://github.com/operator-framework/getting-started). Este artigo fornece mais detalhes sobre o que é um operador e fornece uma passagem para criar um operador simples, usando o operador do Software Development Kit (SDK).

## Considerações ao desenvolver um operador para o {{site.data.keyword.ieam}}

É uma melhor prática fazer uso liberal da capacidade de status do operador porque o {{site.data.keyword.ieam}} relata qualquer que seja o status que o operador cria no hub de gerenciamento do {{site.data.keyword.ieam}}. Ao gravar um operador, a estrutura do operador gera uma Custom Resource Definition
(CRD) do Kubernetes para o operador. O CRD de todo operador possui um objeto de status, que deve ser preenchido com informações de status importantes sobre o estado do operador e do serviço de borda que ele está implementando. Isso não é feito automaticamente pelo Kubernetes; ele precisa ser
gravado na implementação do operador pelo desenvolvedor do operador. O agente {{site.data.keyword.ieam}} em um cluster de borda reúne periodicamente o status do operador e o relata ao hub de gerenciamento.

Se desejado, o operador pode anexar as variáveis de ambiente {{site.data.keyword.ieam}} específicas do serviço a quaisquer serviços que ele iniciar. Quando o operador é iniciado, o agente {{site.data.keyword.ieam}} cria um configmap do Kubernetes chamado `hzn-env-vars`, que contém as variáveis de ambiente específicas do serviço. O operador pode, opcionalmente, anexar esse mapa de configuração a quaisquer implementações que ele cria, o que permite que os serviços que ele inicia reconheçam as mesmas variáveis de ambiente específicas do serviço. Essas são as mesmas variáveis de ambiente que são injetadas em serviços que são executados em dispositivos de borda. A única exceção é as variáveis de ambiente ESS*, pois o Model Management System (MMS) ainda não é suportado para os serviços de cluster de borda.

Se desejado, os operadores que são implementados pelo {{site.data.keyword.ieam}} podem ser implementados em um namespace diferente do namespace padrão. Isso é executado pelo desenvolvedor do operador, que modifica os arquivos YAML do operador para apontar para o namespace. Existem duas formas de fazer isso:

 * Modifique a definição de Implantação do operador (geralmente chamada **./deploy/operator.yaml**) para especificar um namespace

ou

* Inclua um arquivo YAML de definição de namespace com os arquivos YAML de definição do operador; por exemplo, no diretório **./deploy** do projeto do operador.

Nota: quando um operador é implementado em um namespace não padrão, o {{site.data.keyword.ieam}} cria o namespace quando ele não existe e o remove quando a implementação do operador é removida pelo {{site.data.keyword.ieam}}.

## Gravando um operador para {{site.data.keyword.ieam}}

Depois que um operador é gravado e testado, ele precisa ser empacotado para implementação pelo {{site.data.keyword.ieam}}:

1. Assegure-se de que o operador seja empacotado para ser executado como uma implementação dentro de um cluster. Isso significa que o operador é construído em um contêiner e enviado por push para o registro de contêiner a partir do qual o contêiner é recuperado quando implementado pelo {{site.data.keyword.ieam}}. Geralmente, isso é feito por meio da construção do operador, usando os comandos **operator-sdk build**, seguidos por **docker push**. Isso é descrito em [Operator Framework ![Abre em uma nova guia](../../images/icons/launch-glyph.svg "Abre em uma nova guia")](https://github.com/operator-framework/getting-started#1-run-as-a-deployment-inside-the-cluster).

2. Assegure-se de que o um ou mais contêineres de serviço que são implementados pelo operador também sejam enviados por push para o registro a partir do qual o operador irá implementá-los.

3. Crie um archive que contenha os arquivos de definição de yaml do operador a partir do projeto do operador:

   ```bash
   cd <operator-project>/<operator-name>/deploy
    tar -zcvf <archive-name>.tar.gz
   ```
   {: codeblock}

4. Use as ferramentas de criação de serviço do {{site.data.keyword.ieam}} para criar uma definição de serviço para o serviço do operador, por exemplo, siga estas etapas:

   1. Crie um novo projeto:

      ```bash
      hzn dev service new -V <a version> -s <a service name> -c cluster
      ```
      {: codeblock}

   2. Edite o arquivo **horizon/service.definition.json** para apontar para o archive YAML do operador, criado na etapa 3.

   3. Crie ou use uma chave de assinatura de serviço pré-existente.

   4. Publique o serviço

      ```
      hzn exchange service publish -k <signing key> -f ./horizon/service.definition.json
      ```
      {: codeblock}

5. Crie uma política de implementação ou um padrão para implementar o serviço do operador em um cluster de borda.
