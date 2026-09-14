from .no import No


class Fila:

    def __init__(self):
        self._inicio = None
        self._fim = None
        self._tamanho = 0

    def esta_vazia(self):
        return self._inicio is None

    def enfileirar(self, valor):
        novo = No(valor)
        if self.esta_vazia():
            self._inicio = novo
        else:
            self._fim.proximo = novo
        self._fim = novo
        self._tamanho += 1

    def desenfileirar(self):
        if self.esta_vazia():
            return None

        removido = self._inicio
        self._inicio = removido.proximo

        if self._inicio is None:
            self._fim = None

        self._tamanho -= 1
        return removido.valor

    def frente(self):
        if self.esta_vazia():
            return None
        return self._inicio.valor

    def __iter__(self):
        atual = self._inicio
        while atual is not None:
            yield atual.valor
            atual = atual.proximo

    def __len__(self):
        return self._tamanho

    def __repr__(self):
        return f"Fila({self._tamanho} itens)"
