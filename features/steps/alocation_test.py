from behave import given, when, then
import time
import random
from features.steps.data import MAX_TEMPO_BUSCA, RAIO_INICIAL, INCREMENTO_RAIO

@given("o sistema inicia a busca por um entregador disponível")
def step_given_sistema_em_busca(context):
    context.tempo_busca = 0  # Inicializa o tempo de busca
    context.raio_busca = RAIO_INICIAL  # Inicia o raio de busca
    context.entregador_encontrado = False  # Flag para verificar se um entregador foi encontrado
    context.entregadores_proximos = []  # Lista de entregadores para alerta

    print(f"[INFO] Iniciando busca por entregador. Raio inicial: {context.raio_busca}m")

    while context.tempo_busca < MAX_TEMPO_BUSCA:
        time.sleep(60)  # Simula a passagem de um minuto real
        context.tempo_busca += 1
        context.raio_busca += INCREMENTO_RAIO  # Aumenta o raio de busca

        print(f"[INFO] Minuto {context.tempo_busca}: Expansão da busca para {context.raio_busca}m.")

        # Simula a chance de encontrar um entregador (40% de chance por minuto)
        if random.random() < 0.4:  
            context.entregador_encontrado = True
            print(f"[SUCESSO] Entregador encontrado no minuto {context.tempo_busca} dentro de {context.raio_busca}m.")
            break  # Encerra a busca

        # Simula a identificação de entregadores que estão finalizando pedidos
        if random.random() < 0.3:  
            entregador_id = f"E{random.randint(100, 999)}"
            print(f"[ALERTA] Entregador {entregador_id} pode ser alertado para um novo pedido.")
            context.entregadores_proximos.append(entregador_id)

    context.erro = None  # Inicializa a variável de erro
    if not context.entregador_encontrado:
        context.erro = "Nenhum entregador disponível dentro do tempo máximo"
        print(f"[ERRO] {context.erro}. Total de {len(context.entregadores_proximos)} entregadores próximos identificados.")
    else:
        print(f"[SUCESSO] Entregador alocado com sucesso em {context.tempo_busca} minutos.")

@when("o sistema encontra um entregador antes de 15 minutos")
def step_when_encontra_entregador(context):
    context.tempo_busca = random.randint(1, 14)  # Garante que o tempo de busca será abaixo de 15 minutos
    context.entregador_encontrado = True
    print(f"[SUCESSO] Entregador encontrado dentro de {context.tempo_busca} minutos.")

@when("o tempo de busca ultrapassa 15 minutos")
def step_when_tempo_excedido(context):
    try:
        if context.tempo_busca <= 15:
            raise ValueError(f"Erro: Tempo de busca não ultrapassou 15 minutos.")
        
        context.busca_falhou = True  # Marca que a busca não teve sucesso
        print(f"[LOG] Tempo final de busca: {context.tempo_busca} minutos. Nenhum entregador encontrado.")
    
    except Exception as e:
        context.erro = str(e)
        print(f"[ERRO] {context.erro}")

@when("não há entregadores próximos com pedidos quase finalizados")
def step_when_nao_ha_entregadores_proximos(context):
    context.entregadores_proximos = []  # Simula a ausência de entregadores próximos
    print("[LOG] Nenhum entregador próximo identificado.")

@when("há entregadores próximos com pedidos quase finalizados")
def step_when_ha_entregadores_proximos(context):
    # Simula a presença de entregadores próximos com pedidos quase finalizados
    context.entregadores_proximos = [f"E{random.randint(100, 999)}" for _ in range(3)]
    print(f"[INFO] {len(context.entregadores_proximos)} entregadores próximos identificados.")

@then("o sistema deve alocar o entregador para a entrega")
def step_then_alocar_entregador(context):
    if context.entregador_encontrado:
        print(f"[SUCESSO] Entregador alocado para a entrega após {context.tempo_busca} minutos.")
    else:
        print("[ERRO] Nenhum entregador encontrado.")

@then("o sistema deve alertar entregadores próximos com pedidos quase finalizados")
def step_then_alertar_entregadores(context):
    try:
        if not context.entregadores_proximos:
            print("[LOG] Nenhum entregador próximo disponível para alerta.")
            return

        # Simulação do envio de alertas para os entregadores próximos
        context.entregadores_alertados = []
        for entregador in context.entregadores_proximos:
            # Aqui poderia ser uma chamada para um serviço de notificação
            print(f"[ALERTA] Notificando entregador {entregador} sobre a nova entrega.")
            context.entregadores_alertados.append(entregador)
        
        print(f"[SUCESSO] {len(context.entregadores_alertados)} entregadores foram notificados.")

    except Exception as e:
        context.erro = str(e)
        print(f"[ERRO] Falha ao enviar alertas: {context.erro}")

@then("o sistema não deve enviar alertas")
def step_then_nao_enviar_alertas(context):
    if context.erro == "Nenhum entregador disponível dentro do tempo máximo":
        print("[LOG] Não há entregadores para alertar, portanto nenhum alerta será enviado.")
    else:
        print("[ERRO] O sistema tentou enviar alertas quando não deveria.")

@then("o sistema deve alertar todos os entregadores próximos disponíveis")
def step_then_alertar_todos_os_entregadores(context):
    if context.entregadores_proximos:
        # Alertar todos os entregadores próximos
        context.entregadores_alertados = []  # Lista para armazenar os entregadores alertados
        for entregador in context.entregadores_proximos:
            print(f"[ALERTA] Notificando entregador {entregador} sobre a nova entrega.")
            context.entregadores_alertados.append(entregador)
        
        # Verificar se todos os entregadores foram alertados
        if len(context.entregadores_alertados) == len(context.entregadores_proximos):
            print(f"[SUCESSO] {len(context.entregadores_alertados)} entregadores foram alertados com sucesso.")
        else:
            print("[ERRO] Nem todos os entregadores foram alertados.")
    else:
        print("[ERRO] Não há entregadores próximos para alertar.")