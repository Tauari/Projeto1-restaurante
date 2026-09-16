from estruturas import ListaEncadeada
from .item_pedido import ItemPedido
from .ingrediente import Ingrediente


class Bebida(ItemPedido):

    SABORES = ("Coca Cola", "Suco", "Agua")

    def __init__(self, nome, preco):
        if nome not in Bebida.SABORES:
            raise ValueError(f"Bebida invalida: {nome}. Use uma de {Bebida.SABORES}")
        super().__init__(nome, preco)

    def ingredientes(self):
        lista = ListaEncadeada()
        lista.inserir(Ingrediente(self._nome, 1))
        return lista

    def tipo(self):
        return "Bebida"
