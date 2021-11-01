from bisect import bisect_left,bisect_right
import sys

input=sys.stdin.readline

n,target=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()

result=bisect_right(arr,target)-bisect_left(arr,target)

if result!=0:
    print(result)
else:
    print(-1)
