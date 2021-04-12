# Algoritmos Genéticos

Aplicação de algoritimo genético, utilizando a linguagem Python e o framework DEAP que permite trabalhar com computação evolucionária, incluindo o algoritmo genético. Aplicado ao problema da mochila da disciplina Inteligência Artificial ministrada pelo professor Adolfo Pinto na Universidade Tiradentes - UNIT.  

Desenvolvedores:
* Cristiano Macedo Guimarães de Oliveira
* Vinícius José Santana de Mendonça

## Framework DEAP

A documentação do framework DEAP utilizado no projeto está disponível no seguinte link:  [Documentação DEAP](https://github.com/DEAP/deap)

## O Problema da Mochila

Um problema clássico da computação é o problema da Mochila. Segundo o Wikipedia:

```
O problema da mochila (em inglês, Knapsack problem) é um problema de optimização combinatória. O nome dá-se devido ao modelo de uma situação em que é necessário preencher uma mochila com objetos de diferentes pesos e valores. O objetivo é que se preencha a mochila com o maior valor possível, não ultrapassando o peso máximo.
O problema da mochila é um dos 21 problemas NP-completos de Richard Karp, exposto em 1972. A formulação do problema é extremamente simples, porém sua solução é mais complexa. Este problema é a base do primeiro algoritmo de chave pública (chaves assimétricas).
Normalmente este problema é resolvido com programação dinâmica, obtendo então a resolução exata do problema, mas também sendo possível usar PSE (procedimento de separação e evolução). Existem também outras técnicas, como usar algoritmo guloso, meta-heurística (algoritmos genéticos) para soluções aproximadas.
```

## Instalação dos requisitos

Para a instalação dos requisitos do projeto através do promp de comando, navegue até a pasta do projeto e insira o seguinte comando:

```
pip install -r requirements.txt
```

Após a instação dos requisitos, execute o arquivo `main.py`

## Projeto

O projeto utilizou a implementação OneMax com a biblioteca DEAP. Foram criados "itens" com pesos e valores aleatórios que serão colocados na mochila. Foram criados 10 individuos, declarados como uma lista de itens. Foi definida uma população de 300 indivíduos para que tenhamos uma grande quantidade de dados a analisar afim de ter soluções mais precisas e próximas a solução ótima. Foi aplicado Cross Over e mutação de algoritmos genéticos, afim de fazer a seleção dos "melhores" dados. Com isso, é retornada uma lista de itens, com seus respectivos valores e pesos, que fazem parte de uma população. Essa lista tende a se apróximar da solução ótima, sendo seu peso inferior ou igual ao peso máximo permitido pela mochila, e seu valor o mais próximo ao "valor ótimo", tendo assim, uma otimização na mochila. 
