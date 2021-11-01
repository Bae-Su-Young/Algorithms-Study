import sys
input=sys.stdin.readline
n,k=map(int, input().split())
info=[]
for _ in range(n):
    info.append(list(map(int,input().split())))

info.sort(key=lambda x:(x[1],x[2],x[3]),reverse=True)

rank=1
for i in range(len(info)):
    if k==info[i][0]:
        print(rank)
        break
    if info[i][1:]!=info[i+1][1:]:
        rank+=1
#100점============================================
import sys
input=sys.stdin.readline
n,k=map(int, input().split())
info=[]
for _ in range(n):
    info.append(list(map(int,input().split())))

info.sort(key=lambda x:(x[1],x[2],x[3]),reverse=True)

rank=1
for i in range(len(info)):
    if k==info[i][0]:
        idx=i

for i in range(n):
    if info[idx][1:]!=info[i][1:]:
        print(i+1)
        break
        
#===20점 =====================================
N, K = map(int,input().split())
cnt = []

for i in range(N):
    a = list(map(int,input().split()))
    cnt.append(a)

score = {}
for i in cnt:
    score[i[0]] = i[1]*3 + i[2]*2 + i[3]*1

score = sorted(list(score.items()),key = lambda x : x[1],reverse = True)

answer = [[score[0][0]]]
first = score[0][1]
for i in score[1:]:
    if first > i[1]:
        answer.append([i[0]])
        first = i[1]
    else:
        answer[-1].extend([i[0]])

for i in range(len(answer)):
    if K in answer[i]:
        print(i+1)
        break

