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
        aux = self.completaCadena(message)
        cifrado = ""
        for i in range(len(aux)):
            index_aux = self.alphabet.find(aux[i])
            index_mes = self.alphabet.find([message[i]])
            index = index_aux + index_mes % len(self.alphabet)

                  

    def decipher(self, ciphered):
        """
        Implementación del algoritmo de decifrado, según el criptosistema de vigenere.
        :param ciphered: El criptotexto a decifrar.
        :return: El texto plano correspondiente del parámetro recibido.
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
        diferencia = long_m - long_p
        if diferencia == 0:
            return self.password
        else:
            if long_m < long_p:
                return self.password[:long_m]
            else:
                n, r = divmod(long_m, long_p)
                return self.password * n + self.password[:r]



alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
message = "ES"
short = "PASS"
long = "ENDURECIDAMENTE"
semi_long = "ENDURECIMIENTO"
vig_short = Vigenere(alphabet, short)
print(vig_short.cipher(message))
"TSMWTSNFBEFLPJWUENG"