print("Ejemplo de listas")
arcoiris=["verde", "azul", "morado", "rojo"]
print(arcoiris) 
longitud=len(arcoiris)
print("Elementos que contiene la lista arcoiris ", longitud)
print(f"Elementos que contiene la lista arcoiris v2 {longitud}")
print("Accediendo a un elemento de la lista")
print(arcoiris[2])
print(f"Elemento en la posicion 0 es {arcoiris[0]}")
print(f"El primer color del arcoiris es: ",arcoiris[0])
print("Agregar un elemento de la lista")
print(arcoiris)
arcoiris.append("naranja")
print(arcoiris)
print("Listar los elementos de la lista ciclo for")
for aleman in arcoiris:
    print(aleman)
