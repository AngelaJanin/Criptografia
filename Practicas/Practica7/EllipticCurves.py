from sympy import mod_inverse
class Curve():

    def __init__(self, A, B, p):
        """
        Construcutor de clase que va a representar a la curva elíptica de la
        forma y^2 = x^3 + Ax + B (mod p).
        :param A: primer coeficiente de la curva.
        :param B: segundo coeficiente de la curva.
        :param p: el tamaño del campo sobre el cual se hace la curva.
        """
        self.A = A
        self.B = B
        self.p = p 

    def is_on_curve(self, point):
        """
        Método de clase regresa true si un punto está en la curva, éste punto 
        está representado a manera de tupla, como (x, y).
        :param point: Una tupla de enteros representando a un punto.
        :return: true si el punto está en la curva, false en otro caso.
        """
        if point == None :
        	return True
        x, y = point[0], point[1]
        return pow(y,2) % self.p == ((pow(x,3) + (self.A * x) + self.B) % self.p)

    def determinant(self):
        """
        Regresa el determinante de una curva, recordando que su determinante
        es calculado de la forma 4A^3 + 27B^2.
        :return: El entero con el valor del determinante.
        """
        return (4 * pow(self.A,3)) + (27 * pow(self.B,2))

def add_points(p, q, curve):
    """
    Dados un par de puntos y una curva elíptica, calcula el punto de la suma
    bajo la curva elíptica recibida como parámetro, se asume que p y q ya 
    forman parte de la curva.
    :param p: una tupla representando un punto de la curva.
    :param q: una tupla representando un punto de la curva.
    :param curve: una instancia de la clase de este script.
    :return: Una tupla que contiene el resultado de la suma o None en caso de
    que haya sido evaluada al punto infinito.
    """
    # Caso en el que se tiene el mismo punto o un punto con la misma coordenada x
    # O que su coordenada x sea igual y la coordenada y cumple con -y1 = y2
    if (p == q) or ((p[0] == q[0]) and (-p[1] ==  q[1])):
    	return None
    # Caso en el que el punto q es es el punto al infinito
    elif (q == None) and p != None:
    	return p 
    # Caso en el que el punto p es el punto al infinito
    elif (p == None) and q != None:
    	return q
    else:
    	x1, x2, y1, y2 = p[0], q[0], p[1], p[1]
    	if (x1 == x2):
    		return None
    	l = calculaLambda(p, q, curve)
    	x = pow(l,2) - x1 - x2
    	y = (l * (x1 - x)) - y1
    	return(x,y)

def scalar_multiplication(p, k, curve):
    """
    Dado un escalar del campo, k, calcula el punto kP bajo la definición
    de curvas elípticas.
    :param p: una tupla representando un punto de la curva.
    :param k: el escalar a multiplicar por el punto. 
    :param curve: la curva sobre la cual se calculan las operaciones.
    :return: una tupla representando a kP o None si al sumar ese punto cayó 
    en algún momento al punto infinito.
    """
    if k == 1:
    	return p
    return add_points(p, scalar_multiplication(p,(k-1), curve),curve)

"""
Función auxiliar para calcular el término lambda que se 
utiliza para la suma de puntos.
:param p: punto a sumar
:param q: punto a sumar
:param c: 
"""
def calculaLambda(p, q, c):
	x1, x2, y1, y2 = p[0], q[0], p[1], q[1]
	if p == q :
		return (3 * pow(x1,2) + c.A) * mod_inverse((2 * y1),c.p)
	return (y1 - y2) * mod_inverse((x1 - x2), c.p)
