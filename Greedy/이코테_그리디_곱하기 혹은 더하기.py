# 두 수중 하나라도 1이하의 수자가 있으면 더하고, 두 수가 모두 2이상인 경우 곱한다.

data=input()
result=int(data[0])

for i in range(1,len(data)):
    num=int(data[i])
    if num >=1 or result<=1:
        result+=num
    else:
        result*=num

print(result)