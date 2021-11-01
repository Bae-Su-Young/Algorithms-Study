n,k=map(int,input().split())
num=[i+1 for i in range(n)]
result=[]

index=0
while len(num)!=0:
    index+=k-1
    index%=len(num)
    result.append(num[index])
    num.pop(index)

print("<",end='')
print(", ".join(map(str,result)),end='')
# for i in range(len(result)):
#     if i !=n-1:
#         print(result[i],end=', ')
#     else:
#         print(result[i],end='')

print(">")

#k-1번째 요소를 빼서 다시 뒤에 넣어준 뒤, k-1번째까지 뺀 큐에서 pop을 하고 반복.....