from estruturas import ListaEncadeada


class Contagem:

    def __init__(self, nome):
        self.nome = nome
        self.quantidade = 0
        self.valor = 0


class Relatorios:

    def __init__(self, restaurante):
        self._restaurante = restaurante

    def vendas(self):
        print("RELATORIO DE VENDAS")
        print("-" * 70)

        total_geral = 0
        formas = ListaEncadeada()

        for pagamento in self._restaurante.pagamentos():
            print(pagamento)
            total_geral = total_geral + pagamento.valor
            forma = self._procurar(formas, pagamento.forma)
            forma.quantidade = forma.quantidade + 1
            forma.valor = forma.valor + pagamento.valor

        print("-" * 70)
        print(f"Comandas pagas: {len(self._restaurante.pagamentos())}")
        for forma in formas:
            print(f"{forma.nome}: {forma.quantidade} pagamentos, R$ {forma.valor:.2f}")
        print(f"TOTAL VENDIDO: R$ {total_geral:.2f}")
        print()

    def consumo(self):
        print("RELATORIO DE CONSUMO")
        print("-" * 70)

        itens = ListaEncadeada()

        for consumo in self._restaurante.consumos():
            print(consumo)
            item = self._procurar(itens, consumo.nome_item)
            item.quantidade = item.quantidade + 1
            item.valor = item.valor + consumo.preco

        print("-" * 70)
        print("Total consumido por item:")
        for item in itens:
            print(f"  {item.quantidade}x {item.nome} - R$ {item.valor:.2f}")
        print()

    def estoque(self):
        print("ESTOQUE ATUAL")
        print("-" * 70)

        for produto in self._restaurante.estoque.produtos():
            total = self._restaurante.estoque.quantidade_disponivel(produto.nome)
            print(f"{produto.nome}: {total} un em {len(produto.lotes)} lote(s)")
            for lote in produto.lotes:
                print(f"    {lote}")
        print()

    def _procurar(self, lista, nome):
        for contagem in lista:
            if contagem.nome == nome:
                return contagem
        nova = Contagem(nome)
        lista.inserir(nova)
        return nova
