
# Funcion qu despliega el Menu y pide un resultado
def menu():
    print("selcciona una operación")
    print("1) Calcular el área de un rectángulo")
    print("2) Calcular el área de un triángulo")
    print("3) Calcular el área de un cuadrado")
    print("4) Calcular el área de un círculo")
    print("5) Salir")
    resultado = int(input("Selecciona una opción: "))
    return resultado


opcion = 0

# Mientras la opción sea diferente de 5
while opcion != 5:
    # Despliega el menu y regresa la opcion de usuario
    opcion = menu()
