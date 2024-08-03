botas={}
limite=int(input())
for entradas in range(0,limite):
    numero,pe=input().split(' ')
    try:
        botas[numero]+=pe
    except:
        botas[numero]=pe
pares=0
for numero in botas:
    if botas[numero].count('D')<= botas[numero].count('E'):
        pares+=botas[numero].count('D')
    else:
        pares+=botas[numero].count('E')
print(pares)