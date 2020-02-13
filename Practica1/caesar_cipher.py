import random 

class Caesar():

    def __init__(self, alphabet, key=None):
        """
        Constructor de clase que tiene como parámetro todos los atributos
        que necesita el algoritmo de cifrado de César.
        Parámetro:
            alphabet -- el alfabeto sobre quien se cifra el mensaje.
            key -- el tamaño del desplazamiento sobre el alfabeto, si es
                   None, se debe de escoger una llave aleatoria, válida.
        """
        self.alphabet = alphabet
        self.key = key 
        if self.key is None:
            self.key = random.randint(0,26)
        pass

    def cipher(self, message, flag=None):
        longitud = len(message)
        resultado = ""

        for i in range (longitud):
            actual = message[i]
            position = self.alphabet.find(actual) 
            if position < 0:
                resultado += message[i]
            else:
                positionEn = (position + self.key)%len(self.alphabet)
                resultado += self.alphabet[positionEn]
        return resultado        


        """
        Cifra el mensaje recibido como parámetro con el algoritmo de
        cifrado césar, un desplazamiento sobre el alfabeto predefinido.
        Parámetro:
            message -- el mensaje a cifrar.
        """

        pass

    def decipher(self, criptotext, flag=None):
        """
        Descifra el mensaje recuperando el texto plano siempre y cuando
        haya sido cifrado con el algoritmo de césar.
        Parámetro:
            cryptotext -- el mensaje a descifrar.
        """
        longitud = len(criptotext)
        resultado = ""
        for i in range (longitud):
            actual = criptotext[i]
            position = self.alphabet.find(actual) 
            if position < 0:
                resultado += criptotext[i]
            else:
                positionEn = (position - self.key)%len(self.alphabet)
                resultado += self.alphabet[positionEn]
        return resultado        
        pass
