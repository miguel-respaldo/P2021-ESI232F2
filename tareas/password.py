# Importamos la biblioteca de Hash
import hashlib
# El password es: perrito
dbu =["perro", "gato"]
dbp =["f807754c5523c1a630076b3035d484d59dc053bc95a4c9a81f2d550e252b7b0f", "f807754c5523c1a630076b3035d484d59dc053bc95a4c9a81f2d550e252b7b0f"]

usuario = input("Escribe tu usuario: ")
password = input("Escribe tu password: ")
cifrado = hashlib.sha3_256(password.encode())

#print("Passowrd: ", password)
#print("Cifado: ", cifrado.hexdigest())
#print("a: ", hashlib.sha3_256("a".encode()).hexdigest())
#print("A: ", hashlib.sha3_256("A".encode()).hexdigest())


if usuario in dbu:
    posicion = dbu.index(usuario)
    if cifrado.hexdigest() == dbp[posicion]:
        print("Login existoso")
    else:
        print("Usuario o Password Incorrectos")
else:
    print("Usuario o Password Incorrectos")

