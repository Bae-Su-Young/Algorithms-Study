import sys
from math import log2, ceil
input=sys.stdin.readline

MAX=1000000

def add(node, start, end, index, cnt):
    if start>index or index>end:
        return
    tree[node]+=cnt
    if start!=end:
        mid=(start+end)//2
        add(node*2,start,mid, index,cnt)
        add(node*2+1,mid+1,end, index,cnt)

def get(node,start,end,seq):
    if start==end: return start
    mid=(start+end)//2
    if tree[node*2]>=seq:
        return get(node*2,start,mid,seq)
    else:
        return get(node*2+1, mid+1,end,seq-tree[node*2])
height=ceil(log2(MAX))
size=2**(height+1)
tree=[0 for _ in range(size)]

for _ in range(int(input())):
    menu=list(map(int,input().split()))
    if menu[0]==1:
        #사탕 빼기
        index=get(1,0,MAX-1,menu[1])
        print(index)
        add(1,0,MAX-1,index,-1)
    else:
        #사탕 넣기
        #menu[1]=넣을 사탕 맛
        #menu[2]=넣는 갯수
        add(1,0,MAX-1,menu[1],menu[2])
