---

copyright:
years: 2020
lastupdated: "2020-10-7"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Considerações de GDPR

## Aviso
{: #notice}
<!-- This is boilerplate text provided by the GDPR team. It cannot be changed. -->

Este documento tem como objetivo ajudá-lo a se preparar para o GDPR. Ele fornece informações de recursos do {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) você pode configurar e aspectos do uso do produto a serem considerados quando você estiver preparando a sua organização para o GDPR. Esta informação não é uma lista completa. Os clientes podem escolher e configurar os recursos de muitas maneiras diferentes e usar o produto de várias formas e com aplicativos e sistemas de terceiros.

<p class="ibm-h4 ibm-bold">Os clientes são responsáveis por assegurar sua própria conformidade com várias leis e regulamentações, inclusive com a General Data Protection Regulation da União Europeia. Os clientes são os únicos responsáveis por obter conselhos de consultoria jurídica competente quanto à identificação e interpretação de quaisquer leis e regulamentações relevantes que possam afetar os negócios dos clientes e quaisquer ações que eles precisem tomar para obedecer tais leis e regulamentações.</p>

<p class="ibm-h4 ibm-bold">Os produtos, serviços e outros recursos que são descritos aqui não são adequados para todas as situações do cliente e podem restringir a disponibilidade. A IBM não fornece assessoria jurídica, contábil ou de auditoria nem representa ou garante que seus serviços ou produtos asseguram que os clientes estejam em conformidade com qualquer lei ou regulamento.</p>

## Índice

* [GDPR](#overview)
* [Configuração do Produto para GDPR](#productconfig)
* [Ciclo de Vida de Dados](#datalifecycle)
* [Processamento de Dados](#dataprocessing)
* [Capacidade para restringir o uso de dados pessoais](#datasubjectrights)
* [Apêndice](#appendix)

## GDPR
{: #overview}

<!-- This is boilerplate text provided by the GDPR team. It cannot be changed. -->
O Regulamento Geral sobre a Proteção de Dados (GDPR) foi adotado pela União Europeia (UE) e é aplicável a partir de 25 de maio de 2018.

### Por que é importante? GDPR

O GDPR estabelece uma estrutura regulamentar de proteção de dados mais forte para processamento de dados pessoais de indivíduos. GDPR traz:

* Novos direitos e aprimorado para indivíduos
* Definição ampliada de dados pessoais
* Novas obrigações para empresas e organizações que lidam com dados pessoais
* Penalidades financeiras significativas por falta de conformidade
* Notificação de violação de dados obrigatórios

A IBM estabeleceu um programa de prontidão global com a tarefa de preparar os processos internos e as ofertas comerciais da IBM para conformidade com o GDPR.

### Mais informações

* [Portal de Informações de GDPR da UE](https://gdpr.eu/)
*  [Website do ibm.com/GDPR](https://www.ibm.com/data-responsibility/gdpr/)

## Configuração do produto - considerações para preparação para o GDPR
{: #productconfig}

As seções a seguir descrevem aspectos do {{site.data.keyword.ieam}} e fornecem informações sobre recursos para ajudar os clientes com os requisitos do GDPR.

### Ciclo de Vida de Dados
{: #datalifecycle}

O {{site.data.keyword.ieam}} é um aplicativo para desenvolver e gerenciar aplicativos conteinerizados locais. É um ambiente integrado para gerenciar cargas de trabalho de contêiner na borda. Ele inclui o orquestrador de contêineres Kubernetes, um registro de imagem privado, um console de gerenciamento, um agente do nó de borda e estruturas de monitoramento.

Dessa forma, o {{site.data.keyword.ieam}} trabalha principalmente com dados técnicos relacionados à configuração e gerenciamento do aplicativo, alguns dos quais podem estar sujeitos ao GDPR. O {{site.data.keyword.ieam}} também lida com informações sobre usuários que gerenciam o aplicativo. Esses dados são descritos ao longo deste documento para conscientizar os clientes responsáveis por atender aos requisitos do GDPR.

Esses dados são persistidos no {{site.data.keyword.ieam}} em sistemas de arquivos locais ou remotos como arquivos de configuração ou em bancos de dados. Os aplicativos desenvolvidos para serem executados no {{site.data.keyword.ieam}} podem usar outras formas de dados pessoais sujeitos ao GDPR. Os mecanismos que são usados para proteger e gerenciar dados também estão disponíveis para os aplicativos executados no {{site.data.keyword.ieam}}. Mais mecanismos podem ser necessários para gerenciar e proteger dados pessoais que são coletados por aplicativos executados no {{site.data.keyword.ieam}}.

Para entender os fluxos de dados do {{site.data.keyword.ieam}}, deve-se entender como o Kubernetes, o Docker e os Operadores funcionam. Esses componentes de software livre são fundamentais para o {{site.data.keyword.ieam}}. Use o {{site.data.keyword.ieam}} para colocar instâncias de contêineres de aplicativos (serviços de borda) em nós de borda. Os serviços de borda contêm os detalhes sobre o aplicativo e as imagens do Docker contêm todos os pacotes de software que seus aplicativos precisam para serem executados.

O {{site.data.keyword.ieam}} inclui um conjunto de exemplos de serviços de borda de software livre. Para visualizar uma lista de todos os gráficos do {{site.data.keyword.ieam}}, consulte [open-horizon/examples](https://github.com/open-horizon/examples){:new_window}. É responsabilidade do cliente determinar e implementar os controles apropriados do GDPR para software livre.

### Que tipos de fluxo de dados através do {{site.data.keyword.ieam}}

O {{site.data.keyword.ieam}} lida com várias categorias de dados técnicos que podem ser considerados dados pessoais, como:

* ID do usuário e senha do operador ou administrador
* endereço IP
* Nomes do nó do Kubernetes

As informações sobre como esses dados técnicos são coletados e criados, armazenados, acessados, protegidos, registrados e excluídos são descritos em seções posteriores deste documento.

### Dados pessoais usados para contato on-line com a IBM

Os clientes do {{site.data.keyword.ieam}} podem enviar comentários, feedback e solicitações on-line para a IBM sobre assuntos relacionados ao {{site.data.keyword.ieam}} de várias maneiras, principalmente:

* A Comunidade de folga do {{site.data.keyword.ieam}} pública
* Área de comentários públicos nas páginas da documentação do produto do {{site.data.keyword.ieam}}
* Comentários públicos no espaço do {{site.data.keyword.ieam}} de dW Answers

Normalmente, apenas o nome do cliente e o endereço de e-mail são usados para permitir respostas pessoais para o assunto do contato. Esse uso de dados pessoais está em conformidade com a [Declaração de Privacidade On-line da IBM](https://www.ibm.com/privacy/us/en/){:new_window}.

### Autenticação

O gerenciador de autenticação do {{site.data.keyword.ieam}} aceita credenciais de usuário do {{site.data.keyword.gui}} e encaminha as credenciais para o provedor OIDC de back-end, que valida as credenciais do usuário com relação ao diretório corporativo. O provedor OIDC então retorna um cookie de autenticação (`auth-cookie`) com o conteúdo de um JSON Web Token (`JWT`) para o gerenciador de autenticação. O token JWT persistir informações como o ID do usuário e o endereço de e-mail, além de associação ao grupo no momento da solicitação de autenticação. Esse cookie de autenticação é, então, enviado de volta para a {{site.data.keyword.gui}}. O cookie é atualizado durante a sessão. Ele é válido por 12 horas depois que você sair da {{site.data.keyword.gui}} ou fechar o navegador da web.

Para todas as solicitações de autenticação subsequentes feitas a partir do {{site.data.keyword.gui}}, o servidor NodeJS de front-end decodifica o cookie de autenticação disponível na solicitação e valida a solicitação chamando o gerenciador de autenticação.

A CLI do {{site.data.keyword.ieam}} requer que o usuário forneça uma chave de API. As chaves de API são criadas usando o comando `cloudctl`.

As CLIs **cloudctl**, **kubectl** e **oc** também requerem credenciais para acessar o cluster. Essas credenciais podem ser obtidas do console de gerenciamento e expiram após 12 horas.

### Mapeamento de função

O {{site.data.keyword.ieam}} suporta controle de acesso baseado na função (RBAC). No estágio de mapeamento de função, o nome do usuário fornecido no estágio de autenticação é mapeado para uma função de usuário ou grupo. As funções são utilizadas para autorizar quais atividades podem ser realizadas pelo usuário autenticado. Consulte [Controle de acesso baseado na função](rbac.md) para obter detalhes sobre as funções do {{site.data.keyword.ieam}}.

### Segurança de Pod

As políticas de segurança de pod são usadas para configurar o hub de gerenciamento ou o controle do cluster de borda sobre o que um pod pode fazer ou acessar. Para obter mais informações sobre pods, consulte [Instalando o hub de gerenciamento](../hub/hub.md) e [Clusters de borda](../installing/edge_clusters.md).

## Processamento de Dados
{: #dataprocessing}

Os usuários do {{site.data.keyword.ieam}} podem controlar a maneira pela qual dados técnicos relacionados à configuração e ao gerenciamento são processados e assegurados por meio da configuração do sistema.

* O controle de acesso baseado na função (RBAC) controla quais dados e funções podem ser acessados pelos usuários.

* As políticas de segurança de pod são usadas para configurar o controle de nível do cluster sobre o que um pod pode fazer ou o que ele pode acessar.

* Os dados em trânsito são protegidos usando `TLS`. Utiliza-se `HTTPS` (`TLS` subjacente) para proteger a transferência de dados entre o cliente usuário e os serviços de back-end. Os usuários podem especificar o certificado raiz para usar durante a instalação.

* A proteção de dados em repouso é suportada usando `dm-crypt` para criptografar os dados.

* Os períodos de retenção de dados para criação de log (ELK) e monitoramento (Prometheus) são configuráveis e a exclusão de dados é suportada por meio de APIs fornecidas.

Esses mesmos mecanismos que são usados para gerenciar e proteger os dados técnicos do  {{site.data.keyword.ieam}} podem ser usados para gerenciar e proteger os dados pessoais para aplicativos desenvolvidos ou fornecidos pelo usuário. Os clientes podem desenvolver suas próprias capacidades para implementar controles adicionais.

Para obter mais informações sobre certificados, consulte [Instalar o {{site.data.keyword.ieam}}](../hub/installation.md).

## Capacidade para restringir o uso de dados pessoais
{: #datasubjectrights}

Ao usar os recursos resumidos neste documento, o {{site.data.keyword.ieam}} permite que um usuário restrinja o uso de quaisquer dados técnicos dentro do aplicativo que sejam considerados dados pessoais.

Sob o GDPR, os usuários têm direitos para acessar, modificar e restringir o processamento. Consulte outras seções deste documento para controlar:
* Direito de acesso
  * Os administradores do {{site.data.keyword.ieam}} podem usar os recursos do {{site.data.keyword.ieam}} para fornecer às pessoas acesso a seus dados.
  * Os administradores do {{site.data.keyword.ieam}} podem usar os recursos do {{site.data.keyword.ieam}}  para fornecer aos indivíduos informações sobre quais dados o {{site.data.keyword.ieam}} coleta e retém sobre o indivíduo.
* Certo modificar
  * Os administradores do {{site.data.keyword.ieam}} podem usar recursos do {{site.data.keyword.ieam}} para permitir que um indivíduo modifique ou corrija seus dados.
  * Os administradores do {{site.data.keyword.ieam}} podem usar recursos do {{site.data.keyword.ieam}} para corrigir os dados de um indivíduo para eles.
* Certo para restringir o processamento
  * Os administradores do {{site.data.keyword.ieam}} podem usar recursos do {{site.data.keyword.ieam}} para parar o processamento de dados de um indivíduo.

## Apêndice - Dados registrados pelo {{site.data.keyword.ieam}}
{: #appendix}

Como um aplicativo, o {{site.data.keyword.ieam}} lida com várias categorias de dados técnicos que podem ser considerados dados pessoais:

* ID do usuário e senha do operador ou administrador
* endereço IP
* Nomes do nó do Kubernetes. 

O {{site.data.keyword.ieam}}  também lida com informações sobre usuários que gerenciam os aplicativos que são executados no {{site.data.keyword.ieam}} e pode apresentar outras categorias de dados pessoais desconhecidos para o aplicativo.

### {{site.data.keyword.ieam}} segurança

* O dados são registrados
  * ID do usuário, nome do usuário e endereço IP dos usuários conectados
* Quando os dados são registrados
  * Com pedidos de login
* Onde dados são registrados
  * Nos logs de auditoria em `/var/lib/icp/audit`???
  * Nos logs de auditoria em `/var/log/audit`???
  * Logs do Exchange em ???
* Como excluir dados
  * Procure os dados e exclua o registro do log de auditoria

### API {{site.data.keyword.ieam}}

* O dados são registrados
  * ID do usuário, nome do usuário e endereço IP do cliente nos logs do contêiner
  * Dados de estado do cluster do Kubernetes no servidor `etcd`
  * Credenciais do OpenStack e do VMware no servidor `etcd`
* Quando os dados são registrados
  * Com pedidos de API
  * As credenciais armazenadas do `credentials-set` comando
* Onde dados são registrados
  * Em logs de contêiner, Elasticsearch e servidor `etcd`.
* Como excluir dados
  * Exclua logs do contêiner (`platform-api`, `platform-deploy`) dos contêineres ou exclua as entradas de log específicas do usuário do Elasticsearch.
  * Limpe os pares chave-valor `etcd` selecionados usando o comando `etcdctl rm`.
  * Remova as credenciais chamando o comando `credentials-unset`.


Para obter informações adicionais, consulte

  * [Criação de log Kubernetes](https://kubernetes.io/docs/concepts/cluster-administration/logging/){:new_window}
  * [etcdctl](https://github.com/coreos/etcd/blob/master/etcdctl/READMEv2.md){:new_window}

### {{site.data.keyword.ieam}} de monitoramento

* O dados são registrados
  * Endereço IP, nomes de pods, liberação, imagem
  * Os dados extraídos de aplicativos desenvolvidos pelo cliente podem incluir dados pessoais
* Quando os dados são registrados
  * Quando o Prometheus extrai métricas de destinos configurados
* Onde dados são registrados
  * No servidor Prometheus ou volumes persistentes configurados
* Como excluir dados
  * Procure e exclua dados usando a API do Prometheus

Para obter mais informações, consulte [Documentação Prometheus](https://prometheus.io/docs/introduction/overview/){:new_window}.


### {{site.data.keyword.ieam}} Kubernetes

* O dados são registrados
  * Topologia implementada de cluster (informações de nó para controlador, trabalhador, proxy e va)
  * Configuração de serviço (mapa de configuração do k8s) e segredos (segredos do k8s)
  * ID do usuário no log do apiserver
* Quando os dados são registrados
  * Ao implementar um cluster
  * Ao implementar um aplicativo do catálogo do Helm
* Onde dados são registrados
  * Topologia de cluster implementada no `etcd`
  * Configuração e segredo para aplicativos implementados em `etcd`
* Como excluir dados
  * Use o {{site.data.keyword.ieam}} {{site.data.keyword.gui}}
  * Procure e exclua dados usando o {{site.data.keyword.gui}} do k8s (`kubectl`) ou a API de REST `etcd`
  * Procure e exclua dados de log do apiserver usando a API do Elasticsearch

Tenha cuidado ao modificar a configuração do cluster Kubernetes ou ao excluir dados do cluster.

  Para obter mais informações, consulte [Kubernetes kubectl](https://kubernetes.io/docs/reference/kubectl/overview/){:new_window}.

### {{site.data.keyword.ieam}} API Helm

* O dados são registrados
  * Nome do usuário e função
* Quando os dados são registrados
  * Quando um usuário recupera gráficos ou repositórios que são incluídos em uma equipe
* Onde dados são registrados
  * Logs de implementação api-helm, Elasticsearch
* Como excluir dados
  * Procure e exclua dados do log helm-api usando a API do Elasticsearch

### {{site.data.keyword.ieam}} Service Broker

* O dados são registrados
  * ID do usuário (somente no nível de log de depuração 10, não no nível de log padrão)
* Quando os dados são registrados
  * Quando solicitações de API são feitas no broker de serviço
  * Quando o broker de serviço acessa o catálogo de serviços
* Onde dados são registrados
  * Log de contêiner do broker de serviço, Elasticsearch
* Como excluir dados
  * Procure e exclua o log do apiserver que usa a API do Elasticsearch
  * Procure e exclua o log do contêiner do apiserver
      ```
      kubectl logs $(kubectl get pods -n kube-system | grep  service-catalogapiserver | awk '{print $1}') -n kube-system | grep admin
      ```
      {: codeblock}


  Para obter mais informações, consulte [Kubernetes kubectl](https://kubernetes.io/docs/reference/kubectl/overview/){:new_window}.
