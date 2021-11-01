import sys
input=sys.stdin.readline

num=int(input())
table=[0]*3001


# 점화식
# a_i = i를 1로 만들기 위한 최소 연산 횟수
# a_i = min(a_i-1, ai/2, ai/3,ai/5)+1

for i in range(2,num+1):
    table[i]=table[i-1]+1
    if i%2==0: 
        table[i]=min(table[i],table[i//2]+1)
    if i%3==0: 
        table[i]=min(table[i],table[i//3]+1)
    if i%5==0: 
        table[i]=min(table[i],table[i//5]+1)
    
print(table[num])
