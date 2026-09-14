from estruturas import ListaEncadeada, Fila, Pilha

lista = ListaEncadeada()
lista.inserir("Coca Cola")
lista.inserir("Suco")
lista.inserir("Água")
lista.inserir("Maçã")

for bebida in lista:
    print(bebida)

print(len(lista))
lista.remover("Água")
print(list(lista))
print(len(lista))