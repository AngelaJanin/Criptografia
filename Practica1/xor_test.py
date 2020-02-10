import xor_cipher as XOR

def test_xor():
    xors = [("HOLA","INM@"),
            ("Do not spill the beans","En!onu!rqhmm!uid!cd`or"),
            ("Ésta es una frase en español","Èru`!dr!to`!gs`rd!do!drq`ðnm")]
    for tup in xors:
        mess, crip = tup
        assert XOR.cipher(mess) == crip
        assert XOR.decipher(crip) == mess
