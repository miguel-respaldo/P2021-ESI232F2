import math
import time
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
    area = lado**2
    return area


def area_cir(radio):
    area = (math.pi*(radio**2))/2
    return area


opcion = 0
while opcion < 5:
    opcion = menu()
    if opcion == 1:
        base = float(input("Introduce el valor de la base del rectangulo: "))
        altura = float(input("Introduce el valor de la altura del rectangulo: "))
        resultado = area_rec(base,altura)
        print("El area de tu rectangulo es de: ", resultado)
        time.sleep(5)
    elif opcion == 2:
        base = float(input("Introduce el valor de la base del rectangulo: "))
        altura = float(input("Introduce el valor de la altura del rectangulo: "))
        resultado = area_tri(base,altura)
        print("El area de t triangulo es de: ",resultado)
        time.sleep(5)
    elif opcion == 3:
        lado = float(input("introduce el valor del lado del cuadrado: "))
        resultado = area_cua(lado)
        print("El area de tu cuadrado es de: ", resultado)
        time.sleep(5)
    elif opcion == 4:
        radio = float(input("Ingrese el valor del radio del circulo: "))
        resultado = area_cir(radio)
        print("El area de tu circul es de: ",resultado)
        time.sleep(5)
