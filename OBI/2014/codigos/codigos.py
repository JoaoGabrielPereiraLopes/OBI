def decodifica():
    retorno=''
    entrada=input()
    for x in range(0,len(entrada)-1):
        if entrada[x-1]=='p' and entrada[x+1]=='p' or entrada[x]==' ' or entrada[x+1]==' ':
            retorno+=entrada[x]
    return retorno+entrada[len(entrada)-1]
print(decodifica())