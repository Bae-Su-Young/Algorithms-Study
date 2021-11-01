#어떠한 수 N이 1이 될 때까지의 두 과정중 하나를 반복적으로 수행
# 1. N-1
# 2. N // K

# idea: 최대한 많이 나누기를 하는 것
# 맞아 떨어질 때마다 나누기를 하는 것

n,k=map(int, input().split())

result=0
while True:
    target=(n//k)*k # k로 나누어 떨어지는 수
    result+=(n-target)

    n=target

    if n<k:
        break

    result+=1
    n//k

result+=(n-1)
print(result)

