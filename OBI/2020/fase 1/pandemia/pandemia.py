info_grupo=input()
string=''
for x in info_grupo:
    if x.isnumeric():
        string+=x
    else:
        total_de_amigos=int(string)
        string=''
total_de_reunioes=int(string)
iniciador=input()
x=''
string=''
for x in iniciador:
    if x.isnumeric():
        string+=x
    else:
        id_infectado=int(string)
        string=''
prim_reuniao=int(string)
infectados=[id_infectado]
execucoes=0
string=''
while execucoes<=total_de_reunioes:
    participantes=input()
    presentes=[]
    if execucoes>= prim_reuniao:
        print('entrou')
        for x in participantes+'f':
            if x.isnumeric():
                string+=x
            else:
                presentes+=[int(string)]
                string=''
        for x in presentes:
            if x in infectados:
                for x in presentes:
                    if x not in infectados:
                        infectados+=[x]
                        print('adicionou')
    execucoes+=1
print(len(infectados))