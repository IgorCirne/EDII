import Classes
import Parts
import networkx as nx
import matplotlib.pyplot as plt

# Aqui estou fazendo o código da primeira tarefa de implementar o histograma e fazer o filtro
# Declarando arrays que serão usadas
setups = []
setups_teamscore = []
setups_filtered = []
setups_teamscore_filtered = []

# Codigo para criar cada setup

for a in range(8):
    for b in range(8):
        for c in range(8):
            for d in range(8):
                for e in range(8):
                    for f in range(8):
                        temp_setup = Classes.Setup(Parts.Brakes[a], Parts.Gboxes[b], Parts.Bwings[c], Parts.Fwings[d],
                                                   Parts.Suspensions[e], Parts.Engines[f])
                        setups.append(temp_setup)

for x in range(len(setups)):
    setups_teamscore.append(setups[x].teamscore)

# Plotando o Histograma

plt.hist(setups_teamscore)
plt.show()

#Ordenando a array de setups em ordem decrescente de acordo com o parâmetro teamscore

setups.sort(key=lambda temp: temp.teamscore, reverse=True)

#Filtrando so 50 melhores valores numa nova array

for i in range(50):
    setups_filtered.append(setups[i])
    print(setups_filtered[i].teamscore)

print(len(setups_filtered))