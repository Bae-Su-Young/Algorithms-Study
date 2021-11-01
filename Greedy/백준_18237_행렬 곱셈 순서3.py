import heapq

n=int(input())
h=[]
for _ in range(n):
    r,c=map(int,input().split())
    heapq.heappush(h,(r,c))


