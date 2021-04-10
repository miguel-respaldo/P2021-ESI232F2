# Importamos la biblioteca de Hash
import hashlib
# El password es: perrito
db =["f807754c5523c1a630076b3035d484d59dc053bc95a4c9a81f2d550e252b7b0f"]

password = input("Escribe tu password: ")
cifrado = hashlib.sha3_256(password.encode())

#print("Passowrd: ", password)
#print("Cifado: ", cifrado.hexdigest())
#print("a: ", hashlib.sha3_256("a".encode()).hexdigest())
#print("A: ", hashlib.sha3_256("A".encode()).hexdigest())

if cifrado.hexdigest() == db[0]:
    print("Si es el password")
else:
    print("password incorrecto")

