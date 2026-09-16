from datetime import datetime, timedelta

from servicos import Restaurante, Relatorios
from servicos import dados
from modelos import Bebida


def linha(titulo):
    print()
    print("=" * 70)
    print(titulo)
    print("=" * 70)


restaurante = Restaurante()

linha("1. GERANDO DADOS ALEATORIOS COM FAKER")
dados.gerar_dados(restaurante, quantidade_comandas=6)
print(f"{len(restaurante.comandas())} comandas geradas e fechadas")
print(f"{len(restaurante.estoque.produtos())} produtos diferentes no estoque")

relatorios = Relatorios(restaurante)

linha("2. ESTOQUE ANTES DO ATENDIMENTO")
relatorios.estoque()

linha("3. SIMULANDO UM ATENDIMENTO COMPLETO")

agora = datetime.now()
comanda = restaurante.abrir_comanda("Orlando Saraiva", agora)
print(f"Comanda {comanda.numero} aberta para {comanda.cliente}")

prato = dados.criar_refeicao("Prato Feito", 25.00, [("Arroz", 1), ("Feijao", 1), ("Carne", 1)])
frango = dados.criar_refeicao("Frango Grelhado", 28.00, [("Arroz", 1), ("Frango", 1), ("Batata", 1)])
coca = Bebida("Coca Cola", 8.00)
agua = Bebida("Agua", 5.00)

comanda.adicionar_item(prato)
comanda.adicionar_item(frango)
comanda.adicionar_item(coca)
comanda.adicionar_item(agua)

print("\nItens da comanda:")
for item in comanda.itens():
    print(f"  {item.tipo()}: {item}")
print(f"Total parcial: R$ {comanda.total():.2f}")

print("\nCliente desistiu do Frango Grelhado")
comanda.remover_item("Frango Grelhado")

print("\nItens da comanda:")
for item in comanda.itens():
    print(f"  {item.tipo()}: {item}")
print(f"Refeicoes: {comanda.contar_por_tipo('Refeicao')}")
print(f"Bebidas: {comanda.contar_por_tipo('Bebida')}")
print(f"Total: R$ {comanda.total():.2f}")

arroz = restaurante.estoque.buscar("Arroz")
print("\nLotes de Arroz ANTES do fechamento:")
for lote in arroz.lotes:
    print(f"  {lote}")

fechamento = agora + timedelta(minutes=45)
pagamento = restaurante.fechar_comanda(comanda.numero, "PIX", fechamento)
print(f"\nPagamento registrado: {pagamento}")

print("\nLotes de Arroz DEPOIS do fechamento:")
for lote in arroz.lotes:
    print(f"  {lote}")
print("A baixa saiu do lote mais antigo, que e o primeiro da fila")

print("\nTentando adicionar item em comanda fechada:")
comanda.adicionar_item(coca)

linha("4. EDITANDO A QUANTIDADE EM ESTOQUE")
lote_mais_antigo = arroz.lotes.primeiro()
print("Lote mais antigo de Arroz:", lote_mais_antigo)
restaurante.estoque.alterar_quantidade("Arroz", 100)
print("Depois de editar: ", lote_mais_antigo)
print("Tentando colocar valor negativo:")
restaurante.estoque.alterar_quantidade("Arroz", -10)

linha("5. RELATORIO DE VENDAS")
relatorios.vendas()

linha("6. RELATORIO DE CONSUMO")
relatorios.consumo()

linha("7. SALVANDO E CARREGANDO COM PICKLE")
dados.salvar(restaurante)
restaurante_carregado = dados.carregar()
print(f"Comandas no arquivo: {len(restaurante_carregado.comandas())}")
print(f"Pagamentos no arquivo: {len(restaurante_carregado.pagamentos())}")
print(f"Consumos no arquivo: {len(restaurante_carregado.consumos())}")
print("Ultima comanda carregada:", restaurante_carregado.buscar_comanda(comanda.numero))
