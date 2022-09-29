'''
n 연속한 자연수들로 표현하는 방법 return

n <= 10000 이하 -> 완전 제곱 가능할 듯 

'''
def solution(n):
    answer = 0
    for i in range(1,n+1):
        tmp = 0
        for j in range(i, n+1):
            tmp += j
            if tmp == n:
                answer += 1
                break
            elif tmp > n:
                break
        
    return answer