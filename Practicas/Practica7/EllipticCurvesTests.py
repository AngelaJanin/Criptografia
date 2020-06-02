import EllipticCurves as ec

c = ec.Curve(2, 3, 97)

def test_class():
    assert c.is_on_curve((17, 10))
    assert c.is_on_curve((95, 31))
    assert not c.is_on_curve((13, 13))
    assert c.is_on_curve(None)
    assert c.determinant() == 275

P, Q = (17, 10), (95, 31)
    
def test_add_curve():
    p_plus_q = ec.add_points(P, Q, c)
    assert c.is_on_curve(p_plus_q)
    inf = ec.add_points(P, (17, 87), c)
    assert c.is_on_curve(inf) and inf == None
    p_plus_p = ec.add_points(P, P, c)
    assert c.is_on_curve(p_plus_p)

def test_scalar_mult():
    one_p = ec.scalar_multiplication(P, 1, c)
    assert c.is_on_curve(one_p)
    k = 1
    while one_p != None :
        one_p = ec.add_points(P, one_p, c)
        k += 1
    assert ec.scalar_multiplication(P, k, c) == None
    

