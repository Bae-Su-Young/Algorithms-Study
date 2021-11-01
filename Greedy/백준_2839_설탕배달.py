#kg=int(input())
#result=0
#if (kg%8 >3) or (kg%8 >5):
#    print(-1)
#else:
#    if (kg//3>=5):
#        result+=(kg//5)
#        kg=kg%5
#        result+=(kg//3)
#    else:
#       result+=(kg//3)
#        kg=kg%3
#        result+=(kg//5)
#    print(result)

kg=int(input())
result=-1
if (kg%5==0):
    result=0
    result+=(kg//5)
else:
    result=0
    while(kg>0):
        kg-=3
        result+=1
        if kg%5==0:
            result+=(kg//5)
            break
        else:
            continue
    if(kg<0):
        result=-1

print(result)