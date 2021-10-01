---

copyright:
years: 2020
lastupdated: "2020-1-31"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Usando o console {{site.data.keyword.edge_notm}}
{: #accessing_ui}

Use o console para executar funções de gerenciamento de computação de borda. 
 
## Navegando para o console do {{site.data.keyword.edge_notm}}

1. Acesse o console do {{site.data.keyword.edge_notm}}, navegando para `https://<cluster-url>/edge`, em que `<cluster-url>` é o ingresso externo do cluster.
2. Digite suas credenciais do usuário. A página de login do {{site.data.keyword.mcm}}
é exibida.
3. Na barra de endereços do navegador, remova `/multicloud/welcome` do final da URL, inclua `/edge` e pressione **Enter**. A página {{site.data.keyword.edge_notm}}
é exibida.

## Navegadores Suportados

O {{site.data.keyword.edge_notm}} foi testado com sucesso com esses navegadores.

|Plataforma|Navegadores Suportados|
|--------|------------------|
|Microsoft Windows™|<ul><li>Mozilla Firefox - versão mais recente para Windows</li><li>Google Chrome - versão mais recente para Windows</li></ul>|
|{{site.data.keyword.macOS_notm}}|<ul><li>Mozilla Firefox - versão mais recente para Mac</li><li>Google Chrome - versão mais recente para Mac</li></ul>|
{: caption="Tabela 1. Navegadores suportados no {{site.data.keyword.edge_notm}}" caption-side="top"}


## Explorando o Console do
{{site.data.keyword.edge_notm}}
{: #exploring-management-console}

Os recursos do console do {{site.data.keyword.edge_notm}} incluem:

* Integração fácil e simples, com links de sites periféricos oferecendo um suporte mais seguro
* Amplos recursos de visibilidade e gerenciamento:
  * Visualizações de gráficos abrangentes, incluindo status do nó, arquitetura e informações de erro
  * Detalhes de erros, com links para suporte de resolução
  * Localização e filtragem de conteúdo que inclui informações sobre: 
    * Proprietários
    * Arquitetura 
    * Pulsação (por exemplo, os últimos 10 minutos, hoje e assim por diante)
    * Estado do nó (Ativo, Inativo, Com erro e assim por diante)
    * Tipo de implementação (política ou padrão)
  * Detalhes úteis sobre nós de borda do Exchange, incluindo:
    * Propriedades
    * Restrições 
    * Implementações
    * Serviços ativos

* Recursos de visualização potentes

  * Capacidade de rapidamente localizar e filtrar por: 
    * Owner
    * Arquitetura
    * Versão
    * Público (true ou false)
  * Visualizações de serviço de lista ou cartão
  * Serviços agrupados que compartilham um nome
  * Detalhes para cada serviço na troca que inclui: 
    * Propriedades
    * Restrições
    * Implementações
    * Variáveis de serviço
    * Dependências do serviço
  
* Gerenciamento da política de implementação

  * Capacidade de rapidamente localizar e filtrar por:
    * ID de política
    * Owner
    * Rótulo
  * Implementar qualquer serviço do Exchange
  * Incluir propriedades em políticas de implementação
  * Um construtor de restrições para a construção de expressões 
  * Um modo avançado, permitindo a gravação de restrições diretamente no JSON
  * A capacidade de ajustar as versões de implementação de retrocesso e as configurações de funcionamento do nó
  * Visualizar e editar detalhes da política, que incluem:
    * Propriedades de serviço e de implementação
    * Restrições
    * Recuperações
    * Configurações de funcionamento do nó
  
