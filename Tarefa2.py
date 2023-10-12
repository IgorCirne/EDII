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

# Criando os nodes do grafo

Functions.add_nodes_from_setups(G, setups_filtered)
Functions.add_nodes_from_parts(G)



# Criando e adicionando peso nas arestas do grafo

Functions.add_edges(G,setups_filtered)
out_degrees = dict(G.out_degree())
max_out_degree = max(out_degrees.values())
edge_widths = [1.5 * out_degrees[edge[0]] / max_out_degree for edge in G.edges()]

# Calcular posições dos nós usando circular layout

positions = nx.circular_layout(G, scale=20.0)

# Desenhando o Digrafo

colors = ["lightblue" if n[1]['part'] else "red" for n in G.nodes(data=True)]
nx.draw(G, pos=positions, width=edge_widths, with_labels=True, node_size=300, node_color=colors, font_size=12, font_color='black', font_weight='bold')
plt.show()


