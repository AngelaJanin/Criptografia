from EllipticCurves import scalar_multiplication, Curve
from random import randint
from sympy import mod_inverse
import math

class ECIES():

    def __init__(self, curve, A, B, N, s, p):
        self.curve = curve
        self.A = A
        self.B = B
        self.N = N
        self.s = s
        self.q = p 

    def encrypt(self, message):
    	enc = []
    	k = randint(1, (self.N-1))
    	# Calculamos los valores de kA,kB junto con el punto de compresión
    	kA = scalar_multiplication(self.A, k, self.curve)
    	kB = scalar_multiplication(self.B, k, self.curve)
    	# Si no se cumple la condición de kA[0] mod q != 0 mod q
    	# y kB[0] != 0 mod q volvemos a intentar con otra k
    	while (kA[0] == (0 % self.q)) or (kB[0] == (0 % self.q)) :
    		k = randint(1, (self.N-1))
    		kA = scalar_multiplication(self.A, k, self.curve)
    		kB = scalar_multiplication(self.B, k, self.curve)
    	# Calculamos el punto de compresión
    	p_comp = (kA[0], kA[1] % 2)
    	# Ciframos cada letra del mensaje
    	for m in message:
    		r = int((ord(m) * kB[0]) % self.q)
    		enc.append((p_comp, r))
    	return enc

    def decrypt(self, criptotext):
    	mssg = ""
    	for c in criptotext:
        	v1,y = c
        	x, k = v1[0], v1[1]
        	# Evaluamos en la curva el punto x
        	z = (pow(x,3) + (self.curve.A * x) + self.curve.B) % self.curve.p
        	# Sacamos la raíz y checamos si es perfecta
        	root = math.sqrt(z)
        	p_root = int(root)
        	# Sumamos el primo hasta que obtengamos una raíz perfecta
        	while root != p_root:
        		z = self.q + z
        		root = math.sqrt(z)
        		p_root = int(root)
        	# Checamos k para saber qué raíz tomar 
        	if k == 1:
        		proot = -1 * p_root
        	p = (x,p_root)
        	# Obtenemos el descifrado de la letra
        	p = scalar_multiplication(p, self.s, self.curve)
        	n = (y * mod_inverse(p[0],self.q)) % self.q
        	mssg += chr(n+62)
    	return mssg

