# Abro el archivo
archivo = open("prueba.txt","r")

# Leo una linea
contenido = archivo.readline()
# imprmo el contenido en pantalla
print("linea 1 " + contenido)

# Leo otra linea
contenido = archivo.readline()
# imprmo el contenido en pantalla
print("linea 2 " + contenido)

# cierro el archivo
archivo.close()
