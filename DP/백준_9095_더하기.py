import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    num=int(input())

    d=[0]*(num+3)
    d[0]=0
    d[1]=1
    d[2]=2
    d[3]=4
    for i in range(4,num+1):
        d[i]=d[i-1]+d[i-2]+d[i-3]
        
    print(d[num])