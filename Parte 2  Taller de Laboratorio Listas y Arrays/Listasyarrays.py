#Valores de los examenes
resultadoexamenes = [5, 7, 8, 6, 9, 4, 10]
print("Resultados de los exámenes:", resultadoexamenes)

#Para añadir un nuevo elemento al final
#Añade un nuevo elemento al final de la lista
resultadoexamenes.append(3)
print("Nuevo elemento añadido:", resultadoexamenes)

#Para insertar un nuevo elemento en una posición específica de la lista
#Inserta un nuevo elemento en la posición 1
resultadoexamenes.insert(1, 2)
print("Nuevo elemento insertado:", resultadoexamenes)

#Para modificar un elemento del array
#Cambia el elemento posicionado 2 por un 10 
resultadoexamenes[2]= 10
print("Elemento modificado:", resultadoexamenes)

resultadoexamenes.remove(3)
print("Elemento eliminado:", resultadoexamenes)

#Usamos for para que la aplicacion haga el recorrido y con los condicionales saber si aprovaron o reprobaron
for resultadocalificacion in resultadoexamenes:
  if resultadocalificacion < 6:
    print("El estudiante ha reprobado")
  else:
    print("El estudiante ha aprovado")