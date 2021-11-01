import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline()

def dfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    if graph[x][y]==1:
        graph[x][y]=0
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
    
    for _ in range(k):
        u,v=map(int, input().split())
        graph[u][v]=1

    for i in range(n):
        for j in range(m):
            if dfs(i,j)==True:
                result+=1
    print(result)


#Run-time Error
# import sys
# sys.setrecursionlimit(10**6)
# def dfs(x,y):
#     if x<=-1 or x>=n or y<=-1 or y>=m:
#         return False
#     if graph[x][y]==1:
#         graph[x][y]=0
#         dfs(x-1,y)
#         dfs(x+1,y)
#         dfs(x,y-1)
#         dfs(x,y+1)
#         return True
#     return False

# t=int(input())

# for _ in range(t):
#     result=0
#     n,m,k=map(int, input().split())
#     graph=[[0]*m for i in range(n)]
    
#     for _ in range(k):
#         u,v=map(int, input().split())
#         graph[u][v]=1

#     for i in range(n):
#         for j in range(m):
#             if dfs(i,j)==True:
#                 result+=1
#     print(result)




