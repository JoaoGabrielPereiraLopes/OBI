s=int(input())
a=int(input())
b=int(input())
total=0
for x in range(a,b+1):
    soma=0
    x=str(x)
    for y in x:
        soma+=int(y)
    if soma==s:
        total+=1
print(total)