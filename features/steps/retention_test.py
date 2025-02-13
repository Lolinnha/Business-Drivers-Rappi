import logging
import time
from behave import given, when, then

# Configuração do logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

# Simulação de banco de dados em memória
entregadores_db = {}

@given('um entregador cadastrado no sistema')
def step_impl(context):
    context.entregador_id = "E123"
    entregadores_db[context.entregador_id] = {"pedidos": 0, "status": "ativo", "incentivos": []}
    logging.info(f"Entregador {context.entregador_id} cadastrado no sistema.")

@given('o entregador já completou {num_pedidos:d} pedidos')
def step_impl(context, num_pedidos):
    entregadores_db[context.entregador_id]["pedidos"] = num_pedidos
    logging.info(f"Entregador {context.entregador_id} já completou {num_pedidos} pedidos.")

@when('o entregador realiza mais um pedido com sucesso')
def step_impl(context):
    entregadores_db[context.entregador_id]["pedidos"] += 1
    time.sleep(1)  # Simula tempo de processamento
    logging.info(f"Entregador {context.entregador_id} realizou um novo pedido. Total: {entregadores_db[context.entregador_id]['pedidos']} pedidos.")

@then('o sistema deve registrar o {num_pedidos:d}º pedido no banco de dados')
def step_impl(context, num_pedidos):
    if entregadores_db[context.entregador_id]["pedidos"] == num_pedidos:
        logging.info(f"Pedido {num_pedidos} registrado com sucesso para entregador {context.entregador_id}.")
    else:
        logging.error(f"Erro ao registrar o pedido {num_pedidos} para entregador {context.entregador_id}. Valor esperado: {num_pedidos}, encontrado: {entregadores_db[context.entregador_id]['pedidos']}.")
    assert entregadores_db[context.entregador_id]["pedidos"] == num_pedidos

@then('o sistema deve enviar um incentivo para o entregador')
def step_impl(context):
    if entregadores_db[context.entregador_id]["pedidos"] == 20:
        entregadores_db[context.entregador_id]["incentivos"].append("Bônus de Retenção")
        logging.info(f"Incentivo enviado para entregador {context.entregador_id}: Bônus de Retenção.")
    else:
        logging.warning(f"Entregador {context.entregador_id} ainda não atingiu 20 pedidos. Sem incentivo no momento.")
    assert "Bônus de Retenção" in entregadores_db[context.entregador_id]["incentivos"]

@then('o entregador deve ser notificado sobre o incentivo no app')
def step_impl(context):
    if "Bônus de Retenção" in entregadores_db[context.entregador_id]["incentivos"]:
        logging.info(f"Notificação enviada para entregador {context.entregador_id}: Bônus de Retenção recebido!")
        print(f"SUCESSO: Notificação enviada para {context.entregador_id}.")
    else:
        logging.error(f"Erro ao enviar notificação para entregador {context.entregador_id}. Nenhum incentivo encontrado.")
    assert "Bônus de Retenção" in entregadores_db[context.entregador_id]["incentivos"]
