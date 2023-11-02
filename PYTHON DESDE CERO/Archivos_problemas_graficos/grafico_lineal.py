import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Archivos_problemas_graficos\\goles.csv")

#Creando el grafico
sns.lineplot(x="fecha",y="goles",data=df)

#Crando un punto en el momento de más goles
plt.plot("01-13",9,"o")

#Mostrando el grafico
plt.show()