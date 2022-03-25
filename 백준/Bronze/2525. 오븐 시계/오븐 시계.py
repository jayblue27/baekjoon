#시각
A, B = input().split(' ')
A = int(A)
B = int(B)

#소요시간
C = int(input())

# 소요시간 더하기
BC = B + C

# 소요시간 더했을때, 분이 60 안넘어가면
if BC < 60:
    print(A,BC)  # 그대로 출력

# 소요시간 더한 값이 60 넘어가면
else:    
    A = (A + (BC//60)) #60 나눈 몫만큼 시에 더함
    BC = BC % 60       #나머지는 분으로 
    
    if A < 24:         # 24시간 표기니까 24시 안넘어가면 그대로 출력
        print(A, BC)
    else:              # 24시 넘어가면 24사로 나눈 몫으로 출력
        A = A%24
        print(A, BC)
