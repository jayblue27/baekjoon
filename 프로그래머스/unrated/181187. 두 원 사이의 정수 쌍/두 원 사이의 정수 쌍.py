# dp로 푸는 문제인듯? 

# 반지름의 길이에 따른 점수개수 규칙 찾고
# r2 의 점개수 - r1의 점개수 + 4 로 추정

# 숫자가 너무 커지는데?
# def solution(r1, r2):
#     dp = [0] * (r2 +1)

#     # 점화식 찾기
#     dp[0] = 1
#     dp[1] = 5
#     for i in range(2, len(dp)):
#         if i%2 == 0:
#             dp[i] = dp[i-1] + ((dp[i-1] - dp[i-2]) + 4 )
#         else:
#             dp[i] = dp[i-1] + ((dp[i-1] - dp[i-2])*2)
            
#     return dp[r2] - dp[r1] + 4


import math

def solution(r1, r2):
    inner_dot_num = 0
    for x in range(1, r2 + 1):
        y_max = math.floor(math.sqrt(r2**2 - x**2))
        y_min = 0 if x >= r1 else math.ceil(math.sqrt(abs(r1**2 - x**2)))
        inner_dot_num += y_max - y_min + 1
    
    return inner_dot_num * 4
