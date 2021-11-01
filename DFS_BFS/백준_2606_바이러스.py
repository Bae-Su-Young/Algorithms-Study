def dfs(v):
    global result
    visited[v]=True
    result+=1
    for i in network[v]:
        if not visited[i]:
            dfs(i)

n=int(input())
m=int(input())
visited=[False]*(n+1)
result=0
network=[[] for _ in range(n+1)]
for _ in range(m):
    u,v=map(int, input().split())
    network[u].append(v)
    network[v].append(u)

dfs(1)
print(result-1)