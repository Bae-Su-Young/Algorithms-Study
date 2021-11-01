from bisect import bisect_left,bisect_right
import sys
input=sys.stdin.readline

n=int(input())
card_list=list(map(int,input().split()))

m=int(input())
find_list=list(map(int,input().split()))

card_list.sort()
for i in range(len(find_list)):
    print(bisect_right(card_list,find_list[i])-bisect_left(card_list,find_list[i]))


#Counter libray
# from collections import Counter
# _ = input()
# N = input().split()
# _ = input()
# M = input().split()

# C = Counter(N)
# ans = []
# for i in M :
#     if i in C :
#         ans.append(C[i])
#     else :
#         ans.append(0)
# print(*ans)