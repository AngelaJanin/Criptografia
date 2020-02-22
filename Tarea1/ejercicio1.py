from PIL import Image
import PIL.Image as Image
import io

class Ejercicio1: 

    def imagen2Array():
        with open("imagen.enc", "rb") as image:
            img = image.read()
            imagenByte = bytearray(img)   
        return imagenByte
    
    alfabeto = len(list(range(0, 256)))    

    for intento in range(alfabeto):
        imagenByte = imagen2Array()     
        longitud = len(imagenByte)


        for i in range(longitud):
            imagenByte[i] = (imagenByte[i] + intento) % 256  
        
        idImagen = "imagen" + str(intento) + ".jpg"
        f = open(idImagen, 'wb')
        f.write(imagenByte)
        f.close()

    


    
    



    


