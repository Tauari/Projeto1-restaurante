from estruturas import ListaEncadeada
from modelos import Comanda, Pagamento, Consumo
from .estoque import Estoque


class Restaurante:

    def __init__(self):
        self.estoque = Estoque()
        self._comandas = ListaEncadeada()
        self._pagamentos = ListaEncadeada()
        self._consumos = ListaEncadeada()
        self._proximo_numero = 1

    def abrir_comanda(self, cliente, data_abertura):
        comanda = Comanda(self._proximo_numero, cliente, data_abertura)
        self._comandas.inserir(comanda)
        self._proximo_numero = self._proximo_numero + 1
        return comanda

    def buscar_comanda(self, numero):
        for comanda in self._comandas:
            if comanda.numero == numero:
                return comanda
        return None

    def fechar_comanda(self, numero, forma_pagamento, data_hora):
        comanda = self.buscar_comanda(numero)

        if comanda is None:
            print(f"Comanda {numero} nao encontrada")
            return None

        if comanda.fechada:
            print(f"Comanda {numero} ja foi fechada")
            return None

        if forma_pagamento not in Pagamento.FORMAS:
            print(f"Forma de pagamento invalida: {forma_pagamento}")
            return None

        for item in comanda.itens():
            for ingrediente in item.ingredientes():
                self.estoque.dar_baixa(ingrediente.nome_produto, ingrediente.quantidade)
            consumo = Consumo(comanda.numero, comanda.cliente, item.nome, item.tipo(), item.preco, data_hora)
            self._consumos.inserir(consumo)

        pagamento = Pagamento(comanda.cliente, comanda.numero, forma_pagamento, comanda.total(), data_hora)
        self._pagamentos.inserir(pagamento)
        comanda.fechar()
        return pagamento

    def comandas(self):
        return self._comandas

    def pagamentos(self):
        return self._pagamentos

    def consumos(self):
        return self._consumos
