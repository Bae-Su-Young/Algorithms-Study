# 문제: A가 1인 모든 입력에 대해서, 꺼낼 사탕의 맛의 번호를 출력.
# A=2이면서 C<0일 때는 출력하지 않는다.
from bisect import bisect_left,bisect_right
import sys
input=sys.stdin.readline

n=int(input())
candy=[]
menu=[]#0:a 1:b 2:c
for _ in range(n):
    menu=list(map(int, input().split()))

    # a=1: 사탕을 빼는 경우
    if menu[0]==1:
        # b: 꺼낼 사탕의 순위를 의미
        candy.sort()
        print(candy[menu[1]-1])
        candy.pop(menu[1]-1)

    # a=2: 사탕을 넣는 경우
    elif menu[0]==2:    
        # b: 넣을 사탕의 맛
        # c 양수: 그러한 사탕의 갯수
        if menu[2]>0:
            for _ in range(menu[2]):
                candy.append(menu[1])
        # c 음수: 사탕을 빼는        
        elif menu[2]<=0:
            candy.pop(menu[1]-1)

