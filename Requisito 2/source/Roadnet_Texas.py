import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

G = nx.Graph()
fig, ax = plt.subplots(figsize=(9, 9))

# Criando dois conjuntos de nós
nodes_from = set()
nodes_to = set()

# Lendo o arquivo de texto referente a roadNET-CA e fazendo o grafo correspondente

with open('roadNET-TX.txt', 'r') as file:
    next(file)
    next(file)
    next(file)
    next(file)
    for line in file:
        from_node, to_node = map(int, line.strip().split('\t'))
        nodes_from.add(from_node)
        nodes_to.add(to_node)

# Adicionando os nós aos conjuntos correspondentes no grafo
G.add_nodes_from(nodes_from, bipartite=0)
G.add_nodes_from(nodes_to, bipartite=1)

# Lendo o arquivo novamente para adicionar as arestas
with open('roadNET-TX.txt', 'r') as file:
    next(file)
    next(file)
    next(file)
    next(file)
    for line in file:
        from_node, to_node = map(int, line.strip().split('\t'))
        G.add_edge(from_node, to_node)

# Calculando o coeficiente da assortatividade
assortativity = nx.degree_assortativity_coefficient(G)
print(f'Coeficiente de assortatividade: {assortativity:.4f}')

# Contando o número de nós e arestas
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
print(f'Números de nós: {num_nodes}')
print(f'Números de arestas: {num_edges}')

# Calculando o número de componentes conectados
num_connected_components = nx.number_connected_components(G)
print(f'Quantidade de componentes conectados: {num_connected_components}')

num_connected_components = list(nx.connected_components(G))
gcc = max(num_connected_components, key=len)
gcc_size = len(gcc)
print(f'Tamanho do componente gigante(GCC): {gcc_size}')

# Calculando a média do coeficiente de clustering
clustering_media = nx.average_clustering(G)
print(f'Média do coeficiente de clustering: {clustering_media:.4f}')

# Calculando o coeficiente de clustering
clustering = nx.clustering(G)
#print(f'Coeficiente de clustering: {clustering}')

# Conectividade média dos graus dos nós
avg_degree_connectivity = nx.average_degree_connectivity(G)

# Descompactando os resultados em duas listas (graus e conectividades médias)
degrees, avg_connectivities = zip(*avg_degree_connectivity.items())

# Crie um gráfico de dispersão
plt.scatter(degrees, avg_connectivities, s=60, alpha=0.5, edgecolors = 'k', label='Scatter Plot')
b, a = np.polyfit(degrees, avg_connectivities, deg=1)
xsequence = np.linspace(min(degrees), max(degrees), num=100)
ax.plot(xsequence, a + b * xsequence, color='red', lw=2.5)

# Defina rótulos dos eixos e legenda
plt.xlabel('Node Degree')
plt.ylabel('Average Neighbor Degree')
plt.legend()

plt.show()