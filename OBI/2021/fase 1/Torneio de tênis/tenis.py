jogo=0
vitorias=0
while jogo<6:
    resultado=input()
    if resultado=="V":
        vitorias+=1
    jogo+=1
if vitorias>=5:
    print(3)
elif vitorias<5 and vitorias>=3:
    print(2)
elif vitorias==1 or vitorias==2:
    print(1)
else:
    print(-1)