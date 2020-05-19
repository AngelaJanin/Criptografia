from RSA import RSA
from utils import prime_relative

c = RSA()

def test_constructor():
    str_n = str(c.n)
    assert len(str_n) >= 100
    phi_n = c.__phi__()
    assert prime_relative(phi_n, c.pub_key)
    assert (c.pub_key * c.priv_key) % phi_n == 1

def test_cipher():
    m = "NO DERRAMES LA COCA"
    res = c.encrypt(m)
    if not(c.padding_scheme):
        assert len(res) == len(m)
    assert c.decrypt(res) == m
