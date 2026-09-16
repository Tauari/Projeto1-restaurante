class Produto:

    def __init__(self, nome, preco_compra, preco_venda, data_compra, data_vencimento, quantidade):
        self.nome = nome
        self.preco_compra = preco_compra
        self.preco_venda = preco_venda
        self.data_compra = data_compra
        self.data_vencimento = data_vencimento
        self.quantidade = quantidade

    def alterar_quantidade(self, nova_quantidade):
        if nova_quantidade < 0:
            print("Quantidade nao pode ser negativa")
            return False
        self.quantidade = nova_quantidade
        return True

    def retirar(self, quantidade_desejada):
        if quantidade_desejada > self.quantidade:
            retirado = self.quantidade
        else:
            retirado = quantidade_desejada
        self.quantidade = self.quantidade - retirado
        return retirado

    def __str__(self):
        compra = self.data_compra.strftime("%d/%m/%Y")
        vencimento = self.data_vencimento.strftime("%d/%m/%Y")
        return f"{self.nome} | comprado {compra} | vence {vencimento} | {self.quantidade} un"
