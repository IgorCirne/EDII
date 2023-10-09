import Classes
import Parts

#Função que cria todos os setups possíveis baseados nas 6 cartas para um carro
def Create_Setups(setups = []):
        for a in range(8):
            for b in range(8):
                for c in range(8):
                    for d in range(8):
                        for e in range(8):
                            for f in range(8):
                                temp_setup = Classes.Setup(Parts.Brakes[a], Parts.Gboxes[b], Parts.Bwings[c],
                                                       Parts.Fwings[d],
                                                       Parts.Suspensions[e], Parts.Engines[f])
                                setups.append(temp_setup)


# Essa função recebe duas arrays: Uma com todos os setups e uma vazia, ele coloca os top 50 baseados em teamscore na array vazia
def Top_50(setups = [],filtered_setups = []):
    setups.sort(key=lambda temp: temp.teamscore, reverse=True)
    for i in range(50):
        filtered_setups.append(setups[i])


