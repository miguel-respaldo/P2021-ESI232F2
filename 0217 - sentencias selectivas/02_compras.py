#Comprar  4 productos(tele, compu, refri, cel)
# tele si 10 % < 5000 < 20 %
# compu si 10 % < 15000 < 20 %
# refri si 10 % < 10000 < 20 %
# cel si 10 % < 8000 < 20 %

print("1. Tele")
print("2. Compu")
print("3. Regri")
print("4. Cel")
producto = int(input("¿Que deseas comprar?"))
precio = int(input("¿Cuanto cuesta?"))

if producto == 1:
    if precio > 5000:
        print("Tienes un descuento de 20%")
        precio_final = precio * 0.8
    else:
        print("Tienes un descuento de 10%")
        precio_final = precio * 0.9
    print("El precio final es", precio_final)
elif producto == 2:
    if precio > 15000:
        print("Tienes un descuento de 20%")
        precio_final = precio * 0.8
    else:
        print("Tienes un descuento de 10%")
        precio_final = precio * 0.9
    print("El precio final es", precio_final)
elif producto == 3:
    if precio > 10000:
        print("Tienes un descuento de 20%")
        precio_final = precio * 0.8
    else:
        print("Tienes un descuento de 10%")
        precio_final = precio * 0.9
    print("El precio final es", precio_final)
elif producto == 4:
    if precio > 8000:
        print("Tienes un descuento de 20%")
        precio_final = precio * 0.8
    else:
        print("Tienes un descuento de 10%")
        precio_final = precio * 0.9
    print("El precio final es", precio_final)
else:
    print("El producto no existe")

