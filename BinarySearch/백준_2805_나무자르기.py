import sys
input=sys.stdin.readline

n,m=map(int,input().split())
namu=[]

namu=list(map(int,input().split()))

start=0
end=max(namu)

while start<=end:# start<end (x)
    mid=(start+end)//2
    sum=0
    for i in range(n):
        if namu[i]>mid:
            sum+=(namu[i]-mid)
    if sum<m:
        end=mid-13
        
    else:
        result=mid
        start=mid+1
        
  
print(result)      


    



