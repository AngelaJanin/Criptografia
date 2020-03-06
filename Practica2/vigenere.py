import math, random, string
class Vigenere():

    def __init__(self, alphabet, password=None):
        #Recomendación, ingeniárselas para no cargar siempre O(n^2) en memoria aunque esto no
        #será evaluado, con n el tamaño del alfabeto.
        """
        Constructor de clase, recibe un parámetro obligatorio correspondiente al alfabeto
        y un parámetro opcional que es la palabra clave, en caso de ser None, entonces
        generar una palabra pseudoaleatoria de al menos tamaño 4.
        :param alphabet: Alfabeto a trabajar con el cifrado.
        :param password: El password que puede ser o no dada por el usuario.
        """
        self.alphabet = alphabet
        self.password = password if password else self.construyePass()

    def cipher(self, message):
        """
        Usando el algoritmo de cifrado de vigenere, cifrar el mensaje recibido como parámetro,
        usando la tabla descrita en el PDF.
        :param message: El mensaje a cifrar.
        :return: Una cadena de texto con el mensaje cifrado.
        """
        # Checamos cómo es el mensaje recibido con respecto a la llave y formamos una nueva
        # cadena sólo con la llave pero de la longitud del mensaje para poder hacer el cifrado. 
        aux = self.completaCadena(message)
        criptotexto = ""
        # Ciframos cada letra del mensaje 
        for i in range(len(aux)):
            index_aux = self.alphabet.find(aux[i])
            index_mes = self.alphabet.find(message[i])
            index = (index_aux + index_mes) % len(self.alphabet)
            criptotexto += self.alphabet[index]
        return criptotexto

    def decipher(self, ciphered):
        """
        Implementación del algoritmo de decifrado, según el criptosistema de vigenere.
        :param ciphered: El criptotexto a decifrar.
        :return: El texto plano correspondiente del parámetro recibido.
        """
        # Checamos cómo el cifrado recibido con respecto a la llave y formamos una nueva
        # cadena sólo con la llave pero de la longitud del mensaje encriptado para poder 
        # hacer el descifrado. 
        aux = self.completaCadena(ciphered)
        texto = ""
        # Desciframos cada letra del mensaje
        for i in range(len(aux)):
            index_aux = self.alphabet.find(aux[i])
            index_ci = self.alphabet.find(ciphered[i])
            index = (index_ci - index_aux) % len(self.alphabet)
            texto += self.alphabet[index]
        return texto

    """
    Función auxiliar que construye una llave para el cifrado de Vigenere con longitud al 
    menos de 4 y máximo de 10
    """
    def construyePass(self):
        return ''.join(random.choice(self.alphabet) for i in range(4,10))

    """
    Función auxiliar que acompleta la cadena que recibe de acuerdo a la longitud del 
    password
    """
    def completaCadena(self, cadena):
        long_m = len(cadena)
        long_p = len(self.password)
        # Obtenemos la diferencia de longitud entre el mensaje y la llave
        diferencia = long_m - long_p
        # En caso de que sean iguales, se regresa la llave
        if diferencia == 0:
            return self.password
        # En caso de que sean diferentes checamos cómo es la relación
        else:
            # Si la longitud del mensaje es mayor al de la llave, cortamos
            # la llave y la regresamos
            if long_m < long_p:
                return self.password[:long_m]
                # Si la longitud de la llave es mayor, acompletamos la cadena
                # repitiendo la llave tantas veces sea necesario
            else:
                n, r = divmod(long_m, long_p)
                return self.password * n + self.password[:r]


