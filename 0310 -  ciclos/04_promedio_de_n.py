# Escribimos el mensaje de inicio
print("Este progrma saca el promedio de los números que ingreses")

promedio = 0
numero = 1
contador = 0

# Mientras no leamos el número 0 seguimos preguntando
while numero != 0:
    numero = float(input("Ingresa un número o 0 para salir: "))
    promedio = promedio + numero
    contador = contador + 1

# Sacamos el promedio
promedio = promedio / contador
# Imprimimos el promedio
print("El promedio es: ", promedio)