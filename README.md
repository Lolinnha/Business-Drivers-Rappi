# Business Drivers da Rappi

&emsp;&emsp;Os business drivers são fatores estratégicos que impulsionam o sucesso de uma empresa. No caso da Rappi, foram definidos dois business drivers para otimizar a operação logística e a retenção de entregadores neste trabalho. 

&emsp;&emsp;O primeiro foca em garantir que pelo menos 50% dos entregadores realizem **20 pedidos em até 14 dias**, promovendo engajamento e continuidade na plataforma. O segundo busca reduzir **o tempo de alocação de entregadores**, garantindo que **90% dos pedidos sejam aceitos em até 15 minutos**, melhorando a experiência dos clientes.  

# Tabela de Business Drivers 

| **Business Driver** | **Objetivo** | **Métrica** | **Indicador de Sucesso** | **Impacto** |
|--------------------|-------------|------------|------------------------|------------|
| **Taxa de Retenção nos Primeiros 20 Pedidos** | 50% dos entregadores que aceitaram o primeiro pedido devem completar pelo menos 20 pedidos em até duas semanas. | Taxa de retenção de entregadores. | Se 50% dos entregadores completarem pelo menos 20 pedidos dentro desse período. | Melhorar a retenção de entregadores e garantir uma base ativa na plataforma. |
| **Tempo Máximo para Encontrar um Entregador** | O tempo máximo permitido para encontrar um entregador é de 15 minutos. | Tempo de alocação do entregador. | 90% dos pedidos devem ser alocados dentro de 15 minutos. | Reduzir o tempo de espera dos clientes e melhorar a experiência do usuário. |

# Diagramas Structurizr 

&emsp;&emsp;Os diagramas abaixo representam a estrutura dos sistemas da Rappi para acompanhar os dois business drivers escolhidos:  
1. **Taxa de Retenção nos Primeiros 20 Pedidos**  
2. **Tempo Máximo para Encontrar um Entregador**  

Cada diagrama mostra como os principais componentes se relacionam dentro da plataforma da Rappi.  

---

## 1. Diagrama - Taxa de Retenção nos Primeiros 20 Pedidos  

&emsp;&emsp;O diagrama representa a relação entre os **entregadores**, a plataforma da **Rappi** e o **acompanhamento da taxa de retenção**. Ele mostra como os dados dos entregadores são processados para verificar se **50% dos entregadores completaram pelo menos 20 pedidos em até duas semanas**.

&emsp;&emsp;Segue abaixo o código utilizado para a construção no Structurizr:

```plaintext
workspace "Taxa de Retenção nos Primeiros 20 pedidos" "Mapa do fluxo de retenção de entregadores nos primeiros 20 pedidos." {

    model {
        entregador = person "Entregador"
        appRappi = softwareSystem "App Rappi"
        moduloRetencao = softwareSystem "Módulo de Retenção de Entregadores"
        bancoDados = softwareSystem "Banco de Dados de Entregadores"

        entregador -> appRappi "Realiza entregas"
        appRappi -> moduloRetencao "Registra progresso do entregador"
        moduloRetencao -> bancoDados "Armazena dados de retenção"
        bancoDados -> moduloRetencao "Fornece insights sobre retenção"
        moduloRetencao -> appRappi "Gera incentivos e feedback"
        appRappi -> entregador "Notifica incentivos e feedback"
    }
}
```

&emsp;&emsp;No PlantUML, podemos representar o fluxo de interação entre os elementos como um diagrama de componentes ou diagrama de sequência. Aqui o relacionamento estabelecido é entre o entregador e o App onde podem realizar as entregas e o banco de dados fornecendo as informações de retenção e churn dos entregadores. 

<div align="center">
  <sub>Figura 1: Diagrama Taxa de Retenção</sub>
  <img src="./images/diagrama-taxa-retencao.png" alt="Taxa de Retenção" width="100%">
  <sup>Fonte: Anna Aragão (2025)</sup>
</div>

## 2. Diagrama - Tempo Máximo para Alocar 90% dos Entregadores em 15 minutos

&emsp;&emsp;O diagrama representa o fluxo operacional da alocação de entregadores no aplicativo Rappi, garantindo que 90% dos entregadores sejam alocados em até 15 minutos.

&emsp;&emsp;Segue abaixo o código utilizado para a construção no Structurizr:

```plaintext
workspace "Tempo Máximo para Encontrar um Entregador em 15 minutos" "Fluxo de alocação de entregadores no app Rappi." {

    model {
        entregador = person "Entregador"
        appRappi = softwareSystem "App Rappi"
        alocador = softwareSystem "Alocador de Entregadores"
        bancoDados = softwareSystem "Banco de Dados de Entregadores"

        appRappi -> alocador "Solicita entregador"
        alocador -> bancoDados "Consulta entregadores disponíveis"
        bancoDados -> alocador "Retorna entregadores disponíveis"
        alocador -> appRappi "Envia entregador selecionado"
        appRappi -> entregador "Notifica entrega disponível"
        entregador -> appRappi "Aceita entrega"
    }
    
}
```

&emsp;&emsp;No PlantUML, podemos representar o fluxo de interação entre os elementos como um diagrama de componentes ou diagrama de sequência. O relacionamento aqui estabelecido é entre o entregador e o aplicativo, ao qual ele pode aceitar entregas. No entanto, antes da etapa de aceite, há um processo de back-office responsável pela alocação dos entregadores. Esse processo envolve a interação entre o banco de dados, o time de operações (responsável pela alocação) e o aplicativo, que seleciona os entregadores mais adequados para determinada solicitação. Nesse contexto, ocorre a mudança de estado do entregador: de "disponível", quando está em busca de entregas, para "aguardando pedido" ou "a caminho do pedido", caso seja corretamente alocado.

<div align="center">
  <sub>Figura 2: Diagrama Alocação dos Entregadores</sub>
  <img src="./images/diagrama-alocacao-entregadores.png" alt="Alocação dos Entregadores" width="100%">
  <sup>Fonte: Anna Aragão (2025)</sup>
</div>