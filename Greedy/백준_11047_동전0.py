import sys
input=sys.stdin.readline

n,k=map(int, input().split())
coin=[]

for _ in range(n):
    coin.append(int(input()))

coin.reverse()
cnt=0
for i in range(n):
    cnt+=k//coin[i]
    k=k%coin[i]
            
        
print(cnt)       

