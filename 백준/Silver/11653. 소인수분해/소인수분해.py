#입력
#N : 정수
N = int(input())

# 소인수 2부터 시작, N이 1이 될 때까지 반복
i = 2
while N > 1:
    if N%i == 0: 
        N = N//i 

    #출력 
    #N의 소인수 분해 한줄에 하나씩
        print(i)
   
    # 소인수로 안 나눠지는 경우 소인수를 1씩 늘린다. 
    else:
        i+=1