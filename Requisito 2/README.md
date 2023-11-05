# Análise dos gráficos das networks

 Para este trabalho, foram utilizadas cinco redes para mostrar o funcionamento de conceitos sobre assortatividade, small worlds e homofilia. As redes escolhidas possuem características bastante variadas, contendo redes sociais (Twitch e Wiki-Vote), uma rede de envio de emails, uma rede de estradas e uma de co-autoria em artigos e pesquisas. Três dos gráficos gerados possuem uma linha de assortatividade subindo, enquanto dois apresentam linhas descendentes. A seguir, uma análise dos dados fornecidos pelas redes contidas no SNAP.

 
  A rede do General Relativity and Quantum Cosmology collaboration trata-se de um e-print do [arXiv](https://arxiv.org) que cobre autores e artigos ligados a relatividade geral e cosmologia quântica. O parâmetro utilizado para a conexão realizada é se um autor X fez um artigo com autor Y, dessa forma, os nós X e Y serão conectados. Como podemos ver no gráfico gerado, existe uma linha positiva de assortatividade, indicando que autores que colaboram em artigos tendem a colaborar bastante em artigos entre si.


  A rede do email-Eu-core é uma rede de envio de emails, explicitando o tráfego de emails entre usuários de uma instituição de pesquisa anônima. Usuários conectados dependem somente se eles enviaram ao menos um email para o outro. Como podemos ver no gráfico, apesar de possuir uma linha de assortatividade positiva, esta é praticamente uma reta, indicando que os membros da instituição enviavam e-mails somente para as mesmas pessoas, existindo algumas poucas que enviavam e-mails para muitas, isso pode ser um indicativo de que os funcionários costumavam enviar emails somente para pessoas dentro do próprio setor.


  A rede de estradas do Texas, com nós sendo interseções e endpoints e arestas sendo as estradas que se conectam a elas. Ao contrário dos gráficos anteriores, aqui foi observado uma dispersão bem maior porque o gráfico trata de espaço e como a rede em questão trata de um estado como um todo e não um fragmento, menos elementos aparecerão. Como podemos ver no gráfico, há uma distância grande entre os nós, mas a linha de assortatividade sobe, logo, podemos dizer que há uma estrada que conecta vários dos pontos.


  A rede do Wiki-Vote é a rede do voto público para administração do site. Os nós são os usuários e as arestas são os votos, os votos dos usuários e administradores se encontram misturados. Como é uma forma de votação, vemos que a linha de assortatividade desce, indicando possivelmente que há vários usuários inscritos para a posição de admin e muitos votos em poucas dessas pessoas, indicando assim, baixa assortatividade e a formação de uma rede de proximidades.


  A rede do Twitch Social Networks escolhida é uma rede dos usuários da twitch, como há vários datasets, o dataset escolhido foi o dos usuários brasileiros. Os nós são os próprios usuários e as arestas são as amizades mútuas entre eles. Assim como podemos ver no gráfico do wiki-vote, vemos que há muitos usuários com um grau de nó baixo e poucos com um grau alto, indicando que há muitos usuários com poucas amizades, e provavelmente esses com poucas possuem os mesmos amigos em comum. Fora esses outliers do grafo, a linha negativa de assortatividade indica que os usuários ficam restritos a pequenos ciclos de amizade.
