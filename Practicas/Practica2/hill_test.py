import pytest

from utils import CryptographyException
from hill import Hill
from random import randint

alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
cipher = None
key2 = "EBAY"

def test_init():
    size = randint(4, 9)
    if size == 4:
        with pytest.raises(CryptographyException):
            cipher = Hill(alphabet, size, "DBBB")
    elif size == 9:
        with pytest.raises(CryptographyException):
            cipher = Hill(alphabet, size, "DDDABCEFG")
    else:
        with pytest.raises(CryptographyException):
            cipher = Hill(alphabet, size)

def test_known_key():
    cipher = Hill(alphabet, 4, key2)
    criptotext = cipher.cipher("UN MENSAJE CON Ñ")
    assert True
    assert criptotext == "PBYSQPJJRWSBCA"
    assert cipher.decipher(criptotext) == "UNMENSAJECONÑA"
    criptotext = cipher.cipher("UN MENSAJE DE LONGITUD PAR")
    assert criptotext == "PBYSQPJJSUAFSBFLTMBVRR"
    assert cipher.decipher("UNMENSAJEDELONGITUDPAR")

def test_random_key():
    cipher = Hill(alphabet, 4)
    c1 = cipher.cipher("UN MENSAJE CON Ñ")
    assert cipher.decipher(c1) == "UNMENSAJECONÑA"
    c2 = cipher.cipher("UN MENSAJE DE LONGITUD PAR")
    assert cipher.decipher(c2) == "UNMENSAJEDELONGITUDPAR"
