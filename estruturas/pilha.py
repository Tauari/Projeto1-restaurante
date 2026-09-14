from .no import No


class Pilha:

    def __init__(self):
        self._topo = None
        self._tamanho = 0

    def esta_vazia(self):
        return self._topo is None

    def empilhar(self, valor):
        novo = No(valor)
        novo.proximo = self._topo
        self._topo = novo
        self._tamanho += 1

    def desempilhar(self):
        if self.esta_vazia():
            return None

        removido = self._topo
        self._topo = removido.proximo
        self._tamanho -= 1
        return removido.valor

    def espiar(self):
        if self.esta_vazia():
            return None
        return self._topo.valor

    def __iter__(self):
        atual = self._topo
        while atual is not None:
            yield atual.valor
            atual = atual.proximo

    def __len__(self):
        return self._tamanho

    def __repr__(self):
        return f"Pilha({self._tamanho} itens)"
