# Abro el archivo
archivo = open("prueba.txt","r")

# Leo el contenido
contenido = archivo.read()

# imprmo el contenido en pantalla
print(contenido)

# cierro el archivo
archivo.close()