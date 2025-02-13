Feature: Registro de pedidos e envio de incentivos para entregadores

  Scenario: Registro de um novo pedido para um entregador
    Given um entregador cadastrado no sistema
    And o entregador já completou 19 pedidos
    When o entregador realiza mais um pedido com sucesso
    Then o sistema deve registrar o 20º pedido no banco de dados
    And o sistema deve enviar um incentivo para o entregador
    And o entregador deve ser notificado sobre o incentivo no app

  Scenario: Enviar incentivo apenas quando o entregador atinge 20 pedidos
    Given um entregador cadastrado no sistema
    And o entregador já completou 19 pedidos
    When o entregador realiza mais um pedido com sucesso
    Then o sistema deve registrar o 20º pedido no banco de dados
    And o sistema deve enviar um incentivo para o entregador
    And o entregador deve ser notificado sobre o incentivo no app
