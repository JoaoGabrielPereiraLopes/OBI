sequencia=input().split(' ')
falsa='f'
for x in sequencia:
    if sequencia.count(x)==2:
        if sequencia[sequencia.index(x)]==sequencia[sequencia.index(x)+2]:
            falsa='v'
        break
print(falsa.upper())