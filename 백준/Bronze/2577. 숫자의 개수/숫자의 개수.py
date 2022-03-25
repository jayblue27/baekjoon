# 세개의 자연수 
A = int(input())
B = int(input())
C = int(input())
res = str(A*B*C)


# 계산된 결과값 안에 0부터 9까지 숫자가 각각 몇 번 사용 됐는지 반환
for i in range(10):                    # i : 0~9 까지 반복    
    k = 0
    for j in range(len(res)):          # j : 숫자 자리                 
        if res[j] == str(i):           # j값이 계산값과 같으면 
            k+=1                       # count 증가
        else:                          # 그 외
            pass                       # pass
    print(k)                           # count 출력
