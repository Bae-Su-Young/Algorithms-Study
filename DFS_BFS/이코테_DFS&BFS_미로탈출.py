from collections import deque

def bfs(x,y):
    queue=deque()
    queue.append((x,y))

    while queue:
        x,y=queue.popleft()
        print(x,y)
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx >= n    or ny<0 or ny>=m:
                continue
            if graph[nx][ny]==0:
                continue
            if graph[nx][ny]==1:
                graph[nx][ny]=graph[x][y]+1
                queue.append((nx,ny))
    return graph[n-1][m-1] #가장 좌하단이 목적지이므로 목적지 노드에 거리 값이 들어있음.

n,m=map(int, input().split())
graph=[list(map(int,input())) for _ in range(n)]

#이동 벡터
#상,하,좌,우
dx=[0,0,1,-1]
dy=[-1,1,0,0]

print(bfs(0,0))