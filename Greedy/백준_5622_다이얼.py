#=======================
#2019년 9월 26일
a={2:['A','B','C'],3:['D','E','F'],4:['G','H','I'],5:['J','K','L'],6:['M','N','O'],7:['P','Q','R','S'],8:['T','U','V'],9:['W','X','Y','Z']}

str=input()
time=0
for s in str:
    for k,v in a.items():
        if s in v:
            time+=k+1
print(time)      
