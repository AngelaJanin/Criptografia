from random import randint
class Participant():


    def __init__(self, p, g, participant):
        """
        Constructor de clase
        """
        self.p = p
        self.g = g
        self.participant = participant
        self. num = randint(1,self.p)

    def seed(self):
        """
        Generador de la parte propia del intercambio de Diffie-Hellmann
        """
        secret_num = pow(self.g, self.num, self.p)
        return secret_num
    def exchange(self):
        """
        Adquiero el número de la otra persona y calculo mi propia llave.
        """
        secret_num = self.participant.seed()
        secret_num = pow(secret_num,self.num,self.p)
        return secret_num