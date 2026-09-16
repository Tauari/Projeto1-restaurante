class Pagamento:

    FORMAS = ("PIX", "Cartao", "Dinheiro")

    def __init__(self, cliente, numero_comanda, forma, valor, data_hora):
        self.cliente = cliente
        self.numero_comanda = numero_comanda
        self.forma = forma
        self.valor = valor
        self.data_hora = data_hora

    def __str__(self):
        momento = self.data_hora.strftime("%d/%m/%Y %H:%M")
        return f"Comanda {self.numero_comanda} | {self.cliente} | {self.forma} | R$ {self.valor:.2f} | {momento}"
