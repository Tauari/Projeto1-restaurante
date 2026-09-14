class No:

    def __init__(self, valor):
        self._valor = valor
        self._proximo = None

    @property
    def valor(self):
        return self._valor

    @property
    def proximo(self):
        return self._proximo

    @proximo.setter
    def proximo(self, no):
        self._proximo = no

    def __repr__(self):
        return f"No({self._valor})"
