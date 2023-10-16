import Classes
import Parts


# Função que cria todos os setups possíveis baseados nas cartas para um carro
def Create_Setups(setups=[], t=0):
    for a in range(8):
        for b in range(8):
            for c in range(8):
                for d in range(8):
                    for e in range(8):
                        for f in range(8):
                            temp_setup = Classes.Setup(Parts.Brakes[a], Parts.Gboxes[b], Parts.Bwings[c],
                                                       Parts.Fwings[d],
                                                       Parts.Suspensions[e], Parts.Engines[f], t)
                            t += 1
                            setups.append(temp_setup)


# Essa função recebe duas arrays: Uma com todos os setups e uma vazia, ele coloca os top 50 baseados em teamscore na array vazia
def Top_10(setups=[], filtered_setups=[]):
    setups.sort(key=lambda temp: temp.teamscore, reverse=True)
    for i in range(10):
        filtered_setups.append(setups[i])


def add_edges_setups(G, parts, setups_filtered):
    for setup in setups_filtered:
        for part in parts:
            if (
                    part.name in [setup.Brake.name, setup.Gbox.name, setup.Suspension.name, setup.Fwing.name,
                                  setup.Bwing.name, setup.Engine.name]
            ):
                G.add_edge(part, setup)


def add_edges_bottles(G, nodes_A, bottles, node_index=0):
    if node_index >= len(nodes_A):
        return  # Caso base: Todos os nós de atributo foram verificados

    node_A = nodes_A[node_index]
    attribute_name = node_A.lower().replace(' ', '_')

    for bottle in bottles:
        attribute_value = getattr(bottle, attribute_name)
        if attribute_value != 0:
            G.add_edge(node_A, bottle)

    # Chame a função recursiva para o próximo nó de atributo
    add_edges_bottles(G, nodes_A, bottles, node_index + 1)
