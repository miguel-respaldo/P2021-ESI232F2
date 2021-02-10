# Funciones de cadena de texto

s = "Hola Mundo"
print("isdigit:", s.isdigit())
print("isalpha:", s.isalpha())
print("isupper:", s.isupper())  # Upper Case
print("islower:", s.islower())  # Lower Case

### Buscando sub candenas

s = 'Bienvenido a Python'
print("termina con thon: ", s.endswith("thon"))
print("comienza con Buen", s.startswith("Buen"))
print("Posición de ido: ", s.find("ido"))
print("Posición derecha de venida:", s.rfind("venida"))
print("Número de o:", s.count("o"))

## Elimando espacios en blanco en cadenas

s = "  Hola Mundo   "
s.lstrip()
print(s.rstrip())
print(s.strip())
