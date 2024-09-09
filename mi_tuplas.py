print("Ejemplos de tuplas")
canciones= ("Te amo", "El NoNoa", "amor eterno")
print(canciones)
y = list(canciones)
y[1] = "La puerta negra"
canciones = tuple(y)
print(canciones)