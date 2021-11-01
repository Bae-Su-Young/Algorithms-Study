import sys
input=sys.stdin.readline

t=int(input())

for _ in range(t):
    n,m=map(int,input().split())
    d=[0]*m
    gold=[[0 for j in range(m)]for i in range(n)]
    data=list(map(int,input().split()))
    for k in range(n*m):
        gold[k//m][k-(m*(k//m))]=data[k]

    # ai=해당 열까지 이동시 얻는 최대 금의 크기
    # ai= a_i-1+max(gold[i])
    # 이동방향
    d[0]=max([l[0] for l in gold])
    for i in range(1,m):
        temp=[l[i] for l in gold]
        pre_temp=[ll[i-1] for ll in gold]
        max_index=pre_temp.index(max(pre_temp))   
        print(max_index)
        if max_index-1==0:
            d[i]=d[i-1]+max(temp[max_index],temp[(max_index+1)])
        elif max_index+1==n:
            d[i]=d[i-1]+max(temp[max_index],temp[(max_index-1)])
        else:
            d[i]=d[i-1]+max(temp[max_index],temp[(max_index-1)],temp[(max_index+1)])
        
    print(d[-1])
    

    


    


    

   