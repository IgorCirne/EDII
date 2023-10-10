import Classes
import Parts
import Functions
import networkx as nx
import matplotlib.pyplot as plt

setups = []
setups_teamscore = []
setups_filtered = []
G = nx.Graph()

Functions.Create_Setups(setups)

for x in range(len(setups)):
    setups_teamscore.append(setups[x].teamscore)

Functions.Top_50(setups, setups_filtered)


Functions.add_nodes_from_parts(G)

#Criando os nodes dos setups baseados no índice deles

for i in range(len(setups_filtered)):
    G.add_node(setups_filtered[i].n)

nx.draw(G, with_labels=True)
plt.show()


