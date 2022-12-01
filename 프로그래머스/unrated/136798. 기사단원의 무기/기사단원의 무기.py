'''
기사단 1번부터 number 까지 번호 지정 (<10만)

약수의 개수가 공격력인데
이웃나라와의 협약으로 정해진 공격력의 limit넘어가면
power로 지정
'''
# 1차시도 -> 시간 초과
# 약수 구하는 함수에서 시간을 조금 줄일필요 있겠다.
def counting_divisor(n):
    cnt = 0
    for i in range(1, int(n**(1/2)) + 1):
        if n%i == 0:
            cnt += 1
            if i!=n//i:
                cnt += 1
    return cnt

def solution(number, limit, power):    
    answer = 0
    for i in range(1, number+1):
        tmp = counting_divisor(i)
        # 만약 파워(약수의 개수)가 limit를 넘으면 power(지정 파워)를 더해준다.
        if tmp > limit:
            answer += power
        # 그 외에는 파워 (약수의 개수)를 더한다.
        else:
            answer += tmp
            
    return answer