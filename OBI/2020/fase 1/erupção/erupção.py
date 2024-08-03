from random import *
numero=''
for x in input()+'f':
    if x.isnumeric():
        numero+=x
    elif x==' ':
        tamanho=int(numero)
        numero=''
    else:
        forca=int(numero)
        numero=''
matriz=[]
x=0
while x<tamanho:
    lista=[]
    for y in input():
        lista+=[int(y)]
    matriz+=[lista]
    x+=1
matriz[0][0]='*'
continua=True
for x in range(0,len(matriz)):
    for y in range(0,len(matriz[x])):
        if matriz[x][y] !='*':
            if x>=2:
                if matriz[x-1][y]=='*':
                    continua=True
            if matriz[x][y] <= forca and continua:
                matriz[x][y]='*'
            elif matriz[x][y]!='*':
                continua=False
                matriz[x][y]=str(matriz[x][y])
        else:
            matriz[x][y]='*'
    continua=True
    string=''
    for y in matriz[x]:
        string+=y
    print(string)