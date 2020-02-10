import pytest
from utils import CryptographyException
from utils import prime_relative
from affine_cipher import Affine

alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
message = "UNMENSAJEENESPAÑOL"

def test_must_fail():
    with pytest.raises(CryptographyException):
        a = Affine(alphabet, 3, 10)

def test_correct_key():
    a = Affine(alphabet)
    n = len(alphabet)
    assert prime_relative(n, a.A)

def test_basic():
    a = Affine(alphabet, 1, 0)
    assert a.cipher(message) == message
    assert a.decipher(message) == message
    a.B = 1
    crip = "VÑNFÑTBKFFÑFTQBOPM"
    assert a.cipher(message) == crip
    assert a.decipher(crip) == message

def test_normal():
    a = Affine(alphabet, 4, 10)
    crip = "NIEZIFKSZZIZFTKMPA"
    assert a.cipher(message) == crip
    assert a.decipher(crip) == message
    a.A = 5
    crip = "HUPDUXKBDDUDXJKZEL"
    assert a.cipher(message) == crip
    assert a.decipher(crip) == message
    a.B = 3
    crip = "AÑJWÑQDUWWÑWQCDSXE"
    assert a.cipher(message) == crip
    assert a.decipher(crip) == message