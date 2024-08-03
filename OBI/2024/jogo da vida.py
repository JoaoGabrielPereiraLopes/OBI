n,q=input().split(' ')
q=int(q)
n=int(n)
exec=0
listão=[]
import pandas as pd
while exec<n:
    listinha=[]
    for x in input():
        listinha+=[int(x)]
    listão+=[listinha]
    exec+=1
exec=0
while exec<q:
    for x in range(0,n):
        for y in range(0,n):
            vivos=0
            try:
                if listão[y+1][x+1]==1:
                    vivos+=1
            except IndexError:
                pass
            try:
                if listão[y+1][x]==1:
                    vivos+=1
            except IndexError:
                pass
            try:
                if listão[y+1][x-1]==1:
                    vivos+=1
            except IndexError:
                pass
            try:
                if listão[y][x+1]==1:
                    vivos+=1
            except IndexError:
                pass
            try:
                if listão[y][x-1]==1:
                    vivos+=1
            except IndexError:
                pass
            try:
                if listão[y-1][x+1]==1:
                    vivos+=1
            except IndexError:
                pass
            try:
                if listão[y-1][x]==1:
                    vivos+=1
            except IndexError:
                pass
            try:
                if listão[y-1][x-1]==1:
                    vivos+=1
            except IndexError:
                pass
            if vivos>3 and listão[y][x]==1:
                listão[y][x]=0
            elif vivos<2 and listão[y][x]==1:
                listão[y][x]=0
            elif vivos == 3:
                listão[y][x]=1 
    for x in listão:
        texto=''
        for y in x:
            texto+=str(x)
        print(texto)
    print(pd.DataFrame(listão))
    exec+=1