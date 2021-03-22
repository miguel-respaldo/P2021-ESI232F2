import random
##importa random
i = int(input("Adivina el numero que se generó: "))
##Aqui el usuario escribe el numero que el cree que se haya generado
x = random.randint(1, 10)
##aqui se genera un numero aleatorio del 1 al 10
for i in range(10):
 if x != i:
    x = int(input("No, ese no es el numero, intenta de nuevo: "))
##revisa si el numero generado es igual al que ingresaste
 else:
##si no es igual tendras que ingresar otro numero hasta que le atines
  print("Felicidades Adivinaste el numero generado")
##imprime "Felicidades Adivinaste el numero generado" cuando adivines el numero.

