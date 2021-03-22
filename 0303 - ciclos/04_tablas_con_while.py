# Pido la tabla de multiplicar
tabla = int(input("¿Que tabla de multiplicar quieres?: "))

i = 1
# Mientras el valor de i es menor o igual a 10
while i <=10:
    # imprime la tabla de multiplicar
    print(i, "x", tabla, "=", i * tabla)
    # e incrementa el valor de i
    i = i + 1
