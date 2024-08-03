numero_de_cidades = int(input())
cidades = {}
for x in range(1, numero_de_cidades + 1):  # Corrigindo o loop para incluir o número de cidades
    numeros = input().split(' ')
    cidades[x] = [int(num) for num in numeros]

maior_caminho = 0
for x in cidades:
    caminho = 0
    empresa = cidades[x][2]
    destino = cidades[x][1]
    empresa_destino = cidades[destino][2]
    while destino != empresa:  # Corrigindo a condição do loop while
        caminho += 1
        destino = cidades[destino][1]  # Corrigindo o acesso aos dados da cidade
        empresa_destino = cidades[destino][2]  # Corrigindo o acesso aos dados da cidade
    if caminho > maior_caminho:
        maior_caminho = caminho
