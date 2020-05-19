from random import randint
from random import randrange

def big_int(size=None):
    """
    Generador de números aleatorios de un tamaño fijo recibido como parámetro, si el parámetro es
    menor que 100 o None, entonces la función no le hace caso y genera uno de tamaño arbitrario,
    máximo es de 150 dígitos.
    :return: Un número del tamaño descrito.
    """
    # Checamos si el parámeto size es válido y si no lo es, elegimos un número random entre 100 y 150 
    size = size if size and size >= 100 else randint(100,150)
    # Formamos un número del tamaño de la longitud de dígitos, tomando cada dígito al azar entre 0 y 9
    return ''.join(["{}".format(randint(0, 9)) for num in range(0, size)])


def miller_rabin(n):
    """
    Implementación del test de primalidad de Miller-Rabin.
    :param n: El número a determinar su primalidad.
    :return: True si n es primo, False en otro caso.
    """
    n = int(n)
    # Caso Base
    if n == 3:
        return True
    # Si el número es par, entonces regresamos False
    if esPar(n):
        return False
    else:     
        t = 512
        s = 0
        r = n-1
        # Encontramos una s impar
        while r % 2 == 0:
            r>>=1
            s+=1
        assert(2**s * r == n-1)
        # Ejecutamos t veces el test
        for i in range(t):
            a = randint(2, n-2)
            y = pow(a,r,n)
            if (y != 1 and y != n-1):
                j = 1
                while j <= (s-1) and y != (n-1):
                    y = pow(y,2,n)  
                    if y == 1:
                        return False
                    j = j + 1
                if y != (n-1):
                    return False
        return True


def wilson(n):
    """
    Implementaión del test de primalidad de Wilson, basado en el teorema de Wilson,
    (p-1)! ≡ -1 mod p
    :param n: El número a determinar su primalidad.
    :return: True si n es primo, False en otro caso.
    """
    return factorial(n - 1) % n == n - 1

def generate_prime(size=None):
    """
    Genera un primo de al menos $size dígitos, si no se especifica,
    este tiene que asegurar que al menos tiene 100 dígitos.

    :param size: El tamaño del primo a generar.
    :return: Un número que se asegura que es primo.
    """
    primo = big_int(size)
    while not (miller_rabin(primo)):
        primo = big_int(size)
    return int(primo)

def esPar(n):
    return (n % 2) == 0

    
