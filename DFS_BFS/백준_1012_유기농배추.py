import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

# visited 테이블이 없으면 메모리 초과 -> 같은 노드를 반복해서 방문하게 되기 때문
def dfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    if graph[x][y]==1 and visited[x][y]==False:
        graph[x][y]=0
        visited[x][y]=True
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False

t=int(input())
for _ in range(t):
    result=0
    n,m,k=map(int, input().split())
    graph=[[0]*m for i in range(n)]
    visited=[[False]*m for i in range(n)]

    for _ in range(k):
        u,v=map(int, input().split())
        graph[u][v]=1

    for i in range(n):
        for j in range(m):
            if dfs(i,j)==True:
                result+=1
    print(result)

