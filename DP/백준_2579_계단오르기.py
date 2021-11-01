import sys
input=sys.stdin.readline

cnt=int(input())
score=[]
d=[0]*(cnt)
for _ in range(cnt):
    score.append(int(input()))

if cnt==1:
    print(score[1])
else:
    #print(*score)
    d[0]=score[0]
    d[1]=max(score[0]+score[1],score[1])
    d[2]=max(score[0]+score[2],score[1]+score[2])
    for i in range(3,cnt):
        #연속된 세개의 계다을 모두 밟아서는 안된다. 시작점은 포함 x
            # 마지막 계단 전의 계단을 밟은 경우
                # 마지막 계단의 전전 계단을 밟지 못한다
            # 마지막 계단 전의 계단을 밟지 않은 경우
        d[i]=max(d[i-2]+score[i],score[i-1]+d[i-3]+score[i])            
    print(d.pop())
        