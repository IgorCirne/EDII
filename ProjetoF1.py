import Classes
import Parts
import Functions
import networkx as nx
import matplotlib.pyplot as plt

# Aqui estou fazendo o código da primeira tarefa de implementar o histograma e fazer o filtro
# Declarando arrays que serão usadas
setups = []
setups_teamscore = []
setups_filtered = []
setups_teamscore_filtered = []

# Chama a função que cria todos os setups possíveis

Functions.Create_Setups(setups)

# Alocando todos teamscores de um setup em outra array para plotar o Histograma

for x in range(len(setups)):
    setups_teamscore.append(setups[x].teamscore)

# Plotando o Histograma

plt.hist(setups_teamscore)
plt.show()

#Ordenando a array de setups em ordem decrescente de acordo com o parâmetro teamscore

setups.sort(key=lambda temp: temp.teamscore, reverse=True)

#Filtrando so 50 melhores valores numa nova array

Functions.Top_50(setups, setups_filtered)

print(len(setups_filtered))




