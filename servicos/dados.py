import os
import pickle
import random
from datetime import timedelta

from faker import Faker

from estruturas import ListaEncadeada
from modelos import Produto, Ingrediente, Refeicao, Bebida

ARQUIVO = os.path.join("dados", "restaurante.pkl")

INGREDIENTES = ["Arroz", "Feijao", "Carne", "Frango", "Batata", "Alface", "Tomate", "Macarrao", "Queijo"]

CARDAPIO = [
    ("Prato Feito", 25.00, [("Arroz", 1), ("Feijao", 1), ("Carne", 1)]),
    ("Frango Grelhado", 28.00, [("Arroz", 1), ("Frango", 1), ("Batata", 1)]),
    ("Macarronada", 22.00, [("Macarrao", 1), ("Queijo", 1), ("Tomate", 1)]),
    ("Salada Completa", 18.00, [("Alface", 1), ("Tomate", 1), ("Queijo", 1)]),
]

BEBIDAS = [
    ("Coca Cola", 8.00),
    ("Suco", 7.00),
    ("Agua", 5.00),
]


def criar_refeicao(nome, preco, ingredientes):
    lista = ListaEncadeada()
    for nome_produto, quantidade in ingredientes:
        lista.inserir(Ingrediente(nome_produto, quantidade))
    return Refeicao(nome, preco, lista)


def sortear_refeicao():
    nome, preco, ingredientes = random.choice(CARDAPIO)
    return criar_refeicao(nome, preco, ingredientes)


def sortear_bebida():
    nome, preco = random.choice(BEBIDAS)
    return Bebida(nome, preco)


def gerar_estoque(restaurante, fake):
    nomes_bebidas = []
    for nome, preco in BEBIDAS:
        nomes_bebidas.append(nome)

    for nome in INGREDIENTES + nomes_bebidas:
        for numero_lote in range(2):
            dias_atras = 30 - (numero_lote * 20)
            data_compra = fake.date_this_month(before_today=True, after_today=False)
            data_compra = data_compra - timedelta(days=dias_atras)
            data_vencimento = data_compra + timedelta(days=random.randint(40, 90))
            preco_compra = round(random.uniform(2.0, 9.0), 2)
            preco_venda = round(preco_compra * 2.5, 2)
            quantidade = random.randint(15, 30)
            lote = Produto(nome, preco_compra, preco_venda, data_compra, data_vencimento, quantidade)
            restaurante.estoque.adicionar_lote(lote)


def gerar_comandas(restaurante, fake, quantidade_comandas):
    for numero in range(quantidade_comandas):
        cliente = fake.name()
        abertura = fake.date_time_between(start_date="-7d", end_date="now")
        comanda = restaurante.abrir_comanda(cliente, abertura)

        for pedido in range(random.randint(1, 3)):
            comanda.adicionar_item(sortear_refeicao())

        for pedido in range(random.randint(1, 3)):
            comanda.adicionar_item(sortear_bebida())

        fechamento = abertura + timedelta(minutes=random.randint(30, 90))
        forma = random.choice(["PIX", "Cartao", "Dinheiro"])
        restaurante.fechar_comanda(comanda.numero, forma, fechamento)


def gerar_dados(restaurante, quantidade_comandas=6):
    fake = Faker("pt_BR")
    gerar_estoque(restaurante, fake)
    gerar_comandas(restaurante, fake, quantidade_comandas)
    return fake


def salvar(restaurante, caminho=ARQUIVO):
    pasta = os.path.dirname(caminho)
    if pasta != "" and not os.path.exists(pasta):
        os.makedirs(pasta)
    arquivo = open(caminho, "wb")
    pickle.dump(restaurante, arquivo)
    arquivo.close()
    print(f"Dados salvos em {caminho}")


def carregar(caminho=ARQUIVO):
    if not os.path.exists(caminho):
        print(f"Arquivo {caminho} nao encontrado")
        return None
    arquivo = open(caminho, "rb")
    restaurante = pickle.load(arquivo)
    arquivo.close()
    print(f"Dados carregados de {caminho}")
    return restaurante
