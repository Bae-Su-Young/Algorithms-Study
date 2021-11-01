from collections import deque

def dfs(graph, v, visited):
    visited[v]=True
    print(v,end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)


def bfs(graph,start,visited):
    visited[start]=True
    queue=deque([start])
    while queue:
        v=queue.popleft()
        print(v,end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True
    


n,m,v=map(int,input().split())
graph=[[] for i in range(n+1)]
visited=[False]*(n+1)

for i in range(m):
    src,dst=map(int,input().split())
    graph[src].append(dst)
    graph[dst].append(src)

for i in range(len(graph)):
    graph[i].sort()

dfs(graph,v,visited)
visited=[False]*(n+1)
print()
bfs(graph,v,visited)