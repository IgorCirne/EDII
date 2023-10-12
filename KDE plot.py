import seaborn as sb
import Tarefa2 as t2
import matplotlib.pyplot as plt

sb.kdeplot(t2.G.out_degree)
plt.show()
