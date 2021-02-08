# Concatenación de cadenas

s1 = "Algoritmos"
s2 = "Programación"

s = s1 + " y " + s2

print(s)

s3 = 3*s1  # Repetición 3 veces

print(s3)

# Algoritmos para imprimir la s3 con espacios

s3 = 3*(s1+" ")
print(s3)

# Imprimir solo una parte de la cadena
# De Algoritmos imprimir solo Algo
#    0123456789
print(s1[0:4]) # Subcadena del 0 y menor que 4
# Subcadnea  s[inicio:fin] donde es desde inicio < fin
#   inicio <= x < fin

print(s1[4:9]) #imprimir ritmo

## s1 es "Algoritmos"
print("algo"  in s1)  # imprime false
print("gramo" in s2)  # imprime false
print("Algo"  in s1)  # imprime false
