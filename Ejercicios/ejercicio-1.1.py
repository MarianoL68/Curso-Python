#Promedio de duración
min = 2.5
max = 7
promedio = 4
actual = 1.5

#Duración de crudos
crudo_promedio = 5
crudo_actual = 3.5

#Difererencias de duración
diferencia_con_min = 100 - actual / min * 100
diferencia_con_max = 100 - actual * 1000 // max / 10
diferencia_con_promedio = 100 - actual / promedio * 100

#Calculando el porcentaje de tiempo vacio 
tiempo_vacio_promedio = 100 - promedio * 1000 // crudo_promedio / 10
tiempo_vacio_actual = 100 - actual * 1000 // crudo_actual / 10

#Mostrando las diferencias de duración (ejercicio A)
print("................")
print("Este curso dura:")
print(f' - Un {diferencia_con_min}% menos que el más rapido')
print(f' - Un {diferencia_con_max}% menos que el más lento')
print(f' - Un {diferencia_con_promedio}% menos que el promedio')
print("................")

#Mostrando la cantidad de espacios vacios que se remueven (ejercicio B)
print("................")
print(f'Un curso promedio elimina un {tiempo_vacio_promedio}% de tiempo vacio')
print(f'Este curso eliminó el {tiempo_vacio_actual}% de tiempo vacio')
print("................")

#Mostrando diferencias si los cursos duraran 10 horas
print("................")
print(f'Ver 10 horas de este curso equivale a ver {promedio * 100 // actual / 10} horas de otros cursos')
print(f'Ver 10 horas de otros cursos equivale a ver {actual * 100 // promedio / 10} horas de este curso')
print("................")