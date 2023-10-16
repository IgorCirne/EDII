import Functions
import networkx as nx
import matplotlib.pyplot as plt
import Parts
import Classes

setups = []
setups_teamscore = []
setups_filtered = []
G = nx.DiGraph()
Functions.Create_Setups(setups)
parts = Parts.Brakes + Parts.Suspensions + Parts.Gboxes + Parts.Engines + Parts.Fwings + Parts.Bwings


for x in range(len(setups)):
    setups_teamscore.append(setups[x].teamscore)

Functions.Top_10(setups, setups_filtered)

# Criando os nodes do grafo

G.add_nodes_from(parts)
G.add_nodes_from(setups_filtered)

# Criando as arestas do grafo

Functions.add_edges_setups(G, parts, setups_filtered)

# Declarando o tamanho dos nodes

node_sizes = {}
for setup in setups_filtered:
    node_sizes[setup] = setup.teamscore

for part in parts:
    node_sizes[part] = 100 + 50*G.out_degree(part)

node_size_values = [node_sizes[node] for node in G.nodes()]
#edge_widths = [1.5 * out_degrees[edge[0]] / max_out_degree for edge in G.edges()]

# Calcular posições dos nós usando circular layout

positions = nx.circular_layout(G, scale=50.0)

# Ajustando os labels e cores dos nodes do grafo

node_colors = ['red' if node in setups_filtered else 'purple' for node in G.nodes()]
node_labels_A = {node: node.name for node in parts}
node_labels_B = {node: node.n for node in G.nodes() if isinstance(node, Classes.Setup)}
node_labels = {**node_labels_A, **node_labels_B}


# Desenhando o Digrafo


nx.draw(G, pos=positions, with_labels=False, node_color=node_colors, node_size=node_size_values)
nx.draw_networkx_labels(G, pos=positions, labels=node_labels, font_size=12, font_color='black')
plt.show()


