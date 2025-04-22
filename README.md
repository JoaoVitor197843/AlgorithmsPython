# ALGORITMOS DE ORDENAÇÃO EM PYTHON

> Algumas implementações básicas de algoritmos de ordenação clássicos, feitas totalmente em Python com foco em entendimento de lógica, desempenho e modularização.

## STATUS

<h4 align="center">
🏗️🚧 Ainda em Desenvolvimento 🚧🏗️
</h4>

ÍNDICE
======
* [O que são algoritmos de ordenação?](#o-que-são-algoritmos-de-ordenação)
* [O que é a notação big O?](#o-que-é-a-notação-big-o)
* [Algoritmos implementados](#algoritmos-implementados)
  * [Heap Sort](#heap-sort)
  * [Quick Sort Híbrido](#quick-sort-híbrido-quickion)
* [Contatos](#-contatos)
* [Licença](#licença)
* [Autores](#-autores)
## O QUE SÃO ALGORITMOS DE ORDENAÇÃO?

Algoritmos de ordenação são métodos utilizados para reorganizar elementos de uma lista ou array em uma determinada ordem (normalmente em ordem crescente como utilizado nestes códigos, ou decrescentes) Eles são fundamentais em ciência da computação e aparecem em diversas áreas como bancos de dados, algoritmos de busca, compressão de dados e inteligência artificial.

## O QUE É A NOTAÇÃO BIG O?

A notação Big O serve para descrever o comportamento de um algoritmo em relação ao seu tempo de execução ou uso de memória, conforme o tamanho da entrada cresce. Ela ajuda a prever a eficiência de um algoritmo. Aqui estão alguns exemplos da notação Big O:

- O(n): tempo linear
- O(n log n): tempo quase linear (ótimo para ordenação)
- O(n²): tempo quadrático (ruim para listas grandes)

Os atuais algoritmos vistos trabalham em O(n log n), porém o insertion sort visto em nosso quick sort híbrido utiliza a notação (n²) em seu pior caso, assim como o quick sort padrão utiliza uma notação O(n²) em seu pior caso.
Obs: a notação big O não é calculada em tempo, e sim em quantidades de execução, a notação Big O é descrita levando em conta o infinito

## ALGORITMOS IMPLEMENTADOS

### 📦 Heap Sort

Um algoritmo de ordenação baseado em uma estrutura de heap binário (árvore), utilizando o conceito de "max-heap" atualmente. Ideal para manter estabilidade de desempenho, com tempo garantido de O(n log n) mesmo nos piores casos.  
Implementado de forma modular, com uso de herança e separação entre construção da heap e fase de ordenação.

### ⚡ Quick Sort Híbrido (Quickion)

O quick sort é um algoritmo de ordenação baseado normalmente em recursão ou em criação de pilhas manuais, ele é o algoritmo de ordenação mais rápido em comparação com os outros algoritmos padrões, porém com seu pior caso sendo O(n²).
Por conta disso fiz uma implementação híbrida retirando o melhor de dois mundos, a notação de quick sort, a velocidade de insertion sort para as sublistas, e o pivô central para melhorar o desempenho geral em listas pre-ordenadas, aqui estão alguns exemplos gerais:
- A velocidade média do Quick Sort
- O desempenho ótimo do Insertion Sort para sublistas pequenas
- O uso de pivô central adaptado, que melhora o balanceamento em listas já ordenadas

Como resultado, a versão híbrida entrega ganhos reais mesmo em listas com mais de 1 milhão de elementos, evitando os colapsos típicos do Quick Sort em casos degenerados.

## 🤳 CONTATOS

Caso deseje entrar em contato comigo, fique a vontade para utilizar qualquer um dos meios de contato a seguir:

- GitHub: [JoaoVitor197843](https://github.com/JoaoVitor197843)

- Discord: [.ghost_pro](https://discord.com/)

- Email: [João_Vitor](mailto:jv2093809@gmail.com?subject=Algoritmos%20de%20Ordenação&body=Olá!%20Gostaria%20de%20falar%20sobre%20seu%20projeto...)

## 👨‍💻 AUTORES

[<img loading="lazy" src="https://avatars.githubusercontent.com/u/118195418?v=4" width=115><br><sub>João Vitor</sub>](https://github.com/JoaoVitor197843)

## 📄 LICENÇA

Este projeto está sob a licença MIT. Consulte o arquivo [LICENÇA MIT](LICENSE) para mais detalhes.
