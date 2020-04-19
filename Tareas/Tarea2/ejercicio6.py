import base64
"""
Funcion que se encarga de encriptar la imagen llamada imagen.png
que le manda Bartolo a Alicia en el ejercicio 6
"""
def encriptaImagen():
    # Leemos y decodificamos la cadena que estaba en base 64
    # y la pasamos a bytes
    llave = open("cinta_aleatoria.txt","rb")
    llave = llave.read()
    llave = base64.b64decode(llave)
    llave = bytearray(llave)
    # Leemos la imagen y la pasamos a bytes
    imagen = open("imagen.png","rb")
    imagen = imagen.read()
    imagen = bytearray(imagen)
    # Aplicamos la funcion XOR y vamos guardando el cifrado
    cifrado = ""
    for i in range(len(llave)):
        cifrado += chr(imagen[i]^llave[i])
    # Guardamos el cifrado en un archivo.txt
    cifrado = bytearray(cifrado)
    guardaCifrado(cifrado)
    imprimeBytes(cifrado, 2)

"""
Funcion que se encarga de guardar el cifrado de la imagen
en un archivo .txt llamado imagen_cifrada.txt
"""
def guardaCifrado(cifrado):
    c = open("imagen_cifrada.mp3","wb")
    c.write(cifrado)

"""
Funcion que se encarga de imprimir los primeros num
bytes del cifrado recibido 
"""
def imprimeBytes(cifrado,num):
    for i in range(num):
        print (cifrado[i])

"""
Funcion que revisa o checa si la longitud de la llave 
es igual a la de la imagen
"""
def checaLongitud(llave, imagen):
    print len(llave)
    return len(llave) == len(imagen)




encriptaImagen()