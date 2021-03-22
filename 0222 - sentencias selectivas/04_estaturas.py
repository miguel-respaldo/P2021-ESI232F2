# Determinar  si una persona es
# baja, media o alta  de estatura,
# considerando que menor de 1.50 metros es baja
# y mayor a 1.70 metros es alta.

estatura = float(input("Escribe tu estatura en metros: "))

if estatura <= 1.50:
    print("Tu estatura es baja")
elif estatura >= 1.70:
    print("Tu estatura es alta")
else:
    print("Tu estatura es media")
