from ECIES import ECIES
from EllipticCurves import Curve

cipher = None

def test_encrypt():
    c = Curve(7, 19, 31)
    p = 31
    A = (18, 26)
    B = (10, 2)
    cipher = ECIES(c, A, B, 39, 8, 31)
    result = cipher.encrypt("PUMAS")
    for r in result:
        y1, y2 = r
        assert y1[1] in range(0, 2)
        assert y1[0] in range(1, 31)
        assert y2 in range(1, 31)
    assert cipher.decrypt(result) == "PUMAS"
        
