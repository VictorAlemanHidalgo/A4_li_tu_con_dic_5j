print("Ejemplos de tuplas")
canciones= ("Te amo", "El NoNoa", "amor eterno")
print(canciones)
y = list(canciones)
print(y)
y[1] = "La puerta negra"
canciones = tuple(y)
print(canciones)
print("Listado de elementos de la tupla canciones")
for aleman in canciones:
  print(aleman)