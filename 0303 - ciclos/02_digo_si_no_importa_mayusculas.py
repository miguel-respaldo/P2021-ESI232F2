# Pedimos al usuario una respesta
respuesta = input("¿Quieres que continue?: ")

# hacemos minusculas la respuesta
respuesta = respuesta.lower()

# mientras la resupesta sea si
while respuesta == "si":
    # pido si le sigo o no
    respuesta = input("Le sigo: ")
    # hacemos minusculas la respuesta
    respuesta = respuesta.lower()