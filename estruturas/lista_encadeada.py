from .no import No


class ListaEncadeada:

    def __init__(self):
        self._primeiro = None
        self._tamanho = 0

    def esta_vazia(self):
        return self._primeiro is None

    def inserir(self, valor):
        novo = No(valor)
        if self._primeiro is None:
            self._primeiro = novo
        else:
            atual = self._primeiro
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo
        self._tamanho = self._tamanho + 1

    def remover(self, valor):
        anterior = None
        atual = self._primeiro
        while atual is not None:
            if atual.valor is valor:
                if anterior is None:
                    self._primeiro = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                self._tamanho = self._tamanho - 1
                return True
            anterior = atual
            atual = atual.proximo
        return False

    def __iter__(self):
        atual = self._primeiro
        while atual is not None:
            yield atual.valor
            atual = atual.proximo

    def __len__(self):
        return self._tamanho
