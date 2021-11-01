n=int(input())
l=[]
for _ in range(n):
    x,y=map(int,input().split())
    l.append([x,y])

l.sort(key=lambda x:(x[0],x[1])) 

for i in l:
    print(i[0],i[1])