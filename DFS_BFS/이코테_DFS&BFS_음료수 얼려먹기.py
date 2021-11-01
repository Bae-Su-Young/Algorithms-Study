#DFS: 상,하,좌,우로 붙어있는 경우 서로 연결
#connected component 찾기

def dfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    
    if graph[x][y]==0:
        graph[x][y]=1 # 방문처리
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)#상,하,좌,우로 연결된 노드를 다 방문하고 나서야
        print("True 반환: ",x,y) #true반환
        return True #
    ("False 반환",x,y) 
    return False #막힌 곳이므로 False 반환


n,m=map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int, input())))

result=0
for i in range(n):
    for j in range(m):
        if dfs(i,j)==True:
            print("result+=1: ",i,j)
            result+=1
    print()

print(result)

