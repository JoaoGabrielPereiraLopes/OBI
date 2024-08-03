tamanho=int(input())
lista=[int(x) for x in input().split(' ')]
operacoes=0
index=0
exec=0
while exec<=len(lista):
    lista[index]==lista[len(lista)-index-1]
    if lista[index]==lista[len(lista)-index-1]:
        index+=1
        exec+=2
    elif lista[index]<lista[len(lista)-index-1]:
        operacoes+=1
        lista[index]+=lista[index+1]
        lista.pop(index+1)
    elif lista[index]>lista[len(lista)-index-1]:
        operacoes+=1
        lista[len(lista)-index-1]+=lista[len(lista)-index-2]
        lista.pop(len(lista)-index-2)
print(operacoes)