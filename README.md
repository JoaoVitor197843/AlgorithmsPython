# ALGORITMOS DE ORDENAÇÃO EM PYTHON

> Algumas implementações básicas de algoritmos de ordenação clássicos, feitas totalmente em Python com foco em entendimento de lógica, desempenho e modularização.

## STATUS

> **🏗️🚧 Ainda em Desenvolvimento 🚧🏗️**

## ÍNDICE

* [O que são algoritmos de ordenação?](#o-que-são-algoritmos-de-ordenação)

* [O que é a notação big O?](#o-que-é-a-notação-big-o)

* [Algoritmos implementados](#algoritmos-implementados)

  * [Heap Sort](#-heap-sort)

  * [Quick Sort Híbrido](#-quick-sort-híbrido-quickion)

* [Contatos](#-contatos)

* [Licença](#-licença)

* [Autores](#-autores)

## O QUE SÃO ALGORITMOS DE ORDENAÇÃO?

Algoritmos de ordenação são métodos utilizados para reorganizar elementos de uma lista ou array em uma determinada ordem (normalmente em ordem crescente como utilizado nestes códigos, ou decrescentes) Eles são fundamentais em ciência da computação e aparecem em diversas áreas como bancos de dados, algoritmos de busca, compressão de dados e inteligência artificial.

---

## O QUE É A NOTAÇÃO BIG O?

A notação Big O serve para descrever o comportamento de um algoritmo em relação ao seu tempo de execução ou uso de memória, conforme o tamanho da entrada cresce. Ela ajuda a prever a eficiência de um algoritmo. Aqui estão alguns exemplos da notação Big O:

* O(n): tempo linear
* O(n log n): tempo quase linear (ótimo para ordenação)
* O(n²): tempo quadrático (ruim para listas grandes)

Os atuais algoritmos vistos trabalham em O(n log n), porém o insertion sort visto em nosso quick sort híbrido utiliza a notação (n²) em seu pior caso, assim como o quick sort padrão utiliza uma notação O(n²) em seu pior caso.
Obs: a notação big O não é calculada em tempo, e sim em quantidades de execução, a notação Big O é descrita levando em conta o infinito

---


## ⚙️ COMO EXECUTAR O PROJETO

Certifique-se de ter o Python 3 instalado.

Instale as dependências:

pip install pytest pytest-benchmark

---

## 🧪 COMO EXECUTAR OS TESTES

Os testes são executados com pytest.

Heap Sort

cd Heap_Sort
pytest -v

Quick Sort Híbrido

cd Hybrid_Quick_Sort
pytest -v

---

## 🏗️ ESTRUTURA DO PROJETO

Algorithms/
├── heap_sort/
│   ├── src/
│   │   ├── heap_sort.py
│   │   ├── make_binary_heap.py
│   │   └── list_verification.py
│   ├── tests/
│   │   └── heap_sort_test.py
│
├── hybrid_quick_sort/
│   ├── src/
│   │   └── hybrid_quick_sort.py
│   ├── tests/
│   │   └── test_hybrid_quick_sort.py

- src/ → implementação dos algoritmos
- tests/ → testes unitários e de desempenho com pytest

---

## 🧠 ALGORITMOS IMPLEMENTADOS

### 📦 Heap Sort

Algoritmo baseado em uma estrutura de heap binário (max-heap), com desempenho garantido de O(n log n) mesmo no pior caso.

#### 🔧 Estrutura modular:

- make_binary_heap.py
  
  - Criação da heap
  - Acesso a filhos (esquerdo/direito)
  - Heapify (down)
  - Construção de max-heap

- list_verification.py
  
  - Validação de entrada
  - Tratamento de erros e tipos inválidos

- heap_sort.py
  
  - Algoritmo de ordenação
  - Extração e reorganização da heap

#### 🧪 Testes incluem:

- 100k, 200k e 300k elementos
- Listas ordenadas
- Elementos repetidos
- Casos inválidos (strings, tipos mistos)
- Listas pequenas (1 ou 2 elementos)

---

### ⚡ Quick Sort Híbrido (Quickion)

Implementação híbrida combinando:

- Quick Sort
- Insertion Sort
- Pivô central

#### 🎯 Objetivo:

Melhorar desempenho em:

- Listas grandes
- Listas já ordenadas
- Sublistas pequenas

#### 🧩 Componentes:

- Quick Sort recursivo
- Partition (escolha de pivô)
- Insertion Sort para otimização

#### 🧪 Testes incluem:

- 100k, 200k e 300k elementos
- Listas ordenadas

---

## 🚀 DIFERENCIAIS DO PROJETO

- Arquitetura modular
- Separação entre lógica, validação e estrutura
- Testes automatizados com grandes volumes de dados
- Benchmark de desempenho com pytest
- Implementação híbrida otimizada
- Foco em entendimento + aplicação prática

---

## 🤳 CONTATOS

Caso deseje entrar em contato comigo, fique a vontade para utilizar qualquer um dos meios de contato a seguir:

* GitHub: [JoaoVitor197843](https://github.com/JoaoVitor197843)

* Discord: [.ghost_pro](https://discord.com/)

* Email: [João_Vitor](mailto:jv2093809@gmail.com?subject=Algoritmos%20de%20Ordenação&body=Olá!%20Gostaria%20de%20falar%20sobre%20seu%20projeto...)

---

## 👨‍💻 AUTORES

[<img loading="lazy" src="https://avatars.githubusercontent.com/u/118195418?v=4" width=115><br><sub>João Vitor</sub>](https://github.com/JoaoVitor197843)

---

## 📄 LICENÇA

Este projeto está sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.
