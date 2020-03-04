import math, random, string
import numpy as np
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
        self.key = key if key else self.construyeLllave()
        self.key = self.llenaMatriz(self.key, raiz, True)
        print(self.key)
        # Si el determinante es 0, entonces no tiene matriz inversa y se levanta excepción
        if np.linalg.det(self.key) == 0 :
            raise CryptographyException()


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
        for b in bloques:
            m = self.llenaMatriz(b,raiz, False)
            print(m)


    def decipher(self, ciphered):
        """
        Usando el algoritmo de decifrado, recibiendo una cadena que se asegura que fue cifrada
        previamente con el algoritmo de Hill, obtiene el texto plano correspondiente.
        :param ciphered: El criptotexto de algún mensaje posible.
        :return: El texto plano correspondiente a manera de cadena.
        """
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
            matriz = np.zeros(shape=(raiz,raiz))
            # Recorremos cada renglón y columna para llenarla de acuerdo 
            # a la letra con el número que le corresponde
            for renglon in range(raiz):
                for columna in range(raiz):
                    matriz[renglon][columna] = self.alphabet.find(key[c])
                    c += 1
        # Caso en que la matriz no es cuadrada
        else:
            matriz = np.zeros(shape=(raiz,1))
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
                            matriz[renglon][columna] = self.alphabet.find(key[c])
                    # Caso en el que el tamaño del mensaje es igual al número de renglones
                    else :
                        matriz[renglon][columna] = self.alphabet.find(key[c])
                    c += 1
        return matriz

    """
    Función auxiliar que construye una llave en caso de que no se de una en el constructor
    :return: una llave aleatoria 
    """
    def construyeLllave(self):
        return ''.join(random.choice(self.alphabet) for i in range(self.n))

h = Hill("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ", 4, "EBAY")
h.cipher("UN MENSAJE CON Ñ")

