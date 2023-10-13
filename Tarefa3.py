import networkx as nx
import matplotlib.pyplot as plt
import Classes
import Parts

G = nx.DiGraph()

nodes_A = ['Speed', 'Cornering', 'Power Unit', 'Reliability', 'Pit Stop', 'Overtaking', 'Defending', 'Race Start',
           'Tyre Management']

#Definindo os nodes do grafo

G.add_nodes_from(nodes_A, bipartite=0)
G.add_nodes_from(Parts.Bottles, bipartite=1)

# Definindo cores e labels do grafo

node_colors = ['lightblue' if node in nodes_A else 'lightyellow' for node in G.nodes()]
node_labels_A = {node: node for node in nodes_A}
node_labels_B = {node: node.name for node in G.nodes() if isinstance(node, Classes.Bottle)}
node_labels = {**node_labels_A, **node_labels_B}

#Layout do Grafo

pos = nx.bipartite_layout(G, nodes=nodes_A)

# Desenhando o Grafo e os labels do mesmo

nx.draw(G, pos, with_labels=False, node_color=node_colors, font_size=12, font_color='black')
nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=12, font_color='black')
plt.show()