consoante=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','x','z']
palavra=input()
resultado=''
for x in palavra:
    criptografia=x
    if x in consoante:
        if consoante.index(x)<2:
            criptografia+='a'
        elif consoante.index(x)>=2 and consoante.index(x)<5:
            criptografia+='e'
        elif consoante.index(x)>=5 and consoante.index(x)<9:
            criptografia+='i'
        elif consoante.index(x)>=9 and consoante.index(x)<14:
            criptografia+='o'
        else:
            criptografia+='u'
        if not x =='z':
            criptografia+=consoante[consoante.index(x)+1]
        else:
            criptografia+='z'
    resultado+=criptografia
print(resultado)