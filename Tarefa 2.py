import Classes
import Parts
import Functions
import networkx as nx
import matplotlib.pyplot as plt

setups = []
setups_teamscore = []
setups_filtered = []
G = nx.DiGraph()

Functions.Create_Setups(setups)

for x in range(len(setups)):
    setups_teamscore.append(setups[x].teamscore)

Functions.Top_50(setups, setups_filtered)


Functions.add_nodes_from_parts(G)

# Criando os nodes dos setups baseados no índice deles

Functions.add_edges(G,setups_filtered)

# Calculando Centralidade de cada nó
degree_centrality = nx.degree_centrality(G)

# Calcular posições dos nós usando spring layout
positions = nx.spring_layout(G, k=0.3)

# Desenhando o Digrafo
nx.draw(G, pos=positions, with_labels=True, node_size=500, node_color='lightblue', font_size=12, font_color='black')
plt.axis('off')
plt.show()


