N=int(input())
AN=[int(x) for x in input().split(' ')]
possivel=True
AN.sort()
if not(AN[0]>8):
    for x in range(1,len(AN)):
        if AN[x]-AN[x-1]>8:
            possivel=False
            break
        if not possivel:
            break
else:
    possivel=False
if possivel:
    print('S')
else:
    print('N')