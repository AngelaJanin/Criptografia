def cipher(message):
    """
    Cifra el mensaje recibido como parámetro con el algoritmo de cifrado
    XOR.
    Parámetro:
       message -- el mensaje a cifrar.
    """
   cadena_binario = ""
    letras_nums = []
    xor = []
    cifrado = ""
    # Pasamos cada letra del mensaje a una cadena binaria y
    # guardamos su valor en binario en una lista para no perderlos
    for letra in message:
        aux = aBinario(letra)
        cadena_binario = cadena_binario + aux
        letras_nums.append(aux)
 
    # Le aplicamos a cada elemento de la lista la funcion XOR
    for elemento in letras_nums:
        palabra_binaria = ""
        longitud = len(elemento)
        c = 0
        # Aplicamos XOR para cada bit de la letra 
        for i in range(longitud):
            if c == longitud-1:
                if elemento[c] != format(1, 'b'):
                    palabra_binaria = palabra_binaria + "1"
                else:
                    palabra_binaria = palabra_binaria + "0"
            else:
                palabra_binaria = palabra_binaria + elemento[c]
            c = c + 1 
        xor.append(palabra_binaria)

    cifrado = ""
    # Concatenamos cada letra cifrada con XOR 
    for elem in xor:
        entero = aEntero(elem)
        palabra_cifrada = aLetra(entero)
        cifrado = cifrado + palabra_cifrada
    return cifrado

def decipher(criptotext):
    """
    Descifra el mensaje recuperando el texto plano siempre y cuando haya
    sido cifrado con XOR.
    Parámetro:
       cryptotext -- el mensaje a descifrar.
    """
   cadena_binario = ""
    letras_nums = []
    xor = []
    texto_claro = ""
    # Pasamos cada letra del criptotexto a una cadena binaria y
    # guardamos su valor en binario en una lista para no perderlos
    for criptoletra in criptotext:
        aux = aBinario(criptoletra)
        cadena_binario = cadena_binario + aux
        letras_nums.append(aux)
 
    # Le aplicamos a cada elemento la función inversa de XOR
    for elemento in letras_nums:
        palabra_binaria = ""
        longitud = len(elemento)
        c = 0
        # Ahora encontramos los 1 para cambiarlos por 0
        for i in range(longitud):
            if c == longitud-1:
                if elemento[c] == format(1, 'b'):
                    palabra_binaria = palabra_binaria + "0"
                else:
                    palabra_binaria = palabra_binaria + "1"
            else:
                palabra_binaria = palabra_binaria + elemento[c]
            c = c + 1 
        xor.append(palabra_binaria)

    cifrado = ""
    # Concatenamos cada letra en claro
    for elem in xor:
        entero = aEntero(elem)
        palabra_clara = aLetra(entero)
        texto_claro = texto_claro + palabra_clara
    return texto_claro

"""
Función auxiliar que convierte una letra a su número binario
correspondiente 
"""
def aBinario(letra):
    return format(ord(letra), 'b')

"""
Función auxiliar que convierte un número binario a un 
número entero 
"""
def aEntero(numero):
    return int(numero , 2)

"""
Función auxiliar que convierte un número entero a su 
letra o caracter correspondiente 
"""
def aLetra(numero):
    return chr(numero)
