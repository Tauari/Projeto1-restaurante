class Ingrediente:

    def __init__(self, nome_produto, quantidade):
        self._nome_produto = nome_produto
        self._quantidade = quantidade

    @property
    def nome_produto(self):
        return self._nome_produto

    @property
    def quantidade(self):
        return self._quantidade

    def __repr__(self):
        return f"{self._quantidade}x {self._nome_produto}"
