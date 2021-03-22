# Obtener el mayor de tres números.
#
#  1. pedir los tres números
#  2. Comparar 2 primero y luego otros 2
#  3. Al final digo cual es el mayor

num1 = int(input("Escribe el primer número: "))
num2 = int(input("Escribe el segundo número: "))
num3 = int(input("Escribe el tercer número: "))

if num1 > num2:
    if num1 > num3:
        print("El mayor es:", num1)
    else:
        print("El mayor es:", num3)
else:
    if num2 > num3:
        print("El mayor es", num2)
    else:
        print("El mayor es", num3)
