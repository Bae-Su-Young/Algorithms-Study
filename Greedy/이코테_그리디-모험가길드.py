#오름차순 정렬 후
#공포도 하나씩 확인하며 '현재 그룹에 포함된 모함가의 수'>='현재 확인하고 있는 공포도'

n=int(input())
gongpo=list(map(int,input().split()))
gongpo.sort()

result=0 #총 그룹의 수
cnt=0 #모험가의 수

for i in gongpo:
    cnt+=1
    if cnt>=i:
        result+=1
        count=0
print(result)