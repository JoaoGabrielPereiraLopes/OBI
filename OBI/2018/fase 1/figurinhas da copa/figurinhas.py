tamanho,carimbadas,compradas=input().split(' ')
carimbadas=input().split(' ')
obtidas=input().split(' ')
diferentes=carimbadas
for x in obtidas:
    if x not in diferentes:
        diferentes+=x
print(int(tamanho)-len(diferentes))
