from collections import deque
from collections import deque
import sys
input=sys.stdin.readline

def bfs(n):
    queue=deque()
    queue.append(n)
    while queue:
        curr=queue.popleft()
        if curr==k:
            print(distance[curr])
            return
        for next in (curr-1, curr+1,curr*2):
            if 0<=next<MAX and not distance[next]:
                distance[next]=distance[curr]+1
                queue.append

MAX=100001
n,k=map(int,input().split())
distance=[0]*MAX
bfs()


