E, I, V = [int(x) for x in input().split()]
conjunto_geral = {}

# Leitura das implicações
for _ in range(I):
    a, b = [int(x) for x in input().split()]
    if b not in conjunto_geral:
        conjunto_geral[b] = []
    conjunto_geral[b].append(a)

# Leitura das observações
observacoes = set([int(x) for x in input().split()])
aconteceu = set(observacoes)

# Realização das deduções
mudanca = True
while mudanca:
    mudanca = False
    novos_acontecimentos = set()
    for efeito, causas in conjunto_geral.items():
        if efeito not in aconteceu and all(causa in aconteceu for causa in causas):
            novos_acontecimentos.add(efeito)
            mudanca = True
    aconteceu.update(novos_acontecimentos)

# Impressão do resultado
resultado = ' '.join(map(str, sorted(aconteceu)))
print(resultado)
