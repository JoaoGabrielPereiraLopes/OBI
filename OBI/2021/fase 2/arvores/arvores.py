arvores=int(input())
a=[int(x) for x in input().split(' ')]
sepracoes=[]
for x in range(0,arvores//2):
    soma=0
    for x in range(x,arvores//2):
        soma+=a[x-1]
    sepracoes+=[soma]
sepracoes2=[]
for x in range(arvores//2,arvores):
    soma=0
    for x in range(x,arvores):
        soma+=a[x-1]
    sepracoes2+=[soma]
retangulos=False
for x in sepracoes2:
    if x in sepracoes: 
        retangulos=True
if retangulos:
    print('S')
else:
    print('N')