peças={}
objetivo=0
for x in range(0,int(input())):
    entrada=input().split(' ')
    peças[int(entrada[0])]=[entrada[1],int(entrada[2])]
texto=''
for x in range(0,len(peças)):
    texto+=peças[objetivo][0]
    objetivo=peças[objetivo][1]
print(texto)