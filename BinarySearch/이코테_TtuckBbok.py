import sys
input=sys.stdin.readline

length=[]
n,m=map(int,input().split())

length=list(map(int, input().split()))

start=0
end=max(length)
result=0
while start<=end:
    mid=(start+end)//2
    sum=0
    for i in length:
        if i>mid: ## 아니면 - 음수 값이 생김
            sum+=i-mid
    if sum<m:
        end=mid-1
    else:
        result=mid
        start=mid+1

print(result)