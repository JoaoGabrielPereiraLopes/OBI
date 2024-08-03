l,h=input().split(' ')
l=int(l)
h=int(h)
mapa=[]
for x in range(0,l):
    lista=input().split(' ')
    nova_lista=[]
    for y in lista:
        nova_lista+=[int(y)]
    mapa+=[nova_lista]
    nova_lista=[]
atual=0
achou=False
for y_da_emilia in range(0,l):
    for x_da_emilia in range(0,h):
        if mapa[x_da_emilia][y_da_emilia]==2:
            achou=True
            break
    if achou:
        break
andadas=0
if mapa[y_da_emilia+1][x_da_emilia]==1:
    mapa[y_da_emilia+1][x_da_emilia]=4
    andadas+=1
elif mapa[y_da_emilia-1][x_da_emilia]==1:
    mapa[y_da_emilia-1][x_da_emilia]=4
    andadas+=1
elif mapa[y_da_emilia][x_da_emilia+1]==1:
    mapa[y_da_emilia-1][x_da_emilia]=4
    andadas+=1
elif mapa[y_da_emilia][x_da_emilia-1]==1:
    mapa[y_da_emilia][x_da_emilia-1]=4
    andadas+=1
saiu=False
while not saiu:
    andou=False
    for y in range(0,l):
        for x in range(0,h):
            if mapa[y][x]==4:
                if y+1<len(mapa[x]):
                    if mapa[y+1][x]==1 and mapa[y][x]== 4:
                        mapa[y+1][x]=4
                        if not andou:
                            andadas+=1
                        andou=True
                    elif mapa[y+1][x]==3:
                        if andou:
                            andadas-=1
                        saiu=True
                        break
                elif y!=0:
                    if mapa[y-1][x]==1 and mapa[y][x]== 4:
                        mapa[y-1][x]=4
                        if not andou:
                            andadas+=1
                    elif mapa[y-1][x]==3:
                        if andou:
                            andadas-=1
                        saiu=True
                        break
                elif x+1<len(mapa):
                    if mapa[y][x+1]==1 and mapa[y][x]== 4:
                        mapa[y-1][x]=4
                        if not andou:
                            andadas+=1
                    elif mapa[y][x+1]==3:
                        if andou:
                            andadas-=1
                        saiu=True
                        break
                elif x!=0:
                    if mapa[y][x-1]==1 and mapa[y][x]== 4:
                        mapa[y][x-1]=4
                        if not andou:
                            andadas+=1
                    elif mapa[y][x-1]==3:
                        if andou:
                            andadas-=1
                        saiu=True
                        break
print(andadas)