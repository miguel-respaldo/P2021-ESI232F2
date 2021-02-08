# Inicializar una cadena

s1 = str() # Esta es una cadena vacia
s2 = ""    # Tambien es una cadena vacia

s3 = str("un texto")  # inicializamos con un texto
s4 = "un texto"

print(s3)  # imprime "un texto" sin las comillas
print(s4)  # imprime "un texto" sin las comillas

print(s3[0]) # imprime "u"

# "un texto"
#  01234567

print(s3[5]) # imprime "x"
print(s3[7]) # imprime "o"

print("---",s3[2],"---")  # tambien los espacios en blanco cuentan
