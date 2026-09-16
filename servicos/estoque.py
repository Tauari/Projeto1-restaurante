from estruturas import ListaEncadeada, Fila


class ProdutoEmEstoque:

    def __init__(self, nome):
        self.nome = nome
        self.lotes = Fila()


class Estoque:

    def __init__(self):
        self._produtos = ListaEncadeada()

    def buscar(self, nome):
        for produto in self._produtos:
            if produto.nome == nome:
                return produto
        return None

    def adicionar_lote(self, lote):
        produto = self.buscar(lote.nome)
        if produto is None:
            produto = ProdutoEmEstoque(lote.nome)
            self._produtos.inserir(produto)
        produto.lotes.enfileirar(lote)

    def quantidade_disponivel(self, nome):
        produto = self.buscar(nome)
        if produto is None:
            return 0
        total = 0
        for lote in produto.lotes:
            total = total + lote.quantidade
        return total

    def dar_baixa(self, nome, quantidade):
        produto = self.buscar(nome)
        if produto is None:
            return 0
        retirado = 0
        while retirado < quantidade and not produto.lotes.esta_vazia():
            lote = produto.lotes.primeiro()
            retirado = retirado + lote.retirar(quantidade - retirado)
            if lote.quantidade == 0:
                produto.lotes.desenfileirar()
        return retirado

    def alterar_quantidade(self, nome, nova_quantidade):
        produto = self.buscar(nome)
        if produto is None:
            print(f"Produto {nome} nao existe no estoque")
            return False
        lote = produto.lotes.primeiro()
        if lote is None:
            print(f"Produto {nome} nao possui lotes")
            return False
        return lote.alterar_quantidade(nova_quantidade)

    def produtos(self):
        return self._produtos
