import random
from utils import CryptographyException,prime_relative

class Affine():

    def __init__(self, alphabet, A=None, B=None):
        """
        Constructor de clase que tiene como parámetro todos los atributos
        que necesita el algoritmo de cifrado afín.
        Parámetro:
            alphabet -- el alfabeto sobre quien se cifra el mensaje.
            A -- El coeficiente A que necesita el cifrado.
            B -- El coeficiente B de desplazamiento.
        """
        self.alphabet = alphabet
        # Checamos que se haya pasado un parámetro A
        auxiliar = A
        if not auxiliar:
            auxiliar = 1

        # Checamos si A y la longitud del alfabeto son primos relativos.
        if prime_relative(auxiliar,len(self.alphabet)):
            self.A = A
        else:
            raise CryptographyException()
        self.B = B

    def cipher(self, message):
        """
        Cifra el mensaje recibido como parámetro con el algoritmo de
        cifrado afín, un desplazamiento sobre el alfabeto predefinido.
        Parámetro:
            message -- el mensaje a cifrar.
        """
        cifrado = ""
        # Por cada letra que hay en el mensaje le aplicamos la fórmula (ax+b) mód n 
        # y concatenamos la letra ya cifrada para regresar el texto cifrado o criptotexto.
        for letra in message:
            entero = ((self.A * self.alphabet.find(letra)) + self.B) % len(self.alphabet)
            letra_cifrada = self.alphabet[entero]
            cifrado = cifrado + letra_cifrada
        return cifrado

    def decipher(self, criptotext):
        """
        Descifra el mensaje recuperando el texto plano siempre y cuando
        haya sido cifrado con el cifrado afín.
        Parámetro:
            criptotext -- el mensaje a descifrar.
        """
        # Encontramos el inverso del parámetro A
        inverso = self.modInverse(self.A, len(self.alphabet))
        texto_claro = ""
        # Para cada letra del criptotexto calculamos su letra correspondiente siguiendo la 
        # fórmula x = (a^-1 (y-b)) mód n 
        for criptoLetra in criptotext:
            num_letra = (inverso * (self.alphabet.find(criptoLetra) - self.B)) % len(self.alphabet)
            letra_clara = self.alphabet[num_letra]
            texto_claro = texto_claro + letra_clara
        return texto_claro 


    """
    Función auxiliar que busca el inverso multiplicativo del 
    parámetro A.
    Sacado de: https://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m/
    """
    def modInverse(self, a, m) : 
        a = a % m; 
        for x in range(1, m) : 
            if ((a * x) % m == 1) : 
                return x 
        return 1
