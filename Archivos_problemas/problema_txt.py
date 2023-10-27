#2 listas, una con nombres y otra con apellidos
nombres = ["Lionel","Cristian","Enzo","Julian","Rodrigo"]
apellidos = ["Messi","Romero","Fernandez","Alvarez","De Paul"]

#Registrar esta informacion en un txt de forma óptima
with open("Archivos_problemas_resueltos\\nombres_y_apellidos.txt","w") as arch:
    arch.writelines("Los datos son:\n\n")
    [arch.writelines(f"Nombre: {n}\nApellido: {a}\n--------------\n")for n,a in zip (nombres,apellidos)]