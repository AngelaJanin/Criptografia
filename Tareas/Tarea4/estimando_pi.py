from random import randint
from math import gcd,sqrt
from os import urandom

"""
Función que obtiene el número de parejas que son primos relativos
con la función randint.
"""
def obtenParejasR(num):
    primos = 0
    for i in range(num):
        n1 = randint(0,2**(7*8)-1)
        n2 = randint(0,2**(7*8)-1)
        # Checamos si son primos relativos
        if(gcd(n1, n2) == 1):
            primos += 1
    return primos


# Guardamos el número de parejas que fueron primos de las 100 parejas.
print("Estimaciones con la función randint")
primos = obtenParejasR(100)
print("El número de parejas que son primos relativos son: " + str(primos))
resultado = sqrt(6 / (primos / 100))
print("El valor estimado de pi con 100 parejas es: " + str(resultado))
# Guardamos el número de parejas que fueron primos de las 1000 parejas
primos = obtenParejasR(1000)
print("El número de parejas que son primos relativos son: " + str(primos))
resultado = sqrt(6 / (primos / 1000))
print("El valor estimado de pi con 1 000 parejas es: " + str(resultado))
# Guardamos el número de parejas que fueron primos de las 1000 parejas
primos = obtenParejasR(10000)
print("El número de parejas que son primos relativos son: " + str(primos))
f1 = sqrt(6 / (primos / 10000))
print("El valor estimado de pi con 10 000 parejas es: " + str(f1))


"""
Algoritmo RC4 para generar números pseudoaleatorios
"""
def rc4(key):
    # Inicialización
    x = 0
    box = list(range(256))
    for i in range(256):
        x = (x + box[i] + key[i % len(key)]) % 256
        box[i], box[x] = box[x], box[i]
        
    # Generación de bytes pseudoaleatorios y cifrado
    x = 0
    y = 0
    out = []
    for byte in key:
        x = (x + 1) % 256
        y = (y + box[x]) % 256
        box[x], box[y] = box[y], box[x]
        out.append(box[(box[x] + box[y]) % 256])
    return bytes(out)


"""
Función que obtiene el número de parejas que son primos relativos
con el algoritmo RC4.
"""
def obtenParejasRC4(num):
    primos = 0
    for i in range(num):
        semilla1 = urandom(4)
        semilla2 = urandom(4)
        n1 = int(rc4(semilla1).hex(),16)
        n2 = int(rc4(semilla2).hex(),16)
        # Checamos si son primos relativos
        if(gcd(n1, n2) == 1):
            primos += 1
    return primos

# Guardamos el número de parejas que fueron primos de las 100 parejas.
print("Estimaciones con el algoritmo RC4")
primos = obtenParejasRC4(100)
print("El número de parejas que son primos relativos son: " + str(primos))
resultado = sqrt(6 / (primos / 100))
print("El valor estimado de pi con 100 parejas es: " + str(resultado))
# Guardamos el número de parejas que fueron primos de las 1000 parejas
primos = obtenParejasRC4(1000)
print("El número de parejas que son primos relativos son: " + str(primos))
resultado = sqrt(6 / (primos / 1000))
print("El valor estimado de pi con 1 000 parejas es: " + str(resultado))
# Guardamos el número de parejas que fueron primos de las 1000 parejas
primos = obtenParejasRC4(10000)
print("El número de parejas que son primos relativos son: " + str(primos))
f1 = sqrt(6 / (primos / 10000))
print("El valor estimado de pi con 10 000 parejas es: " + str(f1))

"""
Función que obtiene el número de parejas que son primos relativos 
con la función urandom
"""
def obtenParejasUR(num):
    primos = 0
    for i in range(num):
        n1 = int(urandom(7).hex(),16)
        n2 = int(urandom(7).hex(),16)
        # Checamos si son primos relativos
        if(gcd(n1, n2) == 1):
            primos += 1
    return primos

print("Estimaciones con la función urandom")
# Guardamos el número de parejas que fueron primos de las 100 parejas.
primos = obtenParejasUR(100)
print("El número de parejas que son primos relativos son: " + str(primos))
resultado = sqrt(6 / (primos / 100))
print("El valor estimado de pi con 100 parejas es: " + str(resultado))
# Guardamos el número de parejas que fueron primos de las 1000 parejas
primos = obtenParejasUR(1000)
print("El número de parejas que son primos relativos son: " + str(primos))
resultado = sqrt(6 / (primos / 1000))
print("El valor estimado de pi con 1 000 parejas es: " + str(resultado))
# Guardamos el número de parejas que fueron primos de las 1000 parejas
primos = obtenParejasR(10000)
print("El número de parejas que son primos relativos son: " + str(primos))
f1 = sqrt(6 / (primos / 10000))
print("El valor estimado de pi con 10 000 parejas es: " + str(f1))
