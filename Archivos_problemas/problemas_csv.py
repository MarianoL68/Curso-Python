#Cambiar el tipo de dato de una columna
import pandas as pd

df = pd.read_csv("Archivos_problemas\\datos.csv")

#Convertir a string los datos de una columnna
df['edad'] = df['edad'].astype(str)

# #Mostrar el tipo de dato del primer elemento de la columna edad
# print(type(df['edad'][0]))

#Remplazando el el dato nombre "Lionel" por "GOAT" 
df['nombre'].replace("Lionel","GOAT", inplace=True)
# print(df['nombre'])

#Eliminando las filas con datos faltantes
df = df.dropna()

#Eliminando las filas repetidas
df = df.drop_duplicates()


#Creando un CSV con el dataframe resultante(limpio)
df.to_csv("Archivos_problemas\\datos_limpios.csv")

