import sys
input=sys.stdin.readline

n=int(input())
power=list(map(int,input().split()))
power.reverse()  ## 왜 뒤집??
d=[1]*n

for i in range(1,n):
    for j in range(0,i):
        if power[i-1]<power[i]:
            d[i]=max(d[j]+1,d[i])


print(n-max(d))