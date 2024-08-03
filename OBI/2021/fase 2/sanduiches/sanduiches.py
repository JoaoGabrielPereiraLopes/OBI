import math
def fatorial(a,b):
    fatorial=1
    for x in range(1,b+1):
        fatorial*=x
    return fatorial
a, b = [int(x) for x in input().split(" ")]
pares = {}
for x in range(1, a + 1):
    pares[x] = []
for x in range(0,b):
    par=[int(x) for x in input().split(" ")]
    pares[par[0]]+=[str(par[1])]
    pares[par[1]]+=[str(par[0])]
possibilidades=0
for x in range(1,len(pares)):
    possibilidades+=math.comb(x,len(pares)-x)
print(possibilidades-b)