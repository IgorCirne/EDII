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
options = {'node_color': 'red',
           'node_size': 200,
           'width': 3,
          }

for i in range(len(Parts.Brakes)):
    G.add_node(Parts.Brakes[i].name)

nx.draw(G, with_labels=True,**options)
plt.show()


