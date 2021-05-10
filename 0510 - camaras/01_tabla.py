import csv

archivo = open("ejemplo.csv", "r")
lector = csv.reader(archivo)
for fila in lector:
    if fila[0] == "Nombre":
        continue
    print("{:<15s}{:>5d}{:>5d}".format(fila[0], int(fila[1]), int(fila[2])))
archivo.close()
print("------------------")

buscar = "OxígEno"
buscar = buscar.lower()
archivo = open("ejemplo.csv", "r")
lector = csv.reader(archivo)
for fila in lector:
    if fila[0] == "Nombre":
        continue
    if fila[0]  == buscar:
        #print("{:<15s}{:>5d}{:>5d}".format(fila[0], int(fila[1]), int(fila[2])))
        print("Nombre: ", fila[0])
        print("Masa: ", fila[1])
        print("nose -> {:>10s}".format(fila[2]))
archivo.close()
