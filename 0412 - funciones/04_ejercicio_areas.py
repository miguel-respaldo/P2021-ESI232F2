import math
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
def area_rec(base,altura):
    area = base*altura
    return area

def area_tri(base,altura):
    area = (base*altura)/2
    return area

def area_cua(lado):
    area = lado*2
    return area

def area_vir(radio):
    area = (math.pi+(radio^2))/2
    return area

opcion = 0
while opcion != 5:
    opcion = menu()
    if opcion == 1:
        base = float(int("Introduce el valor de la base del rectangulo"))
        altura = float(int("Introduce el valor de la altura del rectangulo"))
    elif opcion == 1:
        base = float(int("Introduce el valor de la base del rectangulo"))
        altura = float(int("Introduce el valor de la altura del rectangulo"))
