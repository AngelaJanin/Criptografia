'''
Función que encripta y desencripta usando RC4 
tomada de Omar Arroyo
'''
def rc4_encrypt(key, data):
    # Inicialización
    x = 0
    box = list(range(256))
    for i in range(256):
        x = (x + box[i] + key[i % len(key)]) % 256
        box[i], box[x] = box[x], box[i]
        
    # Generación de bytes pseudoaleatorios y cifrado
    x = 0
    y = 0
    out = []
    for byte in data:
        x = (x + 1) % 256
        y = (y + box[x]) % 256
        box[x], box[y] = box[y], box[x]
        out.append(byte ^ box[(box[x] + box[y]) % 256])
    return bytes(out)
'''
Función que aplica el xor entre los dos parámetros recibidos
que son el flujo aleatorio y los números de cuenta
'''
def xor(aleatorio, num):
    encriptado = []
    for i in range(len(num)):
        encriptado.append(aleatorio[i] ^ num[i])
    return bytes(encriptado)

# Leemos el archivo tarea.txt que tiene el formato indicado
archivo = open("tarea.txt","rb")
archivo = archivo.read()
# Encriptamos la tarea con RC4
archivo = rc4_encrypt(b'criptografia', archivo)
aux = archivo
descifrado = rc4_encrypt(b'criptografia',archivo)
print("La tarea sin modificar es:")
print(descifrado)
# Obtenemos el número de cuenta de 0123456789
aux = aux[15:25]
# Obtenemos el flujo aleatorio con el que se cifró la tarea
# Ejecutando el xor del cifrado y número de cuenta 0123456789
flujo = xor(aux, b'0123456789')
# Obtenemos el número de cuenta 1231231231 haciendo el xor
# entre el flujo aleatorio obtenido y el número de cuenta 1231231231.
num_cifrado = xor(flujo,b'1231231231')
# Reemplazamos en el archivo original el número de cuenta de 
# 0123456789 por 1231231231
archivo = archivo.replace(aux,num_cifrado)
# Desencriptamos la tarea modificada y la imprimimos 
tarea = rc4_encrypt(b'criptografia',archivo)
print("La tarea con el número de cuenta ya modficado es:")
print(tarea)

