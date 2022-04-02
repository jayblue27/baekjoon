ans=[]

while True:
    # 입력
    lst = list(map(int, input().split()))
    lst = sorted(lst)
    
    # 입력 값 0 0 0 받으면 종료
    if lst[0] == 0 and lst[1] == 0 and lst[2] == 0:
        break   
    
    else:
        # 피타고라스 정리에 해당하면
        if lst[0]**2 + lst[1]**2 == lst[2]**2:
            ans.append('right')
        else:  
            ans.append('wrong')
    

for i in ans:
    print(i)          