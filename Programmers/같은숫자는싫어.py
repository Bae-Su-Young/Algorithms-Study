import sys
input=sys.stdin.readline()

def solution(arr):
    answer=[]
    idx=0
    find=arr[idx+1:].index(arr[idx])
    print(find)
    # while idx<=len(arr):
    #     find=arr[idx+1:].index(arr[idx])
    #     print(find)
    #     idx+=find
    return ['g']
    

def main():
   arr = [1, 1, 3, 3, 0, 1, 1] 
   answer=solution(arr)

   print(*answer)

if __name__=='__main__':
    main()
