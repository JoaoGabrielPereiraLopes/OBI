def retornador(y):
    for y in malha_ferroviaria:
        if str(x) in y:
            utilizadas+=y
cidades,Ferrovias,Rodovias=input().split(' ')
cidades=int(cidades)
Ferrovias=int(Ferrovias)
Rodovias=int(Rodovias)
malha_ferroviaria={}
for x in range(0,Ferrovias):
    entrada=input().split(' ')
    malha_ferroviaria[entrada[0]+ ',' +entrada[1]]=int(entrada[2])
malha_rodoviaria={}
for x in range(0,Rodovias):
    entrada=input().split(' ')
    malha_rodoviaria[entrada[0]+ ',' +entrada[1]]=int(entrada[2])
conectadas=[]
for x in range(0,cidades):
    utilizadas=[]