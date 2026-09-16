from estruturas import ListaEncadeada


class Ingrediente:

    def __init__(self, nome_produto, quantidade):
        self.nome_produto = nome_produto
        self.quantidade = quantidade

    def __str__(self):
        return f"{self.quantidade}x {self.nome_produto}"


class Item:

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def ingredientes(self):
        return ListaEncadeada()

    def tipo(self):
        return "Item"

    def __str__(self):
        return f"{self.nome} (R$ {self.preco:.2f})"


class Refeicao(Item):

    def __init__(self, nome, preco, ingredientes):
        super().__init__(nome, preco)
        self._ingredientes = ingredientes

    def ingredientes(self):
        return self._ingredientes

    def tipo(self):
        return "Refeicao"


class Bebida(Item):

    BEBIDAS_PERMITIDAS = ("Coca Cola", "Suco", "Agua")

    def __init__(self, nome, preco):
        super().__init__(nome, preco)

    def ingredientes(self):
        lista = ListaEncadeada()
        lista.inserir(Ingrediente(self.nome, 1))
        return lista

    def tipo(self):
        return "Bebida"
