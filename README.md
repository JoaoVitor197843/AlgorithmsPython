# HeapSort Manual em Python 🛠️

Este projeto implementa do zero o algoritmo **Heap Sort**, usando uma estrutura de **Max Heap** construída manualmente em Python, sem o uso de bibliotecas externas como `heapq`.

---

## 📌 Sobre o Projeto

O objetivo principal é entender a lógica por trás da construção de uma **árvore binária heapificada** e como ela é utilizada para ordenação eficiente de listas. Toda a lógica foi escrita do zero com foco didático, clareza e boas práticas.

## 🧠 O que foi implementado

- Classe `binary_heap`:
  - Verificação de tipos válidos
  - Cálculo dos nós pais e filhos
  - Função de heapificação (`_heapify`)
  - Montagem do Max Heap (`_max_heapify`)

- Classe `heap_sort` (herda de `binary_heap`):
  - Organiza os elementos em ordem decrescente utilizando o Heap Sort
  - Executa todo o processo no `__init__`, recebendo uma lista e já retornando ordenada

## 🧪 Exemplo de uso

`from heap_sort import heap_sort`
`lista = [10, 3, 15, 7, 8, 23, 1]`
`ordenada = heap_sort(lista)`
`print(ordenada)`
`# Saída: [1, 3, 7, 8, 10, 15, 23]`

## 🚧 Limitações

Apenas números (int ou float) são aceitos na lista.

Atualmente, a ordenação é feita diretamente no __init__.

## 🔬 Testes

> Esses testes verificam tanto o funcionamento quanto a performance do algoritmo.

Para fazer testes com este algoritmo instale o pytest e pytest-benchmark:

`pip install pytest pytest-benchmark`

E então execute o teste com o comando:

`pytest`

Testes implementados:

- Teste e benchmark com 100.000 elementos
- Teste e benchmark com 200.000 elementos
- Teste e benchmark com 300.000 elementos
- Teste e benchmark com lista ordenada com 100.000 elementos
- Teste e benchmark com listas repetidas com 100.000 elementos
- Teste de verificação de lista com 1 elemento
- Teste de lista com 2 elementos
- Teste de lista com strings
- Teste com não lista

## 📁 Estrutura do Projeto

heap_sort/  
├─ src  
| └── heap_sort.py  
| └── make_binary_heap.py  
├── README.md  
├── .gitignore  
├── LICENSE
└── test/  
    └── heap_sort_test.py  

## 📖 Licença

Este projeto está licenciado sob a [licença MIT](LICENSE). Sinta-se livre para usar, modificar e distribuir.
