irma1=int(input())
irma2=int(input())
irma3=int(input())
if irma1>irma2 and irma1<irma3 or irma1>irma3 and irma1<irma2:
    print(irma1)
elif irma2>irma3 and irma2<irma1 or irma2>irma3 and irma2<irma1:
    print(irma2)
else:
    print(irma3)