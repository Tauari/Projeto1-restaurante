# Sistema de Restaurante — Comandas, Estoque e Pagamento

Projeto 1 das disciplinas **Estrutura de Dados** e **Linguagem de Programação 2**
Fatec Rio Claro — Prof. Orlando Saraiva Júnior

## Sobre

Sistema que simula o atendimento completo de um restaurante: abertura de comanda,
inclusão de refeições e bebidas, fechamento, pagamento e baixa de estoque.

Conforme o enunciado, **todas as estruturas de dados usadas para resolver o problema
foram implementadas do zero**, sem uso das estruturas built-in do Python (`list`,
`deque`, `queue`) para armazenar os dados do domínio.

## Estrutura do projeto

```
restaurante/
├── estruturas/          estruturas de dados próprias
│   ├── no.py            unidade básica: dado + ponteiro para o próximo
│   ├── lista_encadeada.py
│   ├── fila.py
│   └── pilha.py
├── modelos/             classes do domínio
├── servicos/            regras de negócio
└── main.py              simulação do atendimento
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

## Progresso

- [x] Parte 1 — Estruturas de dados (Nó, Lista Encadeada, Fila, Pilha)
- [ ] Parte 2 — Modelos do domínio (Produto, Refeição, Bebida)
- [ ] Parte 3 — Estoque com baixa FIFO
- [ ] Parte 4 — Comandas
- [ ] Parte 5 — Pagamento polimórfico e fechamento
- [ ] Parte 6 — Geração de dados (Faker) e persistência (pickle)
- [ ] Parte 7 — Relatórios de vendas e consumo
