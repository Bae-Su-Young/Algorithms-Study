import sys
input=sys.stdin.readline

INF=int(1e9)

n,m=map(int,input().split())
graph=[[INF]*(n+1) for _ in range(n+1)]

for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b]=0

for _ in range(m):
    u,v=map(int,input().split())
    graph[u][v]=1
    graph[v][u]=1

x,k=map(int,input().split())

for kk in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b],graph[a][kk]+graph[kk][b])
result=graph[1][k]+graph[k][x]
if result !=INF:
    print(result)
else:
    print(-1)
