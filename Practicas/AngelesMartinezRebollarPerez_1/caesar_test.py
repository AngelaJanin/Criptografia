from caesar_cipher import Caesar

alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
c1, c2, c3 = Caesar(alphabet, 1), Caesar(alphabet, 7), Caesar(alphabet, 27)

def aux_tests(caesar, message, ciphered):
    one = caesar.cipher(message) == ciphered
    two = caesar.decipher(ciphered) == message
    return (one, two)

def test_caesar_basic():
    mess = "UNMENSAJECONÑ"
    mess1, mess7 = "VÑNFÑTBKFDPÑO", "BTSLTZHPLJVTU"
    assert c1.cipher(mess) == mess1
    assert c2.cipher(mess) == mess7
    assert c3.cipher(mess) == mess
    assert c1.decipher(mess1) == mess
    assert c2.decipher(mess7) == mess
    assert c3.decipher(mess) == mess
    caesar = Caesar(alphabet)
    crip = caesar.cipher(mess)
    assert mess == caesar.decipher(crip)

def test_caesar_spaces():
    mess = "UN MENSAJE CON Ñ Y ESPACIOS"
    mess1, mess7 = "VÑ NFÑTBKF DPÑ O Z FTQBDJPT", "BT SLTZHPL JVT U F LZWHJOVZ"
    assert c1.cipher(mess, True) == mess1
    assert c2.cipher(mess, True) == mess7
    assert c1.decipher(mess1, True) == mess
    assert c2.decipher(mess7, True) == mess

def test_remove_spaces():
    mess = "UN MENSAJE CON ESPACIOS"
    mess1, mess7 = "VÑNFÑTBKFDPÑFTQBDJPT", "BTSLTZHPLJVTLZWHJOVZ"
    assert c1.cipher(mess) == mess1
    assert c2.cipher(mess) == mess7
    assert c1.decipher(mess1) == c2.decipher(mess7)


def test_caesar_different_alphabet():
    mess = "UN MENSAJE SIN ELLA"
    c2.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXY "
    assert c2.cipher(mess) == "BUGTLU HQLG PUGLSSH"



