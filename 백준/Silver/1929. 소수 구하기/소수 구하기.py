# 백준 - 소수 구하기 
# https://www.acmicpc.net/problem/1929
#
# M 이상 N이하의 소수 모두 출력
# 원래 방식으로는 break 써도 시간초과 생긴다.

# 입력
# M이상 N 이하 (한줄에 입력), 소수가 하나 이상 있는 입력만 주어진다.
M, N = map(int, input().split())


# 소수 구하기
for num in range(M, N+1):
    # 1은 소수가 아님
    if num == 1:
        continue
    
    # 그외 
    else:
        # 제곱근 이상의 수는 생략 해줘야 시간초과 안뜸
        # 그리고 제곱근에 1을 더해줘야 해당수의 제곱근 까지 순회 가능함 
        #16 -> 4(16의 제곱근), 4까지 순회하고 싶으면 range 뒤에 5가 나와야 하기때문
        for i in range(2, int(num**0.5)+1):  
            if num%i == 0:
                break
        else:
            print(num)