from estruturas import ListaEncadeada
from .item_pedido import ItemPedido


class Refeicao(ItemPedido):

    def __init__(self, nome, preco):
        super().__init__(nome, preco)
        self._ingredientes = ListaEncadeada()

    def adicionar_ingrediente(self, ingrediente):
        self._ingredientes.inserir(ingrediente)

    def ingredientes(self):
        return self._ingredientes

    def tipo(self):
        return "Refeicao"
