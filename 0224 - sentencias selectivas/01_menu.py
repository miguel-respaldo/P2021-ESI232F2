# Realizar  4 operaciones  aritméticas:
# suma, resta, multiplicación  y división,
# con dos números enteros. Elegir una de
# las opciones y realizar  el calculo correspondiente.

# Pedimos los datos
num1 = float(input("Escribe un número: "))
num2 = float(input("Escribe otro número: "))

# Mostramos el menu

print("1. Suma")
print("2. Resta")
print("3. Multiplicaicón")
print("4. División")
print("")
op = int(input("Opción: "))

if op == 1:
    print("La suma es:", num1 + num2)
elif op == 2:
    resultado = num1 - num2
    print("La resta es:", resultado)
elif op == 3:
    print("La multiplicación es:", num1 * num2)
elif op == 4:
    if num2 == 0:
        print("No se puede dividir entre 0")
    else:
        resultado = num1 / num2
        print("La resta es:", resultado)
else:
    print("Opción invalida.")