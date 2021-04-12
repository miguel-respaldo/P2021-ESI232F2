
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

while opcion != 5:
    opcion = menu()
