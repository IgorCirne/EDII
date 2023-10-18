# Projeto 1 Unidade 2
Aluno: Igor Cirne Borges de Oliveira

Matrícula: 20230001623

Este repositório contém os códigos feitos para a realização do primeiro projeto da unidade 2
Tal atividade é um projeto relacionado com grafos e visa como objetivo testar os conhecimentos adquiridos durante o mesmo para criar e gerenciar grafos usando
a biblioteca do NetworkX, os códigos nesse branch do repositório contém as funções, classess e basse de dadoss utilizada para concluir as quatro tarefas propostas para o projeto.
Link do vídeo no [Loom](https://www.loom.com/share/3c7937d7006747d7a559b57799523e8d?sid=2923b28a-6cd7-45f8-bd9c-6609f4e540fb)

## Tarefa 1

A primeira tarefa consiste na criação de todos os possíveis setups utilizando as partes dispostas a nós, tais partes podem ser encontradas no arquivo Parts.py.
Além disso, deve-se criar um histograma contendo os teamscores de todos so 262144 setups possíveis, e filtrar alguns dos melhores setups.

Para a realização da tarefa, foi criada a função Create_Setups(), a qual recebe uma array vazia e coloca todos os setups nela, com os setups criados, podemos plotar o histograma baseado nos teamscores dos objetos, e assim, filtrá-los
Para a filtragem, foram escolhidos os 10 melhores setups possíveis.
O código pode ser encontrado no arquivo ProjetoF1.py


## Tarefa 2

A segunda tarefa consiste na criação de um digrafo contendo todas as peças possíveis e os setups filtrados como nós, devem-se ter arestas apontando das peças para os setups que elas fazem parte, além disso, também deve ser feito gráfico de densidade de probabilidade de acordo com o out degree dos nós

Para a realização da tarefa, foram primeiramente crtiados os nodes num grafo G que receberam os melhores 10 setups, e as todas as peças, isso foi feito com as funções add_nodes_from_setups() e add_nodes_from_parts(), encontradas no arquivo Functions.py.
Após criar os nodes, foram adicionada as arestas usando a função add_edges_setups(), que também está no arquivo Functions.py.
Com isso, muda-se as cores dos nós para facilitar a identificação dos mesmos e desenha-se o grafo coim layout circular, para facilitar sua visualização.
em relação ao gráfico de densidade de probabilidade, o mesmo pode ser encontrado no arquivo KDE plot.py.
O código pode ser encontrado no arquivo Tarefa2.py

## Tarefa 3

A terceira tarefa consiste em fazer um digrafo bipartido para as garrafinhas do jogo F1 Clash, o grafo bipartido consiste em dois conjuntos de nós, um com as garrafinhas e outro com os possíveis atributos, os nós dos atributos devem apontar para as garrafinhas que possuem aquele atributo diferente de 0.

Para a realização da tarefa, foram criados dois conjuntos de nós, o primeiro com os atributos e o segundo com todas as garrafinhas, as arestas foram adicionadas com a função add_edges_bottles() que está presente no arquivo Functions.py.
Após isso, os tamanhos e cores de nodes foram ajustados conforme especificações da tarefa e o grafo é printado em layout circular, para facilitar a visualização do mesmo.
O código pode ser encontrado no arquivo Tarefa3.py

## Tarefa 4

A quarta tarefa é feita de forma livre, então foi decidido que ela seria feita de uma forma simples, visto que o objetivo da mesma foi sendo realizado durante as três tarefas antecedentes.
Tal tarefa consiste em encontrar o melhor setup possível, dessa vez considerando fatores como motorista e garrafinha.

Para a realização da tarefa, foram selecionadas as cards com os melhores atributos de teamscore e armazenadas em variáveis que depois seriam usadas para construir o setup.
Todas as cards com exceção da garrafinha foram escolhidas com base no teamscore das mesmas, calculado dentro da própria classe.
as garrafinhas foram escolhidas com base nos atributos "Speed" e "Cornering", visto que a tarefa diz que estes são os mais importantes.
O código então adiciona cada variável contendo as melhores peças em um setup chamado Best_Setup, esse setup consiste de uma classe de setup diferente dos outros setups usados nas tarefas 1 e 2, visto que este também recebe um motorista e uma garrafinha.
O código pode ser encontrado no arquivo Tarefa4.py

## Funções Usadas

### Create_Setups:
Esta função cria todos os setups baseados nas listas de todas as peças possíveis do veículo, criando um objeto Setup e armazenando em uma array "setups" que é usada como argumento de chamada da função

### Top_10:
Esta função usa como argumento duas listas: "setups" e "filtered_setups".
A função ordena de maneira decrescente os objetos da array "setups" com base no atributo "teamscore" das mesmas, depois disso, armazena os 10 primeiros arquivos da lista na outra lista usada como argumento.

### add_edges_setups:
Esta função leva como argumento um grafo "G", uma array "parts" e uma array "setups_filtered".
A função utiliza das arrays que contém os setups e todas as peças possíveis, para cada peça, ele checa se está em um setup, caso esteja, ele cria uma aresta da peça respectiva para o setup respectivo

### add_edges_bottles:
Esta função leva como argumento um grafo "G", e duas arrays, "nodes_A" e "bottles" respectivamente.
A função irá checar dentro da lista de garrafas os atributos que cada garrafa possui, criando arestas dos atributos para cada garrafa que possui tal atributo.
  
