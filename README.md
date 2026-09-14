# Sistema de Restaurante — Comandas, Estoque e Pagamento

Projeto 1 das disciplinas **Estrutura de Dados** e **Linguagem de Programação 2**
Fatec Rio Claro — Prof. Orlando Saraiva Júnior

## Sobre

Sistema que simula o atendimento completo de um restaurante: abertura de comanda,
inclusão de refeições e bebidas, fechamento, pagamento e baixa de estoque.

## Estrutura do projeto

```
restaurante/
├── estruturas/          
│   ├── no.py            
│   ├── lista_encadeada.py
│   ├── fila.py
│   └── pilha.py
├── modelos/             
├── servicos/            
└── main.py              
```

## Decisões de projeto

| Estrutura | Onde é usada | Por quê |
| --- | --- | --- |
| Lista Encadeada | comandas, itens do pedido, pagamentos | coleções que crescem e encolhem, com remoção em qualquer posição |
| Fila (FIFO) | lotes de produtos no estoque | produtos são perecíveis: o lote mais antigo sai primeiro |
| Pilha (LIFO) | desfazer o último item lançado | a última ação é a primeira a ser revertida |

## Como executar

```bash
python -m venv venv
venv\Scripts\activate
pip install faker
python main.py
```