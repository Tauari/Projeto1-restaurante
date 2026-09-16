class Consumo:

    def __init__(self, numero_comanda, cliente, nome_item, tipo_item, preco, data_hora):
        self.numero_comanda = numero_comanda
        self.cliente = cliente
        self.nome_item = nome_item
        self.tipo_item = tipo_item
        self.preco = preco
        self.data_hora = data_hora

    def __str__(self):
        momento = self.data_hora.strftime("%d/%m/%Y %H:%M")
        return f"Comanda {self.numero_comanda} | {self.cliente} | {self.nome_item} ({self.tipo_item}) | R$ {self.preco:.2f} | {momento}"
