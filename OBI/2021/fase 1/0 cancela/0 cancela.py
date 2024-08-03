n_de_compras=int(input())
lista=[]
n_digitados=0
while n_digitados<n_de_compras:
    numero=int(input())
    if numero==0:
        del lista[-1]
    else:
        lista+=[numero]
    n_digitados+=1
soma=0
for x in lista:
    soma+=x
print(soma)