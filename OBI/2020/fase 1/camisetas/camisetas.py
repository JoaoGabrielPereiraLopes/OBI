n_premidos=int(input())
tamanho=input()
quant_pequenas=int(input())
quant_medio=int(input())
if tamanho.count('1')<=quant_pequenas and tamanho.count('2')<=quant_medio:
    print('S')
else:
    print('N')