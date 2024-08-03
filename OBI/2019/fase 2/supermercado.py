N=int(input())
preço=[float(x) for x in input().split(' ')]
preço=preço[0]/preço[1]
for x in range(N-1):
    novo_preço=[float(x) for x in input().split(' ')]
    novo_preço=novo_preço[0]/novo_preço[1]
    if novo_preço<=preço:
        preço=novo_preço
print(round(preço*1000,2))