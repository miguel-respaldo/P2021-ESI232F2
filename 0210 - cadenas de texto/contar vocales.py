#Ejercicio1.
# Contador de letras.  Contar las vocales  de una cadena de texto.
# No considerar  vocales  con acento.
# Ejemplo:
# Entrada: Programacion
# Salida: 2 a
#         0 e
#         1 i
#         2 o
#         0 u
palabra = input("Ingresa una palabra: ")
print(palabra.count("a"),"a")
print(palabra.count("e"),"e")
print(palabra.count("i"),"i")
print(palabra.count("o"),"o")
print(palabra.count("u"),"u")