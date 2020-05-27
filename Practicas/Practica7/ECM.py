from EllipticCurves import Curve, add_points
from random import randint
from sympy import mod_inverse
from math import gcd

def lenstra(n):
    """
    Implementación del algoritmo de Lenstra para encontrar los factores
    primos de un número n de la forma n = p*q. Se asume que la proposición
    anterior es cierta, es decir, que en efecto n = p*q, regresando ambos
    factores de n.
    """
    # Gerneramos puntos aleatorios para definir la curva
    x = randint(0, n-1)
    y = randint(0, n-1)
    A = randint(0, n-1)
    # Despejamos a B de la ecuación de la curva
    B = (pow(y,2) - pow(x,3) - (A * x)) % n
    c = Curve(A,B,n)
    # Tomamos al primer punto aleatorio para empezar a sumar 
    p1 = (x,y)
    p2 = p1
    # Calculamos el valor del cual tenemos que verificar si se tiene inverso modular
    # para poder obtener la lambda en la suma de puntos
    l = calculaL(p1,p2)
    # Verificamos que tenga inverso modular n
    inv = checaInv(l,n)
    # Si hay inverso entonces seguimos sumando hasta que no haya
    while inv: 
        p2 = add_points(p1,p2,c)
        # Calculamos el valor del cual tenemos que verificar si se tiene inverso modular
        # para poder obtener la lambda en la suma de puntos
        l = calculaL(p1,p2)
        # Verificamos que tenga inverso modular n
        inv = checaInv(l,n)
    # Calculamos los posibles candidatos p y q
    p = gcd(l,n)
    q = n / p
    # Checamos que sea un factor no trivial y si es trivial
    # volvemos a ejecutar lenstra
    if (p == 1) or (p == n):
        return lenstra(n)
    else:
        return (p,q)
    
'''
Función auxiliar que determina el valor que se ocupa en lambda
del cual obtenemos el inverso modular para la suma de puntos
:param p1: punto 1 para calcular el valor
:param p2: punto 2 para calcular el valor
:return: el valor
'''
def calculaL(p1,p2):
    if p1 == p2:
            return 2 * p2[1]
    else:
        return p1[0] - p2[0]
'''
Función auxiliar que sirve para indicar si el valor de l
cuenta con un inverso modular n
:param l: el valor a checar su inverso
:param n: el módulo
:return: True si tiene inverso, False en otro caso
'''
def checaInv(l,n):
    inv = True
    try:
        mod_inverse(l,n)
    # Manejamos la excepción que lanza el mod_inverse cuando no existe
    # el inverso modular para aprovecharlo en la bandera y regresar False
    except:
        inv = False
    return inv 


