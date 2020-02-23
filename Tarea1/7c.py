# Ejercicio 7 c) 
"""
Función que descifra el audio.mp3  encriptado con afin
"""
def decipher():
    # Leemos el archivo y lo pasamos a un arreglo de bytes
    encriptado = open("audio.enc", "rb")
    archivo = encriptado.read()
    audio = bytearray(archivo)
    audio_descifrado = audio 
    # Para cada byte del audio lo desciframos usando la fórmula x = (a^-1 (y-b)) mód n 
    for i,b in enumerate(audio):
        audio_descifrado[i]=(197*(audio[i] - 255))%256
	# Guardamos y escribimos el audio descifrado
    audio = open("audio_descrifrado.mp3", "wb")
    audio.write(audio_descifrado)

# Ejecutamos la función para descifrar el audio
decipher()