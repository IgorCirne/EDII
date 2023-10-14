import networkx as nx
import matplotlib.pyplot as plt
import Classes
import Functions
import Parts

G = nx.DiGraph()

nodes_A = ['Speed', 'Cornering', 'Power Unit', 'Reliability', 'Pit Stop', 'Overtaking', 'Defending', 'Race Start',
           'Tyre Management']

# Definindo os nodes do grafo

G.add_nodes_from(nodes_A, bipartite=0)
G.add_nodes_from(Parts.Bottles, bipartite=1)

# Adicionando as arestas do grafo

edges = []

# Functions.add_edges_bottles(edges)
Functions.add_edges_bottles(G, nodes_A, Parts.Bottles)
# G.add_edges_from(edges)

out_degrees = dict(G.out_degree())
max_out_degree = max(out_degrees.values())
node_sizes = [300 + 500 * out_degrees[node] / max_out_degree for node in G.nodes()]

# Definindo cores e labels do grafo

node_colors = ['lightblue' if node in nodes_A else 'lightyellow' for node in G.nodes()]
node_labels_A = {node: node for node in nodes_A}
node_labels_B = {node: node.name for node in G.nodes() if isinstance(node, Classes.Bottle)}
node_labels = {**node_labels_A, **node_labels_B}

# Layout do Grafo

pos = nx.bipartite_layout(G, nodes=nodes_A, scale=20.0)

# Desenhando o Grafo e os labels do mesmo

nx.draw(G, pos, with_labels=False, node_color=node_colors, node_size=node_sizes)
nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=12, font_color='purple')
plt.show()