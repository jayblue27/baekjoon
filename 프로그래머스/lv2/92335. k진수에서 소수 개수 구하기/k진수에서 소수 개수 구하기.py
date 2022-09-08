'''
양의정수 n을 k진수로 바꿨을 때
아래 조건에 맞는 소수가 몇개인지 알아보기 
1) 0P0 - 소수 양쪽에 0이 있는 경우
2) P0 - 소수 오른쪽에만 0이 있는 경우
3) 0P - 소수 왼쪽에만 0이 있는 경우
4) P - 소수 양쪽에 아무것도 없는 경우
단, P는 0을 포함하지 않는 소수이다.

-> 0을 기준으로 split 하고 P위치의 숫자가 소수인지 판별한다.
소수일 경우 result += 1 
'''
# n을 k진수로 변환
def to_k_number(n, k):  
    ret = ""
    while n > 0:
        ret += str(n % k)
        n = n //  k
    return ''.join(reversed(ret))

def is_prime_num(k):
    if k == 2 or k == 3: return True  
    if k % 2 == 0 or k < 2: return False  
    for i in range(3, int(k ** 0.5) + 1, 2):
        if k % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    k_num = to_k_number(n, k) 
    # k_num을 0을 기준으로 분할하여 n을 가져옴
    for n in k_num.split('0'):
        if n == "": 
            continue
        if is_prime_num(int(n)):  # n이 소수인 경우 answer+=1
            answer += 1
    return answer
