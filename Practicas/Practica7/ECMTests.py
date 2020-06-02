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
	l = lenstra(6)
	assert l == (2, 3) or l == (3, 2)
	l = lenstra(130063)
	assert l == (113, 1151) or l == (1151, 113)
	criba = sieve(10000)
	p, q = criba[randint(0, len(criba))], criba[randint(0, len(criba))]
	l = lenstra(p*q)
	assert l == (p, q) or l == (q, p)
