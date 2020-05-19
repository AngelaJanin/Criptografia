from prime_generator import generate_prime
from random import randint
from sympy import mod_inverse
from utils import prime_relative

class RSA():

    def __init__(self):
        """
        Constructor de RSA, aquí se deben de generar los primos p y q
        para que puedan ser vistos por toda la clase, así como la llave
        pública y privada.
        """
        #Aquí también deben de generar su priv_key y pub_key

        # Generamos los números primos p y q
        self.p = generate_prime(100)
        self.q = generate_prime(100)
        self.n = self.p * self.q
        self.phi = self.__phi__()
        # Calculamos el número e para la llave pública
        e = self.get_prime_relative()
        # Asignamos la llave pública y privada
        self.pub_key = e
        self.priv_key = mod_inverse(e,self.phi)
        # Creamo los archivos .pem
        pub = self.write_file(self.pub_key, 'pub_key.pem')
        priv = self.write_file(self.priv_key, 'priv_key.pem')
        self.padding_scheme = False

    def __phi__(self):
        """
        Función completamente privada y auxiliar, únicamente para el uso de las
        pruebas unitarias.
        :return: el número de primos relativos con n.
        """
        return (self.p - 1) * (self.q - 1)

    def encrypt(self, message):
        """
        Encripta un mensaje recibido como parámetro y lo regresa a manera
        de lista de enteros.
        :param message: el mensaje a encriptar.
        :return: una lista de enteros con el mensaje encriptado.
        """
        cifrado = []
        for m in message:
            c = pow(ord(m), self.pub_key, self.n)
            cifrado.append(c)
        return cifrado

    def decrypt(self, criptotext):
        """
        Desencripta un criptotexto cifrado con RSA y lo regresa a manera
        de cadena, recuperando la información del mensaje original.
        :param criptotext: el mensaje recibido que se va a desencriptar.
        :return: una cadena con el mensaje original.
        """
        mensaje = ""
        for c in criptotext:
            m = pow(c, self.priv_key, self.n)
            mensaje += chr(m) 
        return mensaje 

    def get_prime_relative(self):
        while True:
            k = randint(1, self.phi)
            if prime_relative(k, self.phi):
                break
        return k   

    def write_file(self, key, name):
        pem = open(name, 'w')
        pem.write(str(self.n) + "," + str(key))
        pem.close()

        