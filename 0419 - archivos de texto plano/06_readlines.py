# Abro el archivo
archivo = open("prueba.txt","r")

# Leo todas las lineas y las guardo en una lista
contenido = archivo.readlines()
# imprmo el contenido en pantalla
print(contenido)

# cierro el archivo
archivo.close()
