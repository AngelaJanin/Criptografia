from math import sqrt, ceil
from random import randint
from ECM import lenstra

def sieve(n):
    arr = [True]*n
    root = ceil(sqrt(n))
    for i in range(2, root):
        if arr[i]:
            j = i+i
            while j < n:
                arr[j] = False
                j += i
    primes = []
    for i in range(2, len(arr)):
        if(arr[i]):
            primes.append(i)
    return primes

def test_ecm():
    assert lenstra(6) == (2, 3) or lenstra(6) == (3, 2)
    assert lenstra(130063) == (113, 1151) or lenstra(1151, 113)
    criba = sieve(10000)
    p, q = criba[randint(0, len(criba))], criba[randint(0, len(criba))]
    assert lenstra(p*q) == (p, q) or lenstra(p*q) == (q, p)
