from abc import ABC, abstractmethod


class ItemPedido(ABC):

    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    @property
    def nome(self):
        return self._nome

    @property
    def preco(self):
        return self._preco

    @abstractmethod
    def ingredientes(self):
        pass

    @abstractmethod
    def tipo(self):
        pass

    def __repr__(self):
        return f"{self._nome} - R$ {self._preco:.2f}"
