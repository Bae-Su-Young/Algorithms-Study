import sys
input=sys.stdin.readline
n=int(input())

d=[0,1]

# # 백준_2748_피보나치 수2
# for i in range(2,n+1):
#     d[i]=d[i-1]+d[i-2]
# print(d[-1])

# 백준_2749_피보나치 수3
mod=10**6
period=15*(mod//10)
for i in range(2,period+1):
    d.append(d[i-1]+d[i-2])
    d[i]%=mod

print(d[n%period])