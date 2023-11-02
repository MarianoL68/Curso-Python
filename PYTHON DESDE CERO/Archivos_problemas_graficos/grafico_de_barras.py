import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Archivos_problemas_graficos\\cofla_ingresos.csv")

#Creando el grafico
sns.barplot(x="fuente",y="ingresos",data=df)

#Obteniendo el total de ingresos
total_ingresos = df['ingresos'].sum()

#Mostrando el total
print(f'El total de ingresos es de: ${total_ingresos} USD')

#Mostrando el grafico
plt.show()