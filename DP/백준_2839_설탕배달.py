import sys
input=sys.stdin.readline

n=int(input())
d=[5001]*(n+5)  # 최소값을 구해야 하므로
                # n의 범위보다 하나 큰 값인 5001로 초기화
                # +5 : n이 5보다 작은 값일 때
d[3]=d[5]=1

for i in range(6,n+1):
    d[i]=min(d[i-3],d[i-5])+1

print(d[n] if d[n]<5001 else -1)

