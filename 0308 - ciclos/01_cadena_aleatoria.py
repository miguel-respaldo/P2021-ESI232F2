import random
# Investigar  las  siguientes  funciones: ord(), chr(), randint()
# para resolver  el siguiente  problema:
# 1. Generar  una cadena aleatoria  de cierta longitud.
# La longitud de la cadena es un dato de entrada.
# Ejemplo:
#  Entrada
#    Longitud de la cadena: 10
#  Salida
#    hjqoapmsje

# ord("h"): Return the integer that represents the character "h":
# chr(97): Get the character that represents the unicode 97:

## Pido los datos de entrada (longitud de la cadena)
longitud = int(input("Longitud de la cadena: "))

salida = ""

for i in range(longitud):
    letra_int = random.randint(ord("a"), ord("z"))
    salida = salida + chr(letra_int)

print(salida)
#    salida
# 1   b
# 2   br
# 3   brf
# 4   brfn
# 5   brfno