numero_de_cidade=int(input())
cidade={}
x=0
while len(cidade)<numero_de_cidade-1:
    numeros=input().split(' ')
    cidade[x]=[int(numeros[0]),int(numeros[1]),int(numeros[2])]
    x+=1
maior_caminho=0
for x in range(1,len(cidade)-2):
    caminho=0
    empresa=cidade[x][2]
    destino=cidade[x][1]
    empresa_destino=cidade[destino][2]
    entrou=False
    while empresa_destino==empresa:
        entrou=True
        caminho+=1
        if destino<=len(cidade):
            destino=cidade[destino][1]
            empresa_destino=cidade[empresa_destino][2]
        else:
            break
    if not entrou:
        caminho=1
    if caminho>maior_caminho:
        maior_caminho=caminho
print(maior_caminho)