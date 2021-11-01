import sys
t=int(input())

for _ in range(t):

    result=1
    n=int(input())
    boad=[[0]for _ in  range(n)]
    for i in range(n):
        s,m=map(int,sys.stdin.readline().split())
        boad[i]=([s,m])

    boad.sort()
    Max=boad[0][1]

    for i in range(1,n):
        if Max>boad[i][1]:
            result+=1
            Max=boad[i][1]

    print(result)





    







