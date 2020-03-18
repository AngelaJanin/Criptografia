from vigenere import Vigenere

alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
message = "ESTEESUNMENSAJECONÑ"
short = "PASS"
long = "ENDURECIDAMENTE"
semi_long = "ENDURECIMIENTO"

def test_short():
    vig_short = Vigenere(alphabet, short)
    ciphered = vig_short.cipher(message)
    assert ciphered == "TSMWTSNFBEFLPJWUENG"
    assert vig_short.decipher(ciphered) == message

def test_long():
    vig_long = Vigenere(alphabet, long)
    ciphered = vig_long.cipher(message)
    assert ciphered == "IFWYVWWUOEYWNCIGBPI"
    assert vig_long.decipher(ciphered) == message


def test_semi_long():
    vig_semi_long = Vigenere(alphabet, semi_long)
    ciphered = vig_semi_long.cipher(message)
    assert ciphered == "IFWYVWWUXMQFTXIORHF"
    assert vig_semi_long.decipher(ciphered) == message


def test_extra_points():
    vig_random = Vigenere(alphabet)
    ciphered = vig_random.cipher(message)
    assert vig_random.decipher(ciphered) == message
    assert len(vig_random.password) >= 4