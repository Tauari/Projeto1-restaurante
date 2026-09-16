from estruturas import ListaEncadeada


class Comanda:

    def __init__(self, numero, cliente, data_abertura):
        self.numero = numero
        self.cliente = cliente
        self.data_abertura = data_abertura
        self.fechada = False
        self._itens = ListaEncadeada()

    def adicionar_item(self, item):
        if self.fechada:
            print(f"Comanda {self.numero} ja esta fechada")
            return False
        self._itens.inserir(item)
        return True

    def remover_item(self, nome_item):
        if self.fechada:
            print(f"Comanda {self.numero} ja esta fechada")
            return False
        for item in self._itens:
            if item.nome == nome_item:
                return self._itens.remover(item)
        return False

    def itens(self):
        return self._itens

    def total(self):
        soma = 0
        for item in self._itens:
            soma = soma + item.preco
        return soma

    def contar_por_tipo(self, tipo):
        quantidade = 0
        for item in self._itens:
            if item.tipo() == tipo:
                quantidade = quantidade + 1
        return quantidade

    def fechar(self):
        self.fechada = True

    def __str__(self):
        abertura = self.data_abertura.strftime("%d/%m/%Y %H:%M")
        if self.fechada:
            situacao = "fechada"
        else:
            situacao = "aberta"
        return f"Comanda {self.numero} | {self.cliente} | {abertura} | {len(self._itens)} itens | R$ {self.total():.2f} | {situacao}"
