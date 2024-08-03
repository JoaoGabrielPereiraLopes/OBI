entrada=input().split(" ")
IA=1==int(entrada[0])
IB=1==int(entrada[1])
FA=1==int(entrada[2])
FB=1==int(entrada[3])
if FA==IA and FB==IB:
    minimo=0
elif FA!=IA and FB !=IB or FA!=IA and FB == IB:
    minimo=1
elif FA==IA and FB!=IB:
    minimo=2
print(minimo)