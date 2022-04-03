# 입력
# M이상, N이하의 자연수

M = int(input())
N = int(input())

# 수열(M이상, N이하) 생성
sliced_numbers = set(range(M,N+1)) 
# 소수 집합
prime_numbers = set()
# 소수가 아닌 수 집합
not_prime_numbers = set()


for num in sliced_numbers:
    # 1은 소수가 아님
    if num == 1:
        not_prime_numbers.add(num)
    
    # 그외 소수가 아닐 경우, 소수가 아닌 수의 집합에 추가
    else:
        for i in range(2, num):
            if num%i == 0:
                not_prime_numbers.add(num)
                break

# 소수 = M이상, N이하의 수열에서, 소수가 아닌 수를 제외한 나머지
prime_numbers = sliced_numbers - not_prime_numbers


# 출력
# 1. M이상 N이하 자연수 중 소수의 합
# 2. 상기 소수의 값중 최솟값
# 단, 소수가 없을경우 -1 출력

# 예외 처리
if len(prime_numbers) == 0:
    print(-1) 

#출력
else:
    print(sum(prime_numbers)) # 출력 1
    print(min(prime_numbers)) # 출력 2

# numpy 불러오니까 에러남