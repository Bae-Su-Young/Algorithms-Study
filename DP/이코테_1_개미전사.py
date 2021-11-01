import sys
input=sys.stdin.readline


n=int(input())
storage=list(map(int,input().split()))
table=[0]*n
# 점화식
# a_i=max(a_i-1, a_i-2+k)
# k:i번째 창고의 식량 수

table[0]=storage[0]
table[1]=max(storage[0],storage[1])
#table[1]=storage[1] -> 1번만 골랐을 때
for i in range(2,n):
    table[i]=max(table[i-1],table[i-2]+storage[i])

print(table[-1])
