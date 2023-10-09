import Classes
import Parts
import networkx as nx
import matplotlib.pyplot as plt

dados = Parts.Engine_teamscore + Parts.Brakes_teamscore + Parts.Suspension_teamscore + Parts.Bwing_teamscore + Parts.Fwing_teamscore + Parts.Gbox_teamscore
idade = [1,2,3,4]

plt.title('Histograma')
plt.xlabel('Teamscore')
plt.xlim(min(dados),max(dados))
plt.hist(dados, rwidth=0.9)
print(sorted(dados))
plt.show()