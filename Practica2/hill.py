import math, random, string
from sympy import *
from sympy import Matrix
from utils import CryptographyException
class Hill():

    def __init__(self, alphabet, n, key=None):
        """
        Constructor de clase, recibiendo un alfabeto completamente necesario pero
        podría no recibir una llave de cifrado, en cuyo caso, hay que generar una,
        para el caso del tamañHo de la llave, hay que asegurarse que tiene raíz entera.
        :param alphabet: una cadena con todos los elementos del alfabeto.
        :param n: el tamaño de la llave, obligatorio siempre.
        :param key: una cadena que corresponde a la llave, en caso de ser una llave inválida
        arrojar una CryptographyException.
        """
        self.alphabet = alphabet
        self.n = n
        # Checamos si la raíz de la longitud de la llave es entera
        raiz = self.encuentraRaiz(self.n)
        if not (isinstance (raiz, int)):
            raise CryptographyException()
        # Checamos si se nos pasa una llave y sino, la generamos
        self.key = key if key else self.construyeLllave(raiz)
        self.key = self.llenaMatriz(self.key, raiz, True)
        #self.key = self.key % len(self.alphabet) 
        # Si el determinante es 0, entonces no tiene matriz inversa y se levanta excepción
        if self.key.det() == 0 :
            raise CryptographyException()
        # Si la longitud del alfabeto % determinante de la llave es 0 se levanta la excepción
        elif len(self.alphabet) % self.key.det() == 0:
            raise CryptographyException


    def cipher(self, message):
        """
        Aplica el algoritmo de cifrado con respecto al criptosistema de Hill, el cual recordando
        que todas las operaciones son mod |alphabet|.
        :param message: El mensaje a enviar que debe ser cifrado.
        :return: Un criptotexto correspondiente al mensaje, este debe de estar en representación de
        cadena, no lista.
        """
        message = message.replace(" ", "")
        raiz = self.encuentraRaiz(self.n)
        # Dividimos el mensaje en bloques de longitud de la raíz
        bloques = [message[i:i+raiz] for i in range(0,len(message), raiz)]
        criptotexto = ""
        # Recorremos cada bloque para cifrarlo de acuerdo al método de Hill
        for b in bloques:
            matriz = self.llenaMatriz(b, raiz, False)
            matriz = self.key * matriz
            matriz = matriz % len(self.alphabet)
            # Concatenamos todos los cifrados de los bloques
            for i in range(raiz):
                criptotexto += self.alphabet[matriz[i,0]]
        return criptotexto

    def decipher(self, ciphered):
        """
        Usando el algoritmo de decifrado, recibiendo una cadena que se asegura que fue cifrada
        previamente con el algoritmo de Hill, obtiene el texto plano correspondiente.
        :param ciphered: El criptotexto de algún mensaje posible.
        :return: El texto plano correspondiente a manera de cadena.
        """
        raiz = self.encuentraRaiz(self.n)
        texto = ""
        det = self.key.det()
        inv_mul = self.modInverse(det, len(self.alphabet))
        adj = self.key.adjugate()
        # Dividimos el mensaje en bloques de longitud de la raíz
        bloques = [ciphered[i:i+raiz] for i in range(0,len(ciphered), raiz)]
        # Recorremos cada bloque para descifrarlo y crear su matriz correspondiente
        for b in bloques:
            matriz = self.llenaMatriz(b,raiz, False)
            inversa = inv_mul * adj
            inversa = inversa * matriz
            inversa = inversa % len(self.alphabet)
            # Concatenamos el descifrado de todos los bloques
            for i in range(raiz):
                texto += self.alphabet[inversa[i,0]]
        return texto
            
        
    """
    Función auxiliar que regresa la raíz cuadrada
    :param n: La longitud de la llave
    :return: Regresa la raíz cuadrada si es perfecta en entero, en otro caso en float
    """
    def encuentraRaiz(self,n):
        raiz = math.sqrt(n)
        if (raiz*raiz) == n:
            return int(raiz)
        else:
            return raiz

    """
    Función auxiliar que regresa la matriz creada a partir de una llave 
    :param key: La llave para generar la matriz
    :param raiz: La raiz de la longitud de la llave
    :param cuadrada: Bandera que indica si una matriz es cuadrada o no
    :return: la matriz generada a partir de la llave
    """
    def llenaMatriz(self, key, raiz, cuadrada):
        c = 0
        # Caso en que la matriz sea cuadrada
        if cuadrada:
            matriz = zeros(raiz,raiz)
            # Recorremos cada renglón y columna para llenarla de acuerdo 
            # a la letra con el número que le corresponde
            for renglon in range(raiz):
                for columna in range(raiz):
                    matriz[renglon, columna] = self.alphabet.find(key[c])
                    c += 1
        # Caso en que la matriz no es cuadrada
        else:
            matriz = zeros(raiz,1)
            # Checamos si hay espacios vacíos en el mensaje para la matriz
            diferencia = raiz - len(key)
            # Recorremos cada renglón y columna para llenarla de acuerdo
            # a la letra con el número que le corresponde
            for renglon in range(raiz):
                for columna in range(1):
                    # Checamos si ya llegamos al renglón vacío y si sí nos 
                    # salimos porque inicializamos la matriz con ceros
                    if diferencia != 0:
                        if raiz - renglon  == diferencia: 
                            break
                        # Caso en el que hay diferencia pero aún no llegamos a un renglón vacío
                        else: 
                            matriz[renglon, columna] = self.alphabet.find(key[c])
                    # Caso en el que el tamaño del mensaje es igual al número de renglones
                    else :
                        matriz[renglon, columna] = self.alphabet.find(key[c])
                    c += 1
        return matriz

    """
    Función auxiliar que construye una llave en caso de que no se de una en el constructor
    :return: una llave aleatoria 
    """
    def construyeLllave(self, raiz):
        llave = ""
        valida = 0
        while valida != 1 :
            llave = ''.join(random.choice(self.alphabet) for i in range(self.n))
            m_llave = self.llenaMatriz(llave, raiz, True)
            det = m_llave.det()
            # Si el determinante es 0, entonces no tiene matriz inversa y se levanta excepción
            if det != 0 and len(self.alphabet) % det != 0:
                valida = 1
        return llave
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


