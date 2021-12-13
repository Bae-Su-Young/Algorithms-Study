import math

def getXY(num):
    x=num//3
    y=num-(num//3)+1
    return [x,y]
    
def solution(numbers, hand):
    numbers=[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
    hand='right'

    pre_num=[0,0] # L, R
    dist_right=0
    dist_left=0
    answer = ''
    for i in range(len(numbers)):
        n=numbers[i]
        if n==1 or n==4 or n==7:
            answer+='L'
            pre_num[0]=n
        elif n==3 or n==6 or n==9:
            answer+='R'
            pre_num[1]=n
        else:
            pre_left=[]
            pre_right=[]
            num_XY=[]
      
            pre_left=getXY(pre_num[0])
            pre_right=getXY(pre_num[1])
            num_xy=getXY(n)
                                         
            #오른손 거리
            dist_right=math.hypot((num_xy[0]-pre_right[0],num_xy[1]-pre_right[1]))
                                  
            #왼손 거리
            dist_left=math.hypot((num_xy[0]-pre_left[0],num_xy[1]-pre_left[1]))
            
            # 두 거리 비교
            if dist_right==dist_left:
                if hand=='left': answer+='L'
                else: answer+='R'
            # 오른손 거리가 짧을 때
            elif dist_right<dist_left:
                 answer+="R"
                
            # 왼손 거리가 짧을 때
            else:
                answer+='L'
            
            
    return answer