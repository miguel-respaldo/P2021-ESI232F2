# Hacer un algoritmo que nos diga el grado
# de una alumno de acuerdo a su calificación
#  A es mayor o igual a 90
#  B es mayor o igual a 80
#  C es mayor o igual a 70
#  D es mayor o igual a 60
#  R es menor a 60

calificacion = int(input("Ingresa la calificación: "))

if calificacion >= 90:
    grado = "A"
else:
    if calificacion >= 80:
        grado ="B"
    else:
        if calificacion >= 70:
            grado = "C"
        else:
            if calificacion >= 60:
                grado = "D"
            else:
                grado = "R"

print("Tu grado de calificación es:", grado)

if calificacion >= 90:
    grado = "A"
elif calificacion >= 80:
    grado = "B"
elif calificacion >= 70:
    grado = "C"
elif calificacion >=60:
    grado = "D"
else:
    grado ="R"

print("Tu grado de calificación es:", grado)







