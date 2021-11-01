import sys
from collections import deque

def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    while queue:
        x,y=queue.popleft()
        for i in range(len(dx)):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=l or ny<0 or ny>=l:
                continue
            if chess[nx][ny]==0:
                chess[nx][ny]=chess[x][y]+1
                queue.append((nx,ny))
    return chess[dist_x][dist_y]

    
input=sys.stdin.readline

dx=[-2,-2,-1,-1,1,1,2,2]
dy=[1,-1,2,-2,2,-2,1,-1]

t=int(input())

for _ in range(t):
    l=int(input())
    chess=[[0]*l for _ in range(l)]
    curr_x,curr_y=map(int,input().split())
    dist_x,dist_y=map(int,input().split())
    if curr_x==dist_x and curr_y==dist_y:
        print(0)
    else:
        print(bfs(curr_x,curr_y))


