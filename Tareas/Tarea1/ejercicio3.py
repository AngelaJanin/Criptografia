from collections import OrderedDict
from operator import itemgetter

class Ejercicio3: 
    cifrado = "GIR DYK NBWBTBQ. PRIIK K HGRDYH RSBLRIJA K SJQÑGRIJA, ÑGIJ QR ÑQYDR MYG NGCBR OJQRI PRHLR GQ LGTPJ AJ HG DJOBR NGQ ÑYÑBLIG. HGRDYH HG ÑYHJ LRA BDÑRTBGALG MYG QR ÑBATPJ TJA HY ORIBLR K QG ÑIGANBJ WYGSJ, K PRIIK LYOJ MYG RÑRSRIQJ TJA HY HJDCIGIJ. IJA, GA QR DGHR ÑIJUBDR, AJ GHLRCR LGABGANJ DYTPR DRH HYGILG. ¡XBASRINBYD QGOBJHR! SIBLJ, RSBLRANJ HYH QRISJH CIREJH TJDJ YA DJQBAJ. QJ GHLRH NBTBGANJ DRQ. PRIIK JKJ MYG PGIDBJAG QJ IGZBR. GH XBASRINBYD QGOBJHR, ÑIJAYATBR SRI DRH TQRIJ K DRH QRISJ. NBQJ LY, GALJATGH, HB GIGH LRA BALGQBSGALG NBVJ IJA TJA IRCBR. PGIDBJAG HG RIIGDRASJ QRH DRASRH NG HY LYABTR, RSBLJ QR ORIBLR K NBVJ QRH ÑRQRCIRH DRSBTRH. QR ÑQYDR HG GQGOJ NGQ ÑYÑBLIG K QQGSJ PRHLR DRH NG YA DGLIJ ÑJI GATBDR NG HYH TRCGERH. ¡JP, CBGA PGTPJ! SIBLJ GQ ÑIJWGHJI WQBLXBTF, RÑQRYNBGANJ. ¡DBIRN, PGIDBJAG SIRASGI QJ PR TJAHGSYBNJ! RQ WBARQBERI QR TQRHG, IJA GHLRCR NG DYK DRQ PYDJI. AJ GH IRIJ MYG ARNBG QR RSYRALG NBVJ R PRIIK, TYRANJ HG RCIBRA ÑRHJ GA GQ ÑRHBQQJ. GH YAR ÑGHRNBQQR, LG QJ NBSJ GA HGIBJ. RQSYBGA TPJTJ TJALIR PRIIK. GIR PGIDBJAG. PRIIK ÑYNJ OGI HY TRIR K QG HJIÑIGANBJ OGI MYG GHLRCR QQJIRANJ."
    decifrado = ""
    diccionario = {}
    sortDiccionario = {}

    for x in cifrado:
        if x in diccionario:
            diccionario[x]=diccionario[x]+1
        else:
            diccionario[x]=1
    
    sortDiccionario = OrderedDict(sorted(diccionario.items(), key = itemgetter(1), reverse = True))           

    decifrado = cifrado.translate(str.maketrans({'G': 'E', 'I': 'R', 'R': 'A', 'D': 'M', 
    'Y': 'U', 'K':'Y', 'S':'G', 'B':'I','L':'T', 'J':'O', 'A':'N', 'P':'H', 'Q':'L', 
    'Ñ':'P', 'N':'D', 'H':'S', 'O':'V', 'M':'Q', 'C':'B', 'T':'C', 'W':'F', 'U':'X', 'E':'Z',
    'V':'J', 'X':'W', 'F':'K' }))        
 
    print(sortDiccionario) 
    print("\n")     
    print(cifrado)  
    print("\n")     
    print(decifrado)
    
