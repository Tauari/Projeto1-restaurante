from .no import No


class ListaEncadeada:

    def __init__(self):
        self._primeiro = None
        self._ultimo = None
        self._tamanho = 0

    def esta_vazia(self):
        return self._primeiro is None

    def inserir(self, valor):
        novo = No(valor)
        if self.esta_vazia():
            self._primeiro = novo
        else:
            self._ultimo.proximo = novo
        self._ultimo = novo
        self._tamanho += 1

    def remover(self, valor):
        anterior = None
        atual = self._primeiro

        while atual is not None:
            if atual.valor == valor:
                if anterior is None:
                    self._primeiro = atual.proximo
                else:
                    anterior.proximo = atual.proximo

                if atual is self._ultimo:
                    self._ultimo = anterior

                self._tamanho -= 1
                return True

            anterior = atual
            atual = atual.proximo

        return False

    def buscar(self, condicao):
        for valor in self:
            if condicao(valor):
                return valor
        return None

    def __iter__(self):
        atual = self._primeiro
        while atual is not None:
            yield atual.valor
            atual = atual.proximo

    def __len__(self):
        return self._tamanho

    def __repr__(self):
        return f"ListaEncadeada({self._tamanho} itens)"
