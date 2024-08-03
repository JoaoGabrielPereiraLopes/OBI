altura,largura=input().split(' ')
altura=int(altura)
largura=int(largura)
matriz=[]
for x in range(0,altura):
    lista=[]
    for x in input():
        lista+=[x]
    matriz+=[lista]
for y in range(0,altura):
    for x in range(0,largura):
            try:
                if matriz[y-1][x]=='O' and matriz[y][x]=='.' :
                    matriz[y][x]='O'
                elif matriz[y+1][x]=='#' or matriz[y+1][x+1]=='#' or matriz[y+1][x-1]=='#':
                    matriz[y][x]='O'
            except:
                if matriz[y-1][x]=='O':
                    matriz[y][x]='O'
                try:
                    if matriz[y+1][x]=='#' or matriz[y+1][x-1]=='#':
                        matriz[y][x]='O'
                except:
                    pass
for x in matriz:
    texto=''
    for y in x:
        texto+=str(y)
    print(texto)