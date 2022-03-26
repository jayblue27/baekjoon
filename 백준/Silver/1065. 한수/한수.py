#한수
#입력 - 1000보다 작거나 같은 자연수 N
N = int(input())
count = 0  # 카운트 변수 선언

for i in range(1, N+1): # 1에서 N까지 순환
    if i < 100:  # 100 미만일경우 전부 등차수열
        count = i   # 그 값을 반환 하면 됨
    elif i < 1000:        # 100이상 1000미만 일경우
        first = i//100        # 백자리 수
        second = (i - (i//100*100) ) //10  # 십자리 수
        third = i%10         # 일자리 수
        
        if first-second == second-third:     #첫째-둘째  둘째-셋째 비교해서 값이 같으면
            count += 1         # 등차수열
    else:   # 1000일때
        pass  #1000은 등차수열 아니니까 계산 안하고 넘김

print(count)
