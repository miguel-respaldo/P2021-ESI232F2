# leemos la cantidad a leer
cantidad = int(input("¿Cuantos números quieres promediar?: "))

# Inicializamos la variable promedio con 0.0 para que sea float
promedio = 0.0

# Leemos todos los numeros
i=1
while i <= cantidad:
    num = float(input("Introduce el número: "))
    print(i, ": promedio = ", promedio, " num = ", num)
    promedio = promedio + num
    i = i + 1

# Hacemos la division
promedio = promedio / cantidad
# imprimimos en pantalla el promedio
print("El promedio fue:", promedio)
