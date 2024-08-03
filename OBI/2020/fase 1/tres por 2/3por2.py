n=int(input())
chocolates=[]
for x in range(0,n):
    chocolates+=[int(input())]
chocolates.sort()
chocolates.reverse()
for x in range(2,len(chocolates),int((len(chocolates)+(3-len(chocolates)%3))/3)):
    chocolates[x]=0
soma=0
for x in chocolates:
    soma+=x
print(soma)
