import Classes
import Parts
import networkx as nx


#Função que cria todos os setups possíveis baseados nas 6 cartas para um carro
def Create_Setups(setups = [], t = 0):
        for a in range(8):
            for b in range(8):
                for c in range(8):
                    for d in range(8):
                        for e in range(8):
                            for f in range(8):
                                temp_setup = Classes.Setup(Parts.Brakes[a], Parts.Gboxes[b], Parts.Bwings[c],
                                                       Parts.Fwings[d],
                                                       Parts.Suspensions[e], Parts.Engines[f],t)
                                t +=1
                                setups.append(temp_setup)



# Essa função recebe duas arrays: Uma com todos os setups e uma vazia, ele coloca os top 50 baseados em teamscore na array vazia
def Top_50(setups = [],filtered_setups = []):
    setups.sort(key=lambda temp: temp.teamscore, reverse=True)
    for i in range(10):
        filtered_setups.append(setups[i])


# Essa função recebe um grafo G e coloca nodes com cada parte possível
def add_nodes_from_parts(G):
    for i in range(len(Parts.Brakes)):
        G.add_node(Parts.Brakes[i].name)
    for i in range(len(Parts.Gboxes)):
        G.add_node(Parts.Gboxes[i].name)
    for i in range(len(Parts.Fwings)):
        G.add_node(Parts.Fwings[i].name)
    for i in range(len(Parts.Bwings)):
        G.add_node(Parts.Bwings[i].name)
    for i in range(len(Parts.Engines)):
        G.add_node(Parts.Engines[i].name)
    for i in range(len(Parts.Suspensions)):
        G.add_node(Parts.Suspensions[i].name)


def add_edges(G, setups_filtered = []):
    for i in range(len(Parts.Brakes)):
        for j in range(len(setups_filtered)):
            if setups_filtered[j].Brake.name == Parts.Brakes[i].name:
                G.add_edge(Parts.Brakes[i].name, setups_filtered[j].n)

    for i in range(len(Parts.Gboxes)):
        for j in range(len(setups_filtered)):
            if setups_filtered[j].Gbox.name == Parts.Gboxes[i].name:
                G.add_edge(Parts.Gboxes[i].name, setups_filtered[j].n)

    for i in range(len(Parts.Suspensions)):
        for j in range(len(setups_filtered)):
            if setups_filtered[j].Suspension.name == Parts.Suspensions[i].name:
                G.add_edge(Parts.Suspensions[i].name, setups_filtered[j].n)

    for i in range(len(Parts.Bwings)):
        for j in range(len(setups_filtered)):
            if setups_filtered[j].Bwing.name == Parts.Bwings[i].name:
                G.add_edge(Parts.Bwings[i].name, setups_filtered[j].n)

    for i in range(len(Parts.Fwings)):
        for j in range(len(setups_filtered)):
            if setups_filtered[j].Fwing.name == Parts.Fwings[i].name:
                G.add_edge(Parts.Fwings[i].name, setups_filtered[j].n)

    for i in range(len(Parts.Engines)):
        for j in range(len(setups_filtered)):
            if setups_filtered[j].Engine.name == Parts.Engines[i].name:
                G.add_edge(Parts.Engines[i].name, setups_filtered[j].n)