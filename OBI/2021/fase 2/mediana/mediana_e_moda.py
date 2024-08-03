lista=sorted([int(x) for x in input().split(' ')])
numero=0
import time
trocar=False
while True:
    lista_ordenada=sorted(lista+[numero])
    soma=0
    for x in lista_ordenada:
        soma+=x
    media=soma/len(lista)
    if len(lista_ordenada)%2==0:
        mediana=(lista[(len(lista_ordenada)+1)//2]+lista[int((len(list)+1)/2+0.5)])/2
    elif len(lista_ordenada)%2==1:
        mediana=lista[(len(lista_ordenada)-1)//2]
    if float(mediana)==float(media):    
        break
    elif trocar:
        numero*=-1
        numero+=1
        trocar=False
    else:
        numero*=-1
        trocar=True